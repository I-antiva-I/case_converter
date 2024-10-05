from typing import Set, Dict


class SharedDataModel:
    """
    The `SharedDataModel` class manages shared data, providing access for all other models.

    Properties:

    * small_words : Set[str] - SHARED PROPERTY. A set of small words such as "and", "or", "the"
    """
    def __init__(self):
        self._data: Dict[str, object] = {}

    def update_shared(self, key: str, value: object) -> None:
        """
        Updates the shared data with the given key-value pair.
        :param key: Data key.
        :param value: Data value.
        """

        self._data[key] = value

    def get_shared(self, key) -> object:
        """
        Retrieves the value associated with the specified key from the shared data.
        :param key: Data key.
        :return: Data value.
        :raises KeyError: If the specified key does not exist in the shared data.
        """

        if key in self._data:
            return self._data.get(key)
        else:
            raise KeyError(f"[!] No key named {key} in shared data")

    @property
    def small_words(self) -> Set[str]:
        return self._data.get("small_words", set())

    def set_small_words(self, value) -> None:
        self._data["small_words"] = value


