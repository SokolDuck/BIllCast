import os
from typing import Tuple
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware

from bill_cast.api.api_v1.api import api_router
from bill_cast.core.config import settings


app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)


class SinglePageApplication(StaticFiles):
    """Acts similar to the bripkens/connect-history-api-fallback
    NPM package."""

    def __init__(self, directory: os.PathLike, index='index.html') -> None:
        self.index = index

        # set html=True to resolve the index even when no
        # the base path is passed in
        super().__init__(directory=directory, packages=None, html=True, check_dir=True)

    def lookup_path(self, path: str) -> Tuple[str, os.stat_result]:
        """Returns the index file when no match is found.

        Args:
            path (str): Resource path.

        Returns:
            [tuple[str, os.stat_result]]: Always returns a full path and stat result.
        """
        full_path, stat_result = super().lookup_path(path)

        # if a file cannot be found
        if stat_result is None:
            return super().lookup_path(self.index)

        return (full_path, stat_result)


# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=(
            "*" if settings.DEBUG else [str(origin) for origin in settings.BACKEND_CORS_ORIGINS]
        ),
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router, prefix=settings.API_V1_STR)

if os.path.exists(settings.STATIC_FILES_PATH):
    app.mount("/", SinglePageApplication(directory=settings.STATIC_FILES_PATH), name="spa")
