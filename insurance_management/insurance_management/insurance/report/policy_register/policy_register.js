// Copyright (c) 2024, Insurance Management
// License: MIT

frappe.query_reports["Policy Register"] = {
    filters: [
        {
            fieldname: "policy_status",
            label: __("Policy Status"),
            fieldtype: "Select",
            options: "\nDraft\nActive\nLapsed\nExpired\nCancelled\nSurrendered",
        },
        {
            fieldname: "policy_type",
            label: __("Policy Type"),
            fieldtype: "Link",
            options: "Policy Type",
        },
        {
            fieldname: "insurance_provider",
            label: __("Insurance Provider"),
            fieldtype: "Link",
            options: "Insurance Provider",
        },
        {
            fieldname: "customer",
            label: __("Customer"),
            fieldtype: "Link",
            options: "Customer",
        },
        {
            fieldname: "agent",
            label: __("Agent"),
            fieldtype: "Link",
            options: "Agent",
        },
        {
            fieldname: "from_date",
            label: __("Start Date From"),
            fieldtype: "Date",
        },
        {
            fieldname: "to_date",
            label: __("End Date To"),
            fieldtype: "Date",
        },
        {
            fieldname: "payment_status",
            label: __("Payment Status"),
            fieldtype: "Select",
            options: "\nUp to Date\nDue\nOverdue\nDefault",
        },
    ],
};
