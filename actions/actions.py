from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from . import Repo

class ActionAskName(Action):

    def name(self) -> Text:
        return "action_ask_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(response="utter_ask_name")

        return []


class ActionAskEmpCode(Action):

    def name(self) -> Text:
        return "action_ask_empcode"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(response="utter_ask_empcode")

        return []


class ActionAskEmail(Action):

    def name(self) -> Text:
        return "action_ask_email"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(response="utter_ask_email")

        return []


class ActionSaveDetails(Action):

    def name(self) -> Text:
        return "action_save_candidate"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        Repo.insert(tracker.get_slot('PERSON'), tracker.get_slot('emp_code'), tracker.get_slot('email'))

        dispatcher.utter_message(response="utter_display_details")

        return []


class ActionSelectAll(Action):

    def name(self) -> Text:
        return "action_select_all"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        rows = Repo.select()

        dispatcher.utter_message(text=rows)

        return []


class ActionDeleteCandidate(Action):

    def name(self) -> Text:
        return "action_delete_candidate"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        value = tracker.latest_message['entities'][0]['value']

        Repo.delete(value)

        dispatcher.utter_message(text="Deleted successfully")

        return []