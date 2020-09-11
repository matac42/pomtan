cart = {}
name = 'name'
price = 'price'
OUT_TAX_RATE_8 = 0.08
OUT_TAX_RATE_10 = 0.10
TAX_RATE_8  = 1.08
TAX_RATE_10 = 1.10
TAX_RATE_8_ = 8
TAX_RATE_10_ = 10

items = {
    1: {name: 'りんご',price: 100, 'tax_flag': True},
    2: {name: 'ドラゴンフルーツ',price: 400, 'tax_flag': True},
    3: {name: 'しゃけ弁',price: 390, 'tax_flag': True}
}


def buy(cart, id, num):
    if id not in cart:
        cart[id] = num
    else:
        cart[id] += num
    return cart
    
def sum(value, num):
    return value * num

def add_tax(price, flag):
    if flag:
        return price * TAX_RATE_8
    else:
        return price * TAX_RATE_10

def calculate_change(money, total_price):
    if money >= total_price:
        return money - total_price
    else:
        return -1
        

def main():
    total_price = 0
    small_price = 0
    
    total_price_10 = 0
    total_price_8 = 0
    while True:
        print(f'~~~~~~~~~~~~~~商品リスト~~~~~~~~~~~~~')
        for id in items:
            print(f'{id}.{items[id][name]}: {items[id][price]}円')
        print(f'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        selected_id = input('「商品を選択してください。会計する場合はEnterを押してください。」(´・ω・｀): ')

        try:
            selected_id = int(selected_id)
        except:
            break
        
        if selected_id > len(items):
            print('範囲外')
            break
        num = int(input(f'「{items[selected_id][name]}何個いるんだい...？」(´・ω・｀): '))
    
        buy(cart, selected_id, num)
        small_price += sum(items[selected_id][price], num)
        print(f'-------------------------------------')
        print(f'カートに{items[selected_id][name]}を{num}個追加しました。')
        print(f'-------------------------------------')
    
    if small_price > 0:
        print(f'-------------------------------------')
        print('(商品名 定価　個数　小計)')
        for id in cart:
            print(f'{items[id][name]} {items[id][price]}円 {cart[id]}個 {sum(items[id][price], cart[id])}円')
        print(f'-------------------------------------') 
        print(f'小計{small_price}円')
        total_price = int(add_tax(small_price, True))
        print(f'外税額8%対象額 {small_price}円')
        print(f'外税額8% {total_price - small_price}円')
        print(f'-------------------------------------') 
        print(f'「合計{total_price}円だよ」(´・ω・｀)')
        print(f'-------------------------------------')
        while True:
            try:
                money = int(input('お金入力: '))
                break
            except:
                print('「お金以外のものを入れないで！」(｀；ω；´)')

        change = calculate_change(money, total_price)
        if change >= 0:
            print('「買ってくれたのか、お前いいやっちゃな」 (´・ω・｀)')
            if change != 0:
                print(f'「お釣りの{change}円だよ」(´・ω・｀)')        
        else:
            print('「お金が足りないよ.....」(# ﾟДﾟ)')
    '''
    else:
        print('「けっ、冷やかしは帰んな！」(# ﾟДﾟ)')
    '''
    print('「ありがとうございました！」(´・ω・｀)')

main()
