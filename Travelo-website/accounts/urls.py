from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('register', views.register, name="register"),
    # path('login', views.login , name="login"),
    # path('logout',views.logout,name= "logout")
]
#  {% if user.is_authenticated % } 
#                                              <li>Hello , {{user.first_name}}</li>
#                                             <li><a href="accounts/logout">logout</a></li>
#                                              {% else %} 
#                                             <li><a href="accounts/register">Register</a></li>
#                                             <li><a href="accounts/login">login</a></li>
#                                              { % endif %} 
# this is used in index.html for login and logout