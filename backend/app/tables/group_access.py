# tables/group_access.py

from flask import jsonify
from app.database import connect_to_database

def get_group_access_data():
    conn = connect_to_database()
    try:
        cursor = conn.cursor()
        query = 'SELECT * FROM GroupAccess'
        cursor.execute(query)
        rows = cursor.fetchall()

        data = []
        for row in rows:
            id = row[0]
            group_id = row[1]
            access_id = row[2]
            created_date = row[3]
            created_by = row[4]
            updated_date = row[5]
            updated_by = row[6]

            row_data = {
                'ID': id,
                'GroupID': group_id,
                'AccessID': access_id,
                'CreatedDate': created_date,
                'CreatedBy': created_by,
                'UpdatedDate': updated_date,
                'UpdatedBy': updated_by
            }

            data.append(row_data)

        return jsonify(data), 200
    except Exception as error:
        return jsonify({"error": str(error)}), 500
    finally:
        conn.close()

def delete_group_access_by_id(group_access_id):
    conn = connect_to_database()
    try:
        cursor = conn.cursor()
        query = 'DELETE FROM GroupAccess WHERE ID = %s'
        cursor.execute(query, (group_access_id,))
        conn.commit()

        if cursor.rowcount > 0:
            return jsonify({"message": f"Row with ID {group_access_id} deleted successfully"}), 200
        else:
            return jsonify({"message": f"No rows found with ID {group_access_id}"}), 404
    except Exception as error:
        conn.rollback()  # Roll back changes if an error occurs
        return jsonify({"error": str(error)}), 500
    finally:
        conn.close()

def update_group_access_by_id(group_access_id, updated_data):
    conn = connect_to_database()
    try:
        cursor = conn.cursor()

        # Check if the group access record exists
        check_query = 'SELECT * FROM GroupAccess WHERE ID = %s'
        cursor.execute(check_query, (group_access_id,))
        existing_row = cursor.fetchone()

        if not existing_row:
            return jsonify({"message": f"No row found with ID {group_access_id}"}), 404

        # Construct the UPDATE query
        update_query = """
            UPDATE GroupAccess
            SET
                GroupID = %s,
                AccessID = %s,
                CreatedDate = %s,
                CreatedBy = %s,
                UpdatedDate = %s,
                UpdatedBy = %s
            WHERE ID = %s
        """

        # Extract values from the updated_data dictionary or use existing values
        values = (
            updated_data.get('GroupID', existing_row[1]),
            updated_data.get('AccessID', existing_row[2]),
            updated_data.get('CreatedDate', existing_row[3]),
            updated_data.get('CreatedBy', existing_row[4]),
            updated_data.get('UpdatedDate', existing_row[5]),
            updated_data.get('UpdatedBy', existing_row[6]),
            group_access_id,
        )

        # Update the row with the provided data
        cursor.execute(update_query, values)
        conn.commit()

        if cursor.rowcount > 0:
            return jsonify({"message": f"Row with ID {group_access_id} updated successfully"}), 200
        else:
            return jsonify({"message": f"No rows updated with ID {group_access_id}"}), 404
    except Exception as error:
        conn.rollback()
        return jsonify({"error": str(error)}), 500
    finally:
        conn.close()