# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Endorsement(Document):
    def validate(self):
        pass
    
    def on_submit(self):
        pass
    
    def on_cancel(self):
        pass
