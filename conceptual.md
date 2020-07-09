### Conceptual Exercise

#### Answer the following questions below:

- What are important differences between Python and JavaScript?

  1. They come from different places. The person who made python wanted a language that was easy to use and read. He wanted to make it begeinnner friendly.
  JS was written originally in a rush. It is actively worked on and improved. The ugly parts of it cannot go away because it has to support legacy code. It is the language of the web.

  2. JavaScript is a scripting language used to create and control your website content.
  Python is an interpreted, high-level, strongly-typed programming language featuring dynamic semantics and object-oriented design. It is meant to be easy to read, as well as easy to implement. The high-level language is primarily developed to build applications. The language is also used for data analysis, machine learning and developing games.

  3. JavaScript can be used to run on the frontend or backend whereas python is on server side or backend.

  4. JavaScript uses curly brackets, whereas pyyhon uses indentation.

  4. JS uses prototype based inheritance model. Python uses class based inheritance model.

  In JS, the mechanism is known as the prototype chain.

  In class based languages, like Python, classes act as blueprints. No object of that class actyally exists until you instantiate it in your program. So, you define the class, then you create an instance of that class.

  In JS prototypes are objects themselves. In fact, every function in JS has a __proto__ attribute and a special property called 'prototype' that allows you to access the __proto__ attributes.
  Example, with this function:
  ```
  function doSomething(){}
  ```

  If we do:
  ```
  console.log( doSomething.prototype );
  ```

  Every JS function also inherits certain attributes and qualities from JS's default Object().prototype. We can add data and methods to our doSomething prototype by setting them using .prototype.

  ex: 

  ```
  doSomething.prototype.foo = "bar"
  ```

  This line will add this property to our doSomething function, as shown here:

  ```
  {
      foo: "bar",
      constructor: ƒ doSomething(),
      __proto__: {
          constructor: ƒ Object(),
          ... // other default methods here
      }
  }
  ```

  Another thing you can do with JS, which you cannot do with Python is modify the parent object via the instance using Object.getPrototypeOf(instance), as it is done here:

  ```
  class Person {
    constructor(boyName) {
      this.boyfriend = {}
      this.boyfriend.name = boyName
      this.boyfriend.hungry = true
      this.boyfriend.angry = true
      this.money = 0
    }
    cook() {
      this.boyfriend.hungry = false
    }
    clean() {
      this.boyfriend.angry = false
    }
    code() {
      this.money ++
    }
  }

  let sansa = new Person('Petyr')
  sansa.code()
  sansa.clean()
  Object.getPrototypeOf(sansa).cook = function() { this.boyfriend.name = 'HAHA!' }
  sansa.cook()

  sansa.boyfriend //?


  let arya = new Person('Gendry')
  arya.code()
  arya.clean()
  arya.cook()
  arya.boyfriend
  ```

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you can try to get a missing key (like "c") *without* your programming crashing.

  One can use the get method, which will return None if the key doesn' exist: `dict.get('student')`

  Or use try/except:
  ```py
  try:
    dict['student']
  except:
    print('This is not a key in the dictionary')
  ```

  One last thing you could do is use an if statement to check if the key exists before accessing:

  ```py
  if student in dict:
    dict['student']
  ```

- What is a unit test?

  It is a method where one focus on one bit of functionality and makes sure it works.


- What is an integration test?

  It is a method where units that were independently depeloped are tested and made sure that they work together. This could be testing a view function to make sure all the routing and returning works correctly.


- What is the role of web application framework, like Flask?

  A web application framework provides you with tools, libraries and technologies that allow you to build a web application. This web application can be some web pages, a blog, a commercial website.
  Flask is a micro-framework, which means it has little to no dependencies to external libraries. The advantage of this is that it makes the framework light and less prone to vulnerabilities or bugs. The disadvantage is that one will have to manually add those dependencies.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

  There isn't an exact better way to do this but it depends on the situation. You can generally use query string parameters if you are describing the object you are on vs using the route for the object itself. For example, in the above case I would use /foods/pretzel and then use a query string parameter if I am decribing the pretzel such as /foods/pretzel?type=salty or /foods/pretzel?type=sugar.


- How do you collect data from a URL placeholder parameter using Flask?


You can specify the variable in the app.route and then use that variable as a paramater in the routing function. Here is an example of the pretzel:

```py
  @app.route('/foods/<food>')
  def grocery(food):
      x = food
```


- How do you collect data from the query string using Flask?

  With a query string the data can be found in the request.args dictionary:

  ```py
    @app.route('/foods')
    def grocery():
        x = request.args.get('type')
  ```


- How do you collect data from the body of the request using Flask?


  You can get the data form a post request in the body using the request.form dictionary

  ```py
    @app.route('/foods')
    def grocery():
        x = request.form.get('type')
  ```

- What is a cookie and what kinds of things are they commonly used for?

  A cookie is a small piece of data, a key and a value, sent from the server to the browser. It remembers stateful information for the the stateless http protocol. So, for instance a browser can remember if you logged in to a site before.

- What is the session object in Flask?
  
  Session is yet another way to store user-specific data between requests. It works similar to cookies. To use session you must set the secret key first. The session object of the flask package is used to set and get session data. The session object works like a dictionary but it can also keep track modifications.

- What does Flask's `jsonify()` do?
jsonify will take JSON serializeable data in python and convert it to a JSON string.

  It creates a response with the JSON representation of the given arguments. This is better explained with an example.

  The following code:
  ```
  from flask import jsonify

  @app.route('/_get_current_user')
  def get_current_user():
      return jsonify(username=g.user.username,
                    email=g.user.email,
                    id=g.user.id)
  ```

  Will return this:

  ```
  {
      "username": "admin",
      "email": "admin@localhost",
      "id": 42
  }
  ```

  - What was the hardest part of this past week for you?
    What was the most interesting?
    Hardest thing is absrobing all the new concepts. Most interesting is moving forward.
