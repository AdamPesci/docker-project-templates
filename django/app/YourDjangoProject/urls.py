from django.urls import path
from .views import HomePageView, DebugFormView

urlpatterns = [
    path('', HomePageView.as_view()),
    path('debug-form', DebugFormView.as_view())
]
