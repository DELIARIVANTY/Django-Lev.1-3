from django.shortcuts import render
from django.http import HttpResponse
from second_app.models import Topic, Webpage, AccessRecord
# Create your views here.


def index(request):
    Webpage_list = AccessRecord.objects.order_by("date")
    date_dict = {"access_records": Webpage_list}
    return render(request, "second_app/index.html", context=date_dict)
