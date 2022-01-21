from typing import Any, Optional
import ctypes
import functools
import os


class EnvVariablesController:
    def __init__(self) -> None:
        self._environ = None

    def get(self, value: str) -> Optional[str]:
        """
        Read environment variables.
        """
        return os.environ.get(value, None)

    def set(self, name: str, value: Any) -> None:
        """
        Set environment variables.
        """
        os.environ[name] = value

    def check_vars(self, *vars: Any) -> dict:
        for var in vars:
            if not self.get(var):
                return {"status": "error", "msg": f"{var} NÃO SETADA"}
        return {"status": "ok"}