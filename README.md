I want to test sending back gzipped data from a Flask app in response to Ajax requests.
The data may get gzipped upstream so I don't want Flask to do it for me.

To get started:

    make    # build the gzipped file
    virtualenv -p python3.4 venv
    source venv/bin/activate
    pip install -r requirements.txt
    python app.py

