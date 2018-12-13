# node-python image-classification

Serve your Fast.ai Python application using Node.js.

## Setup

1. Make sure you can import all the necessary Fast.ai libraries from the root folder of this project.
2. Install *zerorpc*: `pip install zerorpc`.
3. Install Node.js dependencies: `npm install`.

## Run

1. Create a *data* folder inside the project root. And download/copy your dataset inside it. (Here's the link to the DogsCats dataset: http://files.fast.ai/data/dogscats.zip)
2. You may use `dogscats.ipynb` to train your model.
3. Edit `config.py` and set your `PATH`, and `model` variables.
4. `npm start` to start the server.
5. Load *localhost:3030* on your browser.
