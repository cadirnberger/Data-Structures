from array import array
from datastructures.hashmap import HashMap
import os
import gzip
import pickle
from typing import Any


def get_file_size(file_path: str) -> int:
    try:
        size = os.path.getsize(file_path)
        return size
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return 0


class BCZip:
    def __init__(self, name: str):
        self._name = name
        self.data = HashMap()

    @staticmethod
    def save_to_binary(data: Any, file_name: str) -> None:
        try:
            with gzip.open(file_name, 'wb') as f:
                pickle.dump(data, f)
            print(f"Data saved to {file_name} in compressed binary format.")
        except Exception as e:
            print(f"Error saving to binary: {e}")

    @staticmethod
    def load_from_binary(file_name: str) -> Any:
        try:
            with gzip.open(file_name, 'rb') as f:
                data = pickle.load(f)
            print(f"Data loaded from {file_name}.")
            return data
        except FileNotFoundError:
            print(f"Error: File '{file_name}' not found.")
            return None

    def compress(self):
        try:
            with open(self._name, 'r', encoding='utf-8', errors='replace') as file:
                content = file.read()

            # Tokenize content and populate HashMap
            words = content.split()
            positions = 0
            max_word = len(words)/500
            for word in words:
                if positions < max_word:
                    positions += 1
                    if word =='\n':
                        self.data[-positions] = word
                    self.data[positions] = word

            # Save HashMap to binary file
            compressed_file = f"{self._name}.BCZiP"
            self.save_to_binary(self.data, compressed_file)

            # Print file sizes
            input_size = get_file_size(self._name)
            compressed_size = get_file_size(compressed_file)
            print(f"Input file size: {input_size} bytes")
            print(f"Compressed file size: {compressed_size} bytes")
        except Exception as e:
            print(f"Error during compression: {e}")

    def decompress(self):
        compressed_file = f"{self._name}.BCZiP"
        try:
            self.data = self.load_from_binary(compressed_file)
        except FileNotFoundError:
            print(f"Error: File '{compressed_file}' not found.")
            return

        # Reconstruct the text
        max_position = len(self.data)*50

        reconstructed = [None] * max_position
        for positions, word in self.data.items():
            if positions < 0:
                reconstructed[-positions - 1] = word + '\n'
            else:
                reconstructed[positions - 1] = word
                

        output_file = compressed_file + ".txt"
        with open(output_file, 'w') as file:
            file.write(' '.join(filter(None, reconstructed)))
        compressed_size = get_file_size(self._name)
        decompressed_size = get_file_size(compressed_file)
        print(f"Input file size: {decompressed_size} bytes")
        print(f"Decompressed file size: {compressed_size} bytes")
