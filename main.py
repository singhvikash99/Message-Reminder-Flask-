from flask import Flask, request, jsonify
from datetime import datetime
import models, db

app = Flask(__name__)

# API endpoint to accept reminder data
@app.route('/api/reminders', methods=["POST"])
def create_reminder(db = db.db_session()):
    try:
        # Parse request JSON data
        data = request.get_json()
        
        # Extract date, time, and message from request data
        date_str = data.get('data')
        time_str = data.get('time')
        message_txt = data.get('message')
        
        # Concatenate date and time strings to form datetime object
        datetime_str = f"{date_str} {time_str}"

        # Convert datetime string to datetime object
        datetime_obj = datetime.strptime(datetime_str, '%d-%m-%Y %H:%M')
        
        # Create new Reminder object with parsed data
        new_reminder = models.Reminders()
        new_reminder.date = datetime_obj
        new_reminder.message = message_txt

        # Add new reminder to database session
        db.add(new_reminder)

        # Commit changes to database
        db.commit()

       

        # Return success message
        return jsonify({'message': 'Reminder saved successfully!'}), 201
    
    except Exception as err:
        # Rollback changes if an error occurs
        db.rollback()
        return jsonify({'error': str(err)}), 500
    
    finally:
        # close database connection
        db.close()


if __name__ == '__main__':
    app.run(debug=True)

    