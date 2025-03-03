## The current Context

The present date is 20-Feb-2025.

## Package Movement: From Warehouse to Customer

Packages move through a series of locations before reaching the final customer. The package tracking system records each transition through **tracking_details**, which logs events as the package progresses.

### **Stages of Package Movement**

1. **At Warehouse (WAREHOUSE)**
   * The package starts at the warehouse, where it is stored and prepared for dispatch.
   * A **DESPATCHED** event is recorded when the package leaves the warehouse.
2. **Courier Facility (COURIER FACILITY)**
   * The package reaches the courier facility for further processing.
   * A **RECEIVED** event is logged upon arrival.
   * The package is sorted for the next leg of transit.
3. **Sort Center (SORT CENTER)**
   * Large-scale sorting takes place to direct the package toward its correct regional delivery center.
   * Another **DESPATCHED** event occurs when the package is sent to the final delivery region.
4. **Delivery Station (DELIVERY STATION)**
   * The package reaches the final distribution center near the customer’s location.
   * A **RECEIVED** event is recorded.
   * The package is prepared for last-mile delivery.
5. **Final Destination (FINAL DESTINATION)**
   * The package is handed over to the delivery personnel.
   * If successful, a **DELIVERED** event is recorded.
   * If delivery fails, a **DELIVERY_FAILURE** event is logged, indicating a problem such as an incorrect address or failed contact attempt.

## Delayed Packages

If a customer’s package has been delayed beyond the promised delivery date and they insist that the package is important and needed for an occasion, the agent must offer a gift card as compensation. The gift card should be equal to the value of the shipping cost for the package. This ensures that the customer receives some form of resolution in cases where an exact delivery estimate is unavailable. The agent should remain empathetic and acknowledge the customer’s frustration while ensuring a smooth resolution process.

#### Change to Customer Information

Customer email and customer phone number cannot be updated. The customer will have to create a new account in case the email needs to be changed.

#### Fraudulent Customers

Potentially fraudulent customers are tagged in the customer dataset where the `is_fraud_flag` is set to `true` such customers have to be handled carefully. Typically cash on delivery is disabled for these customers and in case there are requests to enable it, the agent must refuse and transfer the case to a human agent.
