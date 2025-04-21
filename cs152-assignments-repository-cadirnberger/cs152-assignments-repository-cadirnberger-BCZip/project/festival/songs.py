from dataclasses import dataclass
from typing import Any


@dataclass(order=True)
class Song:
    title: str
    artist: str
    duration: int 
    genre: str
    energy_level: int  # 1-10 scale
    def __it__(self, song2: Any) -> bool:
        return type(song2) is Song and self.energy_level < song2.energy_level
    