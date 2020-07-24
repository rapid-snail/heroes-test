import os

# url стенда возьмем из переменной окружения
HEROES_BASE_URL = os.environ.get("HEROES_BASE_URL", "http://localhost")
