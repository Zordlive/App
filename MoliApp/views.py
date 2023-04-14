from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def nav(request):
    return render(request, 'nav.html')

def about(request):
    return render(request, 'about.html')

def actualite(request):
    return render(request, 'actualite.html')

def header(request):
    return render(request, 'header.html')

def footer(request):
    return render(request, 'footer.html')
def inscription(request):
    return render(request, 'inscription.html')