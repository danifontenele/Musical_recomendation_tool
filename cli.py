import json

# function that read("r") and load the json file to return it as a dictionary
def load_data() -> dict:
    with open("data/data_set.json", "r") as f:
        data = json.load(f)
    return data


# Get the first input, the genre
def get_genre():
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


# Select the songs with the same choosen genre among data_set dict options
def filter_by_genre(data: dict, genre: str):
    tracks = []
    for track in data.values():
        if track["genre"] == genre:
            tracks.append(track)
    return tracks


# Show the songs with that genre and ask for a selection by the user
def select_songs(tracks: list):
    selected =[]
    print("\nChoose songs(0 to finish):")
    for i, song in enumerate(tracks, 1):
        print(f"{i}) {song['name']} ({song['artist']})")

    while True:
        try:
            choice = int(input("Choice: "))
            if choice == 0:
                break
            if choice >= 1 and choice <= len(tracks):
                selected.append(tracks[choice - 1])
        except ValueError:
            print("invalid option, try again!")
    return selected


def main():
    print("=== Music Tool Recommender ===")

    data = load_data()
    genre = get_genre()
    tracks = filter_by_genre(data, genre)
    selected = select_songs(tracks)

    print("\nYou selected:")
    for song in selected:
        print(f"- {song['name']} ({song['artist']})")


if __name__ == "__main__":
    main()
