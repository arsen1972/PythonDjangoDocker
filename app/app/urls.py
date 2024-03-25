import constants
from django.contrib import admin
from django.urls import path
from lemma.views import LemmaAPIView, MakeLemma

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/lemma/', LemmaAPIView.as_view()),
    path(constants.ENDPOINT_01, MakeLemma.as_view()),
]
