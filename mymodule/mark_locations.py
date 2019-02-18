import get_json
import folium
import requests


def get_locations(dct):
    #  get user's object
    lst_users = dct['users']
    ans = list()

    #  create list with locations
    for el in lst_users:
        ans.append((el['screen_name'], el['location']))
    return ans

def get_coordinates(lst):

    coor_lst = list()
    GOOGLE_MAPS_API_URL = 'https://maps.googleapis.com/maps/api/geocode/json'

    for el in lst:
        params = {
            'address': el[1],
            'sensor': 'false',
            'key': 'AIzaSyDdO3p0H7ortsOLqh2Pr4LtiVXY1JpPQSI'
        }

        # Do the request and get the response data
        req = requests.get(GOOGLE_MAPS_API_URL, params=params)
        res = req.json()

        # Use the first result
        if not res['results']:
            #print(res)
            continue
        result = res['results'][0]

        lat = result['geometry']['location']['lat']
        lng = result['geometry']['location']['lng']
        coor_lst.append([lat, lng, el[0]])
    return coor_lst


def draw_map(lst_locations, user):

    # Create an empty map
    my_map = folium.Map(location=[48.314775, 25.082925], zoom_start=4)

    # Add all coordinates from list into one feature group
    users = folium.FeatureGroup(name="Map")
    for el in lst_locations:
        location = [el[0], el[1]]
        users.add_child(folium.Marker(location=location,
                                      popup=el[2], icon=folium.Icon()))

    #  Create and save the map
    my_map.add_child(users)
    my_map.save('templates/Map_{}.html'.format(user))


def main(user):
    dct = get_json.get_object(user)
    lst = get_locations(dct)
    coor_lst = get_coordinates(lst)
    draw_map(coor_lst, user)