gameid = 'a1bb95e5-ab26-4772-8fbb-531a47988f98'
count = 200

payload = {"gameId":gameid,"points":count}
length = str(len(str(payload).replace(' ', '')))
print(length)
