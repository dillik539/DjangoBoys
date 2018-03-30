from django.conf.urls import url
from .import views

'''Add url patterns for blog app'''
urlpatterns = [
    url(r'^$', views.post_list, name = 'post_list'),

]
