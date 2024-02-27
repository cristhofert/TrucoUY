""""
Copyright © Krypton 2019-2023 - https://github.com/kkrypt0nn (https://krypton.ninja)
Description:
🐍 A simple template to start to code your own and personalized discord bot in Python programming language.

Version: 6.1.0
"""

import random

import aiohttp
import discord
from discord.ext import commands
from discord.ext.commands import Context


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


class ShowCardsView(discord.ui.View):
    value = None

    def __init__(self, cards) -> None:
        super().__init__()
        for i, item in enumerate(self.children):
            if isinstance(item, discord.ui.Button):
                if item.custom_id == "button1":
                    if len(cards) >= 1:
                        item.label = cards[0][0]
                        item.emoji = cards[0][1]
                    else:
                        item.disabled = True
                        item.emoji = "📓"
                        item.label = ""
                elif item.custom_id == "button2":
                    if len(cards) >= 2:
                        item.label = cards[1][0]
                        item.emoji = cards[1][1]
                    else:
                        item.disabled = True
                        item.emoji = "📓"
                        item.label = ""
                elif item.custom_id == "button3":
                    if len(cards) >= 3:
                        item.label = cards[2][0]
                        item.emoji = cards[2][1]
                    else:
                        item.disabled = True
                        item.emoji = "📓"
                        item.label = ""

    @discord.ui.button(
        label="Button 1", custom_id="button1", style=discord.ButtonStyle.secondary
    )
    async def on_button1_click(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        self.value = (int(button.label), button.emoji.name)
        embed = discord.Embed(
            color=discord.Color.dark_teal(),
            title="Jugada",
            description=self.card((button.emoji, button.label)),
        )
        embed.set_author(
            name=interaction.user.name, icon_url=interaction.user.display_avatar.url
        )
        await interaction.response.send_message(embed=embed)
        self.stop()

    @discord.ui.button(
        label="Button 2", custom_id="button2", style=discord.ButtonStyle.secondary
    )
    async def on_button2_click(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        self.value = (int(button.label), button.emoji.name)
        embed = discord.Embed(
            color=discord.Color.dark_teal(),
            title="Jugada",
            description=self.card((button.emoji, button.label)),
        )
        embed.set_author(
            name=interaction.user.name, icon_url=interaction.user.display_avatar.url
        )
        await interaction.response.send_message(embed=embed)
        self.stop()

    @discord.ui.button(
        label="Button 3", custom_id="button3", style=discord.ButtonStyle.secondary
    )
    async def on_button3_click(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        self.value = (int(button.label), button.emoji.name)
        embed = discord.Embed(
            color=discord.Color.dark_teal(),
            title="Jugada",
            description=self.card((button.emoji, button.label)),
        )
        embed.set_author(
            name=interaction.user.name, icon_url=interaction.user.display_avatar.url
        )
        await interaction.response.send_message(embed=embed)
        self.stop()

    def card(self, card: tuple) -> str:
        return f"{card[0]}{card[1]} "

    async def on_button_click(
        self, button: discord.ui.Button, interaction: discord.Interaction
    ):
        print("button.label")
        print(button.label)


class AcceptPoints(discord.ui.View):
    def __init__(self) -> None:
        super().__init__()
        self.value = None

    @discord.ui.button(label="Accept", style=discord.ButtonStyle.blurple)
    async def confirm(
        self, button: discord.ui.Button, interaction: discord.Interaction
    ) -> None:
        self.value = "accept"
        self.stop()

    @discord.ui.button(label="Decline", style=discord.ButtonStyle.blurple)
    async def cancel(
        self, button: discord.ui.Button, interaction: discord.Interaction
    ) -> None:
        self.value = "decline"
        self.stop()

    @discord.ui.button(label="Re envido", style=discord.ButtonStyle.blurple)
    async def re(
        self, button: discord.ui.Button, interaction: discord.Interaction
    ) -> None:
        self.value = "re"
        self.stop()

    @discord.ui.button(label="Al resto", style=discord.ButtonStyle.blurple)
    async def al(
        self, button: discord.ui.Button, interaction: discord.Interaction
    ) -> None:
        self.value = "al"
        self.stop()


class AcceptBet(discord.ui.View):
    def __init__(self) -> None:
        super().__init__()
        self.value = None

    @discord.ui.button(label="Accept", style=discord.ButtonStyle.blurple)
    async def confirm(
        self, button: discord.ui.Button, interaction: discord.Interaction
    ) -> None:
        self.value = "accept"
        self.stop()

    @discord.ui.button(label="Decline", style=discord.ButtonStyle.blurple)
    async def cancel(
        self, button: discord.ui.Button, interaction: discord.Interaction
    ) -> None:
        self.value = "decline"
        self.stop()


class AcceptRe(discord.ui.View):
    def __init__(self) -> None:
        super().__init__()
        self.value = None

    @discord.ui.button(label="Accept", style=discord.ButtonStyle.blurple)
    async def confirm(
        self, button: discord.ui.Button, interaction: discord.Interaction
    ) -> None:
        self.value = "accept"
        self.stop()

    @discord.ui.button(label="Decline", style=discord.ButtonStyle.blurple)
    async def cancel(
        self, button: discord.ui.Button, interaction: discord.Interaction
    ) -> None:
        self.value = "decline"
        self.stop()


class AcceptAl(discord.ui.View):
    def __init__(self) -> None:
        super().__init__()
        self.value = None

    @discord.ui.button(label="Accept", style=discord.ButtonStyle.blurple)
    async def confirm(
        self, button: discord.ui.Button, interaction: discord.Interaction
    ) -> None:
        self.value = "accept"
        self.stop()

    @discord.ui.button(label="Decline", style=discord.ButtonStyle.blurple)
    async def cancel(
        self, button: discord.ui.Button, interaction: discord.Interaction
    ) -> None:
        self.value = "decline"
        self.stop()


class Players(discord.ui.View):
    value = 2
    user1 = None
    user2 = None

    def __init__(self) -> None:
        super().__init__()
        self.value = 2

    @discord.ui.button(
        label="Jugador 1", style=discord.ButtonStyle.blurple, custom_id="player1"
    )
    async def player1(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ) -> None:
        if interaction.user == self.user2:
            await interaction.response.send_message(
                "No puedes seleccionarte a ti mismo"
            )
            return

        self.user1 = interaction.user
        button.disabled = True
        self.player1_disabled = True
        # Actualiza la vista para reflejar el cambio
        await interaction.response.edit_message(view=self)
        if self.user2 is not None and self.user1 is not None:
            self.stop()

    @discord.ui.button(label="Jugador 2", style=discord.ButtonStyle.blurple)
    async def player2(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ) -> None:
        if interaction.user == self.user1:
            await interaction.response.send_message(
                "No puedes seleccionarte a ti mismo"
            )
            return
        self.user2 = interaction.user
        button.disabled = True
        self.player2_disabled = True
        # Actualiza la vista para reflejar el cambio
        await interaction.response.edit_message(view=self)
        if self.user2 is not None and self.user1 is not None:
            self.stop()


class Card(discord.ui.View):
    def __init__(self, card) -> None:
        super().__init__()
        for i, item in enumerate(self.children):
            if isinstance(item, discord.ui.Button):
                if item.custom_id == "card":
                    item.label = card[0]
                    item.emoji = card[1]

    @discord.ui.button(
        label="Card",
        custom_id="card",
        style=discord.ButtonStyle.secondary,
        disabled=True,
    )
    async def on_button1_click(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ) -> None:
        self.stop()


class Truco(commands.Cog, name="truco"):
    game = None

    def __init__(self, bot) -> None:
        self.bot = bot
        self.game = Game()

    def card(self, card: tuple) -> str:
        return f"{card[0]}{card[1]} "

    async def both_send(self, message=None, view=None, embed=None):
        await self.game.user1.send(message, view=view, embed=embed)
        await self.game.user2.send(message, view=view, embed=embed)

    @commands.hybrid_command(name="jugar", description="Empieza a jugar.")
    async def play(self, context: Context) -> None:
        """

        :param context: The hybrid command context.
        Arquitectura de la partida:
        1. Seleccionar la cantidad de jugadores
        2. Seleccionar las cartas
        3. Jugar
        4. Mostrar el resultado
        * Toda solo pasar datos a otros objetos y recibir los datos de otros objetos en esta función
        """
        # Verificar que se aun canal y no un DM
        if context.channel.type == discord.ChannelType.private:
            await context.send("No se puede iniciar partida en un mensaje directo.")
            return

        self.game.start()
        view = Players()
        await context.send("Selección de jugadores", view=view)
        await view.wait()
        self.game.user1 = view.user1
        self.game.user2 = view.user2
        do = True
        if view.value == 2:
            while do:
                # repartir cartas
                self.game.dealing()
                embed = discord.Embed(
                    title="Muestra",
                    description=f"{self.game.show_card[0]}{self.game.show_card[1]} ",
                    color=0xB9B91E,
                )
                await self.both_send(embed=embed)
                if self.game.user1 is None or self.game.user2 is None:
                    await self.both_send("No hay jugadores")
                    return
                # primera mano
                hand1_player1 = ShowCardsView(self.game.cards_player1)
                await self.game.user1.send(view=hand1_player1)
                await hand1_player1.wait()
                self.game.play(1, hand1_player1.value)
                await self.both_send(
                    f"{self.game.user1.name} jugó", view=Card(hand1_player1.value)
                )
                hand1_player2 = ShowCardsView(self.game.cards_player2)
                await self.game.user2.send(view=hand1_player2)
                await hand1_player2.wait()
                self.game.play(2, hand1_player2.value)
                await self.both_send(
                    f"{self.game.user2.name} jugó", view=Card(hand1_player2.value)
                )
                # segunda mano
                hand2_player1 = ShowCardsView(self.game.cards_player1)
                await self.game.user1.send(view=hand2_player1)
                await hand2_player1.wait()
                self.game.play(1, hand2_player1.value)
                await self.both_send(
                    f"{self.game.user1.name} jugó {self.card(hand2_player1.value)}"
                )
                hand2_player2 = ShowCardsView(self.game.cards_player2)
                await self.game.user2.send(view=hand2_player2)
                await hand2_player2.wait()
                self.game.play(2, hand2_player2.value)
                await self.both_send(
                    f"{self.game.user2.name} jugó {self.card(hand2_player2.value)}"
                )
                # tercer mano
                hand3_player1 = ShowCardsView(self.game.cards_player1)
                await self.game.user1.send(view=hand3_player1)
                await hand3_player1.wait()
                self.game.play(1, hand3_player1.value)
                await self.both_send(
                    f"{self.game.user1.name} jugó {self.card(hand3_player1.value)}"
                )
                hand3_player2 = ShowCardsView(self.game.cards_player2)
                await self.game.user2.send(view=hand3_player2)
                await hand3_player2.wait()
                self.game.play(2, hand3_player2.value)
                await self.both_send(
                    f"{self.game.user2.name} jugó {self.card(hand3_player2.value)}"
                )
                # Resultado
                self.game.result()
                # fin de la partida
                if self.game.surrender:
                    embed = discord.Embed(
                        title="Resultado",
                        description=f"Jugador {self.game.surrender_team} se fué",
                        color=0xB9B91E,
                    )
                    await self.both_send(embed=embed)
                    do = False
                print(
                    f"Jugador 1: {self.game.match_score_1} - Jugador 2: {self.game.match_score_2}"
                )
                if self.game.match_score_1 >= self.game.limit_score:
                    embed = discord.Embed(
                        title="Resultado",
                        description=f"Jugador 1 ganó {self.game.match_score_1} a {self.game.match_score_2}",
                        color=0xB9B91E,
                    )
                    await self.both_send(embed=embed)
                    do = False
                if self.game.match_score_2 >= self.game.limit_score:
                    embed = discord.Embed(
                        title="Resultado",
                        description=f"Jugador 2 ganó {self.game.match_score_2} a {self.game.match_score_1}",
                        color=0xB9B91E,
                    )
                    await self.both_send(embed=embed)
                    do = False

        else:
            print("No implementado")
            print(view.value)

    @commands.hybrid_command(name="truco", description="Comando para jugar al truco.")
    async def up_bet(self, context: Context) -> None:
        view = AcceptBet()
        if self.game.bet > 4:
            await self.both_send("No hay mas")
            return
        if self.game.bet == 1:
            bet_name = "Truco"
        elif self.game.bet == 2:
            bet_name = "Retruco"
        elif self.game.bet == 3:
            bet_name = "Vale cuatro"
        await self.both_send(bet_name, view=view)
        await view.wait()
        if view.value == "accept":
            await self.both_send("Aceptaste")
            self.game.bet += 1
        else:
            await self.both_send("No aceptaste")
            self.game.surrender = True

    @commands.hybrid_command(name="envido", description="Comando para jugar al envido.")
    async def points(self, context: Context) -> None:
        view = AcceptPoints()
        await self.both_send("Envido", view=view)
        await view.wait()
        if view.value == "accept":
            await self.both_send("Aceptaste")
            # se cuenta los puntos de las cartas
            # quien gane se lleva lso puntos
            if self.game.count_points() == 1:
                # el usuario que echo gana un punto
                await self.both_send("Ganó el jugador 1")
            else:
                # el usuario que echo gana un punto
                await self.both_send("Ganó el jugador 2")
        elif view.value == "re":
            re_view = AcceptRe()
            await self.both_send("Re envido", view=re_view)
            await re_view.wait()
            if re_view.value == "accept":
                await self.both_send("Aceptaste")
                # se cuenta los puntos de las cartas
                # quien gane se lleva lso puntos
                if self.game.count_points_re() == 1:
                    # el usuario que echo gana un punto
                    await self.both_send("Ganó el jugador 1")
                else:
                    # el usuario que echo gana un punto
                    await self.both_send("Ganó el jugador 2")
        elif view.value == "al":
            al_view = AcceptAl()
            await self.both_send("Al resto", view=al_view)
            await al_view.wait()
            if al_view.value == "accept":
                await self.both_send("Aceptaste")
                # se cuenta los puntos de las cartas
                # quien gane se lleva lso puntos
                if self.game.count_points_al() == 1:
                    # el usuario que echo gana un punto
                    await self.both_send("Ganó el jugador 1")
                else:
                    # el usuario que echo gana un punto
                    await self.both_send("Ganó el jugador 2")
        else:
            # el usuario que echo gana un punto
            await self.both_send("No aceptaste")


class Game(metaclass=SingletonMeta):
    SIGN = ("🍷", "🗡", "🌿", "🪙")
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
        self.deck = self.original_deck.copy()
        for card in self.deck:
            r = random.choice(self.deck)
            self.deck.remove(r)
            self.deck.append(card)
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
        self.cards_player1.sort(key=lambda x: self.order_number.index(x))
        self.cards_player2.sort(key=lambda x: self.order_number.index(x))

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
        special_cards_points = {
            (2, self.show_card[1]): 30,
            (4, self.show_card[1]): 29,
            (5, self.show_card[1]): 28,
            (10, self.show_card[1]): 27,
            (11, self.show_card[1]): 27,
        }
        user1_points = 0
        user2_points = 0
        # contar envido
        if self.cards_player1[0] in special_cards_points:
            user1_points += special_cards_points[self.cards_player1[0]]
        else:
            user1_points += self.cards_player1[0][0]
        user1_points += self.cards_player1[1][0]
        user1_points += self.cards_player1[2][0]

        if self.cards_player2[0] in special_cards_points:
            user2_points += special_cards_points[self.cards_player2[0]]
        else:
            user2_points += self.cards_player2[0][0]
        user2_points += self.cards_player2[1][0]
        user2_points += self.cards_player2[2][0]
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


async def setup(bot) -> None:
    await bot.add_cog(Truco(bot))
