__author__ = 'Amit'

from bs4 import BeautifulSoup
# noinspection PyUnresolvedReferences
from WS_Specs import ws_specs


def title_string_scrap(html_response_data):
    """
    A) Takes html response data (bytes)--> Returns string value in the title section
    """
    soup = BeautifulSoup(html_response_data)
    return soup.title.string.strip()


# noinspection PyBroadException
def clean_up_name(name_str, name_remove_str):
    """
    A) Takes a string value and cleans up the string to be removed (Both provided by calling function)
    B) Returns original string if name_remove_str is not found in name_str
    """
    try:
        val = name_str.index(name_remove_str)
        name = name_str[: val]
        return name
    except:
        return name_str


def data_scrap(html_text, data_marker_str, data_start_str, data_end_str):
    """
    A) Takes html page as text and three string parameters (**All 4 provided by calling function**) to locate data
    B) 'Data' as string 0r 'None - Value Error'
    1) data_marker-str-->identify the block for data-->Unique to page being scraped
    2) data_start_str-->identify position on left of data-->Unique to page being scraped
    3) data_end_str-->identify position on right of data-->Unique to page being scraped
    """
    # noinspection PyBroadException
    try:
        data_marker_pos = html_text.index(data_marker_str)
        data_start_pos = html_text.index(data_start_str, data_marker_pos)
        data_end_pos = html_text.index(data_end_str, data_marker_pos)
        data_text = html_text[data_start_pos + 1:data_end_pos]
    except:
        data_text = 'None - Value Error'
    return data_text


def get_title_plus_data(html_response_data):
    # Using Response data to pull Title - Name
    data_title_string = title_string_scrap(html_response_data)
    data_title_clean = clean_up_name(data_title_string, ws_specs['name_remove_str'])

    #  Extract HTML text from data to pull data
    soup = BeautifulSoup(html_response_data)
    html_text = soup.get_text()
    data_string = data_scrap(html_text, ws_specs['data_marker_str'], ws_specs['data_start_str'], ws_specs['data_end_str'])
    return [data_title_clean, data_string]











