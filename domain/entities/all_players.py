from domain.entities.player.player_base import PlayerBase

class AllPlayers:

    def players_have_cards(self, players: [PlayerBase]):
        """
            :returns False if one player in the game has no more cards. Else it will return True
        """
        for player in players:
            if not player.has_cards():
                return False
        return True

    def calculate_winner(self, players: [PlayerBase]):
        """
        Calculates the winner. If two players have the same quartet count and if one player is the winner.
        Both players have then won.
        :param players: A list of all players.
        :return: A list of all the winners.
        """
        winner = max(players, key=lambda x: x.get_quartet_count())
        winners = []
        lista = players.copy()
        lista.remove(winner)
        for lista in players:
            if lista.get_quartet_count() == winner.get_quartet_count():
                winners.append(lista)
        return winners

    def resetGame(self, players: [PlayerBase]):
        """
        Resets the points and hand of all players

        :param players: A list of all players.
        """
        for player in players:
            player.reset()