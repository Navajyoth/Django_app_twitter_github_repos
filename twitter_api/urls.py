from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'twitter_api.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'tweets.views.Home', name='home'),
    url(r'^tweets/$', 'tweets.views.retrive_tweet', name='retrive_tweet'),
    url(r'^repos/$', 'tweets.views.retrive_repos', name='retrive_repos'),
   
)

