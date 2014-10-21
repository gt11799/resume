from django.conf.urls import patterns, include, url
import views
import contact.views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('views',
    (r'^$', views.resume_index),
    (r'^contact/thanks/$', contact.views.thanks),
    (r'^contact/$', contact.views.contact),
    (r'^1179905405$', views.check_email),
    (r'', views.resume_index),
)
