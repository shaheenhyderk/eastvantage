import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import custom modules
from app.api.routes import api_router
from app.core.config import settings
from app.core.exception_handler import add_exception_handlers
from app.core.logger import setup_loggers
from app.core.middlewares import log_requests
from app.db.engine import create_db_and_tables

# Setup the FastAPI application
app = FastAPI(title=settings.PROJECT_NAME)

# Setup logging
setup_loggers()

# CORS middleware configuration
# This allows cross-origin requests from any origin.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Add custom request logging middleware
app.middleware("http")(log_requests)

# Add global exception handlers
add_exception_handlers(app)

# Include the main router from api_router with a URL prefix from settings
app.include_router(api_router, prefix=settings.ROOT_URL_PREFIX)


# Startup event handler
@app.on_event("startup")
async def startup_event():
    logger = logging.getLogger('server')
    logger.info("Server starting up...")
    # Create database and tables, typically should be idempotent
    create_db_and_tables()


# Shutdown event handler
@app.on_event("shutdown")
async def shutdown_event():
    logger = logging.getLogger('server')
    logger.info("Server shutting down...")
