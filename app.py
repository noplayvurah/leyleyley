from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = 'ley-love-game-secret-2026'

QUESTIONS = {
    'start': {
        'prompt': 'hi baby do you love me?',
        'yes': 'gift_offer',
        'no': 'sad_bunny'
    },
    'gift_offer': {
        'prompt': 'aawww i love you want to open a gift i got you? :-)',
        'yes': 'memory_game',
        'no': 'sad_bunny'
    },
    'memory_game': {
        'prompt': 'match the cards to see ur gift',
        'game': True,
        'bunny': 'happy'
    },
    'sad_bunny': {
        'prompt': ':( ',
        'end': True,
        'bunny': 'sad'
    }
}


@app.route('/', methods=['GET'])
def index():
    session['current'] = 'start'
    node = QUESTIONS['start']
    return render_template(
        'leyan.html',
        prompt=node['prompt'],
        end=False,
        bunny_state='normal',
        game_mode=False
    )


@app.route('/answer', methods=['POST'])
def answer():
    choice = request.form.get('answer')
    if choice == 'restart':
        session['current'] = 'start'
        node = QUESTIONS['start']
        return render_template(
            'leyan.html',
            prompt=node['prompt'],
            end=False,
            bunny_state='normal',
            game_mode=False
        )

    current = session.get('current', 'start')
    node = QUESTIONS.get(current, QUESTIONS['start'])
    next_key = node.get(choice)
    if not next_key or next_key not in QUESTIONS:
        next_key = 'start'

    session['current'] = next_key
    next_node = QUESTIONS[next_key]
    bunny_state = next_node.get('bunny', 'normal')
    game_mode = next_node.get('game', False)

    return render_template(
        'leyan.html',
        prompt=next_node['prompt'],
        end=next_node.get('end', False),
        bunny_state=bunny_state,
        game_mode=game_mode
    )


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
