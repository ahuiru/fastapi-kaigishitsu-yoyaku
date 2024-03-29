from sqlalchemy.orm import Session
from . import models, schemas

# ユーザー一覧
def get_users(db: Session, skip: int=0, limit: int=100):
  return db.query(models.User).offset(skip).limit(limit).all()

# 会議室一覧
def get_rooms(db: Session, skip: int=0, limit: int=100):
  return db.query(models.Room).offset(skip).limit(limit).all()

# 予約一覧
def get_bookings(db: Session, skip: int=0, limit: int=100):
  return db.query(models.Booking).offset(skip).limit(limit).all()


# ユーザー作成
def create_user(db: Session, user: schemas.User):
  # インスタンスの生成
  db_user = models.User(user_name=user.user_name)
  db.add(db_user)
  db.commit()
  db.refresh(db_user)
  return db_user

# 会議室作成
def create_room(db: Session, room: schemas.Room):
  # インスタンスの生成
  db_room = models.Room(room_name=room.room_name, capacity=room.capacity)
  db.add(db_room)
  db.commit()
  db.refresh(db_room)
  return db_room

# 予約作成
def create_booking(db: Session, booking: schemas.Booking):
  # インスタンスの生成
  db_booking = models.Booking(
    user_id=booking.user_id,
    room_id=booking.room_id,
    booked_num=booking.booked_num,
    start_datetime=booking.start_datetime,
    end_datetime=booking.end_datetime,
  )
  db.add(db_booking)
  db.commit()
  db.refresh(db_booking)
  return db_booking
