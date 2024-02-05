import unittest
from flip_note import FlipNote


class TestFlipNote(unittest.TestCase):
    def setUp(self) -> None:
        self.small_note = {
            "modelName": "Basic",
            "tags": ["tag", "another_tag"],
            "fields": {
                "Front": "front content",
                "Back": "back content"
            }
        }
        self.big_note = {
                "deckName": "Default",
                "modelName": "Basic",
                "fields": {
                    "Front": "front content",
                    "Back": "back content"
                },
                "tags": [
                    "yomichan"
                ],
                "audio": [{
                    "url": "https://assets.languagepod101.com/dictionary/japanese/audiomp3.php?kanji=猫&kana=ねこ",
                    "filename": "yomichan_ねこ_猫.mp3",
                    "skipHash": "7e2c2f954ef6051373ba916f000168dc",
                    "fields": [
                        "Front"
                    ]
                }],
                "video": [{
                    "url": "https://cdn.videvo.net/videvo_files/video/free/2015-06/small_watermarked/Contador_Glam_preview.mp4",
                    "filename": "countdown.mp4",
                    "skipHash": "4117e8aab0d37534d9c8eac362388bbe",
                    "fields": [
                        "Back"
                    ]
                }],
                "picture": [{
                    "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/A_black_cat_named_Tilly.jpg/220px-A_black_cat_named_Tilly.jpg",
                    "filename": "black_cat.jpg",
                    "skipHash": "8d6e4646dfae812bf39651b59d7429ce",
                    "fields": [
                        "Back"
                    ]
                }]
            }

    def test_flip_field(self) -> None:
        expected = {
            "modelName": "Basic",
            "tags": ["tag", "another_tag"],
            "fields": {
                "Front": "back content",
                "Back": "front content"
            }
        }
        actual = FlipNote.flip_fields(self.small_note)
        self.assertEqual(expected, actual)

    def test_flip_media_fields(self) -> None:
        input_note = self.big_note
        del input_note["picture"]
        del input_note["video"]
        expected = {
                "deckName": "Default",
                "modelName": "Basic",
                "fields": {
                    "Front": "front content",
                    "Back": "back content"
                },
                "tags": [
                    "yomichan"
                ],
                "audio": [{
                    "url": "https://assets.languagepod101.com/dictionary/japanese/audiomp3.php?kanji=猫&kana=ねこ",
                    "filename": "yomichan_ねこ_猫.mp3",
                    "skipHash": "7e2c2f954ef6051373ba916f000168dc",
                    "fields": [
                        "Back"
                    ]
                }]
            }
        actual = FlipNote.flip_media_fields(input_note, "audio")
        self.assertEqual(expected, actual)

    def test_flip_note(self) -> None:
        expected = {
                "deckName": "Default",
                "modelName": "Basic",
                "fields": {
                    "Front": "back content",
                    "Back": "front content"
                },
                "tags": [
                    "yomichan"
                ],
                "audio": [{
                    "url": "https://assets.languagepod101.com/dictionary/japanese/audiomp3.php?kanji=猫&kana=ねこ",
                    "filename": "yomichan_ねこ_猫.mp3",
                    "skipHash": "7e2c2f954ef6051373ba916f000168dc",
                    "fields": [
                        "Back"
                    ]
                }],
                "video": [{
                    "url": "https://cdn.videvo.net/videvo_files/video/free/2015-06/small_watermarked/Contador_Glam_preview.mp4",
                    "filename": "countdown.mp4",
                    "skipHash": "4117e8aab0d37534d9c8eac362388bbe",
                    "fields": [
                        "Front"
                    ]
                }],
                "picture": [{
                    "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/A_black_cat_named_Tilly.jpg/220px-A_black_cat_named_Tilly.jpg",
                    "filename": "black_cat.jpg",
                    "skipHash": "8d6e4646dfae812bf39651b59d7429ce",
                    "fields": [
                        "Front"
                    ]
                }]
            }
        actual = FlipNote().flip_note(self.big_note)
        self.assertEqual(expected, actual)

    def test_flip_note_no_media(self) -> None:
        expected = {
            "modelName": "Basic",
            "tags": ["tag", "another_tag"],
            "fields": {
                "Front": "back content",
                "Back": "front content"
            }
        }
        actual = FlipNote().flip_note(self.small_note)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
