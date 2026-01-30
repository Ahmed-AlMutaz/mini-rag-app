from enum import Enum

class LLMEnums(Enum):
<<<<<<< HEAD
        OPENAI = "OPENAI"
        COHERE = "COHERE"
        ANTHROPIC = "ANTHROPIC"

class OpenAIEnums(Enum):
        SYSTEM = "system"
        USER = "user"
        ASSISTANT = "assistant"

class CohereEnums(Enum):
        SYSTEM = "SYSTEM"
        USER = "USER"
        ASSISTANT = "CHATBOT"
        
class DocumentTypeEnums(Enum):
        DOCUMENT = "document"
        QUERY = "query"




=======
    OPENAI = "OPENAI"
    COHERE = "COHERE"

class OpenAIEnums(Enum):
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"

class CoHereEnums(Enum):
    SYSTEM = "SYSTEM"
    USER = "USER"
    ASSISTANT = "CHATBOT"

    DOCUMENT = "search_document"
    QUERY = "search_query"


class DocumentTypeEnum(Enum):
    DOCUMENT = "document"
    QUERY = "query"
>>>>>>> master
