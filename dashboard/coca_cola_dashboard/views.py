from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from django.views.generic import TemplateView
from django.db import connections

db_conn = connections['default']


class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)



def search_if_present(name: str, number: str):
    query = "select * from COCA_COLA_CUSTOMERS where name={} and number={};".format(name, number)
    with db_conn.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchone()
        print(result)


@csrf_exempt
def send_sms(request, **kwargs):
    name = request.POST.get("name")
    number = request.POST.get("number")
    product = request.POST.get("product")
    if_present = search_if_present(name, number)
    return HttpResponse("hello world")
