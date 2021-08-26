from flask_app import app
from flask import render_template, redirect, request, session, flash, jsonify
from flask_app import data 

@app.route('/')
def index():
    if 'page_head' in session:
        if session['page_head'] != 'home':
            if 'invincible' in session:
                session.pop('invincible')
    session['page_head'] = 'home'
    session['page'] = 'home'
    session['page_type'] = 'base'
    context = {
        'about_me': data.about_me,
        'all_tech': data.tech,
        'all_edu': data.edu,
    }
    return render_template('home.html', **context)

@app.route('/edu')
def edu():
    session['page_head'] = 'edu'
    session['page'] = 'edu'
    session['page_type'] = 'index_page'
    context = {
        'all_edu': data.edu
    }
    return render_template('edu.html', **context)

@app.route('/edu/<int:edu_id>')
def show_edu(edu_id):
    session['page_head'] = 'education'
    session['page'] = f'education {edu_id}'
    session['page_type'] = 'detail_page'
    context = {
        'edu': data.edu[edu_id]
    }
    return render_template('edu_show.html', **context)

@app.route('/jobs')
def jobs():
    session['page_head'] = 'jobs'
    session['page'] = 'jobs'
    session['page_type'] = 'index_page'
    context = {
        'all_jobs': data.jobs
    }
    return render_template('jobs.html', **context)

@app.route('/job/<int:job_id>')
def show_job(job_id):
    session['page_head'] = 'jobs'
    session['page'] = f'job {job_id}'
    session['page_type'] = 'detail_page'
    context = {
        'job': data.jobs[job_id]
    }
    return render_template('job_show.html', **context)

@app.route('/projects')
def projects():
    session['page_head'] = 'projects'
    session['page'] = 'projects'
    session['page_type'] = 'index_page'
    context = {
        'all_projects': data.projects
    }
    return render_template('projects.html', **context)

@app.route('/project/<int:project_id>')
def show_project(project_id):
    session['page_head'] = 'projects'
    session['page'] = f'project {project_id}'
    session['page_type'] = 'detail_page'
    context = {
        'project': data.projects[project_id]
    }
    return render_template('project_show.html', **context)

@app.route('/contact_me')
def contact_me():
    session['page_head'] = 'contact me'
    session['page'] = 'contact me'
    session['page_base'] = 'base'

    context = {
        'about_me': data.about_me
    }

    return render_template('contact_me.html', **context)

@app.route('/about_me')
def about_me():
    session['page_head'] = 'about me'
    session['page'] = 'about me'
    session['page_base'] = 'base'
    context = {
        "about_me": data.about_me
    }
    return render_template('about_me.html', **context)

@app.route('/invincible')
def invincible():
    session['invincible'] = True
    return redirect('/')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return 'page not found'