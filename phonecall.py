from twilio.rest import Client

account_sid = 'AC9958d44b511b28f26d3c6a0ac56e9a2b' 
auth_token = 'ffadc7fa15dba1e7151037e52718827e' 
client = (account_sid, auth_token)
call = client.calls.create(
twiml = '<Response><Say>Hello this is Dheirya Mehta</Say></Response>',
to='+917708226575',
from_= '+12056563442'
)
print(call.sid)