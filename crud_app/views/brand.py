from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.urls import reverse
from django.contrib import messages
from ..models import Brand
from ..forms import BrandForm


def show_brands(request):
    brands = Brand.objects.all()
    form = BrandForm()
    context = {"brands": brands, "form": form}
    return render(request, "brand/show.html", context)


def get_brand(request):
    if not request.GET or "id" not in request.GET:
        return JsonResponse({"error": "Missing id parameter"}, status=400)

    data = {}
    id = request.GET["id"]
    try:
        brand = Brand.objects.get(id=id)
        data = {
            "id": brand.id,
            "name": brand.name,
        }
    except Brand.DoesNotExist:
        data = {"error": "Brand not found"}

    return JsonResponse(data)


def create_brand(request):
    if request.method == "POST":
        form = BrandForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Nueva Marca Agregada.")
            return redirect(reverse("crud:show_brand"))
        else:
            messages.error(request, "Formulario inválido. Inténtalo de nuevo.")

    # Handle GET method or form errors
    return render(request, "brand/show.html", {"form": form})


def delete_brand(request):
    if request.method == "POST" and "id_brand" in request.POST:
        id = request.POST["id_brand"]
        try:
            brand = Brand.objects.get(id=id)
            brand.delete()
            # If the deletion is successful, send a success response
            return JsonResponse(
                {"success": True, "message": "El registro se ha eliminado!"}
            )
        except Brand.DoesNotExist:
            # If the brand is not found, send an error response
            return JsonResponse({"success": False, "error": "Marca no encontrada."})
        except Exception as e:
            # Handle any other errors
            return JsonResponse({"success": False, "error": f"Error: {e}"})

    return JsonResponse({"success": False, "error": "Invalid request."})


def update_brand(request):
    if (
        request.method == "POST"
        and "id_brand" in request.POST
        and "name_brand" in request.POST
    ):
        id = request.POST["id_brand"]
        name = request.POST["name_brand"]
        try:
            brand = Brand.objects.get(id=id)
            brand.name = name
            brand.save()
            messages.success(request, "El registro se ha actualizado con exito!")
        except Brand.DoesNotExist:
            messages.error(request, "Marca no encontrada.")
        except Exception as e:
            messages.error(request, f"Error: {e}")

    return redirect(reverse("crud:show_brand"))
