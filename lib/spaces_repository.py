from lib.space import Space


class SpaceRepository:
    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all spaces
    def all(self):
        rows = self._connection.execute('SELECT * from spaces')
        spaces = []
        for row in rows:
            item = Space(row["id"], row["name"], row["availability"])
            spaces.append(item)
        return spaces

    # Find a singlespace by its id
    def find(self, space_id):
        rows = self._connection.execute(
            'SELECT * from spaces WHERE id = %s', [space_id])
        row = rows[0]
        return Space(row["id"], row["name"], row["availability"])

    # Create a newspace
    def create(self, space):
        rows = self._connection.execute('INSERT INTO spaces (name, availability) VALUES (%s, %s) RETURNING id', [
            space.name, space.availability])
        row = rows[0]
        space.id = row["id"]
        return space

    # Delete aspace by its id
    def delete(self, space_id):
        self._connection.execute(
            'DELETE FROM spaces WHERE id = %s', [space_id])
        return None
