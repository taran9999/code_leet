def solution(prices):
    buy_price = max(prices)
    sell_price = 0
    profit = 0

    for p in prices:
        if p < buy_price:
            buy_price = p
            sell_price = p
        elif p > sell_price:
            sell_price = p
            if sell_price - buy_price > profit: profit = sell_price - buy_price

    return profit
