from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home,name='home'),
	path('pagedetail/<int:id>',views.page_detail,name='pagedetail'),
    path('faq',views.faq_list,name='faq'),
	path('enquiry',views.enquiry,name='enquiry'),
    path('gallery',views.gallery,name='gallery'),
	path('gallerydetail/<int:id>',views.gallery_detail,name='gallery_detail'),
	path('pricing',views.pricing,name='pricing'),



   
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)