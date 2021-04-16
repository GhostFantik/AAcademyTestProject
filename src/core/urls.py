from django.urls import path
from core.views import ResourceView, TotalCost

urlpatterns = [
    path('resources/', ResourceView.as_view(http_method_names=['get', 'post']), name='resources'),
    path('resources/<int:pk>', ResourceView.as_view(http_method_names=['patch', 'put', 'delete']), name='resources-pk'),
    path('total_cost/', TotalCost.as_view(), name='total-cost')
]
