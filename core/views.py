from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade) :
    return HttpResponse('<h1>Hello {} de {} anos</h1>'.format(nome, idade))


def somar(request, n1 ,n2) :
    soma = n1 + n2
    return HttpResponse('<h1>Números {} e {} <br>soma = {}</h1>'.format(n1, n2, soma))