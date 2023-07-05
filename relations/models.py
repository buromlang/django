from django.db import models


# Create your models here.
class Manufacturer(models.Model):
    manufacturer_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.manufacturer_name}"


class Car(models.Model):
    manufacturer = models.ForeignKey("Manufacturer", on_delete=models.DO_NOTHING,
                                     limit_choices_to={'manufacturer_name': 'manu1'}, related_name='cars',
                                     related_query_name='car')
    car_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.manufacturer} ----> {self.car_name}"


# class Bus(models.Model):
#     # manufacturer = models.ManyToManyField("Manufacturer", through='PartnerShip')
#     manufacturer = models.ManyToManyField("Manufacturer")
#     # bus_name = models.CharField(max_length=100, null=True)
#     bus_names = models.CharField(max_length=100, null=True)
#
#     def __str__(self):
#         return f"{self.bus_names}"

class Truck(models.Model):
    manufacturer = models.ManyToManyField("Manufacturer", through='PartnerShip', through_fields=('truck', 'manufacturer1'))
    # bus_name = models.CharField(max_length=100, null=True)
    truck_name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"{self.truck_name}"


class PartnerShip(models.Model):
    truck = models.ForeignKey('Truck', on_delete=models.CASCADE)
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE, related_name='manufacturer')
    manufacturer1 = models.ForeignKey('Manufacturer', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.manufacturer1} --> {self.manufacturer1} --> {self.truck}"


class Bike(models.Model):
    one_to_one = models.OneToOneField('Manufacturer', on_delete=models.CASCADE, parent_link=False, null=True)
    bike_name = models.CharField(max_length=100, null=True)

    foreign_key = models.ForeignKey('Manufacturer', on_delete=models.CASCADE, related_name='foreign_key', null=True)

    many_to_many = models.ManyToManyField('Manufacturer', related_name='many_to_many')

    def __str__(self):
        return f"{self.bike_name}"


class Company(models.Model):
    company_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.company_name}"


class Employee(models.Model):
    company_name = models.ManyToManyField('Company', default='select company')
    emp_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.company_name} ---> {self.emp_name}"


class Vehicle(models.Model):
    vehicle_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.vehicle_name}"


class Owner(models.Model):
    vehicle_name = models.ForeignKey('Vehicle', on_delete=models.CASCADE)
    owner_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.owner_name} ---> {self.vehicle_name}"


class Aadhar(models.Model):
    aadhar_id = models.PositiveBigIntegerField()

    def __str__(self):
        return f"{self.aadhar_id} "


class Person(models.Model):
    aadhar_id = models.OneToOneField('Aadhar', on_delete=models.CASCADE)
    person_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.aadhar_id} ---> {self.person_name}"

