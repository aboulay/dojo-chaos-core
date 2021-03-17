import os

import core_types.anger_core as anger_core
import core_types.curiosity_core as curiosity_core
import core_types.intelligence_core as intelligence_core
import core_types.morality_core as morality_core

from flask import Flask, request, Response, jsonify
app = Flask(__name__)

def initialize_external_core():
    print("Core Initialization:")
    if os.environ.get("CORE_TYPE") is None:
        raise Exception("Invalid Core Type")
    switch={
        "ANGER":anger_core.AngerCore(),
        "CURIOSITY":curiosity_core.CuriosityCore(),
        "INTELLIGENCE":intelligence_core.IntelligenceCore(),
        "MORALITY":morality_core.MoralityCore()
    }
    print("Core initialized: {0}".format(os.environ.get("CORE_TYPE")))
    core = switch.get(os.environ.get("CORE_TYPE"), "Error: Unknown type.")
    return core

core = initialize_external_core()

@app.route('/')
def myapp():
    message = {"sentence": core.get_sentence() }
    return jsonify(message)

@app.route('/ping')
def healthcheck():
    return "Core Status: Healthy"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.environ.get("PORT", 5000))