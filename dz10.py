
def mainer(sale):
    lists = []
    i = 0
    count = 0
    while i < len(sale) and count < 100:
        sare = sale[1]
        if sare.lower() not in ('m', 'n'):
            lists.append(sare)
            count += 1
        i += 1
    return lists


sale = input()
sake = mainer(sale)
print(mainer)