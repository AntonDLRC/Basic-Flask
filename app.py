from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    names = ["Anton", "Nik", "Muricio", "Malacai", "William", "Harrison"]
    return render_template('index.html', names=names) 

if __name__ == '__main__':
    app.run(debug=True, port=5090)

