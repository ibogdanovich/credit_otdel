from django.shortcuts import render
from .models import Action, Bank
import datetime
from django.db import connection

def all_actions(request, ):
    actions = Action.objects.all()
    return render(request, "index.html", {
        'header': 'Все акции',
        'actions': actions,
    })

def shop_actions(request, shop):
    banks = []
    bankslist = {}
    actions = Action.objects.filter(shop=shop).exclude(last_update__lt=datetime.date.today())
    for i in Bank.objects.all():
        bankslist[int(i.ext_id)] = i.name
    
    for a in actions:
        banks.append(bankslist[a.bank_id])
        
    return render(request, "index.html", {
        'header': 'Акции в %s за сегодня' % shop,
        'actions': actions,
        'banks': banks
    })
    