from django.urls import re_path,path, include

urlpatterns = [
   re_path('api/', include('snippets.urls')),
]