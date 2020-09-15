import sys

sys.path.append("Functions")
sys.path.append("../Functions")
import defaults
import APIFunctions as af


def getRecentMatches():
    allRecentMatches = []
    matchIds = []
    for accountId in defaults.ACCOUNT_IDS:
        playerRecentMatches = af.getPlayerRecentMatches(accountId)
        for recentMatch in playerRecentMatches:
            if not recentMatch["match_id"] in matchIds and recentMatch["party_size"] > 3:
            # if not recentMatch["match_id"] in matchIds:
                allRecentMatches.append(recentMatch)
                matchIds.append(recentMatch["match_id"])
    return allRecentMatches