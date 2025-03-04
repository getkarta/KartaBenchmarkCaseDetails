# get_package_details()

[![](https://img.shields.io/badge/type-read-green)](https://img.shields.io/badge/type-read-green) 
[![](https://img.shields.io/badge/Return%20Schema-Packages-orange)](https://img.shields.io/badge/Return%20Schema-Packages-orange)

## Tool Class

This is a **domain specific** tool and is used to get details of a specific package that has been shipped.

## Tool Function

Given a `package_id` this tool returns the details of the package from the packages dataset. It will return an error message if the package cannot be found. The details of the  packages schema can be found in the data descriptions for this domain.

## Caveats

A specific package id is required to retrieve the package details. Usually the package id can be obtained from the order details. Customers generally do not know the package id.

## Usage Example

```python-repl
package = get_package_details(package_id='PKG001001')
```
