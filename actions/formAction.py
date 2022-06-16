from typing import Any, Text, Dict, List
from rasa.core.actions.forms import FormAction
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa.shared.core.domain import Domain, Union
from rasa.core.actions.action import ActionExecutionRejection, Optional, EndpointConfig


class RestaurantForm(FormAction):
    """Example of a custom form action"""

    def __init__(form_name: Text, action_endpoint: Optional[EndpointConfig]) -> None:
        pass

    # 定义action的名字
    def name(self) -> Text:
        """
        Unique identifier of the form
        :return:
        """
        return 'fault_form'

    # 实现slots函数
    @staticmethod
    def required_slots(domain: Domain) -> List[Text]:
        """
        A list of required slots that the form has to fill
        :param domain:
        :return:
        """
        # if tracker.get_slot('detailStatus')=='':
        return ['detailStatus', 'detailUnit', 'detailPhenomenon']

    def submit(self):
        """
        Define what the form has to do
        after all required slots are filled
        :return:
        """
        CollectingDispatcher.utter_template('utter_submit', Tracker)
        return []

    def slot_mappings(self):
        # type: () -> Dict[Text: Union[Dict, List[Dict]]]
        """A dictionary to map required slots to
        - an extracted entity
        - intent: value pairs
        - a whole message or a list of them, where a first
                                     match will be picked"""
        # return {"outdoor_seating": [self.from_entity(entity="seating"),
        #                             self.from_intent(intent='affirm',
        #                                              value=True),
        #                             self.from_intent(intent='deny',
        #                                              value=False)]}

    def from_entity(
            self,
            entity: Text,
            intent: Optional[Union[Text, List[Text]]] = None,
            not_intent: Optional[Union[Text, List[Text]]] = None,
            role: Optional[Text] = None,
            group: Optional[Text] = None,
    ) -> Dict[Text, Any]:
        pass

    def get_mappings_for_slot(
            self, slot_to_fill: Text, domain: Domain
    ) -> List[Dict[Text, Any]]:
        pass

    def entity_mapping_is_unique(
            self, slot_mapping: Dict[Text, Any], domain: Domain
    ) -> bool:
        pass

    @staticmethod
    def get_entity_value_for_slot(
            name: Text,
            tracker: "DialogueStateTracker",
            slot_to_be_filled: Text,
            role: Optional[Text] = None,
            group: Optional[Text] = None,
    ) -> Any:
        pass

    def get_slot_to_fill(self, tracker: "DialogueStateTracker") -> Optional[str]:
        pass

    async validate(tracker: "DialogueStateTracker", domain: Domain, output_channel: OutputChannel, nlg: NaturalLanguageGenerator) -> List[Union[SlotSet, Event]]:
        pass


    def validate(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Domain) -> List[dict]:
    """
    Validate extracted requested slot
    else reject the execution of the form action
    :param dispatcher:
    :param tracker:
    :param domain:
    :return:
    """
    # extract other slots that were not requested
    # but set by corresponding entity
    slot_values = self.extract_other_slots(dispatcher, tracker, domain)

    # extract requested slot
    slot_to_fill = tracker.get_slot("")
    if slot_to_fill:
        slot_values.update(self.extract_requested_slot(dispatcher, tracker, domain))
        if not slot_values:
            # reject form action execution
            # if some slot was requested but nothing was extracted
            # it will allow other policies to predict another action
            raise ActionExecutionRejection(self.name(),
                                           "Failed to validate slot {0}"
                                           "with action {1}"
                                           "".format(slot_to_fill,
                                                     self.name()))
        # we'll check when validation failed in order
        # to add appropriate utterances
        for slot, value in slot_values.items():
            if slot == 'num_people':
                if not self.is_int(value) or int(value) <= 0:
                    dispatcher.utter_template('utter_wrong_num_people',
                                              tracker)
                    # validation failed, set slot to None
                    slot_values[slot] = None
