from bottery.conf.patterns import Pattern, DefaultPattern
from bottery.views import pong
from views import hello, greetings, not_found


patterns = [
    Pattern('ping', pong),
    Pattern('hello', hello),
    Pattern('olá', greetings),
    DefaultPattern(not_found),
]
