# python-task
## running the application
run the following command to run the pub/sub service, and the django server:
- run the command docker-compose up --build -d 

run the following commands to run the iot simulator:
- cd iot_simulator
- pip install -r requirements.txt 
- python iot_simulator.py

the `iot_simulator.py` script will send a data entry for 3 simulated iot devices every second to the django server, which will store the data in a mysql database,
the following endpoints are available to query the database:
- /data-point/max-temperature: 
takes device_id as a query parameters, returns the max temperature for a given device id .
mysql query:
`SELECT *, MAX(temperature) as max_temperature FROM device_entry GROUP BY `device_id`;`

- /data-point/count
takes device_id as a query parameters, returns the number of data points for a given device id.
mysql query:
`SELECT id, device_id, COUNT(*) FROM device_entry GROUP BY device_id;`

- data-point/max-temperature-per-day:
takes device_id and date as query parameters, returns the max temperature for a given device, on a given day.
mysql query:
`SELECT *, MAX(temperature) as max_temperature FROM device_entry WHERE time BETWEEN 
        '{} 00:00:00' AND '{} 23:59:59'  GROUP BY device_id;`
