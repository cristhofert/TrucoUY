""""
Copyright © Krypton 2019-2023 - https://github.com/kkrypt0nn (https://krypton.ninja)
Description:
🐍 A simple template to start to code your own and personalized discord bot in Python programming language.

Version: 6.1.0
"""

import platform
import random

import aiohttp
import discord
from discord import app_commands
from discord.ext import commands
from discord.ext.commands import Context


class General(commands.Cog, name="general"):
    SIGN = (":wine_glass:", ":dagger:", ":herb:", ":coin:")
    round = 0
    cards_player1 = []
    cards_player2 = []
    played_card_p1 = []
    played_card_p2 = []
    score_p1 = 0
    score_p2 = 0
    current_player = 1
    limit_score = 10
    deck = []
    show_card = (0, "")
    special_cards = []
    order_number = []

    def __init__(self, bot) -> None:
        self.bot = bot
        self.context_menu_user = app_commands.ContextMenu(
            name="Grab ID", callback=self.grab_id
        )
        self.bot.tree.add_command(self.context_menu_user)
        self.context_menu_message = app_commands.ContextMenu(
            name="Remove spoilers", callback=self.remove_spoilers
        )
        self.bot.tree.add_command(self.context_menu_message)

    # Message context menu command
    async def remove_spoilers(
        self, interaction: discord.Interaction, message: discord.Message
    ) -> None:
        """
        Removes the spoilers from the message. This command requires the MESSAGE_CONTENT intent to work properly.

        :param interaction: The application command interaction.
        :param message: The message that is being interacted with.
        """
        spoiler_attachment = None
        for attachment in message.attachments:
            if attachment.is_spoiler():
                spoiler_attachment = attachment
                break
        embed = discord.Embed(
            title="Message without spoilers",
            description=message.content.replace("||", ""),
            color=0xBEBEFE,
        )
        if spoiler_attachment is not None:
            embed.set_image(url=attachment.url)
        await interaction.response.send_message(embed=embed, ephemeral=True)

    # User context menu command
    async def grab_id(
        self, interaction: discord.Interaction, user: discord.User
    ) -> None:
        """
        Grabs the ID of the user.

        :param interaction: The application command interaction.
        :param user: The user that is being interacted with.
        """
        embed = discord.Embed(
            description=f"The ID of {user.mention} is `{user.id}`.",
            color=0xBEBEFE,
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @commands.hybrid_command(
        name="help", description="List all commands the bot has loaded."
    )
    async def help(self, context: Context) -> None:
        prefix = self.bot.config["prefix"]
        embed = discord.Embed(
            title="Help", description="List of available commands:", color=0xBEBEFE
        )
        for i in self.bot.cogs:
            if i == "owner" and not (await self.bot.is_owner(context.author)):
                continue
            cog = self.bot.get_cog(i.lower())
            commands = cog.get_commands()
            data = []
            for command in commands:
                description = command.description.partition("\n")[0]
                data.append(f"{prefix}{command.name} - {description}")
            help_text = "\n".join(data)
            embed.add_field(
                name=i.capitalize(), value=f"```{help_text}```", inline=False
            )
        await context.send(embed=embed)

    @commands.hybrid_command(
        name="botinfo",
        description="Get some useful (or not) information about the bot.",
    )
    async def botinfo(self, context: Context) -> None:
        """
        Get some useful (or not) information about the bot.

        :param context: The hybrid command context.
        """
        embed = discord.Embed(
            description="Used [Krypton's](https://krypton.ninja) template",
            color=0xBEBEFE,
        )
        embed.set_author(name="Bot Information")
        embed.add_field(name="Owner:", value="Krypton#7331", inline=True)
        embed.add_field(
            name="Python Version:", value=f"{platform.python_version()}", inline=True
        )
        embed.add_field(
            name="Prefix:",
            value=f"/ (Slash Commands) or {self.bot.config['prefix']} for normal commands",
            inline=False,
        )
        embed.set_footer(text=f"Requested by {context.author}")
        await context.send(embed=embed)

    @commands.hybrid_command(
        name="serverinfo",
        description="Get some useful (or not) information about the server.",
    )
    async def serverinfo(self, context: Context) -> None:
        """
        Get some useful (or not) information about the server.

        :param context: The hybrid command context.
        """
        roles = [role.name for role in context.guild.roles]
        num_roles = len(roles)
        if num_roles > 50:
            roles = roles[:50]
            roles.append(f">>>> Displaying [50/{num_roles}] Roles")
        roles = ", ".join(roles)

        embed = discord.Embed(
            title="**Server Name:**", description=f"{context.guild}", color=0xBEBEFE
        )
        if context.guild.icon is not None:
            embed.set_thumbnail(url=context.guild.icon.url)
        embed.add_field(name="Server ID", value=context.guild.id)
        embed.add_field(name="Member Count", value=context.guild.member_count)
        embed.add_field(
            name="Text/Voice Channels", value=f"{len(context.guild.channels)}"
        )
        embed.add_field(name=f"Roles ({len(context.guild.roles)})", value=roles)
        embed.set_footer(text=f"Created at: {context.guild.created_at}")
        await context.send(embed=embed)

    @commands.hybrid_command(
        name="ping",
        description="Check if the bot is alive.",
    )
    async def ping(self, context: Context) -> None:
        """
        Check if the bot is alive.

        :param context: The hybrid command context.
        """
        embed = discord.Embed(
            title="🏓 Pong!",
            description=f"The bot latency is {round(self.bot.latency * 1000)}ms.",
            color=0xBEBEFE,
        )
        await context.send(embed=embed)

    @commands.hybrid_command(
        name="invite",
        description="Get the invite link of the bot to be able to invite it.",
    )
    async def invite(self, context: Context) -> None:
        """
        Get the invite link of the bot to be able to invite it.

        :param context: The hybrid command context.
        """
        embed = discord.Embed(
            description=f"Invite me by clicking [here]({self.bot.config['invite_link']}).",
            color=0xD75BF4,
        )
        try:
            await context.author.send(embed=embed)
            await context.send("I sent you a private message!")
        except discord.Forbidden:
            await context.send(embed=embed)

    @commands.hybrid_command(
        name="server",
        description="Get the invite link of the discord server of the bot for some support.",
    )
    async def server(self, context: Context) -> None:
        """
        Get the invite link of the discord server of the bot for some support.

        :param context: The hybrid command context.
        """
        embed = discord.Embed(
            description=f"Join the support server for the bot by clicking [here](https://discord.gg/mTBrXyWxAF).",
            color=0xD75BF4,
        )
        try:
            await context.author.send(embed=embed)
            await context.send("I sent you a private message!")
        except discord.Forbidden:
            await context.send(embed=embed)

    @commands.hybrid_command(
        name="8ball",
        description="Ask any question to the bot.",
    )
    @app_commands.describe(question="The question you want to ask.")
    async def eight_ball(self, context: Context, *, question: str) -> None:
        """
        Ask any question to the bot.

        :param context: The hybrid command context.
        :param question: The question that should be asked by the user.
        """
        answers = [
            "It is certain.",
            "It is decidedly so.",
            "You may rely on it.",
            "Without a doubt.",
            "Yes - definitely.",
            "As I see, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again later.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful.",
        ]
        embed = discord.Embed(
            title="**My Answer:**",
            description=f"{random.choice(answers)}",
            color=0xBEBEFE,
        )
        embed.set_footer(text=f"The question was: {question}")
        await context.send(embed=embed)

    @commands.hybrid_command(
        name="bitcoin",
        description="Get the current price of bitcoin.",
    )
    async def bitcoin(self, context: Context) -> None:
        """
        Get the current price of bitcoin.

        :param context: The hybrid command context.
        """
        # This will prevent your bot from stopping everything when doing a web request - see: https://discordpy.readthedocs.io/en/stable/faq.html#how-do-i-make-a-web-request
        async with aiohttp.ClientSession() as session:
            async with session.get(
                "https://api.coindesk.com/v1/bpi/currentprice/BTC.json"
            ) as request:
                if request.status == 200:
                    data = await request.json(
                        content_type="application/json"
                    )  # For some reason the returned content is of type JavaScript
                    embed = discord.Embed(
                        title="Bitcoin price",
                        description=f"The current price is {data['bpi']['USD']['rate']} :dollar:",
                        color=0xBEBEFE,
                    )
                else:
                    embed = discord.Embed(
                        title="Error!",
                        description="There is something wrong with the API, please try again later",
                        color=0xE02B2B,
                    )
                await context.send(embed=embed)

    def card(self, card: tuple) -> str:
        return f"{card[0]}{card[1]}   "

    @commands.hybrid_command(
        name="nueva",
        description="Nueva partida.",
    )
    async def new(self, context: Context) -> None:
        """
        Get the current price of bitcoin.

        :param context: The hybrid command context.
        """
        self.deck = [
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
        self.match = []
        self.played_card_p1 = []
        self.played_card_p2 = []
        self.score_p1 = 0
        self.score_p2 = 0
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
        self.round = 1

        embed = discord.Embed(
            title="Jugador 1",
            description=f"{self.card(self.cards_player1[0])}{self.card(self.cards_player1[1])}{self.card(self.cards_player1[2])} ",
            color=0xB9B91E,
        )

        await context.send(embed=embed)

        embed = discord.Embed(
            title="Jugador 2",
            description=f"{self.card(self.cards_player2[0])}{self.card(self.cards_player2[1])}{self.card(self.cards_player2[2])} ",
            color=0xB9B91E,
        )

        await context.send(embed=embed)

        embed = discord.Embed(
            title="Muestra",
            description=f"{self.card(self.show_card)} ",
            color=0xB9B91E,
        )

        await context.send(embed=embed)

    @commands.hybrid_command(
        name="j",
        description="Nueva mano.",
    )
    async def play(self, context: Context, *, data: str) -> None:
        """ """
        data = data.split(" ")
        card_number: int = int(data[0])
        card_sign: str = data[1]

        SIGN = (":wine_glass:", ":dagger:", ":herb:", ":coin:")

        alt_sign = [
            "🍷",
            "🗡️",
            "🌿",
            "🪙",
        ]
        if card_sign in alt_sign:
            card_sign = self.SIGN[alt_sign.index(card_sign)]
        if card_number not in range(1, 12):
            embed = discord.Embed(
                title="ERROR",
                description=f" No es un numero valido {card_number}",
                color=0xDD0000,
            )

            await context.send(embed=embed)
            return
        elif card_sign not in self.SIGN:
            print(card_sign, self.SIGN)
            embed = discord.Embed(
                title="ERROR",
                description=f" No es un signo valido {card_sign}",
                color=0xDD0000,
            )

            await context.send(embed=embed)
            return
        if self.current_player == 1:
            cards_player = self.cards_player1
        else:
            cards_player = self.cards_player2

        if (card_number, card_sign) not in cards_player:
            embed = discord.Embed(
                title="ERROR",
                description=f" No tienes esa carta {card_number} {card_sign}",
                color=0xDD0000,
            )

            await context.send(embed=embed)
            return

        played_card = (card_number, card_sign)
        if self.current_player == 1:
            self.played_card_p1 = played_card
            print(self.cards_player1, played_card)
            self.cards_player1.remove(played_card)
        else:
            self.played_card_p2 = played_card
            print(self.cards_player2, played_card)
            self.cards_player2.remove(played_card)

        embed = discord.Embed(
            title=f"Jugador {self.current_player} ha jugado {self.card(played_card)}",
            description=f"la carta muestra es {self.card(self.show_card)}",
            color=0xB9B91E,
        )

        await context.send(embed=embed)

        if self.current_player == 1:
            self.current_player = 2
        else:
            # Verificar quien gano la mano
            o_p1 = self.played_card_p1[0]
            o_p2 = self.played_card_p2[0]
            if o_p1 > o_p2:
                self.score_p1 += 1
            elif o_p1 < o_p2:
                self.score_p2 += 1
            else:
                pass

            stick_score_p1 = self.score_p1
            stick_score_p2 = self.score_p2
            embed = discord.Embed(
                title="Jugador 1 | Jugador 2",
                description=f"""
{stick_score_p1} | {stick_score_p2}""",
                color=0xFFFF90,
            )

            await context.send(embed=embed)

            description = ""
            for i in self.cards_player1:
                description += f"{self.card(i)} "

            embed = discord.Embed(
                title="Jugador 1",
                description=description,
                color=0xB9B91E,
            )

            await context.send(embed=embed)

            description = ""
            for i in self.cards_player2:
                description += f"{self.card(i)} "
            embed = discord.Embed(
                title="Jugador 2",
                description=description,
                color=0xB9B91E,
            )

            await context.send(embed=embed)

            embed = discord.Embed(
                title="Muestra",
                description=f"{self.card(self.show_card)} ",
                color=0xB9B91E,
            )

            await context.send(embed=embed)

            self.current_player = 1
            if self.round == 3:
                self.round = 0
                self.cards_player1 = []
                self.cards_player2 = []
                self.played_card_p1 = []
                self.played_card_p2 = []
                self.deck = [
                    (1, self.SIGN[0]),
                    (2, self.SIGN[0]),
                    (3, self.SIGN[0]),
                    (4, self.SIGN[0]),
                    (5, self.SIGN[0]),
                    (6, self.SIGN[0]),
                    (7, self.SIGN[0]),
                    (8, self.SIGN[0]),
                    (9, self.SIGN[0]),
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
                    (8, self.SIGN[1]),
                    (9, self.SIGN[1]),
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
                    (8, self.SIGN[2]),
                    (9, self.SIGN[2]),
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
                    (8, self.SIGN[3]),
                    (9, self.SIGN[3]),
                    (10, self.SIGN[3]),
                    (11, self.SIGN[3]),
                    (12, self.SIGN[3]),
                ]
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

                description = ""
                for i in self.cards_player1:
                    description += f"{self.card(i)} "

                embed = discord.Embed(
                    title="Jugador 1",
                    description=description,
                    color=0xB9B91E,
                )

                await context.send(embed=embed)

                description = ""
                for i in self.cards_player2:
                    description += f"{self.card(i)} "
                embed = discord.Embed(
                    title="Jugador 2",
                    description=description,
                    color=0xB9B91E,
                )

                await context.send(embed=embed)

                embed = discord.Embed(
                    title="Muestra",
                    description=f"{self.card(self.show_card)} ",
                    color=0xB9B91E,
                )

                await context.send(embed=embed)

            else:
                self.round += 1


async def setup(bot) -> None:
    await bot.add_cog(General(bot))
