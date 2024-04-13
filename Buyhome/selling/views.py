from django.shortcuts import get_object_or_404, render, redirect
from .models import Properties
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required

@login_required
def sell(request):
    if request.method == 'POST':
        # Récupération des données du formulaire
        name = request.POST.get('name')
        description = request.POST.get('description')
        state = request.POST.get('state')
        city = request.POST.get('city')
        bedrooms = request.POST.get('bedrooms')
        bathrooms = request.POST.get('bathrooms')
        properties_geo = request.POST.get('properties_geo')
        swimming_pool = request.POST.get('swimming_pool') == 'true'
        emergency_exit = request.POST.get('emergency_exit') == 'true'
        price = request.POST.get('price')
        phone = request.POST.get('phone')
        image = request.FILES.get('image')
        status = request.POST.get('status')


        # Vérification des champs obligatoires
        if not (name and description and state and city and bedrooms and bathrooms and price and phone and image):
            messages.error(request, "Veuillez remplir tous les champs obligatoires.")
            return redirect('sell')

        # Création d'une nouvelle instance de propriété
        property_instance = Properties(
            name=name,
            description=description,
            state=state,
            city=city,
            bedrooms=bedrooms,
            bathrooms=bathrooms,
            properties_geo=properties_geo,
            swimming_pool=swimming_pool,
            emergency_exit=emergency_exit,
            price=price,
            phone=phone,
            image=image,
            owner=request.user,
            status = status
        )

        # Enregistrement de la nouvelle propriété
        property_instance.save()

        messages.success(request, 'Votre propriété a été ajoutée avec succès.')
        return redirect('properties_list')

    return render(request, 'sell.html')

def properties_list(request):
    properties = Properties.objects.filter(status='available')
    return render(request, 'properties.html', {'properties': properties})

def property_detail(request, property_id):
    # Récupérer la propriété spécifique à partir de son ID ou renvoyer une erreur 404 si elle n'existe pas
    property = get_object_or_404(Properties, id=property_id)

    # Passer la propriété au template pour l'affichage
    return render(request, 'property_details.html', {'property': property})

@login_required
def user_properties(request):
    user = request.user
    user_properties_for_sale = Properties.objects.filter(owner=user)
    user_properties_bought = Properties.objects.filter(owner=user, status='sold')

    return render(request, 'user-properties.html', {
        'user_properties_for_sale': user_properties_for_sale,
        'user_properties_bought': user_properties_bought,
    })




@login_required
def buy_property(request, property_id):
    property = get_object_or_404(Properties, id=property_id)
    if request.user == property.owner:
        messages.error(request, "Vous ne pouvez pas acheter votre propre maison.")
        return redirect('properties_list')
        
    if request.method == 'POST':
        if property.status == 'available':
            property.status = 'sold'
            property.save()
            messages.success(request, f"{property.name} a été vendu avec succès !")
            return redirect('properties_list')
        else:
            messages.error(request, "Cette propriété n'est pas disponible à la vente.")
            return redirect('properties_list')

@login_required
def delete(request, property_id):
    property = get_object_or_404(Properties, id=property_id, owner=request.user)
    if request.method == 'POST':
        property.delete()
        messages.success(request, f"La propriété {property.name} a été supprimée avec succès.")
        return redirect('properties_list')  # Redirection vers la liste des propriétés
    return render(request, 'user-properties.html', {'property': property})



