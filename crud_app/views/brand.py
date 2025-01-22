from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
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
    context = {}
    return render(request, "brand/show.html", context)


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
