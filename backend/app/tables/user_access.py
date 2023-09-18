# tables/user_access.py

from flask import jsonify
from app.database import connect_to_database

def get_user_access_data():
    conn = connect_to_database()
    try:
        cursor = conn.cursor()
        query = 'SELECT * FROM UserAccess'
        cursor.execute(query)
        rows = cursor.fetchall()

        data = []
        for row in rows:
            id = row[0]
            user_id = row[1]
            access_id = row[2]
            created_date = row[3]
            created_by = row[4]
            updated_date = row[5]
            updated_by = row[6]
            is_deleted = row[7]
            deleted_by = row[8]
            deleted_date = row[9]

            row_data = {
                'ID': id,
                'UserID': user_id,
                'AccessID': access_id,
                'CreatedDate': created_date,
                'CreatedBy': created_by,
                'UpdatedDate': updated_date,
                'UpdatedBy': updated_by,
                'IsDeleted': is_deleted,
                'DeletedBy': deleted_by,
                'DeletedDate': deleted_date,
            }

            data.append(row_data)

        return jsonify(data), 200
    except Exception as error:
        return jsonify({"error": str(error)}), 500
    finally:
        conn.close()

def delete_user_access_by_id(user_access_id):
    conn = connect_to_database()
    try:
        cursor = conn.cursor()
        query = 'DELETE FROM UserAccess WHERE ID = %s'
        cursor.execute(query, (user_access_id,))
        conn.commit()

        if cursor.rowcount > 0:
            return jsonify({"message": f"Row with ID {user_access_id} deleted successfully"}), 200
        else:
            return jsonify({"message": f"No rows found with ID {user_access_id}"}), 404
    except Exception as error:
        conn.rollback()
        return jsonify({"error": str(error)}), 500
    finally:
        conn.close()

def update_user_access_by_id(user_access_id, updated_data):
    conn = connect_to_database()
    try:
        cursor = conn.cursor()

        # Check if the user access record exists
        check_query = 'SELECT * FROM UserAccess WHERE ID = %s'
        cursor.execute(check_query, (user_access_id,))
        existing_row = cursor.fetchone()

        if not existing_row:
            return jsonify({"message": f"No row found with ID {user_access_id}"}), 404

        # Construct the UPDATE query
        update_query = """
            UPDATE UserAccess
            SET UserID = %s,
                AccessID = %s,
                CreatedDate = %s,
                CreatedBy = %s,
                UpdatedDate = %s,
                UpdatedBy = %s,
                IsDeleted = %s,
                DeletedBy = %s,
                DeletedDate = %s
            WHERE ID = %s
        """

        # Update the row with the provided data
        cursor.execute(update_query, (
            updated_data.get('UserID', existing_row[1]),
            updated_data.get('AccessID', existing_row[2]),
            updated_data.get('CreatedDate', existing_row[3]),
            updated_data.get('CreatedBy', existing_row[4]),
            updated_data.get('UpdatedDate', existing_row[5]),
            updated_data.get('UpdatedBy', existing_row[6]),
            updated_data.get('IsDeleted', existing_row[7]),
            updated_data.get('DeletedBy', existing_row[8]),
            updated_data.get('DeletedDate', existing_row[9]),
            user_access_id,
        ))

        conn.commit()

        if cursor.rowcount > 0:
            return jsonify({"message": f"Row with ID {user_access_id} updated successfully"}), 200
        else:
            return jsonify({"message": f"No rows updated with ID {user_access_id}"}), 404
    except Exception as error:
        conn.rollback()
        return jsonify({"error": str(error)}), 500
    finally:
        conn.close()