class FlipNote:
    @staticmethod
    def flip_fields(note: dict) -> dict:
        front = note["fields"]["Front"]
        note["fields"]["Front"] = note["fields"]["Back"]
        note["fields"]["Back"] = front

        return note

    @staticmethod
    def flip_media_fields(note: dict, media_key: str) -> dict:
        for j, _ in enumerate(note[media_key]):
            for i, value in enumerate(note[media_key][j]["fields"]):
                if value == "Front":
                    note[media_key][j]["fields"][i] = "Back"
                else:
                    note[media_key][j]["fields"][i] = "Front"

        return note

    def flip_note(self, note: dict) -> dict:
        if "fields" in note.keys():
            note = self.flip_fields(note)

        for media_key in ["audio", "video", "picture"]:
            if media_key in note.keys():
                self.flip_media_fields(note, media_key)

        return note
