import gamerequests
from random import randint
from time import sleep

def main(ticket, aBalance):
    print("\nДоступных билетов: ", ticket)
    print("Нынешний баланс: ", aBalance)
    i = 0
    total = 0
    
    while ticket != 0:
        try:
            response = gamerequests.play(urlPlay, headers)
            statusPlay = response[0]
            jr = response[2]
            if statusPlay == 200: 
                gameid = response[1]
                count = randint(200, 280)
                payload = {"gameId": gameid, "points": count}
                print(f'\n{payload}')
                sleep(31)
                response = gamerequests.claim(urlClaim, headersClaim, payload)
                statusClaim = response
                while statusClaim != 200:
                    print(f"\nClaim Выдал ошибку {statusClaim}")
                    response = gamerequests.claim(urlClaim, headersClaim, payload)
                    statusClaim = response
                    sleep(3)
                else:
                    i+=1
                    total+=count
                    ticket-=1
                    print(f"- Тикет: {i} выполнился на {count} поинтов!")
                    sleep(5)
                    print("Начинаю фарм нового билета")
            else:
                print(f"\nPlay Выдал ошибку {statusPlay}")
                print(jr)
                sleep(4)
                continue
        except:
            continue
    else:
        print(f'\nТикетов нет, всего нафармило {total} поинтов')
        input("Enter - чтобы выйти")
            
jwt = input("Введи ключ авторизации: ")
urlPlay = "https://game-domain.blum.codes/api/v1/game/play"
urlClaim = "https://game-domain.blum.codes/api/v1/game/claim"
urlBalance = "https://game-domain.blum.codes/api/v1/user/balance"
headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 13; K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/128.0.6613.127 Mobile Safari/537.36', 'authorization': jwt, 'sec-ch-ua-platform': 'Android'}
headersClaim = {'user-agent': 'Mozilla/5.0 (Linux; Android 13; K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/128.0.6613.127 Mobile Safari/537.36', 'authorization': jwt, 'sec-ch-ua-platform': 'Android', 'accept': 'application/json, text/plain, */*', 'content-type': 'application/json', 'accept-encoding': 'gzip, deflate, br, zstd', 'accept-language': 'ru,ru-RU;q=0.9,en-US;q=0.8,en;q=0.7', 'lang': 'en'}

response = gamerequests.balance(urlBalance, headers)
ticket = response[1]
aBalance = response[0]

if __name__ == "__main__":
    main(ticket, aBalance)