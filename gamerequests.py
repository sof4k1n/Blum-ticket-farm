import requests
import json

def balance(urlBalance, headers, jwt):
    headers["authorization"] = jwt
    r = requests.get(urlBalance, headers=headers)
    jr = json.loads(r.content)
    avaibalance = jr.get("availableBalance")
    ticket = jr.get("playPasses")
    return avaibalance, ticket

def play(urlPlay, headers, jwt):
    headers["authorization"] = jwt
    r = requests.post(urlPlay, headers=headers)
    jr = json.loads(r.content)
    gameid = jr.get("gameId")
    return r.status_code, gameid, r

def claim(urlClaim, headers, payload, jwt):
    headers["authorization"] = jwt
    r = requests.post(urlClaim, headers=headers, json=payload)
    return r.status_code

def auth(urlAuth, headers, token):
    r = requests.post(urlAuth, headers=headers, json=token)
    r.encoding = "RFC 7932"
    jwt = json(r.content).get("token").get("access")
    return f"Bearer {jwt}"
