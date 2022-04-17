from django.db import models

class Rol(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class User_College(models.Model):
    name = models.CharField(max_length=40)
    identification = models.CharField(max_length=11)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    password = models.CharField(max_length=200)
    rol = models.ForeignKey(
        Rol, on_delete=models.CASCADE
    )
    state = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Type_Place(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Place(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    type_place = models.ForeignKey(
        Type_Place, on_delete=models.CASCADE
    )
    state = models.BooleanField(default=True)

    def __str__(self):
        return self.name

def place_directory_path(instance, filename):
    return 'static/upload/place/{0}/{1}'.format(instance.place.id, filename)

class Image_Place(models.Model):
    place = models.ForeignKey(
        Place, on_delete=models.CASCADE
    )
    image = models.FileField(upload_to=place_directory_path, null=True, blank=True)
    location = models.IntegerField()
    state = models.BooleanField(default=True)

    def __str__(self):
        return self.location

class User_Place(models.Model):
    user_college = models.ForeignKey(
        User_College, on_delete=models.CASCADE
    )
    place = models.ForeignKey(
        Place, on_delete=models.CASCADE
    )
    state = models.BooleanField(default=True)

    def __str__(self):
        return self.id

class Type_Service(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    type_service = models.ForeignKey(
        Type_Service, on_delete=models.CASCADE
    )
    state = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Line_Day(models.Model):
    day = models.IntegerField()
    start_hour = models.TimeField()
    end_hour = models.TimeField()

    def __str__(self):
        return self.day

class Schedule_Service(models.Model):
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE
    )
    line_day = models.ForeignKey(
        Line_Day, on_delete=models.CASCADE
    )
    state = models.BooleanField(default=True)

    def __str__(self):
        return self.id

class Service_Place(models.Model):
    place = models.ForeignKey(
        Place, on_delete=models.CASCADE
    )
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE
    )
    state = models.BooleanField(default=True)

    def __str__(self):
        return self.id

def catalog_directory_path(instance, filename):
    return 'static/upload/service/{0}/catalog/{1}'.format(instance.service.id, filename)

class Catalog_Service(models.Model):
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE
    )
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    cost = models.IntegerField()
    image = models.FileField(upload_to=catalog_directory_path, null=True, blank=True)
    state = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Order_Service(models.Model):
    user_college = models.ForeignKey(
        User_College, on_delete=models.CASCADE
    )
    date = models.DateField(auto_now_add=True)
    status = models.IntegerField()

    def __str__(self):
        return self.date

class Order_Catalog(models.Model):
    order_service = models.ForeignKey(
        Order_Service, on_delete=models.CASCADE, null=True
    )
    catalog_service = models.ForeignKey(
        Catalog_Service, on_delete=models.CASCADE
    )
    quantity = models.IntegerField()

    def __str__(self):
        return self.id

class Traceability_Order_Service(models.Model):
    order_service = models.ForeignKey(
        Order_Service, on_delete=models.CASCADE, null=True
    )
    date_time = models.DateTimeField(auto_now_add=True)
    action = models.CharField(max_length=30)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.action

class Fines(models.Model):
    user_college = models.ForeignKey(
        User_College, on_delete=models.CASCADE
    )
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE
    )
    date_time = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField()

    def __str__(self):
        return self.date_time
