from django.contrib import admin
from django.urls import path, include
from shopify import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing_page, name='landing_page'),  # dashboard.html
     # Your homepage view
    path('', include('shopify.urls')),        # Include app-level URLs
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
