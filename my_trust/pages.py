from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Send(Page):
    
    form_model = 'group'
    form_fields = ['sent_amount']

    def is_displayed(self):
        return self.player.id_in_group == 1


class Sendback(Page):
    
    form_model = 'group'
    form_fields = ['sentback_amount']

    def is_displayed(self):
        return self.player.id_in_group == 2
    
    def vars_for_template(self):
        return dict(
            tripled_amount = self.group.sent_amount * Constants.multiplication_factor
        )

class Results(Page):
    pass

class WaitForP1(WaitPage):
    pass

class ResultsWaitPage(WaitPage):

    after_all_players_arrive = 'set_payoffs'

page_sequence = [
    Send,
    WaitForP1,
    Sendback,
    ResultsWaitPage,
    Results
]
