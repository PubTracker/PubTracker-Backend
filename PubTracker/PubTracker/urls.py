from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'PubTracker.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', include('pub.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
