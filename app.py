from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Welcome to Cloud Native DevOps!</h1>
    <h2>Application Successfully Deployed</h2>
    <p>This application is running inside Docker
    and Kubernetes.</p>
    """

@app.route('/health')
def health():
    return {"status": "healthy"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)