from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone
from django.views import View

from place.forms import OrderForm, AddPizzaForm
from place.models import Pizza, Order


def order(request):
    if request.GET:
        return render(request, 'index.html', {'pizzas': Pizza.objects.all()})
    if request.POST:
        return HttpResponse('WIP')

    raise Http404


class Menu(View):

    def get(self, request):

        return render(request, 'index.html', {'pizzas': Pizza.objects.all()})


class CreateOrderView(View, LoginRequiredMixin):

    def get(self, request):
        form = OrderForm()

        return render(request, 'create_order.html', {'form': form})

    def post(self, request):
        form = OrderForm(request.POST)

        if form.is_valid():
            order = form.save()

            return redirect(f"/orders/{order.pk}/")

        return render(request, 'create_order.html', {'form': form})


class EditOrderView(View, LoginRequiredMixin):

    def get(self, request, order_id):
        try:
            order = Order.objects.get(pk=order_id)
        except Order.DoesNotExist:
            return redirect('/orders/')
        form = AddPizzaForm()

        return render(request, 'edit_order.html', {'form': form,
                                                   'order': order})

    def post(self, request, order_id):
        form = AddPizzaForm(request.POST)

        print(f"POST FORM: {form.is_valid()}")
        if form.is_valid():
            receipt_item = form.save(commit=False)
            order = Order.objects.get(pk=order_id)
            receipt_item.order = order
            receipt_item.save()
            return redirect(f"/orders/{order.pk}/")

        return render(request, 'create_order.html', {'form': form})


class CloseOrderForm(View, LoginRequiredMixin):

    def post(self, request, order_id):
        order = Order.objects.get(pk=order_id)
        order.closed_at = timezone.now()
        order.save()
        return redirect(f"/orders/{order.pk}/")