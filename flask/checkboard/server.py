from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/<int:num>')
def change_num(num):
    return render_template("index.html",num = num)

@app.route('/<int:num>/<int:num2>')
def change_num2(num,num2):
    return render_template("index.html", num=num ,num2 = num2)

# @app.route('/<int:num>/<int:num2>/<color1>/color2')
# def change_num2(num,num2,color1,color2):
#     return render_template("index.html", num=num ,num2 = num2)

if __name__ == '__main__':
    app.run(debug = True)