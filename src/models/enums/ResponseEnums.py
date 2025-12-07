from enum import Enum

class ResponseSignal( Enum):
    File_Validated_Success = "File validated Successfully"
    File_Type_Not_Supported = "File type not Supported"
    File_Size_Exceeded = "File size Exceeded"
    File_Upload_Success = "File uploaded Successfully"
    File_Upload_Failed = "File upload Failed"
    Processing_Failed = "processing_failed"
    Processing_Success = "Processing_Success"

