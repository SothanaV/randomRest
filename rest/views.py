from django.shortcuts import render
import random
from .models import Rest
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
# Create your views here.
@staff_member_required
def getRest(request):
    a = Rest.objects.all().order_by("-no").values('no')
    b = a[0]['no']
    print(a)
    print(b)
    x = random.randint(1,b)
    print(x)
    data = Rest.objects.all().filter(no=x).values('rest',)
    r = data[0]['rest']
    print(r)
    return render(request, 'random.html', {'rest':r})