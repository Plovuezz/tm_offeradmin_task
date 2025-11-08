from typing import Any, Annotated
from uuid import UUID

from litestar import get, Router
from litestar.di import Provide
from litestar.exceptions import NotFoundException
from sqlalchemy.ext.asyncio import AsyncSession

from database.db import get_session
from schemas import OfferWallSchema
from crud.offer_walls import get_offerwall_by_token, get_offer_names_list


@get(
    "/{token:str}",
    response_model=OfferWallSchema,
    dependencies={"db_session": Provide(get_session)}
)
async def retrieve_offerwall(token: UUID, db_session: AsyncSession) -> Any:
    offerwall = await get_offerwall_by_token(db_session, token)
    if offerwall is None:
        raise NotFoundException(f"OfferWall with token={token} not found")
    return offerwall


@get("/get_offer_names")
async def get_offer_names() -> dict[str, list[str]]:
    return {"offer_names": get_offer_names_list()}


router = Router(
    path="/offerwalls",
    route_handlers=[retrieve_offerwall, get_offer_names],
)
