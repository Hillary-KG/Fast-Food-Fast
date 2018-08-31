from . views import Index
from django.urls import path
urlpatterns = [
	path('frontend/',Index.as_view(),name='index')
]