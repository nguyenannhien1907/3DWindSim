"""
Ung dung Flask: tinh tai trong gio TCVN 2737:2023 o phia server (Python),
tra ve JSON cho trang web ve 3 toa nha 3D (Three.js) o phia trinh duyet.

Chay:  python app.py
Mo:    http://127.0.0.1:5000
"""
from flask import Flask, render_template, request, jsonify
import numpy as np

app = Flask(__name__)

SHAPES = [
    {"key": "square", "label": "Square", "c": 1.40, "color": "#b4432f"},
    {"key": "chamfer", "label": "Chamfer 10-15%", "c": 1.10, "color": "#1c7293"},
    {"key": "round", "label": "Round", "c": 0.95, "color": "#2c6e3f"},
]
TERRAIN = {"A": (0.12, 250.0), "B": (0.16, 300.0), "C": (0.22, 400.0)}
B_WIDTH = 30.0       # be rong don gio (m)
H_FLOOR = 3.5        # chieu cao moi tang (m)
K_STORY = 3.5e5      # do cung moi tang (kN/m)


def build_stiffness(n):
    """Lap ma tran do cung [K] - tam duong cheo (xem Buoc 6 buoi truoc)."""
    K = np.zeros((n, n))
    for i in range(n):
        if i == n - 1:
            K[i, i] = K_STORY
        else:
            K[i, i] = 2 * K_STORY
            K[i, i + 1] = -K_STORY
            K[i + 1, i] = -K_STORY
    return K


def compute_all(w0: float, terrain_key: str, num_floors: int) -> dict:
    """Tinh toan toan bo vat ly cho 3 phuong an hinh khoi - dung lai simulate.py."""
    alpha, zg = TERRAIN.get(terrain_key, TERRAIN["B"])
    floors = np.arange(1, num_floors + 1)
    z = floors * H_FLOOR
    k_z = 2.01 * (np.maximum(z, 3.0) / zg) ** (2 * alpha)
    K = build_stiffness(num_floors)

    results = {}
    for shape in SHAPES:
        p = w0 * k_z * shape["c"]                 # ap luc gio (kPa)
        F = p * (B_WIDTH * H_FLOOR)                # luc gio tung tang (kN)
        u = np.linalg.solve(K, F) * 1000            # chuyen vi ngang (mm)
        results[shape["key"]] = {
            "p": p.tolist(),
            "u": u.tolist(),
            "baseShear": float(F.sum()),
            "topDisp": float(u[-1]),
        }

    return {
        "z": z.tolist(),
        "hFloor": H_FLOOR,
        "numFloors": num_floors,
        "shapes": SHAPES,
        "results": results,
    }


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/simulate")
def api_simulate():
    """vi du: /api/simulate?w0=1.25&terrain=B&floors=30"""
    try:
        w0 = float(request.args.get("w0", 1.25))
        terrain = request.args.get("terrain", "B").upper()
        floors = int(request.args.get("floors", 30))
    except ValueError:
        return jsonify({"error": "Tham số không hợp lệ"}), 400

    if terrain not in TERRAIN:
        return jsonify({"error": "Dạng địa hình phải là A, B hoặc C"}), 400
    if not (5 <= floors <= 60):
        return jsonify({"error": "Số tầng phải trong khoảng 5–60"}), 400

    return jsonify(compute_all(w0, terrain, floors))


if __name__ == "__main__":
    app.run(debug=True, port=5000)
