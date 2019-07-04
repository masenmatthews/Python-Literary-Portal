import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Book(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    year = db.Column(db.String, nullable=False)
    reviews = db.relationship("Review", backref="book", lazy=True)

    def add_review(self, title, rating, body):
        r = Review(title=title, rating=rating, body=body, book_id=self.id)
        db.session.add(r)
        db.session.commit()


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)


class Review(db.Model):
    __tablename__ = "reviews"

    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey("books.id"), nullable=False)
    title = db.Column(db.String, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    body = db.Column(db.String, nullable=False)