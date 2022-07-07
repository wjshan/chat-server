from fastapi import APIRouter

from chat_server.exceptions.base_errors import UrlNotFindError, ValidateError
from .chat import router as chat_router
main_router = APIRouter(prefix="/api", responses={
    422: {"model": ValidateError},
    404: {"model": UrlNotFindError},
})
main_router.include_router(chat_router, tags=["chat"])
