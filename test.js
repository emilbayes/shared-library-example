var assert = require('assert')

var v1 = require('./version-1')
var v2 = require('./version-2')

assert.equal(v1.version(), 1)
assert.equal(v2.version(), 2)
assert.equal(v1.version(), 1)
assert.equal(v2.newmethod(), 3)

var dep = require('./dependent')

assert.equal(dep.version(), 2)
assert.equal(dep.newmethod(), 3)
