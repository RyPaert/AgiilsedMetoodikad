import json, datetime

def validate_record(record):
    truck_id = record.get("truck_id")
    if not truck_id or not isinstance(truck_id, str):
        return False, "Invalid or missing truck_id"
    
    latitude = record.get("latitude")
    if not latitude or not isinstance(latitude, float):
        return False, "Invalid or missing latitude"
    
    longitude = record.get("longitude")
    if not longitude or not isinstance(longitude, float):
        return False, "Invalid or missing longitude"
    
    timestamp = record.get("timestamp")
    if not timestamp:
        return False, "missing timestamp"
         