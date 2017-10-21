from bottery.message import render


def hello(message):
    return render(message , 'hello.md')

def hello_world(message):
    return 'Hello World!!'

def not_found(message):
    return "Sorry, I didn't understand you :/"
