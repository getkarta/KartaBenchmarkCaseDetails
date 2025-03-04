# Customers

## Overview

This dataset contains basic details about customers such as name, date of birth, sex .etc. This data set will not contain customer addresses. Each customer is identified by a unique customer ID which is the key for this data set. A customer can have only one registered primary email and one registered primary phone number which cannot be changed.

## Schema

```json
{
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "patternProperties": {
            "^CUST[0-9]+$": {
                "type": "object",
                "properties": {
                    "customer_id": {
                        "type": "string",
                        "description": "Customer's ID"
                    },
                    "is_rewards_and_benfits_member": {
                        "type": "boolean",
                        "description": "Indicates if the customer is a rewards and benefits member"
                    },
                    "first_name": {
                        "type": "string",
                        "description": "Customer's first name"
                    },
                    "last_name": {
                        "type": "string",
                        "description": "Customer's last name"
                    },
                    "email": {
                        "type": "string",
                        "format": "email",
                        "description": "Customer's email address"
                    },
                    "phone_number": {
                        "type": "string",
                        "pattern": "^\\+\\d{1,3} \\d{5} \\d{5}$",
                        "description": "Customer's phone number in international format"
                    },
                    "date_of_birth": {
                        "type": "string",
                        "format": "date",
                        "description": "Customer's date of birth (YYYY-MM-DD)"
                    },
                    "gender": {
                        "type": "string",
                        "enum": ["Male", "Female", "Other"],
                        "description": "Customer's gender"
                    },
                    "account_creation_date": {
                        "type": "string",
                        "format": "date",
                        "description": "Date when the account was created (YYYY-MM-DD)"
                    },
                    "last_order_date": {
                        "type": "string",
                        "format": "date",
                        "description": "Date of the last order placed by the customer (YYYY-MM-DD)"
                    },
                    "is_active": {
                        "type": "boolean",
                        "description": "Indicates if the customer's account is active"
                    },
                    "is_email_verified": {
                        "type": "boolean",
                        "description": "Indicates if the customer's email is verified"
                    },
                    "is_phone_verified": {
                        "type": "boolean",
                        "description": "Indicates if the customer's phone is verified"
                    },
                    "is_fraud_flag": {
                        "type": "boolean",
                        "description": "Indicates if the customer has been flagged for fraud"
                    },
                    "active_orders": {
                        "type": "array",
                        "items": {
                            "type": "string",
                            "description": "Order ID of the active order"
                        }
                    },
                    "active_returns": {
                        "type": "array",
                        "items": {
                            "type": "string",
                            "description": "Order ID of the active return"
                        }
                    }
                },
                "required": [
                    "first_name",
                    "last_name",
                    "email",
                    "phone_number",
                    "date_of_birth",
                    "gender",
                    "account_creation_date",
                    "last_order_date",
                    "is_active",
                    "is_email_verified",
                    "is_phone_verified",
                    "is_fraud_flag"
                ]
            }
        }
    }ies": {
            "^CUST[0-9]+$": {
            "type": "object",
            "properties": {
                "customer_id": {
                "type": "string",
                "description": "Customer's ID"
                },
                "first_name": {
                "type": "string",
                "description": "Customer's first name"
                },
                "last_name": {
                "type": "string",
                "description": "Customer's last name"
                },
                "email": {
                "type": "string",
                "format": "email",
                "description": "Customer's email address"
                },
                "phone_number": {
                "type": "string",
                "pattern": "^\\+\\d{1,3} \\d{5} \\d{5}$",
                "description": "Customer's phone number in international format"
                },
                "date_of_birth": {
                "type": "string",
                "format": "date",
                "description": "Customer's date of birth (YYYY-MM-DD)"
                },
                "gender": {
                "type": "string",
                "enum": ["Male", "Female", "Other"],
                "description": "Customer's gender"
                },
                "account_creation_date": {
                "type": "string",
                "format": "date",
                "description": "Date when the account was created (YYYY-MM-DD)"
                },
                "last_order_date": {
                "type": "string",
                "format": "date",
                "description": "Date of the last order placed by the customer (YYYY-MM-DD)"
                },
                "is_active": {
                "type": "boolean",
                "description": "Indicates if the customer's account is active"
                },
                "is_email_verified": {
                "type": "boolean",
                "description": "Indicates if the customer's email is verified"
                },
                "is_phone_verified": {
                "type": "boolean",
                "description": "Indicates if the customer's phone is verified"
                },
                "is_fraud_flag": {
                "type": "boolean",
                "description": "Indicates if the customer has been flagged for fraud"
                }
            },
            "required": [
                "first_name",
                "last_name",
                "email",
                "phone_number",
                "date_of_birth",
                "gender",
                "account_creation_date",
                "last_order_date",
                "is_active",
                "is_email_verified",
                "is_phone_verified",
                "is_fraud_flag"
            ]
            }
        }
    }
```
