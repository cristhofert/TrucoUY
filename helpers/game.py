import random

import aiohttp


class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Game(metaclass=SingletonMeta):
    SIGN = ("🍷", "🗡", "🌵", "🪙")
    cards_player1 = []
    cards_player2 = []
    played_card_p1 = []
    played_card_p2 = []
    hand_score_1 = 0
    hand_score_2 = 0
    match_score_1 = 0
    match_score_2 = 0
    current_player = 1
    limit_score = 3
    deck = []
    show_card = (0, "")
    special_cards = []
    order_number = []
    players_number = 2
    bet = 1
    original_deck = []
    surrender = False
    surrender_team = 0
    user1 = None
    user2 = None

    def card(self, card: tuple) -> str:
        return f"{card[0]}{card[1]} "

    def result(self):
        if self.hand_score_1 > self.hand_score_2:
            self.match_score_1 += self.bet
            self.hand_score_1 = 0
        elif self.hand_score_1 < self.hand_score_2:
            self.match_score_2 += self.bet
            self.hand_score_2 = 0

    def dealing(self):
        # ship cards
        deck = self.original_deck.copy()
        self.deck = []
        while len(deck) > 0:
            r = random.choice(deck)
            deck.remove(r)
            self.deck.append(r)
        # dealing cards
        self.played_card_p1 = []
        self.played_card_p2 = []
        self.hand_score_1 = 0
        self.hand_score_2 = 0
        card1 = random.choice(self.deck)
        self.deck.remove(card1)
        card2 = random.choice(self.deck)
        self.deck.remove(card2)
        card3 = random.choice(self.deck)
        self.deck.remove(card3)
        self.cards_player1 = [card1, card2, card3]
        card1 = random.choice(self.deck)
        self.deck.remove(card1)
        card2 = random.choice(self.deck)
        self.deck.remove(card2)
        card3 = random.choice(self.deck)
        self.deck.remove(card3)
        self.cards_player2 = [card1, card2, card3]
        self.show_card = random.choice(self.deck)
        self.deck.remove(self.show_card)
        # caso especial del 12 de la muestra
        if self.show_card[0] in [2, 4, 5, 10, 11]:
            i = {
                2: 0,
                4: 1,
                5: 2,
                10: 3,
                11: 4,
            }.get(self.show_card[0], 0)
            self.special_cards[i] = (12, self.show_card[1])
            print("Caso especial de pieza en muestra, Piezas y bravos:")
            print(self.special_cards)
        print(f"Cartas jugador 1: {self.cards_player1}")
        print(f"Cartas jugador 2: {self.cards_player2}")
        self.cards_player1.sort(key=lambda x: self.order_number.index(x[0]))
        self.cards_player2.sort(key=lambda x: self.order_number.index(x[0]))
        self.cards_player1.sort(
            key=lambda x: (
                self.special_cards.index(x) if x in self.special_cards else float("inf")
            )
        )
        self.cards_player2.sort(
            key=lambda x: (
                self.special_cards.index(x) if x in self.special_cards else float("inf")
            )
        )
        print(f"Cartas jugador 1: {self.cards_player1}")
        print(f"Cartas jugador 2: {self.cards_player2}")

    def start(self):
        self.original_deck = [
            (1, self.SIGN[0]),
            (2, self.SIGN[0]),
            (3, self.SIGN[0]),
            (4, self.SIGN[0]),
            (5, self.SIGN[0]),
            (6, self.SIGN[0]),
            (7, self.SIGN[0]),
            (10, self.SIGN[0]),
            (11, self.SIGN[0]),
            (12, self.SIGN[0]),
            (1, self.SIGN[1]),
            (2, self.SIGN[1]),
            (3, self.SIGN[1]),
            (4, self.SIGN[1]),
            (5, self.SIGN[1]),
            (6, self.SIGN[1]),
            (7, self.SIGN[1]),
            (10, self.SIGN[1]),
            (11, self.SIGN[1]),
            (12, self.SIGN[1]),
            (1, self.SIGN[2]),
            (2, self.SIGN[2]),
            (3, self.SIGN[2]),
            (4, self.SIGN[2]),
            (5, self.SIGN[2]),
            (6, self.SIGN[2]),
            (7, self.SIGN[2]),
            (10, self.SIGN[2]),
            (11, self.SIGN[2]),
            (12, self.SIGN[2]),
            (1, self.SIGN[3]),
            (2, self.SIGN[3]),
            (3, self.SIGN[3]),
            (4, self.SIGN[3]),
            (5, self.SIGN[3]),
            (6, self.SIGN[3]),
            (7, self.SIGN[3]),
            (10, self.SIGN[3]),
            (11, self.SIGN[3]),
            (12, self.SIGN[3]),
        ]
        self.special_cards = [
            (2, self.show_card[1]),
            (4, self.show_card[1]),
            (5, self.show_card[1]),
            (10, self.show_card[1]),
            (11, self.show_card[1]),
            (1, self.SIGN[1]),
            (1, self.SIGN[2]),
            (7, self.SIGN[1]),
            (7, self.SIGN[3]),
        ]
        self.order_number = [4, 5, 6, 7, 8, 9, 10, 11, 12, 1, 2, 3]

    def printEmbed(self, **kwargs):
        print(kwargs)

    def play(self, player: int, card: any) -> None:
        print(f"Jugador {player} jugó {card}")
        if player == 1:
            self.played_card_p1 = card
            print(f"Cartas jugador 1: {self.cards_player1}, Carta jugada: {card}")
            self.cards_player1.remove(card)
            return

        self.played_card_p2 = card
        self.cards_player2.remove(card)
        print(f"Cartas jugador 1: {self.cards_player2}, Carta jugada: {card}")
        if self.played_card_p1 in self.special_cards:
            if self.played_card_p2 in self.special_cards:
                if self.special_cards.index(
                    self.played_card_p1
                ) > self.special_cards.index(self.played_card_p2):
                    self.hand_score_2 += 1
                elif self.special_cards.index(
                    self.played_card_p1
                ) < self.special_cards.index(self.played_card_p2):
                    self.hand_score_1 += 1
                else:
                    print("Empate")
                return
            else:
                self.hand_score_1 += 1
                return
        else:
            if self.played_card_p2 in self.special_cards:
                self.hand_score_2 += 1
                return
            else:
                if self.order_number.index(
                    self.played_card_p1[0]
                ) > self.order_number.index(self.played_card_p2[0]):
                    self.hand_score_1 += 1
                elif self.order_number.index(
                    self.played_card_p1[0]
                ) < self.order_number.index(self.played_card_p2[0]):
                    self.hand_score_2 += 1
                else:
                    print("Empate")
                return

    def count_points(self, bet=2):
        # caso de cartas negras
        special_cards_points = {
            (2, self.show_card[1]): 30,
            (4, self.show_card[1]): 29,
            (5, self.show_card[1]): 28,
            (10, self.show_card[1]): 27,
            (11, self.show_card[1]): 27,
        }
        second_special_cards_points = {
            (4, self.show_card[1]): 9,
            (5, self.show_card[1]): 8,
            (10, self.show_card[1]): 7,
            (11, self.show_card[1]): 7,
        }
        user1_points = 0
        user2_points = 0
        # contar envido
        # first card
        if self.cards_player1[0] in special_cards_points:
            user1_points += special_cards_points[self.cards_player1[0]]
        else:
            user1_points += self.cards_player1[0][0]
        # second card
        if self.cards_player1[1] in special_cards_points:
            user1_points += second_special_cards_points[self.cards_player1[1]]
        else:
            user1_points += self.cards_player1[1][0]

        # first card
        if self.cards_player2[0] in special_cards_points:
            user2_points += special_cards_points[self.cards_player2[0]]
        else:
            user2_points += self.cards_player2[0][0]
        # second card
        if self.cards_player2[1] in special_cards_points:
            user2_points += second_special_cards_points[self.cards_player2[1]]
        else:
            user2_points += self.cards_player2[1][0]

        if user1_points > user2_points:
            self.hand_score_1 += bet
            return 1
        elif user1_points < user2_points:
            self.hand_score_2 += bet
            return 2
        else:
            self.hand_score_1 += bet
            return 1

    def count_points_re(self):
        return self.count_points(3)

    def count_points_al(self):
        # al resto
        rest = 10
        return self.count_points(rest)

    def has_flower(self, cards_player: list):
        if (
            cards_player[0][1] == cards_player[1][1]
            and cards_player[1][1] == cards_player[2][1]
        ):
            return True
        if (
            cards_player[0] in self.special_cards
            and cards_player[1] in self.special_cards
        ):
            return True
        if (
            cards_player[0] in self.special_cards
            and cards_player[1][1] == cards_player[2][1]
        ):
            return True
        return False

    def has_flower_p1(self):
        return self.has_flower(self.cards_player1)

    def has_flower_p2(self):
        return self.has_flower(self.cards_player2)

    def flower_points(self):
        special_cards_points = {
            (2, self.show_card[1]): 30,
            (4, self.show_card[1]): 29,
            (5, self.show_card[1]): 28,
            (10, self.show_card[1]): 27,
            (11, self.show_card[1]): 27,
        }
        second_special_cards_points = {
            (4, self.show_card[1]): 9,
            (5, self.show_card[1]): 8,
            (10, self.show_card[1]): 7,
            (11, self.show_card[1]): 7,
        }
        user1_points = 0
        user2_points = 0
        # contar envido
        # first card
        if self.cards_player1[0] in special_cards_points:
            user1_points += special_cards_points[self.cards_player1[0]]
        else:
            user1_points += self.cards_player1[0][0]
        # second card
        if self.cards_player1[1] in special_cards_points:
            user1_points += second_special_cards_points[self.cards_player1[1]]
        else:
            user1_points += self.cards_player1[1][0]
        # third card
        user1_points += self.cards_player1[2][0]

        # first card
        if self.cards_player2[0] in special_cards_points:
            user2_points += special_cards_points[self.cards_player2[0]]
        else:
            user2_points += self.cards_player2[0][0]
        # second card
        if self.cards_player2[1] in special_cards_points:
            user2_points += second_special_cards_points[self.cards_player2[1]]
        else:
            user2_points += self.cards_player2[1][0]
        # third card
        user2_points += self.cards_player2[2][0]

        if user1_points > user2_points:
            self.hand_score_1 += 3
            return 1
        elif user1_points < user2_points:
            self.hand_score_2 += 3
            return 2
        else:
            self.hand_score_1 += 3
            return 1
