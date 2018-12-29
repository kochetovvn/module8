import random

times = ["утром", "днём", "вечером", "ночью", "после обеда", "перед сном"]
advices = ["ожидайте", "предостерегайтесь", "будьте открыты для"]
promises = ["гостей из забытого прошлого", "встреч со старыми знакомыми",
            "неожиданного праздника", "приятных перемен"]


def generate_prophecies(total_num=5, num_sentences=3):
    prophecies = []

    for i in range(total_num):
        forecast = ""
        for j in range(num_sentences):
            t = random.choice(times)
            a = random.choice(advices)
            p = random.choice(promises)

            full_sentence = f"{t[0].title()}{t[1:]} {a} {p}."
            if j != num_sentences - 1:
                full_sentence = full_sentence + " "

            forecast = forecast + full_sentence

        prophecies.append(forecast)

    return prophecies

def generate_about():

    param_list = []
    full_sentence = f'<img src="virgo.jpg" height="100" width="100">'
    full_sentence += '<ol><li>Времена дня</li><ul>'
    for t in times:
        full_sentence += f'<li>{t}</li>'
    full_sentence += f'</ul><li>Глаголы</li><ul>'
    for t in advices:
        full_sentence += f'<li>{t}</li>'
    full_sentence += f'</ul><li>Ожидания</li><ul>'
    for t in promises:
        full_sentence += f'<li>{t}</li>'
    full_sentence += f'</ul></ol>'
    param_list.append(full_sentence)

    return param_list
