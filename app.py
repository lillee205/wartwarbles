from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# This list will contain all my warbles/tweets! I can later use this to "load" them into the page
warbleList = []

@app.route('/', methods=["POST", "GET"])
def index():
    global warbleList
    if request.method == "POST" and request.form.get("msg") != "":
        newWarble = {
            "author": "wart_is_law", #for now, we'll just say every author is wally :)
            "msg" : request.form.get("msg") if random.random() <= 0.75 else pig_translate(request.form.get("msg"))
        }
        warbleList.append(newWarble)
        return redirect(url_for('index'))
    return render_template("index.html", warbleList = warbleList) #then, I will pass in my warbleList into the rendering of the HTML pg

def pig_translate(S):
    retStr = ''
    V = ['a','A','e','E','i','I','o','O','u','U']
    currFront = S[0]
    seen_vowel = False
    for i in range(len(S)):
        if S[i] == ' ':
            if currFront in V:
                retStr += 'yay '
            else:
                retStr += currFront.lower() + 'ay '
        elif i == len(S)-1:
            if currFront in V:
                retStr += S[i]+ 'yay'
            else:
                retStr += S[i] + currFront.lower() + 'ay'
        else:
            if S[i-1] == ' ' or i == 0:
                seen_vowel = False
                currFront = S[i]
                if currFront in V:
                    retStr += S[i]
                    seen_vowel = True
            else:
                if S[i] in V:
                    seen_vowel = True
                    retStr += S[i]
                else:
                    if not seen_vowel:
                        currFront += S[i]
                    else:
                        retStr += S[i]
    return retStr

if __name__ == "__main__":
    app.run(debug = True)

