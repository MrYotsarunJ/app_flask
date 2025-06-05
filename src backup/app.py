from flask import Flask
from flask_sqlalchemy import SQLAlchemy  # ✅ เพิ่มบรรทัดนี้
from controllers.main_controller import main_bp
from controllers.register_controller import register_bp
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)  # ✅ สร้าง SQLAlchemy instance และผูกกับ app

app.register_blueprint(main_bp)
app.register_blueprint(register_bp)

print(app.config['SQLALCHEMY_DATABASE_URI'])

if __name__ == "__main__":
    app.run(debug=True)
