from django.core.cache import cache
from rest_framework.response import Response
from rest_framework import generics
from .models import FAQ
from .serializers import FAQSerializer
from rest_framework.views import APIView

# Create your views here.
class FAQListCreateView(generics.ListCreateAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def get_serializer_context(self):
        return {'request': self.request}  # Pass request for language selection

    def list(self, request, *args, **kwargs):
        lang = request.GET.get('lang', 'en')
        cache_key = f'faqs_{lang}'  # Cache key per language
        cached_data = cache.get(cache_key)

        if cached_data:
            return Response(cached_data)

        response = super().list(request, *args, **kwargs)
        cache.set(cache_key, response.data, timeout=3600)  # Cache for 1 hour
        return response

class FAQRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def get_serializer_context(self):
        return {'request': self.request}  # Pass request for language selection
    
class ClearCacheView(APIView):
    def post(self, request):
        cache.clear()
        return Response({'message': 'Cache cleared successfully'})