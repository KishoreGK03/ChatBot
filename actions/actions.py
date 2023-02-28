# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionAdd(Action):
    def name(self) -> Text:
        return "action_add"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        num1 = tracker.get_slot("num1")
        num2 = tracker.get_slot("num2")
        result = num1 + num2
        dispatcher.utter_message(template="utter_add", num1=num1, num2=num2, result=result)
        return []

class ActionSubtract(Action):
    def name(self) -> Text:
        return "action_subtract"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        num1 = tracker.get_slot("num1")
        num2 = tracker.get_slot("num2")
        result = num1 - num2
        dispatcher.utter_message(template="utter_subtract", num1=num1, num2=num2, result=result)
        return []

class ActionMultiply(Action):
    def name(self) -> Text:
        return "action_multiply"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        num1 = tracker.get_slot("num1")
        num2 = tracker.get_slot("num2")
        result = num1 * num2
        dispatcher.utter_message(template="utter_multiply", num1=num1, num2=num2, result=result)
        return []

class ActionDivide(Action):
    def name(self) -> Text:
        return "action_divide"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        num1 = tracker.get_slot("num1")
        num2 = tracker.get_slot("num2")
        if num2 == 0:
            dispatcher.utter_message("Can't divide by zero, please enter a valid number.")
            return []
        result = num1 / num2
        dispatcher.utter_message(template="utter_divide", num1=num1, num2=num2, result=result)
        return []
