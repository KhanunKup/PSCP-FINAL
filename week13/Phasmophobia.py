"""Phasmophobia"""
def ghost():
    """Find the possible ghost that might appear"""
    ghosts_evidence = {
    "Banshee": {"EMF Level 5", "Fingerprints", "Freezing Temperatures"},
    "Demon": {"Ghost Writing", "Freezing Temperatures", "Spirit Box"},
    "Jinn": {"EMF Level 5", "Ghost Orb", "Spirit Box"},
    "Mare": {"Spirit Box", "Ghost Orb", "Freezing Temperatures"},
    "Oni": {"EMF Level 5", "Ghost Writing", "Spirit Box"},
    "Phantom": {"EMF Level 5", "Ghost Orb", "Freezing Temperatures"},
    "Poltergeist": {"Fingerprints", "Ghost Orb", "Spirit Box"},
    "Revenant": {"EMF Level 5", "Fingerprints", "Ghost Writing"},
    "Shade": {"EMF Level 5", "Ghost Writing", "Ghost Orb"},
    "Spirit": {"Fingerprints", "Ghost Writing", "Spirit Box"},
    "Wraith": {"Fingerprints", "Spirit Box", "Freezing Temperatures"},
    "Yurei": {"Ghost Writing", "Ghost Orb", "Freezing Temperatures"}
    }
    item_found = set()
    found = False
    for _ in range(3):
        item = input()
        if item == "No evidence":
            continue
        item_found.add(item)
    for key, value in ghosts_evidence.items():
        if item_found.issubset(value):
            found = True
            print(key)
    if not found:
        print("Not yet discovered")
ghost()
