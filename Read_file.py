import json

KEY_SEPARATORS = [":", "//"]

swift_msg = "{1:F01PRCBBGSFAXXX0000001163}{2:I199TRCKCHZZXXXXN}{3:{121:caa9ab6a-d5d2-472d-90b3-8d512ea0e98b}}{4:" \
            ":20:00000000116" \
            ":21:15133842" \
            ":79://2011200900+0200" \
            "//ACCC" \
            "//PRCBBBBB" \
            "//BGN15893,52" \
            "//EXCH//USD/BGN/1,626000" \
            "-}"

fields = swift_msg.split("}{")


def parse_message_as_dict(segments):
    data = {}

    for segment in segments:
        segment = segment.replace("{", "").replace("}", "").replace("\n", "")
        message = segment.split(KEY_SEPARATORS[0], 1)
        message[1] = check_for_subkeys(message[1])
        data.update({message[0]: message[1]})
    return data


def check_for_subkeys(message):
    if KEY_SEPARATORS[0] in message:

        if message.startswith(KEY_SEPARATORS[0]):
            message = message[1:]

        subkeys = message.split(KEY_SEPARATORS[0])

        if len(subkeys) > 2:
            return find_and_parse_special_message(subkeys)

        return {subkeys[0]: subkeys[1]}
    return message


def find_and_parse_special_message(subkeys):
    subdict = {}
    for iterator, subkey in enumerate(subkeys):

        if iterator % 2 == 0:
            subdict.update({subkey: subkeys[iterator + 1]})
            if KEY_SEPARATORS[1] in subkeys[iterator + 1]:
                special_subdict = handle_special_message(subkeys[iterator + 1], subkeys[iterator])
                subdict.update(special_subdict)
    return subdict


def handle_special_message(message, subkey):
    if message.startswith(KEY_SEPARATORS[1]):
        message = message[2:]
    message = message.split(KEY_SEPARATORS[1])

    special_subdict = {
        'date': message[0][:8],
        'time': message[0][8:],
        'bank': message[1],
        'account': message[2],
        'amount': float(message[3][3:].replace(',', '.')),
        'operation': message[4],
        'currency_pair': message[5][:7],
        'exchange_rate': float(message[5][8:-1].replace(',', '.')),
    }
    return {subkey: special_subdict}

### print JSON file ###

#print(json.dumps(parse_message_as_dict(fields), indent=4))

### print every key, value on new line ###
for key, value in parse_message_as_dict(fields).items():
    try:
        for sub_key, sub_value in value.items():

            try:
                for sub_sub_key, sub_sub_value in sub_value.items():
                    print(f"Tag: {sub_key} -> {sub_sub_key}: {sub_sub_value}")
            except:
                print(f"Tag: {key} -> Sub_tag: {sub_key} -> {sub_value}")
    except:
        print(f"Tag: {key} -> {value}")
