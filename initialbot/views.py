from bottery.message import render

def hello(message):
    return "Hello World!!"

def greetings(message):
    return render(message, 'hello.md')
