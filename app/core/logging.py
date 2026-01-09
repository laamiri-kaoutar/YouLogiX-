import logging
import sys
from loguru import logger

# 1. The "Bridge" Class
# This class acts as a bridge. It grabs logs from Uvicorn (the server)
# and passes them to Loguru so everything ends up in the same file.
class InterceptHandler(logging.Handler):
    def emit(self, record):
        # Find the corresponding Loguru level (INFO, ERROR, etc.)
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # Send the log to Loguru
        logger.opt(depth=6, exception=record.exc_info).log(level, record.getMessage())

def configure_logging():
    # 2. Remove default handlers
    # We remove the default console logger to avoid seeing double logs
    logging.getLogger().handlers = [InterceptHandler()]
    
    # 3. Configure the File Output
    # This creates a folder named 'logs' and a file 'app.log'
    logger.add(
        "logs/app.log",             # The file path
        rotation="10 MB",           # New file when size > 10MB
        retention="7 days",         # Delete logs older than 7 days
        level="INFO",               # Capture INFO, WARNING, ERROR, etc.
        enqueue=True                # simpler async writing
    )

    # 4. Configure the Console Output (Optional but recommended for Docker)
    # This ensures you still see logs in your VS Code terminal
    logger.add(sys.stderr, level="INFO")

    # 5. Tell Uvicorn to use our Bridge
    # This specifically targets FastAPI/Uvicorn loggers
    logging.getLogger("uvicorn.access").handlers = [InterceptHandler()]
    logging.getLogger("uvicorn.error").handlers = [InterceptHandler()]