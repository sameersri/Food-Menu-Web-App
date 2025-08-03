from django.urls import path
from food import views

urlpatterns=[
    path('',views.home_view,name="home"),
    path('signup/',views.register_view,name="register"),
    path('login/',views.login_view,name="login"),
    path('about/',views.about_view,name="about"),
    path('contact/',views.contact_view,name="contact"),
    path('menu/',views.menu_view,name="menu"),
    path('logout/',views.logout_view,name="logout"),
    path('create/',views.create_item,name="create"),
    path('delete/<int:id>',views.delete_item,name="delete"),
    path('update/<int:id>',views.update,name="update"),
    path('add/<int:id>',views.update,name="add"),

] 