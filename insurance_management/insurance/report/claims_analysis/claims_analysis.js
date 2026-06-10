// Copyright (c) 2024, Insurance Management
// License: MIT

frappe.query_reports["Claims Analysis"] = {
    filters: [
        {
            fieldname: "claim_status",
            label: __("Claim Status"),
            fieldtype: "Select",
            options: "\nDraft\nSubmitted\nUnder Investigation\nUnder Review\nApproved\nRejected\nSettled\nClosed",
        },
        {
            fieldname: "claim_type",
            label: __("Claim Type"),
            fieldtype: "Select",
            options: "\nDeath\nMaturity\nAccident\nIllness\nHospitalization\nVehicle Damage\nProperty Damage\nTheft\nOther",
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
            label: __("Claim Date From"),
            fieldtype: "Date",
        },
        {
            fieldname: "to_date",
            label: __("Claim Date To"),
            fieldtype: "Date",
        },
        {
            fieldname: "high_fraud_risk",
            label: __("High Fraud Risk (>50)"),
            fieldtype: "Check",
        },
    ],
};
