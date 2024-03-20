from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render

from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic
#from bootstrap_modal_forms.mixins import PassRequestMixin
from .models import Book, Category, Client, Event, Salary, Service, Setting, User, Chat, DeleteRequest, Feedback
from django.contrib import messages
from django.db.models import Sum
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView, ListView
from .forms import BookForm, CategoryForm, ChatForm, ClientForm, EventForm, SalaryForm, ServiceForm, SettingForm, UserForm
from . import models
import operator
import itertools
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, logout
from django.contrib import auth, messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from datetime import datetime

from . utils import send_email_with_html_body


""""
import smtplib, email, ssl

import html 
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
"""



# email sending

def create_view(request, *args, **kwargs):
	"""This view help to create and account for testing sending mails."""
	cxt = {}
	if request.method == "POST":
		email = request.POST.get('email')
		subjet = request.POST.get('subjet')
		file = request.POST.get('file')
		message = request.POST.get('message')
		subjet=subjet
		file=file
		message=message
		template = 'email.html'
		context = {
			'date': datetime.today().date,
			'email': email,
			'subjet': subjet,
			'file': file,
			'message': message
		}

		receivers = [email]

		has_send = send_email_with_html_body(
			subjet=subjet,
			file=file,
			message=message,
			receivers=receivers,
			template=template,
			context=context
			)

		if has_send:
		    cxt =  {"msg":"mail envoyee avec success."} 
		else:
			cxt = {"msg":"email envoie echoue."}

	return render(request, 'compose_mail.html', cxt) 


"""
part2 = MIMEText(html, "html")
 
# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
message.attach(part2)
 
filename = "Mon fichier.pdf"  # In same directory as script
 
# Open PDF file in binary mode
with open(filename, "rb") as attachment:
	# Add file as application/octet-stream
	# Email client can usually download this automatically as attachment
	part = MIMEBase("application", "octet-stream")
	part.set_payload(attachment.read())
 
# Encode file in ASCII characters to send by email
encoders.encode_base64(part)
 
# Add header as key/value pair to attachment part
part.add_header(
	'Content-Disposition', 'attachment', filename="%s" % filename,
	)
 
# Add attachment to message and convert message to string
message.attach(part)
text = message.as_string()
 
# Log in to server using secure context and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("ssl0.ovh.net", 465, context=context) as server:
	server.login(sender_email, password)
	server.sendmail(sender_email, receiver_email, text)
	
"""



# Shared Views
def login_form(request):
	return render(request, 'bookstore/login.html')


def logoutView(request):
	logout(request)
	return redirect('home')


def loginView(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None and user.is_active:
			auth.login(request, user)
			if user.is_admin or user.is_superuser:
				return redirect('dashboard')
			else:
				return redirect('publisher')
		else:
			messages.info(request, "Invalid username or password")
			return redirect('home')



def lockView(request):
	if request.method == 'POST':
		password = request.POST['password']
		user = authenticate(request, password=password)
		if user is not None and user.is_active:
			auth.login(request, user)
			if user.is_admin or user.is_superuser:
				return redirect('dashboard')
			else:
				return redirect('publisher')
		else:
			messages.info(request, "Invalid password")
			return redirect('home')



"""

elif user.is_librarian:
				return redirect('librarian')

def register_form(request):
	#return render(request, 'bookstore/register.html')


def registerView(request):
	if request.method == 'POST':
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		password = make_password(password)

		a = User(username=username, email=email, password=password)
		a.save()
		messages.success(request, 'Account was created successfully')
		return redirect('home')
	else:
		messages.error(request, 'Registration fail, try again later')
		return redirect('regform')
"""


















			


# Publisher views

@login_required
def settings(request):
	return render(request, 'publisher/settings.html')


@login_required
def profilep(request):
	return render(request, 'publisher/profile.html')


@login_required
def calendarp(request):
	return render(request, 'publisher/calendar.html')



@login_required
def logout(request):
	return render(request, 'bookstore/login.html')


@login_required
def lockp(request):
	return render(request, 'bookstore/lock_screen.html')



@login_required
def publisher(request):
	return render(request, 'publisher/home.html')


@login_required
def uabook_form(request):
	return render(request, 'publisher/add_book.html')


@login_required
def request_form(request):
	return render(request, 'publisher/delete_request.html')


@login_required
def feedback_form(request):
	return render(request, 'publisher/send_feedback.html')

@login_required
def about(request):
	return render(request, 'publisher/about.html')	


@login_required
def usearch(request):
	query = request.GET['query']
	print(type(query))


	#data = query.split()
	data = query
	print(len(data))
	if( len(data) == 0):
		return redirect('publisher')
	else:
				a = data

				# Searching for It
				qs5 =models.Ranger.objects.filter(id__iexact=a).distinct()
				qs6 =models.Ranger.objects.filter(id__exact=a).distinct()

				qs7 =models.Ranger.objects.all().filter(id__contains=a)
				qs8 =models.Ranger.objects.select_related().filter(id__contains=a).distinct()
				qs9 =models.Ranger.objects.filter(id__startswith=a).distinct()
				qs10 =models.Ranger.objects.filter(id__endswith=a).distinct()
				qs11 =models.Ranger.objects.filter(id__istartswith=a).distinct()
				qs12 =models.Ranger.objects.all().filter(id__icontains=a)
				qs13 =models.Ranger.objects.filter(id__iendswith=a).distinct()




				files = itertools.chain(qs5, qs6, qs7, qs8, qs9, qs10, qs11, qs12, qs13)

				res = []
				for i in files:
					if i not in res:
						res.append(i)


				# word variable will be shown in html when user click on search button
				word="Searched Result :"
				print("Result")

				print(res)
				files = res




				page = request.GET.get('page', 1)
				paginator = Paginator(files, 10)
				try:
					files = paginator.page(page)
				except PageNotAnInteger:
					files = paginator.page(1)
				except EmptyPage:
					files = paginator.page(paginator.num_pages)
   


				if files:
					return render(request,'publisher/result.html',{'files':files,'word':word})
				return render(request,'publisher/result.html',{'files':files,'word':word})



@login_required

def create_clientp_form(request):

	return render(request, 'publisher/add_client.html')


class ADeleteClientp(SuccessMessageMixin, DeleteView):
	model = Client
	template_name='publisher/confirm_delete6.html'
	success_url = reverse_lazy('alclient')
	success_message = "Data successfully deleted"


class AEditClientp(SuccessMessageMixin, UpdateView): 
	model = Client
	form_class = ClientForm
	template_name = 'publisher/edit_client.html'
	success_url = reverse_lazy('alclient')
	success_message = "Data successfully updated"


class ListClientpView(generic.ListView):
	model = Client
	template_name = 'publisher/list_clients.html'
	context_object_name = 'clients'
	paginate_by = 6

	def get_queryset(self):
		return Client.objects.order_by('-id')


def create_clientp(request):
	if request.method == 'POST':
		firt_name = request.POST['firt_name']
		last_name = request.POST['last_name']
		society = request.POST['society']
		email = request.POST['email']
		address = request.POST['address']
		contact = request.POST['contact']
		date = request.POST['date']
		description = request.POST['description']

		a = Client(firt_name=firt_name, last_name=last_name, society=society, email=email, 
			 address=address, contact=contact, date=date, description=description)
		a.save()
		messages.success(request, 'Client was Created successfully')
		return redirect('alclient')
	else:
		messages.error(request, 'Client was not Created successfully')
		return redirect('create_client_form')



class ALViewClientp(DetailView):
	model = Client
	template_name='publisher/client_detail.html'


class ListPayepView(generic.ListView):
	model = Salary
	template_name = 'publisher/payements.html'
	context_object_name = 'payement'
	paginate_by = 4

	def get_queryset(self):
		return Salary.objects.order_by('-id')


class ListSettingpView(generic.ListView):
	model = Setting
	template_name = 'publisher/settings.html'
	context_object_name = 'alsetting'
	paginate_by = 6

	def get_queryset(self):
		return Setting.objects.all()



@login_required
def delete_request(request):
	if request.method == 'POST':
		book_id = request.POST['delete_request']
		current_user = request.user
		user_id = current_user.id
		username = current_user.username
		user_request = username + "  want book with id  " + book_id + " to be deleted"

		a = DeleteRequest(delete_request=user_request)
		a.save()
		messages.success(request, 'Request was sent')
		return redirect('request_form')
	else:
		messages.error(request, 'Request was not sent')
		return redirect('request_form')



@login_required
def send_feedback(request):
	if request.method == 'POST':
		feedback = request.POST['feedback']
		current_user = request.user
		user_id = current_user.id
		username = current_user.username
		feedback = username + " " + " says " + feedback

		a = Feedback(feedback=feedback)
		a.save()
		messages.success(request, 'Feedback was sent')
		return redirect('feedback_form')
	else:
		messages.error(request, 'Feedback was not sent')
		return redirect('feedback_form')



def publisher(request):
	book = Ranger.objects.all().count()
	user = User.objects.all().count()
	chat = Chat.objects.all().count()
	client = Client.objects.all().count()
	earnings = Salary.objects.all().count()
	feedback = Feedback.objects.all().count()

	context = {'book':book, 'user':user, 'chat':chat, 'client':client, 'earnings':earnings, 'feedback':feedback}

	return render(request, 'publisher/home.html', context)



class UBookListView(LoginRequiredMixin,ListView):
	model = Book
	template_name = 'publisher/book_list.html'
	context_object_name = 'books'
	paginate_by = 2

	def get_queryset(self):
		return Book.objects.order_by('-id')

@login_required
def uabook(request):
	if request.method == 'POST':
		title = request.POST['title']
		category = request.POST['category']
		date = request.POST['date']
		desc = request.POST['desc']
		pdf = request.FILES['pdf']
		current_user = request.user
		user_id = current_user.id
		username = current_user.username
		

		a = Ranger(title=title, date=date, category=category, 
			desc=desc, pdf=pdf, uploaded_by=username, user_id=user_id)
		a.save()
		messages.success(request, 'Book was uploaded successfully')
		return redirect('publisher')
	else:
		messages.error(request, 'Book was not uploaded successfully')
		return redirect('uabook_form')	



class UCreateChat(LoginRequiredMixin, CreateView):
	form_class = ChatForm
	model = Chat
	template_name = 'publisher/chat_form.html'
	success_url = reverse_lazy('ulchat')


	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.user = self.request.user
		self.object.save()
		return super().form_valid(form)


class UListChat(LoginRequiredMixin, ListView):
	model = Chat
	template_name = 'publisher/chat_list.html'

	def get_queryset(self):
		return Chat.objects.filter(posted_at__lt=timezone.now()).order_by('posted_at')






























"""
# Librarian views
def librarian(request):
	book = Ranger.objects.all().count()
	user = User.objects.all().count()
	chat = Chat.objects.all().count()

	context = {'book':book, 'user':user, 'chat':chat}

	return render(request, 'librarian/home.html', context)


@login_required
def labook_form(request):
	return render(request, 'librarian/add_book.html')


@login_required
def labook(request):
	if request.method == 'POST':
		title = request.POST['title']
		author = request.POST['author']
		year = request.POST['year']
		publisher = request.POST['publisher']
		desc = request.POST['desc']
		cover = request.FILES['cover']
		pdf = request.FILES['pdf']
		current_user = request.user
		user_id = current_user.id
		username = current_user.username

		a = Ranger(title=title, author=author, year=year, publisher=publisher, 
			desc=desc, cover=cover, pdf=pdf, uploaded_by=username, user_id=user_id)
		a.save()
		messages.success(request, 'Book was uploaded successfully')
		return redirect('llbook')
	else:
		messages.error(request, 'Book was not uploaded successfully')
		return redirect('llbook')



class LRangerListView(LoginRequiredMixin,ListView):
	model = Ranger
	template_name = 'librarian/book_list.html'
	context_object_name = 'books'
	paginate_by = 3

	def get_queryset(self):
		return Ranger.objects.order_by('-id')


class LManageRanger(LoginRequiredMixin,ListView):
	model = Ranger
	template_name = 'librarian/manage_books.html'
	context_object_name = 'books'
	paginate_by = 3

	def get_queryset(self):
		return Ranger.objects.order_by('-id')


class LDeleteRequest(LoginRequiredMixin,ListView):
	model = DeleteRequest
	template_name = 'librarian/delete_request.html'
	context_object_name = 'feedbacks'
	paginate_by = 3

	def get_queryset(self):
		return DeleteRequest.objects.order_by('-id')


class LViewRanger(LoginRequiredMixin,DetailView):
	model = Ranger
	template_name = 'librarian/book_detail.html'

	
class LEditView(LoginRequiredMixin,UpdateView):
	model = Ranger
	form_class = RangerForm
	template_name = 'librarian/edit_book.html'
	success_url = reverse_lazy('lmbook')
	success_message = 'Data was updated successfully'


class LDeleteView(LoginRequiredMixin,DeleteView):
	model = Ranger
	template_name = 'librarian/confirm_delete.html'
	success_url = reverse_lazy('lmbook')
	success_message = 'Data was deleted successfully'


class LDeleteRanger(LoginRequiredMixin,DeleteView):
	model = Ranger
	template_name = 'librarian/confirm_delete2.html'
	success_url = reverse_lazy('librarian')
	success_message = 'Data was dele successfully'



@login_required
def lsearch(request):
	query = request.GET['query']
	print(type(query))


	#data = query.split()
	data = query
	print(len(data))
	if( len(data) == 0):
		return redirect('publisher')
	else:
				a = data

				# Searching for It
				qs5 =models.Ranger.objects.filter(id__iexact=a).distinct()
				qs6 =models.Ranger.objects.filter(id__exact=a).distinct()

				qs7 =models.Ranger.objects.all().filter(id__contains=a)
				qs8 =models.Ranger.objects.select_related().filter(id__contains=a).distinct()
				qs9 =models.Ranger.objects.filter(id__startswith=a).distinct()
				qs10 =models.Ranger.objects.filter(id__endswith=a).distinct()
				qs11 =models.Ranger.objects.filter(id__istartswith=a).distinct()
				qs12 =models.Ranger.objects.all().filter(id__icontains=a)
				qs13 =models.Ranger.objects.filter(id__iendswith=a).distinct()




				files = itertools.chain(qs5, qs6, qs7, qs8, qs9, qs10, qs11, qs12, qs13)

				res = []
				for i in files:
					if i not in res:
						res.append(i)


				# word variable will be shown in html when user click on search button
				word="Searched Result :"
				print("Result")

				print(res)
				files = res




				page = request.GET.get('page', 1)
				paginator = Paginator(files, 10)
				try:
					files = paginator.page(page)
				except PageNotAnInteger:
					files = paginator.page(1)
				except EmptyPage:
					files = paginator.page(paginator.num_pages)
   


				if files:
					return render(request,'librarian/result.html',{'files':files,'word':word})
				return render(request,'librarian/result.html',{'files':files,'word':word})


class LCreateChat(LoginRequiredMixin, CreateView):
	form_class = ChatForm
	model = Chat
	template_name = 'librarian/chat_form.html'
	success_url = reverse_lazy('llchat')


	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.user = self.request.user
		self.object.save()
		return super().form_valid(form)



		file_path = 'path/path/file.docx'
with open(file_path,'rb') as doc:
   response = HttpResponse(doc.read(), content_type='application/ms-word')
   # response = HttpResponse(template_output)
   response['Content-Disposition'] = 'attachment;filename=name.docx'
   return response




class LListChat(LoginRequiredMixin, ListView):
	model = Chat
	template_name = 'librarian/chat_list.html'

	def get_queryset(self):
		return Chat.objects.filter(posted_at__lt=timezone.now()).order_by('posted_at')
"""













# Admin views

@login_required
def dashboard(request):
	book = Book.objects.all().count()
	user = User.objects.all().count()
	chat = Chat.objects.all().count()
	client = Client.objects.all().count()
	earnings = Salary.objects.all().count()
	feedback = Feedback.objects.all().count()

	context = {'book':book, 'user':user, 'chat':chat, 'client':client, 'earnings':earnings, 'feedback':feedback}
	return render(request, 'dashboard/home.html', context)


@login_required
def logout(request):
	return render(request, 'bookstore/login.html')


@login_required
def lock(request):
	return render(request, 'bookstore/lock_screen.html')


@login_required
def settings(request):
	return render(request, 'dashboard/settings.html')


@login_required
def profile(request):
	return render(request, 'dashboard/profile.html')


@login_required
def calendar(request):
	return render(request, 'dashboard/calendar.html')


# mail views
@login_required 
def compose(request):
	return render(request, 'emails/compose_mail.html')


@login_required
def inbox(request):
	return render(request, 'emails/inbox.html')


@login_required
def mailview(request):
	return render(request, 'emails/mail_view.html')


@login_required
def create_setting_form(request):
	return render(request, 'dashboard/edit_settings.html')



def create_setting(request):
	if request.method == 'POST':
		cname = request.POST['cname']
		pname = request.POST['pname']
		address = request.POST['address']
		country = request.POST['country']
		city = request.POST['city']
		postal = request.POST['postal']
		email = request.POST['email']
		number1 = request.POST['number1']
		number2 = request.POST['number2']
		number3 = request.POST['number3']
		website = request.POST['website']

		a = Setting(cname=cname, pname=pname, address=address, country=country, city=city, postal=postal, email=email, 
			 number1=number1, number2=number2, number3=number3, website=website)
		a.save()
		messages.success(request, 'Settings was Updated successfully')
		return redirect('alsetting')
	else:
		messages.error(request, 'Settings was not Updated successfully')
		return redirect('create_setting_form')



class ListSettingView(generic.ListView):
	model = Setting
	template_name = 'dashboard/settings.html'
	context_object_name = 'alsetting'
	paginate_by = 6

	def get_queryset(self):
		return Setting.objects.all()




def create_salary_form(request):

	return render(request, 'dashboard/add_salary.html')


class ADeleteSalary(SuccessMessageMixin, DeleteView):
	model = Salary
	template_name='dashboard/confirm_delete7.html'
	success_url = reverse_lazy('alsalary')
	success_message = "Data successfully deleted"


class AEditSalary(SuccessMessageMixin, UpdateView): 
	model = Salary
	form_class = SalaryForm
	template_name = 'dashboard/edit_salary.html'
	success_url = reverse_lazy('alsalary')
	success_message = "Data successfully updated"

class ListSalaryView(generic.ListView):
	model = Salary
	template_name = 'dashboard/list_salary.html'
	context_object_name = 'salary'
	paginate_by = 7

	def get_queryset(self):
		return Salary.objects.order_by('-id')



def create_salary(request):
	if request.method == 'POST':
		amount = request.POST['amount']
		date = request.POST['date']

		a = Salary(amount=amount, date=date)
		a.save()
		messages.success(request, 'Salary was Updated successfully')
		return redirect('alsalary')
	else:
		messages.error(request, 'Salary was not Updated successfully')
		return redirect('create_salary_form')


class ALViewSalary(DetailView):
	model = Salary
	template_name='dashboard/salary_detail.html'


class ListPayeView(generic.ListView):
	model = Salary
	template_name = 'dashboard/payements.html'
	context_object_name = 'payement'
	paginate_by = 4

	def get_queryset(self):
		return Salary.objects.order_by('-id')



def create_user_form(request):
	choice = ['1', '0', 'Publisher', 'Admin']
	choice = {'choice': choice}

	return render(request, 'dashboard/add_user.html', choice)


class ADeleteUser(SuccessMessageMixin, DeleteView):
	model = User
	template_name='dashboard/confirm_delete3.html'
	success_url = reverse_lazy('aluser')
	success_message = "Data successfully deleted"


class AEditUser(SuccessMessageMixin, UpdateView): 
	model = User
	form_class = UserForm
	template_name = 'dashboard/edit_user.html'
	success_url = reverse_lazy('aluser')
	success_message = "Data successfully updated"

class ListUserView(generic.ListView):
	model = User
	template_name = 'dashboard/list_users.html'
	context_object_name = 'users'
	paginate_by = 4

	def get_queryset(self):
		return User.objects.order_by('-id')


def create_user(request):
	choice = ['1', '0', 'Publisher', 'Admin']
	choice = {'choice': choice}
	if request.method == 'POST':
			first_name=request.POST['first_name']
			last_name=request.POST['last_name']
			username=request.POST['username']
			userType=request.POST['userType']
			email=request.POST['email']
			password=request.POST['password']
			password = make_password(password)
			print("User Type")
			print(userType)
			if userType == "Publisher":
				a = User(first_name=first_name, last_name=last_name, username=username, email=email, password=password, is_publisher=True)
				a.save()
				messages.success(request, 'Member was created successfully!')
				return redirect('aluser')
			elif userType == "Admin":
				a = User(first_name=first_name, last_name=last_name, username=username, email=email, password=password, is_admin=True)
				a.save()
				messages.success(request, 'Member was created successfully!')
				return redirect('aluser')
			else:
				messages.success(request, 'Member was not created')
				return redirect('create_user_form')   
	else:
		return redirect('create_user_form')


"""
			elif userType == "Librarian":
				a = User(first_name=first_name, last_name=last_name, username=username, email=email, password=password, is_librarian=True)
				a.save()
				messages.success(request, 'Member was created successfully!')
				return redirect('aluser')
			""" 


class ALViewUser(DetailView):
	model = User
	template_name='dashboard/user_detail.html'


@login_required
def create_service_form(request):

	return render(request, 'dashboard/add_service.html')


class ADeleteService(SuccessMessageMixin, DeleteView):
	model = Service
	template_name='dashboard/confirm_delete5.html'
	success_url = reverse_lazy('alservice')
	success_message = "Data successfully deleted"



class AEditService(SuccessMessageMixin, UpdateView): 
	model = Service
	form_class = ServiceForm
	template_name = 'dashboard/edit_service.html'
	success_url = reverse_lazy('alservice')
	success_message = "Data successfully updated"


class ListServiceView(generic.ListView):
	model = Service
	template_name = 'dashboard/list_services.html'
	context_object_name = 'services'
	paginate_by = 5

	def get_queryset(self):
		return Service.objects.order_by('-id')



def create_service(request):
	if request.method == 'POST':
		name = request.POST['name']
		prix = request.POST['prix']
		description = request.POST['description']

		a = Service(name=name, prix=prix, description=description)
		a.save()
		messages.success(request, 'Service was created successfully')
		return redirect('alservice')
	else:
		messages.error(request, 'Service was not created successfully')
		return redirect('create_service_form')



class ALViewService(DetailView):
	model = Service
	template_name='dashboard/service_detail.html'


"""
def testing(request):
  mydata = Category.objects.values_list('cname')
  template = loader.get_template('template.html')
  context = {
    'mycategories': mydata,
  }
  return HttpResponse(template.render(context, request))
"""

def create_category_form(request):

	return render(request, 'dashboard/add_category.html')


class ADeleteCategory(SuccessMessageMixin, DeleteView):
	model = Category
	template_name='dashboard/confirm_delete4.html'
	success_url = reverse_lazy('alcategory')
	success_message = "Data successfully deleted"


class AEditCategory(SuccessMessageMixin, UpdateView): 
	model = Category
	form_class = CategoryForm
	template_name = 'dashboard/edit_category.html'
	success_url = reverse_lazy('alcategory')
	success_message = "Data successfully updated"


class ListCategoryView(generic.ListView):
	model = Category
	template_name = 'dashboard/list_categories.html'
	context_object_name = 'categories'
	paginate_by = 4

	def get_queryset(self):
		return Category.objects.order_by('-id')


def create_category(request):
	if request.method == 'POST':
		cname = request.POST['cname']

		a = Category(cname=cname)
		a.save()
		messages.success(request, 'Category was Created successfully')
		return redirect('alcategory')
	else:
		messages.error(request, 'Category was not Created successfully')
		return redirect('create_category_form')



class ALViewCategory(DetailView):
	model = Category
	template_name='dashboard/category_detail.html'






def create_client_form(request):

	return render(request, 'dashboard/add_client.html')


class ADeleteClient(SuccessMessageMixin, DeleteView):
	model = Client
	template_name='dashboard/confirm_delete6.html'
	success_url = reverse_lazy('alclient')
	success_message = "Data successfully deleted"


class AEditClient(SuccessMessageMixin, UpdateView): 
	model = Client
	form_class = ClientForm
	template_name = 'dashboard/edit_client.html'
	success_url = reverse_lazy('alclient')
	success_message = "Data successfully updated"

class ListClientView(generic.ListView):
	model = Client
	template_name = 'dashboard/list_clients.html'
	context_object_name = 'clients'
	paginate_by = 6

	def get_queryset(self):
		return Client.objects.order_by('-id')


def create_client(request):
	if request.method == 'POST':
		firt_name = request.POST['firt_name']
		last_name = request.POST['last_name']
		society = request.POST['society']
		email = request.POST['email']
		address = request.POST['address']
		contact = request.POST['contact']
		date = request.POST['date']
		description = request.POST['description']

		a = Client(firt_name=firt_name, last_name=last_name, society=society, email=email, 
			 address=address, contact=contact, date=date, description=description)
		a.save()
		messages.success(request, 'Client was Created successfully')
		return redirect('alclient')
	else:
		messages.error(request, 'Client was not Created successfully')
		return redirect('create_client_form')



class ALViewClient(DetailView):
	model = Client
	template_name='dashboard/client_detail.html'




def create_event_form(request):
	choice = ['1', '0', 'Danger', 'Success', 'Info', 'Primary', 'Warning']
	choice = {'choice': choice}

	return render(request, 'dashboard/add_event.html', choice)


class ADeleteEvent(SuccessMessageMixin, DeleteView):
	model = Event
	#template_name='dashboard/confirm_delete8.html'
	success_url = reverse_lazy('adevent')
	success_message = "Data successfully deleted"


class AEditEvent(SuccessMessageMixin, UpdateView): 
	model = Event
	form_class = EventForm
	#template_name = 'dashboard/edit_event.html'
	success_url = reverse_lazy('aeevent')
	success_message = "Data successfully updated"


class ListEventView(generic.ListView):
	model = Event
	#template_name = 'dashboard/list_events.html'
	context_object_name = 'events'
	paginate_by = 4

	def get_queryset(self):
		return Event.objects.order_by('-id')



def create_event(request):
	choice = ['1', '0', 'Danger', 'Success', 'Info', 'Primary', 'Warning']
	choice = {'choice': choice}
	if request.method == 'POST':
			name=request.POST['name']
			date=request.POST['date']
			eventType=request.POST['eventType']

			print("Event Type")
			print(eventType)
			if eventType == "Danger":
				a = Event(name=name, date=date, is_danger=True)
				a.save()
				messages.success(request, 'Event was created successfully!')
				return redirect('alevent')
			elif eventType == "Success":
				a = Event(name=name, date=date, is_success=True)
				a.save()
				messages.success(request, 'Event was created successfully!')
				return redirect('alevent')
			elif eventType == "Info":
				a = Event(name=name, date=date, is_info=True)
				a.save()
				messages.success(request, 'Event was created successfully!')
				return redirect('alevent')
			elif eventType == "Primary":
				a = Event(name=name, date=date, is_primary=True)
				a.save()	
				messages.success(request, 'Event was created successfully!')
				return redirect('alevent')
			elif eventType == "Danger":
				a = Event(name=name, date=date, is_danger=True)
				a.save()	
				messages.success(request, 'Event was created successfully!')
				return redirect('alevent')     
			else:
				messages.success(request, 'Event was not created')
				return redirect('create_event_form')
	else:
		return redirect('create_event_form')
		

		
class ALViewEvent(DetailView):
	model = Event
	#template_name='dashboard/event_detail.html'


"""
def create_mail(request):
	if request.method == 'POST':
		email = request.POST['email']
		subject = request.POST['subject']
		file = request.POST['file']
		message = request.POST['message']

		a = Ranger(cname=cname)
		a.save()
		messages.success(request, 'Category was Created successfully')
		return redirect('alcategory')
	else:
		messages.error(request, 'Category was not Created successfully')
		return redirect('create_category_form')
"""



class ACreateChat(LoginRequiredMixin, CreateView):
	form_class = ChatForm
	model = Chat
	template_name = 'dashboard/chat_form.html'
	success_url = reverse_lazy('alchat')


	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.user = self.request.user
		self.object.save()
		return super().form_valid(form)




class AListChat(LoginRequiredMixin, ListView):
	model = Chat
	template_name = 'dashboard/chat_list.html'

	def get_queryset(self):
		return Chat.objects.filter(posted_at__lt=timezone.now()).order_by('posted_at')


@login_required
def aabook_form(request):
	return render(request, 'dashboard/add_book.html')


@login_required
def aabook(request):
	if request.method == 'POST':
		title = request.POST['title']
		category = request.POST['category']
		date = request.POST['date']
		desc = request.POST['desc']
		pdf = request.FILES['pdf']
		current_user = request.user
		user_id = current_user.id
		username = current_user.username
		

		a = Book(title=title, date=date, category=category, 
			desc=desc, pdf=pdf, uploaded_by=username, user_id=user_id)
		a.save()
		messages.success(request, 'Book was uploaded successfully')
		return redirect('albook')
	else:
		messages.error(request, 'Book was not uploaded successfully')
		return redirect('aabook_form')
		


class ABookListView(LoginRequiredMixin,ListView):
	model = Book
	template_name = 'dashboard/book_list.html'
	context_object_name = 'books'
	paginate_by = 3

	def get_queryset(self):
		return Book.objects.order_by('-id')




class AManageBook(LoginRequiredMixin,ListView):
	model = Book
	template_name = 'dashboard/manage_books.html'
	context_object_name = 'books'
	paginate_by = 3

	def get_queryset(self):
		return Book.objects.order_by('-id')




class ADeleteBook(LoginRequiredMixin,DeleteView):
	model = Book
	template_name = 'dashboard/confirm_delete2.html'
	success_url = reverse_lazy('ambook')
	success_message = 'Data was dele successfully'


class ADeleteBook(LoginRequiredMixin,DeleteView):
	model = Book
	template_name = 'dashboard/confirm_delete.html'
	success_url = reverse_lazy('dashboard')
	success_message = 'Data was delete successfully'


class AViewBook(LoginRequiredMixin,DetailView):
	model = Book
	template_name = 'dashboard/book_detail.html'




class AEditView(LoginRequiredMixin,UpdateView):
	model = Book
	form_class = BookForm
	template_name = 'dashboard/edit_book.html'
	success_url = reverse_lazy('ambook')
	success_message = 'Data was updated successfully'




class ADeleteRequest(LoginRequiredMixin,ListView):
	model = DeleteRequest
	template_name = 'dashboard/delete_request.html'
	context_object_name = 'feedbacks'
	paginate_by = 3

	def get_queryset(self):
		return DeleteRequest.objects.order_by('-id')



class AFeedback(LoginRequiredMixin,ListView):
	model = Feedback
	template_name = 'dashboard/feedback.html'
	context_object_name = 'feedbacks'
	paginate_by = 3

	def get_queryset(self):
		return Feedback.objects.order_by('-id')



@login_required
def asearch(request):
	query = request.GET['query']
	print(type(query))


	#data = query.split()
	data = query
	print(len(data))
	if( len(data) == 0):
		return redirect('dashborad')
	else:
				a = data

				# Searching for It
				qs5 =models.Ranger.objects.filter(id__iexact=a).distinct()
				qs6 =models.Ranger.objects.filter(id__exact=a).distinct()

				qs7 =models.Ranger.objects.all().filter(id__contains=a)
				qs8 =models.Ranger.objects.select_related().filter(id__contains=a).distinct()
				qs9 =models.Ranger.objects.filter(id__startswith=a).distinct()
				qs10 =models.Ranger.objects.filter(id__endswith=a).distinct()
				qs11 =models.Ranger.objects.filter(id__istartswith=a).distinct()
				qs12 =models.Ranger.objects.all().filter(id__icontains=a)
				qs13 =models.Ranger.objects.filter(id__iendswith=a).distinct()




				files = itertools.chain(qs5, qs6, qs7, qs8, qs9, qs10, qs11, qs12, qs13)

				res = []
				for i in files:
					if i not in res:
						res.append(i)


				# word variable will be shown in html when user click on search button
				word="Searched Result :"
				print("Result")

				print(res)
				files = res




				page = request.GET.get('page', 1)
				paginator = Paginator(files, 10)
				try:
					files = paginator.page(page)
				except PageNotAnInteger:
					files = paginator.page(1)
				except EmptyPage:
					files = paginator.page(paginator.num_pages)
   


				if files:
					return render(request,'dashboard/result.html',{'files':files,'word':word})
				return render(request,'dashboard/result.html',{'files':files,'word':word})


















