# Train Model
# Represents a train entity with all relevant information

from datetime import datetime

class Train:
    """Train model class"""
    
    def __init__(self, train_number, train_name, from_station, to_station):
        self.train_number = train_number
        self.train_name = train_name
        self.from_station = from_station
        self.to_station = to_station
        self.status = 'Scheduled'
        self.delay_minutes = 0
        self.distance_covered = 0
        self.total_distance = 0
        self.current_speed = 0
        self.next_station = None
        self.last_updated = datetime.now()
    
    def to_dict(self):
        return {
            'train_number': self.train_number,
            'train_name': self.train_name,
            'from_station': self.from_station,
            'to_station': self.to_station,
            'status': self.status,
            'delay_minutes': self.delay_minutes,
            'distance_covered': self.distance_covered,
            'total_distance': self.total_distance,
            'current_speed': self.current_speed,
            'next_station': self.next_station,
            'last_updated': self.last_updated.isoformat()
        }
    
    def get_delay_status(self):
        """Get delay status as string"""
        if self.delay_minutes == 0:
            return 'On Time'
        elif self.delay_minutes > 0:
            return f'Delayed by {self.delay_minutes} mins'
        else:
            return f'Running {abs(self.delay_minutes)} mins early'
    
    def get_progress_percentage(self):
        """Get journey progress percentage"""
        if self.total_distance == 0:
            return 0
        return (self.distance_covered / self.total_distance) * 100
