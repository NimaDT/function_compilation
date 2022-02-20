def dict_make(dataseries):
    """Takes list or series of a dataframe and makes a dictionary of all elements.
    Parameters: 
    dataseries (list or Pandas series): The set of data whose elements to make dictionary from
    
    Returns:
    final_dict: Dictionary of elements in dataseries"""
    unique = {element for element in dataseries}
    unique_list = [element for element in unique]
    final_dict = {index:unique_list[index] for index in range(0, len(unique_list))
            }
    return final_dict


def list_interpreter(in_list, in_dict):
    """Takes a list of keys and a dictionary containing key-value pairs corresponding to keys in list. Returns interpretation of old list.
    Parameters:
    in_list (list): a list containing elements matching the keys in dictionary
    in_dict (dict): dictionary used to intepret elements in list
    
    Returns:
    new_list: interpreted version of in_list"""
    new_list = []
    for value in in_list:
        new_list.append(in_dict[value])
    return new_list


def interpret_insert(list, dataframe):
    pass


def reverse_dict(in_dict):
    """Reverses key-value pairs of input
    Parameters:
    in_dict (dict): dictionary to be reversed
    
    Returns:
    reversed_dict: version of in_dict with key-value pairs reversed"""
    reversed_dict = {in_dict[index]:index for index in range(0, len(in_dict))}
    return reversed_dict
