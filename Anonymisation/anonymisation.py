from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine, OperatorConfig
from presidio_anonymizer.operators import Operator, OperatorType

from typing import Dict

class InstanceCounterAnonymizer(Operator):
    REPLACING_FORMAT = "<{entity_type}_{index}>"

    def operate(self, text: str, params: Dict = None) -> str:
        entity_type: str = params["entity_type"]

        # entity_mapping is a dict of dicts containing mappings per entity type
        entity_mapping: Dict[Dict:str] = params["entity_mapping"]

        entity_mapping_for_type = entity_mapping.get(entity_type)
        if not entity_mapping_for_type:
            new_text = self.REPLACING_FORMAT.format(
                entity_type=entity_type, index=0
            )
            entity_mapping[entity_type] = {}

        else:
            if text in entity_mapping_for_type:
                return entity_mapping_for_type[text]

            previous_index = self._get_last_index(entity_mapping_for_type)
            new_text = self.REPLACING_FORMAT.format(
                entity_type=entity_type, index=previous_index + 1
            )

        entity_mapping[entity_type][text] = new_text
        return new_text

    @staticmethod
    def _get_last_index(entity_mapping_for_type: Dict) -> int:
        """Get the last index for a given entity type."""

        def get_index(value: str) -> int:
            return int(value.split("_")[-1][:-1])

        indices = [get_index(v) for v in entity_mapping_for_type.values()]
        return max(indices)

    def validate(self, params: Dict = None) -> None:
        if "entity_mapping" not in params:
            raise ValueError("An input Dict called `entity_mapping` is required.")
        if "entity_type" not in params:
            raise ValueError("An entity_type param is required.")

    def operator_name(self) -> str:
        return "entity_counter"

    def operator_type(self) -> OperatorType:
        return OperatorType.Anonymize
    

def anonymize_prompt(prompt: str):
    analyzer = AnalyzerEngine()
    analyzer_results = analyzer.analyze(text=prompt, language="en")
    
    anonymizer_engine = AnonymizerEngine()
    anonymizer_engine.add_anonymizer(InstanceCounterAnonymizer)
    entity_mapping = dict()
    anonymized_result = anonymizer_engine.anonymize(
        prompt,
        analyzer_results,
        {
            "DEFAULT": OperatorConfig(
                "entity_counter", {"entity_mapping": entity_mapping}
            )
        },
    )
    return anonymized_result, entity_mapping
    

def deanonymize_response(response: str, entity_mapping: dict) -> str:
    reverse_mapping = {}
    
    for _, mappings in entity_mapping.items():
        for real_value, placeholder in mappings.items():
            reverse_mapping[placeholder] = real_value
            
    for placeholder, real_value in reverse_mapping.items():
        response = response.replace(placeholder, real_value)
    return response

