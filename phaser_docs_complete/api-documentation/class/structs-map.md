# Map

Phaser.Structs.Map

The keys of a Map can be arbitrary values.

```
Copy
var map = new Map([

   [ 1, 'one' ],

   [ 2, 'two' ],

   [ 3, 'three' ]

]);


```

**Constructor**

`new Map(elements)`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| elements | Array.<\*> | No | An optional array of key-value pairs to populate this Map with. |
| --- | --- | --- | --- |

---

**Scope**: static

> Source: [src/structs/Map.js#L18](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/Map.js#L18)  
> Since: 3.0.0

# Public Members

## entries

### entries: Object.<string, \*>

**Description:**

The entries in this Map.

**Tags:**

* genericUse

> Source: [src/structs/Map.js#L47](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/Map.js#L47)  
> Since: 3.0.0

---

## size

### size: number

**Description:**

The number of key / value pairs in this Map.

> Source: [src/structs/Map.js#L59](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/Map.js#L59)  
> Since: 3.0.0

---

# Public Methods

## clear

### <instance> clear()

**Description:**

Delete all entries from this Map.

**Tags:**

* genericUse

**Returns:** [Phaser.Structs.Map](structs-map.md) - This Map object.

> Source: [src/structs/Map.js#L217](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/Map.js#L217)  
> Since: 3.0.0

---

## contains

### <instance> contains(value)

**Description:**

Returns `true` if the value exists within this Map. Otherwise, returns `false`.

**Tags:**

* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | \* | No | The value to search for. |
| --- | --- | --- | --- |

**Returns:** boolean - `true` if the value is found, otherwise `false`.

> Source: [src/structs/Map.js#L330](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/Map.js#L330)  
> Since: 3.0.0

---

## delete

### <instance> delete(key)

**Description:**

Delete the specified element from this Map.

**Tags:**

* genericUse
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The key of the element to delete from this Map. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Structs.Map](structs-map.md) - This Map object.

> Source: [src/structs/Map.js#L193](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/Map.js#L193)  
> Since: 3.0.0

---

## dump

### <instance> dump()

**Description:**

Dumps the contents of this Map to the console via `console.group`.

> Source: [src/structs/Map.js#L278](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/Map.js#L278)  
> Since: 3.0.0

---

## each

### <instance> each(callback)

**Description:**

Iterates through all entries in this Map, passing each one to the given callback.

If the callback returns `false`, the iteration will break.

**Tags:**

* genericUse
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| callback | EachMapCallback | No | The callback which will receive the keys and entries held in this Map. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Structs.Map](structs-map.md) - This Map object.

> Source: [src/structs/Map.js#L300](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/Map.js#L300)  
> Since: 3.0.0

---

## get

### <instance> get(key)

**Description:**

Returns the value associated to the `key`, or `undefined` if there is none.

**Tags:**

* genericUse
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The key of the element to return from the `Map` object. |
| --- | --- | --- | --- |

**Returns:** \* - The element associated with the specified key or `undefined` if the key can't be found in this Map object.

> Source: [src/structs/Map.js#L132](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/Map.js#L132)  
> Since: 3.0.0

---

## getArray

### <instance> getArray()

**Description:**

Returns an `Array` of all the values stored in this Map.

**Tags:**

* genericUse

**Returns:** Array.<\*> - An array of the values stored in this Map.

> Source: [src/structs/Map.js#L153](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/Map.js#L153)  
> Since: 3.0.0

---

## has

### <instance> has(key)

**Description:**

Returns a boolean indicating whether an element with the specified key exists or not.

**Tags:**

* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The key of the element to test for presence of in this Map. |
| --- | --- | --- | --- |

**Returns:** boolean - Returns `true` if an element with the specified key exists in this Map, otherwise `false`.

> Source: [src/structs/Map.js#L176](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/Map.js#L176)  
> Since: 3.0.0

---

## keys

### <instance> keys()

**Description:**

Returns all entries keys in this Map.

**Tags:**

* genericUse

**Returns:** Array.<string> - Array containing entries' keys.

> Source: [src/structs/Map.js#L240](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/Map.js#L240)  
> Since: 3.0.0

---

## merge

### <instance> merge(map, [override])

**Description:**

Merges all new keys from the given Map into this one.

If it encounters a key that already exists it will be skipped unless override is set to `true`.

**Tags:**

* genericUse

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| map | [Phaser.Structs.Map](structs-map.md) | No |  | The Map to merge in to this Map. |
| --- | --- | --- | --- | --- |
| override | boolean | Yes | false | Set to `true` to replace values in this Map with those from the source map, or `false` to skip them. |

**Returns:** [Phaser.Structs.Map](structs-map.md) - This Map object.

> Source: [src/structs/Map.js#L357](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/Map.js#L357)  
> Since: 3.0.0

---

## set

### <instance> set(key, value)

**Description:**

Adds an element with a specified `key` and `value` to this Map.

If the `key` already exists, the value will be replaced.

If you wish to add multiple elements in a single call, use the `setAll` method instead.

**Tags:**

* genericUse
* genericUse
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The key of the element to be added to this Map. |
| --- | --- | --- | --- |
| value | \* | No | The value of the element to be added to this Map. |

**Returns:** [Phaser.Structs.Map](structs-map.md) - This Map object.

> Source: [src/structs/Map.js#L101](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/Map.js#L101)  
> Since: 3.0.0

---

## setAll

### <instance> setAll(elements)

**Description:**

Adds all the elements in the given array to this Map.

If the element already exists, the value will be skipped.

**Tags:**

* generic
* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| elements | Array.<\*> | No | An array of key-value pairs to populate this Map with. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Structs.Map](structs-map.md) - This Map object.

> Source: [src/structs/Map.js#L72](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/Map.js#L72)  
> Since: 3.70.0

---

## values

### <instance> values()

**Description:**

Returns an `Array` of all entries.

**Tags:**

* genericUse

**Returns:** Array.<\*> - An `Array` of entries.

> Source: [src/structs/Map.js#L255](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/Map.js#L255)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [entries](#entries)

    - [entries: Object.<string, \*>](#entries-objectstring-)
  + [size](#size)

    - [size: number](#size-number)
* [Public Methods](#public-methods)

  + [clear](#clear)

    - [<instance> clear()](#instance-clear)
  + [contains](#contains)

    - [<instance> contains(value)](#instance-containsvalue)
  + [delete](#delete)

    - [<instance> delete(key)](#instance-deletekey)
  + [dump](#dump)

    - [<instance> dump()](#instance-dump)
  + [each](#each)

    - [<instance> each(callback)](#instance-eachcallback)
  + [get](#get)

    - [<instance> get(key)](#instance-getkey)
  + [getArray](#getarray)

    - [<instance> getArray()](#instance-getarray)
  + [has](#has)

    - [<instance> has(key)](#instance-haskey)
  + [keys](#keys)

    - [<instance> keys()](#instance-keys)
  + [merge](#merge)

    - [<instance> merge(map, [override])](#instance-mergemap-override)
  + [set](#set)

    - [<instance> set(key, value)](#instance-setkey-value)
  + [setAll](#setall)

    - [<instance> setAll(elements)](#instance-setallelements)
  + [values](#values)

    - [<instance> values()](#instance-values)

Back to top

©2025[Phaser](https://docs.phaser.io)