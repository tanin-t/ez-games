from django.urls import path

from snippets import views

urlpatterns = [
    path("data/", views.SnippetList.as_view()),
    path("score/", views.HighestList.as_view()),
    path("score/new-high/", views.HighestList.as_view()),
]
