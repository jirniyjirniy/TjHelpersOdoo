import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)

CONST_EXP = 'Odoo school constant example'


class OdooSchoolLibraryBook(models.Models):
    _name = 'odoo.school.library.book'
    _description = 'Book'

    name = fields.Char()
    
    active = fields.Boolean(default=True, )
    description = fields.Text()

    res_partner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Main Author',
    )
