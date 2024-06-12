from utilities.general_utils import rank_keys
from config.settings import DEFAULT_STARTING_AMBIANCE
class Ambiance_System():
    def __init__(self, starting_value=DEFAULT_STARTING_AMBIANCE):
        self._current_ambiance = starting_value
        self._ranked_keys = rank_keys(self._current_ambiance)

    @property
    def current_ambiance(self):
        return self._current_ambiance

    @current_ambiance.setter
    def current_ambiance(self, value):
        self._current_ambiance = value
        self._ranked_keys = rank_keys(value)

    @property
    def ranked_keys(self):
        return self._ranked_keys