import logging


import trueskill
from configobj import ConfigObj
import os

LOBBY_IP = os.getenv('LOBBY_IP', '37.58.123.3')
LOBBY_UDP_PORTS = [int(port) for port in os.getenv('LOBBY_UDP_PORTS', '7,53,67,80,123,194,547,3478,3535,6112,30351').split(',')]
LOBBY_NAT_ADDRESSES = list(map(lambda p: ('0.0.0.0', p), LOBBY_UDP_PORTS))

logging.getLogger('aiomeasures').setLevel(logging.INFO)

logging.getLogger().setLevel(logging.DEBUG)

trueskill.setup(mu=1500, sigma=500, beta=250, tau=5, draw_probability=0.10)

STATSD_SERVER = os.getenv('STATSD_SERVER', '127.0.0.1:8125')

RULE_LINK = 'http://forums.faforever.com/forums/viewtopic.php?f=2&t=581#p5710'
WIKI_LINK = 'http://wiki.faforever.com'
APP_URL = 'http://app.faforever.com'
CONTENT_URL = 'http://content.faforever.com'
CONTENT_PATH = '/content/'  # Must have trailing slash

SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.mandrillapp.com")
SMTP_PORT = os.getenv("SMTP_PORT", 587)
SMTP_USERNAME = os.getenv("SMTP_USERNAME", "admin@faforever.com")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD", "")

MANDRILL_API_KEY = os.getenv("MANDRILL_API_KEY", '')
MANDRILL_API_URL = os.getenv("MANDRILL_API_URL", 'https://mandrillapp.com/api/1.0')

VERIFICATION_HASH_SECRET = os.getenv("VERIFICATION_HASH_SECRET", "")
VERIFICATION_SECRET_KEY = os.getenv("VERIFICATION_SECRET_KEY", "")
