class Item:
  def __init__(self, id, name, description):
    self.id = id
    self.name = name
    self.description = description

  def __str__(self):
    return f'{self.name}, '


  # Items                                               #Locations Options
    # An bag of old Halloween candy                         Outside
    # A tooth retainer                                      Foyer
    # A small statue of Elvis                               Overlook
    # A plactic glove filled with birdseed                  narrow
    # A glob of something creamy/gray, perhaps oatmeal.     treasure
    # Watermelon                                            player's inventory (satchel, backpack)
    # Ornate 7 tiered cake
    # Sequin cape
    # One yellow flip-flop
    # Box of Kraft Mac&Cheese
    # Walkman with Hall&Oats tape
    # Can of yams
    # Racoon wearing a fedora
    # Grand piano
    # Cactus wearing a bowtie
    # Box of 90s era cellphones
