from getpass import getpass
from imaplib import IMAP4_SSL
import imaplib
import logging


class LoginError(Exception):
    def __init__(self, username: str) -> None:
        msg = f'Unable to login for {username}'
        super().__init__(msg)


class MailBox(object):
    def __init__(
        self,
        host: str,
        user: str,
        password: str,
        logger: logging.Logger
    ) -> None:
        self._log = logger.getChild(MailBox.__name__)
        self._log.info(f'Connecting to IMAP host: {host}')
        self._client: IMAP4_SSL = IMAP4_SSL(host)
        self._log.info(f'Logging in for {user}')
        try:
            self._client.login(user, password)
        except imaplib.IMAP4.error as err:
            self._log.error(err)
            raise LoginError(username)


if __name__ == '__main__':
    logging.basicConfig(level='INFO')
    log = logging.getLogger('root').getChild('checker')
    host = input('IMAP host: ')
    username = input('Email address: ')
    password = getpass('Email password: ')

    mb = MailBox(host, username, password, log)
