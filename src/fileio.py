# fileio.py

import csv
import json

def save_as_csv(assignments, filename="assignments.csv"):
    """
    Writes a CSV with headers: Student,Major,Advisor.
    """
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Student", "Major", "Advisor"])
        writer.writerows(assignments)
    print(f"[✅ Saved] {filename}")

def save_as_json(assignments, filename="assignments.json"):
    """
    Writes a JSON list of dicts.
    """
    data = [
        {"student": s, "major": m, "advisor": a}
        for s, m, a in assignments
    ]
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)
    print(f"[✅ Saved] {filename}")