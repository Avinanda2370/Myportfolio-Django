from django.db import models

# Create your models here.
class Social(models.Model):
    name = models.CharField(max_length=20)
    icon_class = models.CharField(max_length=50)
    link = models.URLField()

    def __str__(self):
        return f"{self.name} {self.icon_class}"

class Email(models.Model):
    email = models.EmailField()
    def __str__(self):
        return f"{self.email}"

class Phone(models.Model):
    phone_number = models.CharField(max_length=15)
    def __str__(self):
        return f"{self.phone_number}"

class Address(models.Model):
    address = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.address}"

class Skills(models.Model):
    TYPE_CHOICES = (
        ("Technical Skills", "Technical Skills"),
        ("Professional Skills", "Professional Skills"),
    )

    type = models.CharField(max_length=100,choices=TYPE_CHOICES)
    name = models.CharField(max_length=100)
    percentage = models.IntegerField()
    def __str__(self):
        return f"{self.name}"

class About(models.Model):
    description = models.TextField(max_length=300)
    skills = models.ManyToManyField(Skills)
    file = models.FileField(upload_to='resume/')

    def __str__(self):
        return f"{self.description}"

class Global(models.Model):
    name = models.CharField(max_length=20)
    designation = models.CharField(max_length=50)
    email = models.ManyToManyField(Email)
    phone_number = models.ManyToManyField(Phone)
    address = models.ManyToManyField(Address)
    image = models.ImageField(default=None,upload_to='profile')
    social_link = models.ManyToManyField(Social)
    def __str__(self):
        return f"{self.name}"

class Experences(models.Model):
    TYPE_CHOICE =(
        ("Education","Education"),
        ("Work","Work")
    )
    type = models.CharField(max_length=20,choices=TYPE_CHOICE)
    title = models.CharField(max_length=30)
    institution =models.CharField(max_length=30)
    description = models.TextField()
    starting_year = models.CharField(max_length=10)
    ending_year = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.title}"

class Client(models.Model):
    image = models.ImageField(default=None,upload_to='client')
    description = models.TextField()
    name = models.CharField(max_length=30)
    designation = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name}"