# Copyright 2025 Karta

import os
import json
from karta_benchmarks.evaluation_datasets.ecommerce.data_factory.factory import factory as data_factory
from typing import Dict, Any, List
from datetime import datetime
import copy
from karta_benchmarks.general_helpers.get_frame_info import get_frame_info
from karta_benchmarks.evaluation_datasets.ecommerce.schemas.schemas import SCHEMAS
import inspect

def factory() -> Dict[str, Any]:
    """
    This is the tool factory that generates a set of tools (callables) that will operate 
    on a fresh instance of the data. Each tool comes with a docstring which can be used when
    binding to the agent.

    Returns:
        Dict[str, Any]: A dictionary that contains:
            - tool_mapping: A mapping between the tool name and the tool callable
            - read_tools: All the read tools 
            - update_tools: All the update tools
    """
    data = data_factory()
    
    # Creating a copy of the data
    DATA = copy.deepcopy(data)

    # An empty call history
    CALL_HISTORY = []

    def vend_schemas() -> Dict[str, Any]:
        """
        Vend the schemas of the different datasets in the domain
        """
        return SCHEMAS

    def get_db_state() -> dict:
        """
        Get the current state of the database.

        Returns:
            dict: The current state of the database.
        """
        return DATA
    
    def get_call_history() -> List:
        """
        Get the call history after the latest reset.

        Returns:
            List: The call history.
        """
        return CALL_HISTORY
    
    def reset_call_history() -> None:
        """
        Reset the call history.
        """
        CALL_HISTORY.clear()

    def calculate_date_difference(date1: str, date2: str) -> int:
        """
        Calculate the difference in days between two dates which are specified as strings in the format YYYY-MM-DD.

        Args:
            date1 (str): The first date in YYYY-MM-DD format.
            date2 (str): The second date in YYYY-MM-DD format.

        Returns:
            int: The difference in days between the two dates in days.
        """
        CALL_HISTORY.append(get_frame_info(inspect.currentframe()))
        date1 = datetime.strptime(date1, "%Y-%m-%d")
        date2 = datetime.strptime(date2, "%Y-%m-%d")
        return (date2 - date1).days
    
    def get_customer_by_id(customer_id: str) -> Dict[str, Any]:
        """
        Gets Basic Customer Information by the ID of the customer

        Args:
            customer_id (str): The ID of the customer

        Returns:
            Dict[str, Any]: A dictionary containing the customer information. 
            The customer information contains the customer_id, first_name, date of birth,
            gender, account_creation_date, last_order_date, is_active, is_email_verified,
            is_phone_verified, is_fraud_flag.
            If the customer_id is not found, an error message is returned
        """
        CALL_HISTORY.append(get_frame_info(inspect.currentframe()))
        if customer_id not in DATA["customers"]:
            raise f"<error> Customer with ID {customer_id} not found </error>"
        return DATA["customers"][customer_id]
    
    def get_customer_by_email(email: str) -> Dict[str, Any]:
        """
        Gets Basic Customer Information by the email of the customer

        Args:
            email (str): The email of the customer

        Returns:
            Dict[str, Any]: A dictionary containing the customer information. 
            The customer information contains the customer_id, first_name, date of birth,
            gender, account_creation_date, last_order_date, is_active, is_email_verified,
            is_phone_verified, is_fraud_flag.
            If the customer with the given email is not found, an error message is returned
        """
        CALL_HISTORY.append(get_frame_info(inspect.currentframe()))
        for customer_id, customer_info in DATA["customers"].items():
            if customer_info["email"] == email:
                return customer_info
        return f"<error> Customer with email {email} not found </error>"
        
        

    return {
        "tool_mapping": {
            "get_db_state": get_db_state,
            "get_call_history": get_call_history,
            "reset_call_history": reset_call_history,
            "calculate_date_difference": calculate_date_difference,
            "get_customer_by_id": get_customer_by_id,
            "get_customer_by_email": get_customer_by_email
        },
        "read_tools": [calculate_date_difference, get_customer_by_id, get_customer_by_email],
        "update_tools": []
    } 
    
    