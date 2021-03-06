# -*- coding: utf-8 -*-

from django.db import models
from monitoreo.encuestas.models import *

# Create your models here.

# Indicador 13. Propiedades y Bienes

CHOICE_AMBIENTE = ((1,"1"),
                   (2,"2"),
                   (3,"3"),
                   (4,"4"),
                   (5,"5"))
                   
class Casa(models.Model):
    nombre = models.CharField(max_length=100)
    nombre_en = models.CharField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return self.nombre
        
    class Meta:
        verbose_name_plural = "Tipos de casa"
        
class Piso(models.Model):
    nombre = models.CharField(max_length=100)
    nombre_en = models.CharField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return self.nombre
        
    class Meta:
        verbose_name_plural = "Pisos"

class Techo(models.Model):
    nombre = models.CharField(max_length=100)
    nombre_en = models.CharField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return self.nombre
        
    class Meta:
        verbose_name_plural = "Techos"

class TipoCasa(models.Model):
    '''Modelo tipos de casa
    '''
    tipo = models.ManyToManyField(Casa, verbose_name='Tipo de la casa', null=True, blank=True)
    piso = models.ManyToManyField(Piso, verbose_name="Piso", null=True, blank=True)
    techo = models.ManyToManyField(Techo, verbose_name="Techo", null=True, blank=True)
    encuesta = models.ForeignKey(Encuesta)
    
#    def __unicode__(self):
#        return u'%s' % self.get_tipo_display()

    class Meta:
        verbose_name_plural = "13.1-Vivienda"


class DetalleCasa(models.Model):
    '''Modelo detalle de casa
    '''
    tamano = models.IntegerField('Tamaño en mt cuadrado',null=True, blank=True)
    ambientes = models.IntegerField(choices=CHOICE_AMBIENTE,null=True, blank=True)
    letrina = models.IntegerField(choices=CHOICE_OPCION,null=True, blank=True)
    encuesta = models.ForeignKey(Encuesta)
    
    def __unicode__(self):
        return u'%s' % str(self.tamano)

    class Meta:
        verbose_name_plural = "Detalles de casa"

class Equipos(models.Model):
    nombre = models.CharField(max_length=100)
    nombre_en = models.CharField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Propiedades-Equipos"


class Infraestructuras(models.Model):
    nombre = models.CharField(max_length=100)
    nombre_en = models.CharField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Propiedades-Infraestructura"

class Propiedades(models.Model):
    '''Modelo propiedades
    '''
    equipo = models.ForeignKey(Equipos, null=True, blank=True)
    cantidad_equipo = models.IntegerField(null=True, blank=True)
    encuesta = models.ForeignKey(Encuesta)
    
    def __unicode__(self):
        return u'%s' % self.equipo.nombre
    
    class Meta:
        verbose_name_plural = "13.2 Equipos"
        
        
class Infraestructura(models.Model):
    infraestructura = models.ForeignKey(Infraestructuras, null=True, blank=True)
    cantidad_infra = models.IntegerField('Cantidad', null=True, blank=True)
    encuesta = models.ForeignKey(Encuesta)
    
    def __unicode__(self):
        return u'%s' % self.infraestructura.nombre
    
    class Meta:
        verbose_name_plural = "Infraestructura"

class NombreHerramienta(models.Model):
    nombre = models.CharField(max_length=100)
    nombre_en = models.CharField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Herramientas-Nombres"

class Herramientas(models.Model):
    '''Modelo herramientas
    '''
    herramienta = models.ForeignKey(NombreHerramienta, null=True, blank=True)
    numero = models.IntegerField(null=True, blank=True)
    encuesta = models.ForeignKey(Encuesta)

    def __unicode__(self):
        return self.herramienta.nombre

    class Meta:
        verbose_name_plural = "13.3-Herramientas"


class NombreTransporte(models.Model):
    nombre = models.CharField(max_length=100)
    nombre_en = models.CharField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Transporte-Nombre"


class Transporte(models.Model):
    '''Modelo transporte
    '''
    transporte = models.ForeignKey(NombreTransporte, null=True, blank=True)
    numero = models.IntegerField(null=True, blank=True)
    encuesta = models.ForeignKey(Encuesta)
    
    def __unicode__(self):
        return u'%s' % self.transporte.nombre
    
    class Meta:
        verbose_name_plural = "Medio de transporte"
#-------------------------------------------------------------------------------
