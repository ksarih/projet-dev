from bike_data import get_bike_data, get_bike_routes
from simulation import simulation

date = '2024-09-30'
stations, trajets = get_bike_data(date)

bikes_routes = get_bike_routes(stations, trajets)

simulation(bikes_routes, date)