import view as main
from blog import view as blog
from passwords import view as passwords
from scanner import view as scanner
from malware import view as malware
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^test$', main.test),
    url(r'^$', main.home),

    url(r'^blog/$', blog.home),
    url(r'^blog/(?P<blog>\S+)/$', blog.blog),

    url(r'^passwords/$', passwords.hashes),
    url(r'^passwords/hashes/$', passwords.hashes),
    url(r'^passwords/hashes/stats/(?P<stats_file>\S+)/$', passwords.stats),
    url(r'^passwords/password_checker/$', passwords.password_checker),

    url(r'^scanner/$', scanner.map),
    url(r'^scanner/map/$', scanner.map),
    url(r'^scanner/search/$', scanner.search),
    url(r'^scanner/exploit/$', scanner.exploit),

    url(r'^malware/$', malware.hash),
    url(r'^malware/hashes/$', malware.hash),
    url(r'^malware/hashes/\w*/$', malware.result),
    #url(r'^admin/', include(admin.site.urls)),

    #url(r'^$', HomePageView.as_view(), name='home'),
    #url(r'^formset$', DefaultFormsetView.as_view(), name='formset_default'),
    #url(r'^form$', DefaultFormView.as_view(), name='form_default'),
    #url(r'^form_by_field$', DefaultFormByFieldView.as_view(), name='form_by_field'),
    #url(r'^form_horizontal$', FormHorizontalView.as_view(), name='form_horizontal'),
    #url(r'^form_inline$', FormInlineView.as_view(), name='form_inline'),
    #url(r'^form_with_files$', FormWithFilesView.as_view(), name='form_with_files'),
    #url(r'^pagination$', PaginationView.as_view(), name='pagination'),
    #url(r'^misc$', MiscView.as_view(), name='misc'),

)
