from src.invoke import invoke
from src.anki_tools import add_deck, add_notes
from src.flip_note import FlipNote


origin_deck = "Polish - Croatian"
new_deck = "Croatian - Polish"


if __name__ == "__main__":
    if new_deck not in invoke('deckNames'):
        add_deck(new_deck)

    new_note_base = {
        "deckName": new_deck,
        "options": {
            "allowDuplicate": False,
            "duplicateScope": "deck"
        }
    }

    notes_ids = invoke('findNotes', query="*")
    all_notes = invoke('notesInfo', notes=notes_ids)

    for i, note in enumerate(all_notes):
        del note['cards']
        del note['noteId']

        note['fields'] = {
            'Front': note['fields']['Front']['value'],
            'Back': note['fields']['Back']['value']
        }

        note.update(new_note_base)

        all_notes[i] = FlipNote().flip_note(note)

    add_notes(all_notes)

    invoke('sync')
