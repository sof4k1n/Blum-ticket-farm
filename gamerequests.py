import requests

def balance(urlBalance, headers):
    r = requests.get(urlBalance, headers=headers)
    jr = r.json()
    avaibalance = jr.get("availableBalance")
    ticket = jr.get("playPasses")
    return avaibalance, ticket

def play(urlPlay, headers):
    r = requests.post(urlPlay, headers=headers)
    jr = r.json()
    gameid = jr.get("gameId")
    return r.status_code, gameid, jr

def claim(urlClaim, headersClaim, payload):
    r = requests.post(urlClaim, headers=headersClaim, json=payload)
    return r.status_code