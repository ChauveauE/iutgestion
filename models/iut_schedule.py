#-*- coding: utf-8 -*-

from odoo import models, fields, api

class iut_schedule(models.Model):
    _name = 'iut.schedule'

    date_start = fields.Datetime(string='Horaire début')
    date_stop = fields.Datetime(string='Horaire fin')
    room = fields.Char(string='Salle de classe')

    class_id = fields.Many2one('iut.class', string='Classe')
    course_id = fields.Many2one('iut.course', string='Cours')

    _order="date_start"