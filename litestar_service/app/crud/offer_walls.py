from typing import Optional
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from database.models import OfferWall, OfferWallOffer, OfferWallPopupOffer
from database.models import OfferChoices


async def get_offerwall_by_token(session: AsyncSession, token: UUID) -> Optional[OfferWall]:
    stmt = (
        select(OfferWall)
        .where(OfferWall.token == token)
        .options(
            selectinload(OfferWall.offer_assignments).selectinload(OfferWallOffer.offer),
            selectinload(OfferWall.popup_assignments).selectinload(OfferWallPopupOffer.offer),
        )
    )
    res = await session.execute(stmt)
    return res.scalars().first()


def get_offer_names_list() -> list[str]:
    return [c.value for c in OfferChoices]
