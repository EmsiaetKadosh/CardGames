import random


class Card:
    def __init__(self) -> None:
        pass
    
    def __str__(self) -> str:
        pass


class Cards:
    def __init__(self) -> None:
        self.cards = []
    
    def shuffle(self) -> list:
        result = self.cards.copy()
        random.shuffle(result)
        return result


class Poker(Card):
    __name: list[str] = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'joker', 'JOKER']
    
    def __init__(self, n: int, s: str) -> None:
        super().__init__()
        self.number = n
        self.suits = s
    
    def __str__(self) -> str:
        return '<' + self.suits[0] + self.__name[self.number - 1] + '>'
    
    def __lt__(self, other):
        return self.suits < other.suits if self.number == other.number else self.number < other.number


class Pokers(Cards):
    def __init__(self) -> None:
        super().__init__()
        self.cards = [Poker(14, 'None'), Poker(15, 'None')]
        for i in range(1, 14):
            for j in ['Space', 'Heart', 'Club', 'Diamond']:
                self.cards.append(Poker(i, j))


class CardGame:
    def __init__(self, player_count: int, cards: Cards) -> None:
        self.playerCount = player_count
        self.cards = cards
    
    def play(self) -> list[list]:
        result = self.cards.cards.copy()
        random.shuffle(result)
        return result


class PokerGame(CardGame):
    def __init__(self, player_count: int) -> None:
        super().__init__(player_count, Pokers())
    
    def play(self, leave: int) -> list[list]:
        count: int = len(self.cards.cards)
        draw: int = count - leave
        if draw % self.playerCount != 0:
            raise ValueError('无法平均发牌')
        draw //= self.playerCount
        result = self.cards.cards.copy()
        random.shuffle(result)
        ret = []
        for i in range(self.playerCount + 1):
            ret.append(result[i * draw: (i + 1) * draw + 1])
        ret[0].sort()
        ret[1].sort()
        ret[2].sort()
        ret[3].sort()
        return ret


def _to_str(a: list[list[Poker]]) -> str:
    r: str = ''
    for k in a:
        r += '['
        for j in k:
            r += str(j)
        r += ']\n'
    return r


if __name__ == '__main__':
    res: list[list[Poker]] = PokerGame(3).play(3)
    print(_to_str(res))
