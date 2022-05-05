def elevy_fee(price):
    value = 0
    if price <= 100:
        value = 0
    else:
        value = (((price - 100)*1.5)/100) 
    return value