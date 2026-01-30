from fastapi import FastAPI
<<<<<<< HEAD
from routers import base , data
from motor.motor_asyncio import AsyncIOMotorClient
from helpers.config import get_settings
from stores.llm.LLMProviderFactory import LLMProviderFactory

app = FastAPI()


@app.on_event("startup")
async def startup_db_client():
=======
from routes import base, data, nlp
from motor.motor_asyncio import AsyncIOMotorClient
from helpers.config import get_settings
from stores.llm.LLMProviderFactory import LLMProviderFactory
from stores.vectordb.VectorDBProviderFactory import VectorDBProviderFactory
from stores.llm.templates.template_parser import TemplateParser

app = FastAPI()

async def startup_span():
>>>>>>> master
    settings = get_settings()
    app.mongo_conn = AsyncIOMotorClient(settings.MONGODB_URL)
    app.db_client = app.mongo_conn[settings.MONGODB_DATABASE]

    llm_provider_factory = LLMProviderFactory(settings)
<<<<<<< HEAD

    #generation Client
    app.generation_client = llm_provider_factory.create(settings.GENERATION_BACKEND)
    app.generation_client.set_generation_model(model_id=settings.GENERATION_MODEL_ID)

    #embedding client 
    app.embedding_client = llm_provider_factory.create(settings.EMBEDDING_BACKEND)
    app.embedding_client.set_embedding_model(model_id=settings.EMBEDDING_MODEL_ID, embedding_size=settings.EMBEDDING_MODEL_SIZE)

@app.on_event("shutdown")
async def shutdown_db_client():
    app.mongo_conn.close()


app.include_router(base.base_router)
app.include_router(data.data_router)

 
=======
    vectordb_provider_factory = VectorDBProviderFactory(settings)

    # generation client
    app.generation_client = llm_provider_factory.create(provider=settings.GENERATION_BACKEND)
    app.generation_client.set_generation_model(model_id = settings.GENERATION_MODEL_ID)

    # embedding client
    app.embedding_client = llm_provider_factory.create(provider=settings.EMBEDDING_BACKEND)
    app.embedding_client.set_embedding_model(model_id=settings.EMBEDDING_MODEL_ID,
                                             embedding_size=settings.EMBEDDING_MODEL_SIZE)
    
    # vector db client
    app.vectordb_client = vectordb_provider_factory.create(
        provider=settings.VECTOR_DB_BACKEND
    )
    try:
        app.vectordb_client.connect()
    except Exception as ex:
        import logging
        logger = logging.getLogger('uvicorn.error')
        logger.warning(f"Could not connect to vector DB: {ex}")

    # template parser
    app.template_parser = TemplateParser(
        language=settings.PRIMARY_LANG,
        default_language=settings.DEFAULT_LANG,
    )


async def shutdown_span():
    app.mongo_conn.close()
    try:
        app.vectordb_client.disconnect()
    except Exception:
        pass

app.on_event("startup")(startup_span)
app.on_event("shutdown")(shutdown_span)

app.include_router(base.base_router)
app.include_router(data.data_router)
app.include_router(nlp.nlp_router)
>>>>>>> master
