from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "你絕對猜不到下一任高雄市長會是誰的啦!"
if __name__ == '__main__':
    app.run()