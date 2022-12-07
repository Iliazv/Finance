from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('politics/', views.politics, name='politics'),
    path('case_page/<int:arg>', views.case_page, name='case_page'),
    path('all_cases/', views.all_cases, name='all_cases'),
    path('form_service/', views.form_service, name='form_service'),
    path('form_vebinar/', views.form_vebinar, name='form_vebinar'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)