# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
  def __init__(self, name, room_location, inventory):
    self.name = name
    self.room_location = room_location
    self.inventory = []

  def __str__(self):
    return f"Player {self.name}, is currently located (in the /at the) {self.room_location}"

