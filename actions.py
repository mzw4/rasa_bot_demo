# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import sygic
from rasa_sdk.events import SlotSet


class ActionRecommendPointOfInterest(Action):

    def name(self) -> Text:
        return "action_recommend_poi"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        city = tracker.get_slot('city')
        print(city)

        place = sygic.get_random_place_of_interest(query=city)

        return [SlotSet("place", place or [])]