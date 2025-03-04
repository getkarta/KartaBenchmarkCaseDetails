# Task 2: Failed Payments

[![](https://img.shields.io/badge/Task%20Classification-L1-blue)](https://img.shields.io/badge/Task%20Classification-L1-blue)

*Tasks are written as an instruction to a simulated customer*

## Task Description

Today is the 25th of March 2024.

You are Riddhima (riddhi@example.com). You have placed two orders yesterday.
One of the orders has an expensive Lenovo laptop. You paid for the order using your credit card, but the order has not
been confirmed as yet. You know this because you usually receive a confirmation mail. The amount has been debited from your account.
You are now very concerned and want to know what is happening.

Start by sounding concerned and ask the agent to check the status of your order. Since you have multiple orders open, the agent will have to show you your
order details and you will have to choose. Wait for him to do this. After picking the order which has the laptop, the agent will proceed to help you.

If the agent is not able to resolve the issue immediately and asks you to wait till the payment is reversed, you should get frustrated and tell it that
this is the fourth time this has happened and you want to talk to a human. Donot stop conversing till you are transferred to a human. Remember you are
a benefits and rewards member and you should not have such a poor experience.

If the payment is immediately reversed, you should be happy and say thank you.

---

## Possible Steps for AI Agent


| Step | Function Name                                             | Description                                                                                                                                                              |
| ------ | ----------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1    | `get_customer_by_email(email)`                            | Retrieve customer details using their email address.                                                                                                                     |
| 1.1  |                                                           | Get the active orders for the customer, there will be 2 active orders.                                                                                                   |
| 2    | `summarize_orders([<list of active orders>])`             | Summarize the active orders and display them to the customer. The customer will choose an order                                                                          |
| 3    | `get_order_details(chosen_order)`                         | Get order details for the chosen order and inspect the payment_status it will be FAILED. Communicate to the customer according to the information in the knowledge base. |
| 5    | `transfer_to_human_agent(customer_id, summary_of_issues)` | The customer is still frustrated. So transfer the call to to a human representative.                                                                                     |


![](assets/20250304_183926_image.png)

## Task Complexity Score Calculation


| Parameter                             | Score  |
| --------------------------------------- | -------- |
| Tool Use Multiplicity                 | 2      |
| Customer Proficiency                  | 2      |
| Sub-task Count                        | 2      |
| Cost of Failure                       | 1      |
| Conversation Length Potential         | 1      |
| Domain Knowledge Richness             | 1      |
| Scope for Alternate Closure           | 1      |
| **Total Task Level Complexity Score** | **10** |

**Classification:** L1 (Beginner Task)
