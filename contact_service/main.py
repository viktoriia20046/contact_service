from fastapi import FastAPI, Request, Depends
from slowapi import Limiter
from slowapi.util import get_remote_address
from fastapi.middleware.cors import CORSMiddleware
import aioredis

# Ініціалізація FastAPI
app = FastAPI()

# Налаштування CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Дозволити всі домени
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Налаштування Rate Limiting
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter

# Налаштування Redis
@app.on_event("startup")
async def startup():
    app.state.redis = await aioredis.from_url("redis://localhost")  # Підключення до Redis

@app.on_event("shutdown")
async def shutdown():
    await app.state.redis.close()  # Закриття з'єднання з Redis

# Маршрут із обмеженням кількості запитів
@app.get("/limited-endpoint/")
@limiter.limit("5/minute")  # Максимум 5 запитів на хвилину
async def limited_route(request: Request):  # Додано аргумент request
    return {"message": "This is a rate-limited route"}

# Маршрут із кешуванням у Redis
@app.get("/cached/")
async def cached_example(redis=Depends(lambda: app.state.redis)):
    await redis.set("key", "value")  # Збереження даних у Redis
    value = await redis.get("key")  # Отримання даних із Redis
    return {"cached_value": value.decode()}

# Основний маршрут
@app.get("/")
def root():
    return {"message": "Contact Service API is running"}