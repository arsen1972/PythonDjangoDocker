from django.contrib import admin
from django.urls import path
from lemma.views import LemmaAPIView, MakeLemma

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/lemma/', LemmaAPIView.as_view()),
    path('api/v1/lemma/post/', MakeLemma.as_view()),
]
