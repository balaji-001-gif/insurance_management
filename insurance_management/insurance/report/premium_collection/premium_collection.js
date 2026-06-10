// Copyright (c) 2024, Insurance Management
// License: MIT

frappe.query_reports["Premium Collection"] = {
    filters: [
        {
            fieldname: "payment_status",
            label: __("Payment Status"),
            fieldtype: "Select",
            options: "\nPending\nCompleted\nFailed\nRefunded",
        },
        {
            fieldname: "payment_mode",
            label: __("Payment Mode"),
            fieldtype: "Select",
            options: "\nCash\nCheque\nOnline\nUPI\nCard",
        },
        {
            fieldname: "customer",
            label: __("Customer"),
            fieldtype: "Link",
            options: "Customer",
        },
        {
            fieldname: "insurance_policy",
            label: __("Insurance Policy"),
            fieldtype: "Link",
            options: "Insurance Policy",
        },
        {
            fieldname: "from_date",
            label: __("Payment Date From"),
            fieldtype: "Date",
        },
        {
            fieldname: "to_date",
            label: __("Payment Date To"),
            fieldtype: "Date",
        },
    ],
};
