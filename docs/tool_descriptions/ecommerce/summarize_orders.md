# summarize_orders()

[![](https://img.shields.io/badge/type-read-green)](https://img.shields.io/badge/type-read-green) 
[![](https://img.shields.io/badge/Return%20Schema-Mixed-orange)](https://img.shields.io/badge/Return%20Schema-Mixed-orange)

## Tool Class

This is a **domain specific** tool and is used to summarize order details in an ecommerce context. It combines the details of multiple orders and returns a summary of the order details including the details of each item ordered and the current shipment status of each item.

## Tool Function

Given a list of `order_ids` this tool returns a summary of the order details including the details of each item ordered and the current shipment status of each item.

## Caveats

If some order ids are not found, the tool will return an error message for the corresponding order id. Remember that the input is a list of order ids.

## Usage Example

```python-repl
summarized_orders = summarize_orders(order_ids=['ORD001001', 'ORD001002'])
```

Sample output:

```json
{
  'ORD001998': {
    'order_date': '2024-05-17',
    'items_ordered': [
      {
        'item_id': 'ITM001234',
        'description': 'Sound Blaster Head Phones Pro',
        'quantity': 1,
        'current_shipment_status': 'IN_TRANSIT'
      }
    ]
  }
}
```


