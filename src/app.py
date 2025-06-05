from flask import Flask
from controllers.main_controller import main_bp
from controllers.register_controller import register_bp


app = Flask(__name__)



app.register_blueprint(main_bp)
app.register_blueprint(register_bp)




if __name__=="__main__":
    app.run(debug=True)