# -*- coding: utf-8 -*-
# Copyright 2014 Tecnativa
# Copyright 2016 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from datetime import datetime
from openerp.tests.common import TransactionCase


class HrExpenseCase(TransactionCase):
    def setUp(self, *args, **kwargs):
        super(HrExpenseCase, self).setUp(*args, **kwargs)

        self.employee = self.env.ref("hr.employee")
        self.obj_expense = self.env["hr.expense.expense"]
        self.obj_line = self.env["hr.expense.line"]

    def test_create_expense(self):
        data_header = {
            "employee_id": self.employee.id,
            "date": datetime.now().strftime("%Y-%m-%d"),
            "name": "X expense",
            }
        expense = self.obj_expense.create(data_header)
        data_detail = {
            "expense_id": expense.id,
            "name": "X expense line",
            "unit_amount": 70.0,
            "unit_quantity": 1.0,
            "date_value": datetime.now().strftime("%Y-%m-%d"),
            }
        self.obj_line.create(data_detail)
        self.assertNotEqual(
            expense.number,
            "/")
        expense.signal_workflow("confirm")
        expense.signal_workflow("validate")
        expense.signal_workflow("done")
        self.assertEqual(
            expense.account_move_id.ref,
            expense.number)
