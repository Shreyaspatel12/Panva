# tables/userlogincred.py

from flask import jsonify
from app.database import connect_to_database

def get_userlogincred_data():
    conn = connect_to_database()
    try:
        cursor = conn.cursor()
        query = 'SELECT * FROM UserLoginCredential'
        cursor.execute(query)
        rows = cursor.fetchall()

        data = []
        for row in rows:
            usercred_id = row[0]
            source_id = row[1]
            tenant_id = row[2]
            usertype_id = row[3]
            username = row[4]
            password = row[5]
            is_active = row[6]
            is_social = row[7]
            social_type = row[8]
            social_identity = row[9]
            is_deleted = row[10]
            is_restpassword = row[11]
            created_by = row[12]
            created_on = row[13]
            updated_by = row[14]
            updated_on = row[15]

            row_data = {
                'UserCredID': usercred_id,
                'SourceID': source_id,
                'TenantID': tenant_id,
                'UserTypeID': usertype_id,
                'UserName': username,
                'Password': password,
                'IsActive': is_active,
                'IsSocial': is_social,
                'SocialType': social_type,
                'SocialIdentity': social_identity,
                'IsDeleted': is_deleted,
                'IsRestPassword': is_restpassword,
                'CreatedBy': created_by,
                'CreatedOn': created_on,
                'UpdatedBy': updated_by,
                'UpdatedOn': updated_on,
            }

            data.append(row_data)

        return jsonify(data), 200
    except Exception as error:
        return jsonify({"error": str(error)}), 500
    finally:
        conn.close()

def delete_userlogincred_by_id(usercred_id):
    conn = connect_to_database()
    try:
        cursor = conn.cursor()
        query = 'DELETE FROM UserLoginCredential WHERE UserCredID = %s'
        cursor.execute(query, (usercred_id,))
        conn.commit()

        if cursor.rowcount > 0:
            return jsonify({"message": f"Row with ID {usercred_id} deleted successfully"}), 200
        else:
            return jsonify({"message": f"No rows found with ID {usercred_id}"}), 404
    except Exception as error:
        conn.rollback()  # Roll back changes if an error occurs
        return jsonify({"error": str(error)}), 500
    finally:
        conn.close()

def update_userlogincred_by_id(usercred_id, updated_data):
    conn = connect_to_database()
    try:
        cursor = conn.cursor()

        # Check if the user login credential record exists
        check_query = 'SELECT * FROM UserLoginCredential WHERE UserCredID = %s'
        cursor.execute(check_query, (usercred_id,))
        existing_row = cursor.fetchone()

        if not existing_row:
            return jsonify({"message": f"No row found with UserCredID {usercred_id}"}), 404

        # Construct the UPDATE query
        update_query = """
            UPDATE UserLoginCredential
            SET
                SourceID = %s,
                TenantID = %s,
                UserTypeID = %s,
                UserName = %s,
                Password = %s,
                IsActive = %s,
                IsSocial = %s,
                SocialType = %s,
                SocialIdentity = %s,
                IsDeleted = %s,
                IsRestPassword = %s,
                CreatedBy = %s,
                CreatedOn = %s,
                UpdatedBy = %s,
                UpdatedOn = %s
            WHERE UserCredID = %s
        """

        # Extract values from the updated_data dictionary or use existing values
        values = (
            updated_data.get('SourceID', existing_row[1]),
            updated_data.get('TenantID', existing_row[2]),
            updated_data.get('UserTypeID', existing_row[3]),
            updated_data.get('UserName', existing_row[4]),
            updated_data.get('Password', existing_row[5]),
            updated_data.get('IsActive', existing_row[6]),
            updated_data.get('IsSocial', existing_row[7]),
            updated_data.get('SocialType', existing_row[8]),
            updated_data.get('SocialIdentity', existing_row[9]),
            updated_data.get('IsDeleted', existing_row[10]),
            updated_data.get('IsRestPassword', existing_row[11]),
            updated_data.get('CreatedBy', existing_row[12]),
            updated_data.get('CreatedOn', existing_row[13]),
            updated_data.get('UpdatedBy', existing_row[14]),
            updated_data.get('UpdatedOn', existing_row[15]),
            usercred_id,
        )

        # Update the row with the provided data
        cursor.execute(update_query, values)
        conn.commit()

        if cursor.rowcount > 0:
            return jsonify({"message": f"Row with UserCredID {usercred_id} updated successfully"}), 200
        else:
            return jsonify({"message": f"No rows updated with UserCredID {usercred_id}"}), 404
    except Exception as error:
        conn.rollback()
        return jsonify({"error": str(error)}), 500
    finally:
        conn.close()