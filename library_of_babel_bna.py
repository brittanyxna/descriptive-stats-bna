import random
import string

characters = string.ascii_lowercase + ". "

room = []

for s in range(5):
    shelf = []
    for b in range(32):
        book = []
        for p in range(410):
            page = []
            for l in range(40):
                # This picks 80 random characters for each line
                line = "".join(random.choices(characters, k=80))
                page.append(line)
            book.append(page)
    shelf.append(book)
    room.append(shelf).

# This must be all the way to the left (no spaces)
print(room)
