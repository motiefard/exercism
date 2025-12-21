
def response(hey_bob):
    answers = ["Sure.", "Whoa, chill out!", "Calm down, I know what I'm doing!", "Fine. Be that way!", "Whatever." ]
    
    if len(hey_bob.strip()) != 0 :
        is_question = hey_bob.strip()[-1] == '?'
        if is_question : ans = answers[0]
    else: is_question = False

    is_yelling = hey_bob.isupper()
    if is_yelling : ans = answers[1]


    is_yelling_question = is_question & is_yelling
    if is_yelling_question : ans = answers[2]


    is_silence = hey_bob.isspace() or len(hey_bob) == 0
    if is_silence : ans = answers[3]

    is_sth_else = not any([is_question, is_yelling, is_yelling_question, is_silence])
    if is_sth_else : ans = answers[4]

    return ans
