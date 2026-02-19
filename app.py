from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Logic to handle registration (data can be stored in a list/dict)
        return render_template('success.html')
        return render_template('register.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)