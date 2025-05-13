allSongs = [
    {"title": "Shape of You", "artist": "Ed Sheeran"},
    {"title": "Blinding Lights", "artist": "The Weeknd"},
    {"title": "Bad Guy", "artist": "Billie Eilish"},
    {"title": "Believer", "artist": "Imagine Dragons"},
    {"title": "Thunder", "artist": "Imagine Dragons"},
    {"title": "Perfect", "artist": "Ed Sheeran"},
]
def otsi_muusikat(query):
    if not query:
        return "Palun sisesta otsitav muusika."

    tulemused = []
    for song in allSongs:
        if query in song["title"] or query in song["artist"]:
            tulemused.append(song)

    if tulemused:
        print("Leitud laulud")
        for i in tulemused:
            print(i['artist'], ' - ', i['title'])
        else:
            print("Laulu ei leitud")

otsi_muusikat("Ed Sheeran")