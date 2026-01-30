import requests
import sys


def main(username):
    url = "https://api.github.com/users/alveskz/events"
    response = requests.get(url).json()

    if response.status_code == 200:
        event = response.json()
        latest_events = event
    else:
        print(f"Error fetching events for {username}: {response.status_code}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("Please enter a GitHub username as a command line argument.")