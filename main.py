import redis
r = redis.Redis(host="localhost", port=6379, db=0)

class Player:
  """A person playing the game"""

  def __init__(self, name):
    self.name = name
    self.experience = []
    self.inventory = []

class Action:
  """An action a player can take"""

  def __init__(self, name):
    self.name = name

class Location:
  """Where a thing is"""

  def __init__(self, name, x, y):
    self.name = name
    self.x = x
    self.y = y


# All known actions
#actions = []

# All known locations
#locations = []

# init the player
player = Player(input("What shall we call you?\n"))

player_action = ""
while player_action != "quit":
  # As the player what they want to do
  player_action = input(f"""What do you want to do {player.name}?\n""")

  # Lookup if we know how to do that
  #existing_actions = [x for x in actions if x.name == player_action]
  existing_action = r.get(player_action)
  if existing_action:
    print("Oh I know that one!")
    print(existing_action.instructions)
  else:
    new_action = Action(player_action)
    # If not, ask them how to do it
    new_action.instructions = input("OK, how do you do that?\n")
    new_action.duration = int(input("How long does it take (minutes)?\n"))
    r.set(new_action.name, new_action)
    #actions.append(new_action)
