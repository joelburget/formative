from django.conf.urls.defaults import *
from django.contrib.auth.views import login, logout

from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^website/', include('website.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
     #(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     (r'^$', 'website.views.homepage'),
     (r'^site-admin/', include(admin.site.urls)),
     #(r'^accounts/login/(?P<next>[-/\w]+)?/?$', 'django.contrib.auth.views.login'),
     (r'^accounts/login/$', 'django.contrib.auth.views.login'),
     (r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
)

if not settings.PRODUCTION:
  urlpatterns += patterns('',
      (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
  )

urlpatterns += patterns('',
    (r'', include('website.posts.urls')),
)
