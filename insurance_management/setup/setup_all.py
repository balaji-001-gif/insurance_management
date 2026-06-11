#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Master setup script for the Insurance Management module.
Runs all setup tasks in the correct order.

Usage:
    bench --site your-site-name execute insurance_management.setup.setup_all
    bench --site your-site-name execute insurance_management.setup.setup_all.assign_roles_to_users
"""
from __future__ import unicode_literals
import frappe


def setup_all():
    """Run all setup tasks in the correct order."""
    print("=" * 60)
    print("  Insurance Management Module Setup")
    print("=" * 60)

    # Step 1: Create Module Def
    print("\n📋 Step 1: Creating Module Def...")
    from insurance_management.setup.create_module_def import create_module_def
    create_module_def()

    # Step 2: Create Custom Roles
    print("\n👥 Step 2: Creating Custom Roles...")
    from insurance_management.setup.create_custom_roles import create_roles
    create_roles()

    # Step 3: Commit
    frappe.db.commit()

    print("\n" + "=" * 60)
    print("  ✅ Setup Complete!")
    print("=" * 60)
    print("\nNext steps:")
    print("  1. bench --site your-site-name migrate")
    print("  2. bench build --app insurance_management")
    print("  3. bench restart")
    print("  4. bench --site your-site-name execute insurance_management.setup.setup_all.assign_roles_to_users")


def assign_roles_to_users():
    """Assign Insurance Manager role to Administrator."""
    from insurance_management.setup.create_custom_roles import assign_roles_to_users as _assign
    _assign()
