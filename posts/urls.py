from django.conf.urls.defaults import *
from website.posts.models import Post

info_dict = {
    'queryset': Post.objects.all(),
}

urlpatterns = patterns('',
   (r'^posts/?$', 'django.views.generic.list_detail.object_list', info_dict),
   (r'^$', 'website.posts.views.limited_object_detail', dict(info_dict, slug='', slug_field='slug')),
   (r'^(?P<slug>[-\w]+)/?$', 'website.posts.views.limited_object_detail', dict(info_dict, slug_field='slug')),
)
