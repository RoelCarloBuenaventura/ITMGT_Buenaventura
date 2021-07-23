products = {
    "americano":{"name":"Americano","price":150.00},
    "brewedcoffee":{"name":"Brewed Coffee","price":110.00},
    "cappuccino":{"name":"Cappuccino","price":170.00},
    "dalgona":{"name":"Dalgona","price":170.00},
    "espresso":{"name":"Espresso","price":140.00},
    "frappuccino":{"name":"Frappuccino","price":170.00},
}

def get_product(code):
    for c in products.keys():
        if c == code:
            return products[c]
            break

def get_property(code,property):
    try:
        for c in products.keys():
            if c == code:
                return products[c][property]
                break
    except:
        return "Invalid property"

def main():
    receipt = '''
    \t==
    \tCODE\t\t\t\tNAME\t\t\tQUANTITY\t\t\tSUBTOTAL'''
    orderdict = {}
    total = 0
    while True:
        order = input("{product_code},{quantity}")
        try:
            if order != "/":
                order = order.split(",")
                code = order[0]
                order_quantity = int(order[1])
                if code in products.keys():
                    if code not in orderdict.keys():
                        orderdict[code] = order_quantity
                    else:
                        orderdict[code] += order_quantity
            elif order == "/":
                break
        except:
            continue
    for code in sorted((list(orderdict.keys()))):
        name = get_property(code,"name")
        price = get_property(code,"price")
        if len(code) > 7:
            receipt += '''\n\t{}\t\t\t{}\t\t{}\t\t\t\t{}'''.format(code,name,orderdict[code],price*orderdict[code])
        else:
            receipt += '''\n\t{}\t\t\t\t{}\t\t\t{}\t\t\t\t{}'''.format(code,name,orderdict[code],price*orderdict[code])
        total += price*orderdict[code]
    receipt += '''

    \tTotal:\t\t\t\t\t\t\t\t\t\t\t{}
    \t==
    '''.format(total)
    with open("receipt.txt","w") as r:
        r.write(receipt)

main()
