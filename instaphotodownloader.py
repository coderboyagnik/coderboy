import instaloader

def download_photo(coderboy_agnik):
    loader = instaloader.Instaloader()
    loader.download_profile(username, profile_pic_only=True)

if __name__ == "__main__":
    username = input("Enter Instagram username: ")
    download_photo(username)
