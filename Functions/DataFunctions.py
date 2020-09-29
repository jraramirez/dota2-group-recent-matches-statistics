import sys

sys.path.append("Functions")
sys.path.append("../Functions")
import defaults
import APIFunctions as af


def matchIsParsed(match):
    if not match["version"] == None:
        return True
    return False


def getRecentMatches(parsedOnly):
    allRecentMatches = []
    matchIds = []
    for accountId in defaults.ACCOUNT_IDS:
        playerRecentMatches = af.getPlayerRecentMatches(accountId)
        for recentMatch in playerRecentMatches:
            if not recentMatch["party_size"]:
                continue
            # if not recentMatch["match_id"] in matchIds and recentMatch["party_size"] > 3 and matchIsParsed(recentMatch) :
            if not recentMatch["match_id"] in matchIds and recentMatch["party_size"] > 3 and matchIsParsed(recentMatch):
                allRecentMatches.append(recentMatch)
                matchIds.append(recentMatch["match_id"])
            if not recentMatch["match_id"] in matchIds and recentMatch["party_size"] > 3 and not parsedOnly and not matchIsParsed(recentMatch):
                allRecentMatches.append(recentMatch)
                matchIds.append(recentMatch["match_id"])
    return allRecentMatches


def parseRecentMatches(recentMatches):
    matchesStatus = []
    for match in recentMatches:
        if matchIsParsed(match):
            matchesStatus.append(True)
        else:
            matchesStatus.append(False)
    for match in recentMatches:
        if not matchesStatus[recentMatches.index(match)]:
            af.parseMatch(match["match_id"])
            if matchIsParsed(match):
                matchesStatus[recentMatches.index(match)] = True
            print(str(match["match_id"]) + " - " +  str(matchesStatus[recentMatches.index(match)]))
    print("\nNumber of unparsed: ", matchesStatus.count(False))
    return True


def matchWon(match):
    side = "RADIANT" if match["player_slot"] < 128 else "DIRE"
    if (side == "RADIANT" and match["radiant_win"]) or (side == "DIRE" and not match["radiant_win"]):
        return True
    return False


def matchHasMeteorHammer(matchData):
    if "players" in matchData:
        players = matchData["players"]
        for player in players:
            if player["account_id"] in defaults.ACCOUNT_IDS and (player["purchase"] and "meteor_hammer" in player["purchase"]):
            # if player["account_id"] in defaults.ACCOUNT_IDS and "meteor_hammer" in player["purchase"]:
                return True
    return False


def getTeamSide(match):
    return "RADIANT" if match["player_slot"] < 128 else "DIRE"


def getMatchEnemyHeroes(matchData, side):
    enemyHeroes = []
    if "players" in matchData:
        players = matchData["players"]
        for player in players:
            if side == "DIRE":
                if player["player_slot"] < 128:
                    enemyHeroes.append(player["hero_id"])
            else:
                if player["player_slot"] >= 128:
                    enemyHeroes.append(player["hero_id"])
    return enemyHeroes