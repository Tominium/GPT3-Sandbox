'''
Create a flask app that has a textbox and a button. When the button is clicked, the text in the textbox is sent to the OpenAI API and the response is displayed on the page.
'''
from flask import Flask, render_template, request
from gpt import GPT, Example
import openai

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    prompt = request.form['prompt']
    openai.api_key = ""
    gpt = GPT(engine="davinci", temperature=0.5, max_tokens=100)
    output = gpt.submit_request(prompt)
    return render_template('index.html', output=output.choices[0].text)

if __name__ == '__main__':
    app.run(debug=True)
