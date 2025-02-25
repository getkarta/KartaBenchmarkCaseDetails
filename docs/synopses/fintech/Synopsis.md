## Synopsis of Use Case

The fintech use case simulates a hypothetical financial technology firm offering a payment gateway service that can be embedded into merchant client domains. Data structures and simulated APIs will cover a significantly simplified yet sufficiently complex version of the problem space - a playground that is ideal for testing the efficacy of agents. There are a 5 types of artefacts that will be provided to the user.

1. **Data Artefacts:** Are basically datasets defined as python dictionaries. In this particular case, the following datasets will be provided. (For a more detailed definition of these datasets, refer to the data documentation included in the fintech folder).:
   * `users` - a dataset consisting of customers who are making payments via the gateway to merchants. It is assumed that the users will have to create an account with the payment gateway to make payments.
   * `merchants` - stores the details of the merchants accepting payments.
   * `transactions` - logs all the transactions processed through the gateway.
   * `settlements` - tracks the status of payments from the gateway to the merchant bank accounts.
   * `disputes` - tracks chargebacks and refunds requested by customers.
   * `fees` - tracks the fees charged by the payment gateway to merchants for facilitating transactions.
   * `fraud_logs` - logs transactions logged for fraud risk.
   * `support_tickets` - tracks the customer support requests by both merchants and customers and their resolution status.
   * `domain_verifications` - stores all the domain verification requests and their current status. This is for merchants who are onboarding their domain to the payment gateway.
   * `bank_account_verifications` - verification details of the bank account.
2. **Knowledge Base -** A single markdown document that details the nature of the business and the datasets. Granular details on rules and regulations which should guide the behavior of agents can be found here.
3. **SOP -** more specific than the knowledge base and documents the steps that should be followed to resolve tickets.
4. **Tasks -** a curated set of tasks of varying difficulty that must be solved by the agent. A task consists of a user persona with a very specific mandate on what must be asked of the agent (typically a user with a support need), the ideal sequence of actions that must be taken and the outputs that must be displayed to the user in the course of the conversation with the Agent.
5. **Tool Factory -** a function that returns a set of tools to interact with the dataset, classified as read tools, write tools and evaluation helpers.
