from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

from . import views

app_name='my_portfolio'

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'new/', views.ProjectNew.as_view(), name='new_project'),
    url(r'about/', views.AboutView.as_view(), name='about'),
    url(r'contact/', views.ContactView.as_view(), name='contact'),
    url(r'(?P<pk>\d+)/$', views.ProjectView.as_view(), name='project'),
]
