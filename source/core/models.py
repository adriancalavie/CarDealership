from django.db import models
from django.conf import settings
from django.urls import reverse


class Car(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    price = models.FloatField()
    primary_image = models.CharField(max_length=1000, null=True)
    secondary_image = models.CharField(max_length=1000, null=True)
    featured = models.BooleanField(default=False)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.title + " " + str(self.price)

    def get_absolute_url(self):
        return reverse("core:car_detail", kwargs={"slug": self.slug})

    def get_buy_url(self):
        return reverse("core:buy-car", kwargs={
            'slug': self.slug
        })


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    car = models.ForeignKey(Car,
                            on_delete=models.CASCADE,
                            null=True)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.user.username + " <= " + str(self.car) + " at " + str(self.ordered_date)

    def get_absolute_url(self):
        return reverse("core:order_detail",  kwargs={"slug": self.slug})
