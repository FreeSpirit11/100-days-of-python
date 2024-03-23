from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)


#to make changes to a web page directly go to developer tools and then to console and then
#write js code document.body.contentEditable=true and then enter
#then you can edit the web page and save the new html of the web page by going to file and save
#then use the new html file

'''When you perform a "hard reload" in a web browser by pressing Shift+Reload (depending on the browser),
the browser fetches all the resources, including static files like CSS and JavaScript, from the server
instead of using cached versions. that is a browser saves all the static files of a website because 
its unlikely to change in a single day . so to save your internet and to reduce server load it does so.

But here you do not to hard reolaad because our framework is configured to automatically force a 
"hard reload" or update the changes without the need for you to do it manually. This is typically done
 to streamline the development process and provide a smoother experience for developers.'''

#chatgpt
'''You're correct in noting the difference between specifying the "static" folder in file paths for static files 
and not having to do the same for templates in Flask. This is due to how Flask's URL routing works.

In Flask, when you use the `render_template` function to render HTML templates, Flask automatically 
knows to look for templates in the "templates" folder. This is a built-in convention, and you don't 
need to specify the folder explicitly.

However, when it comes to static files, Flask uses a different mechanism.
 By default, it serves static files from the "static" folder, but it does not automatically 
 prepend "/static" to the file paths in your HTML. You have to specify the path to the static files
 explicitly, like this:

```html
<link rel="stylesheet" href="/static/styles.css" />
```

The reason for this difference is that Flask uses URL routing for static files, and you may have 
multiple folders or even a complex structure for your static assets. Flask allows you to serve
 static files from various locations if you configure it accordingly. Because of this flexibility, 
 Flask requires you to specify the path to the static file in your HTML explicitly,
  so you have control over where those assets are served from.

In summary, while the default is to serve static files from the "static" folder, 
you need to specify "/static" in the file paths in your HTML to access those files, 
unlike templates, which are automatically recognized by Flask.'''