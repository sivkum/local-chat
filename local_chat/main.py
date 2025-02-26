"""FastAPI app creation, logger configuration and main API routes."""

from local_chat.di import global_injector
from local_chat.launcher import create_app

app = create_app(global_injector)
