import asyncio

from pathlib import Path
from typing import BinaryIO
from uuid import uuid4

from src.infrastructure.persistence.storage.base import BaseFileStorage


class LocalFileStorage(BaseFileStorage):
    def __init__(
            self,
            root: Path,
            public_url: str,
            allowed_extensions: set[str]
    ):
        super().__init__(allowed_extensions)
        self._root = root.resolve()
        self._public_url = public_url.rstrip("/")

    def _safe_path(self, path: Path) -> Path:
        if path.is_absolute():
            raise ValueError("Absolute paths are not allowed")

        destination = (self._root / path).resolve()

        if not destination.is_relative_to(self._root):
            raise ValueError("Path traversal is not allowed")

        return destination

    async def _save_impl(self, path: Path, file: BinaryIO) -> None:
        destination = self._safe_path(path)
        destination.parent.mkdir(parents=True, exist_ok=True)

        def write():
            temp = destination.with_suffix(
                destination.suffix + f".{uuid4().hex}.tmp"
            )

            try:
                with open(temp, "wb") as dst:
                    while chunk := file.read(1024 * 1024):
                        dst.write(chunk)

                temp.replace(destination)
            finally:
                temp.unlink(missing_ok=True)

        await asyncio.to_thread(write)

    async def _delete_impl(self, path: Path) -> None:
        self._safe_path(path).unlink(missing_ok=True)

    async def _get_url_impl(self, path: Path) -> str:
        path = self._safe_path(path).relative_to(self._root)
        return f"{self._public_url}/{path.as_posix()}"
