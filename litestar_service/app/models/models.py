import uuid
from enum import Enum
from sqlalchemy import Column, String, Boolean, Integer, Text, ForeignKey, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from base import Base


class OfferChoices(str, Enum):
    Loanplus = "Loanplus"
    SgroshiCPA2 = "SgroshiCPA2"
    Novikredyty = "Novikredyty"
    TurboGroshi = "TurboGroshi"
    Crypsee = "Crypsee"
    Suncredit = "Suncredit"
    Lehko = "Lehko"
    Monto = "Monto"
    Limon = "Limon"
    Amigo = "Amigo"
    FirstCredit = "FirstCredit"
    Finsfera = "Finsfera"
    Pango = "Pango"
    Treba = "Treba"
    StarFin = "StarFin"
    BitCapital = "BitCapital"
    SgroshiCPL = "SgroshiCPL"
    LoviLave = "LoviLave"
    Prostocredit = "Prostocredit"
    Sloncredit = "Sloncredit"
    Clickcredit = "Clickcredit"
    Credos = "Credos"
    Dodam = "Dodam"
    SelfieCredit = "SelfieCredit"
    Egroshi = "Egroshi"
    Alexcredit = "Alexcredit"
    SgroshiCPA1 = "SgroshiCPA1"
    Tengo = "Tengo"
    Credit7 = "Credit7"
    Tpozyka = "Tpozyka"
    Creditkasa = "Creditkasa"
    Moneyveo = "Moneyveo"
    My_Credit = "MyCredit"
    Credit_Plus = "CreditPlus"
    Miloan = "Miloan"
    Avans = "AvansCredit"


class Offer(Base):
    __tablename__ = "offer"

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    id = Column(Integer, nullable=False)
    url = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
    name = Column(String, unique=True)
    sum_to = Column(String, nullable=True)
    term_to = Column(Integer, nullable=True)
    percent_rate = Column(Integer, nullable=True)

    wall_assignments = relationship("OfferWallOffer", back_populates="offer")
    popup_assignments = relationship("OfferWallPopupOffer", back_populates="offer")


class OfferWall(Base):
    __tablename__ = "offer_wall"

    token = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=True)
    url = Column(String, nullable=True)
    description = Column(Text, nullable=True)

    offer_assignments = relationship(
        "OfferWallOffer", back_populates="offer_wall", order_by="OfferWallOffer.order"
    )
    popup_assignments = relationship(
        "OfferWallPopupOffer", back_populates="offer_wall", order_by="OfferWallPopupOffer.order"
    )


class OfferWallOffer(Base):
    __tablename__ = "offer_wall_offer"

    id = Column(Integer, primary_key=True)
    offer_wall_id = Column(ForeignKey("offer_wall.token"))
    offer_id = Column(ForeignKey("offer.uuid"))
    order = Column(Integer, default=0)

    offer_wall = relationship("OfferWall", back_populates="offer_assignments")
    offer = relationship("Offer", back_populates="wall_assignments")


class OfferWallPopupOffer(Base):
    __tablename__ = "offer_wall_popup_offer"

    id = Column(Integer, primary_key=True)
    offer_wall_id = Column(ForeignKey("offer_wall.token"))
    offer_id = Column(ForeignKey("offer.uuid"))
    order = Column(Integer, default=0)

    offer_wall = relationship("OfferWall", back_populates="popup_assignments")
    offer = relationship("Offer", back_populates="popup_assignments")

    __table_args__ = (
        UniqueConstraint("offer_wall_id", "offer_id", name="uix_offer_wall_offer"),
    )
