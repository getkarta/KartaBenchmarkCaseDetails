# summarize_returns()

[![](https://img.shields.io/badge/type-read-green)](https://img.shields.io/badge/type-read-green) 
[![](https://img.shields.io/badge/Return%20Schema-Mixed-orange)](https://img.shields.io/badge/Return%20Schema-Mixed-orange)

## Tool Class

This is a **domain specific** tool and is used to summarize return details in an ecommerce context. It combines the details of multiple returns and returns a summary of the return details including the details of each item returned and the current return status.

## Tool Function

Given a list of `return_ids` this tool returns a summary of the return details including the details of each item returned.

## Caveats

If some return ids are not found, the tool will return an error message for the corresponding return id. Remember that the input is a list of return ids.

## Usage Example

```python-repl
summarized_returns = summarize_returns(return_ids=['RET001001', 'RET001002'])
```
