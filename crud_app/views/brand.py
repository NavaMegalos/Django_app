from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib import messages

from ..models import Brand
from ..forms import BrandForm


def show(request):
    brands = Brand.objects.all()
    form = BrandForm()
    context = {"brands": brands, "form": form}
    return render(request, "brand/show.html", context)


def get(request):
    if not request.GET:
        return

    data = {}
    id = request.GET["id"]
    try:
        brand = Brand.objects.get(id=id)
        data = {
            "id": brand.id,
            "name": brand.name,
        }
    except Brand.DoesNotExist:
        data = {"error": "Brand not Found"}

    return JsonResponse(data)


def create(request):
    context = {}
    if request.method == "POST":
        brand = BrandForm(request.POST)
        if brand.is_valid():
            brand.save()
            return HttpResponseRedirect(
                reverse("crud:show_brand"),
                messages.add_message(
                    request, messages.SUCCESS, "Nueva Marca Agregada."
                ),
            )

    return render(request, "brand/show.html", context)


def delete(request):
    context = {}
    return render(request, "brand/show.html", context)


def update(request):
    context = {}
    return render(request, "brand/show.html", context)
