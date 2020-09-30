import requests
import sys

sys.path.append("Functions")
sys.path.append("../Functions")
import defaults


def chatWinRate(winRate):
    uri = "https://discordapp.com/api/webhooks/" + defaults.DISCORD_WEBHOOK_ID + "/" + defaults.DISCORD_WEBHOOK_TOKEN
    content = "\nTeam's win rate (recent matches): " + "{:.1f}".format(winRate["win_rate"]) + "%"
    print("Number of matches: " + str(winRate["number_of_matches"]))
    data = {"content": content}
    requests.post(uri, data)


def chatMeteorHammerStats(meteorHammerStats):
    uri = "https://discordapp.com/api/webhooks/" + defaults.DISCORD_WEBHOOK_ID + "/" + defaults.DISCORD_WEBHOOK_TOKEN
    content = \
        "\n**Meme Hammer Statistics (Recent Matches)**" + \
        "\n**Number of matches:** " + str(meteorHammerStats["number_of_matches"]) + \
        "\n**Total meme hammers purchased:** " + str(meteorHammerStats["meteor_hammer_total_purchases"]) + \
        "\n**Chance of winning if team purchased at least one meme hammer:** " + "{:.1f}".format(meteorHammerStats["meteor_hammer_win_rate"]) + "%" + \
        "\n**Chance of winning if team did not purchase at least one meme hammer:** " + "{:.1f}".format(meteorHammerStats["no_meteor_hammer_win_rate"]) + "%" + \
        "\n**Win rate of team's number of meteor hammer purchases in a match:**\n"
    for meteorHammerCountWinRate in meteorHammerStats["meteor_hammer_count_win_rates"]:
        if meteorHammerCountWinRate["win_rate"] == "No matches":
            content = content + str(meteorHammerCountWinRate["count"]) + " - " + meteorHammerCountWinRate["win_rate"] + "\n"
        else:
            content = content + str(meteorHammerCountWinRate["count"]) + " - " + meteorHammerCountWinRate["win_rate"] + "%\n"

    content = content + "**Breakdown of meme hammers purchased:**\n"
    for player in meteorHammerStats["meteor_hammer_purchases_per_player"]:
        content = content + "<@!"+ player["discord_user_id"] +"> - " + str(player["meteor_hammer_total_purchases"]) + "\n"

    data = {"content": content}
    requests.post(uri, data)


def chatWinRateAgainst(winRateAgainstStats):
    uri = "https://discordapp.com/api/webhooks/" + defaults.DISCORD_WEBHOOK_ID + "/" + defaults.DISCORD_WEBHOOK_TOKEN
    content = \
        "\n**Enemy Heroes Statistics (Recent Matches)**" + \
        "\n**Top 5 enemy heroes wherein the team has low win rates:**\n"
    for enemyHero in winRateAgainstStats["win_rate_against_bottom_5"]:
        content = content + enemyHero["hero_name"] + " - " + "{:.1f}".format(enemyHero["win_rate_against"]) + "% (" + str(enemyHero["number_of_matches"]) + " games)\n"

    content = content + "\n**Top 5 enemy heroes wherein the team has high win rates:**\n"
    for enemyHero in winRateAgainstStats["win_rate_against_top_5"]:
        content = content + enemyHero["hero_name"] + " - " + "{:.1f}".format(enemyHero["win_rate_against"]) + "% (" + str(enemyHero["number_of_matches"]) + " games)\n"

    data = {"content": content}
    requests.post(uri, data)


def chatHeroWinRates(heroWinRates):
    uri = "https://discordapp.com/api/webhooks/" + defaults.DISCORD_WEBHOOK_ID + "/" + defaults.DISCORD_WEBHOOK_TOKEN
    content = \
        "\n**Team Heroes Statistics (Recent Matches)**" + \
        "\n**Team's top 10 successful heroes:**\n"
    for hero in heroWinRates["hero_win_rate_top_10"]:
        content = content + hero["hero_name"] + " - " + "{:.1f}".format(hero["win_rate"]) + "% (" + str(hero["number_of_matches"]) + " games)\n"

    content = content + \
        "\n**Team's top 10 unsuccessful heroes:**\n"
    for hero in heroWinRates["hero_win_rate_bottom_10"]:
        content = content + hero["hero_name"] + " - " + "{:.1f}".format(hero["win_rate"]) + "% (" + str(hero["number_of_matches"]) + " games)\n"

    data = {"content": content}
    requests.post(uri, data)


def chatG():
    uri = "https://discordapp.com/api/webhooks/" + defaults.DISCORD_WEBHOOK_ID + "/" + defaults.DISCORD_WEBHOOK_TOKEN
    content = "g?"
    data = {"content": content}
    requests.post(uri, data)