import click
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

import importlib
import pkgutil
import models  # ต้องมี __init__.py ใน models/

from df_data import ingest_data  # สำหรับเรียก funtion ในการ import ข้อมูล


#  ฟังก์ชันโหลด models แบบ dynamic
def load_models_dynamically(db):
    for _, module_name, _ in pkgutil.iter_modules(models.__path__):
        module = importlib.import_module(f"models.{module_name}")
        if hasattr(module, "create_model"):
            module.create_model(db)


#  ตั้งค่า Flask App + DB
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)


@click.group()
def cli():
    """Custom CLI tool"""
    pass


@cli.command("migrate-all")
def migrate_all():
    """สร้างตารางทั้งหมดในฐานข้อมูล"""
    with app.app_context():
        load_models_dynamically(db)  #  โหลด models ก่อนสร้าง
        db.create_all()
        click.secho(" Tables created successfully.", fg="green")


@cli.command()
def import_data():
    click.secho("Start Import Register", fg="green")
    ingest_data.import_register()


if __name__ == "__main__":
    cli()
