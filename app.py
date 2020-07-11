
from flask import Flask, request, render_template, Response, jsonify
from model import URLForm
from flask_bootstrap import Bootstrap
import sys
from time import sleep
from subprocess import Popen, PIPE, STDOUT, DEVNULL
from textwrap import dedent
app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY=b'\xd6\x04\xbdj\xfe\xed$c\x1e@\xad\x0f\x13,@G')
Bootstrap(app)
app.debug = True

convert =False
Done = True

def stream_template(template_name, **context):
    app.update_template_context(context)
    t = app.jinja_env.get_template(template_name)
    rv = t.stream(context)
    rv.disable_buffering()
    return rv


def generate(form):
    with Popen([sys.executable or 'python3', '-u', '-c', dedent(f"""\
        # dummy subprocess
        from bookhack_ikoblyk.test import Work
        w = Work('{form}', '/app/books')
        w.run()
        """)], stdin=DEVNULL, stdout=PIPE, stderr=STDOUT,
               bufsize=1, universal_newlines=True) as p:
        for line in p.stdout:
            yield str(line)
            sleep(0.5)

@app.route('/', methods=['GET', 'POST'])
def registration():
    form = URLForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        form_2 = form.url.data
        rows = generate(form_2)
        return Response(stream_template('wait.html', rows=rows))
    else:
        return render_template('registration.html', form=form)



@app.route('/donate', methods=['GET', 'POST'])
def donate():
    return render_template('donate.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')

@app.route('/converting', methods=['POST'])
def converting():
    return jsonify({
        'state': 'converting',
    })



if __name__ == '__main__':
    app.run(host='0.0.0.0')


