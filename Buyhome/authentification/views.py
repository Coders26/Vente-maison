from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def authentification(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not (username and password):
            messages.error(request, "Veuillez remplir tous les champs du formulaire.")
            return redirect('authentification')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print("Utilisateur connecté avec succès:", user)
            return redirect('properties_list')
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
            return redirect('authentification')

    return render(request, 'authentification.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if not (username and password and confirm_password):
            return render(request, 'signup.html', {'error_message': "Veuillez remplir tous les champs du formulaire."})

        if password != confirm_password:
            return render(request, 'signup.html', {'error_message': "Les mots de passe ne correspondent pas."})
        else:
            User.objects.create_user(username=username, password=password)
            return redirect('authentification')

    return render(request, 'signup.html')

def deconnexion(request):
    logout(request)
    return redirect('properties_list')
