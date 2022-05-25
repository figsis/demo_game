from otree.api import *


doc = """
Multiplication app 
"""


class C(BaseConstants):
    NAME_IN_URL = 'multiply_app'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    factors = 2


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    number_entered = models.FloatField()
    pass


# PAGES
class MyPage(Page):
    form_model = "player"
    form_fields = ["number_entered"]
    pass



class Results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        result = player.number_entered * C.factors
        return {
            "results": result
        }
    pass


page_sequence = [MyPage, Results]
