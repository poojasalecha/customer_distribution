from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.upload_data, name='customer-data'),
]