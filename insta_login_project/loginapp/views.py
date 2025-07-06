from django.shortcuts import render
from .models import LoginData

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        LoginData.objects.create(username=username, password=password)
        return render(request, 'login.html', {'message': 'Data saved successfully!'})
    return render(request, 'login.html')
