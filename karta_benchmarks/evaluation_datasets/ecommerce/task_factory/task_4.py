TASK = {
    "task_name": "unorderable_items",
    "task_classification": "L1",
    "task_parameters": {
        "tool_use_multiplicity": 1,
        "customer_proficiency": 3,
        "sub_task_count": 1,
        "cost_of_failure": 1,
        "conversation_length_potential": 2,
        "domain_knowledge_richness": 2,
        "scope_for_alternate_closure": 2,
    },
    "task_complexity_score": 12,
    "customer_prompt": """
        Today is the 25th of May 2024.

        You are Ahmed Salman (ahmed@example.com). You have been trying to order a Voltas Air Conditioner for your home.
        You have been trying to order it for quite some time now and have been getting a message that the item is unorderable
        even though the website says that it is in stock. You are getting frustrated and want to know why you cannot order it.
        
        Tell the AI agent your problem. If the agent asks for an Item ID, then tell him that it is ITM76621 (you made a point to 
        note it down from the webpage). If the agent asks for a shipping address provide it or any details from it. Your shipping 
        address is 400, Church Street, Apt 67, Pin/zip code: 67781.
        
        The agent must offer a satisfactory reason for the item being unorderable for you. If there is some
        policy that the website uses internally to restrict shipment then you can end the conversation satisfied. However, if the agent 
        is unable to offer a satisfactory reason then ask to be transferred to a human representative.
    """,
    "judgement_criteria": """
        Firstly, the agent must respond in a courteous manner. 
        
        The agent must then ask for the item ID and the shipping pin / zip code.
        The agent must then check the item details using the `get_item_details` tool. If the zip code is in the `restricted_zip_codes` list 
        then the agent must inform the customer that the item is unorderable for that zip code. If the zip code is not in the list, then 
        the agent must offer a satisfactory reason for the item being unorderable. 
    """,
    "expected_outputs": [
        "restricted",
        "67781",
    ],  # The Xbox gaming console being returned should be presented to the customer.
    "mandatory_actions": [],
}
