import sys
import json

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
    numberOfMatchesPerMeteorHammerCount = [0] * 6
    numberOfWinsPerMeteorHammerCount = [0] * 6
    for player in meteorHammerPlayerPurchases:
        player["meteor_hammer_total_purchases"] = 0
        player["number_of_matches"] = 0
    for match in matches:
        matchData = af.getMatchData(match["match_id"])
        matchWon = df.matchWon(match)
        matchMeteorHammerCount = 0
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
                    matchMeteorHammerCount += 1
                    meteorHammerTotalPurchases += player["purchase"]["meteor_hammer"]
                    meteorHammerPlayerPurchases[defaults.ACCOUNT_IDS.index(player["account_id"])]["meteor_hammer_total_purchases"] += 1
        else:
            numberOfNoMeteorHammerMatches += 1
            if matchWon:
                noMeteorHammerWinCount += 1
            else:
                noMeteorHammerLossCount += 1
        numberOfMatchesPerMeteorHammerCount[matchMeteorHammerCount] += 1
        if matchWon:
            numberOfWinsPerMeteorHammerCount[matchMeteorHammerCount] += 1

    meteorHammerCountWinRates = []
    count = 0
    for w, m in zip(numberOfWinsPerMeteorHammerCount, numberOfMatchesPerMeteorHammerCount):
        meteorHammerCountWinRates.append({
            "count": count,
            "win_rate": "{:.2f}".format(w/m*100) if not m == 0 else "No matches"
            })
        count += 1
    
    memeHammerStats = {
        "number_of_matches": len(matches),
        "meteor_hammer_win_rate": meteorHammerWinCount/numberOfMeteorHammerMatches*100,
        "no_meteor_hammer_win_rate": noMeteorHammerWinCount/numberOfNoMeteorHammerMatches*100,
        "meteor_hammer_loss_rate": meteorHammerLossCount/numberOfMeteorHammerMatches*100,
        "no_meteor_hammer_loss_rate": noMeteorHammerLossCount/numberOfNoMeteorHammerMatches*100,
        "meteor_hammer_total_purchases" : meteorHammerTotalPurchases,
        "meteor_hammer_purchases_per_player": meteorHammerPlayerPurchases,
        "meteor_hammer_count_win_rates": meteorHammerCountWinRates
    }
    return memeHammerStats


def calculateHeroWinRates(recentMatches):
    heroWinRates = []
    heroesJSON = {}
    with open(defaults.DATA_DIR + "heroes.json") as json_file:
        heroesJSON = json.load(json_file)
    maxId = max([int(id) for id in heroesJSON.keys()])
    heroesGameCount = [0] * (maxId + 1)
    heroesWinCount = [0] * (maxId + 1)
    for match in recentMatches:
        side = df.getTeamSide(match)
        won = df.matchWon(match)
        matchData = af.getMatchData(match["match_id"])
        matchHeroes = df.getMatchHeroes(matchData, side)
        for matchHero in matchHeroes:
            heroesGameCount[matchHero] += 1
            if won:
                heroesWinCount[matchHero] += 1
    for i, gameCount in zip(range(len(heroesGameCount)), heroesGameCount):
        if gameCount > 4:
            winRate = heroesWinCount[i]/gameCount*100
            heroWinRates.append({
                "id": i,
                "hero_name": heroesJSON[str(i)]["localized_name"],
                "number_of_matches": gameCount,
                "win_rate": winRate
            })
    heroWinRates = sorted(heroWinRates, key = lambda i: i['win_rate'], reverse=True)
    heroWinRatesTop10 = heroWinRates[:10]
    heroWinRates = sorted(heroWinRates, key = lambda i: i['win_rate'])
    heroWinRatesBottom10 = [h for h in heroWinRates[:10] if not h in heroWinRatesTop10]
    heroWinRates = {
        "hero_win_rate_top_10" : heroWinRatesTop10,
        "hero_win_rate_bottom_10" : heroWinRatesBottom10
    }
    return heroWinRates


def calculateWinRateAgainst(recentMatches):
    winRateAgainstStats = []
    heroesJSON = {}
    with open(defaults.DATA_DIR + "heroes.json") as json_file:
        heroesJSON = json.load(json_file)
    maxId = max([int(id) for id in heroesJSON.keys()])
    enemyHeroesGameCount = [0] * (maxId + 1)
    enemyHeroesWinCount = [0] * (maxId + 1)
    for match in recentMatches:
        side = df.getTeamSide(match)
        won = df.matchWon(match)
        # print(match["match_id"])
        matchData = af.getMatchData(match["match_id"])
        matchEnemyHeroes = df.getMatchEnemyHeroes(matchData, side)
        for matchEnemyHero in matchEnemyHeroes:
            enemyHeroesGameCount[matchEnemyHero] += 1
            if won:
                enemyHeroesWinCount[matchEnemyHero] += 1
    for i, gameCount in zip(range(len(enemyHeroesGameCount)), enemyHeroesGameCount):
        if gameCount > 4:
            winRate = enemyHeroesWinCount[i]/gameCount*100
            winRateAgainstStats.append({
                "id": i,
                "hero_name": heroesJSON[str(i)]["localized_name"],
                "number_of_matches": gameCount,
                "win_rate_against": winRate
            })
    winRateAgainstStats = sorted(winRateAgainstStats, key = lambda i: i['number_of_matches'], reverse=True)
    winRateAgainstStatsTop5 = sorted(winRateAgainstStats, key = lambda i: i['win_rate_against'], reverse=True)[:5]
    winRateAgainstStatsBottom5 = sorted(winRateAgainstStats, key = lambda i: i['win_rate_against'])[:5]
    winRateAgainstStats = {
        "win_rate_against_top_5" : winRateAgainstStatsTop5,
        "win_rate_against_bottom_5" : winRateAgainstStatsBottom5,

    }
    return winRateAgainstStats
