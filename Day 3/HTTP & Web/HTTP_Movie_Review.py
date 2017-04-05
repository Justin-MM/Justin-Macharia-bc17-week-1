# this application consumes a New York Movie Times Review API
# users can search for a movies by its title and a receive a short summary and rating(if available)
# ensure that the command prompt or shell it runs on has utf-8 configuration on else the requests won't load
# also ensure the requisite modules are installed

import simplejson as json
import requests
import pprint

def get_movie_review():
    print ("")
    print ("")
    print ("          WELCOME       ")
    print ("")
    print ("")
    query = input("Enter a movie title to search(e.g superman): ")
    print ("")
    print ("")

    while not isinstance(query, str):
        query = input("Enter a movie title to search(e.g superman): ")

    my_request = requests.get('https://api.nytimes.com/svc/movies/v2/reviews/search.json?query=' + query +'&api-key=75357ca6a1774e03a2b4754329fdbab2')
    print(type(my_request))

    my_request.headers['content-type']
    my_request = my_request.text
    my_request.encode('ASCII', 'ignore').decode('ASCII')

    # filter results from response to only relevant subjects
    filtered_dict = {k:v for k,v in ((json.loads(my_request))).items() if k in ["status", "copyright"]}
    print(filtered_dict)

    for item in ((json.loads(my_request)))["results"]:

        results_dict = {k:v for k,v in sorted(item.items()) if k in ["headline", "display_title", "mpaa_rating", "summary_short"]}
        print("")
        print("")
        pprint.pprint(results_dict)

    ask = input("Found what you wanted? Press Y to search: ")
    if ask in ['Y', 'y']:
        get_movie_review()
        print("Press CTRL + C to quit")
    else:
        print("Invalid! Press CTRL  C to quit")
        get_movie_review()

if __name__ == "__main__":
    get_movie_review()
__author__ = 'Justin M'
