import uuid
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from models.register import create_model
from sqlalchemy import text

# ✅ Flask + SQLAlchemy setup
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

# ✅ Load dynamic model
Register = create_model(db)


def import_register():
    with app.app_context():
        try:
            # ✅ ล้างข้อมูลเก่า
            table_name = Register.__table__.name
            db.session.execute(
                text(f'TRUNCATE TABLE "{table_name}" RESTART IDENTITY CASCADE')
            )

            # ✅ เพิ่มข้อมูลใหม่โดยไม่กำหนด id
            objects = [
                Register(
                    username="admin",
                    email="admin@example.com",
                    password_hash="hashed_admin",
                ),
                Register(
                    username="testuser",
                    email="test@example.com",
                    password_hash="hashed_test",
                ),
            ]

            db.session.bulk_save_objects(objects)
            db.session.commit()
            print("✅ Imported register data successfully.")
        except Exception as e:
            db.session.rollback()
            print(f"❌ Error importing register: {e}")
        finally:
            db.session.close()
