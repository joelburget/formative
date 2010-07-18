from django.db import models

class StaticPage(models.Model):
    slug = models.SlugField('Slug')
    body = models.TextField()

    class Meta:
        db_table = "static_pages"

    class Admin:
        pass

    def __unicode__(self):
        return self.slug

    def get_absolute_url(self):
        return "/%s/" % self.slug
