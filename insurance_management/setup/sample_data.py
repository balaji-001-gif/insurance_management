# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import frappe
from frappe.utils import nowdate, add_days, add_years, flt, getdate


def create_sample_data():
    """Create comprehensive sample data for testing the full Insurance Management workflow."""

    frappe.flags.in_import = True

    _create_policy_types()
    _create_insurance_providers()
    _create_coverage_types()
    _create_risk_factors()
    _create_commission_structures()
    _create_insurance_products()
    agents = _create_agents()
    customer = _create_customer()
    policy = _create_insurance_policy(agents, customer)
    _create_insurance_claim(policy, customer)

    frappe.flags.in_import = False

    print("✅ Sample data created successfully!")
    print(f"   - {frappe.db.count('Policy Type')} Policy Types")
    print(f"   - {frappe.db.count('Insurance Provider')} Insurance Providers")
    print(f"   - {frappe.db.count('Coverage Type')} Coverage Types")
    print(f"   - {frappe.db.count('Risk Factor')} Risk Factors")
    print(f"   - {frappe.db.count('Commission Structure')} Commission Structures")
    print(f"   - {frappe.db.count('Insurance Product')} Insurance Products")
    print(f"   - {frappe.db.count('Agent')} Agents")
    print(f"   - 1 Customer (from ERPNext)")
    print(f"   - 1 Insurance Policy")
    print(f"   - 2 Insurance Claims")


def _create_policy_types():
    policy_types = [
        {"policy_type_name": "Term Life Insurance", "policy_type_code": "TERM-LIFE", "category": "Life", "default_base_rate": 0.5, "is_active": 1},
        {"policy_type_name": "Whole Life Insurance", "policy_type_code": "WHOLE-LIFE", "category": "Life", "default_base_rate": 1.2, "is_active": 1},
        {"policy_type_name": "Health Insurance", "policy_type_code": "HEALTH", "category": "Health", "default_base_rate": 1.8, "is_active": 1},
        {"policy_type_name": "Motor Insurance", "policy_type_code": "MOTOR", "category": "Motor", "default_base_rate": 3.0, "is_active": 1},
        {"policy_type_name": "Travel Insurance", "policy_type_code": "TRAVEL", "category": "Travel", "default_base_rate": 0.3, "is_active": 1},
    ]
    for pt in policy_types:
        if not frappe.db.exists("Policy Type", pt["policy_type_name"]):
            doc = frappe.get_doc(doctype="Policy Type", **pt)
            doc.flags.ignore_permissions = True
            doc.insert()
            print(f"  Created Policy Type: {pt['policy_type_name']}")


def _create_insurance_providers():
    providers = [
        {"provider_name": "LIC India", "license_number": "LIC-001-IND", "contact_person": "Rajesh Kumar", "email": "contact@licindia.com", "phone": "1800-258-5678", "rating": "A++", "is_active": 1},
        {"provider_name": "HDFC Life", "license_number": "HDFC-002-IND", "contact_person": "Priya Sharma", "email": "support@hdlife.com", "phone": "1800-266-7890", "rating": "A+", "is_active": 1},
        {"provider_name": "ICICI Prudential", "license_number": "ICICI-003-IND", "contact_person": "Amit Patel", "email": "info@icicipru.com", "phone": "1800-208-8888", "rating": "A+", "is_active": 1},
        {"provider_name": "Bajaj Allianz", "license_number": "BAJAJ-004-IND", "contact_person": "Sneha Gupta", "email": "service@bajajallianz.com", "phone": "1800-209-1234", "rating": "A", "is_active": 1},
    ]
    for p in providers:
        if not frappe.db.exists("Insurance Provider", p["provider_name"]):
            doc = frappe.get_doc(doctype="Insurance Provider", **p)
            doc.flags.ignore_permissions = True
            doc.insert()
            print(f"  Created Insurance Provider: {p['provider_name']}")


def _create_coverage_types():
    coverages = [
        {"coverage_name": "Accidental Death", "coverage_code": "AD", "policy_type": "Term Life Insurance", "description": "Coverage for death due to accident", "is_active": 1},
        {"coverage_name": "Critical Illness", "coverage_code": "CI", "policy_type": "Health Insurance", "description": "Coverage for major critical illnesses", "is_active": 1},
        {"coverage_name": "Hospitalization", "coverage_code": "HOSP", "policy_type": "Health Insurance", "description": "Coverage for hospitalization expenses", "is_active": 1},
        {"coverage_name": "Third Party Liability", "coverage_code": "TPL", "policy_type": "Motor Insurance", "description": "Coverage for third party damages", "is_active": 1},
        {"coverage_name": "Baggage Loss", "coverage_code": "BAG", "policy_type": "Travel Insurance", "description": "Coverage for lost baggage", "is_active": 1},
        {"coverage_name": "Natural Death", "coverage_code": "ND", "policy_type": "Term Life Insurance", "description": "Standard death coverage", "is_active": 1},
    ]
    for c in coverages:
        if not frappe.db.exists("Coverage Type", c["coverage_name"]):
            doc = frappe.get_doc(doctype="Coverage Type", **c)
            doc.flags.ignore_permissions = True
            doc.insert()
            print(f"  Created Coverage Type: {c['coverage_name']}")


def _create_risk_factors():
    factors = [
        {"factor_name": "Smoking", "factor_category": "Lifestyle", "weight": 0.4, "scoring_method": "Binary", "low_risk_score": 0, "high_risk_score": 40, "description": "Tobacco usage increases health risk"},
        {"factor_name": "High Blood Pressure", "factor_category": "Health", "weight": 0.3, "scoring_method": "Range", "low_risk_score": 10, "high_risk_score": 30, "description": "Elevated BP levels"},
        {"factor_name": "Diabetes", "factor_category": "Health", "weight": 0.25, "scoring_method": "Binary", "low_risk_score": 0, "high_risk_score": 25, "description": "Diabetic condition"},
        {"factor_name": "Hazardous Occupation", "factor_category": "Occupation", "weight": 0.35, "scoring_method": "Binary", "low_risk_score": 0, "high_risk_score": 35, "description": "Working in high-risk environments"},
        {"factor_name": "Extreme Sports", "factor_category": "Lifestyle", "weight": 0.2, "scoring_method": "Categorical", "low_risk_score": 0, "high_risk_score": 20, "description": "Participation in adventure sports"},
        {"factor_name": "Family Medical History", "factor_category": "Health", "weight": 0.2, "scoring_method": "Binary", "low_risk_score": 0, "high_risk_score": 20, "description": "Genetic predisposition to diseases"},
    ]
    for f in factors:
        if not frappe.db.exists("Risk Factor", f["factor_name"]):
            doc = frappe.get_doc(doctype="Risk Factor", **f)
            doc.flags.ignore_permissions = True
            doc.insert()
            print(f"  Created Risk Factor: {f['factor_name']}")


def _create_commission_structures():
    structures = [
        {"structure_name": "Term Life - Standard", "policy_type": "Term Life Insurance", "commission_type": "Percentage", "first_year_commission": 10, "renewal_commission": 2, "minimum_premium": 5000, "valid_from": add_years(nowdate(), -2)},
        {"structure_name": "Health - Standard", "policy_type": "Health Insurance", "commission_type": "Percentage", "first_year_commission": 8, "renewal_commission": 3, "minimum_premium": 10000, "valid_from": add_years(nowdate(), -2)},
        {"structure_name": "Motor - Standard", "policy_type": "Motor Insurance", "commission_type": "Percentage", "first_year_commission": 5, "renewal_commission": 2, "minimum_premium": 2000, "valid_from": add_years(nowdate(), -2)},
        {"structure_name": "Travel - Flat", "policy_type": "Travel Insurance", "commission_type": "Flat", "first_year_commission": 500, "renewal_commission": 100, "valid_from": add_years(nowdate(), -2)},
    ]
    for s in structures:
        if not frappe.db.exists("Commission Structure", s["structure_name"]):
            doc = frappe.get_doc(doctype="Commission Structure", **s)
            doc.flags.ignore_permissions = True
            doc.insert()
            print(f"  Created Commission Structure: {s['structure_name']}")


def _create_insurance_products():
    products = [
        {"product_name": "Term Life Platinum", "product_code": "TL-PLATINUM", "insurance_provider": "LIC India", "policy_type": "Term Life Insurance", "base_premium_rate": 0.4, "minimum_sum_assured": 500000, "maximum_sum_assured": 50000000, "minimum_age": 18, "maximum_age": 65, "is_active": 1},
        {"product_name": "Term Life Gold", "product_code": "TL-GOLD", "insurance_provider": "HDFC Life", "policy_type": "Term Life Insurance", "base_premium_rate": 0.5, "minimum_sum_assured": 250000, "maximum_sum_assured": 25000000, "minimum_age": 18, "maximum_age": 60, "is_active": 1},
        {"product_name": "Health Shield", "product_code": "HS-100", "insurance_provider": "ICICI Prudential", "policy_type": "Health Insurance", "base_premium_rate": 1.5, "minimum_sum_assured": 100000, "maximum_sum_assured": 10000000, "minimum_age": 0, "maximum_age": 80, "is_active": 1},
        {"product_name": "Motor Secure", "product_code": "MS-200", "insurance_provider": "Bajaj Allianz", "policy_type": "Motor Insurance", "base_premium_rate": 2.8, "minimum_sum_assured": 50000, "maximum_sum_assured": 5000000, "minimum_age": 18, "maximum_age": 75, "is_active": 1},
        {"product_name": "Travel Guard", "product_code": "TG-50", "insurance_provider": "LIC India", "policy_type": "Travel Insurance", "base_premium_rate": 0.25, "minimum_sum_assured": 50000, "maximum_sum_assured": 2000000, "minimum_age": 1, "maximum_age": 85, "is_active": 1},
    ]
    for p in products:
        if not frappe.db.exists("Insurance Product", p["product_name"]):
            doc = frappe.get_doc(doctype="Insurance Product", **p)
            doc.flags.ignore_permissions = True
            doc.insert()
            print(f"  Created Insurance Product: {p['product_name']}")


def _create_agents():
    agent_data = [
        {
            "agent_code": "AGT-001",
            "agent_name": "Arun Singh",
            "email": "arun.singh@example.com",
            "phone": "+91-9876543210",
            "date_of_joining": add_years(nowdate(), -3),
            "license_number": "LIC-AGT-2022-001",
            "license_valid_till": add_years(nowdate(), 2),
            "address": "42, MG Road, Bangalore - 560001",
            "commission_structure": "Term Life - Standard",
            "is_active": 1,
        },
        {
            "agent_code": "AGT-002",
            "agent_name": "Priya Mehta",
            "email": "priya.mehta@example.com",
            "phone": "+91-9876543211",
            "date_of_joining": add_years(nowdate(), -1),
            "license_number": "LIC-AGT-2023-002",
            "license_valid_till": add_years(nowdate(), 3),
            "address": "15, Connaught Place, New Delhi - 110001",
            "commission_structure": "Health - Standard",
            "is_active": 1,
        },
    ]

    agents = []
    for a in agent_data:
        if not frappe.db.exists("Agent", {"agent_code": a["agent_code"]}):
            doc = frappe.get_doc(doctype="Agent", **a)
            doc.flags.ignore_permissions = True
            doc.insert()
            agents.append(doc.name)
            print(f"  Created Agent: {a['agent_name']} ({a['agent_code']})")

    # Set first agent as manager of second, and vice versa for team structure
    if len(agents) >= 2:
        agent2 = frappe.get_doc("Agent", agents[1])
        agent2.db_set("manager", agents[0])

    return agents


def _create_customer():
    """Create an ERPNext Customer for testing."""
    if frappe.db.exists("Customer", "INS-Sample-Rahul"):
        return "INS-Sample-Rahul"

    customer = frappe.get_doc({
        "doctype": "Customer",
        "customer_name": "Rahul Verma",
        "customer_type": "Individual",
        "customer_group": "Individual",
        "territory": "India",
        "customer_primary_contact": "rahul.verma@example.com",
        "mobile_no": "+91-9876543212",
        "email_id": "rahul.verma@example.com",
    })
    customer.flags.ignore_permissions = True
    customer.insert()
    print(f"  Created Customer: Rahul Verma")
    return customer.name


def _create_insurance_policy(agents, customer):
    if not agents:
        print("  WARNING: No agents available, creating policy without agent reference")
        agent = None
    else:
        agent = agents[0]

    policy_type = "Term Life Insurance"
    provider = "LIC India"
    product = "Term Life Platinum"

    start_date = add_days(nowdate(), -30)
    end_date = add_years(start_date, 10)
    sum_assured = 10000000  # 1 Crore
    premium_amount = 45000

    policy = frappe.get_doc({
        "doctype": "Insurance Policy",
        "naming_series": "INS-POL-.YYYY.-",
        "policy_status": "Active",
        "policy_type": policy_type,
        "insurance_provider": provider,
        "insurance_product": product,
        "customer": customer,
        "agent": agent,
        "agent_commission_rate": 10.0,
        "start_date": start_date,
        "end_date": end_date,
        "policy_term": 10,
        "sum_assured": sum_assured,
        "premium_amount": premium_amount,
        "premium_frequency": "Yearly",
        "total_premium_paid": premium_amount,
        "next_premium_due_date": add_years(nowdate(), 1),
        "last_payment_date": start_date,
        "payment_status": "Paid",
        "grace_period_days": 30,
        "risk_score": 15.0,
        "risk_category": "Low Risk",
        "ai_assessment_date": nowdate(),
        "underwriting_notes": "Standard term life policy for a 35-year-old male, non-smoker, with no pre-existing conditions. Risk assessment completed via AI.",
        "terms_and_conditions": """
<h4>General Terms & Conditions</h4>
<ol>
<li>The policy is subject to the terms and conditions mentioned in the policy document.</li>
<li>Premium payments must be made on or before the due date to keep the policy in force.</li>
<li>Grace period of 30 days is available for premium payments.</li>
<li>Non-disclosure of material facts may result in claim rejection.</li>
<li>This policy participates in the bonus distribution as per company rules.</li>
</ol>
""",
        "beneficiaries": [
            {"beneficiary_name": "Anita Verma", "relationship": "Spouse", "benefit_percentage": 60, "contact_number": "+91-9876543213"},
            {"beneficiary_name": "Rohan Verma", "relationship": "Child", "benefit_percentage": 40, "date_of_birth": "2015-06-15"},
        ],
        "coverages": [
            {"coverage_type": "Natural Death", "coverage_amount": sum_assured, "description": "Standard death coverage - full sum assured", "is_rider": 0},
            {"coverage_type": "Accidental Death", "coverage_amount": sum_assured * 2, "description": "Double coverage for accidental death", "is_rider": 1, "additional_premium": 5000},
        ],
    })
    policy.flags.ignore_permissions = True
    policy.flags.ignore_validate = True
    policy.insert()
    policy.submit()
    print(f"  Created Insurance Policy: {policy.name} for Rahul Verma")
    return policy.name


def _create_insurance_claim(policy, customer):
    today = nowdate()

    # Claim 1: Accidental hospitalization claim (Open status)
    claim1 = frappe.get_doc({
        "doctype": "Insurance Claim",
        "naming_series": "INS-CLM-.YYYY.-",
        "claim_status": "Open",
        "claim_type": "Accidental",
        "claim_date": add_days(today, -7),
        "claim_amount": 150000,
        "insurance_policy": policy,
        "claim_settlement_date": "",
        "incident_date": add_days(today, -10),
        "incident_location": "Mumbai - Pune Highway, NH4",
        "incident_description": "Policyholder was involved in a road accident while traveling from Mumbai to Pune. Sustained minor injuries and was hospitalized for 3 days at Sahyadri Hospital, Pune.",
        "police_report_filed": 1,
        "police_report_number": "PCR-MH-2024-0042",
        "witness_details": "Mr. Suresh Patil (co-passenger) - +91-9876543220\nMr. Ajay Deshmukh (attending doctor) - +91-9876543221",
        "payment_method": "Bank Transfer",
        "bank_account_name": "Rahul Verma",
        "bank_account_number": "SBIN000123456789",
        "bank_name": "State Bank of India",
        "ifsc_code": "SBIN0001234",
        "claim_notes": "Initial claim filed with hospitalization bills and police report. Awaiting surveyor assessment.",
    })
    claim1.flags.ignore_permissions = True
    claim1.flags.ignore_validate = True
    claim1.insert()
    print(f"  Created Insurance Claim: {claim1.name} - Open (Accidental)")

    # Claim 2: Medical/Health claim (Approved/Paid)
    claim2 = frappe.get_doc({
        "doctype": "Insurance Claim",
        "naming_series": "INS-CLM-.YYYY.-",
        "claim_status": "Approved",
        "claim_type": "Medical",
        "claim_date": add_days(today, -60),
        "claim_amount": 85000,
        "insurance_policy": policy,
        "claim_settlement_date": add_days(today, -55),
        "incident_date": add_days(today, -65),
        "incident_location": "Bangalore",
        "incident_description": "Policyholder was diagnosed with dengue and hospitalized for 5 days at Apollo Hospitals, Bangalore.",
        "survey_date": add_days(today, -58),
        "survey_report": "Survey completed. All documents verified. Medical reports confirm dengue diagnosis. Hospital stay of 5 days confirmed. Claim recommended for approval.",
        "approved_amount": 78000,
        "claim_settlement_date": add_days(today, -55),
        "fraud_risk_score": 5.0,
        "auto_approved": 0,
        "requires_manual_review": 0,
        "review_notes": "All documentation in order. Medical reports verified with hospital. Approved with standard deduction of INR 7,000 for non-medical expenses.",
        "payment_method": "Bank Transfer",
        "payment_date": add_days(today, -54),
        "payment_reference": "NEFT-BB1234567890",
        "bank_account_name": "Rahul Verma",
        "bank_account_number": "SBIN000123456789",
        "bank_name": "State Bank of India",
        "ifsc_code": "SBIN0001234",
    })
    claim2.flags.ignore_permissions = True
    claim2.flags.ignore_validate = True
    claim2.insert()
    claim2.submit()
    print(f"  Created Insurance Claim: {claim2.name} - Approved (Medical)")


if __name__ == "__main__":
    create_sample_data()
