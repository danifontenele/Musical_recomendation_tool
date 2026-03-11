import json


# function that read and load the json file to return it as a dictionary
def load_data() -> dict:
    with open("data_set.json", "r") as f:
        data = json.load(f)
    return data


# Get the first input, the genre
def get_genre() -> str:
    genres = ["pop", "rock", "hiphop", "brazilian"]
    print("Select a genre:")
    for i, genre in enumerate(genres, 1):
        print(f"{i}) {genre.title()}")
    while True:
        try:
            choice = int(input("Choice: "))
            if 1 <= choice and choice <= len(genres):
                return genres[choice - 1]
        except ValueError:
            pass
        print("invalid option, try again!")


# Select the songs with the same choosen genre among dataset dict options
def filter_by_genre(data: dict, genre: str) -> list:
    tracks = []
    for track in data.values():
        if track["genre"] == genre:
            tracks.append(track)
    return tracks


# Filter only the first song of each artist in dataset
def get_artist_first_song(data: list) -> list:
    artists_seen = set()
    first_songs = []
    for track in data:
        if track["artist"] in artists_seen:
            continue
        else:
            first_songs.append(track)
            artists_seen.add(track["artist"])
    return first_songs


# Show the songs with that genre and ask for a selection by the user
def select_songs(tracks: list) -> list:
    selected = []
    print("\nChoose songs you like(0 to finish):")
    for i, song in enumerate(tracks, 1):
        print(f"{i}) {song['name']} ({song['artist']})")
    while True:
        try:
            choice = int(input("Choice: "))
            if choice == 0:
                break
            if choice < 0 or choice > len(tracks):
                print("invalid option, try again!")
                continue
            song = tracks[choice - 1]
            if song in selected:
                print(f"You already selected {song['name']}!")
            selected.append(tracks[choice - 1])
        except ValueError:
            print("invalid option, try again!")
    return selected


def command_line_interface() -> list:
    print("=== Music Tool Recommender ===")
    data = load_data()
    genre = get_genre()
    tracks = filter_by_genre(data, genre)
    first_songs = get_artist_first_song(tracks)
    selected = select_songs(first_songs)
    return genre, selected
