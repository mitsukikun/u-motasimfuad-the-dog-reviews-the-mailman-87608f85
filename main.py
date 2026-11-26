import os

line = ("One star. Same man, same bag, "
        "same suspicious rustle every morning — "
        "drops paper through my slot, sprints off "
        "before my review, and still expects a tail wag.")

# Entry limit: 200 characters max.
assert len(line) <= 200

os.makedirs("/output", exist_ok=True)

with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(line)
