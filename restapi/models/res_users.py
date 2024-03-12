# -*- coding: utf-8 -*-
# Part of Odoo. See COPYRIGHT & LICENSE files for full copyright and licensing details.

from odoo import models, api


class ResUsers(models.Model):
    _inherit = 'res.users'

    def action_view_authentication(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Authentication',
            'res_model': 'auth.auth',
            'view_mode': 'tree,form',
            'domain': [('user_id', '=', self.id)],
            'context': {'default_user_id': self.env.user.id}
            }

    @api.model
    def name_search(self, name, args=None, operator='ilike', limit=100):
        """
        Override method for apply domain on user
        """
        context = dict(self.env.context)
        setting_user = [self.env.uid]
        if context.get('is_rest_api_user'):
            if self.env.user.has_group('base.group_system'):
                setting_user = (self.env.ref('base.group_user').users).ids
            args.append(('id', 'in', setting_user))
        return super(ResUsers, self).name_search(name, args=args, operator=operator, limit=limit)

    @api.model
    def search_read(self, domain=None, fields=None, offset=0, limit=None, order=None):
        context = dict(self.env.context)
        setting_user = [self.env.uid]
        if context.get('is_rest_api_user'):
            if self.env.user.has_group('base.group_system'):
                setting_user = (self.env.ref('base.group_user').users).ids
            domain = [('id', 'in', setting_user)]
        return super(ResUsers, self).search_read(domain, fields, offset, limit, order)
