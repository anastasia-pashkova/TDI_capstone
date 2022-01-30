import requests
# import dill
from bs4 import BeautifulSoup
from datetime import datetime
from collections import namedtuple
import string

EmplContributions = namedtuple('EmplContributions', ['username', 'count', 'date'] )
_BASE_URL = f'https://github.com/users/'


def get_user_contributions(user: string, start_date: string, end_date: string):
    url = f'{_BASE_URL}{username}/contributions?from={start_date}&to={end_date}'

    page = requests.get(url)

    soup = BeautifulSoup(page.text, "lxml")

    svg = soup.find('svg', attrs={'class': 'js-calendar-graph-svg'})

    rects = svg.find_all('rect', attrs={'class': 'ContributionCalendar-day'})

    contributions = []
    for rect in rects:
        contribution = EmplContributions(username=username, count=rect.get('data-count'), date=rect.get('data-date'))
        contributions.append(contribution)
        print(contribution)
    return contributions


if __name__ == '__main__':
    # example user:
    username = 'domofactor'
    from_date = '2021-01-01'
    to_date = '2021-12-31'

    get_user_contributions(username, from_date, to_date)


#print(contributions)


# ---------------------------------------------------------
# find all users:
# https://github.com/orgs/github/people?page=9&query=
# OR
# https://api.github.com/orgs/github/members?page=1

# an API, but needs authentication
# https://api.github.com/orgs/github/memberships/domofactor
# {
#   "message": "Requires authentication",
#   "documentation_url": "https://docs.github.com/rest/reference/orgs#get-organization-membership-for-a-user"
# }
