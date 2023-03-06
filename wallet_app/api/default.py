import logging
import time

from django.http import HttpRequest, JsonResponse

logger = logging.getLogger(__name__)


async def default_handler(_: HttpRequest) -> JsonResponse:
    logger.debug("this is test logging")
    return JsonResponse({"time": time.asctime()})
