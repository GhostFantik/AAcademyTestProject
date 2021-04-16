from django.urls import path
from core.views import ResourceView

urlpatterns = [
    path('resources/', ResourceView.as_view())
]
