from odoo import models, fields, api

class ModuloApp(models.Model):
    _name = 'modulo_app.modulo_app'
    _description = 'ModuloApp'

    # Definición de campos
    name = fields.Char(string='Name')
    value = fields.Integer(string='Value')
    value2 = fields.Float(string='Value 2', compute='_value_pc', store=True)

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
