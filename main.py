import cli
import input_profile
import engine


def main():
    genre, selected_list = cli.command_line_interface()
    profile = input_profile.input_profile(selected_list, genre)
    engine.engine(profile)


if __name__ == "__main__":
    main()
