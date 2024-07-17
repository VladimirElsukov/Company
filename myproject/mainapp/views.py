from django.shortcuts import render

# Create your views here.
def company(request):
    return render(request, 'index.html', {'greeting': 'Главная страница компании'})


def news(request):
    return render(request, "news.html", {"greeting": "Новости"})


def management(request):
    return render(request, "management.html", {"greeting": "Руководство компании"})


def about(request):
    return render(request, "about.html", {"greeting": "О компании"})


def contacts(request):
    return render(request, "contacts.html", {"greeting": "Контакты"})
