from typing import Any, Text, Dict, List
# from rasa.shared.core.events import ev.
import rasa
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionDetailSolution(Action):
    def name(self) -> Text:
        return "action_getReason_getSolution"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="action_getReason_getSolution!")

        return []


class ActionReasonSolution(Action):
    def name(self) -> Text:
        return "action_getDetail_getSolution"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="action_getDetail_getSolution?")
        return []

class ActionDetailReason(Action):
    def name(self) -> Text:
        return "action_getDetail_getReason"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="action_getDetail_getReason?")
        return []
