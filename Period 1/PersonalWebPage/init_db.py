from database import create_app, db

app = create_app()

# Create database tables
with app.app_context():
    print("Creating database and tables...")
    db.create_all()
    print("Database setup complete!")