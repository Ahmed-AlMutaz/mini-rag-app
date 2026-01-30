from pydantic import BaseModel, Field, validator
from typing import Optional
from bson.objectid import ObjectId
from datetime import datetime

class Asset(BaseModel):
<<<<<<< HEAD
    id : Optional[ObjectId] = Field(None, alias="_id")
    asset_project_id : ObjectId
    asset_type : str = Field(..., min_length=1)
    asset_name : str = Field(..., min_length=1)
    asset_size : int = Field(ge=0 , default=0)
    asset_config : dict = Field(default=None)
    asset_pushed_at : datetime = Field(default=datetime.utcnow) 

=======
    id: Optional[ObjectId] = Field(None, alias="_id")
    asset_project_id: ObjectId
    asset_type: str = Field(..., min_length=1)
    asset_name: str = Field(..., min_length=1)
    asset_size: int = Field(ge=0, default=None)
    asset_config: dict = Field(default=None)
    asset_pushed_at: datetime = Field(default=datetime.utcnow)
>>>>>>> master

    class Config:
        arbitrary_types_allowed = True

    @classmethod
    def get_indexes(cls):
<<<<<<< HEAD
        return [

            { "key":
             [
                ("asset_project_id", 1)
            ],

            "name" :" asset_project_id_1_index_1",

            "unique": False

            },
            { "key":
             [
                ("asset_project_id", 1),
                ("asset_name", 1)
            ],

            "name" :" asset_project_id_name_index_1",
            "unique": True

             }



            ]
=======

        return [
            {
                "key": [
                    ("asset_project_id", 1)
                ],
                "name": "asset_project_id_index_1",
                "unique": False
            },
            {
                "key": [
                    ("asset_project_id", 1),
                    ("asset_name", 1)
                ],
                "name": "asset_project_id_name_index_1",
                "unique": True
            },
        ]
>>>>>>> master
