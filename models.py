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

    inj_dis = relationship("Injury_Disease", backref=backref('t_claims'),
                           cascade="all, delete-orphan")

    specialty = relationship("Specialty", backref=backref('t_claims'),
                             cascade="all, delete-orphan")

    facility_class = relationship("Facility_Class", backref=backref('t_claims'),
                                  cascade="all, delete-orphan")

    def __repr__(self):
        return (
            f"Claims(claim_trans={self.claim_trans!r},"
            f"claim_id={self.claim_id!r}, claim_item={self.claim_item!r}, mem_acct={self.mem_acct!r}, injury_disease={self.injury_disease_id!r}, specialty_id={self.specialty_id}, facility_class_id={self.facility_class_id}, charge_allowed={self.charge_allowed}"
        )


class Injury_Disease(Base):
    __tablename__ = 't_injury_disease'

    id = Column(Integer, primary_key=True)
    injury_disease_title = Column(String)

    claims = relationship('Claims', backref=backref('t_injury_disease'),
                          cascade="all, delete-orphan")


class Specialty(Base):
    __tablename__ = 't_specialty'


class Facility_Class(Base):
    __tablename__ = 't_facility_class'