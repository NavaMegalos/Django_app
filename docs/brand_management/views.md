```markdown
# Views: Brand Management

This section documents the views used for **Brand Management** in the Django project.
```

## `show_brands`


##### Description
This view renders a list of all brands in the system and provides a form to create a new brand.

###### Code:

```python
def show_brands(request):
    brands = Brand.objects.all()
    form = BrandForm()
    context = {"brands": brands, "form": form}
    return render(request, "brand/show.html", context)


```
## `create_brand`


##### Description
This view handles the creation of a new brand. It validates the submitted form and, if valid, saves the brand to the database.


###### Code:
```python
def create_brand(request):
    if request.method == "POST":
        form = BrandForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Nueva Marca Agregada.")
            return redirect(reverse("crud:show_brand"))
        else:
            messages.error(request, "Formulario inválido. Inténtalo de nuevo.")
    return render(request, "brand/show.html", {"form": form})

```
## `delete_brand`


##### Description
This view handles the deletion of a brand. It deletes the specified brand if it exists and returns a success message.


###### Code:
```python
def delete_brand(request):
    if request.method == "POST" and "id_brand" in request.POST:
        id = request.POST["id_brand"]
        try:
            brand = Brand.objects.get(id=id)
            brand.delete()
            return JsonResponse({"success": True, "message": "El registro se ha eliminado!"})
        except Brand.DoesNotExist:
            return JsonResponse({"success": False, "error": "Marca no encontrada."})

```
## `update_brand`


##### Description
This view allows you to update the name of an existing brand. It takes the brand ID and the new name from the POST request and updates the corresponding `Brand` object in the database.

###### Code:
```python
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
```
