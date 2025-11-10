from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/calculate', methods=["POST"])
def calculate():
    data = request.getjson()
    operation = data["operation"]
    a = float(data.get("a", 0))
    b = float(data.get("b", 0))

    try:
        if operation == "add":
            resutl = calculate.addition()
        elif operation == "subtract":
            result = calculate.subtraction()
        elif operation == "multiply":
            result = calculate.multiplication()
        elif operation == "divide":
            result = calculate.division()
        elif operation == "modulus":
            result = calculate.remainder()
        elif operation == "square":
            result = calculate.square()
        elif operation == "square_root":
            result = calculate.square_root()
        elif operation == "exponentiation":
            result = calculate.exponentiation()
        elif operation == "factorials":
            result = calculate.factorials()
        elif operation == "sin":
            result = calculate.sin()
        elif operation == "cos":
            result = calculate.cos()
        elif operation == "tan":
            result = calculate.tan()
    except Exception as e:
        result = f"Error: {e}"

                        
if __name__ == "__main__":
    app.run(debug=True)