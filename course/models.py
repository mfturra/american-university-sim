from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

# initialize the SQLAlchemy object
db = SQLAlchemy()

# student class config
class Student(db.Model):
    __tablename__ = 'students'
    id =            db.Column(db.Integer, primary_key=True)
    firstname =     db.Column(db.String(100), nullable=False)
    lastname =      db.Column(db.String(100), nullable=False)
    email =         db.Column(db.String(80), unique=True, nullable=False)
    age =           db.Column(db.Integer)
    created_at =    db.Column(db.DateTime(timezone=True),
                        server_default=func.now())

# institution class config
class Institution(db.Model):
    __tablename__ = "institutions"

    id =            db.Column(db.Integer, primary_key=True)
    inst_type =     db.Column(db.String(30), nullable=False)
    uni_name =      db.Column(db.String(30), unique=True, nullable=False)
    uni_type =      db.Column(db.String(25), unique=True, nullable=False)
    uni_welcome =   db.Column(db.String(300), nullable=False)
    uni_cost =      db.Column(db.Float(precision=2), unique=False, nullable=False)
    # degrees =       db.relationship("Degree", back_populates="institution")

# degree class config
class Degree(db.Model):
    __tablename__ = "degrees"

    # "unique=True" = Not duplicates
    id =                        db.Column(db.Integer, primary_key=True)
    degree_track =              db.Column(db.String(30), nullable=False)
    degree_name =               db.Column(db.String(30), nullable=False)
    degree_desc =               db.Column(db.String(500), nullable=False)
    curriculum_difficulty =     db.Column(db.Float(precision=2), nullable=False)
    uni_id =                    db.Column(db.Integer, db.ForeignKey("institutions.id"), nullable=False)
    # institution =               db.relationship("Institution", back_populates="degrees")