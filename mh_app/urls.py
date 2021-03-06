from django.conf.urls import url
from . import views

app_name = 'mh_app'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^done/$', views.done, name='done'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^signupValidation/$', views.validate_form_inputs, name='validate_form_inputs'),
    url(r'^signup/$', views.signup, name='signup'),

    url(r'^singInValidate/$', views.check_login, name='check_login'),
    url(r'^verifyEmail/$', views.verify_email, name='verify_email'),
    url(r'^verifyUsername/$', views.verify_username, name='verify_username'),

    url(r'^userProfile/$', views.user_profile, name='user_profile')

]
