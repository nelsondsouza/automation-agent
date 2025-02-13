from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Automation Agent API! Use /run or /read endpoints."

@app.route('/run', methods=['POST'])
def run_task():
    task = request.args.get('task')
    
    if task == "install_uv_and_run_script":
        # Install 'uv' if not already installed
        subprocess.run(["pip", "install", "uv"], check=True)
        
        # Run datagen.py script with an email argument
        email = "example@example.com"  # Replace with actual email if needed
        subprocess.run(["python", "datagen.py", email], check=True)
        
        return jsonify({"message": "UV installed and script executed successfully"}), 200
    
    return jsonify({"message": f"Task '{task}' executed successfully"}), 200

@app.route('/read', methods=['GET'])
def read_file():
    path = request.args.get('path')
    try:
        with open(path, 'r') as file:
            content = file.read()
        return content, 200
    except FileNotFoundError:
        return jsonify({"error": "File not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)