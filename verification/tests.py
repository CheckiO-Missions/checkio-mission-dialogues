init_code = """
if not "NewMessenger" in USER_GLOBAL:
    raise NotImplementedError("Where is 'NewMessenger'?")
NewMessenger = USER_GLOBAL['NewMessenger']

if not "Person1" in USER_GLOBAL:
    raise NotImplementedError("Where is 'Person1'?")
Person1 = USER_GLOBAL['Person1']

if not "Person2" in USER_GLOBAL:
    raise NotImplementedError("Where is 'Person2'?")
Person2 = USER_GLOBAL['Person2']
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
        prepare_test(middle_code='''messenger = NewMessenger()
karl = Person1(messenger)
peter = Person2(messenger)
messenger.connect_person(karl)
messenger.connect_person(peter)
karl.send("Hi! How are you?")
peter.send("Hello. Could we speak later about it?")''',
                     test="messenger.show_dialogue()",
                     answer='''Person1 said: How are you?
Person2 said: Hello. Could we speak later about it?''')
    ],
    "2. Second": [
        prepare_test(middle_code='''messenger = NewMessenger()
bob = Person1(messenger)
ann = Person2(messenger)
messenger.connect_person(bob)
messenger.connect_person(ann)
bob.send("Hi, Ann! Is your part of work done?")
ann.send("Hi, Bob. Sorry, I need a few more hours. Could you wait, please?")
bob.send("Ok. But hurry up, please. It's important.")
ann.send("Sure, thanks.")
''',
                     test="messenger.show_dialogue()",
                     answer='''Person1 said: Hi, Ann! Is your part of work done?
Person2 said: Hi, Bob. Sorry, I need a few more hours. Could you wait, please?
Person1 said: Ok. But hurry up, please. It's important.
Person2 said: Sure, thanks.''')
    ],
    "3. Third": [
        prepare_test(middle_code='''messenger = NewMessenger()
me = Person1(messenger)
you = Person2(messenger)
messenger.connect_person(me)
messenger.connect_person(you)
me.send("What a nice day! Do you have some plans?")
you.send("Code. Code. Code. Nothing else matters.")''',
                     test="messenger.show_dialogue()",
                     answer='''Person1 said: What a nice day! Do you have some plans?
Person2 said: Code. Code. Code. Nothing else matters.''')
    ]

}
