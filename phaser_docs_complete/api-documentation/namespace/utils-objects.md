# Phaser.Utils.Objects

Scope:
static

> Source: [src/utils/object/index.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/object/index.js#L7)

# Static functions

## Clone

### <static> Clone(obj)

**Description:**

Shallow Object Clone. Will not clone nested objects.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| obj | object | No | The object to clone. |
| --- | --- | --- | --- |

**Returns:** object - A new object with the same properties as the input object.

> Source: [src/utils/object/Clone.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/object/Clone.js#L7)  
> Since: 3.0.0

---

## DeepCopy

### <static> DeepCopy(obj)

**Description:**

Deep Copy the given object or array.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| obj | object | No | The object to deep copy. |
| --- | --- | --- | --- |

**Returns:** object - A deep copy of the original object.

> Source: [src/utils/object/DeepCopy.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/object/DeepCopy.js#L7)  
> Since: 3.50.0

---

## Extend

### <static> Extend([args])

**Description:**

This is a slightly modified version of <http://api.jquery.com/jQuery.extend/>

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| args | \* | Yes | The objects that will be mixed. |
| --- | --- | --- | --- |

**Returns:** object - The extended object.

> Source: [src/utils/object/Extend.js#L13](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/object/Extend.js#L13)  
> Since: 3.0.0

---

## GetAdvancedValue

### <static> GetAdvancedValue(source, key, defaultValue)

**Description:**

Retrieves a value from an object. Allows for more advanced selection options, including:

Allowed types:

Explicit:

{

```
Copyx: 4

```

}

From function

{

```
Copyx: function ()

```

}

Randomly pick one element from the array

{

```
Copyx: [a, b, c, d, e, f]

```

}

Random integer between min and max:

{

```
Copyx: { randInt: [min, max] }

```

}

Random float between min and max:

{

```
Copyx: { randFloat: [min, max] }

```

}

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| source | object | No | The object to retrieve the value from. |
| --- | --- | --- | --- |
| key | string | No | The name of the property to retrieve from the object. If a property is nested, the names of its preceding properties should be separated by a dot (`.`) - `banner.hideBanner` would return the value of the `hideBanner` property from the object stored in the `banner` property of the `source` object. |
| defaultValue | \* | No | The value to return if the `key` isn't found in the `source` object. |

**Returns:** \* - The value of the requested key.

> Source: [src/utils/object/GetAdvancedValue.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/object/GetAdvancedValue.js#L10)  
> Since: 3.0.0

---

## GetFastValue

### <static> GetFastValue(source, key, [defaultValue])

**Description:**

Finds the key within the top level of the [source](../class/source.md) object, or returns [defaultValue](../class/defaultValue.md)

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| source | object | No | The object to search |
| --- | --- | --- | --- |
| key | string | No | The key for the property on source. Must exist at the top level of the source object (no periods) |
| defaultValue | \* | Yes | The default value to use if the key does not exist. |

**Returns:** \* - The value if found; otherwise, defaultValue (null if none provided)

> Source: [src/utils/object/GetFastValue.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/object/GetFastValue.js#L7)  
> Since: 3.0.0

---

## GetMinMaxValue

### <static> GetMinMaxValue(source, key, min, max, defaultValue)

**Description:**

Retrieves and clamps a numerical value from an object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| source | object | No | The object to retrieve the value from. |
| --- | --- | --- | --- |
| key | string | No | The name of the property to retrieve from the object. If a property is nested, the names of its preceding properties should be separated by a dot (`.`). |
| min | number | No | The minimum value which can be returned. |
| max | number | No | The maximum value which can be returned. |
| defaultValue | number | No | The value to return if the property doesn't exist. It's also constrained to the given bounds. |

**Returns:** number - The clamped value from the `source` object.

> Source: [src/utils/object/GetMinMaxValue.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/object/GetMinMaxValue.js#L10)  
> Since: 3.0.0

---

## GetValue

### <static> GetValue(source, key, defaultValue, [altSource])

**Description:**

Retrieves a value from an object, or an alternative object, falling to a back-up default value if not found.

The key is a string, which can be split based on the use of the period character.

For example:

```
Copy
const source = {

  lives: 3,

  render: {

    screen: {

      width: 1024

    }

  }

}



const lives = GetValue(source, 'lives', 1);

const width = GetValue(source, 'render.screen.width', 800);

const height = GetValue(source, 'render.screen.height', 600);


```

In the code above, `lives` will be 3 because it's defined at the top level of `source`.

The `width` value will be 1024 because it can be found inside the `render.screen` object.

The `height` value will be 600, the default value, because it is missing from the `render.screen` object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| source | object | No | The primary object to try to retrieve the value from. If not found in here, `altSource` is checked. |
| --- | --- | --- | --- |
| key | string | No | The name of the property to retrieve from the object. If a property is nested, the names of its preceding properties should be separated by a dot (`.`) - `banner.hideBanner` would return the value of the `hideBanner` property from the object stored in the `banner` property of the `source` object. |
| defaultValue | \* | No | The value to return if the `key` isn't found in the `source` object. |
| altSource | object | Yes | An alternative object to retrieve the value from. If the property exists in `source` then `altSource` will not be used. |

**Returns:** \* - The value of the requested key.

> Source: [src/utils/object/GetValue.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/object/GetValue.js#L7)  
> Since: 3.0.0

---

## HasAll

### <static> HasAll(source, keys)

**Description:**

Verifies that an object contains all requested keys

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| source | object | No | an object on which to check for key existence |
| --- | --- | --- | --- |
| keys | Array.<string> | No | an array of keys to ensure the source object contains |

**Returns:** boolean - true if the source object contains all keys, false otherwise.

> Source: [src/utils/object/HasAll.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/object/HasAll.js#L7)  
> Since: 3.0.0

---

## HasAny

### <static> HasAny(source, keys)

**Description:**

Verifies that an object contains at least one of the requested keys

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| source | object | No | an object on which to check for key existence |
| --- | --- | --- | --- |
| keys | Array.<string> | No | an array of keys to search the object for |

**Returns:** boolean - true if the source object contains at least one of the keys, false otherwise

> Source: [src/utils/object/HasAny.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/object/HasAny.js#L7)  
> Since: 3.0.0

---

## HasValue

### <static> HasValue(source, key)

**Description:**

Determine whether the source object has a property with the specified key.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| source | object | No | The source object to be checked. |
| --- | --- | --- | --- |
| key | string | No | The property to check for within the object |

**Returns:** boolean - `true` if the provided `key` exists on the `source` object, otherwise `false`.

> Source: [src/utils/object/HasValue.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/object/HasValue.js#L7)  
> Since: 3.0.0

---

## IsPlainObject

### <static> IsPlainObject(obj)

**Description:**

This is a slightly modified version of jQuery.isPlainObject.

A plain object is an object whose internal class property is [object Object].

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| obj | object | No | The object to inspect. |
| --- | --- | --- | --- |

**Returns:** boolean - `true` if the object is plain, otherwise `false`.

> Source: [src/utils/object/IsPlainObject.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/object/IsPlainObject.js#L7)  
> Since: 3.0.0

---

## Merge

### <static> Merge(obj1, obj2)

**Description:**

Creates a new Object using all values from obj1 and obj2.

If a value exists in both obj1 and obj2, the value in obj1 is used.

This is only a shallow copy. Deeply nested objects are not cloned, so be sure to only use this

function on shallow objects.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| obj1 | object | No | The first object. |
| --- | --- | --- | --- |
| obj2 | object | No | The second object. |

**Returns:** object - A new object containing the union of obj1's and obj2's properties.

> Source: [src/utils/object/Merge.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/object/Merge.js#L9)  
> Since: 3.0.0

---

## MergeRight

### <static> MergeRight(obj1, obj2)

**Description:**

Creates a new Object using all values from obj1.

Then scans obj2. If a property is found in obj2 that *also* exists in obj1, the value from obj2 is used, otherwise the property is skipped.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| obj1 | object | No | The first object to merge. |
| --- | --- | --- | --- |
| obj2 | object | No | The second object to merge. Keys from this object which also exist in `obj1` will be copied to `obj1`. |

**Returns:** object - The merged object. `obj1` and `obj2` are not modified.

> Source: [src/utils/object/MergeRight.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/object/MergeRight.js#L9)  
> Since: 3.0.0

---

## Pick

### <static> Pick(object, keys)

**Description:**

Returns a new object that only contains the `keys` that were found on the object provided.

If no `keys` are found, an empty object is returned.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| object | object | No | The object to pick the provided keys from. |
| --- | --- | --- | --- |
| keys | array | No | An array of properties to retrieve from the provided object. |

**Returns:** object - A new object that only contains the `keys` that were found on the provided object. If no `keys` were found, an empty object will be returned.

> Source: [src/utils/object/Pick.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/object/Pick.js#L9)  
> Since: 3.18.0

---

## SetValue

### <static> SetValue(source, key, value)

**Description:**

Sets a value in an object, allowing for dot notation to control the depth of the property.

For example:

```
Copy
var data = {

  world: {

    position: {

      x: 200,

      y: 100

    }

  }

};



SetValue(data, 'world.position.y', 300);



console.log(data.world.position.y); // 300


```

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| source | object | No | The object to set the value in. |
| --- | --- | --- | --- |
| key | string | No | The name of the property in the object. If a property is nested, the names of its preceding properties should be separated by a dot (`.`) |
| value | any | No | The value to set into the property, if found in the source object. |

**Returns:** boolean - `true` if the property key was valid and the value was set, otherwise `false`.

> Source: [src/utils/object/SetValue.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/object/SetValue.js#L7)  
> Since: 3.17.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Static functions](#static-functions)

  + [Clone](#clone)

    - [<static> Clone(obj)](#static-cloneobj)
  + [DeepCopy](#deepcopy)

    - [<static> DeepCopy(obj)](#static-deepcopyobj)
  + [Extend](#extend)

    - [<static> Extend([args])](#static-extendargs)
  + [GetAdvancedValue](#getadvancedvalue)

    - [<static> GetAdvancedValue(source, key, defaultValue)](#static-getadvancedvaluesource-key-defaultvalue)
  + [GetFastValue](#getfastvalue)

    - [<static> GetFastValue(source, key, [defaultValue])](#static-getfastvaluesource-key-defaultvalue)
  + [GetMinMaxValue](#getminmaxvalue)

    - [<static> GetMinMaxValue(source, key, min, max, defaultValue)](#static-getminmaxvaluesource-key-min-max-defaultvalue)
  + [GetValue](#getvalue)

    - [<static> GetValue(source, key, defaultValue, [altSource])](#static-getvaluesource-key-defaultvalue-altsource)
  + [HasAll](#hasall)

    - [<static> HasAll(source, keys)](#static-hasallsource-keys)
  + [HasAny](#hasany)

    - [<static> HasAny(source, keys)](#static-hasanysource-keys)
  + [HasValue](#hasvalue)

    - [<static> HasValue(source, key)](#static-hasvaluesource-key)
  + [IsPlainObject](#isplainobject)

    - [<static> IsPlainObject(obj)](#static-isplainobjectobj)
  + [Merge](#merge)

    - [<static> Merge(obj1, obj2)](#static-mergeobj1-obj2)
  + [MergeRight](#mergeright)

    - [<static> MergeRight(obj1, obj2)](#static-mergerightobj1-obj2)
  + [Pick](#pick)

    - [<static> Pick(object, keys)](#static-pickobject-keys)
  + [SetValue](#setvalue)

    - [<static> SetValue(source, key, value)](#static-setvaluesource-key-value)

Back to top

©2025[Phaser](https://docs.phaser.io)