import pytest
from checker.mail import MailBox

@pytest.mark.MailBox
def test_init_with_clean_input():
    host = 'test.mail.server'
    principal = 'test@mail.com'
    credentials = 'testpassword@1'
    
    mail_box = MailBox(host, principal, credentials)
