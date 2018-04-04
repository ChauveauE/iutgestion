#-*- coding: utf-8 -*-

from odoo import models, fields, api

class iut_course(models.Model):
    _name = 'iut.course'

    name = fields.Char(required=True, string='Nom cours')

    schedule_ids = fields.One2many('iut.schedule', 'course_id',
        string='Agenda')