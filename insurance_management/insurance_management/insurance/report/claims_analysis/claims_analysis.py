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
        {"label": _("Claim Number"), "fieldname": "claim_number", "fieldtype": "Link", "options": "Insurance Claim", "width": 150},
        {"label": _("Claim Status"), "fieldname": "claim_status", "fieldtype": "Data", "width": 130},
        {"label": _("Claim Type"), "fieldname": "claim_type", "fieldtype": "Data", "width": 120},
        {"label": _("Claim Date"), "fieldname": "claim_date", "fieldtype": "Date", "width": 100},
        {"label": _("Policy Number"), "fieldname": "policy_number", "fieldtype": "Data", "width": 150},
        {"label": _("Customer"), "fieldname": "customer_name", "fieldtype": "Data", "width": 150},
        {"label": _("Claimed Amount"), "fieldname": "claim_amount", "fieldtype": "Currency", "width": 130},
        {"label": _("Approved Amount"), "fieldname": "approved_amount", "fieldtype": "Currency", "width": 130},
        {"label": _("Fraud Risk Score"), "fieldname": "fraud_risk_score", "fieldtype": "Float", "width": 110},
        {"label": _("Incident Date"), "fieldname": "incident_date", "fieldtype": "Date", "width": 100},
        {"label": _("Settlement Date"), "fieldname": "claim_settlement_date", "fieldtype": "Date", "width": 120},
        {"label": _("Payment Method"), "fieldname": "payment_method", "fieldtype": "Data", "width": 110},
    ]


def get_data(filters):
    conditions = get_conditions(filters)
    data = frappe.db.sql(
        """
        SELECT
            ic.claim_number,
            ic.claim_status,
            ic.claim_type,
            ic.claim_date,
            ic.policy_number,
            ic.customer_name,
            ic.claim_amount,
            ic.approved_amount,
            ic.fraud_risk_score,
            ic.incident_date,
            ic.claim_settlement_date,
            ic.payment_method
        FROM `tabInsurance Claim` ic
        WHERE ic.docstatus = 1 {conditions}
        ORDER BY ic.claim_date DESC
        """.format(conditions=conditions),
        filters,
        as_dict=True,
    )
    return data


def get_conditions(filters):
    conditions = []
    if filters.get("claim_status"):
        conditions.append("ic.claim_status = %(claim_status)s")
    if filters.get("claim_type"):
        conditions.append("ic.claim_type = %(claim_type)s")
    if filters.get("customer"):
        conditions.append("ic.customer = %(customer)s")
    if filters.get("insurance_policy"):
        conditions.append("ic.insurance_policy = %(insurance_policy)s")
    if filters.get("from_date"):
        conditions.append("ic.claim_date >= %(from_date)s")
    if filters.get("to_date"):
        conditions.append("ic.claim_date <= %(to_date)s")
    if filters.get("high_fraud_risk"):
        conditions.append("ic.fraud_risk_score > 50")
    return (" AND " + " AND ".join(conditions)) if conditions else ""


def get_message(data):
    total_claims = len(data)
    total_claimed = sum(d.get("claim_amount", 0) or 0 for d in data)
    total_approved = sum(d.get("approved_amount", 0) or 0 for d in data)
    approved_count = len([d for d in data if d.get("claim_status") == "Approved"])
    rejected_count = len([d for d in data if d.get("claim_status") == "Rejected"])

    return "Total Claims: {0} | Claimed: {1:,.2f} | Approved: {2:,.2f} | Approved: {3} | Rejected: {4}".format(
        total_claims, total_claimed, total_approved, approved_count, rejected_count
    )
