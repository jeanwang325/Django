from django.conf import settings
from django.conf.urls.defaults import *
from django.conf.urls.static import static
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from SubTest.views import show_image, view_rank
from SubTest.views import show_image
from SubTest.views import choose_images
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'TPCSite.views.home', name='home'),
    # url(r'^TPCSite/', include('TPCSite.TPCSite.urls')),
    #url(r'^static\/(?P<path>.*)$','django.views.static.serve'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    #url(r'^$','Matching.views.show_image',name='show_image'),
    #url(r'^$','Matching.views.show_result',name='result'),
	url(r'^choose_images/',choose_images,name='img_group'),
    url(r'^display_images/',show_image,name='pairs'),
	# url(r'^result/', view_rank,name='answer'),
)


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)