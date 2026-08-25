import sys
import time

# List of Tuples: ("Teks Lirik", Jeda Setelah Teks)
lyrics = [
    ("I think that you are the one for me", 1.2),
    ("'Cause it gets so hard ", 0.5),
    ("to breathe", 0.9),
    ("When you're looking at me", 0.7),
    ("I've never felt so alive and free", 0.9),
    ("When you're looking at me", 0.7),
    ("I've never felt so happy", 1.6),
    # PRE-CHORUS
    ("And I've heard of a love that comes ", 0.5),
    ("once in a lifetime", 1.1),
    ("And I'm pretty sure that you are that ", 0.5),
    ("love of mine", 1.8),
    # CHORUS
    ("'Cause I'm in a field of dandelions", 0.8),
    ("Wishing on every one that you'd be mine, ", 0.5),
    ("mine", 1.2),
    ("And I see forever in your eyes", 1.0),
    ("I feel okay when I see you smile, ", 0.5),
    ("smile", 1.4),
    ("Wishing on dandelions all of the time", 0.7),
    ("Praying to God that one day you'll be mine", 0.7),
    ("Wishing on dandelions all of the time, ", 0.5),
    ("all of the time", 3.0),
]


def play_lyrics():
    for line, delay in lyrics:
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(
                0.09
            )  
        time.sleep(delay)  
        print()


if __name__ == "__main__":
    play_lyrics()