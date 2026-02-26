# ABOUT: class

# A class in Python does not have private fields that are enforced.

#______________________________________________________________________________

class PlayerCharacter:
    # Class object attribute. 
    # Every instance created from a class will have this value preset
    max_heath: int = 100

    # Constructor
    def __init__(self, name: str, age: int) -> None:
        # Instance specific attributes
        # These are dynamically set
        self.name = name
        self.age = age

    # Methods
    # Having `self` as parameter tells Python that this is a method
    def ninja_run(self):
        print(f"{self.name} is running")

#______________________________________________________________________________

def main() -> None:
    player_one: PlayerCharacter = PlayerCharacter("Kakashi", 30)
    print(f"player_one's name is {player_one.name}")
    print(f"player_one's age is {player_one.age}")
   
    # You can also have named fields
    player_two: PlayerCharacter = PlayerCharacter(name="Tsunade", age=70)
    print(f"player_two's name is {player_two.name}")
    print(f"player_two's age is {player_two.age}")

    player_one.ninja_run()
    print(player_one.max_heath)

if __name__ == "__main__":
    main()
