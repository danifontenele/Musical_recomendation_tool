import cli
import input_profile
import engine


def main():
    genre, selected_list = cli.command_line_interface()
    profile = input_profile.input_profile(selected_list, genre)
    top_tracks = engine.engine(profile)
    print("\n=== Recommended songs ===")
    for i, (track, score) in enumerate(top_tracks, 1):
        print(f"{i}. {track["name"]} - {track["artist"]}")
    print("\n=== Scores by music ===")
    for i, (track, score) in enumerate(top_tracks, 1):
        print(f"{i}. {track["name"]} - {track["artist"]}: {score}")


if __name__ == "__main__":
    main()
