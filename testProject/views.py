from django.shortcuts import render, redirect, HttpResponse

def signinPage(request):
    return render(request, 'signinPage.html')
def signupPage(request):
    return render(request, 'signupPage.html')