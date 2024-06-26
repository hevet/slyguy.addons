from .constants import ALL
from slyguy.language import BaseLanguage

class Language(BaseLanguage):
    REGION  =           30000,
    REGIONS = {
        'Sydney':       30001,
        'Melbourne':    30002,
        'Brisbane':     30003,
        'Perth':        30004,
        'Adelaide':     30005,
        'Darwin':       30006,
        'Hobart':       30007,
        'Canberra':     30008,
        ALL:            30010,
    }
    STATIONS =          30009

_ = Language()
