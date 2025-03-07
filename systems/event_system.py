

import random

class Event_System():
    def __init__(self, game_state, events_data=None):
        self.current_events = [] #list of event ids like bar burned down
        self.game_state = game_state
        self.events_data = events_data#cant make it a Descriptions using tag system, would need an entirely different system lol



    def add_event(self): #things like bertha watching, can pass conditions, etc
        #morgue - please close the doors and cover debbie when ur done...
        #pub - leave darwwer open - have you through my stuf?!?!, also she can come in on you when shes there...
        #backroom - some gibbs minigame
        #alley - fall event and railing?

        #dialogue = gibbs tweaked, mortician zoned out, bertha normal.
        #note : mortician SCARY despite WALKINGSTICK!!


        pass #for now, this is for events passed from dialogue
    def check_events(self):

        pass

    def check_conditions(self):#have to redo this obvi to check all specifics
        #self.current events has event ids that are "current events" to trigger, example: band playing, or introduction to bertha at pub.
        #so this checks conditions for active events
        pass


    def decorate_tags(self, description_tags):
        pass


