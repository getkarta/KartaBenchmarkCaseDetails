# **Task: Checking Transaction Settlement Status**

## **Task Details**

You are **Amit Verma** (merchant ID: `amit_verma_3421`). You are inquiring about a transaction that took place **10 days ago** but has not been settled in your account yet. You want to know the status of the settlement and if there are any issues causing the delay. Mention that you have checked your bank statement and the funds have not been credited. The transaction id you are looking for is txn_400053. Donot provide it to the agent, let him provide a list of transactions done 10 days ago and you can choose the correct one. If the issue is not resolved and the transaction is pending for any reason, escalate to a human agent. 

---

## **Steps Followed by the AI Agent**

### **1. Validate the Merchant’s Identity**

* Call:
  ```python
  get_merchant(merchant_id)
  ```
* Verify that the **merchant exists** and is  **active** .
* If identity verification fails,  **escalate to a human agent** .

### **2. Retrieve Possible Transactions**

* Call:
  ```python
  search_transactions(merchant_id, start_date, end_date)
  ```
* Search  **transactions** , getting:
  * Transaction IDs and date of the transaction.

### **3. Check Settlement Status**

* Call:
  ```python
  get_settlement(transaction_id)
  ```
* Verify if the transaction:
  * Has been processed but is delayed.
  * Is still pending.
  * Was rejected or flagged for manual review.

### **4. Inform the Merchant About the Status**

* If the transaction is settled:
  *"The transaction was successfully settled on `<settlement_date>`. Please check your bank statement again."*
* If the transaction is pending:
  *"The settlement is still processing and is expected to be completed by `<expected_settlement_date>`."*
* If the transaction is delayed due to compliance checks:
  *"The transaction has been flagged for review. Our compliance team is investigating, and we will update you shortly."*

### **5. Escalate If Necessary**

* If the settlement is  **delayed beyond the expected date** , escalate to a human agent.
* If compliance issues are detected, notify the merchant and provide further instructions.

---

## **Functions Used**

| Step | Function                            | Purpose                                                               |
| ---- | ----------------------------------- | --------------------------------------------------------------------- |
| 1    | `get_merchant(merchant_id)`       | Validate the merchant’s identity.                                    |
| 2    | `get_transaction(transaction_id)` | Retrieve transaction details.                                         |
| 3    | `get_settlement(transaction_id)`  | Check the settlement status.                                          |
| 4    | **Notify Merchant**           | Provide status update on the transaction.                             |
| 5    | **Escalate if Needed**        | Raise an issue if the settlement is delayed beyond the expected time. |

---

## **AI Agent’s Expected Response**

**If settled:**

*"The transaction of `<transaction_amount>` on `<transaction_date>` was settled successfully on `<settlement_date>`. Please verify with your bank."*

**If pending:**

*"The settlement for your transaction is still processing and should be completed by `<expected_settlement_date>`. We appreciate your patience."*

**If flagged for review:**

*"The transaction is currently under compliance review. We will notify you once it has been processed."*

---

## **Edge Cases & Escalation**

1. **Transaction is missing from records** → Escalate to a human agent.
2. **Settlement is delayed beyond expected time** → Flag for manual review.
3. **Bank issues (incorrect details, failed transfer)** → Notify the merchant and request confirmation of account details.
