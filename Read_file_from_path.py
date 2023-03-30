while True:
    relatative_file_path = input("Enter file path: ")
    result = {}

    try:
        with open(relatative_file_path, 'r') as file:
            lines = file.read().splitlines()
            current_key = ''
            for line in lines:
                if line.startswith(":"):

                    try:
                        key, value = line[1:].split(":")
                        result[current_key.strip()].update({key.strip(): value.strip()})

                    except:
                        key, value = line[1:].split("::")
                        result[current_key.strip()].update({key.strip(): value.strip()})

                else:
                    current_key = line[1:-1].strip()
                    result[current_key.strip()] = {}

        for key, value in result.items():
            print(key)

            for sub_key, sub_value in value.items():
                print(f"{sub_key} -> {sub_value}")

        break

    except FileNotFoundError:
        print("Wrong file path")