from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def firstView(request, number):
    return HttpResponse(f"Here your number {number}")


def randomFun(request):
    return HttpResponse(f'Here your random number {random.randrange(0,101)}')


def maxNum(request, number):
    max_num = random.randint(0, number)
    return HttpResponse(f'The user gave the number {number}, and the program picks up {max_num}')


def maxMin(request, minnum, maxnum):
    number = random.randint(minnum, maxnum)
    return HttpResponse(f'{minnum} and {maxnum} was borders for {number} number')

def name(request, username):
    return HttpResponse(f'Your name is- {username}')

def calc(request, number1, number2, symbol):
    number1 = int(number1)
    number2 = int(number2)
    if symbol == "+":
        result = number1+number2
    elif symbol == "-":
        result = number1-number2
    elif symbol == ":":
        result = number1 / number2
    elif symbol == "*":
        result = number1 * number2
    return HttpResponse(f'Your result is {result}')
