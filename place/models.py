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
        return f"{self.name} -> {self.ingredients.all()}"


class PizzaRecipe(models.Model):
    pizza_id = models.ForeignKey('place.Pizza', on_delete=models.CASCADE)
    igredient_id = models.ForeignKey('place.Ingredient', on_delete=models.CASCADE)
    portion = models.IntegerField()
