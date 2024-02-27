import random
from typing import List

from app.datas.card_data import _DECK, ALL_SUITS
from app.helpers.deck_helper import Deck


class Chicken:

    def __init__(self, players: List[str] = None, decks: List[str] = None):

        # Закрытая колода (копия базовой колоды)
        self.closed_deck = _DECK.copy()
        # Открытая колода
        self.open_deck = []

        # Мешаем карты в закрытой колоде
        random.shuffle(self.closed_deck)

        # Создаем объекты игроков
        # self.players = [Deck(_, []) for _ in players[: 2]]
        # self.object_first_player = self.PLAYERS[0]
        # self.object_second_player = self.PLAYERS[1]

        self.object_first_player = Deck(3333, 'first_player', [])
        self.object_second_player = Deck(4444, 'second_deck', [])

        # Создаем объекты колод
        self.object_open_deck = Deck(1000, 'open_deck', self.open_deck)
        self.object_closed_deck = Deck(1111, 'closed_deck', self.closed_deck)

        # Создаем объект временной колоды
        self.object_first_temporary_deck = Deck(1100, 'first_temporary_deck', [])

        # Создаем список объектов игроков
        self.list_object_player = [self.object_first_player, self.object_second_player]
        # Создаем список объектов колод
        self.list_object_deck = [self.object_first_player, self.object_second_player, self.object_open_deck,
                                 self.object_closed_deck, self.object_first_temporary_deck]


    @staticmethod
    def card_match(card1=tuple, card2=tuple):
        """Сравнивает масти карт"""
        error_message = f'Переданы невалидные данные:\n' \
                        f'card 1: "{card1}"\n' \
                        f'card 2: "{card2}'
        try:
            if type(card1) is not tuple or type(card2) is not tuple:
                return error_message
            else:
                for card in [card1, card2]:
                    if type(card) is tuple:
                        number, suit = card
                        for _ in [number, suit]:
                            if type(_) is not str:
                                return error_message
                            elif suit not in ALL_SUITS:
                                return error_message
            number1, suit1 = card1
            number2, suit2 = card2
            return suit1 == suit2
        except:
            return error_message

    def end_of_game(self):
        """Проверяет не окончена ли игра"""
        if not self.object_closed_deck.cards and not self.object_first_player.cards:
            return f'Конец игры!\nПобедил игрок: "{self.object_first_player.player_id}"'
        elif not self.object_closed_deck.cards and not self.object_second_player.cards:
            return f'Конец игры!\nПобедил игрок: "{self.object_second_player.player_id}"'

    def step(self, data):
        """Ход игрока"""
        for object_player in self.list_object_player:
            # Находим игрока сделавшего действие
            if object_player.player_id == data['player_id']:
                for object_deck in self.list_object_deck:
                    # Находим колоду из которой взяли карту
                    if object_deck.deck_name == data['deck_name']:
                        # Удаляем карту из указанной колоды
                        object_deck.remove_card(data['card'])
                        # Проверяем не окончена ли игра
                        end_of_game = self.end_of_game()
                        if end_of_game:
                            return end_of_game
                        # Если открытая колода пустая, то взятую карту кладем в неё
                        if not self.object_open_deck.cards:
                            self.object_open_deck.add_cards(data['card'])
                            break
                        # Если открытая колода не пустая, то взятую карту кладем во временную колоду 1
                        else:
                            self.object_first_temporary_deck.add_cards(data['card'])
                            # Сравниваем верхнюю карту открытой колоды с взятой картой
                            results = self.card_match(self.object_first_temporary_deck.cards[-1], data['card'])
                            # Если результат сравнения True,
                            # то взятую карту и все карты из открытой колоды добавляем игроку сделавшего ход.
                            # Чистим открытую и временную колоду
                            if results:
                                object_player.add_cards(data['card'])
                                object_player.add_cards(self.object_first_temporary_deck.cards, sort=True)
                                self.object_open_deck.cards = []
                                self.object_first_temporary_deck.cards = []
                                break
                            # Если результат сравнения False, то добавляем карту в открытую колоду и чистим временную колоду 1
                            else:
                                self.object_open_deck.add_cards(data['card'])
                                self.object_first_temporary_deck.card = []
                                break
                raise ValueError('Передано невалидное название колоды')
        raise ValueError('Передан невалидный ID игрока')


ch = Chicken()
