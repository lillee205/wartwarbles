class Warble:
    def __init__(self, author, msg):
        self.author = author
        self.msg = msg

    def __repr__(self):
        return "Author: {author}\nMsg: {msg}".format(
            author=self.author, msg=self.msg)
