from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>BNSP System Integrator</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; }
            .container { max-width: 800px; margin: 0 auto; }
            .status { color: green; font-weight: bold; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 BNSP System Integrator Project</h1>
            <p class="status">✅ Aplikasi berhasil di-deploy dengan Docker + CI/CD + Monitoring</p>
            <p><strong>Teknologi yang digunakan:</strong></p>
            <ul>
                <li>Docker Containerization</li>
                <li>AWS VPC + EC2</li>
                <li>CI/CD dengan GitHub Actions</li>
                <li>Monitoring: Prometheus + Grafana</li>
            </ul>
            <p><em>Server: {}</em></p>
        </div>
    </body>
    </html>
    '''.format(os.getenv('HOSTNAME', 'Unknown'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)