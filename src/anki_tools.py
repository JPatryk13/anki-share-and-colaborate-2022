from invoke import invoke


def add_deck(deck_name: str):
    invoke('createDeck', deck=deck_name)


def remove_deck(deck_name: str):
    invoke('deleteDecks', decks=[deck_name], cardsToo=True)


def add_note(old_note: dict, deck_name: str):
    new_note = {
        "deckName": deck_name,
        "options": {
            "allowDuplicate": False,
            "duplicateScope": "deck"
        }
    }
    new_note.update(old_note)
    invoke('addNote', note=new_note)


def add_notes(notes_list: list[dict]):
    invoke('addNotes', notes=notes_list)
