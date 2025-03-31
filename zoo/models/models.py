# -*- coding: utf-8 -*-
from odoo import models, fields

class Animal(models.Model):
    _name = 'zoo.animal'
    _description = 'Animal en el Zoo'

    name = fields.Char(string="Nombre", required=True)
    especie = fields.Char(string="Especie", required=True)
    identificador = fields.Char(string="Identificador único")
    pais_id = fields.Many2one('res.country', string="País de procedencia")
    edad = fields.Integer(string="Edad")
    fecha_entrada = fields.Date(string="Fecha de entrada en el zoo")


class Cuidador(models.Model):
    _name = 'zoo.cuidador'
    _description = 'Cuidador del Zoo'

    name = fields.Char(string="Nombre", required=True)
    apellidos = fields.Char(string="Apellidos")
    cargo = fields.Selection([
        ('supervisor', 'Supervisor'),
        ('encargado', 'Encargado'),
        ('cuidador', 'Cuidador'),
    ], string="Cargo")
    fecha_incorporacion = fields.Date(string="Fecha de incorporación")


class Espacio(models.Model):
    _name = 'zoo.espacio'
    _description = 'Espacio del Zoo'

    codigo = fields.Char(string="Código de espacio", required=True)
    tipo = fields.Selection([
        ('jaula', 'Jaula'),
        ('vallado', 'Vallado'),
        ('acuario', 'Acuario'),
        ('terrarium', 'Terrarium'),
    ], string="Tipo")
    area_tematica = fields.Selection([
        ('europa', 'Europa'),
        ('asia', 'Asia'),
        ('africa', 'África'),
        ('america', 'América'),
        ('oceania', 'Oceanía'),
    ], string="Área temática")
