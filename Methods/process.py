import json, datetime

def validate_record(record):
    timestamp = record.get("timestamp")
    
    truck_id = record.get("truck_id")
    if not truck_id or not isinstance(truck_id, str):
        return False, "Invalid or missing truck_id", timestamp
    
    latitude = record.get("latitude")
    if not latitude or not isinstance(latitude, float):
        return False, "Invalid or missing latitude", timestamp
    
    longitude = record.get("longitude")
    if not longitude or not isinstance(longitude, float):
        return False, "Invalid or missing longitude", timestamp
    
    timestamp = record.get("timestamp")
    if not timestamp:
        return False, "missing timestamp", timestamp
         
    return True, "Valid"

def process_log_file(filepath):
    records = []
    
    with open(filepath, "r") as fail:
        records = json.load(fail)
        
    with open("sucess.log","w") as success_log, open("error.log", "w") as error_log:
        for record in records:
            valid, message, timestamp