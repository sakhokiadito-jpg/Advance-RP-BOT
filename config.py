import os

API_FOOTBALL_KEY = "cdf4e1bd879fe741fb012b4b054e9fac"
TOKEN = os.environ.get("BOT_TOKEN", "")

ADMIN_IDS = [
    8413337840,
    7395293179,
    7637671496,
]

# ====== КАЗИНО ======
CASINO_BET   = 500
CASINO_PRIZE = 1000

# ====== СТАРТОВЫЙ БАЛАНС ======
START_BALANCE = 150_000  # 1500 € × 100 ₽

# ====== КУЛДАУНЫ ======
SALARY_COOLDOWN = 90 * 60
BIZ_COOLDOWN    = 3 * 60 * 60

# ====== КАЗИНО ШАНС ======
CASINO_WIN_CHANCE = 45

# ====== БАНК ======
BANK_DEPOSIT_RATE_PER_HOUR = 0.005
BANK_CREDIT_RATE_PER_HOUR  = 0.01
CREDIT_LIMIT_MULT          = 2.0

# ====== КУРС USD/RUB (обновляется динамически) ======
USD_RUB_RATE: float = 90.0   # fallback, реальный курс обновляется каждые 5 мин

# ====== ЧАТЫ ======
REGISTRATION_CHAT_ID  = -1003387594559
REGISTRATION_TOPIC_ID = 14
GAME_CHAT_ID          = -1003387594559
