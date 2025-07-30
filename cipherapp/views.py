from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Message
from . import encryption
from .forms import EncryptForm, DecryptForm

# Home page view
def home(request):
    return render(request, 'cipherapp/home.html')

# User registration view
def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('cipher')
    else:
        form = UserCreationForm()
    return render(request, 'cipherapp/register.html', {'form': form})

# User login view
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())  # Log the user in
            return redirect('cipher')
    else:
        form = AuthenticationForm()
    return render(request, 'cipherapp/login.html', {'form': form})

# User logout view
def logout_user(request):
    logout(request)
    return redirect('login')

# Main cipher view for encrypting and decrypting text
@login_required
def cipher_view(request):
    result = None
    if request.method == 'POST':
        text = request.POST.get('text')
        mode = request.POST.get('mode')
        method = request.POST.get('method', 'caesar')
        try:
            if mode == 'encrypt':
                encrypted = (
                    encryption.encrypt_to_caesar_hex(text)
                    if method == 'caesar'
                    else encryption.encrypt_to_hex(text)
                )
                result = f"Encrypted: {encrypted}"
                Message.objects.create(
                    user=request.user,
                    method=method,
                    original_text=text,
                    encrypted_text=encrypted
                )
            elif mode == 'decrypt':
                decrypted = (
                    encryption.decrypt_from_caesar_hex(text)
                    if method == 'caesar'
                    else encryption.decrypt_from_hex(text)
                )
                result = f"Decrypted: {decrypted}"
                Message.objects.create(
                    user=request.user,
                    method=method,
                    original_text=decrypted,
                    encrypted_text=text
                )
        except Exception as e:
            result = f"Invalid input: {e}"
    return render(request, 'cipherapp/cipher.html', {'result': result})

# View to display the user's message history
@login_required
def history_view(request):
    messages = Message.objects.filter(user=request.user).order_by('-timestamp')
    return render(request, 'cipherapp/history.html', {'messages': messages})

# About page view
def about(request):
    return render(request, 'cipherapp/about.html')