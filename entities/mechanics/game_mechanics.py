__author__ = "6966753, Khalil, 7340644, Hassel"
__email__ = "s7114097@stud.uni-frankfurt.de, s8911049@rz.uni-frankfurt.de"

import entities.mechanics.init_players as init_players
from entities.mechanics.stack import CardStack
from entities.player.bot import Bot
from entities.player.player_interface import PlayerInterface
from entities.player.user import User
from entities.states.game_states import AskPlayerForCardAndPlayer, GameInitialState
from ui.ui_interface import UIInterface


class GameMechanics:

    def __init__(self, ui: UIInterface):
        """
            Constructor which initializes the game.
        """
        self.ui = ui
        self.players = init_players.create_players(self.ui)
        self.stack = CardStack()
        self.state = GameInitialState()

    def start_game(self):
        self.stack.mix(self.players)

        self.ui.show_current_hand(self.players, self.stack)

        for player in self.players:
            if player.has_quartet():
                player.remove_all_quartet(
                    callback=lambda player, card: self.ui.show_player_has_found_a_quartet(player, card))

        while self.players_have_cards(self.players):
            for player in self.players:
                if self.players_have_cards(self.players):
                    self.ui.show_current_move(player)
                    self.ask_player_for_card(player)
                else:
                    # todo show winner
                    # self.ui.show_current_hand(self.players, self.stack)
                    break

    def ask_player_for_card(self, player: PlayerInterface):
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
                    callback=lambda player, card: self.ui.show_player_has_found_a_quartet(player, card))
                self.ui.show_current_hand(self.players, self.stack)
                if self.players_have_cards(self.players):
                    self.ask_player_for_card(player)
            else:
                if not (self.stack.is_stack_empty()):
                    card = self.stack.get_random_card()

                    self.ui.show_player_gets_card_from_stack(player, card)
                    player.add_card(card)
                    self.ui.show_current_move(player)

    def players_have_cards(self, players: [PlayerInterface]):
        for player in players:
            if not player.has_cards():
                return False
        return True
