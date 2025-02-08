from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib import messages

from ..models import ProductPresentation
from ..forms import ProductPresentationForm

def show(request):
    presentations = ProductPresentation.objects.all()
    form = ProductPresentationForm()
    context = {"presentations": presentations, "form": form}
    return render(request, "product_presentation/show.html", context)


def get(request):
    if not request.GET:
        return

    data = {}
    id = request.GET["id"]
    try:
        presentation = ProductPresentation.objects.get(id=id)
        data = {
            "id": presentation.id,
            "name": presentation.name,
        }
    except Presentation.DoesNotExist:
        data = {"error": "presentation not Found"}

    return JsonResponse(data)


def create(request):
    context = {}
    if request.method == "POST":
        presentation = ProductPresentationForm(request.POST)
        if presentation.is_valid():
            presentation.save()
            return HttpResponseRedirect(
                reverse("crud:show_presentation"),
                messages.add_message(
                    request, messages.SUCCESS, "Nueva Presentacion Agregada."
                ),
            )

    return render(request, "product_presentation/show.html", context)


def delete(request):
    if not request.POST:
        return

    id = request.POST["id_presentation"]
    try:
        presentation = ProductPresentation.objects.get(id=id)
        presentation.delete()
    except Exception as e:
        msg = messages.add_message(request, messages.ERROR, f"error: {e}")
        return HttpResponseRedirect(reverse("crud:show_presentation"), msg)

    msg = messages.add_message(request, messages.INFO, "El registro se ha eliminado!")
    return HttpResponseRedirect(reverse("crud:show_presentation"), msg)


def update(request):
    if not request.POST:
        return

    id = request.POST["id_presentation"]
    name = request.POST["name_presentation"]
    try:
        presentation = ProductPresentation.objects.get(id=id)
        presentation.name = name
        presentation.save()
    except Exception as e:
        msg = messages.add_message(request, messages.ERROR, f"error: {e}")
        return HttpResponseRedirect(reverse("crud:show_presentation"), msg)

    msg = messages.add_message(
        request, messages.SUCCESS, "El registro se ha actualizado con exito!"
    )
    return HttpResponseRedirect(reverse("crud:show_presentation"), msg)
