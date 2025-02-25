# Copyright GetKarta.ai 2025

import os
import json
import karta_benchmarks.evaluation_datasets.fintech.raw_data as raw_data

def factory():
    """
    This function loads all the json files in the raw_data directory and 
    returns a dictionary of the data. This is the base data set that will 
    be used in the evaluations.
    """
    json_files = [f for f in os.listdir(raw_data.__path__[0]) if f.endswith('.json')]
    json_data = {}
    for file in json_files:
        with open(os.path.join(raw_data.__path__[0], file), 'r') as f:
            json_data[file.replace('.json', '')] = json.load(f)
    return json_data