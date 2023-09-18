# main.py

from flask import Flask, request, jsonify
from app.authentication import token_required, generate_token
from app.tables.group_access import get_group_access_data, delete_group_access_by_id, update_group_access_by_id
from app.tables.provider import get_provider_data, delete_provider_by_id, update_provider_by_id
from app.tables.customer import get_customer_data, delete_customer_by_id, update_customer_by_id
from app.tables.userlogincred import get_userlogincred_data, delete_userlogincred_by_id, update_userlogincred_by_id
from app.tables.security_access import get_security_access_data, delete_security_access_by_id, update_security_access_by_id
from app.tables.user_access import get_user_access_data, delete_user_access_by_id, update_user_access_by_id
# Import other table modules here

app = Flask(__name__)

# @app.route('/login', methods=['POST'])
# def user_login():
#     return login()

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    print(username)
    password = request.json.get('password')
    print(password)

    # Replace this with your actual authentication logic (e.g., database lookup)
    if username == 'valid_user' and password == 'valid_password':
        token = generate_token(username)
        return jsonify({'token': token}), 200
    else:
        return jsonify({'message': 'Authentication failed'}), 401

@app.route('/get_group_access_data', methods=['GET'])
@token_required
def fetch_group_access_data():
    return get_group_access_data()

@app.route('/delete_group_access_data/<int:group_access_id>', methods=['DELETE'])
@token_required
def del_group_access_data(group_access_id):
    return delete_group_access_by_id(group_access_id)

@app.route('/update_group_access_data/<int:group_access_id>', methods=['PUT'])
@token_required
def update_group_access_data(group_access_id):
    try:
        updated_data = request.json

        response, status_code = update_group_access_by_id(group_access_id, updated_data)

        # Return the response and status code
        return response, status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/get_provider_data', methods=['GET'])
@token_required
def fetch_provider_data():
    return get_provider_data()

@app.route('/delete_provider_data/<int:provider_id>', methods=['DELETE'])
@token_required
def del_provider_data(provider_id):
    return delete_provider_by_id(provider_id)

@app.route('/update_provider_data/<int:provider_id>', methods=['PUT'])
@token_required
def update_provider_data(provider_id):
    try:
        updated_data = request.json

        response, status_code = update_provider_by_id(provider_id, updated_data)

        # Return the response and status code
        return response, status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/get_customer_data', methods=['GET'])
@token_required
def fetch_customer_data():
    return get_customer_data()

@app.route('/delete_customer_data/<int:customer_id>', methods=['DELETE'])
@token_required
def del_customer_data(customer_id):
    return delete_customer_by_id(customer_id)

@app.route('/update_customer_data/<int:customer_id>', methods=['PUT'])
@token_required
def update_customer_data(customer_id):
    try:
        updated_data = request.json

        response, status_code = update_customer_by_id(customer_id, updated_data)

        # Return the response and status code
        return response, status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/get_userlogincred_data', methods=['GET'])
@token_required
def fetch_userlogincred_data():
    return get_userlogincred_data()

@app.route('/delete_userlogincred_data/<int:userlogincred_id>', methods=['DELETE'])
@token_required
def del_userlogincred_data(userlogincred_id):
    return delete_userlogincred_by_id(userlogincred_id)

@app.route('/update_userlogincred_data/<int:userlogincred_id>', methods=['PUT'])
@token_required
def update_userlogincred_data(userlogincred_id):
    try:
        updated_data = request.json

        response, status_code = update_userlogincred_by_id(userlogincred_id, updated_data)

        # Return the response and status code
        return response, status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/get_security_access_data', methods=['GET'])
@token_required
def fetch_security_access_data():
    return get_security_access_data()

@app.route('/delete_security_access_data/<int:security_access_id>', methods=['DELETE'])
@token_required
def del_group_security_data(security_access_id):
    return delete_security_access_by_id(security_access_id)

@app.route('/update_security_access_data/<int:security_access_id>', methods=['PUT'])
@token_required
def update_security_access_data(security_access_id):
    try:
        updated_data = request.json

        response, status_code = update_security_access_by_id(security_access_id, updated_data)

        # Return the response and status code
        return response, status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/get_user_access_data', methods=['GET'])
@token_required
def fetch_user_access_data():
    return get_user_access_data()

@app.route('/delete_user_access_data/<int:user_access_id>', methods=['DELETE'])
@token_required
def del_user_access_data(user_access_id):
    return delete_user_access_by_id(user_access_id)

@app.route('/update_user_access_data/<int:user_access_id>', methods=['PUT'])
@token_required
def update_user_access_data(user_access_id):
    try:
        updated_data = request.json

        # Call the update_user_access_by_id function to update the user access data
        response, status_code = update_user_access_by_id(user_access_id, updated_data)

        # Return the response and status code
        return response, status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run()


# TO DO
# Update query
