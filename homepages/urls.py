from django.urls import path
from .views import indexPageView, primaryPageView, secondaryPageView, testimonyPageView

urlpatterns = [
    path("testimony/", testimonyPageView, name='testimony'),
    path("secondary/", secondaryPageView, name='secondary'),
    path("primary/", primaryPageView, name='primary'),
    path("", indexPageView, name = 'index')
]
