from odoo import models, fields


class Disease(models.Model):
    _inherit = 'hr.hospital.disease'
    _description = 'Disease'

    name = fields.Char(string='Disease Name', required=True)
    description = fields.Text(string='Description')
