from enum import Enum

class LLMEnums(Enum):
        OPENAI = "OPENAI"
        COHERE = "COHERE"
        ANTHROPIC = "ANTHROPIC"

class OpenAIEnums(Enum):
        SYSTEM = "system"
        USER = "user"
        ASSISTANT = "assistant"

class CohereEnums(Enum):
        SYSTEM = "system"
        USER = "user"
        ASSISTANT = "assistant"
class DocumentTypeEnums(Enum):
        DOCUMENT = "document"
        QUERY = "query"




