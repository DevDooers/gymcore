from odoo import fields, models, api
import random


class ResPartner(models.Model):
    _inherit = 'res.partner'

    uid = fields.Char(string='UID', help='Unique Identifier', readonly=True)
    password = fields.Char(string='Password')

    @api.model
    def create(self, vals):
        if vals.get('uid') is None:
            uid = ''.join([str(random.randint(0, 9)) for _ in range(15)])
            vals['uid'] = uid
        return super(ResPartner, self).create(vals)
