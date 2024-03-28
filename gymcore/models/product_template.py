from odoo import fields, models

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    gym_ok = fields.Boolean(string='Is a Gym?', default=True)
