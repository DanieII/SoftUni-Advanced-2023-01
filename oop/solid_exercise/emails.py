from abc import ABC, abstractmethod


# Interfaces
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


class IContent(ABC):

    def __init__(self, content):
        self.content = content

    @abstractmethod
    def get_content(self):
        pass


class ISenderAndReceiver(ABC):

    def __init__(self, sender, receiver):
        self.sender = sender
        self.receiver = receiver

    @abstractmethod
    def get_sender(self):
        pass

    @abstractmethod
    def get_receiver(self):
        pass


# Content types
class MyContent(IContent):

    def get_content(self):
        return '\n'.join(['<myML>', self.content, '</myML>'])


class NoTagContent(IContent):

    def get_content(self):
        return self.content


# Sender and Receiver types
class IMSenderAndReceiver(ISenderAndReceiver):

    def get_sender(self):
        return f'I\'m {self.sender}'

    def get_receiver(self):
        return f'I\'m {self.receiver}'


class NormalSenderAndReceiver(ISenderAndReceiver):

    def get_sender(self):
        return self.sender

    def get_receiver(self):
        return self.receiver


class Email(IEmail):

    def __init__(self, protocol):
        self.protocol = protocol
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, sender: ISenderAndReceiver):
        self.__sender = sender.get_sender()

    def set_receiver(self, receiver: ISenderAndReceiver):
        self.__receiver = receiver.get_receiver()

    def set_content(self, content: IContent):
        self.__content = content.get_content()

    def __repr__(self):
        template = "Sender: {sender}\nReceiver: {receiver}\nContent:\n{content}"

        return template.format(sender=self.__sender, receiver=self.__receiver, content=self.__content)


info = IMSenderAndReceiver("qmal", "james")

email = Email('IM')
email.set_sender(info)
email.set_receiver(info)
content = MyContent('Hello, there!')
email.set_content(content)
print(email)
