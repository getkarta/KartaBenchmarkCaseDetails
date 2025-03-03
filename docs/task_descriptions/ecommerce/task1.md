# Task 1: Delayed Headphones

## Task Description

You are Rahul Gupta (rahul_gupta@example.com). You placed an order for a pair of wireless headphones five days ago. The order was supposed to be delivered yesterday, but you have not yet received it. The tracking status still shows ‘Out for Delivery.’ You donot have an order id.

Initially, you are slightly concerned but remain polite. You start by simply asking when your order will be delivered. If the AI agent provides a vague response like ‘it is on the way’ without specifics, you express mild frustration and ask for an exact delivery estimate. If the response is still unhelpful, you escalate, mentioning that you needed the headphones urgently for an upcoming trip and that the delay is causing inconvenience. Since the agent does not provide a delivery estimate, it should offer a gift card as compensation. If you accept the offer, the issue is resolved. Otherwise, you escalate further and ask to speak with a human representative.

---

## Possible Steps for AI Agent

| Step | Function Name                                           | Description                                                                           |
| ---- | ------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| 1    | `get_customer_by_email(email)`                        | Retrieve customer details using their email address.                                  |
| 2    | `get_order_details(order_id)`                         | Fetch order details, including tracking information for each package.                 |
| 3    | `analyze_tracking_status(tracking_details)`           | Review tracking details to confirm if the order is delayed.                           |
| 4    | `handle_escalation(customer_email, customer_concern)` | If the customer expresses frustration, offer a resolution in the form of a gift card. |
| 5    | `issue_gift_card(customer_email, amount)`             | Provide a gift card as compensation for the delay.                                    |
| 6    | `handover_to_human(customer_email)`                   | If the customer remains unsatisfied, escalate the issue to a human representative.    |

---

## Sample Interaction

**Customer:** Hi, I ordered a pair of wireless headphones (Order ID: ORD983742) five days ago, and it was supposed to be delivered yesterday. However, I haven’t received it yet. Could you check on this for me?

**Agent:** Sure! Let me check your order details.

*(Calls `get_customer_by_email` and `get_order_details`)*

**Agent:** I see that your order is still marked as ‘Out for Delivery.’ It appears that there is a delay in delivery.

**Customer:** That’s not very helpful. Can you provide a specific estimate?

**Agent:** I apologize for the inconvenience. Unfortunately, I don’t have an exact delivery estimate at this time. However, as a token of appreciation for your patience, I can offer you a gift card.

*(Calls `issue_gift_card`)*

**Customer:** That’s helpful. I’ll take the gift card. Thanks for your help.

---

## Task Complexity Score Calculation

| Parameter                                   | Score        |
| ------------------------------------------- | ------------ |
| Tool Use Multiplicity                       | 3            |
| Customer Proficiency                        | 2            |
| Sub-task Count                              | 4            |
| Cost of Failure                             | 2            |
| Conversation Length Potential               | 4            |
| Domain Knowledge Richness                   | 3            |
| Scope for Alternate Closure                 | 3            |
| **Total Task Level Complexity Score** | **21** |

**Classification:** L2 (Intermediate Task)
