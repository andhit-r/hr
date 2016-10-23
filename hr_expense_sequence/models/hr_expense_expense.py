# -*- coding: utf-8 -*-
# Copyright 2014 Tecnativa
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class HrExpense(models.Model):
    _inherit = 'hr.expense'

    number = fields.Char(required=True, default="/", readonly=True, copy=False)

    @api.model
    def create(self, vals):
        if vals.get('number', '/') == '/':
            vals['number'] = self.env['ir.sequence'].get('hr.expense')
        return super(HrExpense, self).create(vals)

    @api.model
    def account_move_get(self, expense_id):
        '''Write expense number on account move'''
        vals = super(HrExpense, self).account_move_get(expense_id)
        expense = self.browse(expense_id)
        vals['ref'] = expense.number
        return vals
