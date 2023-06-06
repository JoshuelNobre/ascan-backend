from fastapi import FastAPI
from routes import event_history_route, status_route, subscription_route, user_route
from database.config import create_db


create_db()

app = FastAPI()

# User route
app.include_router(user_route.router)

# # Client route
# app.include_router(subscription_route.router)

# # Auth route
# app.include_router(status_route.router)

# # Service route
# app.include_router(event_history_route.router)