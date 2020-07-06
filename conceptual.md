### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?

1. They come from different places. The guy who made python wanted a language that was easy to use and read. He wanted to make it begeinnner friendly.
JS was written originally in a rush. It is actively worked on and improved. The ugly parts of it cannot go away because it has to support legacy code. It is the language of the web.

2. JavaScript is a scripting language used to create and control your website content.
Python is an interpreted, high-level, strongly-typed programming language featuring dynamic semantics and object-oriented design. It is meant to be easy to read, as well as easy to implement. The high-level language is primarily developed to build applications. The language is also used for data analysis, machine learning and developing games.

3. JavaScript can be used to run on the frontend or backend whereas python is on server side or backend.

4. JavaScript uses curly brackets, whereas pyyhon uses indentation.

4. JS uses prototype based inheritance model. Python uses class based inheritance model.

In JS, the mechanism is known as the prototype chain.

In class based languages, the classes act as blueprints. No object of that class actyally exists until you instantiate it in your program. So, you define the class, then you create an instance of that class.

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

````
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
arya.boyfriend //?


```





2. JavaScript is not an object oriented language, even though it does have objects. Python, on the other hand, is very object oriented.

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you 
  can try to get a missing key (like "c") *without* your programming 
  crashing.

- What is a unit test?

- What is an integration test?

- What is the role of web application framework, like Flask?

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

- How do you collect data from a URL placeholder parameter using Flask?

- How do you collect data from the query string using Flask?

- How do you collect data from the body of the request using Flask?

- What is a cookie and what kinds of things are they commonly used for?

- What is the session object in Flask?

- What does Flask's `jsonify()` do?

- What was the hardest part of this past week for you?
  What was the most interesting?
