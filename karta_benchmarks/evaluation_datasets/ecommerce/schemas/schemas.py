SCHEMAS = {
    "customers": {
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
    },
    "orders": {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "patternProperties": {
            "^[a-zA-Z0-9_-]+$": {
                "type": "object",
                "properties": {
                    "order_id": {
                        "type": "string",
                        "description": "Unique identifier for the order. This is also the key."
                    },
                    "order_date": {
                        "type": "string",
                        "format": "date",
                        "description": "Date when the order was placed (YYYY-MM-DD)"
                    },
                    "customer_id": {
                        "type": "string",
                        "description": "Unique identifier for the customer placing the order."
                    },
                    "payment_status": {
                        "type": "string",
                        "enum": ["SUCCESS", "FAILED", "PENDING"],
                        "description": "Status of the payment for the order."
                    },
                    "shipping_address": {
                        "type": "object",
                        "properties": {
                            "address_1": {
                                "type": "string",
                                "description": "Primary address line."
                            },
                            "address_2": {
                                "type": "string",
                                "description": "Secondary address line."
                            },
                            "address_3": {
                                "type": "string",
                                "description": "Tertiary address line."
                            },
                            "postal_code": {
                                "type": "string",
                                "description": "Postal or ZIP code of the address."
                            },
                            "contact_number": {
                                "type": "string",
                                "description": "Phone number for delivery contact."
                            }
                        },
                        "required": ["address_1", "pin_code", "contact_number"]
                    },
                    "items_ordered": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "item_number": {
                                    "type": "string",
                                    "description": "Unique identifier for the item."
                                },
                                "qty": {
                                    "type": "integer",
                                    "description": "Quantity of the item ordered.",
                                    "minimum": 1
                                },
                                "promised_delivery_date": {
                                    "type": "string",
                                    "format": "date",
                                    "description": "Date when the item is promised to be delivered."
                                },
                                "item_original_cost": {
                                    "type": "number",
                                    "description": "Cost of the item."
                                },
                                "applied_discount": {
                                    "type": "number",
                                    "description": "Discount applied to the item as a fraction of the item cost."
                                },
                                "item_final_cost": {
                                    "type": "number",
                                    "description": "Final cost of the item after applying the discount."
                                },
                                "package_id": {
                                    "type": "string",
                                    "description": "Unique identifier for the package. Is not present then the item has not shipped yet."
                                }
                            },
                            "required": ["item_number", "qty"]
                        }
                    },
                    "payment_method": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "payment_method_id": {
                                    "type": "string",
                                    "description": "Unique identifier for the payment method."
                                },
                                "type": {
                                    "type": "string",
                                    "enum": ["CREDIT_CARD", "COD", "GIFT_CARD"],
                                    "description": "Type of payment method used."
                                },
                                "amount_paid": {
                                    "type": "number",
                                    "description": "Amount paid using this payment method.",
                                    "minimum": 0
                                }
                            },
                            "required": ["payment_method_id", "type", "amount_paid"]
                        }
                    }
                },
                "required": ["order_id", "customer_id", "shipping_address", "items_ordered", "payment_method"]
            }
        }
    },
    "payment_methods": {
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
    },
    "packages": {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "patternProperties": {
            "^[a-zA-Z0-9_-]+$": {
                "type": "object",
                "properties": {
                    "destination_address": {
                        "type": "object",
                        "properties": {
                            "address_1": {
                                "type": "string",
                                "description": "Primary address line."
                            },
                            "address_2": {
                                "type": "string",
                                "description": "Secondary address line."
                            },
                            "address_3": {
                                "type": "string",
                                "description": "Tertiary address line."
                            },
                            "postal_code": {
                                "type": "string",
                                "description": "Postal or ZIP code."
                            },
                            "contact_number": {
                                "type": "string",
                                "description": "Phone number for delivery contact."
                            }
                        },
                        "required": ["address_1", "postal_code", "contact_number"]
                    },
                    "type": {
                        "type": "string",
                        "enum": ["ORDER_DELIVERY", "RETURN"],
                        "description": "Specifies whether this package is for order delivery or return."
                    },
                    "shipper_name": {
                        "type": "string",
                        "description": "Name of the shipping carrier handling the package."
                    },
                    "origin_code": {
                        "type": "string",
                        "description": "Code representing the origin location of the package."
                    },
                    "current_status": {
                        "type": "string",
                        "enum": [
                            "AT_WAREHOUSE", "IN_TRANSIT", "AT_DELIVERY_STATION", "OUT_FOR_DELIVERY", "DELIVERED", "DELIVERY_FAILURE", "RETURN_PICKEDUP",
                            "RETURN_COMPLETED"
                        ],
                        "description": "The current status of the package."
                    },
                    "estimated_delivery_date": {
                        "type": "string",
                        "format": "date-time",
                        "description": "Estimated delivery date and time of the package."
                    },
                    "tracking_details": {
                        "type": "object",
                        "patternProperties": {
                            "^[0-9TZ:.+-]+$": {
                                "type": "object",
                                "properties": {
                                    "event": {
                                        "type": "string",
                                        "enum": ["DESPATCHED", "RECEIVED", "DELIVERY FAILED"],
                                        "description": "Tracking event type."
                                    },
                                    "location_code": {
                                        "type": "string",
                                        "description": "Code representing the package location.",
                                        "nullable": True
                                    },
                                    "location_type": {
                                        "type": "string",
                                        "enum": ["WAREHOUSE", "COURIER FACILITY", "SORT CENTER", "DELIVERY STATION", "FINAL DESTINATION"],
                                        "description": "Type of location where the event occurred."
                                    }
                                },
                                "required": ["event", "location_type"]
                            }
                        },
                        "description": "A timestamp-based mapping of tracking events with their location details."
                    }
                },
                "required": ["destination_address", "shipper_name", "origin_code", "tracking_details", "current_status"]
            }
        }
    },
    "items": {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "patternProperties": {
            "^[a-zA-Z0-9_-]+$": {
                "type": "object",
                "properties": {
                    "seller_id": {
                        "type": "string",
                        "description": "Unique identifier for the seller."
                    },
                    "item_description": {
                        "type": "string",
                        "description": "Detailed description of the item."
                    },
                    "item_weight": {
                        "type": "number",
                        "description": "Weight of the item in kilograms.",
                        "minimum": 0
                    },
                    "item_cost": {
                        "type": "number",
                        "description": "Cost of the item in the applicable currency.",
                        "minimum": 0
                    },
                    "restricted_zip_codes": {
                        "type": "array",
                        "items": {
                            "type": "string",
                            "description": "ZIP codes where the item cannot be shipped."
                        },
                        "description": "List of restricted ZIP codes for delivery."
                    },
                    "item_category": {
                        "type": "string",
                        "description": "Category of the item (e.g., electronics, apparel, home goods)."
                    },
                    "item_specifications": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "property_name": {
                                    "type": "string",
                                    "description": "Name of the specification."
                                },
                                "property_value": {
                                    "type": "string",
                                    "description": "Value of the specification."
                                }
                            }
                        }
                    }
                },
                "required": ["item_description", "item_weight", "item_cost", "item_category"]
            }
        }
    },

    "contacts" : {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "patternProperties": {
            "^[a-zA-Z0-9_-]+$": {
            "type": "object",
            "properties": {
                "customer_id": {
                "type": "string",
                "description": "Unique identifier for the customer who initiated the contact."
                },
                "contact_source": {
                "type": "string",
                "enum": ["CHATBOT", "EMAIL", "PHONE", "WEB_FORM"],
                "description": "The source through which the contact was initiated before being transferred to a human representative."
                },
                "summary" : {
                    "type": "string",
                    "description": "A summary of the issues raised by the customer."
                }
            },
            "required": ["customer_id", "contact_source", "summary"]
            }
        }
    }
}