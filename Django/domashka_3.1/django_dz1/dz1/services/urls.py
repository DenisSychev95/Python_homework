from django.urls import path
from services import views
from django.conf.urls.static import static
from dz1 import settings


urlpatterns = [
    path('', views.services, name='services'),
    path('<int:detail_id>', views.detail, name='detail')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
