<<<<<<< HEAD
from abc import ABC , abstractmethod
=======
from abc import ABC, abstractmethod
>>>>>>> master

class LLMInterface(ABC):

    @abstractmethod
<<<<<<< HEAD
    def set_generation_model(self , model_id: str):
        pass



    @abstractmethod
    def set_embedding_model(self , model_id: str, embedding_size : int ):
        pass


    @abstractmethod
    def generate_text(self , prompt: str , chat_history: list = [], max_output_tokens : int = None ,
                        temperature : float=None ):
        pass

    @abstractmethod
    def embed_text(self , texts : str , document_type : str = None  ):
        pass

    @abstractmethod
    def construct_prompt(self , prompt : str  , role : str  ):
        pass
=======
    def set_generation_model(self, model_id: str):
        pass

    @abstractmethod
    def set_embedding_model(self, model_id: str, embedding_size: int):
        pass

    @abstractmethod
    def generate_text(self, prompt: str, chat_history: list=[], max_output_tokens: int=None,
                            temperature: float = None):
        pass

    @abstractmethod
    def embed_text(self, text: str, document_type: str = None):
        pass

    @abstractmethod
    def construct_prompt(self, prompt: str, role: str):
        pass
>>>>>>> master
