from flask import Blueprint, render_template, request, redirect, url_for, flash
from services.register_service import get_all_registers, create_register

register_bp = Blueprint("register", __name__)

@register_bp.route("/register_list", methods=["GET"])
def register_list():
    page_name = "Register List Page"
    users = get_all_registers()

    data_list = {
        "page_name": page_name,
        "users": users or []
    }

    return render_template("register/list.html", data_list=data_list)


@register_bp.route("/register_form", methods=["GET", "POST"])
def register_form():
    page_name = "Register Page"
    data_list = {"page_name": page_name}

    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        if username and email and password:
            result = create_register(username, email, password)
            if result:
                return redirect(url_for("register.register_list"))
            else:
                data_list["message"] = "ไม่สามารถเพิ่มผู้ใช้ได้ (อาจมีข้อมูลซ้ำ)"
        else:
            data_list["message"] = "กรุณากรอกข้อมูลให้ครบถ้วน"

    return render_template("register/form.html", data_list=data_list)