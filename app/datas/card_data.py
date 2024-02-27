# Масти карт
PEAK = "♠"
CHERVI = "♥"
KREST = "♣"
BUBEN = "♦"

# Список всех мастей карт
ALL_SUITS = [PEAK, CHERVI, KREST, BUBEN]

# Порядок мастей карт (отображаются в формате словаря {"♠": 0, "♥": 1})
ORDER_SUITS = {nominal: index for index, nominal in enumerate(ALL_SUITS)}

# Список достоинств карт
NOMINALS = ["6", "7", "8", "9", "10", "J", "Q", "K", "A"]

# Порядок достоинств карт (отображаются в формате словаря {"6": 0, "7": 1})
ORDER_NOMINALS = {nominal: index for index, nominal in enumerate(NOMINALS)}

# Полная колода (каждая масть по каждому номиналу) - 36 карт (отображаются в формате словаря [("6", "♠"), ("6", "♥")])
_DECK = [(nom, suit) for nom in NOMINALS for suit in ALL_SUITS]
