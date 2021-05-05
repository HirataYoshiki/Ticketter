from apps.Users.Routers import router as users_router
from apps.Tickets.Routers import router as tickets_router
from apps.Interactions.Routers import router as interactions_router

routers = [
  users_router,
  tickets_router,
  interactions_router
]