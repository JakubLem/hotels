from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100)


class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='cities')


class Person(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    birthdate = models.DateField()
    email = models.EmailField()
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='persons')


class Owner(Person):
    start_date = models.DateField()


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    date_create = models.DateField()
    city =  models.ForeignKey(Country, on_delete=models.CASCADE, related_name='hotels')
    owner = models.OneToOneField(Owner)


class Employee(Person):
    ROLES = {
        'S': 'S',
        'T': 'T'
    }

    role = models.CharField(choices=ROLES)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='employees')


class Family(models.Model):
    surname = models.CharField(max_length=100)


class Client(Person):
    family = models.ForeignKey(Family, on_delete=models.CASCADE, related_name='clients')
