"""
ISCG5421 Practice Test - Semester 2 2020

Kris Pritchard - @krp
"""
import datetime


class InvalidLocation(Exception):
    """InvalidLocation Exception class."""
    # 'pass' not necessary here if you have a docstring.


class Person:
    """Person class for contact tracer."""
    def __init__(self, email):
        self._email = email
        self.visited = set()
        self.last_visit_at = datetime.datetime.now()

    def visit(self, location_id):
        """Add location id to visited set."""
        if location_id < 0:
            raise InvalidLocation('Invalid location id')
        self.visited.add(location_id)
        print(f'visited location: {location_id}')
        self.last_visit_at = datetime.datetime.now()

    def num_locations_visited(self):
        """Return the number of locations visited."""
        return len(self.visited)

    def has_contact(self, other_person):
        """Return True if two people have had contact at the same location."""
        if self.visited.intersection(other_person.visited):
            return True
        return False

        # NOTE: This works too:
        #return bool(self.visited & other_person.visited)

    def _notify(self):
        return self._email.upper()
