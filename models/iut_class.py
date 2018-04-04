#-*- coding: utf-8 -*-

from odoo import models, fields, api

class iut_class(models.Model):
    _name = 'iut.class'

    name = fields.Char(required=True, string='Nom classe')
    level = fields.Selection([('seconde', 'Seconde'), ('premiere', 'Premiere'), ('terminale', 'Terminale')], string='Niveau')
    #student_nb = fields.Integer(compute='_compute_student_nb', string='Nombre d élèves')

    schedule_ids = fields.One2many('iut.schedule', 'class_id',
        string='Agenda')

    student_ids = fields.One2many('iut.student', 'class_id',
        string='Elèves')
    
    teacher_id = fields.Many2one('iut.professor', string='Professeur',
    required=True)

    #@api.depends()
    #def _compute_student_nb(self):