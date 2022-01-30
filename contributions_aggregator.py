import contributions


def contributions_aggregator():
    # call the contribution functions from here

    username = 'domofactor'
    from_date = '2021-01-01'
    to_date = '2021-12-31'

    contributions.get_user_contributions(username, from_date, to_date)

    # pass


if __name__ == '__main__':
    contributions_aggregator()
