import ephem

def get_magnitude(conjunction):
    # Calculate the magnitude of the conjunction
    obj1, obj2 = conjunction
    mag1 = obj1.mag
    mag2 = obj2.mag
    return max(mag1, mag2)

def throw_party(conjunction_time, celestial_objects, rank):
    # Logic to throw a party
    print(f"Party time! The astronomical conjunction of {celestial_objects[0]} and {celestial_objects[1]} occurred at {conjunction_time}! This conjunction is ranked #{rank} in magnitude. Let's celebrate!")

def check_conjunctions(observer, celestial_objects, threshold=1):
    previous_conjunctions = {}
    rank = 1
    while True:
        next_conjunction = None
        next_conjunction_magnitude = float('-inf')
        
        for obj1, obj2 in celestial_objects:
            conjunction = ephem.localtime(observer.next_conjunction(obj1, obj2))
            if conjunction not in previous_conjunctions or \
               previous_conjunctions[conjunction] > threshold:
                previous_conjunctions[conjunction] = 0
                
                magnitude = get_magnitude((obj1, obj2))
                if magnitude > next_conjunction_magnitude:
                    next_conjunction = conjunction
                    next_conjunction_magnitude = magnitude
        
        if next_conjunction is not None:
            subject = f"Astronomical Conjunction Alert: {celestial_objects[0]} and {celestial_objects[1]}"
            body = f"{celestial_objects[0]} and {celestial_objects[1]} are in conjunction on {next_conjunction}. This conjunction is ranked #{rank} in magnitude."
            to_email = 'recipient@example.com'  # Update with recipient's email
            send_email(subject, body, to_email)
            throw_party(next_conjunction, celestial_objects, rank)
            rank += 1
        else:
            # If no next conjunction found, wait for next loop iteration
            pass

if __name__ == "__main__":
    # Set up observer location and celestial objects
    observer = ephem.Observer()
    observer.lat = '51.5074'  # Latitude of observer (e.g., London)
    observer.lon = '0.1278'   # Longitude of observer (e.g., London)
    observer.elevation = 0     # Elevation of observer (in meters)

    sun = ephem.Sun()
    moon = ephem.Moon()
    planets = [
        ephem.Mercury(),
        ephem.Venus(),
        ephem.Mars(),
        ephem.Jupiter(),
        ephem.Saturn(),
        ephem.Uranus(),
        ephem.Neptune()
    ]

    celestial_objects = [(sun, moon)]
    for planet in planets:
        celestial_objects.append((sun, planet))
        celestial_objects.append((moon, planet))

    # Check for conjunctions and throw parties
    check_conjunctions(observer, celestial_objects)
