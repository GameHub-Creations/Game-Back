import pytest

from app.games.chicken import ch


class TestsPlayChicken:

    @pytest.mark.parametrize('valid_cards', [
        (('6', '♠'), ('6', '♥')),
        (('7', '♣'), ('7', '♦')),
        (('7', '♦'), ('7', '♦')),
        (('7', '♣'), ('10', '♣')),
    ])
    def test_positive_check_card_match(self, valid_cards):
        """Позитивная проверка сравнения масти карт"""
        results = ch.card_match(*valid_cards)
        if valid_cards in [(('7', '♦'), ('7', '♦')), (('7', '♣'), ('10', '♣'))]:
            assert results is True
        else:
            assert results is False

    @pytest.mark.parametrize('invalid_cards', [
        ('6', ('6', '♥')),
        (('7', ' '), ('7', '♦')),
        ((7, '♦'), ('7', '♦')),
        (('7', '♣'), ('10', None)),
        (('7', '♣'), None),
        (None, None),
    ])
    def test_negative_check_card_match(self, invalid_cards):
        """Негативная проверка сравнения масти карт"""
        results = ch.card_match(*invalid_cards)
        assert 'Переданы невалидные данные' in results

    @pytest.mark.parametrize('player', [('first', 'second')])
    def test_positive_check_end_of_game(self, player):
        """Позитивная проверка окончания игры"""
        ch.object_closed_deck.cards = []
        if player == 'first':
            ch.object_first_player.cards = []
        else:
            ch.object_first_player.cards = [('7', '♣')]
            ch.object_second_player.cards = []
        results = ch.end_of_game()
        if player == 'first':
            assert results == f'Конец игры!\nПобедил игрок: "{ch.object_first_player.player_id}"'
        else:
            assert results == f'Конец игры!\nПобедил игрок: "{ch.object_second_player.player_id}"'
