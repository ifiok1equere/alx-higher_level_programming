#!/usr/bin/node

const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
let i = 1;
function incr() {
  myObject.value += i;
}
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
