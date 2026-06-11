# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class InsurancePolicy(Document):
    def validate(self):
        if not self.policy_number:
            self.policy_number = self.name
        self.update_risk_assessment()
    
    def on_submit(self):
        self.db_set("policy_status", "Active")
    
    def on_cancel(self):
        self.db_set("policy_status", "Cancelled")
    
    def update_risk_assessment(self):
        if self.risk_score or self.risk_category:
            return
        try:
            from insurance_management.ai.risk_assessment import assess_risk
            customer = frappe.get_doc("Customer", self.customer)
            risk_data = {
                "age": customer.get("age") or 30,
                "sum_assured": self.sum_assured,
            }
            result = assess_risk(risk_data)
            self.risk_score = result.get("risk_score")
            self.risk_category = result.get("risk_category")
        except Exception:
            pass
