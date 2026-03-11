def get_data(selected_list: list, artists: set, decades: set) -> None:
    for track in selected_list:
        artists.add(track["artist"])
        decades.add((track["year"] // 10) * 10)


def input_profile(selected_list: list, input_genre: str):
    artists = set()
    decades = set()
    genre = input_genre
    reference_tracks = selected_list
    get_data(selected_list, artists, decades)
    profile = {
        "genre": genre,
        "artists": artists,
        "decades": decades,
        "reference_tracks": reference_tracks
    }
    return profile
