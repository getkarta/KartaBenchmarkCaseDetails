# Copyright GetKarta.ai 2025

import os
import json
from karta_benchmarks.evaluation_datasets.fintech.data_factory.factory import factory as data_factory
from typing import Callable, Dict, Any, List, Literal, Tuple
import copy
import inspect
from karta_benchmarks.general_helpers.get_frame_info import get_frame_info

def factory() -> Tuple[List[Callable], List[Callable], Dict[str, Callable]]:
    """
    This is a function factory that will create a playground of 
    tools(functions) that the AI agent can use and access.
    """
    data = data_factory()
    DATA = copy.deepcopy(data)
    CALL_HISTORY = []

    def get_db_state() -> dict:
        """
        Get the current state of the database.

        Returns:
            dict: The current state of the database.
        """
        return DATA
    
    def get_call_history() -> List:
        """
        Get the call history of the agent.
        This is not a tool, but a function to get the call history.
        Donot use it with the agentic workflow.
        """
        return CALL_HISTORY
    
    def reset_call_history():
        """
        Reset the call history of the agent.
        This is not a tool, but a function to get the call history.
        Donot use it with the agentic workflow.
        """
        CALL_HISTORY.clear()

    def transfer_to_human_agents(summary: str) -> str:
        """
        Transfer the user to a human agent, with a summary of the user's issue.
        Only transfer if the user explicitly asks for a human agent, or if the
        user's issue cannot be resolved by the agent with the available tools.

        Args:
            summary (str): A summary of the user's issue.

        Returns:
            str: A message indicating the outcome of the transfer.
        """
        CALL_HISTORY.append(get_frame_info(inspect.currentframe()))
        return f"Transfer successful. <SUMMARY>{summary}</SUMMARY>"


    def get_merchant(merchant_id: str) -> dict:
        """
        Get the merchant data for a given merchant id.

        Args:
            merchant_id (str): The id of the merchant to get data for.

        Returns:
            str: A Json formatted string that contains the merchant data. 
            Merchant data typically contains the name, email, phone, creation date,
            business_type, status of the merchant, the status of the doman of the merchant,
            compliance issues and the current settlement details of the merchant. If no merchant is
            found then an error message is returned.
        """
        CALL_HISTORY.append(get_frame_info(inspect.currentframe()))
        try:
            merchant_data = DATA['merchants'][merchant_id]
            return json.dumps(merchant_data)
        except KeyError:
            return f"<ERROR>Merchant with id {merchant_id} not found.</ERROR>"
        
    return ({
        "get_db_state": get_db_state,
        "get_merchant": get_merchant,
        "get_call_history": get_call_history,
        "reset_call_history": reset_call_history,
        "transfer_to_human_agents": transfer_to_human_agents
    },
    # The list of read tools as callable functions
    [
        get_merchant,
        transfer_to_human_agents
    ], 
    # The list of write tools as callable functions
    [
    ]
    )
    

