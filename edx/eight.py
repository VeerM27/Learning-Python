def main():
    difficulty = input("Level: Difficult or Casual? ").lower()
    if not (difficulty == "difficult" or difficulty == "casual"):
        print("Invalid difficulty level.")
        return
    
    players = input("Type: Multiplayer or Singleplayer? ").lower()
    if not (players == "multiplayer" or players == "singleplayer"):
        print("Invalid player type.")
        return
    
    if difficulty == "difficult" and players == "multiplayer":
        recommend("Counter Strike 2")
    elif difficulty == "difficult" and players == "singleplayer":
        recommend("Black Myth Wukong")
    elif difficulty == "casual" and players == "multiplayer":
        recommend("Valorant")
    else:
        recommend("GTA V")



def recommend(game):
    print("You might like " + game + ".")

main()