from django.conf.urls.defaults import *
from website.static.models import StaticPage

info_dict = {
    'queryset': StaticPage.objects.all(),
}

urlpatterns = patterns('',
    (r'^(?P<slug>[-\w]+)/?$', 'django.views.generic.list_detail.object_detail', dict(info_dict, slug_field='slug')),#template_name='base.html')),
)
