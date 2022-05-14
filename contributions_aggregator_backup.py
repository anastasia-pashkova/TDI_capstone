import contributions
import csv
from datetime import datetime
import time

def contributions_aggregator(org='github', filename='contributions.csv'):
    # call the contribution functions from here

    # username = 'domofactor'
    # TODO: not hardcode dates
    # TODO: make date datetime 
    from_date = '2021-01-01'
    to_date = '2021-12-31'

    # contributions.get_user_contributions(username, from_date, to_date)

    usernames = contributions.get_users(org=org)
    all_contributions = []
    
    # TODO just testing - remove this
    # usernames2 = usernames[:1]

    # TODO extend with other users here
    usernames.extend(['domofactor', 'donal', 'dctucker', 'bwestover', 'ashishkeshan', 'oakeyc'])

    with open(filename, 'w') as f:
        w = csv.writer(f)
        w.writerow(contributions.CONTRIBUTION_PROPERTIES) 

        for user in usernames:
            # # getting the next batch
            # if user < 'darcyclarke':
            #     continue

            # sleep
            time.sleep(3)
            print(f'getting user: {user}')
            try:
                current_page_contributions = contributions.get_user_contributions(user, from_date, to_date)
            except AttributeError :
                print(f'!!!bad user: {user}')
                continue
            w.writerows([(c.username, c.count, c.date) for c in current_page_contributions])

            # for user_contrib in current_page_contributions:
            #     print(user_contrib)
            #     w.writerows([(c.username, c.count, c.date) for c in current_page_contributions])

    #print(all_contributions[0])
    
    # with open(filename, 'w') as f:
    #     w = csv.writer(f)
    #     w.writerow(contributions.CONTRIBUTION_PROPERTIES)
    #     for user_contrib in all_contributions:
    #         w.writerows([(c.username, c.count, c.date) for c in user_contrib])

if __name__ == '__main__':

    org = 'github'
    dt = datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = f'contributions-{org}-{dt}.csv'
    contributions_aggregator(org=org, filename=filename)
