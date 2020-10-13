from flask import Flask, request, render_template

app = Flask(__name__, )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['GET', 'POST'])
def send():
    if request.method == "POST":
      attempted = request.form['attempted']
      print('New user with phone: '+attempted)
      return render_template('access.html')
    else:
      return render_template('error.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1024)
