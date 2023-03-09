from math import ceil


class PhotoAlbum:
    MAX_PER_PAGE = 4

    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]
        a = 1

    @classmethod
    def from_photos_count(cls, photos_count):
        return cls(ceil(photos_count / cls.MAX_PER_PAGE))

    def add_photo(self, label):
        for index in range(len(self.photos)):
            page = self.photos[index]

            if len(page) < self.MAX_PER_PAGE:
                page.append(label)
                return f"{label} photo added successfully on page {index + 1} slot {len(page)}"

        return "No more free slots"

    def display(self):
        result = ["-" * 11]
        for page in self.photos:
            result.append(("[] " * len(page)).rstrip())
            result.append("-" * 11)

        return "\n".join(result)

