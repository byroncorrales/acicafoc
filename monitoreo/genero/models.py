# -*- coding: utf-8 -*-

from django.db import models
from monitoreo.encuestas.models import *

# Indicador 25. Género

class ActividadHogar(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.nombre
        
class ActividadFinca(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.nombre
        
choice_si_no = (
                    (1,"Si"),
                    (2,"No"),
                    (3,"Junto con su esposo")
                )
                
class Participacion(models.Model):
    principal = models.ManyToManyField(ActividadHogar, verbose_name="¿Cuál es la actividad principal en su hogar?")
    actividad_finca = models.ManyToManyField(ActividadFinca, verbose_name="¿Cuáles son las actividades que realizan en la finca")
    ingreso = models.FloatField('¿Cuál es el ingreso mensual aproximado total (incluyendo todas las actividades) C$')
    decision = models.IntegerField(choices=choice_si_no, verbose_name="¿Usted toma la decisión en el manejo y administración de los recursos económicos de la familia")
    proporcion = models.FloatField('¿Qué proporción de los ingresos familiares maneja usted? %')
    encuesta = models.ForeignKey(Encuesta)
    
    class Meta:
        verbose_name_plural = "Participación de la mujer en las actividades del hogar y la finca"

class TipoOrganizacion(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.nombre
        
        
class MujerOrganizacion(models.Model):
    participa = models.IntegerField(choices=CHOICE_OPCION, verbose_name="¿Usted participa en alguna organización dentro o fuera de la comunidad")
    tipo_organizacion = models.ForeignKey(TipoOrganizacion, verbose_name="En caso de Si, qué tipo de organización")
    voto = models.IntegerField(choices=CHOICE_OPCION, verbose_name="¿Usted tiene voto en las decisiones de la organización?")
    reuniones = models.FloatField(verbose_name="¿A cuántas reuniones han asistido en los ultimos seis meses?")
    informada = models.IntegerField(choices=CHOICE_OPCION, verbose_name="¿Usted está informado sobre las actividades o decisiones de las organizaciones comunitarias?")
    ideas_familia = models.IntegerField(choices=CHOICE_OPCION, verbose_name="¿Usted comunica sus ideas o puntos de vista en la familia?")
    ideas_comunidad = models.IntegerField(choices=CHOICE_OPCION, verbose_name="¿Usted comunica sus ideas o puntos de vista en la comunidad y organización?")
    
    class Meta: 
        verbose_name_plural = "Participación de la mujer en la organización"
