# calculate_date_difference()

## Tool Class

This is a **generic** tool and can be used for some general computational requirements by the agent.

## Tool Function

Given a date `date1` and a `date2` as string, this tool returns the difference in days between these two dates.

## Caveats

This tool can return a negative integer if the start date is later than the end date. The agent using the tool has to decipher the output and use it accordingly

## Usage Example

```python-repl
days_between_dates = calculate_date_difference(
	date1='2025-01-01',
	date2='2025-01-03'
)
print(days_between_dates)
# Will return: 1
```
