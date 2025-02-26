# start a fastapi server with uvicorn

import uvicorn

from local_chat.main import app
from local_chat.settings.settings import settings

# Set log_config=None to do not use the uvicorn logging configuration, and
# use ours instead. For reference, see below:
uvicorn.run(app, host="0.0.0.0", port=settings().server.port, log_config=None)
