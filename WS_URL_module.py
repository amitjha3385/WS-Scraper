__author__ = 'Amit'
# noinspection PyUnresolvedReferences
from WS_Specs import ws_specs


def url_gen(url_key, url_num):
    """
    Takes a string URL key-->key for dictionary ws_specs--> and generates url in conjunction with url_num
    Takes an integer--> URL num-->Team Id or Player Id
    Returns double quoted string to allow for use in http.request which does not accept iterable
    Ex. url_key = teams_main_url-->'http://www.whoscored.com/Teams/'
        url_num = 52--> for Real Madrid
        Returns--> "'http://www.whoscored.com/Teams/52'"
        can be directly used in the eval function to give string input to http.request('GET',eval(url))
    """
    url = ws_specs[url_key] + str(url_num)
    return repr(url)






