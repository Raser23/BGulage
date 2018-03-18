from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view()),
    url(r'signup', views.SignupView.as_view()),
    url(r'signed', views.SignedView.as_view())
]
