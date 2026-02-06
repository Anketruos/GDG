def get_expensive_products(prices):
    highprice = []   #the high price list
    for price in prices:
        if price > 100:
            highprice.append(price)
    return highprice


prices = [120, 45, 300, 85, 150]
result = get_expensive_products(prices)
print(result)  
