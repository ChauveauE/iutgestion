#-*- coding: utf-8 -*-

from odoo import models, fields, api

class iut_professor(models.Model):
    _name = 'iut.professor'
    _inherit = "res.partner"

    class_id = fields.Many2one('iut.class', string='Classe')
    name = fields.Char(required=False)
    employee_ref = fields.Char(required=False)
    property_account_receivable_id = fields.Integer(required=False)
    property_account_payable_id = fields.Integer(required=False)

    @api.depends('is_company','parent_id.commercial_partner_id')
    def _compute_commercial_partner(self):
        pass