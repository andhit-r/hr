# -*- coding: utf-8 -*-
# © 2013 Michael Telahun Makonnen <mmakonnen@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Employee Infraction Management',
    "version": "8.0.1.0.0",
    'category': 'Generic Modules/Human Resources',
    'author': "OpenSynergy Indonesia,Michael Telahun Makonnen <mmakonnen@gmail.com>,"
                   "Odoo Community Association (OCA)",
    'website': 'http://miketelahun.wordpress.com',
    'license': 'AGPL-3',
    'depends': [
        'hr',
    ],
    'data': [
        'security/ir.model.access.csv',
        'wizard/action.xml',
        'hr_infraction_data.xml',
        'hr_infraction_view.xml',
        'hr_infraction_workflow.xml',
    ],
    'installable': True,
}
