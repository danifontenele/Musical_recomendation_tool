def get_genre() -> int:
    genre = int(input("Select the genre you're looking for:\n"
                      "1) Pop\n"
                      "2) Rock\n"
                      "3) Hip-hop\n"))
    return genre


def get_pop_list() -> list:
    song = None
    song_list = []
    while song != 21:
        song = int(input(
                        "Choose the songs you like in this list:\n"
                        "1) Hotline Bling(Drake)\n"
                        "2) Pumped Up Kicks(Foster the people)\n"
                        "3) What you know(Two Door Cinema Club)\n"
                        "4) Timeless(The Weeknd)\n"
                        "5) One Dance(Drake)\n"
                        "6) Locked Out Of Heaven(Bruno Mars)\n"
                        "7) Somebody that I used to know(Gotye)\n"
                        "8) Memories(David Guetta)\n"
                        "9) Can't feel my face(The weeknd)\n"
                        "10) Paradise(Cold Play)\n"
                        "11) Feel so close - Calvin Harris\n"
                        "12) Love on the brain(Rihanna)\n"
                        "13) Riptide(Vance Joy)\n"
                        "14) Kiss me more(Doja Cat)\n"
                        "15) Get Lucky(Daft Punk)\n"
                        "16) Messy(Lola Young)\n"
                        "17) Work(Rihanna)\n"
                        "18) Birds Of a Feather(Billie Eilish)\n"
                        "19) Adore You(Harry Styles)\n"
                        "20) Espresso(Sabrina Carpenter)\n"
                        "21) Done\n"))
        # 3) Get the answer and save it into a list
        song_list.append(song)
    return song_list


# Main calls all other functions
def main() -> None:
    print("=== Music Tool Recomender ===")
    # 1) Show a numbered list of genres to the user
    genre = get_genre()
    # 2) Show a numbered list of musics to the user(1 list per genre choosen)
    if genre == 1:
        song_list = get_pop_list()
    print(f"Choosen ids:\n{song_list}")
    # 4) Use the ids


if __name__ == "__main__":
    main()
