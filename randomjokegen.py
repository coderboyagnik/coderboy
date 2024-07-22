import requests

def get_joke():
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    joke = response.json()
    print(f"{joke['setup']} - {joke['punchline']}")

if __name__ == "__main__":
    get_joke()
