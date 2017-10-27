import os
from flask import Flask, request, jsonify
from extract import *
app = Flask('app')



@app.route('/find/', methods=['POST'])
def SignUp():
    file = request.files["file.pdf"]
    customer_id = request.form["customer_id"]
    starting_word = request.form["starting_word"]
    directory = os.path.join("Documents", customer_id)
    if not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)
    filename = os.path.join(directory, "file.pdf")

    handle_uploaded_file(file, filename)
    try:
        main_obj = wordsearch(filename)
        find_number_next_to_random_word = []
        if starting_word != 'no':
             find_number_next_to_random_word.append(main_obj.find_word(starting_word))
        else:
            find_number_next_to_random_word.append('You did not ask for it.')
        result = main_obj.searchBWB()
        return jsonify({'Result' : "File Saved", 'word' :find_number_next_to_random_word[0]})
    except:
        return jsonify({'Result' : "An Unknwon Error Occured"})




def handle_uploaded_file(file, filename):
    if file.filename == '':
        print('No selected file')
        return False
    if file:
        print('Filename : ', filename)
        file.save(filename)
        return True
    else:
        return False


if __name__ == "__main__":
    app.run(host='0.0.0.0', port= 5006, debug=True)
























