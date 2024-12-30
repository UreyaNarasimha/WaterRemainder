from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'rmijlkqqqawtre@1((11'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Mysql#123@localhost/WaterRemainder'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)
migrate=Migrate(app,db)
api = Api(app)

with app.app_context():
    db.create_all() 

from . remainder import WaterRemainder, UserRegistration

api.add_resource(WaterRemainder, "/waterremainder")
api.add_resource(UserRegistration, "/userregister")