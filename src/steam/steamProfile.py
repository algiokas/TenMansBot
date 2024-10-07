import urllib.request
from bs4 import BeautifulSoup

STEAM_PROFILE_BASE_URL="https://steamcommunity.com/profiles/"

class SteamProfile:
    def __init__(self, id):
        self.id = id
        self.miniprofile = ""

        fp = urllib.request.urlopen(STEAM_PROFILE_BASE_URL + id)
        if fp.status is 200:
            profileData = fp.read()
            profileString = profileData.decode("utf8")
            fp.close()

            soup = BeautifulSoup(profileString, features="html.parser")
            miniprofile = soup.find(lambda tag: tag is not None and tag.has_attr("data-miniprofile"))
            if (miniprofile is not None):
                self.miniprofile = miniprofile["data-miniprofile"]
        else:
            print(f"could not open profile with ID: {id} - Response Code {fp.status}")




    


