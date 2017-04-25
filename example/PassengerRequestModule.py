class Passenger_request:
	
	request_id;
	request_status;
	
    def create_request(start_lattitude, start_longitude, end_lattitude, end_longitude, timestamp, user_id):
			add request record in database;
			matching(start_lattitude, start_longitude, end_lattitude, end_longitude, timestamp, user_id)

    
    def get_status(user_id):
		pass status and driver details to app
			