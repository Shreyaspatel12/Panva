# tables/security_access.py

from flask import jsonify
from app.database import connect_to_database

def get_security_access_data():
    conn = connect_to_database()
    try:
        cursor = conn.cursor()
        query = 'SELECT * FROM SecurityAccess'
        cursor.execute(query)
        rows = cursor.fetchall()

        data = []
        for row in rows:
            id = row[0]
            access_id = row[1]
            product = row[2]
            description = row[3]
            module = row[4]
            sub_module = row[5]
            is_active = row[6]
            created_date = row[7]
            created_by = row[8]
            updated_date = row[9]
            updated_by = row[10]

            row_data = {
                'ID': id,
                'AccessID': access_id,
                'Product': product,
                'Description': description,
                'Module': module,
                'SubModule': sub_module,
                'IsActive': is_active,
                'CreatedDate': created_date,
                'CreatedBy': created_by,
                'UpdatedDate': updated_date,
                'UpdatedBy': updated_by,
            }

            data.append(row_data)

        return jsonify(data), 200
    except Exception as error:
        return jsonify({"error": str(error)}), 500
    finally:
        conn.close()

def delete_security_access_by_id(security_access_id):
    conn = connect_to_database()
    try:
        cursor = conn.cursor()
        query = 'DELETE FROM SecurityAccess WHERE ID = %s'
        cursor.execute(query, (security_access_id,))
        conn.commit()

        if cursor.rowcount > 0:
            return jsonify({"message": f"Row with ID {security_access_id} deleted successfully"}), 200
        else:
            return jsonify({"message": f"No rows found with ID {security_access_id}"}), 404
    except Exception as error:
        conn.rollback()  # Roll back changes if an error occurs
        return jsonify({"error": str(error)}), 500
    finally:
        conn.close()

def update_security_access_by_id(security_access_id, updated_data):
    conn = connect_to_database()
    try:
        cursor = conn.cursor()

        # Check if the security access record exists
        check_query = 'SELECT * FROM SecurityAccess WHERE ID = %s'
        cursor.execute(check_query, (security_access_id,))
        existing_row = cursor.fetchone()

        if not existing_row:
            return jsonify({"message": f"No row found with ID {security_access_id}"}), 404

        # Construct the UPDATE query
        update_query = """
            UPDATE SecurityAccess
            SET
                AccessID = %s,
                Product = %s,
                Description = %s,
                Module = %s,
                SubModule = %s,
                IsActive = %s,
                CreatedDate = %s,
                CreatedBy = %s,
                UpdatedDate = %s,
                UpdatedBy = %s
            WHERE ID = %s
        """

        # Extract values from the updated_data dictionary or use existing values
        values = (
            updated_data.get('AccessID', existing_row[1]),
            updated_data.get('Product', existing_row[2]),
            updated_data.get('Description', existing_row[3]),
            updated_data.get('Module', existing_row[4]),
            updated_data.get('SubModule', existing_row[5]),
            updated_data.get('IsActive', existing_row[6]),
            updated_data.get('CreatedDate', existing_row[7]),
            updated_data.get('CreatedBy', existing_row[8]),
            updated_data.get('UpdatedDate', existing_row[9]),
            updated_data.get('UpdatedBy', existing_row[10]),
            security_access_id,
        )

        # Update the row with the provided data
        cursor.execute(update_query, values)
        conn.commit()

        if cursor.rowcount > 0:
            return jsonify({"message": f"Row with ID {security_access_id} updated successfully"}), 200
        else:
            return jsonify({"message": f"No rows updated with ID {security_access_id}"}), 404
    except Exception as error:
        conn.rollback()
        return jsonify({"error": str(error)}), 500
    finally:
        conn.close()