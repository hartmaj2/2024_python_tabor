# Co je v nasledujicim kodu za chybu?

character = "Kirby"
health = 100
print(f"Character: {character}")
print(f"Starting Health: {health}")

# Check if the character has enough health
if health > 50:
    print("You are in great shape!")
print("With this much HP you can go fight a dragon!")
if health <= 50:
    print("You need to find a health pack!")  # This line is not indented correctly

print("Let's start the adventure!")