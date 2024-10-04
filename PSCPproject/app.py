from flask import Flask, render_template ,request
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/', methods = ["POST", "GET"])
def index():
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
                lis_t.append(first_cals)
                count = count + 1
            # sec_subject = request.form.get("subject2")
            # th_subject = request.form.get("subject3")
            # fo_subject = request.form.get("subject4")
        plt.xlabel("total")
        plt.ylabel("subject")
        plt.plot(first_subject, first_cals)
        plt.savefig('/static/img/new_plot.png')
        return render_template('index.html', name = 'new_plot', url ='/static/img/new_plot.png')
    else:
        return render_template('index.html')


# @app.route('/register')
# def register():
#     return render_template('register.html')

# @app.route('/login')
# def login():
#     return render_template('login.html')