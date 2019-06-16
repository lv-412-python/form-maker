""" app runner """
from formmaker import APP

@APP.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    APP.run(debug=True)
