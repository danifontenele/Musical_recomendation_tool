import cli
import engine


def main():
    selected_list = cli.command_line_interface()
    engine.engine(selected_list)


if __name__ == "__main__":
    main()
