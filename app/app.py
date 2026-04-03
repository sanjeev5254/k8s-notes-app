from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    app_name = os.getenv("APP_NAME", "Notes App")
    app_env = os.getenv("APP_ENV", "development")
    app_password = os.getenv("APP_PASSWORD", "not-set")

    return f"""
    <h1>{app_name}</h1>
    <p>Environment: {app_env}</p>
    <p>Password loaded from Secret: {app_password}</p>
    <p>Kubernetes project is working!</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)