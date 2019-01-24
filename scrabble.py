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

print(update_point_totals("MONKEY", "Lexi Con"))
