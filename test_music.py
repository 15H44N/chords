from music import Chord, Note


def test_note_transposition():
    # Simple transpositions
    note_c = Note("C")
    transposed_note = note_c.transpose(1)
    assert transposed_note.name == "C#", "C transposed by 1 semitone should be C#"

    note_f = Note("F")
    transposed_note = note_f.transpose(2)
    assert transposed_note.name == "G", "F transposed by 2 semitones should be G"

    # Wrap-around transpositions
    note_b = Note("B")
    transposed_note = note_b.transpose(1)
    assert transposed_note.name == "C", "B transposed by 1 semitone should be C"

    note_csharp = Note("C#")
    transposed_note = note_csharp.transpose(-1)
    assert transposed_note.name == "C", "C# transposed by -1 semitone should be C"

    # Enharmonic equivalents
    enharmonics = note_csharp.get_enharmonic_equivalents()
    assert "Db" in enharmonics, "C# should have Db as an enharmonic equivalent"

    note_eb = Note("Eb")
    enharmonics_eb = note_eb.get_enharmonic_equivalents()
    assert "D#" in enharmonics_eb, "Eb should have D# as an enharmonic equivalent"

    print("Note transposition and enharmonic equivalence tests passed!")


def test_chord_transposition():
    # Test implicit Major chords
    chord_c = Chord("C")
    transposed_chord = chord_c.transpose(2)
    assert (
        transposed_chord.name == "D"
    ), "C transposed by 2 semitones should be D without explicit 'Major'"

    chord_g = Chord("G")
    transposed_chord_g = chord_g.transpose(-1)
    assert (
        transposed_chord_g.name == "F#"
    ), "G transposed by -1 semitone should be F# without explicit 'Major'"

    # Test explicit minor chord transposition
    chord_am = Chord("Am")
    transposed_am = chord_am.transpose(3)
    assert transposed_am.name == "Cm", "Am transposed by 3 semitones should be Cm"

    # Test explicit chord type
    chord_d7 = Chord("D7")
    transposed_chord_d7 = chord_d7.transpose(2)
    assert transposed_chord_d7.name == "E7", "D7 transposed by 2 semitones should be E7"

    # Test double transpositions
    note_b_double_flat = Note("B")
    for _ in range(-12, 0):
        note_b_double_flat = note_b_double_flat.transpose(1)
    assert (
        note_b_double_flat.name == "B"
    ), "B transposed down by 12 semitones and back up should be B"

    print("Chord transposition and type tests passed!")


def test_negative_note_transposition():
    # Negative transpositions
    note_fsharp = Note("F#")
    transposed_note = note_fsharp.transpose(-7)
    assert transposed_note.name == "B", "F# transposed by -7 semitones should be B"

    note_d = Note("D")
    transposed_note = note_d.transpose(-1)
    assert transposed_note.name == "C#", "D transposed by -1 semitone should be C#"

    note_a = Note("A")
    transposed_note = note_a.transpose(-2)
    assert transposed_note.name == "G", "A transposed by -2 semitones should be G"

    print("Negative note transposition tests passed!")


def test_negative_chord_transposition():
    # Negative transpositions with chords
    chord_e = Chord("E")
    transposed_chord = chord_e.transpose(-3)
    assert transposed_chord.name == "C#", "E transposed by -3 semitones should be C#"

    chord_bm = Chord("Bm")
    transposed_bm = chord_bm.transpose(-2)
    assert transposed_bm.name == "Am", "Bm transposed by -2 semitones should be Am"

    # Chord with negative wrap-around
    chord_ab7 = Chord("Ab7")
    transposed_ab7 = chord_ab7.transpose(-5)
    assert transposed_ab7.name == "D#7", "Ab7 transposed by -5 semitones should be D#7"

    print("Negative chord transposition tests passed!")


if __name__ == "__main__":
    test_note_transposition()
    test_chord_transposition()
    test_negative_note_transposition()
    test_negative_chord_transposition()
