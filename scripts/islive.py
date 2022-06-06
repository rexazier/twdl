import requests

import os
import time
import json
import base64

input_url = os.getenv("URL")

def is_live(user_id):
    print("checking...")
    orig_site = "dHdpdGNhc3RpbmcudHY="
    tw_site = base64.b64decode(orig_site).decode("ascii")

    url = f"https://{tw_site}/userajax.php?c=islive&u={user_id}"
    loop = True
    while loop:
        try:
            response = requests.get(url).json()
            if response == 0:
                loop = True
                print(f"{user_id} is OFFLINE")
                time.sleep(15)
            else:
                loop = False
                print(f"{user_id} is ONLINE")
        except:
            continue

is_live(input_url.split("/")[3])
