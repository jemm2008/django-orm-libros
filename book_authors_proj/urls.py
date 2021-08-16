
from django.urls import path
from django.urls import include

urlpatterns = [
    path('', include('Whit_templa_app2.urls')),
    # path('', include('books_authors_app.urls')),
    # path('admin/', admin.site.urls),
]
