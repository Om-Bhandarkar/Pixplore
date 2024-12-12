# Create your views here.
from django.shortcuts import render
import requests
from django.http import JsonResponse

# Unsplash API Access Key
ACCESS_KEY = "h7ta53uAgYjyJgZSGWC7JWPrCfDnW2YGcMDxupD7Wco"

def search_photos_page(request):
    query = request.GET.get('query', '')
    per_page = request.GET.get('per_page', 10)
    url = "https://api.unsplash.com/search/photos?page=1&query={query}"
    headers = {"Authorization": f"Client-ID {ACCESS_KEY}"}
    params = {"query": query, "per_page": per_page}
    response = requests.get(url, headers=headers, params=params)
    photos = response.json().get('results', []) if response.status_code == 200 else []
    return render(request, 'photos/search.html', {'photos': photos, 'query': query})

def about(request):
    return render(request,'photos/about.html')

