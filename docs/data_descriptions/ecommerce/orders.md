# Orders

## Overview

The **Order Table Schema** defines the structure of order records within the system. Each order is uniquely identified by an `order_id`, which also serves as the primary key. The schema includes details such as:

* **Customer Information** : Each order is linked to a `customer_id`.
* **Shipping Address** : A nested object that captures the shipping address details, including `address_1`, `address_2`, `address_3`, `pin_code`, and `contact_number`.
* **Items Ordered** : A list of items in the order, where each item includes an `item_number` and `qty` (quantity ordered).
* **Payment Method** : A list of payment methods used for the order. Each payment entry consists of a `payment_method_id`, `type` (which can be `CREDIT_CARD`, `COD`, or `GIFT_CARD`), and `amount_paid`.
* **Payment Status** : The status of the payment for the order can be one of `SUCCESS`, `FAILED`, or `PENDING`.
* **Associated Returns** : A list of return IDs associated with the order.

## Schema

```json
{
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
                    "enum": [
                        "SUCCESS",
                        "FAILED",
                        "PENDING"
                    ],
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
                    "required": [
                        "address_1",
                        "pin_code",
                        "contact_number"
                    ]
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
                        "required": [
                            "item_number",
                            "qty"
                        ]
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
                                "enum": [
                                    "CREDIT_CARD",
                                    "COD",
                                    "GIFT_CARD"
                                ],
                                "description": "Type of payment method used."
                            },
                            "amount_paid": {
                                "type": "number",
                                "description": "Amount paid using this payment method.",
                                "minimum": 0
                            }
                        },
                        "required": [
                            "payment_method_id",
                            "type",
                            "amount_paid"
                        ]
                    }
                }
            },
            "associated_returns": {
                "type": "array",
                "items": {
                    "type": "string",
                    "description": "Unique identifier for the return."
                }
            },
            "required": [
                "order_id",
                "customer_id",
                "shipping_address",
                "items_ordered",
                "payment_method",
                "associated_returns"
            ]
        }
    }
}
```
