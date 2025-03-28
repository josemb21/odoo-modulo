# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AcademyCourse(models.Model):
    _name = 'academy.course'
    _description = 'Academy Course'

    name = fields.Char(string="Course Name", required=True)
    instructor = fields.Char(string="Instructor")
    start_date = fields.Date(string="Start Date")
    description = fields.Text(string="Description")
