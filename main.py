import re
import CSS
import api

print(CSS.bold(CSS.color("=== MENTAL HEALTH ASSISTANT ===", 'magenta')))

print(CSS.color("Hello! Welcome to an AI-based mental health assistance for CS-related individual ;)\nAs a CS person, it is very important to keep your head leveled. I am designed to do that for you!\nPlease, talk to me about anything!", 'yellow'))

depressed_check = False

while not depressed_check:
    cur_inp = input(">> ")

    # check if too depressed to talk to
    depressed_state = re.findall(r'\d+', api.check_depressed_state(cur_inp))[0]
    if depressed_state.isdigit():
        if int(depressed_state) < 2:
            depressed_check = True
            break

    print(CSS.color(api.get_response(cur_inp), 'yellow'))

print(CSS.color("Oh... Ermm, so like this is a bit awks, but I think you are a lil too much of a debbie downer. I think Imma leave you be for now. 0_0", 'blue'))

print(CSS.color("Likee go cool down for a bit pls.", 'blue'))

print(CSS.color("Once you're better tho! We can talk again ;)", 'yellow'))