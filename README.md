# Password Strength Analyzer

## Overview

Password Strength Analyzer is a web-based cybersecurity tool that evaluates the security level of a password. The application analyzes various password characteristics and provides users with feedback and recommendations to create stronger passwords.

This project was developed as part of a Cyber Security Internship to demonstrate fundamental security concepts, input validation, and secure password practices.

## Features

* Password length verification
* Uppercase letter detection
* Lowercase letter detection
* Numeric character detection
* Special character detection
* Common password identification
* Password strength scoring
* Security improvement suggestions
* User-friendly web interface

## Tech Stack

* Python
* Flask
* HTML5
* CSS3
* Bootstrap
* Regular Expressions (Regex)

## Project Structure

```text
Password-Strength-Analyzer/
│
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── requirements.txt
└── README.md
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Swathi2504/Password-strength-Analyzer.git
```

### 2. Navigate to the Project Directory

```bash
cd Password-Strength-Analyzer
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python app.py
```

### 5. Open in Browser

```text
http://127.0.0.1:5000
```

## Password Evaluation Criteria

The analyzer checks the following security parameters:

* Password length (minimum recommended length)
* Presence of uppercase letters
* Presence of lowercase letters
* Presence of numeric digits
* Presence of special characters
* Detection of commonly used weak passwords

## Sample Results

| Password     | Result |
| ------------ | ------ |
| password     | Weak   |
| Password123  | Medium |
| P@ssword123! | Strong |

## Security Concepts Demonstrated

* Password policy enforcement
* Secure password creation practices
* Input validation
* Pattern matching using Regular Expressions
* Basic cybersecurity awareness

## Learning Outcomes

Through this project, the following skills were practiced:

* Python programming
* Flask web development
* Regex pattern matching
* Cybersecurity fundamentals
* Front-end integration
* User input validation

## Future Enhancements

* Password entropy calculation
* Dark mode support
* Password breach database integration
* Password history analysis
* Advanced security recommendations

## License

This project is created for educational purposes as part of the Decode Labs Cybersecurity Internship. Feel free to use and modify the code for academic and personal projects.

