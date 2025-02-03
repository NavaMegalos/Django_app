from django.urls import path
from .views import views
from .views import brand
from .views import product_presentation

app_name = "crud"
urlpatterns = [
    path("", views.index, name="index"),
    path("brand/", brand.show, name="show_brand"),
    path("brand/get/", brand.get, name="get_brand"),
    path("brand/create/", brand.create, name="create_brand"),
    path("brand/delete/", brand.show, name="delete_brand"),
    path("brand/update/", brand.show, name="update_brand"),
    # path("product_presentation/", views.brand.show, name="show_product_presentation"),
    # path("product_presentation/get/", views.brand.show, name="get_product_presentation"),
    # path("product_presentation/create/", views.brand.show, name="create_product_presentation"),
    # path("product_presentation/delete/", views.brand.show, name="delete_product_presentation"),
    # path("product_presentation/update/", views.brand.show, name="update_product_presentation"),
]
