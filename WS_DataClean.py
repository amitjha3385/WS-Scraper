__author__ = 'Amit'
# noinspection PyUnresolvedReferences
from WS_text_file_module import write_text_file


def extract_team_data_list(string_data):
    """
    This operation is WS specific. depends on the kind of data from WS
    Extracting player data from Team data
    Takes a string of the form Converts string data to list--> Data was saved in form '[Team_name, Data]'
    eval(read_data) gives a list; eval(read_data)[1] gives Data(string) from that list
    Finally returns the team data in the form of a list--> Each entry corresponds to one player
    """
    team_data = eval(string_data)[1]

    # Removes the initial '{' from the string Data
    team_data= team_data[1:]

    # Splits team data into data for each player
    # the player data ends with '{' followed by ',' and starts with '}'
    team_data = team_data.split('},{')
    return team_data


def fix_accidental_split(player_data_list):
    """
    This is WS specific data splitting headache!
    Take a list of player data and fixes all the accidental splits
    Returns the player data as list
    """
    # Not important data has been split... the remainder can be fixed later
    for num, field in enumerate(player_data_list):
        if ':' not in list(field):
            player_data_list[num] = ''
            player_data_list[num-1] = ''
        if '{' in list(field) or '}' in list(field):
            player_data_list[num] = ''

    # Remove the empty cells
    while '' in player_data_list:
        player_data_list.remove('')

    return player_data_list


def clean_up_non_python(list_):
    """
    WS Specific only to create player bio function to remove null and true
    List is in form of key, value as called by function
    input should be of form key, value
    """
    if list_[1] == 'null':
        list_[1] = 'None'
    elif list_[1] == 'true':
        list_[1] = 'True'
    elif list_[1] == 'false':
        list_[1] = 'False'
    return list_


def create_player_bio_dict(player_data_list):
    """
    Takes a list of player data with only bio data type entries
    Cleans up non python specific values like null and true to None and True
    Returns a dictionary for the player
    """
    player_data_dict = {}
    for num, field in enumerate(player_data_list):
        list_field = field.split(':')
        list_field = clean_up_non_python(list_field)
        player_data_dict[eval(list_field[0])] = eval(list_field[1])
    return player_data_dict


def player_data(string_data):
    team_data = extract_team_data_list(string_data)
    for player in team_data:
        player_data_list = player.split(',')
        fix_accidental_split(player_data_list)
        player_data_dict = create_player_bio_dict(player_data_list)
        write_text_file(player_data_dict)