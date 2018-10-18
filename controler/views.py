import time

import paho.mqtt.client as mqtt

from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse

broker_address="celitea.cn" 
# Create your views here.

def index(request):
    return render(request,'console.html')

def forward(request):
    client = mqtt.Client("car")
    client.connect(broker_address)
    client.publish("/home/car","w")
    return redirect(reverse("index"))

def back(request):
    client = mqtt.Client("car")
    client.connect(broker_address)
    client.publish("/home/car","s")
    return redirect(reverse("index"))

def left_turn(request):
    client = mqtt.Client("car")
    client.connect(broker_address)
    client.publish("/home/car","a")
    return redirect(reverse("index"))

def right_turn(request):
    client = mqtt.Client("car")
    client.connect(broker_address)
    client.publish("/home/car","d")
    return redirect(reverse("index"))

def slow(request):
    client = mqtt.Client("led")
    client.connect(broker_address)
    client.publish("/home/led","300")
    return redirect(reverse("index"))

def genner(request):
    client = mqtt.Client("led")
    client.connect(broker_address)
    client.publish("/home/led","150")
    return redirect(reverse("index"))

def fast(request):
    client = mqtt.Client("led")
    client.connect(broker_address)
    client.publish("/home/led","50")
    return redirect(reverse("index"))

def soon(request):
    client = mqtt.Client("led")
    client.connect(broker_address)
    client.publish("/home/led","20")
    return redirect(reverse("index"))