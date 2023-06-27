from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_geek():
    return '<h1>Hello from Flask, Docker & Kubernetes</h2>'

# Health check route
@app.route('/health')
def health_check():
    return 'OK', 200

if __name__ == "__main__":
    app.run(debug=True)



