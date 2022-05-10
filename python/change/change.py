def find_fewest_coins(coins, target):
    if target < 0:
        raise ValueError("target can't be negative")
    if target == 0:
        return []
    if target in coins:
        return [target]
    possible_coins = []
    for coin in coins:
        if coin < target:
            possible_coins.append(coin)
    if len(possible_coins) == 0:
        raise ValueError("can't make target with given coins")
    list_of_coins = []
    steps = 0
    while len(possible_coins) > 0:
        substracted_target = target
        looped_coins = [coin for coin in possible_coins]
        coins_used = []
        while substracted_target != 0 and substracted_target >= min(looped_coins):
            while substracted_target >= looped_coins[-1]:
                substracted_target -= looped_coins[-1]
                coins_used.append(looped_coins[-1])
            looped_coins.pop()
            if len(looped_coins) == 0:
                break
        if substracted_target == 0:
            if steps == 0:
                steps = len(coins_used)
                for coin in coins_used:
                    list_of_coins.append(coin)
            elif len(coins_used) < steps:
                steps = len(coins_used)
                list_of_coins = []
                for coin in coins_used:
                    list_of_coins.append(coin)
        possible_coins.pop()
    if steps == 0 and 1 not in coins:
        substracted_target = target
        for coin in coins:
            next_index = coins.index(coin) + 1
            if next_index < len(coins):
                while substracted_target % coins[next_index] != 0:
                    substracted_target -= coin
                    if substracted_target < 0:
                        raise ValueError("can't make target with given coins")
                    list_of_coins.append(coin)
                    if substracted_target == 0:
                        break
            else:
                while substracted_target > 0:
                    substracted_target -= coin
                    if substracted_target < 0:
                        raise ValueError("can't make target with given coins")
                    list_of_coins.append(coin)
        return list_of_coins
    if len(list_of_coins) == 0:
        raise ValueError("can't make target with given coins")
    list_of_coins = list_of_coins[::-1]
    return list_of_coins
