#-*- coding: utf-8 -*-

from odoo import models, fields, api

class iut_class(models.Model):
    _name = 'iut.class'

    name = fields.Char(required=True, string='Nom classe')
    level = fields.Selection([('seconde', 'Seconde'), ('premiere', 'Premiere'), ('terminale', 'Terminale')], string='Niveau')
    student_nb = fields.Integer(string='Nombre d élèves', compute='_compute_student_nb')

    schedule_ids = fields.One2many('iut.schedule', 'class_id', string='Agenda')

    student_ids = fields.One2many('iut.student', 'class_id', string='Elèves')
    
    teacher_id = fields.Many2one('res.partner', string='Professeur')

    @api.depends('student_ids')
    def _compute_student_nb(self):
        for record in self:
            record.student_nb = len(record.student_ids)