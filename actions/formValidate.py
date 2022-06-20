from typing import Any, Text, Dict, List
from rasa.core.actions.forms import FormAction
from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa.shared.core.domain import Domain, Union
from rasa.core.actions.action import ActionExecutionRejection, Optional, EndpointConfig


# class ValidateFaultForm(FormValidationAction):
#     def name(self) -> Text:
#         return 'validate_fault_form'
#
#     async def _extract_slot(
#             self,
#             slot_name: Text,
#             dispatcher: "CollectingDispatcher",
#             tracker: "Tracker",
#             domain: "DomainDict",
#     ) -> Dict[Text, Any]:
#         text_of_last_user_message = tracker.latest_message.get("text")
#         sit_outside = "outdoor" in text_of_last_user_message
#
#         return {"outdoor_seating": sit_outside}
#
#     # @staticmethod
#     # def cuisine_db() -> List[Text]:
#     #     """Database of supported cuisines"""
#     #
#     #     return ["caribbean", "chinese", "french"]
#     # def validate_detailStatus(
#     #         self,
#     #         slot_value: Any,
#     #         dispatcher: CollectingDispatcher,
#     #         tracker: Tracker,
#     #         domain: Domain
#     # ):
#     #     """
#     #     Validate cuisine value.
#     #     :param slot_value:
#     #     :param dispatcher:
#     #     :param tracker:
#     #     :param domain:
#     #     :return:
#     #     """
#     #     if slot_value.lower() in self.cuisine_db():
#     #         # validation succeeded, set the value of the "cuisine" slot to value
#     #         return {"cuisine": slot_value}
#     #     else:
#     #         # validation failed, set this slot to None so that the
#     #         # user will be asked for the slot again
#     #         return {"cuisine": None}
#
#     def validate_cuisine(
#             self,
#             slot_value: Any,
#             dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Domain,
#     ) -> Dict[Text, Any]:
#         """Validate cuisine value."""
#
#         if slot_value.lower() in self.cuisine_db():
#             # validation succeeded, set the value of the "cuisine" slot to value
#             return {"cuisine": slot_value}
#         else:
#             # validation failed, set this slot to None so that the
#             # user will be asked for the slot again
#             return {"cuisine": None}
#
#     async def extract_detailStatus(
#             self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
#     ) -> Dict[Text, Any]:
#         text_of_last_user_message = tracker.latest_message.get("text")
#         sit_outside = "outdoor" in text_of_last_user_message
#
#         return {"outdoor_seating": sit_outside}
#
#     async def required_slots(
#         self,
#         domain_slots: List[Text],
#         dispatcher: "CollectingDispatcher",
#         tracker: "Tracker",
#         domain: "DomainDict",
#     ) -> List[Text]:
#         additional_slots = ['outdoor_seating']
#         if tracker.slots.get('outdoor_seating') is True:
#             additional_slots.append("shade_or_sun")
#         return additional_slots + domain_slots
#
#      async def required_slots(
#             self,
#             domain_slots: List[Text],
#             dispatcher: "CollectingDispatcher",
#             tracker: "Tracker",
#             domain: "DomainDict",
#         ) -> List[Text]:
#             updated_slots = domain_slots.copy()
#             if tracker.slots.get("existing_customer") is True:
#                 # If the user is an existing customer,
#                 # do not request the `email_address` slot
#                 updated_slots.remove("email_address")
#
#             return updated_slots