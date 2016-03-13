# -*- coding: utf-8 -*-
# © 2016 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    company_facility_ids = fields.One2many(
    	string="Company Facilities",
    	comodel_name="hr.company.facility",
    	inverse_name="employee_id",
    	)
