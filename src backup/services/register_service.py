from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from models.register import create_model
from sqlalchemy.exc import IntegrityError

# ⚙️ สร้าง app + db เพื่อให้ service ใช้ได้อิสระ
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

# โหลด Register model
Register = create_model(db)

# ✅ ดึงผู้ใช้ทั้งหมด
def get_all_registers():
    with app.app_context():
        return db.session.query(Register).all()
    
def create_register(username, email, password):
    with app.app_context():
        try:
            user = Register(
                username=username,
                email=email,
                password_hash=password
            )
            db.session.add(user)
            db.session.commit()
            return user
        except IntegrityError:
            db.session.rollback()
            return None