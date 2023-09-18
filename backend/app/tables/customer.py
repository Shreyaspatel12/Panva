# tables/customer.py

from flask import jsonify
from app.database import connect_to_database

def get_customer_data():
    conn = connect_to_database()
    try:
        cursor = conn.cursor()
        query = 'SELECT * FROM Customer'
        cursor.execute(query)
        rows = cursor.fetchall()

        data = []
        for row in rows:
            customer_id = row[0]
            tenant_id = row[1]
            intent_id = row[2]
            ext_id = row[3]
            prefix = row[4]
            suffix = row[5]
            first_name = row[6]
            last_name = row[7]
            middle_name = row[8]
            dob = row[9]
            gender = row[10]
            emailid = row[11]
            street = row[12]
            city = row[13]
            state = row[14]
            zip = row[15]
            country = row[16]
            customer_latitude = row[17]
            customer_longitude = row[18]
            preftimezone_id = row[19]
            is_emailverified = row[20]
            is_phoneverified = row[21]
            is_active = row[22]
            created_on = row[23]
            created_by = row[24]
            update_on = row[25]
            update_by = row[26]
            is_deleted = row[27]
            agree_terms = row[28]


            row_data = {
                'CustomerID': customer_id,
                'TenantID': tenant_id,
                'InterID': intent_id,
                'ExtID': ext_id,
                'Prefix': prefix,
                'Suffix': suffix,
                'FirstName': first_name,
                'LastName': last_name,
                'MiddleName': middle_name,
                'DOB': dob,
                'Gender': gender,
                'EmailID': emailid,
                'Street': street,
                'City': city,
                'State': state,
                'Zip': zip,
                'Country': country,
                'CusLati': customer_latitude,
                'CusLon': customer_longitude,
                'PrefTimeZoneID': preftimezone_id,
                'IsEmailVerified': is_emailverified,
                'IsPhoneVerified': is_phoneverified,
                'IsActive': is_active,
                'CreatedOn': created_on,
                'CreatedBy': created_by,
                'UpdatedOn': update_on,
                'UpdateBy': update_by,
                'IsDeleted': is_deleted,
                'AgreeTerms': agree_terms,
            }

            data.append(row_data)

        return jsonify(data), 200
    except Exception as error:
        return jsonify({"error": str(error)}), 500
    finally:
        conn.close()

def delete_customer_by_id(customer_id):
    conn = connect_to_database()
    try:
        cursor = conn.cursor()
        query = 'DELETE FROM Customer WHERE CustomerID = %s'
        cursor.execute(query, (customer_id,))
        conn.commit()

        if cursor.rowcount > 0:
            return jsonify({"message": f"Row with ID {customer_id} deleted successfully"}), 200
        else:
            return jsonify({"message": f"No rows found with ID {customer_id}"}), 404
    except Exception as error:
        conn.rollback()  # Roll back changes if an error occurs
        return jsonify({"error": str(error)}), 500
    finally:
        conn.close()

def update_customer_by_id(customer_id, updated_data):
    conn = connect_to_database()
    try:
        cursor = conn.cursor()

        # Check if the customer record exists
        check_query = 'SELECT * FROM Customer WHERE CustomerID = %s'
        cursor.execute(check_query, (customer_id,))
        existing_row = cursor.fetchone()

        if not existing_row:
            return jsonify({"message": f"No row found with CustomerID {customer_id}"}), 404

        # Construct the UPDATE query
        update_query = """
            UPDATE Customer
            SET
                TenantID = %s,
                InterID = %s,
                ExtID = %s,
                Prefix = %s,
                Suffix = %s,
                FirstName = %s,
                LastName = %s,
                MiddleName = %s,
                DOB = %s,
                Gender = %s,
                EmailID = %s,
                Street = %s,
                City = %s,
                State = %s,
                Zip = %s,
                Country = %s,
                CusLati = %s,
                CusLon = %s,
                PrefTimeZoneID = %s,
                IsEmailVerified = %s,
                IsPhoneVerified = %s,
                IsActive = %s,
                CreatedOn = %s,
                CreatedBy = %s,
                UpdatedOn = %s,
                UpdateBy = %s,
                IsDeleted = %s,
                AgreeTerms = %s
            WHERE CustomerID = %s
        """

        # Extract values from the updated_data dictionary or use existing values
        values = (
            updated_data.get('TenantID', existing_row[1]),
            updated_data.get('InterID', existing_row[2]),
            updated_data.get('ExtID', existing_row[3]),
            updated_data.get('Prefix', existing_row[4]),
            updated_data.get('Suffix', existing_row[5]),
            updated_data.get('FirstName', existing_row[6]),
            updated_data.get('LastName', existing_row[7]),
            updated_data.get('MiddleName', existing_row[8]),
            updated_data.get('DOB', existing_row[9]),
            updated_data.get('Gender', existing_row[10]),
            updated_data.get('EmailID', existing_row[11]),
            updated_data.get('Street', existing_row[12]),
            updated_data.get('City', existing_row[13]),
            updated_data.get('State', existing_row[14]),
            updated_data.get('Zip', existing_row[15]),
            updated_data.get('Country', existing_row[16]),
            updated_data.get('CusLati', existing_row[17]),
            updated_data.get('CusLon', existing_row[18]),
            updated_data.get('PrefTimeZoneID', existing_row[19]),
            updated_data.get('IsEmailVerified', existing_row[20]),
            updated_data.get('IsPhoneVerified', existing_row[21]),
            updated_data.get('IsActive', existing_row[22]),
            updated_data.get('CreatedOn', existing_row[23]),
            updated_data.get('CreatedBy', existing_row[24]),
            updated_data.get('UpdatedOn', existing_row[25]),
            updated_data.get('UpdateBy', existing_row[26]),
            updated_data.get('IsDeleted', existing_row[27]),
            updated_data.get('AgreeTerms', existing_row[28]),
            customer_id,
        )

        # Update the row with the provided data
        cursor.execute(update_query, values)
        conn.commit()

        if cursor.rowcount > 0:
            return jsonify({"message": f"Row with CustomerID {customer_id} updated successfully"}), 200
        else:
            return jsonify({"message": f"No rows updated with CustomerID {customer_id}"}), 404
    except Exception as error:
        conn.rollback()
        return jsonify({"error": str(error)}), 500
    finally:
        conn.close()