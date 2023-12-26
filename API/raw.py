from __future__ import print_function

import requests
import time
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint

configuration = sib_api_v3_sdk.Configuration()
configuration.api_key[
    'api-key'] = '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'

api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))
subject = "My Subject"
html_content = "<html><body><h1>This is my first transactional email </h1></body></html>"
sender = {"name": "dsg", "email": "dayasagar.ghodake@lenditt.com"}
to = [{"email": "dayasagar.ghodake@lenditt.com", "name": "dsg2"}]
cc = [{"email": "example2@example2.com", "name": "Janice Doe"}]
bcc = [{"name": "John Doe", "email": "example@example.com"}]
reply_to = {"email": "dayasagar.ghodake@lenditt.com", "name": "John Doe"}
headers = {"Some-Custom-Name": "unique-id-1234"}
params = {"parameter": "My param value", "subject": "New Subject"}
send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(to=to, bcc=bcc, cc=cc, reply_to=reply_to, headers=headers,
                                               html_content=html_content, sender=sender, subject=subject)

try:
    api_response = api_instance.send_transac_email(send_smtp_email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)
