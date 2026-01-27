from enum import Enum

class VectordbEnums(str, Enum):
    Qdrant = "QDRANT" 

class DistanceMethodEnums( Enum):
    COSINE = "cosine"
    DOT= "dot"