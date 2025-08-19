from src.user import User


class Post:
    def __init__(self, author: User, post_type: str,
                 title: str, content: str):
        self.__author: User = author
        self.__title: str = title
        self.__content: str = content
        self.__comments: list['Post'] = []
        self.__likes: list[User] = []

    @property
    def author(self) -> User:
        return self.__author

    @property
    def title(self) -> str:
        return self.__title

    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, new_content: str) -> None:
        if len(new_content) == 0:
            raise ValueError("New content can't be empty")
        self.__content = new_content

    @property
    def comments(sefl) -> list['Post']:
        return self.__comments

    @def add_comment(self, new_comment: list[Post]):
        self.comments.append(new_comment)
