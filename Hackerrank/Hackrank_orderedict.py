n = int(input())
allitems = dict()
for _ in range(n):
    allinput = input().rsplit(" ", 1)
    item_names_str, price = allinput
    net_prices_float = float(price)

    # if item_names_str not in allitems:
    #     allitems[item_names_str] = net_prices_float
    # else:
    #     allitems[item_names_str] = allitems[item_names_str] + net_prices_float
    allitems[item_names_str] = allitems.get(
        item_names_str, 0) + net_prices_float

# print(allitems)
for finallist_ in allitems:
    print(finallist_, allitems[finallist_])
