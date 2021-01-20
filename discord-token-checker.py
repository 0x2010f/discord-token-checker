import requests

with open("tokens.txt") as f:
    for line in f:
        token = line.strip("\n")

        headers = {
            'Content-Type': 'application/json', 'authorization': token
        }

        url = "https://discordapp.com/api/v6/users/@me/library"

        __request = requests.get(url, headers=headers)
        
        if __request.status_code == 200:
            print("[VALID] {}".format(line.strip("\n")))
