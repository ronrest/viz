import os
import random, datetime
from IPython.display import HTML


def add_imagefilelooper_js():
    """ Adds some javascript to Jupyter notebook to be able to embedd a
        widget that loops through image files.
    """
    return HTML(get_image_file_looper_js())


def imagefilelooper_widget(files):
    """ Given a list of filenames of images, it embeds a widget in a Jupyter
        cell to browse through them using PREV, NEXT buttons
    """
    return HTML(get_imagefilelooper_html(files))

def get_image_file_looper_js():
    return """
    <script type="text/javascript">
        class ImageFileLooper {
            constructor(id, files){
                this.i = 0;
                this.id = id;
                this.files = files;

                this.elementContainer = document.getElementById(this.id);
                this.prevButton = document.getElementById(this.id+"_prev");
                this.nextButton = document.getElementById(this.id+"_next");
                this.imgElement = document.getElementById(this.id+"_img");
                this.fileLabel = document.getElementById(this.id+"_label");

                let fl = this;
                this.prevButton.addEventListener('click', function(){fl.prev()});
                this.nextButton.addEventListener('click', function(){fl.next()});
                this.update_image();

            }
            prev(){
                this.i = (this.i-1) %this.files.length;
                if (this.i < 0){
                    this.i = this.files.length + this.i;
                }
                this.update_image();
            }
            next(){
                this.i = (this.i+1) % this.files.length;
                this.update_image();
            }
            update_image(){
                this.imgElement.src = this.files[this.i];
                this.fileLabel.innerHTML = this.files[this.i];
            }
        }
    </script>
    """

def get_imagefilelooper_html(files):
    # Create an id for the html element
    a = int(datetime.datetime.utcnow().timestamp()*1e6)
    b = random.randint(0, 1000000)
    id = hex(int(f"{a}{b:06d}"))[2:]

    return f"""
    <button id="{id}_prev" type="button">PREV</button>
    <button id="{id}_next" type="button">NEXT</button>
    <span id="{id}_label"></span>
    <img id="{id}_img" src="" width="100%"></img>
    <script type="text/javascript">
        var files =  {files};
        fbb = new ImageFileLooper("{id}", files);
    </script>
    """


def create_imagefilelooper_file(files, outfile):
    """ Given a list of filenames of images, it embeds a widget in a Jupyter
        cell to browse through them using PREV, NEXT buttons
    """

    js = get_image_file_looper_js()
    html_snippet = get_imagefilelooper_html(files)
    html = f"""
    <!DOCTYPE html>
    <html lang="en" dir="ltr">
        <head>
            <meta charset="utf-8">
            <title></title>
        </head>
        <body>
            {js}

            {html_snippet}

        </body>
    </html>
    """
    os.makedirs(os.path.abspath(os.path.dirname(outfile)), exist_ok=True)
    with open(outfile, "w") as fob:
        fob.write(html)


#
# files = [
#     "plots/scrap/plot1.jpg",
#     "plots/scrap/plot2.jpg",
#     "plots/scrap/plot3.jpg",
#     "plots/scrap/plot4.jpg",
#     ]
#

# create_imagefilelooper_file([os.path.basename(file) for file in plotfiles], outfile="plots/feature_distributions/browser.html")
# HTML('<iframe src="plots/scrap/browser.html" width="100%" height="500px"></iframe>')
