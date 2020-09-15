import requests

def getPlayerRecentMatches(accountId):
    uri = "https://api.opendota.com/api/players/" + str(accountId) + "/recentMatches"
    r = requests.get(uri)
    return r.json()
    
def getMatchData(matchId):
    uri = "https://api.opendota.com/api/matches/" + str(matchId)
    r = requests.get(uri)
    return r.json()
