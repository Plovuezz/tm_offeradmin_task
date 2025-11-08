from litestar import Litestar, Router
from litestar.exceptions import NotFoundException

from api.offerwalls import router
from exceptions import not_found_error_handler


def build_app() -> Litestar:
    return Litestar(
        route_handlers=[
            Router(
                path="/api",
                route_handlers=[router]
            )
        ],
        exception_handlers={NotFoundException: not_found_error_handler}
    )
