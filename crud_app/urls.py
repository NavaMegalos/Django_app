from django.urls import path
from .views import views
from .views import brand
from .views import product_presentation

app_name = "crud"
urlpatterns = [
    path("", views.index, name="index"),
    path("brand/", brand.show_brands, name="show_brand"),
    path("brand/get/", brand.get_brand, name="get_brand"),
    path("brand/create/", brand.create_brand, name="create_brand"),
    path("brand/delete/", brand.delete_brand, name="delete_brand"),
    path("brand/update/", brand.update_brand, name="update_brand"),
    path("presentation/", product_presentation.show, name="show_presentation"),
    path("presentation/get/", product_presentation.get, name="get_presentation"),
    path("presentation/create/", product_presentation.create, name="create_presentation"),
    path("presentation/delete/", product_presentation.delete, name="delete_presentation"),
    path("presentation/update/", product_presentation.update, name="update_presentation"),
]
