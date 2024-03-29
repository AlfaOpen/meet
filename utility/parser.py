import numpy


def parse_method_name(method_name: str):
    length = len(method_name)
    new_method_name = []
    characters = []
    characters[:] = method_name
    for i in range(0, len(characters)):
        if i == 0 and 65 <= ord(method_name[i]) <= 90:
            new_method_name.append(method_name[i].lower())
        elif i != 0 and 65 <= ord(method_name[i]) <= 90 and 65 <= ord(method_name[i - 1]) <= 90:  # condizione aggiunta
            # affinchè ID me lo scriva "id"
            new_method_name.append(method_name[i].lower())
        elif i != 0 and 65 <= ord(method_name[i]) <= 90:
            new_method_name.append('_')
            new_method_name.append(method_name[i].lower())
        else:
            new_method_name.append(method_name[i])
    new_method_name_str = ''
    for i in range(0, len(new_method_name)):
        new_method_name_str = new_method_name_str + new_method_name[i]
    return new_method_name_str


def parse_method_element(element):
    verifica = numpy.isnan(element)
    if verifica:
        output = None
    else:
        output = element
    return output
