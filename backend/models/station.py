# Station Model
# Represents a railway station

class Station:
    """Station model class"""
    
    def __init__(self, station_code, station_name, state, zone):
        self.station_code = station_code
        self.station_name = station_name
        self.state = state
        self.zone = zone
        self.platforms = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.facilities = []
    
    def to_dict(self):
        return {
            'code': self.station_code,
            'name': self.station_name,
            'state': self.state,
            'zone': self.zone,
            'platforms': self.platforms,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'facilities': self.facilities
        }
