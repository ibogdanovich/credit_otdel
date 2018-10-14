from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^actions/$', views.ActionListView.as_view(), name='subject_list'),
    url(r'^banks/$', views.BankListView.as_view(), name='subject_list'),
]