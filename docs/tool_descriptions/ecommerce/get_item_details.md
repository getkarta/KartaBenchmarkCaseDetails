# get_item_details()

[![](https://img.shields.io/badge/type-read-green)](https://img.shields.io/badge/type-read-green) 
[![](https://img.shields.io/badge/Return%20Schema-Items-orange)](https://img.shields.io/badge/Return%20Schema-Items-orange)

## Tool Class

This is a **domain specific** tool and is used to get details of a specific item being sold in the ecommerce domain.

## Tool Function

Given a `item_id` this tool returns the details of the item from the items dataset. It will return an error message if the item cannot be found. The details of the  items schema can be found in the data descriptions for this domain.

## Caveats

A specific item id is required to retrieve the item details. Ask the customer for the item id if you do not have it. Donot search for the item id by looking at the item name.

## Usage Example

```python-repl
item = get_item_details(item_id='ITEM001001')
```
