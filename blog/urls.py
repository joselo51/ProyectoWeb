from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
   
   
    path('blog',views.blog, name="Blog"),
    path('categoria/<int:categoria_id>/',views.categoria, name="Categoria"),
    

    
   
]

