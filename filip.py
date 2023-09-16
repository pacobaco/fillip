import ephem
from timezonefinder import TimezoneFinder
import pytz
import geopy
import datetime
from geopy.geocoders import Nominatim

def whatcanisee(time, zipcode):
	gps = zipcodegps(zipcode)
	print(gps)
	timez = get_timezone_from_gps(gps[0],gps[1])
	a = localize(timez, time)
	planets = ['Mercury', 'Venus', 'Sun', 'Moon', 'Mars', 'Jupiter', 'Saturn', 'Neptune', 'Uranus', 'Pluto']
	for x in planets: loopatzimuthaltx,(gps[0],gps[1],0,a)

def get_timezone_from_gps(latitude, longitude):
    tz_finder = TimezoneFinder()
    timezone_str = tz_finder.timezone_at(lng=longitude, lat=latitude)
    
    if timezone_str:
        timezone = pytz.timezone(timezone_str)
        return timezone
    else:
        return None

def sky_orientation(azimuth, altitude):
	orient = 'n'
	orient2 = 'half'
	if azimuth<45:
		orient='north to north east'
	if azimuth>=45 and azimuth <90:
		orient = 'east to northeast'
	if azimuth>=90 and azimuth<135:
		orient = 'east to southeast'
	if azimuth>=135 and azimuth<180:
		orient ='south to southeast'
	if azimuth>=180 and azimuth<225:
		orient = 'south to southwest'
	if azimuth>=225 and azimuth<270:
		orient = 'west to southwest'
	if azimuth>=270 and azimuth<315:
		orient = 'west to northwest'
	if azimuth>=315 and azimuth<360:
		orient = 'north to northwest'

	if altitude<30: orient2 = 'above the horizon'
	if altitude>=30 and altitude<60: orient2 = 'halfway up the sky'
	if altitude>=60 and altitude<90: orient2 = 'almost overhead'
	if altitude<0: orient2 = 'under the horizon'

	return(orient,orient2)

def find_planet_rising_time(body_name, observer_lat, observer_lon, observer_elev, date):
    # Create an observer at the specified location
    observer = ephem.Observer()
    observer.lat = str(observer_lat)
    observer.lon = str(observer_lon)
    observer.elev = observer_elev

    # Set the date for the calculation
    observer.date = date

    # Load the planetary body using its name
    body = getattr(ephem, body_name)(observer)

    # Calculate the next rising time for the planet
    next_rising = observer.next_rising(body)

    return next_rising

def calculate_azimuth_altitude(body_name, observer_lat, observer_lon, observer_elev, date):
    # Create an observer at the specified location
    observer = ephem.Observer()
    observer.lat = str(observer_lat)
    observer.lon = str(observer_lon)
    observer.elev = observer_elev

    # Set the date for the calculation
    observer.date = date

    # Load the planetary body using its name
    body = getattr(ephem, body_name)(observer)

    # Compute the position of the body
    body.compute(observer)

    # Calculate azimuth and altitude in degrees
    azimuth = body.az * 180.0 / ephem.pi
    altitude = body.alt * 180.0 / ephem.pi

    return azimuth, altitude


def zipcodegps(zip):
	geolocator = Nominatim(user_agent="filip")

	location = geolocator.geocode(zip)

	if location:
	    latitude = location.latitude
	    longitude = location.longitude
	    print(f"Latitude: {latitude}, Longitude: {longitude}")
	else:
	    print("Location not found for the given zip code.")
	return latitude, longitude

def localize(timezone, dt):
	if timezone:
	    print(f"Timezone: {timezone}")
	    current_time = pytz.utc.localize(dt)
	    local_time = current_time.astimezone(timezone)
	    print(f"Current local time: {local_time}")
	else:
	    print("Could not determine timezone.")

def loopatzimuthalt(planet, lat, long, elev, dat):
    azimuth, altitude = calculate_azimuth_altitude(planet, lat, long, elev, dat)
    print(sky_orientation(azimuth, altitude))
    print(f"Azimuth: {azimuth:.2f} degrees")
    print(f"Altitude: {altitude:.2f} degrees")
    rising_time = find_planet_rising_time(planetary_object, latitude, longitude, elevation, observation_date)


if __name__ == "__main__":
    planetary_object = "Mars"  # Replace with the desired planetary object
    latitude = "25.7617"  # Replace with observer's latitude
    longitude = "80.1918"  # Replace with observer's longitude
    elevation = 6  # Replace with observer's elevation in meters
    observation_date = "2023/08/16 1:34:00"  # Replace with the desired observation date
    whatcanisee(datetime.datetime.utcnow(),'33165')
