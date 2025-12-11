from .BaseController import BaseController
from .ProjectController import ProjectController
import os
from langchain_community.document_loaders import PyMuPDFLoader , TextLoader , UnstructuredWordDocumentLoader
from models import ProcessingEnum
from langchain.text_splitter import RecursiveCharacterTextSplitter





class ProcessController(BaseController):
    def __init__(self , project_id : str):
        super().__init__()

        self.project_id = project_id
        self.project_path = ProjectController().get_Project_Path(project_id = project_id)



    def det_file_extension(self , file_id : str) :
        return os.path.splitext(file_id)[-1]


    def get_file_loader(self , file_id : str ):

        file_ext = self.det_file_extension(file_id = file_id).lower()

        file_path = os.path.join(
            self.project_path,
            file_id
        )


        if file_ext == ProcessingEnum.PDF.value:
            return PyMuPDFLoader(file_path)

        if file_ext == ProcessingEnum.TXT.value :
            return TextLoader(file_path)

        if file_ext == ProcessingEnum.DOCX.value :
            return UnstructuredWordDocumentLoader(file_path)

        else:
            return None
        

    def get_file_content(self , file_id : str):

        loader = self.get_file_loader(file_id = file_id  )
        return loader.load()
    
    def process_file_content(self ,file_content : list ,  file_id : str , chunk_size : int = 1000 , overlap_size : int = 200  ):


        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size = chunk_size ,
            chunk_overlap = overlap_size,
            length_function = len,
            separators = ["\n\n", "\n", " ", ""]
        )

        file_content_texts = [ rec.page_content for rec in file_content ]


        file_content_metadata = [ rec.metadata for rec in file_content ]


        chunks = text_splitter.create_documents(
           file_content_texts,
           metadatas = file_content_metadata
        )

        return chunks

    