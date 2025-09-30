from sqlalchemy.orm import Session
from . import models, schemas

# Get single user by their ID
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

# Get single user by their email
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

# Get list of users with optional pagination
def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

# Create a new user
def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        name=user.name,
        email=user.email,
        phone_number=user.phone_number,
        address=user.address
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Update an existing user
def update_user(db: Session, user_id: int, user_update: schemas.UserCreate):
    db_user = get_user(db, user_id=user_id)
    if db_user:
        update_data = user_update.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_user, key, value)
        db.commit()
        db.refresh(db_user)
        return db_user
    return None

# Delete a user
def delete_user(db: Session, user_id: int):
    db_user = get_user(db, user_id=user_id)
    if db_user:
        db.delete(db_user)
        db.commit()
        return db_user
    return None