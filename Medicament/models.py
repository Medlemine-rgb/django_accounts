from django.db import models
from datetime import datetime
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
Moment_Prise = (
    ('Sans importance','Sans importance'),
    ('En dehors des repas','En dehors des repas'),
    ('Avant le repas','Avant le repas'),
    ('Pendant le repas','Pendant le repas'),
    ('A pres le repas','A pres le repas'),
    
)
class Medicament(models.Model):
    nom_medicament = models.CharField(max_length=50)
    pathologie = models.CharField(max_length=50)
    form_pharmaceatique = models.TextField(max_length=50,choices=Form_phar_TYPE)
    nombre_comprime = models.IntegerField()
    moment_de_prise = models.TextField(max_length=50,choices=Moment_Prise)
    date_de_prise = models.DateTimeField(default=datetime.now)
    img_medical =  models.ImageField(upload_to="medical_img/",default='medical_img/default.png')
