def add_songs(*args):
    result = []
    songs = {}
    for title, lyrics in args:
        if title not in songs:
            songs[title] = []
        songs[title].extend(lyrics)
    for k, v in songs.items():
        result.append(f"- {k}")
        if v:
            result.append("\n".join(v))
    return "\n".join(result)


print(add_songs(
    ("Love of my life",
     ["Love of my life, you've hurt me",
      "You've broken my heart, and now you leave me",
      "Love of my life, can't you see?",
      "Bring it back, bring it back"]),
    ("Beat It", []),
    ("Love of my life",
     ["Don't take it away from me",
      "Because you don't know",
      "What it means to me"]),
    ("Dream On",
     ["Every time that I look in the mirror"]),
))
