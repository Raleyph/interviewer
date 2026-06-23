from abc import ABC, abstractmethod
from pathlib import Path
from typing import BinaryIO
from uuid import uuid4


class BaseFileStorage(ABC):
    def __init__(self, allowed_extensions: set[str]):
        self._allowed_extensions = allowed_extensions

    # should be implemented

    @abstractmethod
    async def _save_impl(self, path: Path, file: BinaryIO) -> None: ...

    @abstractmethod
    async def _delete_impl(self, path: Path) -> None: ...

    @abstractmethod
    async def _get_url_impl(self, path: Path) -> str: ...

    # internal logic

    def _validate_extension(self, original_name: str) -> str:
        ext = Path(original_name).suffix.lower()

        if ext not in self._allowed_extensions:
            raise ValueError("File extension is not allowed")

        return ext

    @staticmethod
    def _generate_path(ext: str) -> Path:
        file_id = uuid4().hex
        filename = f"{file_id}{ext}"
        return Path(file_id[:2]) / file_id[2:4] / filename

    # common methods

    async def save(self, file: BinaryIO, original_name: str) -> Path:
        ext = self._validate_extension(original_name)
        path = self._generate_path(ext)
        await self._save_impl(path, file)
        return path

    async def delete(self, path: Path) -> None:
        await self._delete_impl(path)

    async def get_url(self, path: Path) -> str:
        return await self._get_url_impl(path)
