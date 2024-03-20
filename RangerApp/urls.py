from django.urls import path
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [


# Shared URL's
 path('', views.login_form, name='home'),
 path('login/', views.loginView, name='login'),
 path('locks/', views.lockView, name='locks'),
 path('logout/', views.logoutView, name='logout'),
 #path('regform/', views.register_form, name='regform'),
 #path('register/', views.registerView, name='register'),



 # Publisher URL's
 path('publisher/', views.publisher, name='publisher'),
 path('books/', views.UBookListView.as_view(), name='books'),
 path('uabook_form/', views.uabook_form, name='uabook_form'),
 path('uabook/', views.uabook, name='uabook'),
 path('ucchat/', views.UCreateChat.as_view(), name='ucchat'),
 path('ulchat/', views.UListChat.as_view(), name='ulchat'),
 path('request_form/', views.request_form, name='request_form'),
 path('delete_request/', views.delete_request, name='delete_request'),
 path('feedback_form/', views.feedback_form, name='feedback_form'),
 path('send_feedback/', views.send_feedback, name='send_feedback'),
 path('about/', views.about, name='about'),
 path('usearch/', views.usearch, name='usearch'),
 path('alpayement/', views.ListPayepView.as_view(), name='alpayement'),
 path('alsetting/', views.ListSettingpView.as_view(), name='alsetting'),
 path('calendar/', views.calendarp, name='calendar'),
 path('profile/', views.profilep, name='profile'),
 path('lock/', views.lockp, name='lock'),

# client url's
 path('create_client_form/', views.create_clientp_form, name='create_client_form'),
 path('alclient/', views.ListClientpView.as_view(), name='alclient'),
 path('create_client/', views.create_clientp, name='create_client'),
 path('alvclient/<int:pk>', views.ALViewClientp.as_view(), name='alvclient'),  
 path('aeclient/<int:pk>', views.AEditClientp.as_view(), name='aeclient'),
 path('adclient/<int:pk>', views.ADeleteClientp.as_view(), name='adclient'),






 # Admin URL's
 path('dashboard/', views.dashboard, name='dashboard'),
 path('logout/', views.logout, name='logout'),


# Settings url's
 path('settings/', views.settings, name='settings'),
 path('alsetting/', views.ListSettingView.as_view(), name='alsetting'),
 path('create_setting_form/', views.create_setting_form, name='create_setting_form'),
 path('create_setting/', views.create_setting, name='create_setting'),


# others url's 
 
 path('profile/', views.profile, name='profile'),
 path('lock/', views.lock, name='lock'),
 path('calendar/', views.calendar, name='calendar'),
 path('compose/', views.compose, name='compose'),
 path('inbox/', views.inbox, name='inbox'),
 path('mailview/', views.mailview, name='mailview'),


 # book url's
 path('aabook_form/', views.aabook_form, name='aabook_form'),
 path('aabook/', views.aabook, name='aabook'),
 path('albook/', views.ABookListView.as_view(), name='albook'),
 path('ambook/', views.AManageBook.as_view(), name='ambook'),
 path('adbook/<int:pk>', views.ADeleteBook.as_view(), name='adbook'),
 path('avbook/<int:pk>', views.AViewBook.as_view(), name='avbook'),
 path('aebook/<int:pk>', views.AEditView.as_view(), name='aebook'),
 path('adbookk/<int:pk>', views.ADeleteBook.as_view(), name='adbookk'),

# users url's
 path('create_user_form/', views.create_user_form, name='create_user_form'),
 path('aluser/', views.ListUserView.as_view(), name='aluser'),
 path('create_user/', views.create_user, name='create_user'),
 path('alvuser/<int:pk>', views.ALViewUser.as_view(), name='alvuser'),
 path('aeuser/<int:pk>', views.AEditUser.as_view(), name='aeuser'),
 path('aduser/<int:pk>', views.ADeleteUser.as_view(), name='aduser'),



# Event url's
 path('create_event_form/', views.create_event_form, name='create_event_form'),
 path('alevent/', views.ListEventView.as_view(), name='alevent'),
 path('create_event/', views.create_event, name='create_event'),
 path('alvevent/<int:pk>', views.ALViewEvent.as_view(), name='alvevent'),
 path('aeevent/<int:pk>', views.AEditEvent.as_view(), name='aeevent'),
 path('adevent/<int:pk>', views.ADeleteEvent.as_view(), name='adevent'),




# Salary url's
 path('create_salary_form/', views.create_salary_form, name='create_salary_form'),
 path('alsalary/', views.ListSalaryView.as_view(), name='alsalary'),
 path('create_salary/', views.create_salary, name='create_salary'),
 path('alvsalary/<int:pk>', views.ALViewSalary.as_view(), name='alvusalary'),
 path('aesalary/<int:pk>', views.AEditSalary.as_view(), name='aesalary'),
 path('adsalary/<int:pk>', views.ADeleteSalary.as_view(), name='adsalary'),

 path('alpayement/', views.ListPayeView.as_view(), name='alpayement'),


# service url's
path('create_service_form/', views.create_service_form, name='create_service_form'),
path('alservice/', views.ListServiceView.as_view(), name='alservice'),
path('create_service/', views.create_service, name='create_service'),
path('alvservice/<int:pk>', views.ALViewService.as_view(), name='alvservice'), 
path('aeservice/<int:pk>', views.AEditService.as_view(), name='aeservice'),
path('adservice/<int:pk>', views.ADeleteService.as_view(), name='adservice'),


# category url's
path('create_category_form/', views.create_category_form, name='create_category_form'),
path('create_category/', views.create_category, name='create_category'),
path('aecategory/<int:pk>', views.AEditCategory.as_view(), name='aecategory'),
path('adcategory/<int:pk>', views.ADeleteCategory.as_view(), name='adcategory'),
path('alcategory/', views.ListCategoryView.as_view(), name='alcategory'),
path('alvcategory/<int:pk>', views.ALViewCategory.as_view(), name='alvcategory'), 


# client url's
 path('create_client_form/', views.create_client_form, name='create_client_form'),
 path('alclient/', views.ListClientView.as_view(), name='alclient'),
 path('create_client/', views.create_client, name='create_client'),
 path('alvclient/<int:pk>', views.ALViewClient.as_view(), name='alvclient'),  
 path('aeclient/<int:pk>', views.AEditClient.as_view(), name='aeclient'),
 path('adclient/<int:pk>', views.ADeleteClient.as_view(), name='adclient'),


# chat url's
 path('acchat/', views.ACreateChat.as_view(), name='acchat'),
 path('alchat/', views.AListChat.as_view(), name='alchat'),


 # others url's
 path('adrequest/', views.ADeleteRequest.as_view(), name='adrequest'),
 path('afeedback/', views.AFeedback.as_view(), name='afeedback'),
 path('asearch/', views.asearch, name='asearch'),


]



""""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">
    {% block title %}{% endblock %}
    <title>PIMS</title>


    {% block stylesheets %}
      <!-- Bootstrap CSS -->
   
      <!-- Custom CSS -->
      <style media="screen">
        .invalid {
          color: #dc3545;
          font-size: 80%;
        }
        body {
          display: flex;
          flex-direction: column;
          min-height: 100vh;
        }
        .footer {
          margin: auto 0 0;
          height: 56px;
        }
      </style>
    {% endblock stylesheets %}

    {% load static %}
    <!-- Custom fonts for this template-->
    <link href="{% static 'vendor/fontawesome-free/css/all.min.css' %}" rel="stylesheet" type="text/css">
       <link rel="stylesheet" href="{% static 'assets/css/bootstrap.min.css' %}">
      <!-- Font awesome CSS -->
      <link rel="stylesheet" href="{% static 'assets/fonts/font-awesome-4.7.0/css/font-awesome.min.css' %}">

    <!-- Page level plugin CSS-->
    <link href="{% static 'vendor/datatables/dataTables.bootstrap4.css' %}" rel="stylesheet">

    <!-- Custom styles for this template-->
    <link rel="stylesheet" type="text/css" href="{% static 'css/master.css' %}">
    <link href="{% static 'css/sb-admin.css' %}" rel="stylesheet">
    {% block stylesheet %}{% endblock %}
</head>

<body id="page-top">

<!-- headers-->
<nav class="navbar navbar-expand navbar-dark bg-dark fixed-top">

    <a class="navbar-brand mr-1 text-primary" href="">BookApp Dashboard</a>
    <button class="btn btn-link btn-sm text-white order-1 order-sm-0" id="sidebarToggle" href="#">
        <i class="fas fa-bars"></i>
    </button>

    <!-- Navbar Search -->
      <form class="d-none d-md-inline-block form-inline ml-auto mr-0 mr-md-3 my-2 my-md-0" action="{% url 'asearch' %}">
        <div class="input-group">
            <input type="text" class="form-control" name="query" placeholder="Search for..." aria-label="Search" aria-describedby="basic-addon2">
            <div class="input-group-append">
                <button class="btn btn-primary" type="submit">
                    <i class="fas fa-search"></i>
                </button>
            </div>
        </div>
    </form>

    <!-- Navbar -->
    <ul class="navbar-nav ml-auto ml-md-0">
        <li class="nav-item dropdown no-arrow">
            <a class="nav-link dropdown-toggle" href="#" id="userDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                <i class="fas fa-user-circle fa-fw text-primary"></i>
            </a>
            <div class="dropdown-menu dropdown-menu-right" aria-labelledby="userDropdown">
                <a class="dropdown-item">{{ user.username }}</a>
                <div class="dropdown-divider"></div>
                <a class="dropdown-item" href="" data-toggle="modal" data-target="#logoutModal">Logout</a>
            </div>
        </li>
    </ul>

</nav>

<div id="wrapper" style="padding-top: 50px">


<!-- Sidebar -->
<ul class="sidebar navbar-nav">

    <li class="nav-item active">
        <a class="nav-link" href="{% url 'dashboard' %}">
            <i class="fas fa-fw fa-tachometer-alt"></i>
            <span>Admin Dashboard</span>
        </a>
    </li>
    <li class="nav-item active">
        <a class="nav-link" href="">
            <i class="fas fa-user-circle fa-fw text-warning"></i>
            <span style="color: yellow">Logged As {{ user.username }}</span>
        </a>
    </li>
    <li class="nav-item">
        <a class="nav-link" href="{% url 'alchat' %}">
            <i class="fas fa-book text-primary"></i>
            <span style="color: white">Group Chat</span>
        </a>
    </li>
        <li class="nav-item">
        <a class="nav-link" href="{% url 'aabook_form' %}">
            <i class="fas fa-book text-primary"></i>
            <span style="color: white">Add Book</span>
        </a>
    </li>
    <li class="nav-item">
        <a class="nav-link" href="{% url 'albook' %}">
            <i class="fas fa-book text-primary"></i>
            <span style="color: white">Recent Added Books</span>
        </a>
    </li>

      <li class="nav-item">
        <a class="nav-link" href="{% url 'ambook' %}">
            <i class="fas fa-book text-primary"></i>
            <span style="color: white">Manage Books</span>
        </a>
    </li>
     <li class="nav-item">
        <a class="nav-link" href="{% url 'adrequest' %}">
            <i class="fas fa-book text-primary"></i>
            <span style="color: white">Delete Request</span>
        </a>
    </li>
     <li class="nav-item">
        <a class="nav-link" href="{% url 'afeedback' %}">
            <i class="fas fa-book text-primary"></i>
            <span style="color: white">User Feedback</span>
        </a>
    </li>
     <li class="nav-item">
        <a class="nav-link" href="{% url 'aluser' %}">
            <i class="fas fa-user text-primary"></i>
            <span style="color: white">Manage User</span>
        </a>
    </li>
</ul>    

    {% block body %}{% endblock %}
    {% block content %}{% endblock content %}

    <!-- /.content-wrapper -->
</div>
<!-- /#wrapper -->

<!-- Scroll to Top Button-->
<a class="scroll-to-top rounded" href="#page-top">
    <i class="fas fa-angle-up"></i>
</a>

<!-- Logout Modal-->
<div class="modal fade" id="logoutModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel"
     aria-hidden="true">
    <div class="modal-dialog" role="document">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="exampleModalLabel">Ready to Leave?</h5>
                <button class="close" type="button" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">×</span>
                </button>
            </div>
            <div class="modal-body">Select "Logout" below if you are ready to end your current session.</div>
            <div class="modal-footer">
                <button class="btn btn-secondary" type="button" data-dismiss="modal">Cancel</button>
               <a class="btn btn-primary" href="{% url 'logout' %}">Logout</a>
            </div>
        </div>
    </div>
</div>

    <!-- JavaScript -->
    {% block scripts %}
      <script src="{% static 'assets/js/jquery-3.2.1.min.js' %}"></script>
      <script src="{% static 'assets/js/popper.min.js' %}"></script>
      <script src="{% static 'assets/js/bootstrap.min.js' %}"></script>
      <!-- You can alternatively load the minified version -->
      <script src="{% static 'js/jquery.bootstrap.modal.forms.js' %}"></script>
    {% endblock scripts %}

    {% block extrascripts %}{% endblock extrascripts %}
"""

















"""
<video loop muted autoplay playsinline class="video">
  <source src="{% static 'css/back.mp4' %}" type="video/mp4" />
</video>
<!-- Custom styles for this template-->
    <link href="{% static 'bookstore/css/login.css' %}" rel="stylesheet">
    <link href="{% static 'bookstore/css/bootstrap/bootstrap.min.js' %}" rel="stylesheet">
    <link href="{% static 'bookstore/js/login.css' %}" rel="stylesheet">
    <link href="{% static 'vendor/datatables/dataTables.bootstrap4.css' %}" rel="stylesheet">
    <link href="{% static 'vendor/datatables/dataTables.bootstrap4.css' %}" rel="stylesheet">


    
<head>
	<title>Ranger</title>
</head>
<!--Coded with love by Mutiullah Samim-->
<body> 


<link href="//maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css">
<script src="//maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>
<script src="//cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
<!------ Include the above in your HEAD tag ---------->

<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.0.8/css/all.css">
    <link href="{% static 'css/style.css' %}" rel="stylesheet">



<div class="container">
<br> 


		 <h1 style="color: white" class="text-md-center"><span class="g"></span><span class="o"></span><span class="o1">Ranger</span> <span class="g"></span><span class="l"></span><span class="e"></span></h1>

<div class="row">
	<aside class="col-sm-4">
	</aside> <!-- col.// -->

	<aside class="col-sm-4">
		<h1 style="color: yellow; font-weight: bold; font-size: 40px" class="text-md-center"><span class="g"></span><span class="o"></span><span class="o1"></span>Ranger<span class="g"></span><span class="l"></span><span class="e"></span></h1>
		<br>
<div class="card">
<article class="card-body" style="padding-top: 0px">
<div class="d-flex justify-content-center">




	<div class="container">
  <div class="d-flex justify-content-center h-100">
    <div class="card">
      <div class="card-header">
        <center><h3>Login In Here</h3></center>
        <div class="d-flex justify-content-end">
          <span><i class="fab fa-user"></i></span>
        </div>
      </div>
      <div class="card-body">
        <form method="POST" action="{% url 'login' %}">
          {% csrf_token %}
          <div class="input-group form-group">
            <div class="input-group-prepend">
              <span class="input-group-text"><i class="fas fa-user"></i></span>
            </div>
            <input type="text" class="form-control" placeholder="username" name="username" required="">
            
          </div>
          <div class="input-group form-group">
            <div class="input-group-prepend">
              <span class="input-group-text"><i class="fas fa-key"></i></span>
            </div>
            <input type="password" class="form-control" placeholder="password" name="password" required="">
          </div>
          <div class="form-group">
            <input type="submit" name="sign-in" value="Sign In" class="btn float-left login_btn">
          </div>
        </form>
      </div>
      <div class="card-footer">
        <div class="d-flex justify-content-center">
              {% if messages %}
            <div class="messages">
                {% for message in messages %}

                    <a class="alert alert-success" style="color:red;"> {{ message }}</a>

                {% endfor %}
            </div>
            {% endif %}
              </div>
      </div>
    </div>
  </div>
</div>
		






</article>
</div> <!-- card.// -->




	</aside> <!-- col.// -->
	<aside class="col-sm-4">
	</aside> <!-- col.// -->
</div> <!-- row.// -->

</div> 


                            

</body>
</html>
"""





















"""

<div class="col-md-8 col-sm-5 col-xs-5">


 <div id="content-wrapper">
        <div class="container-fluid">
            <!-- Breadcrumbs-->
            <ol class="breadcrumb">
                <li class="breadcrumb-item">
                    <a href="">Dashboard</a>
                </li>
                <li class="breadcrumb-item active">Overview</li>
            </ol>

            <!-- Icon Cards-->
            <div class="row">
                                <div class="col-xl-3 col-sm-6 mb-3">
                    <div class="card text-white bg-success o-hidden h-100">
                        <div class="card-body">
                            <div class="card-body-icon">
                                <i class="fas fa-fw fa-book"></i>
                            </div>
                            <div class="mr-5"> <strong>Books</strong> : {{ book }}</div>
                        </div>
                        <a class="card-footer text-white clearfix small z-1" href="#">
                            <span class="float-left">Total Books</span><br>
                            <span class="float-right">
                </span>
                        </a>
                    </div>
                </div>

                <div class="col-xl-3 col-sm-6 mb-3">
                    <div class="card text-white bg-warning o-hidden h-100">
                        <div class="card-body">
                            <div class="card-body-icon">
                                <i class="fas fa-user-circle fa-fw"></i>
                            </div>
                            <div class="mr-5"> <strong>Users</strong> : {{ user }}</div>
                        </div>
                        <a class="card-footer text-white clearfix small z-1" href="">
                            <span class="float-left">Total Users</span><br>
                            <span class="float-right">
                </span>
                        </a>
                    </div>
                </div>
            </div>
        </div>
        </div>  



            </div>
        </div>
    </div>
</div>
"""