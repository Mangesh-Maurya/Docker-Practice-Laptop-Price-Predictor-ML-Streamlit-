from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def table():
    table_data = []
    number = None

    if request.method == 'POST':
        try:
            number = int(request.form['number'])
            table_data = [f"{number} x {i} = {number * i}" for i in range(1, 11)]
        except ValueError:
            table_data = ["Invalid input. Please enter a valid number."]

    return render_template('index.html', table=table_data, number=number)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
p