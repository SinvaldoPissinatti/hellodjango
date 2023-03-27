from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade) :
    return HttpResponse('<h1>Hello {} de {} anos</h1>'.format(nome, idade))


def calculo(request, operacao, n1 ,n2) :
    soma = n1 + n2
    subtracao = n1 - n2
    multiplicacao = n1 * n2
    divisao = n1 / n2

    if operacao == 1:
        return HttpResponse('Resultado da soma é: {}'.format(soma))
    elif operacao == 2:
        return HttpResponse('Resultado da subtração é: {}'.format(subtracao))
    elif operacao == 3:
        return HttpResponse('Resultado da multiplicação é: {}'.format(multiplicacao))
    elif operacao == 4:
        return HttpResponse('Resultado da divisão é: {}'.format(divisao))
    else:
        return HttpResponse('<h1>Operação inválida</h1>')