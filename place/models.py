from _decimal import Decimal

from django.db import models


class Ingredient(models.Model):
    """
    This model contains ingredients for a pizza
    """
    name = models.CharField(max_length=50)
    cost = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name


class Pizza(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    ingredients = models.ManyToManyField('place.Ingredient', through='place.PizzaRecipe')

    def __str__(self):
        return f"{self.name}"


class PizzaRecipe(models.Model):
    pizza = models.ForeignKey('place.Pizza', on_delete=models.CASCADE)
    ingredient = models.ForeignKey('place.Ingredient', on_delete=models.CASCADE)
    portion = models.IntegerField()

    def __str__(self):
        return f"{self.pizza.name} ingredient: {self.ingredient.name}"


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Order(models.Model):

    customer = models.ForeignKey('place.Customer', on_delete=models.SET_NULL, null=True)
    pizzas = models.ManyToManyField('place.Pizza', through='place.Placeholder')

    def __str__(self):
        return f"Order {self.pk}, Customer: {self.customer} Total: ${self.get_total()}"

    def get_total(self):
        return self.placeholder_set.all().aggregate(
            total=models.Sum(
                models.F('pizza__price') * models.F('quantity'),
                output_field=models.DecimalField(decimal_places=2)
            )
        )['total']


class Placeholder(models.Model):
    quantity = models.IntegerField()

    pizza = models.ForeignKey('place.Pizza', on_delete=models.CASCADE)
    order = models.ForeignKey('place.Order', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.order}: {self.pizza} ({self.quantity}): $ {self.get_subtotal()}"

    def get_subtotal(self):
        return Decimal(self.quantity) * self.pizza.price
