from fastapi import FastAPI
from store.core.config import settings


class App(FastAPI):
    def __init__(self, *args, **kwargs):
        super().__init__(
            *args,
            **kwargs,
            version="0.0.1",
            title=settings.PROJECT_NAME,
            root_path=settings.ROOT_PATH,
            docs_url="/docs"
        )


app = App()


@app.get("/")
def read_root():
    return {"Hello": "World"}
