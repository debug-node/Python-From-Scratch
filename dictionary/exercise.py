language = {
    "Bihar" : "Bhojpuri",
    "Delhi" : "Hindi",
    "Rajasthan" : "Rajasthani",
    "Karnataka" : "kanada"
}
language["Gujarat"] = "Gujarati" # edit item

# language = {} # make empty of existing dict

# print(language["Bihar"])

# language["Bihar"] = "Bhojpuri","Maithili", # edit item

for key in language:
    # print(key)
    print(key,language[key])  