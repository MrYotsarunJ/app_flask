from flask import Blueprint,render_template,request
register_bp = Blueprint("register",__name__)

@register_bp.route("/register_form", methods=["GET", "POST"])
def register_form():
    page_name = 'Register Page'
    
    data_list={
       'page_name' :page_name,
    }
    
    
    if request.method == "POST":
        name_data = request.form.get('name')
        
        if name_data:
            data_list.update({
                "name_data":name_data
            })
            
            
            
    print(data_list)
    
    return render_template("/register/form.html",data_list=data_list)
 