import sys

sys.path.append("Functions")
sys.path.append("../Functions")
import defaults
import APIFunctions as af
import DataFunctions as df


def calculateMatchesWinRate(matches):
    wins = 0
    for match in matches:
        if match["game_mode"] == 22 and match["leaver_status"] == 0:
            if df.matchWon(match):
                wins += 1
    return {
        "win_rate" : wins/len(matches)*100,
        "number_of_matches" : len(matches),
    }


def calculateMeteorHammerPurchases(matches):
    meteorHammerTotalPurchases = 0
    meteorHammerPlayerPurchases = defaults.ACCOUNTS
    meteorHammerWinCount = 0
    meteorHammerLossCount = 0
    noMeteorHammerWinCount = 0
    noMeteorHammerLossCount = 0
    numberOfWins = 0
    numberOfMeteorHammerMatches = 0
    numberOfNoMeteorHammerMatches = 0
    for player in meteorHammerPlayerPurchases:
        player["meteor_hammer_total_purchases"] = 0
        player["number_of_matches"] = 0
    for match in matches:
        matchData = af.getMatchData(match["match_id"])
        matchWon = df.matchWon(match)
        if matchWon:
            numberOfWins += 1
        if df.matchHasMeteorHammer(matchData):
            numberOfMeteorHammerMatches += 1
            if matchWon:
                meteorHammerWinCount += 1
            else:
                meteorHammerLossCount += 1
            players = matchData["players"]
            for player in players:
                if player["account_id"] in defaults.ACCOUNT_IDS and "meteor_hammer" in player["purchase"]:
                    meteorHammerTotalPurchases = meteorHammerTotalPurchases + player["purchase"]["meteor_hammer"]
                    meteorHammerPlayerPurchases[defaults.ACCOUNT_IDS.index(player["account_id"])]["meteor_hammer_total_purchases"] += 1
        else:
            numberOfNoMeteorHammerMatches += 1
            if matchWon:
                noMeteorHammerWinCount += 1
            else:
                noMeteorHammerLossCount += 1

    memeHammerStats = {
        "number_of_matches": len(matches),
        "meteor_hammer_win_rate": meteorHammerWinCount/numberOfMeteorHammerMatches*100,
        "no_meteor_hammer_win_rate": noMeteorHammerWinCount/numberOfNoMeteorHammerMatches*100,
        "meteor_hammer_loss_rate": meteorHammerLossCount/numberOfMeteorHammerMatches*100,
        "no_meteor_hammer_loss_rate": noMeteorHammerLossCount/numberOfNoMeteorHammerMatches*100,
        "meteor_hammer_total_purchases" : meteorHammerTotalPurchases,
        "meteor_hammer_purchases_per_player": meteorHammerPlayerPurchases
    }
    return memeHammerStats