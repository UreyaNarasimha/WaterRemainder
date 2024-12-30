from flask import jsonify, request
from flask_restx import Resource
from datetime import datetime
from . import db,app
from .models import Users
from .email_helper import start_email_thread, email_validator


class UserRegistration(Resource):

    def post(self):
        
        data = request.get_json()
        
        name = data.get('name')
        email = data.get('email')
        
        if not (name and email):
            msg = 'name and email are required fields'    
            return jsonify(status=400, data={}, message=msg)

        if not email_validator(email): # check valid email
            msg = 'Invalid email address'
            return jsonify(status=400, data={}, message=msg)

        try:
            user = Users.query.filter(Users.email == email).first()
            if user:
                if user.status == False:
                    msg = 'User disabled temporarily'
                    return jsonify(status=400, data={}, message=msg)
                msg = 'User already exist'
                return jsonify(status=400, data={}, message=msg)
            
            today = datetime.now()
            date_time_obj = today.strftime('%Y/%m/%d %H:%M:%S')
            status=True
            user = Users(name, email,status,date_time_obj, date_time_obj)
            db.session.add(user)
            db.session.commit()
            
            data  = {
                "name": name, 
                "email": email
                }
            
            return jsonify(status=200, data=data, message="Registered successfully")
        except:
            return jsonify(status=404, data={}, message="Something went wrong")

class WaterRemainder(Resource):
    
    def post(self):
        
        user_objs = db.session.query(Users).filter_by(status=True).all()
        if not user_objs:
            return jsonify(status=400, data={}, message="No data Found")
        
        email_trigger = start_email_thread(user_objs)
        if not email_trigger:
            return jsonify(status=400, data={}, message="Something went wrong")

        return jsonify(status=200, message="Remainder Sent Successfully", data={})
