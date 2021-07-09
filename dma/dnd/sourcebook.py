from enum import IntEnum

from dataclasses import dataclass


@dataclass
class Sourcebook:
    title: str
    authors: str = None
    link: str = None
    date: str = None
    isbn: str = None


sourcebooks = {
    'unknown':Sourcebook('UNKNOWN'),
    'mm1':Sourcebook('Monster Manual'),
    'ff':Sourcebook('Fiend Folio'),
    'mm2':Sourcebook('Monster Manual 2'),
    'phb':Sourcebook("Player's Handbook"),
    'dmg':Sourcebook("Dungeon Master's Guide"),
    'ua':Sourcebook('Unearthed Arcana')
}


class SourceBook(IntEnum):
    UNKNOWN = 0
    MONSTER_MANUAL = 1
    FIEND_FOLIO = 2
    MONSTER_MANUAL_2 = 3
    PLAYERS_HANDBOOK = 4
    DUNGEON_MASTERS_GUIDE = 5
    UNEARTHED_ARCANA = 7
