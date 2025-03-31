# -*- coding: utf-8 -*-
from odoo import models, fields

class Electrodomestico(models.Model):
    _name = 'mega_market.electrodomestico'
    _description = 'Electrodoméstico'

    name = fields.Char(string="Nombre", required=True)
    codigo_producto = fields.Char(string="Código de producto", required=True)
    pais_id = fields.Many2one('res.country', string='País', required=True)
    importe_compra = fields.Float(string="Importe de compra")
    moneda_id = fields.Many2one('res.currency', string='Moneda', required=True)
    precio_venta = fields.Float(string="Precio de venta")


class Cliente(models.Model):
    _name = 'mega_market.cliente'
    _description = 'Cliente'

    nombre = fields.Char(string="Nombre", required=True)
    apellidos = fields.Char(string="Apellidos")
    nif = fields.Char(string="NIF")
    direccion = fields.Char(string="Dirección")
    fecha_nacimiento = fields.Date(string="Fecha de nacimiento")
    telefono = fields.Char(string="Teléfono")
