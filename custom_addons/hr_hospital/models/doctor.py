from odoo import models, fields


class Doctor(models.Model):
    _inherit = 'hr.hospital.doctor'
    _description = 'Doctor'

    name = fields.Char(string='Doctor Name', required=True)
    specialization = fields.Char(string='Specialization')
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
