import logging

from fastapi import Request
from fastapi.responses import JSONResponse

# Logger for errors
error_logger = logging.getLogger('error')


async def general_exception_handler(request: Request, exc: Exception):
    # Log the exception
    error_logger.error(f"Unhandled exception: {str(exc)}", exc_info=True)
    # Return a generic error response
    return JSONResponse(status_code=500, content={"message": "An internal server error occurred"})


# Function to add all exception handlers to an app
def add_exception_handlers(app):
    app.add_exception_handler(Exception, general_exception_handler)
