from django.db import models
import sys
sys.path.append('/home/joelburget/lib/python')
from BeautifulSoup import BeautifulSoup
from pygments import formatters, lexers, highlight
#import logging
#LOG_FILENAME = '/home/joelburget/website/posts/log.out'
#logging.basicConfig(filename = LOG_FILENAME, level = logging.DEBUG)

class InlineHtmlFormatter(formatters.HtmlFormatter):
  def wrap(self, source, outfile):
    return self._wrap_code(source)

  def _wrap_code(self, source):
    yield 0, '<code>'
    for t in source:
      yield t
    yield 0, '</code>'

class StyleSheet(models.Model):
    name = models.CharField(max_length=50)
    file = models.FileField(upload_to='css')
    media = models.CharField(max_length=100, default='screen')

    def __unicode__(self):
        return self.name

class Script(models.Model):
    name = models.CharField(max_length=50)
    file = models.FileField(upload_to='js')

    def __unicode__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=50)

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField('Slug')
    comments = models.BooleanField('Comments Enabled', default=True)
    public = models.BooleanField('Public', default=False)
    information = models.BooleanField('Display Information', default=True)
    guest_author = models.ForeignKey(Author, null=True)
    published = models.DateTimeField('Date Published', auto_now_add=True)
    last_edited = models.DateTimeField('Date Updated', auto_now=True)
    additional_header = models.TextField(blank=True)
    style_files = models.ManyToManyField(StyleSheet, blank=True, null=True)
    style = models.TextField(blank=True)
    script_files = models.ManyToManyField(Script, blank=True, null=True)
    script = models.TextField(blank=True)
    body = models.TextField()
    body_highlighted = models.TextField(editable=False, blank=True)

    class Meta:
      ordering = ['-published']
      permissions = (
          ("proofread", "Proofread not yet public posts"),
      )

    class Admin:
        pass

    def __unicode__(self):
       return self.title

    def get_absolute_url(self):
        return "/%s/" % self.slug

    def save(self):
        self.body_highlighted = self.highlight_code(self.body)
        super(Post, self).save()

    def highlight_code(self, html):
      BeautifulSoup.QUOTE_TAGS['code'] = None
      soup = BeautifulSoup(html)
      preblocks = soup.findAll('code')
      for pre in preblocks:
        if pre.has_key('class'):
          try:
            code = ''.join([unicode(item) for item in pre.contents])
            if 'inline' in pre['class']:
                lexer = lexers.get_lexer_by_name(pre['class'].split(' ')[0])
                formatter = InlineHtmlFormatter()
                code_hl = highlight(code, lexer, formatter)
                pre.contents = [BeautifulSoup(code_hl)]
                pre.name = 'span'
                print "here"
                print pre
            else:
                lexer = lexers.get_lexer_by_name(pre['class'])
                formatter = formatters.HtmlFormatter(linenos='table')
                code_hl = highlight(code, lexer, formatter)
                pre.contents = [BeautifulSoup(code_hl)]
                pre.name = 'div'
          except:
            #logging.debug(sys.exc_info())
            #logging.debug(pre['class'])
            break
      return unicode(soup)
