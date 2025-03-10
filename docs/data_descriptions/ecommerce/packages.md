# Packages

## Overview

The Packages table defines the structure for tracking packages within the system. Each package is uniquely identified by a  **package_id** , serving as the key. This schema provides information on the package’s destination, shipper details, origin, and tracking history.

## Schema

```json
{
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
                    "required": [
                        "address_1",
                        "postal_code",
                        "contact_number"
                    ]
                },
                "type": {
                    "type": "string",
                    "enum": [
                        "ORDER_DELIVERY",
                        "RETURN"
                    ],
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
                        "AT_WAREHOUSE",
                        "IN_TRANSIT",
                        "AT_DELIVERY_STATION",
                        "OUT_FOR_DELIVERY",
                        "DELIVERED",
                        "DELIVERY_FAILURE",
                        "RETURN_PICKEDUP",
                        "RETURN_COMPLETED",
                        "RETURN_INITIATED"
                    ],
                    "description": "The current status of the package."
                },
                "estimated_delivery_date": {
                    "type": "string",
                    "format": "date-time",
                    "description": "Estimated delivery date and time of the package."
                },
                "final_delivery_date": {
                    "type": "string",
                    "format": "date-time",
                    "description": "Final delivery date and time of the package."
                },
                "final_return_date": {
                    "type": "string",
                    "format": "date-time",
                    "description": "Final return date and time of the package."
                },
                "pickup_date": {
                    "type": "string",
                    "format": "date-time",
                    "description": "Pickup date and time of the package."
                },
                "shipment_cost": {
                    "type": "number",
                    "description": "Cost of the shipment."
                },
                "tracking_details": {
                    "type": "object",
                    "patternProperties": {
                        "^[0-9TZ:.+-]+$": {
                            "type": "object",
                            "properties": {
                                "event": {
                                    "type": "string",
                                    "enum": [
                                        "DESPATCHED",
                                        "RECEIVED",
                                        "PICKED UP",
                                        "DELIVERY FAILED"
                                    ],
                                    "description": "Tracking event type."
                                },
                                "location_code": {
                                    "type": "string",
                                    "description": "Code representing the package location.",
                                    "nullable": true
                                },
                                "location_type": {
                                    "type": "string",
                                    "enum": [
                                        "WAREHOUSE",
                                        "COURIER FACILITY",
                                        "SORT CENTER",
                                        "DELIVERY STATION",
                                        "FINAL DESTINATION"
                                    ],
                                    "description": "Type of location where the event occurred."
                                }
                            },
                            "required": [
                                "event",
                                "location_type"
                            ]
                        }
                    },
                    "description": "A timestamp-based mapping of tracking events with their location details."
                }
            },
            "required": [
                "destination_address",
                "shipper_name",
                "origin_code",
                "tracking_details",
                "current_status"
            ]
        }
    }
}
```
