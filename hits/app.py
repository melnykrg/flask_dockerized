import socket
from flask import Flask

app = Flask(__name__)


class Hits:
    def __init__(self):
        self._count = 0

    def one_more(self):
        self._count += 1

    def current(self):
        return self._count


hits = Hits()


@app.route('/')
def hello():
    hits.one_more()
    message = 'I have been seen {t} times. My Hostname is: {h} \n'.format(
        t=hits.current(), h=socket.gethostname()
    )
    with open('logs/app.log', 'a') as log:
        log.write(message)
    return str(hits.current())


@app.route('/logs')
def logs():
    with open('logs/app.log', 'r') as log:
        return ''.join(list(map(lambda l: '<p>{l}</p>'.format(l=l), log.readlines())))


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
