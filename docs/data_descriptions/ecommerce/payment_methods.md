# Payment Methods

## Overview

The **Payment Methods Table Schema** defines how payment methods are stored for each customer. The table is keyed by  **customer_id** , ensuring that all payment methods associated with a customer are grouped together. Each payment method is further identified by a  **payment_method_id** , allowing multiple payment methods to be linked to the same customer.

## Schema

```json
{
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "patternProperties": {
            "^[a-zA-Z0-9_-]+$": {
                "type": "object",
                "description": "Payment method associated with a specific customer ID. Each payment method id is associated with a single customer ID.",
                "patternProperties": {
                    "^[a-zA-Z0-9_-]+$": {
                        "type": "object",
                        "properties": {
                            "payment_method_type": {
                                "type": "string",
                                "enum": ["CREDIT_CARD", "COD", "GIFT_CARD"],
                                "description": "Type of payment method."
                            },
                            "identification_number": {
                                "type": "string",
                                "description": "Unique identifier for the payment method. Possibly a credit card number with only last 4 digits visible."
                            },
                            "customer_id": {
                                "type": "string",
                                "description": "Customer ID associated with the payment method."
                            },
                            "amount_remaining": {
                                "type": "number",
                                "description": "Remaining balance on the payment method (applicable for GIFT_CARD).",
                                "minimum": 0,
                                "nullable": True
                            },
                            "expiry_date": {
                                "type": "string",
                                "format": "date",
                                "description": "Expiry date of the payment method, if applicable.",
                                "nullable": True
                            },
                            "billing_address": {
                                "type": "object",
                                "description": "Billing address associated with the payment method.",
                                "properties": {
                                    "address_1": {
                                        "type": "string",
                                        "description": "Primary address line.",
                                        "nullable": True
                                    },
                                    "address_2": {
                                        "type": "string",
                                        "description": "Secondary address line.",
                                        "nullable": True
                                    },
                                    "address_3": {
                                        "type": "string",
                                        "description": "Tertiary address line.",
                                        "nullable": True
                                    },
                                    "postal_code": {
                                        "type": "string",
                                        "description": "Postal or ZIP code.",
                                        "nullable": True
                                    }
                                },
                                "nullable": True
                            }
                        },
                        "required": ["payment_method_type"]
                    }
                }
            }
        }
    }
```
