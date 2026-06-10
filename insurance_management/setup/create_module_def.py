#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Run this script on your ERPNext server to create the Module Def for Insurance.
Usage: bench --site your-site-name execute insurance_management.setup.create_module_def
"""
from __future__ import unicode_literals
import frappe


def create_module_def():
    """Create the Module Def for Insurance if it doesn't exist."""
    module_name = "Insurance"
    app_name = "insurance_management"

    if frappe.db.exists("Module Def", module_name):
        print(f"✅ Module Def '{module_name}' already exists.")
        doc = frappe.get_doc("Module Def", module_name)
        print(f"   App Name: {doc.app_name}")
        print(f"   Module Name: {doc.module_name}")
        print(f"   Label: {doc.module_name}")
        return doc.name

    doc = frappe.get_doc({
        "doctype": "Module Def",
        "module_name": module_name,
        "app_name": app_name,
        "icon": "icon-shield",
    })
    doc.flags.ignore_permissions = True
    doc.insert()
    frappe.db.commit()
    print(f"✅ Module Def '{module_name}' created successfully!")
    print(f"   App Name: {app_name}")
    print(f"   Module Name: {module_name}")
    return doc.name
