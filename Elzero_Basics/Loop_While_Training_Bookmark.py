# -----------------------------
# -- Loop =>  While Training --
# -- Simple Bookmark Manage  --
# -----------------------------
from numpy.ma.core import maximum

# Empty List To Fill Later
myFavouriteWebsite = []
# Maximum Allowed Websites
maximumWebsite = 5
while maximumWebsite > 0:
    web = input("Website Name Without https://")
    myFavouriteWebsite.append(f"https://{web.strip().lower()}")
    maximumWebsite -= 1
    print(f"Website Add: {myFavouriteWebsite} Places left")
    print(maximumWebsite)
else:
    print("Bookmark is full")
# Check If List Not Empty
if len(myFavouriteWebsite) > 0:
    myFavouriteWebsite.sort()
    index = 0
    print("printing The List of websites in your "
          "Bookmark")
    while index < len(myFavouriteWebsite):
        print(myFavouriteWebsite[index])
        index = index + 1
