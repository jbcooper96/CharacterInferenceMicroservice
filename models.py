from app import db
from typing import List
from sqlalchemy.orm import Mapped, mapped_column, relationship
from flask_login import UserMixin
from sqlalchemy import ForeignKey, DateTime, desc
import uuid
from datetime import datetime

class User(db.Model, UserMixin):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    devices: Mapped[List["Device"]] = relationship()

    @classmethod
    def find_by_name(cls, username):
        return cls.query.filter_by(username=username).first()
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

class Person(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    chats: Mapped[List["Chat"]] = relationship()

    @classmethod
    def get_or_create_by_name(cls, name):
        person = cls.query.filter_by(name=name).first()
        if person == None:
            person = Person(name=name)
            person.save_to_db()
        return person

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

class Character(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    prompt: Mapped[str]
    chats: Mapped[List["Chat"]] = relationship()

    @classmethod
    def get_by_name(cls, name):
        return cls.query.filter_by(name=name).first()
    
    @classmethod
    def get_all_paginated(cls, page_size=10, page=1):
        return cls.query.limit(page_size*page)
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

class Chat(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str]
    response: Mapped[str]
    token_count: Mapped[int]
    person: Mapped[int] = mapped_column(ForeignKey("person.id"))
    character: Mapped[int] = mapped_column(ForeignKey("character.id"))
    created_at: Mapped[DateTime] = db.Column(DateTime, default=datetime.now())

    @classmethod
    def get_chats_for_person_and_character(cls, person, character):
        return cls.query.filter_by(person=person.id, character=character.id).order_by(desc(Chat.created_at))
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


class Device(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    device_name: Mapped[str]
    device_key: Mapped[str]
    user: Mapped[int] = mapped_column(ForeignKey("user.id"))

    def __init__(self, device_name, user_id, device_key=None):
        self.device_name = device_name
        self.user = user_id
        self.device_key = device_key or uuid.uuid4().hex

    def json(self):
        return {
            'device_name': self.device_name, 
            'device_key': self.device_key, 
            'user_id': self.user
        }
    
    @classmethod
    def find_by_name(cls, device_name):
        return cls.query.filter_by(device_name=device_name).first()
    
    @classmethod
    def find_by_device_key(cls, device_key):
        return cls.query.filter_by(device_key=device_key).first()
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
