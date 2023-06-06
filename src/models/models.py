from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database.config import Base
from sqlalchemy.sql import func


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    created = Column(DateTime(timezone=True), server_default=func.now())


class Status(Base):
    __tablename__ = 'status'
    id = Column(Integer, primary_key=True, index=True)
    status_name = Column(String)


class Subscription(Base):
    __tablename__ = 'subscription'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('user.id', name='fk_user'), nullable=False)
    status_id = Column(Integer, ForeignKey('status.id', name='fk_status'), nullable=False)
    created = Column(DateTime(timezone=True), server_default=func.now())
    modified = Column(DateTime(timezone=True), onupdate=func.now())
    # user = relationship('User', back_populates='subscription')
    # status = relationship('Status', back_populates='subscription')


class EventHistory(Base):
    __tablename__ = 'event_history'
    id = Column(Integer, primary_key=True, index=True)
    subscription_id = Column(Integer, ForeignKey('subscription.id', name='fk_subscription'), nullable=False)
    type = Column(String)
    created = Column(DateTime(timezone=True), server_default=func.now())
    # subscription = relationship('Subscription', back_populates='event_history')
