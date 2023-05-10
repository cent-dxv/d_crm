from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='home'),
    path('login',views.login_user, name='login_user'),
    # path('logout',views.logout_user, name='logout_user'),
    path('register',views.register, name='register'),
    path('records/<int:id>',views.customer_records, name='records'),
    path('add_records',views.add_records, name='add_records'),
]
