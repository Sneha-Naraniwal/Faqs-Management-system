from django.urls import path
from .views import FAQListCreateView, FAQRetrieveUpdateDeleteView
from .views import ClearCacheView

urlpatterns = [
    path('faqs/', FAQListCreateView.as_view(), name='faq-list'),
    path('faqs/<int:pk>/', FAQRetrieveUpdateDeleteView.as_view(),
         name='faq-detail'),
    path('faqs/clear-cache/', ClearCacheView.as_view(), name='clear-cache'),
]
