from flask import Flask
import endpoint
import ai

ai.init_genai_client()

app = Flask(__name__)

endpoint.register(app)
app.run("0.0.0.0", "3378", debug=True)
