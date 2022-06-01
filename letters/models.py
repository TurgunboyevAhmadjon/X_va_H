from django.db import models

class Togri(models.Model):
    soz = models.CharField(max_length=30)
    def __str__(self):
        return self.soz

class Notogri(models.Model):
    soz = models.CharField(max_length=35)
    togri = models.ForeignKey(Togri, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.soz}, {self.togri}"

