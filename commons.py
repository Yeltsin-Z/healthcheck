import json

def fetch_dtml_payload(folder_name):
    json_file = open('./'+folder_name+'/'+folder_name+'.json',)
    json_data = json.load(json_file)
    return json_data


