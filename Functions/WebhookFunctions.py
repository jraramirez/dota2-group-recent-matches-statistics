import requests
import sys

sys.path.append("Functions")
sys.path.append("../Functions")
import defaults


def chatWinRate(winRate):
    uri = "https://discordapp.com/api/webhooks/" + defaults.DISCORD_WEBHOOK_ID + "/" + defaults.DISCORD_WEBHOOK_TOKEN
    content = "\nTeam's win rate (recent matches): " + "{:.2f}".format(winRate["win_rate"]) + "%"
    print("Number of matches: " + str(winRate["number_of_matches"]))
    data = {"content": content}
    requests.post(uri, data)


def chatMeteorHammerStats(meteorHammerStats):
    uri = "https://discordapp.com/api/webhooks/" + defaults.DISCORD_WEBHOOK_ID + "/" + defaults.DISCORD_WEBHOOK_TOKEN
    content = \
        "\n**Meme Hammer Statistics (Recent Games)**" + \
        "\n**Number of matches:** " + str(meteorHammerStats["number_of_matches"]) + \
        "\n**Total meme hammers purchased:** " + str(meteorHammerStats["meteor_hammer_total_purchases"]) + \
        "\n**Chance of winning if team purchased at least one meme hammer:** " + "{:.2f}".format(meteorHammerStats["meteor_hammer_win_rate"]) + "%" + \
        "\n**Chance of winning if team did not purchase at least one meme hammer:** " + "{:.2f}".format(meteorHammerStats["no_meteor_hammer_win_rate"]) + "%" + \
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


def chatG():
    uri = "https://discordapp.com/api/webhooks/" + defaults.DISCORD_WEBHOOK_ID + "/" + defaults.DISCORD_WEBHOOK_TOKEN
    content = "g?"
    data = {"content": content}
    requests.post(uri, data)