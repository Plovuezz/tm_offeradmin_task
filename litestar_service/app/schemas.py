from typing import List, Optional
from uuid import UUID
from pydantic import BaseModel
from database.models import OfferChoices


class OfferSchema(BaseModel):
    model_config = {
        "from_attributes": True
    }

    uuid: UUID
    id: int
    url: str | None = None
    is_active: bool
    name: OfferChoices
    sum_to: str | None = None
    term_to: str | None = None
    percent_rate: str | None = None


class OfferWallOfferSchema(BaseModel):
    model_config = {
        "from_attributes": True
    }

    offer: OfferSchema


class OfferWallPopupOfferSchema(BaseModel):
    model_config = {
        "from_attributes": True
    }

    offer: OfferSchema

class OfferWallSchema(BaseModel):
    model_config = {
        "from_attributes": True
    }

    token: UUID
    name: Optional[str] = None
    url: Optional[str] = None
    description: Optional[str] = None
    offer_assignments: List[OfferWallOfferSchema] = []
    popup_assignments: List[OfferWallPopupOfferSchema] = []
