import datetime

cart = {}
TAX_RATE_8  = 1.08
TAX_RATE_10 = 1.10

tilde = '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
hyphen = '----------------------------------------'

class Item:
    def __init__(self, id, name, price, tax_flag):
        self.id = id
        self.name = name
        self.price = price
        self.tax_flag = tax_flag
        
def buy(cart, id, num):
    if id not in cart:
        cart[id] = num
    else:
        cart[id] += num
    return cart
    
def sum(value, num):
    return value * num

def calculate_change(money, total_price):
    if money >= total_price:
        return money - total_price
    else:
        return -1
        
def main():
    apple = Item(1, 'りんご', 100, True)
    dragon_fruit = Item(2, 'ドラゴンフルーツ', 400, True)
    salmon_bento = Item(3, 'しゃけ弁当', 390, True)
    duvel_beer = Item(4, 'ビール(Duvel 330ml)', 660, False)
 
    items = {1: apple, 2: dragon_fruit, 3: salmon_bento, 4:duvel_beer}

    small_price = 0
    small_price_8 = 0
    small_price_10 = 0

    total_price = 0
    total_price_8 = 0
    total_price_10 = 0

    print(f'~~~~~~~~~~~~~~~~ItemList~~~~~~~~~~~~~~~~')
    for id in items:
        print(f'{id}.{items[id].name}: {items[id].price}円')
    print(tilde + '\n')
    while True:
        while True:
            id = input('「商品番号を入力してください。会計する場合は 0 を入力してください。」(´・ω・｀): ')
            try:
                id = int(id)
            except:
                print('「数字を入力してください！」(｀；ω；´)')
                continue

            if id > len(items) or id < 0:
                    print('「そんな商品番号はない！」(｀；ω；´)')
            else:
                break
        if id == 0:
            break    
        
        while True:
            num = input(f'「{items[id].name}何個いるんだい...？」(´・ω・｀): ')
            try:
                num = int(num)
            except:
                print('「数字を入力してください！」(｀；ω；´)\n')
                continue

            if num < 0:
                    print('「一個以上選んでね！」(｀；ω；´)\n')
            else:
                break

        buy(cart, id, num)

        if items[id].tax_flag:
            small_price_8 += sum(items[id].price, num)
        else:
            small_price_10 += sum(items[id].price, num)

        print(f'\n((( つ•̀ω•́)つ＼[カートに{items[id].name}を{num}個追加しました。]\n')
    
    small_price = small_price_8 + small_price_10
    total_price_8 = int(small_price_8 * TAX_RATE_8)
    total_price_10 = int(small_price_10 * TAX_RATE_10)
    total_price = total_price_8 + total_price_10

    if small_price > 0:
        print(hyphen)
        print('(商品名 定価　個数　小計)')
        for id in cart:
            print(f'{items[id].name} {items[id].price}円 {cart[id]}個 {sum(items[id].price, cart[id])}円')
            
        print(hyphen) 
        print(f'小計{small_price}円')
        print(f'外税額8% {total_price_8 - small_price_8}円')
        print(f'外税額10% {total_price_10 - small_price_10}円')
        print(f'\n「合計{total_price}円だよ」(´・ω・｀)\n')

        while True:
            money = input('お金を入れてください: ')
            try:
                money = int(money)
                break
            except:
                print('「お金以外のものを入れないで！」(｀；ω；´)')

        change = calculate_change(money, total_price)
        if change < 0:
            print('「お金が足りないよ.....」(# ﾟДﾟ)')
        else:
            print(f'「{money}円お預かりいたします。 」(シ_ _)シ\n')
            if change != 0:
                print(f'「お釣りの{change}円だよ」(´・ω・｀)')
            print(f'「レシートだよ」(´・ω・｀)\n')
            now = datetime.datetime.now()

            print(tilde)
            print(f'                 POMTAN                　\n') 
            print(f'担当者: OMUSUBI')
            print(now.strftime('%Y年%m月%d日 %H:%M'))   
            print(hyphen)
            print('(商品名 定価　個数　小計)')
            for id in cart:
                print(f'{items[id].name} {items[id].price}円 {cart[id]}個 {sum(items[id].price, cart[id])}円')
            print(hyphen) 
            print(f' 小計', end='')
            print(f'{small_price}円'.rjust(34))
            print(f'(外税額8%対象額', end='')
            print(f'{small_price_8}円)'.rjust(25))
            print(f' 外税額8%', end='')
            print(f'{total_price_8 - small_price_8}円'.rjust(30))
            print(f'(外税額10%対象額', end='')
            print(f'{small_price_10}円)'.rjust(24))
            print(f' 外税額10%', end='')
            print(f'{total_price_10 - small_price_10}円'.rjust(29))
            print(hyphen) 
            print(f'合計', end='')
            print(f'{total_price}円'.rjust(35))
            print(f'お預り', end='')
            print(f'{money}円'.rjust(33))
            print(f'お釣り', end='')
            print(f'{change}円'.rjust(33))
            print(tilde)
    print('\n「ありがとうございました！」(o^∀^)')
main()
