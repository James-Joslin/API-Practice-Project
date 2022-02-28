def nested_func(idx):
    import requests
    import json
    import dash
    import dash_core_components as dcc
    import dash_html_components as html
    api_Dict = {
        "spells": "https://api.open5e.com/spells/",
        "monsters": "https://api.open5e.com/monsters/",
        "magicitems": "https://api.open5e.com/magicitems/"
        # "feats": "https://api.open5e.com/feats/",
        # "races": "https://api.open5e.com/races/",
        # "classes": "https://api.open5e.com/classes/",
        # "weapons": "https://api.open5e.com/weapons/"
    }
    link = list(api_Dict.values())[idx]

    # Repeated functions
    def final_api(api):
        item = input()
        item = item.lower()
        if " " or "_" in item:
            item = item.replace(" ", "-")
            item = item.replace("_", "-")
        final_url = str(api + item)
        return final_url

    def get_data(conn_string):
        response = requests.get(conn_string)
        pretty_json = json.loads(response.text)
        # pretty_json = json.dumps(pretty_json, indent=2)
        return pretty_json

    # Final functions
    def func_spells(api):
        print("Enter spell name:")
        data = get_data(conn_string=final_api(api))
        print('\n')
        try:
            datastruct_list = [
                str(data.get('name')),
                str(data.get('level') + " " + data.get('school') + " | " + data.get('dnd_class')),
                "\n------------------------------------------------------------------------------\n",
                str("Range: " + data.get('range')),
                str("Casting Time: " + data.get('casting_time')),
                str("Duration: " + data.get('duration')),
                str('Components: ' + data.get('components') + ' (' + data.get('material') + ')'),
                "\n------------------------------------------------------------------------------\n",
                str(data.get('desc'))
            ]

            if data.get('higher_level') != "":
                addl_string = "\n------------------------------------------------------------------------------\n" + str("\nAt higher levels: " + data.get('higher_level'))
                datastruct_list.append(addl_string)

            for element in datastruct_list:
                print(element)
        except:
            print("Spell not found\nIs it spelt correctly?")

    def func_monsters(api):
        print("Enter monster name:")
        data = get_data(conn_string=final_api(api))
        print(data)

    def func_magic_items(api):
        print("Enter magic item:")
        data = get_data(conn_string=final_api(api))
        print(data)

    def func_feats(api):
        print("Enter feat:")
        data = get_data(conn_string=final_api(api))
        print(data)

    def func_races(api):
        print("Enter race:")
        data = get_data(conn_string=final_api(api))
        print(data)

    def func_classes(api):
        print("Enter class:")
        data = get_data(conn_string=final_api(api))
        print(data)

    def func_weapons(api):
        print("Enter weapon name:")
        data = get_data(conn_string=final_api(api))
        print(data)

    func_list = [
        func_spells,
        func_monsters,
        func_magic_items,
        func_feats,
        func_races,
        func_classes,
        func_weapons
    ]
    func_list[idx](api=link)
