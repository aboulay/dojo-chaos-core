import os
import requests
import random
import json

from flask import Flask, request, make_response, render_template
app = Flask(__name__)

class ExternalCore:
    def __init__(self, name, service_url):
        self.name = name
        self.service_url = service_url
    
    def get_name(self):
        return self.name

    def get_service_url(self):
        return self.service_url
    
    def check_health(self):
        try:
            print("Healthcheck Status for Core {0}:".format(self.name))
            r = requests.get("http://{0}/ping".format(self.service_url))
            if r.status_code != 200:
                print("  > Failure")
                return False
        except:
            print("  > Failure")
            return False
        else:
            print("  > OK")
            return True

    def get_sentence(self):
        try:
            r = requests.get("http://{0}/".format(self.service_url))
            return json.loads(r.content)
        except:
            print("Warning: Unhealthy Core detected.")
            return {"sentence": "Error: Unhealthy core {0} detected".format(self.name)}


def initialize_main_core():
    print("Initialize Main Core:")
    print("  > Status Ready")

def initialize_external_core():
    core_list = []
    print("Initialize External Core Connexion:")
    for external_core_name in ["MORALITY", "CURIOSITY", "INTELLIGENCE", "ANGER"]:
        if os.environ.get("{0}_CONNECTOR".format(external_core_name)) is not None:
            core = ExternalCore(external_core_name, os.environ.get("{0}_CONNECTOR".format(external_core_name)))
            core_list.append(core)
            print("""{0}:
  > Status: Linked
  > Targeting url: {1}""".format(core.get_name(), core.get_service_url()))
        else:
            print("{0}: No Core detected".format(external_core_name))
    return core_list

def retrieve_external_core_status(core_list):
    error_code = 200
    core_status = []
    for core in core_list:
        if core.check_health() is False:
            core_status.append((core.get_name(), False))
            error_code = 417
        else:
            core_status.append((core.get_name(), True))
    return core_status, error_code

def populate_sentence(core_list):
    if len(core_list) == 0:
        print("Warning: No core on the list. Aborting")
    choice = random.choice(core_list)
    print("Generating a new chat dialogue from Core {0}".format(choice.get_name()))
    sentence = choice.get_sentence()
    sentence_list.append(sentence["sentence"])

sentence_list = []
initialize_main_core()
core_list = initialize_external_core()

@app.route('/')
def myapp():
    populate_sentence(core_list)
    return render_template('index.html', sentence_list=sentence_list)

@app.route('/healthz')
def healthcheck():
    return render_template('healthz.html')

@app.route('/status')
def readinesscheck():
    core_status, error_code = retrieve_external_core_status(core_list)
    if error_code == 417:
        print("Warning: Core offline detected. Waiting for it return to continue tests")
    return make_response(render_template('status.html', core_status=core_status), error_code)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.environ.get("PORT", 5000))