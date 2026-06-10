# -*- coding: utf-8 -*-
# Copyright (c) 2024, Insurance Management
# License: MIT

from __future__ import unicode_literals
import frappe
from frappe import _


def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    message = get_message(data)
    return columns, data, message


def get_columns():
    return [
        {"label": _("Payment ID"), "fieldname": "name", "fieldtype": "Link", "options": "Premium Payment", "width": 150},
        {"label": _("Policy Number"), "fieldname": "policy_number", "fieldtype": "Data", "width": 150},
        {"label": _("Customer"), "fieldname": "customer_name", "fieldtype": "Data", "width": 150},
        {"label": _("Payment Date"), "fieldname": "payment_date", "fieldtype": "Date", "width": 100},
        {"label": _("Payment Mode"), "fieldname": "payment_mode", "fieldtype": "Data", "width": 100},
        {"label": _("Payment Amount"), "fieldname": "payment_amount", "fieldtype": "Currency", "width": 130},
        {"label": _("Due Amount"), "fieldname": "due_amount", "fieldtype": "Currency", "width": 120},
        {"label": _("Late Fee"), "fieldname": "late_fee", "fieldtype": "Currency", "width": 100},
        {"label": _("Total Amount"), "fieldname": "total_amount", "fieldtype": "Currency", "width": 120},
        {"label": _("Payment Status"), "fieldname": "payment_status", "fieldtype": "Data", "width": 110},
        {"label": _("Receipt Number"), "fieldname": "receipt_number", "fieldtype": "Data", "width": 120},
        {"label": _("Transaction ID"), "fieldname": "transaction_id", "fieldtype": "Data", "width": 140},
    ]


def get_data(filters):
    conditions = get_conditions(filters)
    data = frappe.db.sql(
        """
        SELECT
            pp.name,
            pp.policy_number,
            c.customer_name,
            pp.payment_date,
            pp.payment_mode,
            pp.payment_amount,
            pp.due_amount,
            pp.late_fee,
            pp.total_amount,
            pp.payment_status,
            pp.receipt_number,
            pp.transaction_id
        FROM `tabPremium Payment` pp
        LEFT JOIN `tabCustomer` c ON pp.customer = c.name
        WHERE pp.docstatus = 1 {conditions}
        ORDER BY pp.payment_date DESC
        """.format(conditions=conditions),
        filters,
        as_dict=True,
    )
    return data


def get_conditions(filters):
    conditions = []
    if filters.get("payment_status"):
        conditions.append("pp.payment_status = %(payment_status)s")
    if filters.get("payment_mode"):
        conditions.append("pp.payment_mode = %(payment_mode)s")
    if filters.get("customer"):
        conditions.append("pp.customer = %(customer)s")
    if filters.get("insurance_policy"):
        conditions.append("pp.insurance_policy = %(insurance_policy)s")
    if filters.get("from_date"):
        conditions.append("pp.payment_date >= %(from_date)s")
    if filters.get("to_date"):
        conditions.append("pp.payment_date <= %(to_date)s")
    return (" AND " + " AND ".join(conditions)) if conditions else ""


def get_message(data):
    total_payments = len(data)
    total_collected = sum(d.get("payment_amount", 0) or 0 for d in data)
    total_late_fees = sum(d.get("late_fee", 0) or 0 for d in data)
    completed = len([d for d in data if d.get("payment_status") == "Completed"])
    pending = len([d for d in data if d.get("payment_status") == "Pending"])

    return "Total Payments: {0} | Collected: {1:,.2f} | Late Fees: {2:,.2f} | Completed: {3} | Pending: {4}".format(
        total_payments, total_collected, total_late_fees, completed, pending
    )
