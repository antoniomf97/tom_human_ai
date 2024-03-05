from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'CRT'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    answer1 = models.FloatField(label="A bat and a ball cost $1.10 in total. The bat costs $1.00 more than the ball. How much does the ball cost?")
    answer2 = models.FloatField(label="If it takes 5 machines 5 minutes to make 5 widgets, how long would it take 100 machines to make 100 widgets?")
    answer3 = models.FloatField(label="In a lake, there is a patch of lily pads. Every day, the patch doubles in size. If it takes 48 days for the patch to cover the entire lake, how long would it take for the patch to cover half of the lake?")


# PAGES ===============================
class Intro(Page):
    pass

class Question1(Page):
    form_model = 'player'
    form_fields = ['answer1'] 

class Question2(Page):
    form_model = 'player'
    form_fields = ['answer2'] 

class Question3(Page):
    form_model = 'player'
    form_fields = ['answer3'] 

class End(Page):
    pass


page_sequence = [Intro, Question1, Question2, Question3, End]
