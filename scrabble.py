destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "Sao Paulo, Brazil", "Cairo, Egypt"]

test_traveler = ["Erin Wilkes", "Shanghai, China", ["historical site", "art"]]

def get_destination_index(destination):
  destination_index = destinations.index(destination)
  return destination_index

def get_traveler_location(traveler):
  traveler_destination = test_traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index


test_destination_index = get_traveler_location(test_traveler)

attractions = [[] for i in destinations]
def add_attraction(destination, attraction):
  try:
    destination_index = get_destination_index(destination)
    attractions_for_destination = attractions[destination_index].append(attraction)
  except ValueError:
    return

add_attraction("Los Angeles, USA", ["Venice Beach", ["beach"]])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])


def find_attractions(destination, interests):
  destination_index = get_destination_index(destination)
  attractions_in_city = attractions[destination_index]
  attractions_with_interest = []

  for attraction in attractions_in_city:
    possible_attraction = attraction
    attraction_tags = attraction[1]

    for interest in interests:
      if interest in attraction_tags:
        attractions_with_interest.append(possible_attraction[0])
  return attractions_with_interest


la_arts = find_attractions("Los Angeles, USA", ["art"])

def get_attractions_for_traveler(traveler):
  traveler_destination = traveler[1]
  traveler_interests = traveler[2]
  traveler_attractions = find_attractions(traveler_destination, traveler_interests)
  interests_string = ("Hi ")
  interests_string = interests_string + traveler[0]
  interests_string = interests_string + (", we think you'll like these places around ") + traveler_destination + (": ")
  for attraction in traveler_attractions:
    if len(traveler_attractions) > 1:
      interests_string = interests_string + ("the ") + attraction + (", ")
    else:
      interests_string = interests_string + ("the ") + attraction + (".")
    return interests_string

smills_france = get_attractions_for_traveler(["Dereck Smill", "Paris, France", ["monument"]])
print(smills_france)
  
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
letter_to_points = {key:value for key, value in zip(letters, points)}
letter_to_points[" "] = 0
#print(letter_to_points)
#Returns total value of word entered
def score_words(word):
  point_total = 0
  for letters in word:
    point_total += letter_to_points.get(letters, 0)
  return point_total
#Test score_words function
brownie_points = score_words("MONKEY")
#print(brownie_points)
player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}
print(player_to_words)
player_to_points = {}
for player, words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points += score_words(word)
  player_to_points[player] = player_points
print("\n")
print(player_to_points)
print("\n")

def play_word(player, word):
  player_to_words[player].append(word)
play_word("player1", "BLOCKMAN")
print(player_to_words)
def update_point_totals(word, player):
  player_points = 0
  play_word(player, word)
  player_points += score_words(word)
  player_to_points[player] += player_points
  return print("\nPlayer {} played the word \"{}\" which is worth {} points. \n\nTheir total is now {}.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n".format(player, word, player_points, player_to_points[player]))

pr  int(update_point_totals("MONKEY", "Lexi Con"))
