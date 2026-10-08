"""demo email class."""
from __future__ import annotations
import datetime

class Email:
    """email class"""
    def __init__(self, sender: User, receiver: User, subject: str, body: str) -> None:
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body
        self.timestamp = datetime.datetime.now()
        self.read = False

    def mark_as_read(self) -> None:
        """Mark and email as read."""
        self.read = True

    def display_full_email(self) -> None:
        """Display email."""
        self.mark_as_read()
        print('\n--- Email ---')
        print(f'From: {self.sender.name}')
        print(f'To: {self.receiver.name}')
        print(f'Subject: {self.subject}')
        print(f"Received: {self.timestamp.strftime('%Y-%m-%d %H:%M')}")
        print(f'Body: {self.body}')
        print('------------\n')

    def __str__(self) -> str:
        """String representation of the email object."""
        status = 'Read' if self.read else 'Unread'
        return (
            f"[{status}] From: {self.sender.name} | Subject: {self.subject} "
            f"| Time: {self.timestamp.strftime('%Y-%m-%d %H:%M')}"
        )

class User:
    """User class."""
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.inbox: Inbox = Inbox()

    def send_email(self, receiver: User, subject: str, body: str) -> None:
        """Sends email."""
        email = Email(sender=self, receiver=receiver, subject=subject, body=body)
        receiver.inbox.receive_email(email)
        print(f'Email sent from {self.name} to {receiver.name}!\n')

    def check_inbox(self) -> None:
        """Checks email inbox."""
        print(f"\n{self.name}'s Inbox:")
        self.inbox.list_emails()

    def read_email(self, index: int) -> None:
        """Reads email."""
        self.inbox.read_email(index)

    def delete_email(self, index: int) -> None:
        """Deletes email."""
        self.inbox.delete_email(index)

class Inbox:
    """Inbox class."""
    def __init__(self) -> None:
        self.emails: list[Email] = []

    def receive_email(self, email: Email) -> None:
        """Adds email to email list object."""
        self.emails.append(email)

    def list_emails(self) -> None:
        """Displays list of emails."""
        if not self.emails:
            print('Your inbox is empty.\n')
            return
        print('\nYour Emails:')
        for i, email in enumerate(self.emails, start=1):
            print(f'{i}. {email}')

    def read_email(self, index: int) -> None:
        """Displays the email associated with the index."""
        if not self.emails:
            print('Inbox is empty.\n')
            return
        actual_index = index - 1
        if actual_index < 0 or actual_index >= len(self.emails):
            print('Invalid email number.\n')
            return
        self.emails[actual_index].display_full_email()

    def delete_email(self, index: int) -> None:
        """Deletes the email associated with the index."""
        if not self.emails:
            print('Inbox is empty.\n')
            return
        actual_index = index - 1
        if actual_index < 0 or actual_index >= len(self.emails):
            print('Invalid email number.\n')
            return
        del self.emails[actual_index]
        print('Email deleted.\n')

def main() -> None:
    """Execute the primary script logic to run the email demo."""
    tory = User('Tory')
    ramy = User('Ramy')

    tory.send_email(ramy, 'Hello', 'Hi Ramy, just saying hello!')
    ramy.send_email(tory, 'Re: Hello', 'Hi Tory, hope you are fine.')
    ramy.check_inbox()
    ramy.read_email(1)
    ramy.delete_email(1)
    ramy.check_inbox()
if __name__ == '__main__':
    main()
