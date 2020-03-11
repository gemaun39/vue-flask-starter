from flask import Flask, jsonify
from flask_cors import CORS
import re
import random

app = Flask(__name__)
CORS(app) # avoid Cross-Origin Resource Sharing (CORS) errors

# Declare routes by following the examples below
@app.route('/')
def index():
    return "Hello, World!" # return this data to the client

@app.route('/api/v1.0/shakespeare', methods=['GET'])
def get_shakespeare():
    
    txt = ""
    with open ("shakespeare.txt", "r") as myfile:
        txt=myfile.read()
    print("Performing Regex")
    my_list1 = re.findall(r"[\w]+|[.,!?;\"]", txt)
    list_no_repeats = list(dict.fromkeys(my_list1)) #no repeats
    tree = {}
    print("Adding to tree")
    for i in range(len(list_no_repeats)):
        tree.update({list_no_repeats[i]: []})
    length = len(my_list1)
    print("Appending tree, " + str(length) + " words in corpus")
    count = 0
    period_count = 0
    for i in range(length):
        key = tree[my_list1[i]]
        if (i+1) < length:
            key.append(my_list1[i+1])
    capital_list = re.findall('([A-Z][a-z]+|[A-Z])', txt)
    starting_word = random.choice(capital_list)
    new_text = starting_word + " "
    for i in range(500):
        word = tree[starting_word][random.randint(0, len(tree[starting_word]) - 1)]
        new_text = new_text + word + " "
        starting_word = word
        if starting_word == ".":
            period_count += 1
        if period_count == 12:
            break
    new_text = re.sub(r'\s([?.!,;](?:\s|$))', r'\1', new_text)
    print(new_text)
    return jsonify({'message': new_text})

if __name__ == '__main__':
    app.run(debug=True)