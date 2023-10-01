from django.db import models

class Auriculares(models.Model):

    articulo = models.CharField(max_length=80)
    precio = models.IntegerField()
    stock = models.IntegerField()

    def __str__(self):
        return f'{self.articulo}'
    
class Monitores(models.Model):

    articulo = models.CharField(max_length=80)
    precio = models.IntegerField()
    stock = models.IntegerField()

    def __str__(self):
        return f'{self.articulo}'

class Mouses(models.Model):

    articulo = models.CharField(max_length=80)
    precio = models.IntegerField()
    stock = models.IntegerField()

    def __str__(self):
        return f'Articulo: {self.articulo}'


class Teclados(models.Model):

    articulo = models.CharField(max_length=80)
    precio = models.IntegerField()
    stock = models.IntegerField()

    def __str__(self):
        return f'Articulo: {self.articulo}'



class SillasGamer(models.Model):

    articulo = models.CharField(max_length=80)
    precio = models.IntegerField()
    stock = models.IntegerField()

    def __str__(self):
        return f'{self.articulo}'




      
   




