from flask import Flask, request, jsonify, render_template
import pandas as pd
import random
import time
from sentence_transformers import SentenceTransformer, util

app = Flask(__name__)

df = pd.read_csv("ai_student_grading_dataset.csv")
model = SentenceTransformer("all-MiniLM-L6-v2")

sessions = {}
EXAM_DURATION = 300


def get_remaining_time(session):
    elapsed = time.time() - session["start_time"]
    return max(0, int(EXAM_DURATION - elapsed))


def final_result(session):
    percentage = (session["score"] / 5) * 100

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 75:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    else:
        grade = "Fail"

    return {
        "finished": True,
        "total_score": session["score"],
        "total_marks": 5,
        "percentage": round(percentage, 2),
        "grade": grade
    }


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/start", methods=["POST"])
def start():
    q = df.sample(5).reset_index(drop=True)
    sid = str(random.randint(100000, 999999))

    sessions[sid] = {
        "questions": q.to_dict("records"),
        "index": 0,
        "score": 0,
        "start_time": time.time()
    }

    return jsonify({
        "session_id": sid,
        "question": sessions[sid]["questions"][0]["Question"],
        "time": EXAM_DURATION,
        "index": 0   # ✅ ADDED
    })


@app.route("/resume/<sid>")
def resume(sid):
    if sid not in sessions:
        return jsonify({"error": "invalid"}), 400

    s = sessions[sid]
    remaining = get_remaining_time(s)

    if remaining <= 0 or s["index"] >= 5:
        return jsonify(final_result(s))

    return jsonify({
        "finished": False,
        "question": s["questions"][s["index"]]["Question"],
        "time": remaining,
        "index": s["index"]   # ✅ ADDED
    })


@app.route("/answer", methods=["POST"])
def answer():
    data = request.json
    sid = data["session_id"]
    ans = data["answer"]

    if sid not in sessions:
        return jsonify({"error": "invalid"}), 400

    s = sessions[sid]
    remaining = get_remaining_time(s)

    if remaining <= 0:
        return jsonify(final_result(s))

    q = s["questions"][s["index"]]

    emb1 = model.encode(q["Model_Answer"], convert_to_tensor=True)
    emb2 = model.encode(ans, convert_to_tensor=True)

    sim = util.cos_sim(emb1, emb2).item()

    if sim > 0.75:
        marks = 1
    elif sim > 0.5:
        marks = 0.5
    else:
        marks = 0

    s["score"] += marks
    s["index"] += 1

    if s["index"] >= 5:
        return jsonify(final_result(s))

    return jsonify({
        "finished": False,
        "marks": marks,
        "similarity": round(sim, 2),
        "question": s["questions"][s["index"]]["Question"],
        "time": remaining,
        "index": s["index"]   # ✅ ADDED
    })


if __name__ == "__main__":
    app.run(debug=True)