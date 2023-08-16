import json
import requests
from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, data, headers):
        pass

class ConcreteObserver(Observer):
    def __init__(self, url):
        self.url = url

    def update(self, data, headers):
        requests.post(self.url, data=json.dumps(data), headers=headers)

class Subject:
    def __init__(self):
        self.observers = set()

    def attach(self, observer):
        self.observers.add(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self, data, headers):
        for observer in self.observers:
            observer.update(data, headers)

def main():
    notifier = Subject()
    observer1 = ConcreteObserver("http://example.com/endpoint1")
    observer2 = ConcreteObserver("http://example.com/endpoint2")

    notifier.attach(observer1)
    notifier.attach(observer2)

    data = {"message": "Hello, observers!"}
    headers = {"Content-Type": "application/json"}

    notifier.notify(data, headers)

if __name__ == "__main__":
    main()
