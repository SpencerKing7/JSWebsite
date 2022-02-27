from django.urls import path
from .views import indexPageView, primaryPageView, secondaryPageView, testimonyPageView, saveTestimonyPageView, otherSourcesPageView

urlpatterns = [
    path("otherSources/", otherSourcesPageView, name="other"),
    path("save/", saveTestimonyPageView, name="saveTest"),
    path("testimony/", testimonyPageView, name='testimony'),
    path("secondarySources/", secondaryPageView, name='secondary'),
    path("primarySources/", primaryPageView, name='primary'),
    path("", indexPageView, name = 'index')
]
