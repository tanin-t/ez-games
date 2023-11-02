from django.urls import path

from . import views

urlpatterns = [
    path('player/', views.PlayerListCreateAPIView.as_view()),
    path('bingo-number/generate/', views.GenerateBingoNumber.as_view()),
    path('bingo-number/check/', views.CheckBingoNumberAPI.as_view()),
    path('reset-game/', views.ResetGameAPIView.as_view()),
]
