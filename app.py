
from flask import Flask, render_template, request, jsonify
import arithmetic

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/calculate', methods=["POST"])
def calculate():
    data = request.get_json() or {}
    print("Received data: ", data)

    operation = data.get("operation")
    a = data.get("a")
    b = data.get("b")

    # coerce numbers where provided
    try:
        if a is not None:
            a = float(a)
        if b is not None:
            b = float(b)
    except Exception as e: 
        return jsonify({"result": f"Error parsing numbers: {e}"})

    result = None
    try:
        if operation == "add":
            result = arithmetic.addition(a, b)
        elif operation == "subtract":
            result = arithmetic.subtraction(a, b)
        elif operation == "multiply":
            result = arithmetic.multiplication(a, b)
        elif operation == "divide":
            result = arithmetic.division(a, b)
        elif operation in ("modulus", "remainder"):
            result = arithmetic.remainder(a, b)
        elif operation == "square":
            result = arithmetic.square(a)
        elif operation in ("square_root", "squareRoot", "sqrt"):
            result = arithmetic.square_root(a)
        elif operation in ("exponentiation", "exponent"):
            result = arithmetic.exponentiation(a, b)
        elif operation == "factorials":
            result = arithmetic.factorials(a)
        elif operation == "sin":
            result = arithmetic.sin(a)
        elif operation == "cos":
            result = arithmetic.cos(a)
        elif operation == "tan":
            result = arithmetic.tan(a)
        else:
            result = "Unsupported operation"
    except Exception as e:
        result = f"Error: {e}"

    return jsonify({"result": result})

                        
if __name__ == "__main__":
    app.run(debug=True)