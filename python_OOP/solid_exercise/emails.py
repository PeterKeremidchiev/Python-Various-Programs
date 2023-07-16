from abc import ABC, abstractmethod


class IContent(ABC):
    def __init__(self, text):
        self.text = text

    @abstractmethod
    def format(self):
        pass


class MyContent(IContent):

    def format(self):
        return '\n'.join(['<myML>', self.text, '</myML>'])


class ISender(ABC):
    def __init__(self, sender):
        self.sender = sender

    @abstractmethod
    def send(self):
        pass


class Sender(ISender):

    def send(self):
        return ''.join(["I'm ", self.sender])


class IReceiver(ABC):
    def __init__(self, receiver):
        self.receiver = receiver

    @abstractmethod
    def receive(self):
        pass


class Receiver(IReceiver):

    def receive(self):
        return ''.join(["I'm ", self.receiver])


class IEmail(ABC):


    @abstractmethod
    def set_sender(self, sender):
        pass

    @abstractmethod
    def set_receiver(self, receiver):
        pass

    @abstractmethod
    def set_content(self, content):
        pass


class Email(IEmail):

    def __init__(self, protocol):
        self.protocol = protocol
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, sender: ISender):
        self.__sender = sender.send()

    def set_receiver(self, receiver: IReceiver):
        self.__receiver = receiver.receive()

    def set_content(self, content: IContent):
        self.__content = content.format()

    def __repr__(self):

        template = f"Sender: {self.__sender}\nReceiver: {self.__receiver}\nContent:\n{self.__content}"

        return template



email = Email('IM')
sender = Sender('qmal')
email.set_sender(sender)
receiver = Receiver('james')
email.set_receiver(receiver)
content = MyContent('Hello, there!')
email.set_content(content)
print(email)





