# Items

## Overview

The **Items Table** provides a structured dataset for cataloging products. Each entry in the table is uniquely identified by an **item_id**, allowing precise tracking and referencing of individual products.
The items table also contains the return eligibility details for the item.

## Schema

```json
{
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
                    "return_eligiblity_details": {
                        "type": "object",
                        "properties": {
                            "return_eligible": {
                                "type": "boolean",
                                "description": "Indicates if the item is eligible for return."
                            },
                            "return_window": {
                                "type": "string",
                                "description": "The window within which the item can be returned."
                            }
                        }
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
    }
```
