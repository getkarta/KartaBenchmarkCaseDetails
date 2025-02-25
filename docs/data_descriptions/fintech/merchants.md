# **Merchant Data**

## **Overview**

This dataset contains information about merchants who use the payment gateway for processing transactions. It includes details about the merchant's **business, domain verification status, compliance status, and settlement details**.

This collection maintains **merchant-specific details**, including business information, domain verification status, and settlement details.

### **Schema**

```json
{
  "_id": "<merchant_id>",
  "name": "<merchant_business_name>",
  "email": "<merchant_email>",
  "phone": "<merchant_phone>",
  "created_at": "<timestamp_of_creation>",
  "business_type": "<business_category>",
  "status": "<merchant_status>",
  "domain": {
    "url": "<merchant_domain>",
    "verification_status": "<verification_status>",  
    "verified_on": "<verification_timestamp>",
    "category": "<business_category>",
    "govt_category_code": "<govt_category_code>",
    "compliance_status": "<compliance_status>",
    "compliance_issues": [
      {
        "issue_id": "<compliance_issue_id>",
        "description": "<compliance_issue_description>",
        "severity": "<issue_severity>",
        "resolution_status": "<resolution_status>"
      }
    ]
  },
  "settlement_details": {
    "settlement_account_id": "<settlement_account_id>",
    "bank_name": "<bank_name>",
    "account_number": "<masked_account_number>",
    "IFSC_Code": "<ifsc_code>"
  }
}
```
