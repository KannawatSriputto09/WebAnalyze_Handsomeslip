from flask import Flask, render_template ,request
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/main', methods = ["POST", "GET"])
def main():
    lis_s = []
    lis_t = []
    count = 1
    if request.method == "POST":
        for _ in range(4):
            first_subject = request.form.get(f"subject{str(count)}")
            first_cals = request.form.get(f"cal{str(count)}")
            if count > 4 :
                break
            else:
                lis_s.append(first_subject)
                lis_t.append(int(first_cals))
                count = count + 1
        plt.xlabel("subject")
        plt.ylabel("total")
        plt.ylim(0, 100)
        plt.bar(lis_s,lis_t)
        plt.savefig('static/new_plot.png')
        return render_template('main.html', plot_url ='static/new_plot.png')
    else:
        return render_template('main.html')

# @app.route('/login')
# def login():
#     return render_template('login.html')