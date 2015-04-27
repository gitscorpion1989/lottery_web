from django.conf.urls import include, url, patterns

urlpatterns = patterns('',
    
    url(r'^login/$',  'account.views.login'),
    url(r'^auth/$',  'account.views.auth_view'),    
    url(r'^logout/$', 'account.views.logout'),
    url(r'^loggedin/$', 'account.views.loggedin'),
    url(r'^invalid/$', 'account.views.invalid_login'),
    url(r'^register/$', 'account.views.register_user'),
    url(r'^register_success/$','account.views.register_success'),
    url(r'^bet/$', 'account.views.bet'),
    url(r'^bet_record/$', 'account.views.bet_record'),  

)
