""""
Copyright © Krypton 2019-2023 - https://github.com/kkrypt0nn (https://krypton.ninja)
Description:
🐍 A simple template to start to code your own and personalized discord bot in Python programming language.

Version: 6.1.0
"""

import discord
from discord.ext import commands
from discord.ext.commands import Context

from helpers.game import Game


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
        interaction.response.is_done()
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
        interaction.response.is_done()
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
        interaction.response.is_done()
        self.stop()

    def card(self, card: tuple) -> str:
        return f"{card[0]}{card[1]} "

    async def on_button_click(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        print("button.label")
        print(button.label)


class BetForPoints(discord.ui.View):

    def __init__(self, has_flower: bool) -> None:
        super().__init__()
        self.value = None
        for i, item in enumerate(self.children):
            if isinstance(item, discord.ui.Button):
                if item.custom_id == "points":
                    item.disabled = has_flower
                elif item.custom_id == "flower":
                    item.disabled = not has_flower

    @discord.ui.button(
        label="Envido",
        style=discord.ButtonStyle.blurple,
        disabled=True,
        custom_id="points",
    )
    async def points(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ) -> None:
        self.value = "points"
        interaction.response.is_done()
        self.stop()

    @discord.ui.button(
        label="Flor",
        style=discord.ButtonStyle.blurple,
        disabled=True,
        custom_id="flower",
    )
    async def flower(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ) -> None:
        self.value = "flower"
        interaction.response.is_done()
        self.stop()


class AcceptPoints(discord.ui.View):
    def __init__(self) -> None:
        super().__init__()
        self.value = None

    @discord.ui.button(label="Quiero", style=discord.ButtonStyle.blurple)
    async def confirm(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ) -> None:
        self.value = "accept"
        interaction.response.is_done()
        self.stop()

    @discord.ui.button(label="No Quiero", style=discord.ButtonStyle.blurple)
    async def cancel(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ) -> None:
        self.value = "decline"
        interaction.response.is_done()
        self.stop()

    @discord.ui.button(label="Re envido", style=discord.ButtonStyle.blurple)
    async def re(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ) -> None:
        self.value = "re"
        interaction.response.is_done()
        self.stop()

    @discord.ui.button(label="Al resto", style=discord.ButtonStyle.blurple)
    async def al(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ) -> None:
        self.value = "al"
        interaction.response.is_done()
        self.stop()


class AcceptRePoints(discord.ui.View):
    def __init__(self) -> None:
        super().__init__()
        self.value = None

    @discord.ui.button(label="Quiero", style=discord.ButtonStyle.blurple)
    async def confirm(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ) -> None:
        self.value = "accept"
        interaction.response.is_done()
        self.stop()

    @discord.ui.button(label="No Quiero", style=discord.ButtonStyle.blurple)
    async def cancel(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ) -> None:
        self.value = "decline"
        interaction.response.is_done()
        self.stop()


class AcceptBet(discord.ui.View):
    def __init__(self) -> None:
        super().__init__()
        self.value = None

    @discord.ui.button(label="Accept", style=discord.ButtonStyle.blurple)
    async def confirm(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ) -> None:
        self.value = "accept"
        interaction.response.is_done()
        self.stop()

    @discord.ui.button(label="Decline", style=discord.ButtonStyle.blurple)
    async def cancel(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ) -> None:
        self.value = "decline"
        interaction.response.is_done()
        self.stop()


class AcceptRe(discord.ui.View):
    def __init__(self) -> None:
        super().__init__()
        self.value = None

    @discord.ui.button(label="Accept", style=discord.ButtonStyle.blurple)
    async def confirm(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ) -> None:
        self.value = "accept"
        interaction.response.is_done()
        self.stop()

    @discord.ui.button(label="Decline", style=discord.ButtonStyle.blurple)
    async def cancel(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ) -> None:
        self.value = "decline"
        interaction.response.is_done()
        self.stop()


class AcceptAl(discord.ui.View):
    def __init__(self) -> None:
        super().__init__()
        self.value = None

    @discord.ui.button(label="Accept", style=discord.ButtonStyle.blurple)
    async def confirm(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ) -> None:
        self.value = "accept"
        interaction.response.is_done()
        self.stop()

    @discord.ui.button(label="Decline", style=discord.ButtonStyle.blurple)
    async def cancel(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ) -> None:
        self.value = "decline"
        interaction.response.is_done()
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
            interaction.response.is_done()
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
            interaction.response.is_done()
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
        interaction.response.is_done()
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

    async def points(self, propone, acepta):
        flower = False
        if self.game.current_player == 1:
            flower = self.game.has_flower_p1()
        else:
            flower = self.game.has_flower_p2()
        print(f"Flor: {flower}")
        bet_for_points = BetForPoints(flower)
        await propone.send(view=bet_for_points)
        await bet_for_points.wait()
        if bet_for_points.value == "points":
            # envido
            hand1_re_points = AcceptPoints()
            await acepta.send(view=hand1_re_points)
            await hand1_re_points.wait()
            if hand1_re_points.value == "confirm":
                p = self.game.count_points()
                if p == 1:
                    await self.both_send("Ganó el jugador 1")
                else:
                    await self.both_send("Ganó el jugador 2")
            elif hand1_re_points.value == "re":
                hand1_re_points = AcceptRePoints()
                await propone.send(view=hand1_re_points)
                await hand1_re_points.wait()
                if hand1_re_points.value == "accept":
                    p = self.game.count_points_re()
                    if p == 1:
                        await self.both_send("Ganó el jugador 1")
                    else:
                        await self.both_send("Ganó el jugador 2")
                else:
                    await self.both_send("Ganó el jugador 1")
            elif hand1_re_points.value == "al":
                hand1_al_points = AcceptAl()
                await propone.send(view=hand1_al_points)
                await hand1_al_points.wait()
                if hand1_al_points.value == "accept":
                    p = self.game.count_points_al()
                    if p == 1:
                        await self.both_send("Ganó el jugador 1")
                    else:
                        await self.both_send("Ganó el jugador 2")
                else:
                    await self.both_send("Ganó el jugador 1")
            else:
                await self.both_send("Ganó el jugador 1")
        elif bet_for_points.value == "flower":
            # contra flor
            p = self.game.flower_points()
            if p == 1:
                await self.both_send("Ganó el jugador 1")
            else:
                await self.both_send("Ganó el jugador 2")
        else:
            await self.both_send("Ganó el jugador 1")

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
                self.game.current_player = 1
                hand1_player1 = ShowCardsView(self.game.cards_player1)
                await self.game.user1.send(view=hand1_player1)
                # envido
                await self.points(self.game.user1, self.game.user2)
                await hand1_player1.wait()
                self.game.play(1, hand1_player1.value)
                await self.both_send(
                    f"{self.game.user1.name} jugó", view=Card(hand1_player1.value)
                )
                self.game.current_player = 2
                hand1_player2 = ShowCardsView(self.game.cards_player2)
                await self.game.user2.send(view=hand1_player2)
                await hand1_player2.wait()
                # await self.points(self.game.user2, self.game.user1)
                self.game.play(2, hand1_player2.value)
                await self.both_send(
                    f"{self.game.user2.name} jugó", view=Card(hand1_player2.value)
                )
                # segunda mano
                self.game.current_player = 1
                hand2_player1 = ShowCardsView(self.game.cards_player1)
                await self.game.user1.send(view=hand2_player1)
                await hand2_player1.wait()
                self.game.play(1, hand2_player1.value)
                await self.both_send(
                    f"{self.game.user1.name} jugó {self.card(hand2_player1.value)}"
                )
                self.game.current_player = 2
                hand2_player2 = ShowCardsView(self.game.cards_player2)
                await self.game.user2.send(view=hand2_player2)
                await hand2_player2.wait()
                self.game.play(2, hand2_player2.value)
                await self.both_send(
                    f"{self.game.user2.name} jugó {self.card(hand2_player2.value)}"
                )
                # tercer mano
                self.game.current_player = 1
                hand3_player1 = ShowCardsView(self.game.cards_player1)
                await self.game.user1.send(view=hand3_player1)
                await hand3_player1.wait()
                self.game.play(1, hand3_player1.value)
                await self.both_send(
                    f"{self.game.user1.name} jugó {self.card(hand3_player1.value)}"
                )
                self.game.current_player = 2
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


async def setup(bot) -> None:
    await bot.add_cog(Truco(bot))
