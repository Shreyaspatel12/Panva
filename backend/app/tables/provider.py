# tables/provider.py

from flask import jsonify
from app.database import connect_to_database

def get_provider_data():
    conn = connect_to_database()
    try:
        cursor = conn.cursor()
        query = 'SELECT * FROM Provider'
        cursor.execute(query)
        rows = cursor.fetchall()

        data = []
        for row in rows:
            provider_id = row[0]
            tenant_id = row[1]
            provider_type = row[2]
            unqint_id = row[3]
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
            country = row[15]
            zipcode = row[16]
            provider_latitude = row[17]
            provider_longitude = row[18]
            preftimezone_id = row[19]
            provider_image_url= row[20]
            provider_sign_url = row[21]
            is_emailverified = row[22]
            is_phoneverified = row[23]
            is_licenseverified = row[24]
            is_active = row[25]
            created_on = row[26]
            created_by = row[27]
            update_on = row[28]
            update_by = row[29]
            is_deleted = row[30]
            extemployee_id = row[31]


            row_data = {
                'ProviderID': provider_id,
                'TenantID': tenant_id,
                'ProviderType': provider_type,
                'UnqIntID': unqint_id,
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
                'Country': country,
                'ZipCode': zipcode,
                'ProviderLatitude': provider_latitude,
                'ProviderLongitude': provider_longitude,
                'PrefTimeZoneID': preftimezone_id,
                'ProviderImageURL': provider_image_url,
                'ProviderSignURL': provider_sign_url,
                'IsEmailVerified': is_emailverified,
                'IsPhoneVerified': is_phoneverified,
                'IsLicenseVerified': is_licenseverified,
                'IsActive': is_active,
                'CreatedOn': created_on,
                'CreatedBy': created_by,
                'UpdateOn': update_on,
                'UpdateBy': update_by,
                'IsDeleted': is_deleted,
                'ExtEmployeeId': extemployee_id,
            }

            data.append(row_data)

        return jsonify(data), 200
    except Exception as error:
        return jsonify({"error": str(error)}), 500
    finally:
        conn.close()

def delete_provider_by_id(provider_id):
    conn = connect_to_database()
    try:
        cursor = conn.cursor()
        query = 'DELETE FROM Provider WHERE ProviderID = %s'
        cursor.execute(query, (provider_id,))
        conn.commit()

        if cursor.rowcount > 0:
            return jsonify({"message": f"Row with ID {provider_id} deleted successfully"}), 200
        else:
            return jsonify({"message": f"No rows found with ID {provider_id}"}), 404

    except Exception as error:
        conn.rollback()  # Roll back changes if an error occurs
        return jsonify({"error": str(error)}), 500
    finally:
        conn.close()

def update_provider_by_id(provider_id, updated_data):
    conn = connect_to_database()
    try:
        cursor = conn.cursor()

        # Check if the provider record exists
        check_query = 'SELECT * FROM Provider WHERE ProviderID = %s'
        cursor.execute(check_query, (provider_id,))
        existing_row = cursor.fetchone()

        if not existing_row:
            return jsonify({"message": f"No row found with ProviderID {provider_id}"}), 404

        # Construct the UPDATE query
        update_query = """
            UPDATE Provider
            SET
                TenantID = %s,
                ProviderType = %s,
                UnqIntID = %s,
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
                Country = %s,
                ZipCode = %s,
                ProviderLatitude = %s,
                ProviderLongitude = %s,
                PrefTimeZoneID = %s,
                ProviderImageURL = %s,
                ProviderSignURL = %s,
                IsEmailVerified = %s,
                IsPhoneVerified = %s,
                IsLicenseVerified = %s,
                IsActive = %s,
                CreatedOn = %s,
                CreatedBy = %s,
                UpdateOn = %s,
                UpdateBy = %s,
                IsDeleted = %s,
                ExtEmployeeId = %s
            WHERE ProviderID = %s
        """

        # Extract values from the updated_data dictionary or use existing values
        values = (
            updated_data.get('TenantID', existing_row[1]),
            updated_data.get('ProviderType', existing_row[2]),
            updated_data.get('UnqIntID', existing_row[3]),
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
            updated_data.get('Country', existing_row[15]),
            updated_data.get('ZipCode', existing_row[16]),
            updated_data.get('ProviderLatitude', existing_row[17]),
            updated_data.get('ProviderLongitude', existing_row[18]),
            updated_data.get('PrefTimeZoneID', existing_row[19]),
            updated_data.get('ProviderImageURL', existing_row[20]),
            updated_data.get('ProviderSignURL', existing_row[21]),
            updated_data.get('IsEmailVerified', existing_row[22]),
            updated_data.get('IsPhoneVerified', existing_row[23]),
            updated_data.get('IsLicenseVerified', existing_row[24]),
            updated_data.get('IsActive', existing_row[25]),
            updated_data.get('CreatedOn', existing_row[26]),
            updated_data.get('CreatedBy', existing_row[27]),
            updated_data.get('UpdateOn', existing_row[28]),
            updated_data.get('UpdateBy', existing_row[29]),
            updated_data.get('IsDeleted', existing_row[30]),
            updated_data.get('ExtEmployeeId', existing_row[31]),
            provider_id,
        )

        # Update the row with the provided data
        cursor.execute(update_query, values)
        conn.commit()

        if cursor.rowcount > 0:
            return jsonify({"message": f"Row with ProviderID {provider_id} updated successfully"}), 200
        else:
            return jsonify({"message": f"No rows updated with ProviderID {provider_id}"}), 404
    except Exception as error:
        conn.rollback()
        return jsonify({"error": str(error)}), 500
    finally:
        conn.close()
