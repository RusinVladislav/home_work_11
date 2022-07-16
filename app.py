from flask import Flask, render_template
from utils import load_candidates, get_candidate, get_candidates_by_skill, get_candidates_by_name


app = Flask(__name__)

all_candidates = load_candidates()


@app.get("/part1/")
def page_part1():
    return render_template('part1.html')


@app.get("/")
@app.get("/main/")
def page_main():
    return render_template('main.html')


@app.get("/candidates/")
def page_candidates():
    return render_template('candidates.html', candidates=all_candidates)


@app.get("/candidate/<int:uid>/")
def page_candidate(uid):
    candidate = get_candidate(uid, all_candidates)
    if type(candidate) == str:
        return candidate
    else:
        return render_template('candidate.html', candidate=candidate)


@app.get("/skills/<skill>/")
def page_skills(skill):
    candidates = get_candidates_by_skill(skill, all_candidates)
    if type(candidates) == str:
        return candidates
    else:
        counter = len(candidates)
        return render_template('skill.html', skill=skill, candidates=candidates, counter=counter)


@app.get("/names/<name>/")
def page_names(name):
    candidates = get_candidates_by_name(name, all_candidates)
    if type(candidates) == str:
        return candidates
    else:
        counter = len(candidates)
        return render_template('name.html', name=name, candidates=candidates, counter=counter)


app.run(debug=True)
