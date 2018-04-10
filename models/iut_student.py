#-*- coding: utf-8 -*-

from odoo import models, fields, api

import time

class iut_student(models.Model):
    _name = 'iut.student'

    firstname = fields.Char(required=True, string='Prénom')
    lastname = fields.Char(required=True, string='Nom')
    birthdate = fields.Date(string='Date de naissance')
    age = fields.Integer(compute='_compute_age', string='Age')
 
    class_id = fields.Many2one('iut.class', string='Classe')

    @api.depends()
    def _compute_age(self):
        current_year = time.strftime("%Y-%m-%d")
        print("date" + current_year)