# -*- coding: utf-8 -*-
from __future__ import unicode_literals

def assess_risk(risk_data):
    """Stub: AI-powered risk assessment.

    Replace this with actual AI logic (e.g., calling OpenAI, a local model, etc.).
    Args:
        risk_data (dict): Contains 'age', 'sum_assured', and other risk factors.
    Returns:
        dict: {'risk_score': float, 'risk_category': str}
    """
    age = risk_data.get("age", 30)
    sum_assured = risk_data.get("sum_assured", 0)

    # Simple heuristic placeholder
    score = min(100, max(0, (age / 80) * 30 + (sum_assured / 10000000) * 70))
    if score < 25:
        category = "Low"
    elif score < 50:
        category = "Medium"
    elif score < 75:
        category = "High"
    else:
        category = "Very High"

    return {"risk_score": round(score, 2), "risk_category": category}
