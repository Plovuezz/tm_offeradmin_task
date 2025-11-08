import typing

from litestar import Response, status_codes, MediaType
from litestar.exceptions import NotFoundException


def not_found_error_handler(_: object, exc: NotFoundException) -> Response[dict[str, typing.Any]]:
    return Response(
        media_type=MediaType.JSON,
        content={"detail": str(exc)},
        status_code=status_codes.HTTP_404_NOT_FOUND,
    )
