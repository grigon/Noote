from flask import Flask, request, render_template, redirect, url_for
import data_manger

app = Flask(__name__)
notes = {}
# path = os.path.dirname("flask-note-grigon")
path = app.root_path


@app.route('/')
def main_page():
    notes = data_manger.get_notes()

    return render_template('main.html', notes=notes)

# @app.route('/edit/<note>')
# def note(note=None):
#     return render_template("add_note_form.html.html", note=note)

@app.route('/delete/<note_id>', methods=['POST', 'GET'])
def delete(note_id):
    data_manger.delete_note(note_id)
    notes = data_manger.get_notes()

    return render_template('main.html', notes=notes)


@app.route('/add_note', methods=['POST', 'GET'])
def add_note():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        data_manger.add_note(title, content)
        notes = data_manger.get_notes()
        return render_template('main.html', notes=notes)

    notes = data_manger.get_notes()
    return render_template('add_note_form.html', notes=notes)


@app.route('/edit_note/<note_id>', methods=['POST', 'GET'])
def edit_note(note_id):
    note_id = int(note_id)
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        data_manger.update_note(note_id, title, content)
        notes = data_manger.get_notes()
        return render_template('main.html', notes=notes)

    note = data_manger.get_note_by_id(note_id)[0]
    return render_template('add_note_form.html', note=note)


if __name__ == '__main__':
    app.run(
        host='127.0.0.1',
        debug=True,
        port=5000

    )
