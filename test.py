# client.py

from game import MainWindow


def main():
    # Create an instance of MainWindow
    main_window = MainWindow()

    # Data you want to pass to update_game function
    data = "Hello from client.py!"

    # Call update_game function on the instance
    main_window.update_game(data)


if __name__ == "__main__":
    main()
