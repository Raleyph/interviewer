from typing import BinaryIO
from pathlib import Path


class S3FileStorage:
    def save(self, path: Path, file: BinaryIO) -> Path:
        raise NotImplementedError

    def delete(self, path: Path) -> None:
        raise NotImplementedError

    def get_url(self, path: Path) -> str:
        raise NotImplementedError
