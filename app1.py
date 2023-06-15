from flask import Flask

app1 = Flask(__name__)

# @app1.route('/')
# def hello():
#     return 'Hello, World!'

# if __name__ == '__main__':
#     app1.run()


@app1.route("/<query>")
def return_links(query):
    q_terms = [term.lower() for term in query.strip().split()]
    return jsonify(calc_docs_sorted_order(q_terms)[:20:])


@app1.route("/", methods=['GET', 'POST'])
def home():
    form = SearchForm()
    results = []
    if form.validate_on_submit():
        query = form.search.data
        q_terms = [term.lower() for term in query.strip().split()]
        results = calc_docs_sorted_order(q_terms)[:20:]
    return render_template('index.html', form=form, results=results)

app1.run()