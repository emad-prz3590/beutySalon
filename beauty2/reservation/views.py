from django.shortcuts import render , HttpResponse

def reservation(requets):
    return render(requets, 'reservation/reservation.html')
