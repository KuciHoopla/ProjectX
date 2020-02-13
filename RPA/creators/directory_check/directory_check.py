import os
from creators.variables.variables import jsons_folder


def get_list_of_jsons():
    try:
        list_of_jsons = os.listdir(jsons_folder)
        return list_of_jsons
    except:
        return [0]


