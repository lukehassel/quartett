from domain.entities.player.player_base import PlayerBase

class AllPlayers:

    def players_have_cards(self, players: [PlayerBase]):
        for player in players:
            if not player.has_cards():
                return False
        return True

    def calculate_winner(self, players: [PlayerBase]):
        winner = max(players, key=lambda x: x.get_quartet_count())
        winners = []
        lista = players.copy()
        lista.remove(winner)
        for lista in players:
            if lista.get_quartet_count() == winner.get_quartet_count():
                winners.append(lista)
        return winners
