#!flask/bin/python
import os
import random
from flask import Flask, jsonify, render_template, request, redirect, url_for, send_from_directory
#from flask.ext.cors import CORS
#from flask.ext.images import Images
#from werkzeug import secure_filename
#from os import listdir
#from os.path import isfile, join

app = Flask(__name__)
#images = Images(app)


#CORS(app)
 #This is the path to the upload directory
app.config['UPLOAD_FOLDER'] = '/var/lib/openshift/582615be2d5271e17600000c/app-root/data/uploads/'
# These are the extension that we are accepting to be uploaded
app.config['ALLOWED_EXTENSIONS'] = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']



pills = [
    {
        'id': 1,
        'pill_name': u'amlodipine-valsartan oral',
        'description': u'This medicine is a cream, oval, film-coated tablet imprinted with "1206".',
        'generic_name': ' amlodipine-valsartan',
        'strength': '10-160 mg'
    },
    {
        'id': 2,
        'pill_name': u'baclofen oral',
        'description': u'This medicine is a off-white, oval, scored tablet imprinted with "V" and "22 65".',
        'generic_name': u'benazepril-hydrochlorothiazide',
        'strength':  '5-6.25 mg'
    }
]


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/uploads')
def uploads():
    return render_template('uploads.html')



'''
@app.route('/pillfinder/api/v1.0/delete_item/<filename>/', methods=['GET', 'POST'])
def delete_item(filename):
    os.remove(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return render_template('delete.html')



@app.route('/images')
def images():
    image_names = os.listdir('/var/lib/openshift/582615be2d5271e17600000c/app-root/data/uploads/')
    print image_names
    width = max(0, min(1000, int(request.args.get('width', 200))))
    height = max(0, min(1000, int(request.args.get('height', 200))))
    background = request.args.get('background', '#000000')
    transform = request.args.get('transform', '')
    enlarge = bool(request.args.get('enlarge'))

    return render_template('images.html', image_names=image_names)


@app.route('/pillfinder/api/v1.0/identification', methods=['GET'])
def identification():
     return jsonify({'pills': pills})


# Route that will process the file upload
@app.route('/pillfinder/api/v1.0/upload', methods=['POST'])
def upload():
    # Get the name of the uploaded file
    file = request.files['file']
    # Check if the file is one of the allowed types/extensions
    #if file and allowed_file(file.filename):
        # Make the filename safe, remove unsupported chars
    filename = secure_filename(file.filename)
        # Move the file form the temporal folder to
        # the upload folder we setup
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # Redirect the user to the uploaded_file route, which
        # will basicaly show on the browser the uploaded file
    return redirect(url_for('uploaded_file',
                            filename=filename))

@app.route('/pillfinder/api/v1.0/youtube', methods=['POST'])
def youtube():
   # this will work for posted data
   #url = (request.form['url'])
   content = request.get_json(force=True)
   with open(os.path.join(app.config['UPLOAD_FOLDER'] , 'output.txt'), 'wb') as fo:
      fo.write(content['url'])
   return content['url']
  # with open(app.config['UPLOAD_FOLDER'] + 'output.txt', wb) as fo:
   #   fo.write(url)


# This route is expecting a parameter containing the name
# of a file. Then it will locate that file on the upload
# directory and show it on the browser, so if the user uploads
# an image, that image is going to be show after the upload
@app.route('/pillfinder/api/v1.0/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)
def get_path():
    imgs = []
    #for img in os.listdir('/Users/jd/Documents/Code/pillfinder/uploads'):
    for img in os.listdir('/var/lib/openshift/582615be2d5271e17600000c/app-root/data/uploads/'):
        imgs.append(img)
#    image = random.randint(0, len(imgs)-1) #gen random image path from images in directory
    return imgs #imgs[image].split(".")[0] #get filename without extension

@app.route('/listfiles')
def listfiles():
    img = get_path()
    print img
    return render_template('browseImages.html', img=img) #template just shows image
'''
if __name__ == '__main__':
    app.run(
        debug=True
    )
