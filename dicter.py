def dict_make(dataseries):
    unique = {element for element in dataseries}
    unique_list = [element for element in unique]
    final_dict = {index:unique_list[index] for index in range(0, len(unique_list))
            }
    return final_dict


def list_interpreter(list, dict):
    new_list = []
    for value in list:
        new_list.append(dict[value])
    return new_list


def interpret_insert(list, dataframe):
    pass


def reverse_dict(in_dict):
    reversed_dict = {in_dict[index]:index for index in range(0, len(in_dict))}
    return reversed_dict
