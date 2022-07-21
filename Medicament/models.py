from django.db import models

# Create your models here.

Form_phar_TYPE = (
    ('Comprime','Comprime'),
    ('Gélule','Gélule'),
    ('Sirop / solution buvable','Sirop/ solution buvable'),
    ('Comprimé effervescent','Comprimé effervescent'),
    ('Créme','Créme'),
    ('Ampoule','Ampoule'),
    ('Granules','Granules'),
    ('Granules','Granules'),
    ('Goutte','Goutte'),
    ('Injection','Injection'),
    ('Pommade','Pommade'),
    ('Collyre','Collyre'),
    ('Pulvérisation','Pulvérisation'),
    ('Suppositoire','Suppositoire'),
    ('Sachet','Sachet'),
    ('Inhalation','Inhalation'),
)
class Medicament(models.Model):
    nom_medicament = models.CharField(max_length=50)
    pathologie = models.CharField(max_length=50)
    form_pharmaceatique = models.TextField(max_length=50,choices=Form_phar_TYPE)
    nombre_comprime = models.IntegerField()
