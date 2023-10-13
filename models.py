from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base, relationship, backref

Base = declarative_base()

class Claims(Base):
    __tablename__ = 't_claims'

    claim_trans = Column(Integer, primary_key=True)
    claim_id = Column(Integer)
    claim_item = Column(Integer)
    mem_acct = Column(Integer)
    injury_disease_id = Column(Integer, ForeignKey("t_injury_disease.id"), nullable=False)
    specialty_id = Column(Integer, ForeignKey("t_specialty.id"), nullable=False)
    facility_class_id = Column(Integer, ForeignKey("t_facility_class.id"), nullable=False)
    charge_allowed = Column(Integer)

    def __repr__(self):
        return (
            f"Claims(claim_trans={self.claim_trans!r},"
            f"claim_id={self.claim_id!r}, claim_item={self.claim_item!r}, mem_acct={self.mem_acct!r}, injury_disease={self.injury_disease_id!r}, specialty_id={self.specialty_id}, facility_class_id={self.facility_class_id}, charge_allowed={self.charge_allowed}"
        )


class ClaimsPaid(Base):
    __tablename__ = "t_claims_paid"

    pay_trans = Column(String, primary_key=True)
    claim_trans = Column(Integer, ForeignKey("t_claims.claim_trans"), nullable=False)
    charge_allowed = Column(Integer)
    deduct_copay = Column(Integer)
    charge_trans_date = Column(String)
    period = Column(Integer)
    quarter = Column(String)

    def __repr__(self):
        return (
            f"ClaimsPaid(pay_trans={self.pay_trans!r},"
            f"claim_trans={self.claim_trans}, charge_allowed={self.charge_allowed}, deduct_copay={self.deduct_copay}, charge_trans_date={self.charge_trans_date}, period={self.period}, quarter={self.quarter}"
        )



class InjuryDisease(Base):
    __tablename__ = 't_injury_disease'

    id = Column(Integer, primary_key=True)
    injury_disease_title = Column(String)

    claims = relationship('Claims', backref=backref('t_injury_disease'),
                          cascade="all, delete-orphan")


class Specialty(Base):
    __tablename__ = 't_specialty'

    id = Column(Integer, primary_key=True)
    specialty_title = Column(String)

    claims = relationship('Claims', backref=backref('t_specialty'),
                          cascade='all, delete-orphan')


class FacilityClass(Base):
    __tablename__ = 't_facility_class'

    id = Column(Integer, primary_key=True)
    facility_class_title = Column(String)

    claims = relationship('Claims', backref=backref('t_facility_class'),
                          cascade='all, delete-orphan')


class ClaimCountV(Base):
    __tablename__ = 'v_claim_count'

    Period = Column(Integer, primary_key=True)
    Claim_Count = Column(Integer)