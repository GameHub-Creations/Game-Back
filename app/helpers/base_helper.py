from app.datas.card_data import ORDER_NOMINALS, ORDER_SUITS


class Base:
    def __init__(self, player_id, deck_name, cards):
        self.player_id = player_id
        self.deck_name = deck_name
        self.cards = cards

    def sort_cards(self):
        """
        Сортирует карты по достоинству и масти
        Карты отображаются в формате: [('A, ♣'), ('6, ♦')]
        """
        self.cards.sort(key=lambda c: (ORDER_NOMINALS[c[0]], c[1]))
        self.cards.sort(key=lambda c: (ORDER_SUITS[c[1]], c[1]))
        return self.cards

    def add_cards(self, new_cards, sort=False):
        """Добавляет карту в колоду"""
        if type(new_cards) is list:
            for card in new_cards:
                self.cards.append(card)
        else:
            self.cards.append(new_cards)
        if sort:
            self.sort_cards()
        return self.cards

    def remove_card(self, card):
        """Удаляет карту из колоды"""
        self.cards.remove(card)
        self.sort_cards()
        return self.cards
