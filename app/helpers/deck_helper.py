from app.helpers.base_helper import Base


class Deck(Base):
    def __init__(self, player_id, deck_name, cards):
        super().__init__(player_id, deck_name, cards)
        self.player_id = player_id
        self.deck_name = deck_name
        self.cards = cards
