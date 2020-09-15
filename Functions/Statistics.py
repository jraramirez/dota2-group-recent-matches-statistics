import sys

sys.path.append("Functions")
sys.path.append("../Functions")
import defaults
import APIFunctions as af


def calculateMatchesWinRate(matches):
    wins = 0
    for match in matches:
        if match["game_mode"] == 22 and match["leaver_status"] == 0:
            side = "RADIANT" if match["player_slot"] < 128 else "DIRE"
            if (side == "RADIANT" and match["radiant_win"]) or (side == "DIRE" and not match["radiant_win"]):
                wins = wins + 1
    return {
        "win_rate" : wins/len(matches)*100,
        "number_of_matches" : len(matches),
    }


def calculateMeteorHammerPurchases(matches):
    meteorHammerTotalPurchases = 0
    meteorHammerPlayerPurchases = defaults.ACCOUNTS
    for player in meteorHammerPlayerPurchases:
        player["meteor_hammer_total_purchases"] = 0
    for match in matches:
        matchData = af.getMatchData(match["match_id"])
        players = matchData["players"]
        for player in players:
            if player["account_id"] in defaults.ACCOUNT_IDS and player["purchase"] and "meteor_hammer" in player["purchase"]:
                meteorHammerTotalPurchases = meteorHammerTotalPurchases + player["purchase"]["meteor_hammer"]
                meteorHammerPlayerPurchases[defaults.ACCOUNT_IDS.index(player["account_id"])]["meteor_hammer_total_purchases"] += 1
    return {
        "number_of_matches": len(matches),
        "meteor_hammer_total_purchases" : meteorHammerTotalPurchases,
        "meteor_hammer_average_purchases" : meteorHammerTotalPurchases/len(matches),
        "meteor_hammer_purchases_per_player": meteorHammerPlayerPurchases
    }