# -*- coding: utf-8 -*-
# © 2013 Savoir-faire Linux (<http://www.savoirfairelinux.com>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Experience Management",
    "version": "8.0.0.1.0",
    "author": "Savoir-faire Linux,Odoo Community Association (OCA)",
    "maintainer": 'Savoir-faire Linux',
    "website": "http://www.savoirfairelinux.com",
    "license": "AGPL-3",
    "category": "Human Resources",
    "description": """
Experience Management
=====================

This module allows you to manage your employee experiences:
    * Professional
    * Academic
    * Certification

Contributors
------------
* El Hadji DEM (elhaji.dem@savoirfairelinux.com)
""",

    "depends": ["hr", ],
    'external_dependencies': {},
    'data': [
        "security/ir.model.access.csv",
        "security/hr_security.xml",
        "views/hr_employee_view.xml",
        "views/hr_academic_view.xml",
        "views/hr_professional_view.xml",
        "views/hr_certification_view.xml",
    ],
    "demo": [],
    "test": [],
    'installable': True
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
