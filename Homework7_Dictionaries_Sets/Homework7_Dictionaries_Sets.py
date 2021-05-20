
music = {
    "Title": "Show Me The Meaning",
    "Album": "Millennium",
    "Artist": "Backstreet Boys",
    "Publisher": "Jeff Recordings",
    "YearReleased": "1999",
    "Language": "English",
    "Writer": "Max Martin",
    "Genre": "Pope",
    "Duration": "3.54",
    "Nominations": "Grammy Award for Best Vocal Performance by a Double or Multiple Pop Band"
}

for key in music:
    print("\n{0:s}: \"{1:s}\"".format(key, music[key]))


def guess(key, value):
    return key in music and music[key] == value

print("\n\n\nIs the Name of music \"Show Me The Meaning\"?: {}".format(guess("Title", "Show Me The Meaning")))
print("\nIs the name of Album \"Millennium\"?: {}".format(guess("Album", "Millennium")))