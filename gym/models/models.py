# -*- coding: utf-8 -*-

from odoo import models, fields, api

class GymSession(models.Model):
    _name = 'gym.session'
    _description = 'Modelo para gestionar sesiones de gimnasio'

    name = fields.Char(string="Nombre de la sesión", required=True)  
    start_time = fields.Datetime(string="Hora de inicio")
    end_time = fields.Datetime(string="Hora de fin")
    instructor_id = fields.Many2one('res.users', string="Instructor")
    capacity = fields.Integer(string="Capacidad", default=20)
