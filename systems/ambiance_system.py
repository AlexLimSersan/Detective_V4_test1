from config.settings import DEFAULT_STARTING_AMBIANCE, AMBIANCE_KEYS, AMBIANCE_VALUES


class Ambiance_System():
    def __init__(self, starting_value=DEFAULT_STARTING_AMBIANCE):
        self._current_value = starting_value
        self._ranked_keys = self.rank_keys(self._current_value)

    @property
    def current_value(self):
        return self._current_value

    @current_value.setter
    def current_value(self, value):
        self._current_value = value
        self._ranked_keys = self.rank_keys(value)

    @property
    def ranked_keys(self):
        return self._ranked_keys

    def rank_keys(self, current_value, keys=AMBIANCE_KEYS):
        """Rank mood keys based on the current value, returning keys in the order of closest match."""
        def mood_distance(key):
            return abs(current_value - AMBIANCE_VALUES[key])

        sorted_mood_keys = sorted(keys, key=mood_distance)
        return sorted_mood_keys
