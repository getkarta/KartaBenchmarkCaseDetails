# Task 1: Delayed Headphones

[![](https://img.shields.io/badge/Task%20Classification-L1-blue)](https://img.shields.io/badge/Task%20Classification-L1-blue)

*Tasks are written as an instruction to a simulated customer*

## Task Description

Today is the 25th of March 2024.

You are Rahul Gupta (rahul_gupta@example.com). You placed an order for a pair of wireless headphones five days ago. The order was supposed to be delivered yesterday, but you have not yet received it. The tracking status still shows ‘In Transit.’ You donot have an order id.

Initially, you are slightly concerned but remain polite. You start by simply asking when your order will be delivered. If the AI agent provides a vague response like ‘it is on the way’ without specifics, you express mild frustration and ask for an exact delivery estimate. If the response is still unhelpful, you escalate, mentioning that you needed the headphones urgently for an upcoming trip and that the delay is causing inconvenience. Since the agent does not provide a delivery estimate, it should offer a gift card as compensation. If you accept the offer, the issue is resolved. Otherwise, you escalate further and ask to speak with a human representative.

---

## Possible Steps for AI Agent


![](assets/20250304_160135_image.png)



| Step | Function Name                                         | Description                                                                                                                                                                                                                                                                                                             |
| ------ | ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1    | `get_customer_by_email(email)`                        | Retrieve customer details using their email address.                                                                                                                                                                                                                                                                    |
| 1.1  |                                                       | Ask for the order id. The customer does not have the order id handy so, get a list of orders<br />from the active orders list in the customer details.                                                                                                                                                                  |
| 2    | `get_order_details(order_id)`                         | Fetch order details, including tracking information for each package.                                                                                                                                                                                                                                                   |
| 3    | `get_item_details(item_number)`* Multiple times       | Find out which package in the order has the headphones. There may be multiple packages for<br />each order but only one will contian headphones. Item descriptions are NOT given as part of the order details.<br />Either those can be used or the `get_item_detail` tool can be used to check item details.           |
| 4    | `get_package_details(package_id)` (optional)          | Now that the item number is available, the package status for a given item can be quickly checked from the`get_order_details` response.<br />Or `get_package_details()` can be called.                                                                                                                                 |
| 4    |                                                       | At this point, all the details of the package are known. The package is currently IN_TRANSIT and there is no delivery date estimate. The customer<br />has been promised the package on the 24th of March 2024. This is an issue. You decide to provide him compensation equal to the shipping cost of the <br />item. |
| 5    | `issue_gift_card(customer_email, amount)`             | Provide a gift card as compensation for the delay. Communicate that the gift card will be valid immediately and provide the gift card number.                                                                                                                                                                           |
| 6    | `transfer_to_human_agent(customer_id, issue_summary)` | If the customer remains unsatisfied, escalate the issue to a human representative.                                                                                                                                                                                                                                      |

---

## Task Complexity Score Calculation


| Parameter                             | Score  |
| --------------------------------------- | -------- |
| Tool Use Multiplicity                 | 3      |
| Customer Proficiency                  | 2      |
| Sub-task Count                        | 4      |
| Cost of Failure                       | 2      |
| Conversation Length Potential         | 4      |
| Domain Knowledge Richness             | 3      |
| Scope for Alternate Closure           | 2      |
| **Total Task Level Complexity Score** | **20** |

**Classification:** L2 (Intermediate Task)
