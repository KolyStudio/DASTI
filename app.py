from flask import Flask, request, jsonify
import g4f

app = Flask(__name__)

g4f.debug.logging = True  # Enable logging
g4f.check_version = False  # Disable automatic version checking

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        content = request.json['content']
        response = g4f.ChatCompletion.create(
            model=g4f.models.gpt_4,
            messages=[{"role": "user", "content": content}],
        )

        # Ajoutez des messages de journalisation pour le débogage
        print("Début de la fonction chat()")
        
        # Afficher la réponse dans la console
        print("Réponse de l'API:", response)
        
        # Renvoyer la réponse sous forme de dictionnaire JSON avec la clé 'response'
        return jsonify({"response": response})
    except Exception as e:
        print("Erreur dans la fonction chat():", str(e))
        return jsonify({"error": str(e)})



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)