# authentication.py

import jwt
import datetime
from functools import wraps
from flask import request, jsonify
from app.config import SECRET_KEY

def generate_token(username):
    try:
        payload = {
            'username': username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        return token
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Bearer '):
            return jsonify({'message': 'Invalid token format'}), 401

        token = auth_header.split(' ')[1]
        
        try:
            data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token'}), 401

        request.current_user = data['username']
        return f(*args, **kwargs)

    return decorated
