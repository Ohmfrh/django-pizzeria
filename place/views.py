from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views import View

from place.forms import OrderForm
from place.models import Pizza


def order(request):
    if request.GET:
        return render(request, 'index.html', {'pizzas': Pizza.objects.all()})
    if request.POST:
        return HttpResponse('WIP')

    raise Http404


class Menu(View):

    def get(self, request):

        return render(request, 'index.html', {'pizzas': Pizza.objects.all()})


class Order(View, LoginRequiredMixin):

    def get(self, request):
        form = OrderForm()

        return render(request, 'create_order.html', {'form': form})

    def post(self, request):
        print(request.POST)
        form = OrderForm(request.POST)

        print(f"Valid: {form.is_valid()}")
        if form.is_valid():
            form.save()

        return render(request, 'create_order.html', {'form': form})