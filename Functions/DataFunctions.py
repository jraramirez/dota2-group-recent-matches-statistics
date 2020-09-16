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
            # if not recentMatch["match_id"] in matchIds and recentMatch["party_size"] > 3:
            if not recentMatch["match_id"] in matchIds and recentMatch["version"]:
                allRecentMatches.append(recentMatch)
                matchIds.append(recentMatch["match_id"])
    # print(len(matchIds))
    # for match in allRecentMatches:
    #     print(match["match_id"])
    return allRecentMatches


def parseRecentMatches(recentMatches):
    for match in recentMatches:
        af.parseMatch(match["match_id"])
    return True


def matchWon(match):
    side = "RADIANT" if match["player_slot"] < 128 else "DIRE"
    if (side == "RADIANT" and match["radiant_win"]) or (side == "DIRE" and not match["radiant_win"]):
        return True
    return False


def matchHasMeteorHammer(matchData):
    players = matchData["players"]
    for player in players:
        if player["account_id"] in defaults.ACCOUNT_IDS and (player["purchase"] and "meteor_hammer" in player["purchase"]):
        # if player["account_id"] in defaults.ACCOUNT_IDS and "meteor_hammer" in player["purchase"]:
            return True
    return False
