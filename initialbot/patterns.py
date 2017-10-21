from bottery.conf.patterns import Pattern
from bottery.views import pong
from views import hello, greetings


patterns = [
    Pattern('ping', pong),
    Pattern('hello', hello),
    Pattern('olá', greetings)
]
