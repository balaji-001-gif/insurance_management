# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "insurance_management"
app_title = "Insurance Management"
app_publisher = "Balaji"
app_description = "Comprehensive AI-powered insurance management application for ERPNext"
app_email = "balaji@example.com"
app_license = "MIT"

# Includes
# --------------------------
# include js, css files in header of desk
# app_include_css = "/assets/insurance_management/css/insurance_management.css"
# app_include_js = "/assets/insurance_management/js/insurance_management.js"

# include js, css files in header of web
# web_include_css = "/assets/insurance_management/css/insurance_management.css"
# web_include_js = "/assets/insurance_management/js/insurance_management.js"

# include specific scss files
# app_include_scrs = ["public/scss/insurance_management.scss"]

# include js, css files in header of web template
# web_include_css = "/assets/insurance_management/css/insurance_management.css"
# web_include_js = "/assets/insurance_management/js/insurance_management.js"

# Jenv Template
# --------------------------
# add methods and filters to jinja environment
# jinja = {
#     "methods": ["insurance_management.utils.jinja_methods"],
#     "filters": ["insurance_management.utils.jinja_filters"],
# }

# Installation
# --------------------------
# install_info = [
#     {
#         "app_name": "insurance_management",
#         "title": "Insurance Management",
#         "description": "Comprehensive AI-powered insurance management application for ERPNext",
#         "version": "0.0.1",
#     }
# ]

# Desk Notifications
# --------------------------
# def get_notification_config():
#     return {
#         "notifications": [
#             {"icon": "icon-plus", "color": "green", "route": "Form/Insurance Policy", "reference_doctype": "Insurance Policy"},
#         ]
#     }

# Document Events
# --------------------------
# Hook on document methods and events
# doc_events = {
#     "*": {
#         "validate": "insurance_management.events.validate",
#     },
#     "Sales Invoice": {
#         "validate": "insurance_management.events.validate_sales_invoice",
#     },
# }

# Scheduled Tasks
# --------------------------
# scheduler_events = {
#     "daily": [
#         "insurance_management.tasks.daily",
#     ],
#     "hourly": [
#         "insurance_management.tasks.hourly",
#     ],
#     "weekly": [
#         "insurance_management.tasks.weekly",
#     ],
#     "monthly": [
#         "insurance_management.tasks.monthly",
#     ],
# }

# Testing
# --------------------------
# before_tests = "insurance_management.setup.before_tests"

# Overriding Methods
# ------------------------------
# override_whitelisted_methods = {
#     "frappe.client.get_count": "insurance_management.overrides.get_count",
# }

# Fixtures
# --------------------------
fixtures = [
    {"dt": "Workspace", "filters": [["module", "=", "Insurance"]]},
]
