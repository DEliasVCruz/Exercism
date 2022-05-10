import re


class Luhn:
    def __init__(self, card_num):
        card_num = re.sub(" ", "", card_num)
        self.card_num = card_num

    def valid(self):
        num = self.card_num
        if len(num) <= 1:
            return False

        if re.search("[^0-9]+", num):
            return False

        pars_doubled = []
        odds = []

        i = 1
        while i <= len(num):
            if not (i % 2):
                par_num = int(num[-i]) * 2
                if par_num > 9:
                    par_num = par_num - 9
                pars_doubled.append(par_num)
            i += 1

        i = 1
        while i <= len(num):
            if i % 2:
                odds.append(int(num[-i]))
            i += 1

        sumation = sum(pars_doubled) + sum(odds)

        return not bool(sumation % 10)
