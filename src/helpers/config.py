from pydantic_settings import BaseSettings, SettingsConfigDict

class Sittings(BaseSettings):

    app_name : str 
    app_version : str 
    OPENAIKEY : str
    
    File_Allowed_Types: list
    File_Max_Size_MB: int
    File_Default_Chunk_Size: int

    MongoDB_URI: str
    MongoDB_Database: str


    class Config:
        env_file = ".env"


def get_settings():
    return Sittings()