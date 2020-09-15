import requests
import sys

sys.path.append("Functions")
sys.path.append("../Functions")
import defaults

def chatWinRate(winRate):
    apiCall = "https://discordapp.com/api/webhooks/" + defaults.DISCORD_WEBHOOK_ID + "/" + defaults.DISCORD_WEBHOOK_TOKEN
    content = "\nWinrate ng mga tryhard recently: " + "{:.2f}".format(winRate["win_rate"]) + "%"
    print("Number of matches: " + str(winRate["number_of_matches"]))
    data = {"content": content}
    requests.post(apiCall, data)

def chatmeteorHammerStats(meteorHammerStats):
    apiCall = "https://discordapp.com/api/webhooks/" + defaults.DISCORD_WEBHOOK_ID + "/" + defaults.DISCORD_WEBHOOK_TOKEN
    content = \
        "\nMeme Hammer Statistics"\
        "\nDami ng nabiling meme hammer ng mga tryhard recently: " + str(meteorHammerStats["meteor_hammer_total_purchases"]) + \
        "\nDami ng matches: " + str(meteorHammerStats["number_of_matches"])
    content = content + "\nTryhard\tDami\n"
    for player in meteorHammerStats["meteor_hammer_purchases_per_player"]:
        content = content + player["name"] + "\t" + str(player["meteor_hammer_total_purchases"]) + "\n"

    data = {"content": content}
    requests.post(apiCall, data)