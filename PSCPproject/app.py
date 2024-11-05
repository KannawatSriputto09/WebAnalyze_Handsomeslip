from flask import Flask, render_template ,request
import matplotlib.pyplot as plt
import os
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/main', methods=["POST", "GET"])
def main():
    lis_s = request.form.getlist('subject[]')
    lis_t = request.form.getlist('cal[]')
    if request.method == "POST":
        try:
            lis_t = [int(cal) for cal in lis_t if cal.isdigit() and 0 <= int(cal) <= 100]
        except ValueError:
            return "กรุณากรอกคะแนนเป็นตัวเลขในช่วง 0-100", 400
        plt.clf()
        plt.xlabel("Subject")
        plt.ylabel("Total")
        plt.ylim(0, 100)
        plt.bar(lis_s, lis_t)
        os.makedirs('static', exist_ok=True)
        plt.savefig('static/new_plot.png')
        return render_template('main.html', plot_url='static/new_plot.png')
    return render_template('main.html')
