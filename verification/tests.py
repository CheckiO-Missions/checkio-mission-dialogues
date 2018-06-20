init_code = """
if not "Chat" in USER_GLOBAL:
    raise NotImplementedError("Where is 'Chat'?")
Chat = USER_GLOBAL['Chat']

if not "Human" in USER_GLOBAL:
    raise NotImplementedError("Where is 'Human'?")
Human = USER_GLOBAL['Human']

if not "Robot" in USER_GLOBAL:
    raise NotImplementedError("Where is 'Robot'?")
Robot = USER_GLOBAL['Robot']
"""

run_test = """
RET['code_result'] = {}
"""


def prepare_test(test="", answer=None, middle_code="", show_code=None):
    if show_code is None:
        show_code = middle_code + "\n" + test
    if not test:
        return_code = "\nRET['code_result'] = ''"
        answer = ''
    else:
        return_code = run_test.format(test)
    return {"test_code": {"python-3": init_code + middle_code + return_code},
            "show": {"python-3": show_code},
            "answer": answer}


TESTS = {
    "1. First": [
        prepare_test(middle_code='''chat = Chat()
karl = Human('Karl')
bot = Robot('R2D2')
chat.connect_human(karl)
chat.connect_robot(bot)
karl.send("Hi! How are you?")
bot.send("Hello, human. Could we speak later about it?")''',
                     test="chat.show_robot_dialogue()",
                     answer="""Karl said: 101111011111011
R2D2 said: 10110111010111100111101110011101011010011011""")
    ],
    "2. Second": [
        prepare_test(middle_code='''chat = Chat()
bob = Human('Bob')
ann = Robot('Ann-1244c')
chat.connect_human(bob)
chat.connect_robot(ann)
bob.send("Hi, Ann! Is your part of work done?")
ann.send("Hi, Bob. Sorry, I need a few more hours. Could you wait, please?")
bob.send("Ok. But hurry up, please. It's important.")
ann.send("Sure, thanks.")
''',
                     test="chat.show_human_dialogue()",
                     answer='''Bob said: Hi, Ann! Is your part of work done?
Ann-1244c said: Hi, Bob. Sorry, I need a few more hours. Could you wait, please?
Bob said: Ok. But hurry up, please. It's important.
Ann-1244c said: Sure, thanks.''')
    ],
    "3. Third": [
        prepare_test(middle_code='''chat = Chat()
me = Human('Xander')
my_digital_clone = Robot('Model AX-88')
chat.connect_human(me)
chat.connect_robot(my_digital_clone)
me.send("What a nice day! Do you have some plans?")
my_digital_clone.send("Code. Code. Code. Nothing else matters.")''',
                     test="chat.show_robot_dialogue()",
                     answer='''Xander said: 1101101101011011110110011010110101110111
Model AX-88 said: 101011101011101011101101110110110110111''')
    ],
    "4. Fourth": [
        prepare_test(middle_code='''chat = Chat()
ai_developer = Human('Max')
ai = Robot('Deep Thought')
chat.connect_human(ai_developer)
chat.connect_robot(ai)
ai_developer.send("I need the answer to the great question of life, the universe and everything")
ai.send("42")''',
                     test="chat.show_human_dialogue()",
                     answer='''Max said: I need the answer to the great question of life, the universe and everything
Deep Thought said: 42''')
    ]

}
