from flask import Flask, render_template
app = Flask(__name__)
import config
@app.route("/")
def index():
  return render_template('dashboard.html')

if __name__ == "__main__":
  app.run(port=config.PORT, debug=config.DEBUG_MODE)