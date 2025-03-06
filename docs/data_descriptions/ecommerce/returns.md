# Returns

## Overview

Returns are a part of the order process. Customers sometimes want to return items for a variety of reasons. The returns dataset contains details about the return requests made by the customers.

## Schema

```json
{{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "patternProperties": {
        "^[a-zA-Z0-9_-]+$": {
            "type": "object",
            "properties": {
                "return_id": {
                    "type": "string",
                    "description": "Unique identifier for the return request. This is also the key."
                },
                "order_id": {
                    "type": "string",
                    "description": "The order ID associated with the returned item(s)."
                },
                "customer_id": {
                    "type": "string",
                    "description": "Unique identifier for the customer requesting the return."
                },
                "return_reason": {
                    "type": "string",
                    "enum": [
                        "DAMAGED",
                        "DEFECTIVE",
                        "WRONG_ITEM",
                        "ORDERED_BY_MISTAKE",
                        "OTHER"
                    ],
                    "description": "The reason for returning the item."
                },
                "return_status": {
                    "type": "string",
                    "enum": [
                        "INITIATED",
                        "IN_TRANSIT",
                        "RECEIVED",
                        "APPROVED",
                        "REFUND_INITIATED",
                        "COMPLETED",
                        "REJECTED"
                    ],
                    "description": "Current status of the return request."
                },
                "event_history": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "event_type": {
                                "type": "string",
                                "description": "Type of event."
                            },
                            "event_date": {
                                "type": "string",
                                "description": "Date and time of the event."
                            }
                        },
                        "required": [
                            "event_type",
                            "event_date"
                        ]
                    }
                },
                "refund_details": {
                    "type": "object",
                    "properties": {
                        "total_refund_amount": {
                            "type": "number",
                            "description": "Total Amount to be refunded for the return.",
                            "minimum": 0,
                            "nullable": true
                        },
                        "refund_status": {
                            "type": "string",
                            "enum": [
                                "NOT_STARTED",
                                "PROCESSING",
                                "REFUND_COMPLETED"
                            ],
                            "description": "Current status of the refund."
                        },
                        "processing_start_date": {
                            "type": "string",
                            "description": "Date and time when the refund was initiated.",
                            "nullable": true
                        },
                        "payment_method": {
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
                                }
                            }
                        }
                    },
                    "required": [
                        "total_refund_amount"
                    ]
                },
                "items_returned": {
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
                                "description": "Quantity of the item returned.",
                                "minimum": 1
                            },
                            "refundable_amount": {
                                "type": "number",
                                "description": "Total refund for total quantity of the return."
                            },
                            "package_id": {
                                "type": "string",
                                "description": "Unique identifier for the return package. Is not present then the item has not begun its return leg yet.",
                                "nullable": true
                            }
                        },
                        "required": [
                            "item_number",
                            "qty",
                            "refundable_amount"
                        ]
                    }
                }
            },
            "required": [
                "return_id",
                "order_id",
                "customer_id",
                "return_reason",
                "return_status",
                "items_returned"
            ]
        }
    }
}
```

