#!/usr/bin/node

const person = {
  name: {
    first: 'Bob',
    second: 'Smith'
  },
  age: 32,
  bio () {
    console.log(`${person.name.first} ${this.name.second} is ${this.age} years old`);
  },
  introduceSelf () {
    console.log(`Hi! I'm ${this.name.first}.`);
  }
};
console.log(person.__proto__);
/* person.name.first = 'Bobby Whine';
person.age = 21;

console.log(person.name.first);
console.log(person.age);
person.bio();
person.introduceSelf(); */

/* const person = {
  name: {
    first: 'Bob',
    second: 'Smith'
  },
  age: 32
}

function logProperty(propertyName) {
  console.log(person[propertyName]);
}

logProperty("name");
logProperty("age"); */

/* A function that creates an object, initializes it and returns it */

function createPerson (name) {
  const obj = {};
  obj.name = name;
  obj.introduceSelf = function () {
    console.log(`Hi! I'm ${this.name}.`);
  };
  return obj;
}

/* A constrcutor that does the same as the function above */
function Person (name) {
  this.name = name;
  this.introduceSelf = function () {
    console.log(`Hi! I'm ${this.name}.`);
  };
}

const myName = new Person('wisdom');
console.log(myName.name);
myName.introduceSelf();

const ifiok = createPerson('ifiok');
console.log(ifiok.name);
ifiok.introduceSelf();

const wisdom = createPerson('equere');
console.log(wisdom.name);
wisdom.introduceSelf();

const myDate = new Date();
let object = myDate;

do {
  object = Object.getPrototypeOf(object);
  console.log(object);
} while (object);
