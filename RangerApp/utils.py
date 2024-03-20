import logging

from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import send_mail



logger = logging.getLogger(__name__)


def send_email_with_html_body(subjet: list, file: list, message: list, receivers: list, template:str, context: dict):
    """ This fonction help to send a customize email to a specific user or set of users."""

    try:
        message = render_to_string(template, context)

        send_mail(
            subjet,
            file,
            message,
            settings.EMAIL_HOST_USER,
            receivers,
            fail_silently=True,
            html_message=message,
        )

        return True

    except Exception as e:
        logger.error(e)

    return False
















"""
{% extends 'dashboard/base.html' %}


{% load static %}

{% block body %}
    <div id="content-wrapper">

        <div class="container-fluid">
            <!-- Breadcrumbs-->
            <ol class="breadcrumb">
                <li class="breadcrumb-item">
                    <a href="#">CRUD</a>
                </li>
                <li class="breadcrumb-item active">Add</li>
            </ol>
            <div class="card mb-3">
                <div class="card-header">
                    <i class="fas fa-table"></i>
                    Crud Add
                </div>
                <div class="card-body">
                  <form class="form-horizontal" action="{% url 'create_user' %}" method="POST">
                    {% csrf_token %}
                    <div class="form-group">
                        <div class="form-row">
                            <div class="col-md-6">
                                <div class="form-label-group">
                                    <input type="text" class="form-control" name="first_name" placeholder="First Name" id="inputFirst" required="">
                                    <label for="inputFirst">First Name</label>
                                </div>
                            </div>
                            <div class="col-md-6">
                                <div class="form-label-group">
                                    <input type="text" class="form-control" name="last_name" placeholder="Last Name" id="inputLast" required="">
                                    <label for="inputLast">Last Name</label>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="form-group">
                        <div class="form-row">
                            <div class="col-md-6">
                                <div class="form-label-group">
                                    <input type="text" class="form-control" name="username" placeholder="Username" id="inputdescription" required="">
                                    <label for="inputdescription">Username</label>
                                </div>
                            </div>
                            <div class="col-md-6">
                                <div class="form-label-group">
                                    <input class="form-control" type="tel" name="email" placeholder="Email" id="inputMobile" required="">
                                    <label for="inputMobile">Email</label>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="form-group">
                        <div class="form-row">
                            <div class="col-md-6">
                               <div class="form-label-group">
                                    <input type="text" class="form-control" name="password" placeholder="Password" id="inputdescription" required="">
                                    <label for="inputdescription">Password</label>
                                </div>
                            </div>
                            <div class="col-md-6">
                                <div class="form-label-group">
                                           <select class="w3-select w3-border" name="userType">
  <option value="{{ choice.2 }}">Choose User Role</option>
 
<option value="{{ choice.2 }}"> Publisher</option>
  <option value="{{ choice.3 }}"> Admin</option>
  <option value="{{ choice.4 }}"> Librarian</option>

</select>
                                </div>
                            </div>
                        </div>
                    </div>
                    <button class="btn btn-primary btn-block" type="submit">Submit &nbsp;&nbsp;&nbsp;<span></span></button>
                </form>
                </div>
            </div>
        </div>
    </div>
{% endblock %}
{% block javascript %}
    <script type="text/javascript">
        $("#id_username").attr("placeholder", "Enter Username");
        $("#id_password").attr("placeholder", "Enter Password");
    </script>
{% endblock %}
"""








"""
{% extends 'dashboard/base.html' %}


{% block content %}

<div class="container-fluid">
<div class="row">
<div class="col-sm-3" style="color: red">
  <p style="color: blue"></p>  
</div>



<div class="col-sm-6" style="padding-top: 10px;">
    <div class="card">
</div>


<div class="card mb-2">
<div class="card-body">

<div class="row" style="background-color: black">
	 <div class="card col-sm-12">
  <div class="card-header text-primary">
     <center>Welcome To BookApp Group Chat</center>
  </div>
</div>

    <div class="col-sm-8">
    	<div class="myform">
    	    <form method="POST">
    	{% csrf_token %}
    	{{ form.as_p }}

    	<br><input type="submit" value="Post" class="btn btn-lg btn-outline-primary">
    </form>
</div>

    <div class="col-sm-4"></div>
    </div>


                      </div>
                    </div>  
                  </div>

</div>



<div class="col-sm-2" style="color: red">
</div>

</div>
</div>


{% endblock content %}

"""


