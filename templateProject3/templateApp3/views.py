from django.shortcuts import render
import datetime
# Create your views here.
def dateTimeview(request):
    dt = datetime.datetime.now()
    h1 = dt.strftime('%H')
    h = int(h1)
    if(h < 12):
        msg = "Good Morning"
    elif(h < 15):
        msg = "Good Afternoon"
    elif(h <20):
        msg = "Good Evening"
    else:
        msg = "Good Nights"
    d = {'datetime':dt,'message':msg}
    return render(request,'templateApp3/1.html',d)
