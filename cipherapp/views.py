from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Message
from . import encryption
from .forms import EncryptForm, DecryptForm

def home(request):
    return render(request, 'cipherapp/home.html')

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('cipher')
    else:
        form = UserCreationForm()
    return render(request, 'cipherapp/register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('cipher')
    else:
        form = AuthenticationForm()
    return render(request, 'cipherapp/login.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('login')

@login_required
def cipher_view(request):
    result = None
    if request.method == 'POST':
        text = request.POST.get('text')
        mode = request.POST.get('mode')
        method = request.POST.get('method', 'caesar')
        try:
            if mode == 'encrypt':
                if method == 'caesar':
                    result = f"Encrypted: {encryption.encrypt_to_caesar_hex(text)}"
                else:
                    result = f"Encrypted: {encryption.encrypt_to_hex(text)}"
            elif mode == 'decrypt':
                if method == 'caesar':
                    result = f"Decrypted: {encryption.decrypt_from_caesar_hex(text)}"
                else:
                    result = f"Decrypted: {encryption.decrypt_from_hex(text)}"
        except Exception:
            result = "Invalid input."
    return render(request, 'cipherapp/cipher.html', {'result': result})

@login_required
def history_view(request):
    messages = Message.objects.filter(user=request.user).order_by('-timestamp')
    return render(request, 'cipherapp/history.html', {'messages': messages})


def about(request):
    return render(request, 'cipherapp/about.html')