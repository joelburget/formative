from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic.list_detail import object_detail

def limited_object_detail(request, queryset, slug='', slug_field='slug', template_name=None):
    if(slug == ''):
       slug = 'welcome'
    post = get_object_or_404(queryset, slug=slug)
    if not (post.public or request.user.has_perm('posts.proofread')):
	return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)
    else:
	return object_detail(request, queryset, slug=slug, slug_field=slug_field, template_name=template_name)
