# -*- coding: utf-8 -*-
# © 2016 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields


class HrCompanyFacility(models.Model):
    _name = 'hr.company.facility'
    _description = 'Company Facility'

    name = fields.Char(
    	string='# Company Facility Assignment',
    	required=True,
    	readonly=True,
    	default='/',
        )
    employee_id = fields.Many2one(
    	string='Employee',
    	comodel_name='hr.employee',
    	required=True,
    	)
    product_id = fields.Many2one(
        string='Company Facility',
        comodel_name='product.templete',
        )
    date_issue = fields.Datetime(
        string='Date Issued',
        )
    date_return = fields.Datetime(
        string='Date Returned'
        )
    state = fields.Selection(
        string='State',
        selection=[
            ('draft', 'Draft'),
            ('confirmed', 'Confirmed'),
            ('approved', 'Approved'),
            ('issued', 'Issued'),
            ('returned', 'Returned'),
            ('cancelled', 'Cancelled'),
            ],
        required=True,
        readonly=True,
        default='draft',
        )

