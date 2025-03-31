# -*- coding: utf-8 -*-
from odoo import models, fields

class AcademyCourse(models.Model):
    _name = 'academy.course'
    _description = 'Academy Course'

    name = fields.Char('Course Name', required=True)
    instructor = fields.Char('Instructor Name', required=True)
    start_date = fields.Date('Start Date')
    description = fields.Text('Description')
