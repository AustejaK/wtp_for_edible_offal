import random

from otree.api import *


doc = """
The impact of environmental and social sustainability recalling visual stimuli on consumer willingness to pay, disgust and neophobia for edible animal by-products.  
Software created by: Austėja Kažemekaitytė (a.kazemekaityte@unitn.it) 
Part of EU Horizon 2020 project COMFOCUS 
Joint work with Davide Gallo, Madina Narysheva, Roberta Raffaelli, Simone Cerroni, Giuseppe Nocella
"""


class C(BaseConstants):
    NAME_IN_URL = 'comfocus_madina'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    eda_time = 20 # 20s before eda measurements
    picture_time = 15 # 15s before treatment pictures


def creating_session(subsession):
    # Treatments: 1 = Baseline, 2 = Sustainability, 3 = Tradition
    if subsession.round_number == 1:
        questions = [
            {'form_field': 'PSM1', 'image': 'PSM1.png'},
            {'form_field': 'PSM2', 'image': 'PSM2.png'},
            {'form_field': 'PSM3', 'image': 'PSM3.png'},
            {'form_field': 'PSM4', 'image': 'PSM4.png'},
            {'form_field': 'PSM5', 'image': 'PSM5.png'},
            {'form_field': 'PSM6', 'image': 'PSM6.png'},
            {'form_field': 'PSM7', 'image': 'PSM7.png'},
            {'form_field': 'PSM8', 'image': 'PSM8.png'},
        ]
        for p in subsession.get_players():
            treatments = random.randint(1, 3)
            p.treatment = treatments
            shuffled_questions = questions[:]
            random.shuffle(shuffled_questions)
            p.participant.offal_fields = shuffled_questions



class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    treatment = models.IntegerField()

    consent = models.BooleanField(choices=[[1, "Acconsento a partecipare a questo studio"]], widget=widgets.RadioSelect,
                                  label="")

    trial = models.CurrencyField()
    rabbia_trial = models.IntegerField(
        label="Rabbia", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    interesse_trial = models.IntegerField(
        label="Interesse", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    odio_trial = models.IntegerField(
        label="Odio", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    divertimento_trial = models.IntegerField(
        label="Divertimento", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    disprezzo_trial = models.IntegerField(
        label="Disprezzo", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    orgoglio_trial = models.IntegerField(
        label="Orgoglio", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    disgusto_trial = models.IntegerField(
        label="Disgusto", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    gioia_trial = models.IntegerField(
        label="Gioia", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    paura_trial = models.IntegerField(
        label="Paura", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    piacere_trial = models.IntegerField(
        label="Piacere", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    disappunto_trial = models.IntegerField(
        label="Disappunto", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    soddisfazione_trial = models.IntegerField(
        label="Soddisfazione", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    vergogna_trial = models.IntegerField(
        label="Vergogna", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    amore_trial = models.IntegerField(
        label="Amore", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    rimpianto_trial = models.IntegerField(
        label="Rimpianto", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    ammirazione_trial = models.IntegerField(
        label="Ammirazione", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    colpevolezza_trial = models.IntegerField(
        label="Colpevolezza", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    sollievo_trial = models.IntegerField(
        label="Sollievo", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    tristezza_trial = models.IntegerField(
        label="Tristezza", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    compassione_trial = models.IntegerField(
        label="Compassione", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    nessuna_trial = models.BooleanField(blank=True)
    altro_trial = models.BooleanField(blank=True)

    rabbia_ch1 = models.IntegerField(
        label="Rabbia", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    interesse_ch1 = models.IntegerField(
        label="Interesse", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    odio_ch1 = models.IntegerField(
        label="Odio", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    divertimento_ch1 = models.IntegerField(
        label="Divertimento", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    disprezzo_ch1 = models.IntegerField(
        label="Disprezzo", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    orgoglio_ch1 = models.IntegerField(
        label="Orgoglio", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    disgusto_ch1 = models.IntegerField(
        label="Disgusto", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    gioia_ch1 = models.IntegerField(
        label="Gioia", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    paura_ch1 = models.IntegerField(
        label="Paura", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    piacere_ch1 = models.IntegerField(
        label="Piacere", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    disappunto_ch1 = models.IntegerField(
        label="Disappunto", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    soddisfazione_ch1 = models.IntegerField(
        label="Soddisfazione", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    vergogna_ch1 = models.IntegerField(
        label="Vergogna", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    amore_ch1 = models.IntegerField(
        label="Amore", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    rimpianto_ch1 = models.IntegerField(
        label="Rimpianto", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    ammirazione_ch1 = models.IntegerField(
        label="Ammirazione", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    colpevolezza_ch1 = models.IntegerField(
        label="Colpevolezza", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    sollievo_ch1 = models.IntegerField(
        label="Sollievo", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    tristezza_ch1 = models.IntegerField(
        label="Tristezza", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    compassione_ch1 = models.IntegerField(
        label="Compassione", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    nessuna_ch1 = models.BooleanField(blank=True)
    altro_ch1 = models.BooleanField(blank=True)

    rabbia_ch2 = models.IntegerField(
        label="Rabbia", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    interesse_ch2 = models.IntegerField(
        label="Interesse", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    odio_ch2 = models.IntegerField(
        label="Odio", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    divertimento_ch2 = models.IntegerField(
        label="Divertimento", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    disprezzo_ch2 = models.IntegerField(
        label="Disprezzo", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    orgoglio_ch2 = models.IntegerField(
        label="Orgoglio", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    disgusto_ch2 = models.IntegerField(
        label="Disgusto", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    gioia_ch2 = models.IntegerField(
        label="Gioia", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    paura_ch2 = models.IntegerField(
        label="Paura", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    piacere_ch2 = models.IntegerField(
        label="Piacere", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    disappunto_ch2 = models.IntegerField(
        label="Disappunto", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    soddisfazione_ch2 = models.IntegerField(
        label="Soddisfazione", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    vergogna_ch2 = models.IntegerField(
        label="Vergogna", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    amore_ch2 = models.IntegerField(
        label="Amore", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    rimpianto_ch2 = models.IntegerField(
        label="Rimpianto", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    ammirazione_ch2 = models.IntegerField(
        label="Ammirazione", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    colpevolezza_ch2 = models.IntegerField(
        label="Colpevolezza", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    sollievo_ch2 = models.IntegerField(
        label="Sollievo", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    tristezza_ch2 = models.IntegerField(
        label="Tristezza", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    compassione_ch2 = models.IntegerField(
        label="Compassione", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    nessuna_ch2 = models.BooleanField(blank=True)
    altro_ch2 = models.BooleanField(blank=True)

    rabbia_ch3 = models.IntegerField(
        label="Rabbia", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    interesse_ch3 = models.IntegerField(
        label="Interesse", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    odio_ch3 = models.IntegerField(
        label="Odio", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    divertimento_ch3 = models.IntegerField(
        label="Divertimento", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    disprezzo_ch3 = models.IntegerField(
        label="Disprezzo", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    orgoglio_ch3 = models.IntegerField(
        label="Orgoglio", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    disgusto_ch3 = models.IntegerField(
        label="Disgusto", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    gioia_ch3 = models.IntegerField(
        label="Gioia", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    paura_ch3 = models.IntegerField(
        label="Paura", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    piacere_ch3 = models.IntegerField(
        label="Piacere", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    disappunto_ch3 = models.IntegerField(
        label="Disappunto", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    soddisfazione_ch3 = models.IntegerField(
        label="Soddisfazione", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    vergogna_ch3 = models.IntegerField(
        label="Vergogna", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    amore_ch3 = models.IntegerField(
        label="Amore", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    rimpianto_ch3 = models.IntegerField(
        label="Rimpianto", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    ammirazione_ch3 = models.IntegerField(
        label="Ammirazione", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    colpevolezza_ch3 = models.IntegerField(
        label="Colpevolezza", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    sollievo_ch3 = models.IntegerField(
        label="Sollievo", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    tristezza_ch3 = models.IntegerField(
        label="Tristezza", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    compassione_ch3 = models.IntegerField(
        label="Compassione", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    nessuna_ch3 = models.BooleanField(blank=True)
    altro_ch3 = models.BooleanField(blank=True)

    rabbia_ch4 = models.IntegerField(
        label="Rabbia", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    interesse_ch4 = models.IntegerField(
        label="Interesse", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    odio_ch4 = models.IntegerField(
        label="Odio", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    divertimento_ch4 = models.IntegerField(
        label="Divertimento", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    disprezzo_ch4 = models.IntegerField(
        label="Disprezzo", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    orgoglio_ch4 = models.IntegerField(
        label="Orgoglio", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    disgusto_ch4 = models.IntegerField(
        label="Disgusto", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    gioia_ch4 = models.IntegerField(
        label="Gioia", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    paura_ch4 = models.IntegerField(
        label="Paura", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    piacere_ch4 = models.IntegerField(
        label="Piacere", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    disappunto_ch4 = models.IntegerField(
        label="Disappunto", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    soddisfazione_ch4 = models.IntegerField(
        label="Soddisfazione", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    vergogna_ch4 = models.IntegerField(
        label="Vergogna", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    amore_ch4 = models.IntegerField(
        label="Amore", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    rimpianto_ch4 = models.IntegerField(
        label="Rimpianto", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    ammirazione_ch4 = models.IntegerField(
        label="Ammirazione", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    colpevolezza_ch4 = models.IntegerField(
        label="Colpevolezza", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    sollievo_ch4 = models.IntegerField(
        label="Sollievo", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    tristezza_ch4 = models.IntegerField(
        label="Tristezza", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    compassione_ch4 = models.IntegerField(
        label="Compassione", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    nessuna_ch4 = models.BooleanField(blank=True)
    altro_ch4 = models.BooleanField(blank=True)

    rabbia_ch5 = models.IntegerField(
        label="Rabbia", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    interesse_ch5 = models.IntegerField(
        label="Interesse", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    odio_ch5 = models.IntegerField(
        label="Odio", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    divertimento_ch5 = models.IntegerField(
        label="Divertimento", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    disprezzo_ch5 = models.IntegerField(
        label="Disprezzo", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    orgoglio_ch5 = models.IntegerField(
        label="Orgoglio", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    disgusto_ch5 = models.IntegerField(
        label="Disgusto", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    gioia_ch5 = models.IntegerField(
        label="Gioia", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    paura_ch5 = models.IntegerField(
        label="Paura", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    piacere_ch5 = models.IntegerField(
        label="Piacere", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    disappunto_ch5 = models.IntegerField(
        label="Disappunto", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    soddisfazione_ch5 = models.IntegerField(
        label="Soddisfazione", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    vergogna_ch5 = models.IntegerField(
        label="Vergogna", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    amore_ch5 = models.IntegerField(
        label="Amore", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    rimpianto_ch5 = models.IntegerField(
        label="Rimpianto", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    ammirazione_ch5 = models.IntegerField(
        label="Ammirazione", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    colpevolezza_ch5 = models.IntegerField(
        label="Colpevolezza", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    sollievo_ch5 = models.IntegerField(
        label="Sollievo", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    tristezza_ch5 = models.IntegerField(
        label="Tristezza", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    compassione_ch5 = models.IntegerField(
        label="Compassione", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    nessuna_ch5 = models.BooleanField(blank=True)
    altro_ch5 = models.BooleanField(blank=True)

    rabbia_ch6 = models.IntegerField(
        label="Rabbia", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    interesse_ch6 = models.IntegerField(
        label="Interesse", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    odio_ch6 = models.IntegerField(
        label="Odio", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    divertimento_ch6 = models.IntegerField(
        label="Divertimento", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    disprezzo_ch6 = models.IntegerField(
        label="Disprezzo", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    orgoglio_ch6 = models.IntegerField(
        label="Orgoglio", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    disgusto_ch6 = models.IntegerField(
        label="Disgusto", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    gioia_ch6 = models.IntegerField(
        label="Gioia", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    paura_ch6 = models.IntegerField(
        label="Paura", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    piacere_ch6 = models.IntegerField(
        label="Piacere", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    disappunto_ch6 = models.IntegerField(
        label="Disappunto", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    soddisfazione_ch6 = models.IntegerField(
        label="Soddisfazione", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    vergogna_ch6 = models.IntegerField(
        label="Vergogna", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    amore_ch6 = models.IntegerField(
        label="Amore", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    rimpianto_ch6 = models.IntegerField(
        label="Rimpianto", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    ammirazione_ch6 = models.IntegerField(
        label="Ammirazione", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    colpevolezza_ch6 = models.IntegerField(
        label="Colpevolezza", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    sollievo_ch6 = models.IntegerField(
        label="Sollievo", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    tristezza_ch6 = models.IntegerField(
        label="Tristezza", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    compassione_ch6 = models.IntegerField(
        label="Compassione", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    nessuna_ch6 = models.BooleanField(blank=True)
    altro_ch6 = models.BooleanField(blank=True)

    rabbia_ch7 = models.IntegerField(
        label="Rabbia", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    interesse_ch7 = models.IntegerField(
        label="Interesse", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    odio_ch7 = models.IntegerField(
        label="Odio", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    divertimento_ch7 = models.IntegerField(
        label="Divertimento", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    disprezzo_ch7 = models.IntegerField(
        label="Disprezzo", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    orgoglio_ch7 = models.IntegerField(
        label="Orgoglio", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    disgusto_ch7 = models.IntegerField(
        label="Disgusto", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    gioia_ch7 = models.IntegerField(
        label="Gioia", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    paura_ch7 = models.IntegerField(
        label="Paura", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    piacere_ch7 = models.IntegerField(
        label="Piacere", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    disappunto_ch7 = models.IntegerField(
        label="Disappunto", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    soddisfazione_ch7 = models.IntegerField(
        label="Soddisfazione", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    vergogna_ch7 = models.IntegerField(
        label="Vergogna", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    amore_ch7 = models.IntegerField(
        label="Amore", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    rimpianto_ch7 = models.IntegerField(
        label="Rimpianto", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    ammirazione_ch7 = models.IntegerField(
        label="Ammirazione", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    colpevolezza_ch7 = models.IntegerField(
        label="Colpevolezza", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    sollievo_ch7 = models.IntegerField(
        label="Sollievo", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    tristezza_ch7 = models.IntegerField(
        label="Tristezza", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    compassione_ch7 = models.IntegerField(
        label="Compassione", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    nessuna_ch7 = models.BooleanField(blank=True)
    altro_ch7 = models.BooleanField(blank=True)

    rabbia_ch8 = models.IntegerField(
        label="Rabbia", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    interesse_ch8 = models.IntegerField(
        label="Interesse", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    odio_ch8 = models.IntegerField(
        label="Odio", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    divertimento_ch8 = models.IntegerField(
        label="Divertimento", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    disprezzo_ch8 = models.IntegerField(
        label="Disprezzo", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    orgoglio_ch8 = models.IntegerField(
        label="Orgoglio", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    disgusto_ch8 = models.IntegerField(
        label="Disgusto", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    gioia_ch8 = models.IntegerField(
        label="Gioia", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    paura_ch8 = models.IntegerField(
        label="Paura", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    piacere_ch8 = models.IntegerField(
        label="Piacere", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    disappunto_ch8 = models.IntegerField(
        label="Disappunto", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    soddisfazione_ch8 = models.IntegerField(
        label="Soddisfazione", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    vergogna_ch8 = models.IntegerField(
        label="Vergogna", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    amore_ch8 = models.IntegerField(
        label="Amore", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    rimpianto_ch8 = models.IntegerField(
        label="Rimpianto", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    ammirazione_ch8 = models.IntegerField(
        label="Ammirazione", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    colpevolezza_ch8 = models.IntegerField(
        label="Colpevolezza", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    sollievo_ch8 = models.IntegerField(
        label="Sollievo", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    tristezza_ch8 = models.IntegerField(
        label="Tristezza", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    compassione_ch8 = models.IntegerField(
        label="Compassione", choices=range(1, 7), widget=widgets.RadioSelectHorizontal, blank=True
    )
    nessuna_ch8 = models.BooleanField(blank=True)
    altro_ch8 = models.BooleanField(blank=True)

    PSM1 = models.CurrencyField(min=0)
    PSM2 = models.CurrencyField(min=0)
    PSM3 = models.CurrencyField(min=0)
    PSM4 = models.CurrencyField(min=0)
    PSM5 = models.CurrencyField(min=0)
    PSM6 = models.CurrencyField(min=0)
    PSM7 = models.CurrencyField(min=0)
    PSM8 = models.CurrencyField(min=0)

    page_1 = models.StringField()
    page_2 = models.StringField()
    page_ch1 = models.StringField()
    page_ch2 = models.StringField()
    page_ch3 = models.StringField()
    page_ch4 = models.StringField()
    page_ch5 = models.StringField()
    page_ch6 = models.StringField()
    page_ch7 = models.StringField()
    page_ch8 = models.StringField()
    page_ch8_end = models.StringField()

    age = models.IntegerField(
        label="1. Indica la tua età in anni (compiuti)."
    )
    gender = models.IntegerField(
        choices=[
            [1, 'maschio'],
            [2, 'femmina'],
            [3, 'preferisco non rispondere']
        ],
        label="2.Indica il tuo genere",
        widget=widgets.RadioSelect
    )
    education = models.IntegerField(
        choices=[
            [1, 'scuola elementare'],
            [2, 'scuola media'],
            [3, 'scuola superiore'],
            [4, 'laurea'],
            [5, 'master'],
            [6, 'dottorato'],
            [7, 'laurea specialistica']
        ],
        label="3. Qual è il titolo di studio più alto che hai conseguito?",
        widget=widgets.RadioSelect
    )
    nationality = models.StringField(
        label="4. Indica la tua nazionalità."
    )
    income = models.IntegerField(
        choices=[
            [1, 'Da 0 a 9.999 euro'],
            [2, 'Da 10.000 a 19.999 euro'],
            [3, 'Da 20.000 a 29.999 euro'],
            [4, 'Da 30.000 a 39.999 euro'],
            [5, 'Da 40.000 euro a 49.999 euro'],
            [6, 'Da 50.000 euro a 59.999 euro'],
            [7, 'Da 60.000 euro a 69.999 euro'],
            [8, 'Da 70.000 euro a 79.999 euro'],
            [9, 'Da 80.000 euro e oltre']
        ],
        label="5. Indica il reddito annuo del tuo nucleo familiare per il 2023:",
        widget=widgets.RadioSelect
    )

    hunger = models.IntegerField(
        label="6. Indica, su una scala da 1 a 9, il tuo stato di fame all'inizio della sessione. (1 = per niente affamato; 9 = estremamente affamato).",
        choices=[
            [1, '1 = per niente affamato'],
            [2, '2'],
            [3, '3'],
            [4, '4'],
            [5, '5'],
            [6, '6'],
            [7, '7'],
            [8, '8'],
            [9, '9 = estremamente affamato']
        ],
        widget=widgets.RadioSelectHorizontal
    )
    dietary_style = models.IntegerField(
        choices=[
            [1, 'Onnivoro (non esclude alcun gruppo alimentare)'],
            [2,
             'Semi-vegetariano / flexitariano (dieta prevalentemente vegetariana, ma che occasionalmente include carne, latticini, uova, pollame o pesce)'],
            [3,
             'Vegetariano (niente carne, pesce o frutti di mare, ma altri alimenti di origine animale come latticini o uova)'],
            [4, 'Latto-vegetariano (niente carne, pesce o uova, ma include prodotti caseari come latte o formaggio)'],
            [5,
             'Latto-ovo-vegetariano (niente carne, pesce o uova, ma include prodotti caseari come latte o formaggio)'],
            [6, 'Ovo-vegetariano (senza carne e pesce, ma con prodotti a base di latte come latte e formaggio)'],
            [7, 'Vegano (non consuma alimenti di origine animale)']
        ],
        label="7. Quali delle seguenti categorie descrivono meglio il tuo attuale stile alimentare?",
        widget=widgets.RadioSelect
    )
    meat_diet = models.IntegerField(
        label="8. Indica il numero di volte in cui mangi carne in una settimana.",
        min=0
    )
    offal_diet = models.IntegerField(
        label="9. Indica il numero di volte in cui mangi prodotti secondari di macellazione (es. lingua, cuore, fegato, zampe, stomaco, intestini, cervello, etc.) in un anno.",
        min=0
    )
    offal_family_freq = models.IntegerField(
        label="10. Indica, su una scala da 1 a 9, quanto è frequente il consumo di prodotti secondari di macellazione (es. lingua, cuore, fegato, zampe, stomaco, intestini, cervello, etc.) nella tua famiglia in un anno. (1 = per niente comune; 9 = estremamente comune).",
        choices=[
            [1, '1 = per niente comune'],
            [2, '2'],
            [3, '3'],
            [4, '4'],
            [5, '5'],
            [6, '6'],
            [7, '7'],
            [8, '8'],
            [9, '9 = estremamente comune']
        ],
        widget=widgets.RadioSelectHorizontal
    )
    offal_society_freq = models.IntegerField(
        label="11. Indica, su una scala da 1 a 9, quanto secondo te è comune mangiare prodotti secondari di macellazione (es. lingua, cuore, fegato, zampe, stomaco, intestini, cervello, etc.) in un anno per una persona comune. (1 = per niente comune; 9 = estremamente comune).",
        choices=[
            [1, 'per niente comune'],
            [2, '2'],
            [3, '3'],
            [4, '4'],
            [5, '5'],
            [6, '6'],
            [7, '7'],
            [8, '8'],
            [9, 'estremamente comune']
        ],
        widget=widgets.RadioSelectHorizontal
    )
    offal_health_awareness = models.IntegerField(
        label="12. Indica, su una scala da 1 a 9, se secondo te i prodotti secondari di macellazione (es. lingua, cuore, fegato, zampe, stomaco, intestini, cervello, etc.) hanno delle proprietà nutrizionali positive maggiori rispetto ai tagli tradizionali di carne. (1 = per nulla d’accordo; 9 = estremamente d’accordo).",
        choices=[
            [1, 'per nulla d’accordo'],
            [2, '2'],
            [3, '3'],
            [4, '4'],
            [5, '5'],
            [6, '6'],
            [7, '7'],
            [8, '8'],
            [9, 'estremamente d’accordo']
        ],
        widget=widgets.RadioSelectHorizontal
    )
    offal_dish_familiarity = models.IntegerField(
        label="13. Indica, su una scala da 1 a 9, quanto conosci i piatti e le ricette a base di prodotti secondari di macellazione. (1 = per nulla familiare; 9 = estremamente familiare).",
        choices=[
            [1, 'per nulla familiare'],
            [2, '2'],
            [3, '3'],
            [4, '4'],
            [5, '5'],
            [6, '6'],
            [7, '7'],
            [8, '8'],
            [9, 'estremamente familiare']
        ],
        widget=widgets.RadioSelectHorizontal
    )

    general_disgust_1 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=range(1, 10))
    general_disgust_2 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=range(1, 10))
    general_disgust_3 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=range(1, 10))
    general_disgust_4 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=range(1, 10))
    general_disgust_5 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=range(1, 10))
    general_disgust_6 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=range(1, 10))
    general_disgust_7 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=range(1, 10))
    general_disgust_8 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=range(1, 10))

    food_disgust_sensitivity_1 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=range(1, 10))
    food_disgust_sensitivity_2 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=range(1, 10))
    food_disgust_sensitivity_3 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=range(1, 10))
    food_disgust_sensitivity_4 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=range(1, 10))
    food_disgust_sensitivity_5 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=range(1, 10))

    nep_scale_1 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=range(1, 10))
    nep_scale_2 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=range(1, 10))
    nep_scale_3 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=range(1, 10))
    nep_scale_4 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=range(1, 10))
    nep_scale_5 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=range(1, 10))
    nep_scale_6 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=range(1, 10))
    nep_scale_7 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=range(1, 10))
    nep_scale_8 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=range(1, 10))
    nep_scale_9 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=range(1, 10))
    nep_scale_10 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=range(1, 10))
    nep_scale_11 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=range(1, 10))
    nep_scale_12 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=range(1, 10))
    nep_scale_13 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=range(1, 10))
    nep_scale_14 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=range(1, 10))
    nep_scale_15 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=range(1, 10))

    animal_welfare = models.BooleanField(widget=widgets.RadioSelect, choices=[[1, 'Si'], [2, 'No']])

    fns_1 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=range(1, 10))
    fns_2 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=range(1, 10))
    fns_3 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=range(1, 10))
    fns_4 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=range(1, 10))
    fns_5 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=range(1, 10))
    fns_6 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=range(1, 10))
    fns_7 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=range(1, 10))
    fns_8 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=range(1, 10))
    fns_9 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=range(1, 10))
    fns_10 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=range(1, 10))



# PAGES
class Consent(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

    form_model = 'player'
    form_fields = ['consent']

class Blank_no_time(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1



class EDA_calibration(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1


class EDA_calibration_2(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_1 = str(time.time_ns())

class EDA_calibration_3(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1
    timeout_seconds = 60*4

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_2 = str(time.time_ns())

class Instructions_1(Page):
    pass


class Instructions_2(Page):
    @staticmethod
    def vars_for_template(player: Player):
        rounds = len(player.participant.offal_fields)
        print(player.participant.offal_fields )
        return dict(rounds=rounds)


class Instructions_3(Page):
    @staticmethod
    def vars_for_template(player: Player):
        rounds = len(player.participant.offal_fields)
        return dict(rounds=rounds)


class Instructions_4(Page):
    pass


class Trial_1(Page):
    pass


class Trial_1_blank(Page):
    timeout_seconds = C.eda_time


class Trial_2(Page):
    form_model = 'player'
    form_fields = ['trial', "rabbia_trial",
                            "interesse_trial",
                            "odio_trial",
                            "divertimento_trial",
                            "disprezzo_trial",
                            "orgoglio_trial",
                            "disgusto_trial",
                            "gioia_trial",
                            "paura_trial",
                            "piacere_trial",
                            "disappunto_trial",
                            "soddisfazione_trial",
                            "vergogna_trial",
                            "amore_trial",
                            "rimpianto_trial",
                            "ammirazione_trial",
                            "colpevolezza_trial",
                            "sollievo_trial",
                            "tristezza_trial",
                            "compassione_trial",
                            "nessuna_trial",
                            "altro_trial"]

    @staticmethod
    def vars_for_template(player: Player):
        image = 'comfocus_madina/trial.png'
        return dict(image=image)

    @staticmethod
    def error_message(player, values):
        remaining_fields = ['rabbia_trial', 'interesse_trial', 'odio_trial', 'divertimento_trial',
                            'disprezzo_trial', 'orgoglio_trial', 'disgusto_trial', 'gioia_trial', 'paura_trial',
                            'piacere_trial', 'disappunto_trial', 'soddisfazione_trial', 'vergogna_trial', 'amore_trial',
                            'rimpianto_trial', 'ammirazione_trial', 'colpevolezza_trial', 'sollievo_trial',
                            'tristezza_trial', 'compassione_trial', 'nessuna_trial', 'altro_trial']

        if not any(values[field] for field in remaining_fields):
            return 'Si prega di compilare almeno uno dei campi relativi alle emozioni.'


class Trial_2_blank(Page):
    timeout_seconds = C.eda_time


class Choice_start_1(Page):
    pass

class Choice_start_2(Page):
    pass

class Choice_start_3(Page):
    @staticmethod
    def vars_for_template(player: Player):
        image = 'comfocus_madina/choice_start_3.png'
        return dict(image=image)

class Choice_start_4(Page):
    @staticmethod
    def vars_for_template(player: Player):
        image = 'comfocus_madina/choice_start_4.png'
        return dict(image=image)

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_ch1 = str(time.time_ns())

class ImageBlank(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.treatment > 1

    timeout_seconds = C.eda_time


class Image(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.treatment > 1

    timeout_seconds = C.picture_time


class Choice_start_blank(Page):
    timeout_seconds = C.eda_time


class Choice_1(Page):
    form_model = 'player'

    def get_form_fields(player: Player):
        question = player.participant.vars['offal_fields'][0]
        choice_field = [question['form_field']]
        fields_other = ["rabbia_ch1",
                            "interesse_ch1",
                            "odio_ch1",
                            "divertimento_ch1",
                            "disprezzo_ch1",
                            "orgoglio_ch1",
                            "disgusto_ch1",
                            "gioia_ch1",
                            "paura_ch1",
                            "piacere_ch1",
                            "disappunto_ch1",
                            "soddisfazione_ch1",
                            "vergogna_ch1",
                            "amore_ch1",
                            "rimpianto_ch1",
                            "ammirazione_ch1",
                            "colpevolezza_ch1",
                            "sollievo_ch1",
                            "tristezza_ch1",
                            "compassione_ch1",
                            "nessuna_ch1",
                            "altro_ch1"]
        return choice_field + fields_other

    def vars_for_template(player: Player):
        question = player.participant.vars['offal_fields'][0]
        print(question)
        image = f"comfocus_madina/{question['image']}"
        return dict(image=image,
                    form_name=question['form_field'])

    @staticmethod
    def error_message(player, values):
        question = player.participant.vars['offal_fields'][0]
        remaining_fields = ["rabbia_ch1",
                            "interesse_ch1",
                            "odio_ch1",
                            "divertimento_ch1",
                            "disprezzo_ch1",
                            "orgoglio_ch1",
                            "disgusto_ch1",
                            "gioia_ch1",
                            "paura_ch1",
                            "piacere_ch1",
                            "disappunto_ch1",
                            "soddisfazione_ch1",
                            "vergogna_ch1",
                            "amore_ch1",
                            "rimpianto_ch1",
                            "ammirazione_ch1",
                            "colpevolezza_ch1",
                            "sollievo_ch1",
                            "tristezza_ch1",
                            "compassione_ch1",
                            "nessuna_ch1",
                            "altro_ch1"]

        if not any(values[field] for field in remaining_fields):
            return 'Si prega di compilare almeno uno dei campi relativi alle emozioni.'

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_ch2 = str(time.time_ns())

class Choice_1_blank(Page):
    timeout_seconds = C.eda_time

class Choice_2(Page):
    form_model = 'player'

    def get_form_fields(player: Player):
        question = player.participant.vars['offal_fields'][1]
        choice_field = [question['form_field']]
        fields_other = ["rabbia_ch2",
                            "interesse_ch2",
                            "odio_ch2",
                            "divertimento_ch2",
                            "disprezzo_ch2",
                            "orgoglio_ch2",
                            "disgusto_ch2",
                            "gioia_ch2",
                            "paura_ch2",
                            "piacere_ch2",
                            "disappunto_ch2",
                            "soddisfazione_ch2",
                            "vergogna_ch2",
                            "amore_ch2",
                            "rimpianto_ch2",
                            "ammirazione_ch2",
                            "colpevolezza_ch2",
                            "sollievo_ch2",
                            "tristezza_ch2",
                            "compassione_ch2",
                            "nessuna_ch2",
                            "altro_ch2"]
        return choice_field + fields_other

    def vars_for_template(player: Player):
        question = player.participant.vars['offal_fields'][1]
        image = f"comfocus_madina/{question['image']}"
        return dict(image=image,
                    form_name=question['form_field'])

    @staticmethod
    def error_message(player, values):
        question = player.participant.vars['offal_fields'][1]
        remaining_fields = ["rabbia_ch2",
                            "interesse_ch2",
                            "odio_ch2",
                            "divertimento_ch2",
                            "disprezzo_ch2",
                            "orgoglio_ch2",
                            "disgusto_ch2",
                            "gioia_ch2",
                            "paura_ch2",
                            "piacere_ch2",
                            "disappunto_ch2",
                            "soddisfazione_ch2",
                            "vergogna_ch2",
                            "amore_ch2",
                            "rimpianto_ch2",
                            "ammirazione_ch2",
                            "colpevolezza_ch2",
                            "sollievo_ch2",
                            "tristezza_ch2",
                            "compassione_ch2",
                            "nessuna_ch2",
                            "altro_ch2"]

        if not any(values[field] for field in remaining_fields):
            return 'Si prega di compilare almeno uno dei campi relativi alle emozioni.'

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_ch3 = str(time.time_ns())

class Choice_2_blank(Page):
    timeout_seconds = C.eda_time

class Choice_3(Page):
    form_model = 'player'

    def get_form_fields(player: Player):
        question = player.participant.vars['offal_fields'][2]
        choice_field = [question['form_field']]
        fields_other = ["rabbia_ch3",
                            "interesse_ch3",
                            "odio_ch3",
                            "divertimento_ch3",
                            "disprezzo_ch3",
                            "orgoglio_ch3",
                            "disgusto_ch3",
                            "gioia_ch3",
                            "paura_ch3",
                            "piacere_ch3",
                            "disappunto_ch3",
                            "soddisfazione_ch3",
                            "vergogna_ch3",
                            "amore_ch3",
                            "rimpianto_ch3",
                            "ammirazione_ch3",
                            "colpevolezza_ch3",
                            "sollievo_ch3",
                            "tristezza_ch3",
                            "compassione_ch3",
                            "nessuna_ch3",
                            "altro_ch3"]
        return choice_field + fields_other

    def vars_for_template(player: Player):
        question = player.participant.vars['offal_fields'][2]
        image = f"comfocus_madina/{question['image']}"
        return dict(image=image,
                    form_name=question['form_field'])

    @staticmethod
    def error_message(player, values):
        question = player.participant.vars['offal_fields'][2]
        remaining_fields = ["rabbia_ch3",
                            "interesse_ch3",
                            "odio_ch3",
                            "divertimento_ch3",
                            "disprezzo_ch3",
                            "orgoglio_ch3",
                            "disgusto_ch3",
                            "gioia_ch3",
                            "paura_ch3",
                            "piacere_ch3",
                            "disappunto_ch3",
                            "soddisfazione_ch3",
                            "vergogna_ch3",
                            "amore_ch3",
                            "rimpianto_ch3",
                            "ammirazione_ch3",
                            "colpevolezza_ch3",
                            "sollievo_ch3",
                            "tristezza_ch3",
                            "compassione_ch3",
                            "nessuna_ch3",
                            "altro_ch3"]

        if not any(values[field] for field in remaining_fields):
            return 'Si prega di compilare almeno uno dei campi relativi alle emozioni.'

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_ch4 = str(time.time_ns())

class Choice_3_blank(Page):
    timeout_seconds = C.eda_time

class Choice_4(Page):
    form_model = 'player'

    def get_form_fields(player: Player):
        question = player.participant.vars['offal_fields'][3]
        choice_field = [question['form_field']]
        fields_other = ["rabbia_ch4",
                            "interesse_ch4",
                            "odio_ch4",
                            "divertimento_ch4",
                            "disprezzo_ch4",
                            "orgoglio_ch4",
                            "disgusto_ch4",
                            "gioia_ch4",
                            "paura_ch4",
                            "piacere_ch4",
                            "disappunto_ch4",
                            "soddisfazione_ch4",
                            "vergogna_ch4",
                            "amore_ch4",
                            "rimpianto_ch4",
                            "ammirazione_ch4",
                            "colpevolezza_ch4",
                            "sollievo_ch4",
                            "tristezza_ch4",
                            "compassione_ch4",
                            "nessuna_ch4",
                            "altro_ch4"]
        return choice_field + fields_other

    def vars_for_template(player: Player):
        question = player.participant.vars['offal_fields'][3]
        image = f"comfocus_madina/{question['image']}"
        return dict(image=image,
                    form_name=question['form_field'])

    @staticmethod
    def error_message(player, values):
        question = player.participant.vars['offal_fields'][3]

        remaining_fields = ["rabbia_ch4",
                            "interesse_ch4",
                            "odio_ch4",
                            "divertimento_ch4",
                            "disprezzo_ch4",
                            "orgoglio_ch4",
                            "disgusto_ch4",
                            "gioia_ch4",
                            "paura_ch4",
                            "piacere_ch4",
                            "disappunto_ch4",
                            "soddisfazione_ch4",
                            "vergogna_ch4",
                            "amore_ch4",
                            "rimpianto_ch4",
                            "ammirazione_ch4",
                            "colpevolezza_ch4",
                            "sollievo_ch4",
                            "tristezza_ch4",
                            "compassione_ch4",
                            "nessuna_ch4",
                            "altro_ch4"]

        if not any(values[field] for field in remaining_fields):
            return 'Si prega di compilare almeno uno dei campi relativi alle emozioni.'

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_ch5 = str(time.time_ns())

class Choice_4_blank(Page):
    timeout_seconds = C.eda_time

class Choice_5(Page):
    form_model = 'player'

    def get_form_fields(player: Player):
        question = player.participant.vars['offal_fields'][4]
        choice_field = [question['form_field']]
        fields_other = ["rabbia_ch5",
                            "interesse_ch5",
                            "odio_ch5",
                            "divertimento_ch5",
                            "disprezzo_ch5",
                            "orgoglio_ch5",
                            "disgusto_ch5",
                            "gioia_ch5",
                            "paura_ch5",
                            "piacere_ch5",
                            "disappunto_ch5",
                            "soddisfazione_ch5",
                            "vergogna_ch5",
                            "amore_ch5",
                            "rimpianto_ch5",
                            "ammirazione_ch5",
                            "colpevolezza_ch5",
                            "sollievo_ch5",
                            "tristezza_ch5",
                            "compassione_ch5",
                            "nessuna_ch5",
                            "altro_ch5"]
        return choice_field + fields_other

    def vars_for_template(player: Player):
        question = player.participant.vars['offal_fields'][4]
        image = f"comfocus_madina/{question['image']}"
        return dict(image=image,
                    form_name=question['form_field'])

    @staticmethod
    def error_message(player, values):
        question = player.participant.vars['offal_fields'][4]

        remaining_fields = ["rabbia_ch5",
                            "interesse_ch5",
                            "odio_ch5",
                            "divertimento_ch5",
                            "disprezzo_ch5",
                            "orgoglio_ch5",
                            "disgusto_ch5",
                            "gioia_ch5",
                            "paura_ch5",
                            "piacere_ch5",
                            "disappunto_ch5",
                            "soddisfazione_ch5",
                            "vergogna_ch5",
                            "amore_ch5",
                            "rimpianto_ch5",
                            "ammirazione_ch5",
                            "colpevolezza_ch5",
                            "sollievo_ch5",
                            "tristezza_ch5",
                            "compassione_ch5",
                            "nessuna_ch5",
                            "altro_ch5"]

        if not any(values[field] for field in remaining_fields):
            return 'Si prega di compilare almeno uno dei campi relativi alle emozioni.'

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_ch6 = str(time.time_ns())

class Choice_5_blank(Page):
    timeout_seconds = C.eda_time

class Choice_6(Page):
    form_model = 'player'

    def get_form_fields(player: Player):
        question = player.participant.vars['offal_fields'][5]
        choice_field = [question['form_field']]
        fields_other = ["rabbia_ch6",
                            "interesse_ch6",
                            "odio_ch6",
                            "divertimento_ch6",
                            "disprezzo_ch6",
                            "orgoglio_ch6",
                            "disgusto_ch6",
                            "gioia_ch6",
                            "paura_ch6",
                            "piacere_ch6",
                            "disappunto_ch6",
                            "soddisfazione_ch6",
                            "vergogna_ch6",
                            "amore_ch6",
                            "rimpianto_ch6",
                            "ammirazione_ch6",
                            "colpevolezza_ch6",
                            "sollievo_ch6",
                            "tristezza_ch6",
                            "compassione_ch6",
                            "nessuna_ch6",
                            "altro_ch6"]
        return choice_field + fields_other

    def vars_for_template(player: Player):
        question = player.participant.vars['offal_fields'][5]
        image = f"comfocus_madina/{question['image']}"
        return dict(image=image,
                    form_name=question['form_field'])

    @staticmethod
    def error_message(player, values):
        question = player.participant.vars['offal_fields'][5]

        remaining_fields = ["rabbia_ch6",
                            "interesse_ch6",
                            "odio_ch6",
                            "divertimento_ch6",
                            "disprezzo_ch6",
                            "orgoglio_ch6",
                            "disgusto_ch6",
                            "gioia_ch6",
                            "paura_ch6",
                            "piacere_ch6",
                            "disappunto_ch6",
                            "soddisfazione_ch6",
                            "vergogna_ch6",
                            "amore_ch6",
                            "rimpianto_ch6",
                            "ammirazione_ch6",
                            "colpevolezza_ch6",
                            "sollievo_ch6",
                            "tristezza_ch6",
                            "compassione_ch6",
                            "nessuna_ch6",
                            "altro_ch6"]

        if not any(values[field] for field in remaining_fields):
            return 'Si prega di compilare almeno uno dei campi relativi alle emozioni.'

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_ch7 = str(time.time_ns())

class Choice_6_blank(Page):
    timeout_seconds = C.eda_time

class Choice_7(Page):
    form_model = 'player'

    def get_form_fields(player: Player):
        question = player.participant.vars['offal_fields'][6]
        choice_field = [question['form_field']]
        fields_other = ["rabbia_ch7",
                            "interesse_ch7",
                            "odio_ch7",
                            "divertimento_ch7",
                            "disprezzo_ch7",
                            "orgoglio_ch7",
                            "disgusto_ch7",
                            "gioia_ch7",
                            "paura_ch7",
                            "piacere_ch7",
                            "disappunto_ch7",
                            "soddisfazione_ch7",
                            "vergogna_ch7",
                            "amore_ch7",
                            "rimpianto_ch7",
                            "ammirazione_ch7",
                            "colpevolezza_ch7",
                            "sollievo_ch7",
                            "tristezza_ch7",
                            "compassione_ch7",
                            "nessuna_ch7",
                            "altro_ch7"]
        return choice_field + fields_other

    def vars_for_template(player: Player):
        question = player.participant.vars['offal_fields'][6]
        image = f"comfocus_madina/{question['image']}"
        return dict(image=image,
                    form_name=question['form_field'])

    @staticmethod
    def error_message(player, values):
        question = player.participant.vars['offal_fields'][6]

        remaining_fields = ["rabbia_ch7",
                            "interesse_ch7",
                            "odio_ch7",
                            "divertimento_ch7",
                            "disprezzo_ch7",
                            "orgoglio_ch7",
                            "disgusto_ch7",
                            "gioia_ch7",
                            "paura_ch7",
                            "piacere_ch7",
                            "disappunto_ch7",
                            "soddisfazione_ch7",
                            "vergogna_ch7",
                            "amore_ch7",
                            "rimpianto_ch7",
                            "ammirazione_ch7",
                            "colpevolezza_ch7",
                            "sollievo_ch7",
                            "tristezza_ch7",
                            "compassione_ch7",
                            "nessuna_ch7",
                            "altro_ch7"]

        if not any(values[field] for field in remaining_fields):
            return 'Si prega di compilare almeno uno dei campi relativi alle emozioni.'

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_ch8 = str(time.time_ns())

class Choice_7_blank(Page):
    timeout_seconds = C.eda_time

class Choice_8(Page):
    form_model = 'player'

    def get_form_fields(player: Player):
        question = player.participant.vars['offal_fields'][7]
        choice_field = [question['form_field']]
        fields_other = ["rabbia_ch8",
                            "interesse_ch8",
                            "odio_ch8",
                            "divertimento_ch8",
                            "disprezzo_ch8",
                            "orgoglio_ch8",
                            "disgusto_ch8",
                            "gioia_ch8",
                            "paura_ch8",
                            "piacere_ch8",
                            "disappunto_ch8",
                            "soddisfazione_ch8",
                            "vergogna_ch8",
                            "amore_ch8",
                            "rimpianto_ch8",
                            "ammirazione_ch8",
                            "colpevolezza_ch8",
                            "sollievo_ch8",
                            "tristezza_ch8",
                            "compassione_ch8",
                            "nessuna_ch8",
                            "altro_ch8"]
        return choice_field + fields_other

    def vars_for_template(player: Player):
        question = player.participant.vars['offal_fields'][7]
        image = f"comfocus_madina/{question['image']}"
        return dict(image=image,
                    form_name=question['form_field'])

    @staticmethod
    def error_message(player, values):
        question = player.participant.vars['offal_fields'][7]

        remaining_fields = ["rabbia_ch8",
                            "interesse_ch8",
                            "odio_ch8",
                            "divertimento_ch8",
                            "disprezzo_ch8",
                            "orgoglio_ch8",
                            "disgusto_ch8",
                            "gioia_ch8",
                            "paura_ch8",
                            "piacere_ch8",
                            "disappunto_ch8",
                            "soddisfazione_ch8",
                            "vergogna_ch8",
                            "amore_ch8",
                            "rimpianto_ch8",
                            "ammirazione_ch8",
                            "colpevolezza_ch8",
                            "sollievo_ch8",
                            "tristezza_ch8",
                            "compassione_ch8",
                            "nessuna_ch8",
                            "altro_ch8"]

        if not any(values[field] for field in remaining_fields):
            return 'Si prega di compilare almeno uno dei campi relativi alle emozioni.'

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_ch8_end = str(time.time_ns())

class Questionnaire_0(Page):
    pass

class Questionnaire_1(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'education', 'nationality', 'income']

class Questionnaire_2(Page):
    form_model = 'player'
    form_fields = ['hunger', 'dietary_style', 'meat_diet', 'offal_diet', 'offal_family_freq',
                   'offal_society_freq', 'offal_health_awareness', 'offal_dish_familiarity']

class Questionnaire_3(Page):
    form_model = 'player'
    form_fields = ['general_disgust_1', 'general_disgust_2', 'general_disgust_3', 'general_disgust_4',
                   'general_disgust_5', 'general_disgust_6', 'general_disgust_7', 'general_disgust_8']

class Questionnaire_4(Page):
    form_model = 'player'
    form_fields = ['food_disgust_sensitivity_1', 'food_disgust_sensitivity_2', 'food_disgust_sensitivity_3',
                   'food_disgust_sensitivity_4', 'food_disgust_sensitivity_5']

class Questionnaire_5(Page):
    form_model = 'player'
    form_fields = ['nep_scale_1', 'nep_scale_2', 'nep_scale_3', 'nep_scale_4', 'nep_scale_5', 'nep_scale_6',
                   'nep_scale_7', 'nep_scale_8', 'nep_scale_9', 'nep_scale_10', 'nep_scale_11', 'nep_scale_12',
                   'nep_scale_13', 'nep_scale_14', 'nep_scale_15']

class Questionnaire_6(Page):
    form_model = 'player'
    form_fields = ['animal_welfare', 'fns_1', 'fns_2', 'fns_3', 'fns_4', 'fns_5', 'fns_6', 'fns_7', 'fns_8',
                   'fns_9', 'fns_10']

class End(Page):
    pass

page_sequence = [
    Consent,
    Blank_no_time,
    EDA_calibration,
    EDA_calibration_2,
    EDA_calibration_3,
    Instructions_1,
    Instructions_2,
    Instructions_3,
    Instructions_4,
    Trial_1,
    Trial_1_blank,
    Trial_2,
    Trial_2_blank,
    Choice_start_1,
    Choice_start_2,
    Choice_start_3,
    Choice_start_4,
    ImageBlank,
    Image,
    Choice_start_blank,
    Choice_1,
    Choice_1_blank,
    Choice_2,
    Choice_2_blank,
    Choice_3,
    Choice_3_blank,
    Choice_4,
    Choice_4_blank,
    Choice_5,
    Choice_5_blank,
    Choice_6,
    Choice_6_blank,
    Choice_7,
    Choice_7_blank,
    Choice_8,
    Questionnaire_0,
    Questionnaire_1,
    Questionnaire_2,
    Questionnaire_3,
    Questionnaire_4,
    Questionnaire_5,
    Questionnaire_6,
    End
    ]
