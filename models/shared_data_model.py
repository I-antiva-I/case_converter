from typing import Set, Dict


class SharedDataModel:
    def __init__(self):
        self._data: Dict[str, object] = {}

    def update_shared(self, key: str, value: object) -> None:
        self._data[key] = value

    def get_shared(self, key) -> object:
        if key in self._data:
            return self._data.get(key)
        else:
            raise KeyError(f"[!] No key named {key} in shared data")

    @property
    def small_words(self) -> Set[str]:
        return self._data.get("small_words", set())

    def set_small_words(self, value) -> None:
        self._data["small_words"] = value


