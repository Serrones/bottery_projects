from bottery.conf.patterns import Pattern, DefaultPattern
from bottery.views import pong
from views import hello, hello_world, not_found




patterns = [
    Pattern('ping', pong),
    Pattern('hi bot', hello),
    Pattern('hello', hello_world),
    DefaultPattern(not_found),
]
