import requests
import sys

sys.path.append("Functions")
sys.path.append("../Functions")
import defaults


def chatWinRate(winRate):
    apiCall = "https://discordapp.com/api/webhooks/" + defaults.DISCORD_WEBHOOK_ID + "/" + defaults.DISCORD_WEBHOOK_TOKEN
    content = "\nWin rate ng mga tryhard recently: " + "{:.2f}".format(winRate["win_rate"]) + "%"
    print("Number of matches: " + str(winRate["number_of_matches"]))
    data = {"content": content}
    requests.post(apiCall, data)


def chatmeteorHammerStats(meteorHammerStats):
    apiCall = "https://discordapp.com/api/webhooks/" + defaults.DISCORD_WEBHOOK_ID + "/" + defaults.DISCORD_WEBHOOK_TOKEN
    content = \
        "\nMeme Hammer Statistics (Recent Games)" + \
        "\nNumber of matches: " + str(meteorHammerStats["number_of_matches"]) + \
        "\nTotal meme hammers purchased: " + str(meteorHammerStats["meteor_hammer_total_purchases"]) + \
        "\nWin rate if team purchased at least one meme hammer: " + "{:.2f}".format(meteorHammerStats["meteor_hammer_win_rate"]) + "%" + \
        "\nWin rate if team did not purchase at least one meme hammer: " + "{:.2f}".format(meteorHammerStats["no_meteor_hammer_win_rate"]) + "%" + \
        "\nChance of losing if team purchased at least one meme hammer: " + "{:.2f}".format(meteorHammerStats["meteor_hammer_loss_rate"]) + "%" + \
        "\nChance of losing if team did not purchase at least one meme hammer: " + "{:.2f}".format(meteorHammerStats["no_meteor_hammer_loss_rate"]) + "%"
    content = content + "\n\nTryhard - Meme hammers purchased\n"
    for player in meteorHammerStats["meteor_hammer_purchases_per_player"]:
        content = content + player["name"] + " - " + str(player["meteor_hammer_total_purchases"]) + "\n"

    data = {"content": content}
    requests.post(apiCall, data)


def chatG():
    apiCall = "https://discordapp.com/api/webhooks/" + defaults.DISCORD_WEBHOOK_ID + "/" + defaults.DISCORD_WEBHOOK_TOKEN
    content = "g?"
    data = {"content": content}
    requests.post(apiCall, data)