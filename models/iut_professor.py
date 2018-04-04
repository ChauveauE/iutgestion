#-*- coding: utf-8 -*-

from odoo import models, fields, api

class iut_professor(models.Model):
    _name = 'iut.professor'
    _inherit = "res.partner"

    class_id = fields.Many2one('iut.class', string='Classe')

    @api.depends('is_company','parent_id.commercial_partner_id')
    def _compute_commercial_partner(self):
        pass