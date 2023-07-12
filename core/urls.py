#por terminar. Se van agregando mas archivos en el transcurso
from django.urls import path
from  .views import home, poblar_base_datos,producto,producto_tienda,ficha_producto,nosotros,contacto

urlpatterns = [
    path('',home, name="home"),
    path('nosotros',nosotros, name="nosotros"),
    path('contacto',contacto, name="contacto"),
    path('poblar_base_datos',poblar_base_datos,name="poblar_base_datos"),
    path('producto/<action>/<id>',producto,name="producto"),
    path('producto_tienda',producto_tienda,name="producto_tienda"),
    path('ficha_producto/<id>',ficha_producto,name="ficha_producto"),
]
