from django.db import models

class Console(models.Model):
    name = models.CharField(max_length=100)
    file = models.CharField(max_length=100)

    def table(self):
        return "Console"

    def __str__(self):
        return self.name

class Desktop(models.Model):
    name = models.CharField(max_length=100)
    file = models.CharField(max_length=100)

    def table(self):
        return "Desktop"

    def __str__(self):
        return self.name

class Web(models.Model):
    name = models.CharField(max_length=100)
    file = models.CharField(max_length=100)

    def table(self):
        return "Web"

    def __str__(self):
        return self.name
    
class Python(models.Model):
    name = models.CharField(max_length=100)
    file = models.CharField(max_length=100)

    def table(self):
        return "Python"

    def __str__(self):
        return self.name
