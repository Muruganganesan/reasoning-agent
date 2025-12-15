from agent import solve

questions = [
    "Alice has 3 red apples and twice as many green apples. How many apples total?",
    "A meeting needs 60 minutes. Slots: 09:00–09:30, 09:45–10:30, 11:00–12:00. Which fit?"
]

for q in questions:
    print("\nQuestion:", q)
    print(solve(q))
