# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class InsuranceClaim(Document):
    def validate(self):
        if not self.claim_number:
            self.claim_number = self.name
    
    def on_submit(self):
        self.db_set("claim_status", "Under Review")
        try:
            from insurance_management.ai.fraud_detection import detect_claim_fraud
            detect_claim_fraud(self.name)
        except Exception:
            pass
