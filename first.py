from flask import Flask, request, jsonify
from datetime import datetime
import pytz #For working with time zones

app = Flask(__name__)
def get_current_time():
    utc_time = datetime.now(pytz.UTC)
    current_time = datetime.now()
    #calculating the time diffrence in hours
    time_difference_hours = (current_time - utc_time).total_seconds()/3600
    if abs(time_difference_hours) <= 2:
        return utc_time.strftime("%Y-%m-%dT%H:%M:%SZ")
    else:
        return None
    
@app.route("/my_endpoint", methods=["GET"])
def my_endpoint():
    #Getting parameters
    slack_name = request.args.get("slack_name")
    track = request.args.get("track")
    file_url = request.args.get("file_url")
    source_code_url = request.args.get("source_code_url")

    #Get current day of the week
    current_day_of_week = datetime.now().strftime("%A")
    #Get current UTC time with validation 
    current_utc_time = get_current_utc_time()

    if current_utc_time:
        result = {
            "slack_name": slack_name,
            "day_of_the_week": current_day_of_week,
            "current_utc_time": current_utc_time,
            "track": track,
            "file_url": file_url,
            "source_code_url": source_code_url
        
        }
        return jsonify(result)
    else:
        return jsonify({"error": "Invalid UTC time"}), 400
if __name__ == "__main__":
    app.run (host ="0.0.0.0", port=5000,  debug=True)

