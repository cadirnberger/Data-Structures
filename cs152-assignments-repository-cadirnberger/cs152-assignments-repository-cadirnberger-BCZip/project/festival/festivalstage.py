from project.festival.songs import Song
from datastructures.ilinkedlist import ILinkedList
from datastructures.linkedlist import LinkedList

class FestivalStage():
    """Class to manage a playlist for a music festival stage."""

    def __init__(self, name: str):
        """Initialize the stage with a name and an empty playlist."""
        self._name = name
        self._play_list = LinkedList()

    def add_song(self, song: Song) -> None:
        """Add a song to the end of the playlist."""
        self._play_list.append(song)

    def emergency_insert(self, song: Song, position: int) -> None:
        """Insert a song at a specific position for urgent additions."""
        self._play_list.insert_at(song, position - 1)

    def remove_song(self, title: str) -> Song:
        """Remove and return a song by its title."""
        count = 0
        for i in  self._play_list:
            if title == i.title:
                self._play_list.pop_at(count)
                break 
            else:
                count += 1
        return i 


    def swap_songs(self, pos1: int, pos2: int) -> None:
        """Swap the positions of two songs in the playlist."""
    
        if 0 <= pos1 < len(self._play_list) and 0 <= pos2 < len(self._play_list):
            self._play_list[pos1], self._play_list[pos2] = self._play_list[pos2], self._play_list[pos1]



    def create_energy_wave(self) -> None:
        """Reorder playlist to alternate between high and low energy songs."""
        high_energy = [song for song in self._play_list if song.energy_level >= 8]
        low_energy = [song for song in self._play_list if song.energy_level < 8]

        sorted(high_energy)
        sorted(low_energy)

        energy_wave = []
        while high_energy or low_energy:
            if high_energy:
               energy_wave.append(high_energy.pop(0))
            if low_energy:
                energy_wave.append(low_energy.pop(0))

        self._play_list = energy_wave
        

    def crowd_pleaser_mode(self) -> None:
        """Move all high-energy songs to the front of the playlist."""
        high_energy_threshold = 8

        high_energy = [song for song in self._play_list if song.energy_level >= high_energy_threshold]
        low_energy = [song for song in self._play_list if song.energy_level < high_energy_threshold]

        self._play_list = high_energy + low_energy

    def genre_block(self, genre: str) -> None:
        """Group all songs of a specified genre together."""

        genre_songs = [song for song in self._play_list if song.genre == genre]
        other_songs = [song for song in self._play_list if song.genre != genre]

        self._play_list = genre_songs + other_songs


    def estimated_time_remaining(self) -> int:
        """Calculate total remaining time in the playlist."""
        time = 0
        for i in self._play_list:
            time += i.duration
        return time

    def print_playlist(self) -> None:
        """Display the current playlist with song details."""
        count = 0
        for i in self._play_list:
            count += 1
            print(f'{count}. {i.title} - {i.artist} ({i.duration // 60}:{i.duration % 60:02}) [{i.genre}] Energy: {i.energy_level}')
        remaining_time = self.estimated_time_remaining()
        print(f"Estimated Time Remaining: {remaining_time // 60}:{remaining_time % 60:02}")

    def play_current_song(self) -> Song:
        """Play (remove) the first song in the playlist."""
        self._play_list.pop_front()