from django.urls import path
from core.views import ResourceView, TotalCost

urlpatterns = [
    path('resources/', ResourceView.as_view(http_method_names=['get', 'post'])),
    path('resources/<int:pk>', ResourceView.as_view(http_method_names=['patch', 'put', 'delete'])),
    path('total_cost/', TotalCost.as_view())
]
