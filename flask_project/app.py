from flask import Flask, jsonify
from db import get_db_session
import random

app = Flask(__name__)

@app.route("/health")
def health_check():
    return jsonify({"status": "ok"})

@app.route("/get_graph", methods=["GET"])
def get_graph():
    return jsonify({"graph": "stub"})

@app.route("/update_power", methods=["POST"])
def update_power():
    with get_db_session() as session:
        result = session.run("MATCH (d:Device) RETURN d.device_id AS device_id, d.power_rating_watts AS power_rating")
        updated_devices = []
        for record in result:
            new_power = round(record["power_rating"] * (1 + random.uniform(-0.1, 0.1)))
            session.run(
                "MATCH (d:Device {device_id: $device_id}) SET d.power_rating_watts = $new_power",
                device_id=record["device_id"],
                new_power=new_power
            )
            updated_devices.append({"device_id": record["device_id"], "power_rating_watts": new_power})
    return jsonify({"updated_devices": updated_devices})

@app.route("/get_history", methods=["GET"])
def get_history():
    return jsonify({"history": []})

@app.route("/restore_snapshot", methods=["POST"])
def restore_snapshot():
    return jsonify({"restored": "stub"})

if __name__ == "__main__":
    app.run(debug=True)