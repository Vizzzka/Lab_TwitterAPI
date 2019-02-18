import get_json
import json


def print_inserted_dict(dct):

    new_dct = dct.copy()
    for key, val in dct.items():

        #  replace all lists and dictionaries by ' + ' to mark big content
        if (type(val) is dict) or (type(val) is list):
            new_dct[key] = ' + '
        else:
            new_dct[key] = val

    #  print dictionary as a string
    s = json.dumps(new_dct, indent=4)
    print(s)


def go_down(next_level):

    #  if next_level is list then change it on dict
    if type(next_level) is list:
        new_dct = dict()
        for i in range(len(next_level)):
            new_dct['object {}'.format(i)] = next_level[i]
        return new_dct
    else:
        return next_level


def show_json_struct(main_dct):

    # current level and dictionary
    current_level = 0
    current_dct = main_dct

    # list of all previous levels
    lst = []

    # get requests from user
    while True:

        #  print current dict and ask for new request
        print("Current level is {}".format(current_level))
        print_inserted_dict(current_dct)
        ans = input("Enter 'key' where key is value which you want"
                    " to know \nEnter 'end' to exit \nEnter 'back'"
                    " to move to previous level \n")

        # end the program
        if ans == 'end':
            break

        #  change current dictionary on previous
        #  using lst - list of previous levels
        if ans == 'back':
            if current_level:
                current_dct = lst.pop()
                current_level -= 1
                continue
            else:
                print("You are on the floor")
                continue

        # go down and add new level in lst
        lst.append(current_dct)
        current_level += 1
        current_dct = go_down(current_dct[ans])


if __name__ == '__main__':
    dct = get_json.get_object('usacheva_v')
    show_json_struct(dct)
