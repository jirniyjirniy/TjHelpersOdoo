from odoo import models, fields


class Visit(models.Model):
    _inherit = 'hr.hospital.visit'
    _description = 'Patient Visit'

    patient_id = fields.Many2one('hr.hospital.patient',
                                 string='Patient', required=True)
    visit_date = fields.Date(string='Visit Date', required=True)
    notes = fields.Text(string='Notes')
