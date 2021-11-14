import os
import requests
import commons as cmn

def test_dtml():
    # my_list = os.listdir('./')
    # folder_names = cmn.valid_folders(my_list)
    f_names = ['102', '108']
    for i in range(len(f_names)):
        url = "https://cube-staging.drivetrain.ai/cube/check"
        request_data = cmn.fetch_dtml_payload(folder_name=f_names[i])
        response = requests.post(url=url, data=request_data)
        print(response.status_code)

