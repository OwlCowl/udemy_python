def test_authorisation(user):
    credentials = {}
    if user in ['LSEG', 'MDASS', 'London']:
        credentials[user] = 'green'
    else:
        credentials[user] = 'red'
    return credentials

