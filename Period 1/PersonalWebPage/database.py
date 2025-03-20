from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# Initialize the database object
db = SQLAlchemy()

def create_app():
    """Create and configure the Flask app."""
    app = Flask(__name__)

    # Configure SQLite database
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.path.join(BASE_DIR, 'database.db')}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Initialize the database with the app
    db.init_app(app)

    return app

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    username = db.Column(db.Integer, nullable=False)  # Foreign key to User table

    def __repr__(self):
        return f"<Comment {self.content[:20]}>"