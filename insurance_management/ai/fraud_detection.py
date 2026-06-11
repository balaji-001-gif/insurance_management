# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import frappe


def detect_claim_fraud(claim_name):
    """Stub: AI-powered fraud detection for insurance claims.

    Replace this with actual AI logic (e.g., ML model, rules engine, etc.).
    Updates the claim's fraud_risk_score and fraud_indicators.
    """
    claim = frappe.get_doc("Insurance Claim", claim_name)

    # Simple heuristic placeholder
    score = 5.0  # base score
    indicators = []

    # Check claim amount vs sum assured
    if claim.claim_amount and claim.sum_assured:
        ratio = claim.claim_amount / claim.sum_assured
        if ratio > 0.8:
            score += 20
            indicators.append("claim_amount_high_ratio")

    # Check recent policy start
    if claim.insurance_policy:
        policy = frappe.get_doc("Insurance Policy", claim.insurance_policy)
        days_since_start = (claim.claim_date - policy.start_date).days if claim.claim_date and policy.start_date else 999
        if days_since_start < 30:
            score += 15
            indicators.append("claim_near_policy_start")

    score = min(100, max(0, score))

    claim.db_set("fraud_risk_score", round(score, 2))
    claim.db_set("requires_manual_review", 1 if score > 50 else 0)
    claim.db_set("auto_approved", 0)

    return {"fraud_score": round(score, 2), "indicators": indicators}
