class Parser:
    def parse_method_name(self, method_name: str):
        length = len(method_name)
        new_method_name = []
        characters = []
        characters[:] = method_name
        for i in range(0, len(characters)):
            if i == 0 and 65 <= ord(method_name[i]) <= 90:
                new_method_name.append(method_name[i].lower())
            elif i != 0 and 65 <= ord(method_name[i]) <= 90:
                new_method_name.append('_')
                new_method_name.append(method_name[i].lower())
            else:
                new_method_name.append(method_name[i])
        return str(new_method_name)
