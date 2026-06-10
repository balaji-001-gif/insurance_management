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
        {"label": _("Policy Number"), "fieldname": "policy_number", "fieldtype": "Link", "options": "Insurance Policy", "width": 150},
        {"label": _("Policy Status"), "fieldname": "policy_status", "fieldtype": "Data", "width": 110},
        {"label": _("Policy Type"), "fieldname": "policy_type", "fieldtype": "Link", "options": "Policy Type", "width": 140},
        {"label": _("Insurance Provider"), "fieldname": "insurance_provider", "fieldtype": "Link", "options": "Insurance Provider", "width": 150},
        {"label": _("Customer"), "fieldname": "customer_name", "fieldtype": "Data", "width": 150},
        {"label": _("Agent"), "fieldname": "agent_name", "fieldtype": "Data", "width": 130},
        {"label": _("Start Date"), "fieldname": "start_date", "fieldtype": "Date", "width": 100},
        {"label": _("End Date"), "fieldname": "end_date", "fieldtype": "Date", "width": 100},
        {"label": _("Sum Assured"), "fieldname": "sum_assured", "fieldtype": "Currency", "width": 130},
        {"label": _("Premium Amount"), "fieldname": "premium_amount", "fieldtype": "Currency", "width": 130},
        {"label": _("Premium Frequency"), "fieldname": "premium_frequency", "fieldtype": "Data", "width": 120},
        {"label": _("Total Premium Paid"), "fieldname": "total_premium_paid", "fieldtype": "Currency", "width": 140},
        {"label": _("Payment Status"), "fieldname": "payment_status", "fieldtype": "Data", "width": 110},
        {"label": _("Risk Score"), "fieldname": "risk_score", "fieldtype": "Float", "width": 90},
        {"label": _("Risk Category"), "fieldname": "risk_category", "fieldtype": "Data", "width": 110},
    ]


def get_data(filters):
    conditions = get_conditions(filters)
    data = frappe.db.sql(
        """
        SELECT
            ip.policy_number,
            ip.policy_status,
            ip.policy_type,
            ip.insurance_provider,
            ip.customer_name,
            ip.agent_name,
            ip.start_date,
            ip.end_date,
            ip.sum_assured,
            ip.premium_amount,
            ip.premium_frequency,
            ip.total_premium_paid,
            ip.payment_status,
            ip.risk_score,
            ip.risk_category
        FROM `tabInsurance Policy` ip
        WHERE ip.docstatus = 1 {conditions}
        ORDER BY ip.creation DESC
        """.format(conditions=conditions),
        filters,
        as_dict=True,
    )
    return data


def get_conditions(filters):
    conditions = []
    if filters.get("policy_status"):
        conditions.append("ip.policy_status = %(policy_status)s")
    if filters.get("policy_type"):
        conditions.append("ip.policy_type = %(policy_type)s")
    if filters.get("insurance_provider"):
        conditions.append("ip.insurance_provider = %(insurance_provider)s")
    if filters.get("customer"):
        conditions.append("ip.customer = %(customer)s")
    if filters.get("agent"):
        conditions.append("ip.agent = %(agent)s")
    if filters.get("from_date"):
        conditions.append("ip.start_date >= %(from_date)s")
    if filters.get("to_date"):
        conditions.append("ip.end_date <= %(to_date)s")
    if filters.get("payment_status"):
        conditions.append("ip.payment_status = %(payment_status)s")
    return (" AND " + " AND ".join(conditions)) if conditions else ""


def get_message(data):
    total_policies = len(data)
    total_sum_assured = sum(d.get("sum_assured", 0) or 0 for d in data)
    total_premium = sum(d.get("premium_amount", 0) or 0 for d in data)
    total_paid = sum(d.get("total_premium_paid", 0) or 0 for d in data)

    return "Total Policies: {0} | Total Sum Assured: {1:,.2f} | Total Premium: {2:,.2f} | Total Premium Paid: {3:,.2f}".format(
        total_policies, total_sum_assured, total_premium, total_paid
    )
