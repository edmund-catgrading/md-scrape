# Set

Phaser.Structs.Set

A Set is a collection of unique elements.

**Constructor**

`new Set([elements])`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| elements | Array.<\*> | Yes | An optional array of elements to insert into this Set. |
| --- | --- | --- | --- |

---

**Scope**: static

> Source: [src/structs/Set.js#L18](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/Set.js#L18)  
> Since: 3.0.0

# Public Members

## entries

### entries: Array.<\*>

**Description:**

The entries of this Set. Stored internally as an array.

**Tags:**

* genericUse

> Source: [src/structs/Set.js#L38](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/Set.js#L38)  
> Since: 3.0.0

---

## size

### size: number

**Description:**

The size of this Set. This is the number of entries within it.

Changing the size will truncate the Set if the given value is smaller than the current size.

Increasing the size larger than the current size has no effect.

> Source: [src/structs/Set.js#L416](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/Set.js#L416)  
> Since: 3.0.0

---

# Public Methods

## clear

### <instance> clear()

**Description:**

Clears this Set so that it no longer contains any values.

**Tags:**

* genericUse

**Returns:** [Phaser.Structs.Set](structs-set.md) - This Set object.

> Source: [src/structs/Set.js#L299](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/Set.js#L299)  
> Since: 3.0.0

---

## contains

### <instance> contains(value)

**Description:**

Returns `true` if this Set contains the given value, otherwise returns `false`.

**Tags:**

* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | \* | No | The value to check for in this Set. |
| --- | --- | --- | --- |

**Returns:** boolean - `true` if the given value was found in this Set, otherwise `false`.

> Source: [src/structs/Set.js#L316](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/Set.js#L316)  
> Since: 3.0.0

---

## delete

### <instance> delete(value)

**Description:**

Removes the given value from this Set if this Set contains that value.

**Tags:**

* genericUse
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | \* | No | The value to remove from the Set. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Structs.Set](structs-set.md) - This Set object.

> Source: [src/structs/Set.js#L124](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/Set.js#L124)  
> Since: 3.0.0

---

## difference

### <instance> difference(set)

**Description:**

Returns a new Set containing all the values in this Set which are *not* also in the given Set.

**Tags:**

* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| set | [Phaser.Structs.Set](structs-set.md) | No | The Set to perform the difference with. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Structs.Set](structs-set.md) - A new Set containing all the values in this Set that are not also in the Set provided as an argument to this method.

> Source: [src/structs/Set.js#L389](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/Set.js#L389)  
> Since: 3.0.0

---

## dump

### <instance> dump()

**Description:**

Dumps the contents of this Set to the console via `console.group`.

> Source: [src/structs/Set.js#L149](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/Set.js#L149)  
> Since: 3.0.0

---

## each

### <instance> each(callback, [callbackScope])

**Description:**

Passes each value in this Set to the given callback.

Use this function when you know this Set will be modified during the iteration, otherwise use `iterate`.

**Tags:**

* genericUse
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| callback | EachSetCallback | No | The callback to be invoked and passed each value this Set contains. |
| --- | --- | --- | --- |
| callbackScope | \* | Yes | The scope of the callback. |

**Returns:** [Phaser.Structs.Set](structs-set.md) - This Set object.

> Source: [src/structs/Set.js#L170](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/Set.js#L170)  
> Since: 3.0.0

---

## get

### <instance> get(property, value)

**Description:**

Get an element of this Set which has a property of the specified name, if that property is equal to the specified value.

If no elements of this Set satisfy the condition then this method will return `null`.

**Tags:**

* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| property | string | No | The property name to check on the elements of this Set. |
| --- | --- | --- | --- |
| value | \* | No | The value to check for. |

**Returns:** \* - The first element of this Set that meets the required condition, or `null` if this Set contains no elements that meet the condition.

> Source: [src/structs/Set.js#L82](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/Set.js#L82)  
> Since: 3.0.0

---

## getArray

### <instance> getArray()

**Description:**

Returns an array containing all the values in this Set.

**Tags:**

* genericUse

**Returns:** Array.<\*> - An array containing all the values in this Set.

> Source: [src/structs/Set.js#L109](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/Set.js#L109)  
> Since: 3.0.0

---

## intersect

### <instance> intersect(set)

**Description:**

Returns a new Set that contains only the values which are in this Set and that are also in the given Set.

**Tags:**

* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| set | [Phaser.Structs.Set](structs-set.md) | No | The Set to intersect this set with. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Structs.Set](structs-set.md) - The result of the intersection, as a new Set.

> Source: [src/structs/Set.js#L362](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/Set.js#L362)  
> Since: 3.0.0

---

## iterate

### <instance> iterate(callback, [callbackScope])

**Description:**

Passes each value in this Set to the given callback.

For when you absolutely know this Set won't be modified during the iteration.

The callback must return a boolean. If it returns `false` then it will abort

the Set iteration immediately. If it returns `true`, it will carry on

iterating the next child in the Set.

**Tags:**

* genericUse
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| callback | EachSetCallback | No | The callback to be invoked and passed each value this Set contains. |
| --- | --- | --- | --- |
| callbackScope | \* | Yes | The scope of the callback. |

**Returns:** [Phaser.Structs.Set](structs-set.md) - This Set object.

> Source: [src/structs/Set.js#L215](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/Set.js#L215)  
> Since: 3.0.0

---

## iterateLocal

### <instance> iterateLocal(callbackKey, [args])

**Description:**

Goes through each entry in this Set and invokes the given function on them, passing in the arguments.

**Tags:**

* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| callbackKey | string | No | The key of the function to be invoked on each Set entry. |
| --- | --- | --- | --- |
| args | \* | Yes | Additional arguments that will be passed to the callback, after the child. |

**Returns:** [Phaser.Structs.Set](structs-set.md) - This Set object.

> Source: [src/structs/Set.js#L264](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/Set.js#L264)  
> Since: 3.0.0

---

## set

### <instance> set(value)

**Description:**

Inserts the provided value into this Set. If the value is already contained in this Set this method will have no effect.

**Tags:**

* genericUse
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | \* | No | The value to insert into this Set. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Structs.Set](structs-set.md) - This Set object.

> Source: [src/structs/Set.js#L59](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/Set.js#L59)  
> Since: 3.0.0

---

## union

### <instance> union(set)

**Description:**

Returns a new Set containing all values that are either in this Set or in the Set provided as an argument.

**Tags:**

* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| set | [Phaser.Structs.Set](structs-set.md) | No | The Set to perform the union with. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Structs.Set](structs-set.md) - A new Set containing all the values in this Set and the Set provided as an argument.

> Source: [src/structs/Set.js#L333](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/Set.js#L333)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [entries](#entries)

    - [entries: Array.<\*>](#entries-array)
  + [size](#size)

    - [size: number](#size-number)
* [Public Methods](#public-methods)

  + [clear](#clear)

    - [<instance> clear()](#instance-clear)
  + [contains](#contains)

    - [<instance> contains(value)](#instance-containsvalue)
  + [delete](#delete)

    - [<instance> delete(value)](#instance-deletevalue)
  + [difference](#difference)

    - [<instance> difference(set)](#instance-differenceset)
  + [dump](#dump)

    - [<instance> dump()](#instance-dump)
  + [each](#each)

    - [<instance> each(callback, [callbackScope])](#instance-eachcallback-callbackscope)
  + [get](#get)

    - [<instance> get(property, value)](#instance-getproperty-value)
  + [getArray](#getarray)

    - [<instance> getArray()](#instance-getarray)
  + [intersect](#intersect)

    - [<instance> intersect(set)](#instance-intersectset)
  + [iterate](#iterate)

    - [<instance> iterate(callback, [callbackScope])](#instance-iteratecallback-callbackscope)
  + [iterateLocal](#iteratelocal)

    - [<instance> iterateLocal(callbackKey, [args])](#instance-iteratelocalcallbackkey-args)
  + [set](#set)

    - [<instance> set(value)](#instance-setvalue)
  + [union](#union)

    - [<instance> union(set)](#instance-unionset)

Back to top

©2025[Phaser](https://docs.phaser.io)