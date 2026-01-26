from .LLMEnums import LLMEnums
from Providers import OpenAiProvider , CohereProvider


class LLMProviderFactory :

    def __init__ (self, config:dict):

        self.config = config 

    def create(self, Provider:str):
        
        if Provider == LLMEnums.OPENAI.value:
            return OpenAiProvider(
                api_key = self.config.OPENAI_API_KEY,
                api_url = self.config.OPENAI_API_URL,
                default_input_max_characters = self.config.INPUT_DAFAULT_MAX_CHARACTERS,
                default_generation_max_output_tokens = self.config.GENERATION_DAFAULT_MAX_TOKENS,
                default_generation_temperature = self.config.GENERATION_DAFAULT_TEMPERATURE
            )
             



        if Provider  == LLMEnums.COHERE.value:
            return CohereProvider(
                api_key = self.config.COHERE_API_KEY,
                default_input_max_characters = self.config.INPUT_DAFAULT_MAX_CHARACTERS,
                default_generation_max_output_tokens = self.config.GENERATION_DAFAULT_MAX_TOKENS,
                default_generation_temperature = self.config.GENERATION_DAFAULT_TEMPERATURE
            )
            

        return None

        

