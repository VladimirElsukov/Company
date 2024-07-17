from django.shortcuts import render
from django.http import HttpResponse

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


def all_branches(request):
    return render(request, "branches.html", {"greeting": "Информация о всех филиалах IT-Company"})


def london(request):
    return render(
        request, "london.html", {"greeting": "Вся информация о филиале IT-Company в Лондоне"})


def paris(request):
    return render(
        request,
        "paris.html",
        {"greeting": "Вся информация о филиале IT-Company в Париже"},)
