dictionary_name = {
    "key1": {
        "Name1":"Hari",
        "Age":"25",
        "id":"12345"
    },
    "key2": {
        "Name2":"Aruna",
        "Age":"25",
        "id":"678910"
    }

}

dictionary_name["key1"] ["Name1"]="Hari"
print(dictionary_name)


for i in dictionary_name.keys():
    print(i)
    for a in dictionary_name[i].items():
        print(a)