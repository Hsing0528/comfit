info = {"123 456":9000,"456 789":5000,"789 888":6000,"336 558":10000,"775 666":12000,"566 221":7000}
amount = int(input("輸入查詢組數 N 為:"))
for i in range(amount):
    accpas=input()
    print(f'{info[accpas]}')if accpas in info else print("error")