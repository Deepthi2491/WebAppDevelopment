from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home,name='Home.html'),
    path('Click',views.Link,name='Click.html'),
    path('Edu',views.Edu,name='Edu.html')
]

urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT )
