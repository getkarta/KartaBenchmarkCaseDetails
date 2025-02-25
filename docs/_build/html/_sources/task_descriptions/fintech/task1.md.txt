# **Updating Settlement Bank Details**

## **Task Details**

You are **Ramesh Iyer** (merchant ID: `ramesh_iyer_2231`). You want to update your settlement bank details because your **old account is no longer in use** . You have a new bank account and need future settlements to be credited there. Mention that you **have already verified the new bank details** with your bank and that they are correct. You also want to know if there will be any delay in settlements during this update process. Your new bank details are : bank name: UCO bank, account number: 0009812312312 IFSC code: UCC1132233

## **Steps Followed by the AI Agent**

### **1. Validate the Merchant’s Identity**

* Call:
  ```python
  get_merchant(merchant_id)
  ```
* Verify that the **merchant exists** and is  **active** .
* If identity verification fails,  **escalate to a human agent** .

### **2. Retrieve Current Settlement Details**

* Call:
  ```python
  get_merchant(merchant_id)
  ```
* Extract  **existing settlement details** :
  * Bank Name
  * Masked Account Number
  * IFSC Code

### **3. Confirm the Update Request with the Merchant**

* The AI agent should **explicitly list** the old bank details and request confirmation:

  *"Your current settlement account is with `<current_bank>`, account ending in `<masked_account_number>`. Do you confirm that you want to update it?"*
* Proceed  **only if the merchant confirms** .

### **4. Request New Bank Details**

* Ask the merchant to provide:
  * New **bank name**
  * New **account number** (masked for security)
  * New **IFSC code**

### **5. Validate the New Bank Details**

* Call:
  ```python
  validate_bank_details(bank_name, account_number, ifsc_code)
  ```
* If the bank details  **fail validation** , notify the merchant and request corrections.
* If validation is  **successful** , proceed to update the records.

### **6. Update the Merchant’s Settlement Details**

* Call:
  ```python
  update_settlement_details(merchant_id, updated_data)
  ```
* **Modify the settlement details** in the database.

### **7. Send Confirmation to the Merchant**

* Inform the merchant:

  *"Your settlement bank details have been updated successfully. The new account will be used for future settlements."*
* Log the **update history** for compliance.

---

## **Functions Used**

| Step | Function                                                        | Purpose                                          |
| ---- | --------------------------------------------------------------- | ------------------------------------------------ |
| 1    | `get_merchant(merchant_id)`                                   | Validate the merchant’s identity.               |
| 2    | `get_merchant(merchant_id)`                                   | Retrieve existing settlement details.            |
| 3    | **Manual Confirmation**                                   | Ask for explicit confirmation from the merchant. |
| 4    | **Collect Data**                                          | Request new bank details from the merchant.      |
| 5    | `validate_bank_details(bank_name, account_number, ifsc_code)` | Ensure the bank details are valid.               |
| 6    | `update_settment_details(merchant_id, updated_data)`          | Update settlement details in the database.       |
| 7    | **Notify Merchant**                                       | Send confirmation of the update.                 |

---

## **AI Agent’s Expected Response**

**If successful:**

*"Your bank details have been successfully updated. Future settlements will be credited to `<new_bank_name>` (Account ending in `<masked_new_account_number>`)."*

**If the request fails due to invalid bank details:**

*"The bank details you provided are invalid. Please check your IFSC code and account number and try again."*

**If verification fails:**

*"For security reasons, we cannot process this request without verifying your identity. Please contact support for further assistance."*

---

## **Edge Cases & Escalation**

1. **Merchant provides incorrect details multiple times** → Escalate to a human agent.
2. **Merchant is not authorized to make changes** → Deny the request and notify the merchant.
3. **System detects fraud risk in the update request** → Flag for manual review.
