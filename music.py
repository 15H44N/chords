from dataclasses import dataclass, field
import re
from typing import List, Optional


@dataclass
class Note:
    name: str

    # Define note sequences with enharmonic equivalents

    NOTE_SEQUENCES = [
        ["C"],
        ["C#", "Db"],
        ["D"],
        ["D#", "Eb"],
        ["E"],
        ["F"],
        ["F#", "Gb"],
        ["G"],
        ["G#", "Ab"],
        ["A"],
        ["A#", "Bb"],
        ["B"],
    ]

    def __post_init__(self):
        if not any(self.name in group for group in self.NOTE_SEQUENCES):
            raise ValueError(f"Invalid note name {self.name}")

    def transpose(self, semitones: int) -> "Note":
        for index, group in enumerate(self.NOTE_SEQUENCES):
            if self.name in group:
                current_index = index
                break
        else:
            raise ValueError(f"Invalid note name {self.name}")

        # Calculate the new index
        # Use len(self.NOTE_SEQUENCES) explicitly after modulus to ensure positive index
        # for negative semitones, wrap around will not work, we will offset with length of list to get correct index
        # Calculate the new index with wrap-around for negative semitones
        total_notes = len(self.NOTE_SEQUENCES)
        new_index = (current_index + semitones) % total_notes
        if new_index < 0:
            new_index += total_notes

        # Choose the first item in the new group as default for simplicity
        # first item in every member of sequence is the note name
        new_note = self.NOTE_SEQUENCES[new_index][0]

        return Note(name=new_note)

    def get_enharmonic_equivalents(self) -> List[str]:
        # Return enharmonic equivalents for the current note
        for group in self.NOTE_SEQUENCES:
            if self.name in group:
                return group
        return []


@dataclass
class Chord:
    name: str
    root: Optional[Note] = None
    chord_type: Optional[str] = None
    explicit_type: bool = False  # Track if the chord type was explicitly specified

    # fmt:off
    CHORD_QUALITIES = ['maj7', 'm7', '7', 'm', 'dim', 'aug', '+', 'o',
                       'sus4', 'sus2', '6', '9', '11', '13', 'add9']
    # fmt:on

    def __post_init__(self):
        self.parse_chord(self.name)

    def parse_chord(self, chord_name: str):
        chord_regex = re.compile(r"^([A-G])([b#]?)")
        match = chord_regex.match(chord_name)
        if match:
            root_name = match.group(1) + (match.group(2) or "")
            self.root = Note(name=root_name)

        remaining = chord_name[len(root_name) :]

        for quality in self.CHORD_QUALITIES:
            if remaining.startswith(quality):
                self.chord_type = quality
                self.explicit_type = True
                break
        else:
            # Decide on the implicit "Major" when not explicitly mentioned
            self.chord_type = None if not remaining else remaining

    def transpose(self, semitones: int) -> "Chord":
        if not self.root:
            raise ValueError("Cannot transpose a chord without a root")

        transposed_root = self.root.transpose(semitones)
        # Only include the type if it was explicitly specified
        new_chord_name = (
            f"{transposed_root.name}{self.chord_type or ''}"
            if self.explicit_type
            else transposed_root.name
        )
        return Chord(name=new_chord_name)
