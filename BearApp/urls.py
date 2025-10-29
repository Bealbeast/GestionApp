from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from coloapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('ver-usuarios/', views.ver_usuarios),
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('agreagar/', views.agregar_tarea, name='agregar_tarea' ),
    path('tarea/<int:tarea_id>/completar/', views.completar_tarea, name='completar_tarea'),
    path('tarea/<int:tarea_id>/desmarcar/', views.desmarcar_tarea, name='desmarcar_tarea'),
    path('historial/', views.historial_tareas, name='historial_tareas'),
    path('migrar/', views.ejecutar_migraciones),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
