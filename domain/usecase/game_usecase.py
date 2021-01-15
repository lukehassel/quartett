__author__ = "6966753, Khalil, 7340644, Hassel"
__email__ = "s7114097@stud.uni-frankfurt.de, s8911049@rz.uni-frankfurt.de"

import sys

import domain.entities.init_players as init_players
from domain.entities.all_players import AllPlayers
from domain.entities.player.bot import Bot
from domain.entities.player.player_base import PlayerBase
from domain.entities.player.user import User
from domain.entities.stack import CardStack
from ui.states.game_states import AskPlayerForCardAndPlayer, GameInitialState, GameNewRoundState, GameExitState
from ui.ui_interface import UIInterface


class GameUseCase:

    def __init__(self, ui: UIInterface):
        """
            Constructor which initializes the game.
        """
        self.ui = ui
        self.ui.show_start_message()
        self.state = None
        self.restarted = False
        self.all_players = AllPlayers()
        self.ui.set_callback_new_game(lambda: self.restart())
        self.players = init_players.create_players(self.ui)

        if not self.restarted:
            self.stack = CardStack()
            self.state = GameInitialState()
            self.start_game()

    def restart(self):
        self.restarted = True
        self.players = init_players.create_players(self.ui)

        print("player:    aaa: "+str(self.players))

        if not(self.players is None):
            self.state = GameNewRoundState()
            self.stack = CardStack()
            #self.all_players.resetGame(self.players)
            self.ui.show_new_round()
            self.start_game()

    def start_game(self):
        self.state = GameInitialState()
        self.stack.mix(self.players)

        self.ui.show_current_hand(self.players, self.stack)

        for player in self.players:
            if player.has_quartet():
                player.remove_all_quartet(
                    callback=lambda player1, card1: self.ui.show_player_has_found_a_quartet(player1, card1))

        while self.all_players.players_have_cards(self.players) and not (
                isinstance(self.state, type(GameNewRoundState()))):
            for player in self.players:

                if self.all_players.players_have_cards(self.players) and not (
                        isinstance(self.state, type(GameNewRoundState()))):
                    self.ui.show_current_move(player)
                    self.ask_player_for_card(player)
                else:
                    break
        if not (isinstance(self.state, type(GameNewRoundState()))):
            self.ui.show_current_hand(self.players, self.stack)
            winners = self.all_players.calculate_winner(self.players)
            self.ui.show_winner(winners)
            sys.exit("")
        else:
            self.start_game()

    def ask_player_for_card(self, player: PlayerBase):
        """
            the player asks for a card and looks whether the player is a user or a bot.
        """
        if isinstance(player, type(User(""))):
            self.state = self.ui.show_which_player(self.players, player)
        elif isinstance(player, type(Bot(""))):
            self.state = player.ask_player_for_card(self.players, player)
        if isinstance(self.state, type(AskPlayerForCardAndPlayer(None, None))):
            if self.state.player.has_card(self.state.card):
                player.add_card(self.state.card)
                self.state.player.remove_card(self.state.card)
                self.ui.show_card_move(self.state.player, player, self.state.card)
                player.remove_all_quartet(
                    callback=lambda player1, card1: self.ui.show_player_has_found_a_quartet(player1, card1))
                # self.ui.show_current_hand(self.players, self.stack)
                if self.all_players.players_have_cards(self.players):
                    self.ask_player_for_card(player)
            else:
                if not (self.stack.is_stack_empty()):
                    card = self.stack.get_random_card()

                    self.ui.show_player_gets_card_from_stack(player, card)
                    player.add_card(card)
        elif isinstance(self.state, type(GameExitState())):
            sys.exit("Spiel wurde beendet.")
