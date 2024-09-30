from django.shortcuts import render
from django.http import HttpResponse

def hola(recuest):
    return HttpResponse('Hola, Emi, respondiendo')
