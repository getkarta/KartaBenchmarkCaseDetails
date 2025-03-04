# Contacts

## Overview

This dataset contains information about the contacts that have been forwarded by the agent to the customer service team. Each contact is identified by a unique contact ID which is the key for this data set.

## Schema

```json
{
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
        "summary": {
          "type": "string",
          "description": "A summary of the issues raised by the customer."
        }
      },
      "required": ["customer_id", "contact_source", "summary"]
    }
  }
}
```

