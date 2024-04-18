import logging
import time

from fastapi import Request


async def log_requests(request: Request, call_next):
    """
    Middleware to log details about each request including method, URL, execution time, delay status, and response status code.

    Args:
        request (Request): The incoming HTTP request.
        call_next: A function that proceeds to the next middleware or endpoint handler.

    Returns:
        The response object resulting from the request.

    This function logs the request method and URL, the time taken to execute the request, categorizes the execution speed,
    and logs the response status code. Requests taking longer than 0.5 seconds are marked as "SLOW".
    """
    logger = logging.getLogger('request')
    start_time = time.time()
    response = await call_next(request)
    execution_time = time.time() - start_time
    status = "OK" if execution_time < 0.5 else "SLOW"
    logger.info(
        f"Request {request.method} {request.url}, Time: {execution_time:.2f} sec, Delay Status: {status}, Response status: {response.status_code}")
    return response
