from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.urls import reverse




#User = get_user_model()


class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_publisher = models.BooleanField(default=False)
    #is_librarian = models.BooleanField(default=False)


    class Meta:
        swappable = 'AUTH_USER_MODEL'


class Category(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self): 
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=True, null=False)
    date = models.DateField(null=True, blank=True)
    desc = models.CharField(max_length=1000)
    uploaded_by = models.CharField(max_length=100, null=True, blank=True)
    user_id = models.CharField(max_length=100, null=True, blank=True)
    pdf = models.FileField(upload_to='bookapp/pdfs/')

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        super().delete(*args, **kwargs)        


class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    posted_at = models.DateTimeField(auto_now=True, null=True)


    def __str__(self):
        return str(self.message)


class Mail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(null=True, blank=True)
    subject = models.CharField(max_length=200, null=True, blank=True)
    file = models.FileField(upload_to='bookapp/pdfs/')
    message = models.TextField()
    posted_at = models.DateTimeField(auto_now=True, null=True)


    def __str__(self):
        return str(self.email) 



class DeleteRequest(models.Model):
    delete_request = models.CharField(max_length=100, null=True, blank=True)


    def __str__(self):
        return self.delete_request


class Feedback(models.Model):
    feedback = models.CharField(max_length=100, null=True, blank=True)


    def __str__(self):
        return self.feedback


class Service(models.Model):
    name = models.CharField(max_length=100)
    prix = models.PositiveIntegerField()
    description = models.CharField(max_length=1000)


    def __str__(self) : 
        return self.name
    


class Client(models.Model):
    firt_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    society = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    contact = models.BigIntegerField(null=True, blank=True)
    Service = models.ForeignKey(Service, on_delete=models.CASCADE, default=True, null=False)
    date = models.DateTimeField(null=True, blank=True)
    description = models.CharField(max_length=250, null=True, blank=True)


    def __str__(self) : 
        return self.firt_name




class Salary(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE, default=True, null=False)
    amount = models.PositiveIntegerField(null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)


    def __str__(self) : 
        return self.User



class Setting(models.Model):
    cname = models.CharField(max_length=50, null=True, blank=True)
    pname = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    postal = models.IntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    number1 = models.BigIntegerField(null=True, blank=True)
    number2 = models.BigIntegerField(null=True, blank=True)
    number3 = models.BigIntegerField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)


    def __str__(self) : 
        return self.cname



class Event(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    is_Danger = models.BooleanField(default=False)
    is_Success = models.BooleanField(default=False)
    is_Info = models.BooleanField(default=False)
    is_Primary = models.BooleanField(default=False)
    is_Warning = models.BooleanField(default=False)
    date = models.DateTimeField(null=True, blank=True)


    def __str__(self) : 
        return self.name


"""
 # Librarian URL's
 path('librarian/', views.librarian, name='librarian'),
 path('labook_form/', views.labook_form, name='labook_form'),
 path('labook/', views.labook, name='labook'),
 path('llbook/', views.LRangerListView.as_view(), name='llbook'),
 path('ldrequest/', views.LDeleteRequest.as_view(), name='ldrequest'),
 path('lsearch/', views.lsearch, name='lsearch'),
 path('ldbook/<int:pk>', views.LDeleteRanger.as_view(), name='ldbook'),
 path('lmbook/', views.LManageRanger.as_view(), name='lmbook'),
 path('ldbookk/<int:pk>', views.LDeleteView.as_view(), name='ldbookk'),
 path('lvbook/<int:pk>', views.LViewRanger.as_view(), name='lvbook'),
 path('lebook/<int:pk>', views.LEditView.as_view(), name='lebook'),
 path('lcchat/', views.LCreateChat.as_view(), name='lcchat'),
 path('llchat/', views.LListChat.as_view(), name='llchat'),
"""

