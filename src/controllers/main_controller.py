from flask import Blueprint,render_template,request

main_bp = Blueprint("main",__name__)

@main_bp.route("/")
def home():
    
    page_name = 'Home Page'

    
    data_list={
       'page_name' :page_name,
    }
    
    return render_template("/home/index.html",data_list=data_list)
 
@main_bp.route('/list')
def list_page():
   page_name = 'List Page'
   
   user_list = [
        {"name": "สมชาย", "email": "somchai@example.com", "role": "admin"},
        {"name": "สมชาย2", "email": "somchai2@example.com", "role": "admin"},
        {"name": "สมหญิง", "email": "somying@example.com", "role": "editor"},
        {"name": "ก้อง", "email": "kong@example.com", "role": "viewer"}
    ]
   
   role_p = request.args.get("role")
   if role_p:
      user_list = [
         x for x in user_list if x['role'] == role_p
      ]

   
    
   data_list={
       'page_name' :page_name,
       'user_list':user_list
    }
   
   return render_template("/list/index.html",data_list=data_list)