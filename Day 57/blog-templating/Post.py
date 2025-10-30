class Post:
    def __init__(self, posts, id):
        self.post = next((p for p in posts if p.get("id") == id), None)

    def get(self):
        return self.post
