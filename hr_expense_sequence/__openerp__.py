# -*- coding: utf-8 -*-
# Copyright 2014 Tecnativa
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'HR expense sequence',
    'version': '9.0.1.0.0',
    'category': 'HR',
    'author': "Tecnativa,"
              "Odoo Community Association (OCA)",
    'website': 'http://www.tecnativa.com',
    'depends': [
        'hr_expense',
    ],
    'data': [
        'data/hr_expense_data.xml',
        'views/hr_expense_expense_view.xml',
    ],
    'installable': False,
    "post_init_hook": "assign_old_sequences",
}
