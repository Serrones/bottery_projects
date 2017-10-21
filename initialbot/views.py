from bottery.message import render

def hello(message):
    return "Hello World!!"

def greetings(message):
    return render(message, 'hello.md')

def not_found(message):
    return "Sorry, I can't understand what you're saying :("
