import json, json

def bubble(reviews, rest_search, rest_name):
    '''
    Visualize  Restaurant Avg Price, Rating & Review length
    '''
    visual = {}
    for restid, stuff in rest_search.items():
        name = rest_name[restid].title()
        rating = stuff[0]
        details = stuff[1]
        all_reviews = reviews[restid]
        no_reviews = len(all_reviews)

        #Set params to zero in each loop
        tot_price = 0
        tot_length = 0

        #Getting Avg price and popularity
        for info in details.values():
            tot_price += int(str(info[0]))

        #Calculating total words in all reviews
        for review in all_reviews:
            tot_length += len(review[0].split())

        visual[str(name)] = (str(rating), tot_price/no_reviews,
                             tot_length/no_reviews)

    return visual




if __name__ == '__main__':

    file = open("data/Reviews.json",'r')
    reviews = json.load(file)

    file = open("data/rest_search.json",'r')
    rest_search = json.load(file)

    file = open("data/restname_id.json",'r')
    rest_name = json.load(file)

    visual = bubble(reviews, rest_search, rest_name)

    with open('visualizations/restaurant_avg.json', 'wb') as f:
        json.dump(visual,f)