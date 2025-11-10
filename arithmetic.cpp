#include <iostream>
#include <cmath>

using namespace std;

double const M_PI = 3.1415;

void Addition() {
    // This function will perform addition of numbers
    double a, b, result;
    cout << "Enter two numbers to add: ";
    cin >> a >> b;
    result = a + b;
    cout << result << endl;
}

void Subtraction() {
    // This function will perform subtraction of numbers
    double a, b, result;
    cout << "Enter two numbers to subtract: ";
    cin >> a >> b;
    result = a - b;
    cout << result << endl;
}

void Multiplication() {
    // This function will perform multiplication of numbers
    double a, b, result;
    cout << "Enter two numbers to multiply: ";
    cin >> a >> b;
    result = a * b;
    cout << result << endl;
}

void Division() {
    // This function will perform division of numbers
    double a, b, result;
    cout << "Enter two numbers to divide: ";
    cin >> a >> b;
    if (b != 0) {
        result = a / b;
        cout << result << endl;
    } else {
        cout << "Error: Division by zero!" << endl;
    }
}

void Remainder() {
    // This function will perform modulus / remainder  of numbers
    int a, b, result;
    cout << "Enter two integers to find modulus(remainder): ";
    cin >> a >> b;
    if (b != 0) {
        result = a % b;
        cout << result << endl;
    } else {
        cout << "Error: Division by zero!" << endl;
    }
}

void Square(){
    // This function will square a number
    double a, result;
    cout << "Enter a number to square: ";
    cin >> a;
    result = a * a;
    cout << result << endl;
}

void SquareRoot(){
    // This function will find the square root of a number
    double a, result;
    cout << "Enter a number to find the square root: ";
    cin >> a;
    if (a >= 0) {
        result = sqrt(a);
        cout << result << endl;
    } else {
        cout << "Error: Cannot compute square root of a negative number!" << endl;
    }
}

void Exponents(){
    // This function will find the exponent of a number
    double base, exp, result;
    cout << "Enter the base and exponent: ";
    cin >> base >> exp;
    result = pow(base, exp);
    cout << result << endl;
}

void Factorials(){
    // This function will find the factorial of a number
    double n, result = 1;
    cout << "Enter a number to find the factorial: ";
    cin >> n;
    if (n < 0 || n != static_cast<int>(n)) {
        cout << "Error: Factorial is not defined for negative numbers or non-integers!" << endl;
        return;
    }
    for (int i = 1; i <= static_cast<int>(n); ++i) {
        result *= i;
    }
    cout << result << endl;
}

void sin(){
    // This function will find the sine of an angle in degrees
    double num, result;
    cout << "Enter an angle in degrees to find the sine: ";
    cin >> num;
    result = sin(num * M_PI / 180.0); // Convert degrees to radians
    cout << result << endl;
}

void cos(){
    // This function will find the cosine of an angle in degrees
    double num, result;
    cout << "Enter an angle in degrees to find the cosine: ";
    cin >> num;
    result = cos(num * M_PI / 180.0); // Convert degrees to radians
    cout << result << endl;
}

void tan(){
    // This function will find the tangent of an angle in degrees
    double num, result;
    cout << "Enter an angle in degrees to find the tangent: ";
    cin >> num;
    result = tan(num * M_PI / 180.0); // Convert degrees to radians
    cout << result << endl;
}



int main() {
    //cout << "hey" << endl;

    return 0;
}

// 8 - sin
// 9 - cos
// 10 - tan