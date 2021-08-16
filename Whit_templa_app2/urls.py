from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('author/',views.autor),
    path('authors/',views.autor),
    path('autor/',views.autor),
    path('autores/',views.autor),
    path('autor/<int:id_solicitado>',views.autorid),
    path('libro/<int:id_solicitado>',views.libroid),
    path('borrarautor/<int:id_solicitado>',views.borrarautorid),
    path('borrarlibro/<int:id_solicitado>',views.borrarlibroid),
    path('autoraddlibro/<int:id_solicitado>',views.libroid),
    path('addlibtoautor/<int:id_solicitado>',views.autorid)
]
