from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'CG'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 6
    INITIAL_POT = 5
    POT_INCREMENT = 5


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# PAGES
class Intro(Page):
    pass


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [Intro, ResultsWaitPage, Results]
