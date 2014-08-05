__author__ = 'Amit'

import urllib3
# noinspection PyUnresolvedReferences
from TextScrap import get_title_plus_data
# noinspection PyUnresolvedReferences
from WS_Specs import ws_specs
# noinspection PyUnresolvedReferences
from WS_URL_module import url_gen
# noinspection PyUnresolvedReferences
from WS_text_file_module import write_text_file

file_path = '/home/ketkee/Documents/WS Data/PlayerIncomplete/'
file_name = 'Players500-inc.txt'
file = file_path + file_name


def main_crawl():
    # Instantiate urllib3 PoolManager() object as http
    http_obj = urllib3.PoolManager()
    # start to crawl
    with open(file, 'r') as f:
        for line in f:
            player_dict = eval(line)
            if player_dict != {}:
                num = player_dict['PlayerId']
                # Tracker
                print('fetching url {!s}'.format(num))

                # Get url based on num, and key word:
                url = url_gen('players_main_url', num)

                # Fetch response from url
                response = http_obj.request('GET', eval(url))

                #  Fetching data for the URL
                data_list_row = get_title_plus_data(response.data)

                # Write data to WS_Output.txt file on file path -->file_path = '/home/ketkee/Documents/WS Data/
                write_text_file(data_list_row)
    f.closed
main_crawl()
