def identify_dog_breed(weight, coat_length):
    if weight < 20:
        if coat_length == "short":
            return "Swedish Vallhund"
        elif coat_length == "medium":
            return "Mudi"
        else:
            return "Shetland Sheepdog"
    elif weight < 50:
        if coat_length == "short":
            return "Pembroke Welsh Corgi"
        elif coat_length == "medium":
            return "Australian Shepherd"
        else:
            return "Bearded Collie"
    elif weight < 80:
        if coat_length == "short":
            return "Belgian Malinois"
        elif coat_length == "medium":
            return "German Shepherd"
        else:
            return "Collie"
    else:
        if coat_length == "short":
            return "Beauceron"
        elif coat_length == "medium":
            return "Bouvier des Flandres"
        else:
            return "Old English Sheepdog"