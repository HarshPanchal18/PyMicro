from flask import Flask, render_template_string, request
import requests
from dotenv import load_dotenv
import os
import logging

load_dotenv()

# Set up logging
logging.basicConfig(
  level=logging.INFO,
  format="%(asctime)s\t[%(levelname)s]\t%(message)s",
  handlers=[logging.StreamHandler()]
)

app = Flask(__name__)

FASTAPI_URL = os.environ.get("FAST_API")
logging.info(FASTAPI_URL)

HTML = """
<!doctype html>
<title>Calculator</title>
<h2>Calculator (calls FastAPI backend)</h2>
<form method="post">
  <input name="a" type="number" step="any" required>
  <select name="op">
  <option value="add">+</option>
  <option value="subtract">-</option>
  <option value="multiply">*</option>
  <option value="divide">/</option>
  </select>
  <input name="b" type="number" step="any" required>
  <button type="submit">Calculate</button>
</form>
{% if result is not none %}
  <h3>Result: {{ result }}</h3>
{% elif error %}
  <h3 style="color:red;">Error: {{ error }}</h3>
{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def index():
  result = None
  error = None
  if request.method == "POST":
    a = request.form.get("a")
    b = request.form.get("b")
    op = request.form.get("op")
    logging.info(f"Received input: a={a}, b={b}, op={op}")
    try:
      a = float(a)
      b = float(b)
      resp = requests.post(
        f"{FASTAPI_URL}/{op}",
        json={"a": a, "b": b},
        timeout=5
      )
      logging.info(f"Sent POST to {FASTAPI_URL}/{op} with a={a}, b={b}")
      if resp.status_code == 200:
        result = resp.json().get("result")
        logging.info(f"Calculation result: {result}")
      else:
        error = resp.json().get("detail", "Unknown error")
        logging.error(f"Backend error: {error}")
    except Exception as e:
      error = str(e)
      logging.exception("Exception during calculation")
  return render_template_string(HTML, result=result, error=error)

if __name__ == "__main__":
  app.run(host="0.0.0.0")
