from odoo import models, fields


class Patient(models.Model):
    _inherit = 'hr.hospital.patient'
    _description = 'Patient'

    name = fields.Char(string='Patient Name', required=True)
    age = fields.Integer(string='Patient Age')
    disease_id = fields.Many2one('hr.hospital.disease', string='Disease')
    doctor_id = fields.Many2one('hr.hospital.doctor', string='Attending\
     Doctor')
