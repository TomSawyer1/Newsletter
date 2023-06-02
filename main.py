from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def newsletter():
    # Données de la newsletter
    titre = "Ma Newsletter"
    articles = [
        {
            'titre': "Article 1",
            'contenu': "Ceci est le contenu de l'article 1."
        },
        {
            'titre': "Article 2",
            'contenu': "Ceci est le contenu de l'article 2."
        },
        {
            'titre': "Article 3",
            'contenu': "Ceci est le contenu de l'article 3."
        }
    ]
        #Juste pour voir !!!!
    # Rendu du template HTML
    return render_template('newsletter.html', titre=titre, articles=articles)

if __name__ == '__main__':
    app.run()