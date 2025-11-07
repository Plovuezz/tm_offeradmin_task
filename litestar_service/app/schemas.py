from typing import List, Optional
from uuid import UUID
from pydantic import BaseModel, field_validator
from pydantic.functional_validators import model_validator
from pydantic_core.core_schema import FieldValidationInfo
from models.models import OfferChoices
from models.models import Offer, OfferWallOffer, OfferWallPopupOffer, OfferWall


class OfferSchema(BaseModel):
    model_config = {
        "from_attributes": True
    }

    uuid: UUID
    id: int
    url: Optional[str] = None
    is_active: bool
    name: OfferChoices
    sum_to: Optional[str] = None
    term_to: Optional[int] = None
    percent_rate: Optional[int] = None


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
