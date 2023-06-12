from abc import ABC, abstractmethod


class IStorage(ABC):
    @abstractmethod
    def list_movies(self):
        pass

    @abstractmethod
    def add_movie(self):
        pass

    @abstractmethod
    def delete_movie(self):
        pass

    @abstractmethod
    def update_movie(self):
        pass

    @abstractmethod
    def random_movie(self):
        pass
