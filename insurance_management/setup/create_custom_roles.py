#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Run this script on your ERPNext server to create the custom Insurance roles.
Usage: bench --site your-site-name execute insurance_management.setup.create_custom_roles
"""
from __future__ import unicode_literals
import frappe


ROLES = [
    {
        "role_name": "Insurance Manager",
        "desk_access": 1,
        "is_custom": 1,
        "modules": ["Insurance"],
        "description": "Full access to all Insurance module operations including policies, claims, providers, agents, and settings.",
    },
    {
        "role_name": "Insurance Agent",
        "desk_access": 1,
        "is_custom": 1,
        "modules": ["Insurance"],
        "description": "Access to create and manage policies, quotes, and view their own agent data.",
    },
    {
        "role_name": "Insurance Underwriter",
        "desk_access": 1,
        "is_custom": 1,
        "modules": ["Insurance"],
        "description": "Access to review policies, risk assessments, and underwriting decisions.",
    },
    {
        "role_name": "Claims Adjuster",
        "desk_access": 1,
        "is_custom": 1,
        "modules": ["Insurance"],
        "description": "Access to process and manage insurance claims, surveys, and settlements.",
    },
    {
        "role_name": "Insurance Customer",
        "desk_access": 1,
        "is_custom": 1,
        "modules": ["Insurance"],
        "description": "Limited read-only access for customers to view their own policies and claims.",
    },
]


def create_roles():
    """Create all custom Insurance roles."""
    created = []
    for role_data in ROLES:
        role_name = role_data["role_name"]
        if frappe.db.exists("Role", role_name):
            print(f"⚠️  Role '{role_name}' already exists. Skipping.")
            continue

        role = frappe.get_doc({
            "doctype": "Role",
            "role_name": role_name,
            "desk_access": role_data["desk_access"],
            "is_custom": role_data["is_custom"],
            "description": role_data["description"],
        })
        role.flags.ignore_permissions = True
        role.insert()
        frappe.db.commit()
        created.append(role_name)
        print(f"✅ Created Role: {role_name}")

    if created:
        print(f"\n🎉 Successfully created {len(created)} roles: {', '.join(created)}")
    else:
        print("\nℹ️  All roles already exist. No new roles created.")

    # Now assign roles to the Workspace
    _assign_workspace_roles()


def _assign_workspace_roles():
    """Ensure the Insurance workspace has all custom roles assigned."""
    if not frappe.db.exists("Workspace", "Insurance"):
        print("⚠️  Workspace 'Insurance' not found. Skipping role assignment.")
        return

    ws = frappe.get_doc("Workspace", "Insurance")
    existing_roles = {r.role for r in ws.roles}

    for role_data in ROLES:
        role_name = role_data["role_name"]
        if role_name not in existing_roles:
            ws.append("roles", {"role": role_name})

    ws.flags.ignore_permissions = True
    ws.save()
    frappe.db.commit()
    print(f"\n✅ Workspace 'Insurance' roles updated: {[r.role for r in ws.roles]}")


def assign_roles_to_users():
    """
    Assign Insurance Manager role to Administrator.
    Run separately: bench --site your-site-name execute insurance_management.setup.create_custom_roles.assign_roles_to_users
    """
    if frappe.db.exists("User", "Administrator"):
        user = frappe.get_doc("User", "Administrator")
        existing = {r.role for r in user.roles}
        if "Insurance Manager" not in existing:
            user.append("roles", {"role": "Insurance Manager"})
            user.flags.ignore_permissions = True
            user.save()
            frappe.db.commit()
            print("✅ Assigned 'Insurance Manager' role to Administrator")
        else:
            print("ℹ️  Administrator already has 'Insurance Manager' role")
