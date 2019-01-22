from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView, logout_then_login


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login/$', LoginView.as_view(template_name="portal/login.html"), name='login'),
    url(r'^logout/$', logout_then_login, name='logout'),
    url(r'^my_tasks/$', views.my_tasks, name='my_tasks'),
    url(r'^task_details/(?P<task_id>[0-9]+)/$', views.task_details, name='task_details'),
    url(r'^submit_task/(?P<task_id>[0-9]+)/$', views.submit_task, name='submit_task'),

]
