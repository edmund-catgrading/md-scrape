# Phaser.Utils.Array

Scope:
static

> Source: [src/utils/array/index.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/array/index.js#L7)

# Static functions

## Add

### <static> Add(array, item, [limit], [callback], [context])

**Description:**

Adds the given item, or array of items, to the array.

Each item must be unique within the array.

The array is modified in-place and returned.

You can optionally specify a limit to the maximum size of the array. If the quantity of items being

added will take the array length over this limit, it will stop adding once the limit is reached.

You can optionally specify a callback to be invoked for each item successfully added to the array.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| array | array | No | The array to be added to. |
| --- | --- | --- | --- |
| item | any | Array.<any> | No | The item, or array of items, to add to the array. Each item must be unique within the array. |
| limit | number | Yes | Optional limit which caps the size of the array. |
| callback | function | Yes | A callback to be invoked for each item successfully added to the array. |
| context | object | Yes | The context in which the callback is invoked. |

**Returns:** array - The input array.

> Source: [src/utils/array/Add.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/array/Add.js#L7)  
> Since: 3.4.0

---

## AddAt

### <static> AddAt(array, item, [index], [limit], [callback], [context])

**Description:**

Adds the given item, or array of items, to the array starting at the index specified.

Each item must be unique within the array.

Existing elements in the array are shifted up.

The array is modified in-place and returned.

You can optionally specify a limit to the maximum size of the array. If the quantity of items being

added will take the array length over this limit, it will stop adding once the limit is reached.

You can optionally specify a callback to be invoked for each item successfully added to the array.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| array | array | No |  | The array to be added to. |
| --- | --- | --- | --- | --- |
| item | any | Array.<any> | No |  | The item, or array of items, to add to the array. |
| index | number | Yes | 0 | The index in the array where the item will be inserted. |
| limit | number | Yes |  | Optional limit which caps the size of the array. |
| callback | function | Yes |  | A callback to be invoked for each item successfully added to the array. |
| context | object | Yes |  | The context in which the callback is invoked. |

**Returns:** array - The input array.

> Source: [src/utils/array/AddAt.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/array/AddAt.js#L7)  
> Since: 3.4.0

---

## BringToTop

### <static> BringToTop(array, item)

**Description:**

Moves the given element to the top of the array.

The array is modified in-place.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| array | array | No | The array. |
| --- | --- | --- | --- |
| item | \* | No | The element to move. |

**Returns:** \* - The element that was moved.

> Source: [src/utils/array/BringToTop.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/array/BringToTop.js#L7)  
> Since: 3.4.0

---

## CountAllMatching

### <static> CountAllMatching(array, property, value, [startIndex], [endIndex])

**Description:**

Returns the total number of elements in the array which have a property matching the given value.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| array | array | No | The array to search. |
| --- | --- | --- | --- |
| property | string | No | The property to test on each array element. |
| value | \* | No | The value to test the property against. Must pass a strict (`===`) comparison check. |
| startIndex | number | Yes | An optional start index to search from. |
| endIndex | number | Yes | An optional end index to search to. |

**Returns:** number - The total number of elements with properties matching the given value.

> Source: [src/utils/array/CountAllMatching.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/array/CountAllMatching.js#L9)  
> Since: 3.4.0

---

## Each

### <static> Each(array, callback, context, [args])

**Description:**

Passes each element in the array to the given callback.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| array | array | No | The array to search. |
| --- | --- | --- | --- |
| callback | function | No | A callback to be invoked for each item in the array. |
| context | object | No | The context in which the callback is invoked. |
| args | \* | Yes | Additional arguments that will be passed to the callback, after the current array item. |

**Returns:** array - The input array.

> Source: [src/utils/array/Each.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/array/Each.js#L7)  
> Since: 3.4.0

---

## EachInRange

### <static> EachInRange(array, callback, context, startIndex, endIndex, [args])

**Description:**

Passes each element in the array, between the start and end indexes, to the given callback.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| array | array | No | The array to search. |
| --- | --- | --- | --- |
| callback | function | No | A callback to be invoked for each item in the array. |
| context | object | No | The context in which the callback is invoked. |
| startIndex | number | No | The start index to search from. |
| endIndex | number | No | The end index to search to. |
| args | \* | Yes | Additional arguments that will be passed to the callback, after the child. |

**Returns:** array - The input array.

> Source: [src/utils/array/EachInRange.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/array/EachInRange.js#L9)  
> Since: 3.4.0

---

## FindClosestInSorted

### <static> FindClosestInSorted(value, array, [key])

**Description:**

Searches a pre-sorted array for the closet value to the given number.

If the `key` argument is given it will assume the array contains objects that all have the required `key` property name,

and will check for the closest value of those to the given number.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The value to search for in the array. |
| --- | --- | --- | --- |
| array | array | No | The array to search, which must be sorted. |
| key | string | Yes | An optional property key. If specified the array elements property will be checked against value. |

**Returns:** number, any - The nearest value found in the array, or if a `key` was given, the nearest object with the matching property value.

> Source: [src/utils/array/FindClosestInSorted.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/array/FindClosestInSorted.js#L7)  
> Since: 3.0.0

---

## Flatten

### <static> Flatten(array, [output])

**Description:**

Takes an array and flattens it, returning a shallow-copy flattened array.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| array | array | No | The array to flatten. |
| --- | --- | --- | --- |
| output | array | Yes | An array to hold the results in. |

**Returns:** array - The flattened output array.

> Source: [src/utils/array/Flatten.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/array/Flatten.js#L7)  
> Since: 3.60.0

---

## GetAll

### <static> GetAll(array, [property], [value], [startIndex], [endIndex])

**Description:**

Returns all elements in the array.

You can optionally specify a matching criteria using the `property` and `value` arguments.

For example: `getAll('visible', true)` would return only elements that have their visible property set.

Optionally you can specify a start and end index. For example if the array had 100 elements,

and you set `startIndex` to 0 and `endIndex` to 50, it would return matches from only

the first 50 elements.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| array | array | No | The array to search. |
| --- | --- | --- | --- |
| property | string | Yes | The property to test on each array element. |
| value | \* | Yes | The value to test the property against. Must pass a strict (`===`) comparison check. |
| startIndex | number | Yes | An optional start index to search from. |
| endIndex | number | Yes | An optional end index to search to. |

**Returns:** array - All matching elements from the array.

> Source: [src/utils/array/GetAll.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/array/GetAll.js#L9)  
> Since: 3.4.0

---

## GetFirst

### <static> GetFirst(array, [property], [value], [startIndex], [endIndex])

**Description:**

Returns the first element in the array.

You can optionally specify a matching criteria using the `property` and `value` arguments.

For example: `getAll('visible', true)` would return the first element that had its `visible` property set.

Optionally you can specify a start and end index. For example if the array had 100 elements,

and you set `startIndex` to 0 and `endIndex` to 50, it would search only the first 50 elements.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| array | array | No |  | The array to search. |
| --- | --- | --- | --- | --- |
| property | string | Yes |  | The property to test on each array element. |
| value | \* | Yes |  | The value to test the property against. Must pass a strict (`===`) comparison check. |
| startIndex | number | Yes | 0 | An optional start index to search from. |
| endIndex | number | Yes | "array.length" | An optional end index to search up to (but not included) |

**Returns:** object - The first matching element from the array, or `null` if no element could be found in the range given.

> Source: [src/utils/array/GetFirst.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/array/GetFirst.js#L9)  
> Since: 3.4.0

---

## GetRandom

### <static> GetRandom(array, [startIndex], [length])

**Description:**

Returns a Random element from the array.

**Tags:**

* generic
* genericUse
* genericUse

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| array | Array.<T> | No |  | The array to select the random entry from. |
| --- | --- | --- | --- | --- |
| startIndex | number | Yes | 0 | An optional start index. |
| length | number | Yes | "array.length" | An optional length, the total number of elements (from the startIndex) to choose from. |

**Returns:** T - A random element from the array, or `null` if no element could be found in the range given.

> Source: [src/utils/array/GetRandom.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/array/GetRandom.js#L7)  
> Since: 3.0.0

---

## MoveAbove

### <static> MoveAbove(array, item1, item2)

**Description:**

Moves the given array element above another one in the array.

If the given element is already above the other, it isn't moved.

Above means toward the end of the array.

The array is modified in-place.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| array | array | No | The input array. |
| --- | --- | --- | --- |
| item1 | \* | No | The element to move above base element. |
| item2 | \* | No | The base element. |

**Returns:** array - The input array.

> Source: [src/utils/array/MoveAbove.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/array/MoveAbove.js#L7)  
> Since: 3.55.0

---

## MoveBelow

### <static> MoveBelow(array, item1, item2)

**Description:**

Moves the given array element below another one in the array.

If the given element is already below the other, it isn't moved.

Below means toward the start of the array.

The array is modified in-place.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| array | array | No | The input array. |
| --- | --- | --- | --- |
| item1 | \* | No | The element to move below base element. |
| item2 | \* | No | The base element. |

**Returns:** array - The input array.

> Source: [src/utils/array/MoveBelow.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/array/MoveBelow.js#L7)  
> Since: 3.55.0

---

## MoveDown

### <static> MoveDown(array, item)

**Description:**

Moves the given array element down one place in the array.

The array is modified in-place.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| array | array | No | The input array. |
| --- | --- | --- | --- |
| item | \* | No | The element to move down the array. |

**Returns:** array - The input array.

> Source: [src/utils/array/MoveDown.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/array/MoveDown.js#L7)  
> Since: 3.4.0

---

## MoveTo

### <static> MoveTo(array, item, index)

**Description:**

Moves an element in an array to a new position within the same array.

The array is modified in-place.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| array | array | No | The array. |
| --- | --- | --- | --- |
| item | \* | No | The element to move. |
| index | number | No | The new index that the element will be moved to. |

**Returns:** \* - The element that was moved.

> Source: [src/utils/array/MoveTo.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/array/MoveTo.js#L7)  
> Since: 3.4.0

---

## MoveUp

### <static> MoveUp(array, item)

**Description:**

Moves the given array element up one place in the array.

The array is modified in-place.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| array | array | No | The input array. |
| --- | --- | --- | --- |
| item | \* | No | The element to move up the array. |

**Returns:** array - The input array.

> Source: [src/utils/array/MoveUp.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/array/MoveUp.js#L7)  
> Since: 3.4.0

---

## NumberArray

### <static> NumberArray(start, end, [prefix], [suffix])

**Description:**

Create an array representing the range of numbers (usually integers), between, and inclusive of,

the given `start` and `end` arguments. For example:

`var array = Phaser.Utils.Array.NumberArray(2, 4); // array = [2, 3, 4]`

`var array = Phaser.Utils.Array.NumberArray(0, 9); // array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`

`var array = Phaser.Utils.Array.NumberArray(8, 2); // array = [8, 7, 6, 5, 4, 3, 2]`

This is equivalent to `Phaser.Utils.Array.NumberArrayStep(start, end, 1)`.

You can optionally provide a prefix and / or suffix string. If given the array will contain

strings, not integers. For example:

`var array = Phaser.Utils.Array.NumberArray(1, 4, 'Level '); // array = ["Level 1", "Level 2", "Level 3", "Level 4"]`

`var array = Phaser.Utils.Array.NumberArray(5, 7, 'HD-', '.png'); // array = ["HD-5.png", "HD-6.png", "HD-7.png"]`

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| start | number | No | The minimum value the array starts with. |
| --- | --- | --- | --- |
| end | number | No | The maximum value the array contains. |
| prefix | string | Yes | Optional prefix to place before the number. If provided the array will contain strings, not integers. |
| suffix | string | Yes | Optional suffix to place after the number. If provided the array will contain strings, not integers. |

**Returns:** Array.<number>, Array.<string> - The array of number values, or strings if a prefix or suffix was provided.

> Source: [src/utils/array/NumberArray.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/array/NumberArray.js#L7)  
> Since: 3.0.0

---

## NumberArrayStep

### <static> NumberArrayStep([start], [end], [step])

**Description:**

Create an array of numbers (positive and/or negative) progressing from `start`

up to but not including `end` by advancing by `step`.

If `start` is less than `end` a zero-length range is created unless a negative `step` is specified.

Certain values for `start` and `end` (eg. NaN/undefined/null) are currently coerced to 0;

for forward compatibility make sure to pass in actual numbers.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| start | number | Yes | 0 | The start of the range. |
| --- | --- | --- | --- | --- |
| end | number | Yes | null | The end of the range. |
| step | number | Yes | 1 | The value to increment or decrement by. |

**Returns:** Array.<number> - The array of number values.

> Source: [src/utils/array/NumberArrayStep.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/array/NumberArrayStep.js#L9)  
> Since: 3.0.0

---

## QuickSelect

### <static> QuickSelect(arr, k, [left], [right], [compare])

**Description:**

A [Floyd-Rivest](https://en.wikipedia.org/wiki/Floyd%E2%80%93Rivest_algorithm) quick selection algorithm.

Rearranges the array items so that all items in the [left, k] range are smaller than all items in [k, right];

The k-th element will have the (k - left + 1)th smallest value in [left, right].

The array is modified in-place.

Based on code by [Vladimir Agafonkin](https://www.npmjs.com/~mourner)

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| arr | array | No |  | The array to sort. |
| --- | --- | --- | --- | --- |
| k | number | No |  | The k-th element index. |
| left | number | Yes | 0 | The index of the left part of the range. |
| right | number | Yes |  | The index of the right part of the range. |
| compare | function | Yes |  | An optional comparison function. Is passed two elements and should return 0, 1 or -1. |

> Source: [src/utils/array/QuickSelect.js#L25](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/array/QuickSelect.js#L25)  
> Since: 3.0.0

---

## Range

### <static> Range(a, b, [options])

**Description:**

Creates an array populated with a range of values, based on the given arguments and configuration object.

Range ([a,b,c], [1,2,3]) =

a1, a2, a3, b1, b2, b3, c1, c2, c3

Range ([a,b], [1,2,3], qty = 3) =

a1, a1, a1, a2, a2, a2, a3, a3, a3, b1, b1, b1, b2, b2, b2, b3, b3, b3

Range ([a,b,c], [1,2,3], repeat x1) =

a1, a2, a3, b1, b2, b3, c1, c2, c3, a1, a2, a3, b1, b2, b3, c1, c2, c3

Range ([a,b], [1,2], repeat -1 = endless, max = 14) =

Maybe if max is set then repeat goes to -1 automatically?

a1, a2, b1, b2, a1, a2, b1, b2, a1, a2, b1, b2, a1, a2 (capped at 14 elements)

Range ([a], [1,2,3,4,5], random = true) =

a4, a1, a5, a2, a3

Range ([a, b], [1,2,3], random = true) =

b3, a2, a1, b1, a3, b2

Range ([a, b, c], [1,2,3], randomB = true) =

a3, a1, a2, b2, b3, b1, c1, c3, c2

Range ([a], [1,2,3,4,5], yoyo = true) =

a1, a2, a3, a4, a5, a5, a4, a3, a2, a1

Range ([a, b], [1,2,3], yoyo = true) =

a1, a2, a3, b1, b2, b3, b3, b2, b1, a3, a2, a1

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| a | array | No | The first array of range elements. |
| --- | --- | --- | --- |
| b | array | No | The second array of range elements. |
| options | object | Yes | A range configuration object. Can contain: repeat, random, randomB, yoyo, max, qty. |

**Returns:** array - An array of arranged elements.

> Source: [src/utils/array/Range.js#L28](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/array/Range.js#L28)  
> Since: 3.0.0

---

## Remove

### <static> Remove(array, item, [callback], [context])

**Description:**

Removes the given item, or array of items, from the array.

The array is modified in-place.

You can optionally specify a callback to be invoked for each item successfully removed from the array.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| array | array | No | The array to be modified. |
| --- | --- | --- | --- |
| item | \* | Array.<\*> | No | The item, or array of items, to be removed from the array. |
| callback | function | Yes | A callback to be invoked for each item successfully removed from the array. |
| context | object | Yes | The context in which the callback is invoked. |

**Returns:** *, Array.<*> - The item, or array of items, that were successfully removed from the array.

> Source: [src/utils/array/Remove.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/array/Remove.js#L9)  
> Since: 3.4.0

---

## RemoveAt

### <static> RemoveAt(array, index, [callback], [context])

**Description:**

Removes the item from the given position in the array.

The array is modified in-place.

You can optionally specify a callback to be invoked for the item if it is successfully removed from the array.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| array | array | No | The array to be modified. |
| --- | --- | --- | --- |
| index | number | No | The array index to remove the item from. The index must be in bounds or it will throw an error. |
| callback | function | Yes | A callback to be invoked for the item removed from the array. |
| context | object | Yes | The context in which the callback is invoked. |

**Returns:** \* - The item that was removed.

> Source: [src/utils/array/RemoveAt.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/array/RemoveAt.js#L9)  
> Since: 3.4.0

---

## RemoveBetween

### <static> RemoveBetween(array, startIndex, endIndex, [callback], [context])

**Description:**

Removes the item within the given range in the array.

The array is modified in-place.

You can optionally specify a callback to be invoked for the item/s successfully removed from the array.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| array | array | No | The array to be modified. |
| --- | --- | --- | --- |
| startIndex | number | No | The start index to remove from. |
| endIndex | number | No | The end index to remove to. |
| callback | function | Yes | A callback to be invoked for the item removed from the array. |
| context | object | Yes | The context in which the callback is invoked. |

**Returns:** Array.<\*> - An array of items that were removed.

> Source: [src/utils/array/RemoveBetween.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/array/RemoveBetween.js#L9)  
> Since: 3.4.0

---

## RemoveRandomElement

### <static> RemoveRandomElement(array, [start], [length])

**Description:**

Removes a random object from the given array and returns it.

Will return null if there are no array items that fall within the specified range or if there is no item for the randomly chosen index.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| array | array | No |  | The array to removed a random element from. |
| --- | --- | --- | --- | --- |
| start | number | Yes | 0 | The array index to start the search from. |
| length | number | Yes | "array.length" | Optional restriction on the number of elements to randomly select from. |

**Returns:** object - The random element that was removed, or `null` if there were no array elements that fell within the given range.

> Source: [src/utils/array/RemoveRandomElement.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/array/RemoveRandomElement.js#L9)  
> Since: 3.0.0

---

## Replace

### <static> Replace(array, oldChild, newChild)

**Description:**

Replaces an element of the array with the new element.

The new element cannot already be a member of the array.

The array is modified in-place.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| array | array | No | The array to search within. |
| --- | --- | --- | --- |
| oldChild | \* | No | The element in the array that will be replaced. |
| newChild | \* | No | The element to be inserted into the array at the position of `oldChild`. |

**Returns:** boolean - Returns true if the oldChild was successfully replaced, otherwise returns false.

> Source: [src/utils/array/Replace.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/array/Replace.js#L7)  
> Since: 3.4.0

---

## RotateLeft

### <static> RotateLeft(array, [total])

**Description:**

Moves the element at the start of the array to the end, shifting all items in the process.

The "rotation" happens to the left.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| array | array | No |  | The array to shift to the left. This array is modified in place. |
| --- | --- | --- | --- | --- |
| total | number | Yes | 1 | The number of times to shift the array. |

**Returns:** \* - The most recently shifted element.

> Source: [src/utils/array/RotateLeft.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/array/RotateLeft.js#L7)  
> Since: 3.0.0

---

## RotateRight

### <static> RotateRight(array, [total])

**Description:**

Moves the element at the end of the array to the start, shifting all items in the process.

The "rotation" happens to the right.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| array | array | No |  | The array to shift to the right. This array is modified in place. |
| --- | --- | --- | --- | --- |
| total | number | Yes | 1 | The number of times to shift the array. |

**Returns:** \* - The most recently shifted element.

> Source: [src/utils/array/RotateRight.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/array/RotateRight.js#L7)  
> Since: 3.0.0

---

## SafeRange

### <static> SafeRange(array, startIndex, endIndex, [throwError])

**Description:**

Tests if the start and end indexes are a safe range for the given array.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| array | array | No |  | The array to check. |
| --- | --- | --- | --- | --- |
| startIndex | number | No |  | The start index. |
| endIndex | number | No |  | The end index. |
| throwError | boolean | Yes | true | Throw an error if the range is out of bounds. |

**Returns:** boolean - True if the range is safe, otherwise false.

> Source: [src/utils/array/SafeRange.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/array/SafeRange.js#L7)  
> Since: 3.4.0

---

## SendToBack

### <static> SendToBack(array, item)

**Description:**

Moves the given element to the bottom of the array.

The array is modified in-place.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| array | array | No | The array. |
| --- | --- | --- | --- |
| item | \* | No | The element to move. |

**Returns:** \* - The element that was moved.

> Source: [src/utils/array/SendToBack.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/array/SendToBack.js#L7)  
> Since: 3.4.0

---

## SetAll

### <static> SetAll(array, property, value, [startIndex], [endIndex])

**Description:**

Scans the array for elements with the given property. If found, the property is set to the `value`.

For example: `SetAll('visible', true)` would set all elements that have a `visible` property to `false`.

Optionally you can specify a start and end index. For example if the array had 100 elements,

and you set `startIndex` to 0 and `endIndex` to 50, it would update only the first 50 elements.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| array | array | No | The array to search. |
| --- | --- | --- | --- |
| property | string | No | The property to test for on each array element. |
| value | \* | No | The value to set the property to. |
| startIndex | number | Yes | An optional start index to search from. |
| endIndex | number | Yes | An optional end index to search to. |

**Returns:** array - The input array.

> Source: [src/utils/array/SetAll.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/array/SetAll.js#L9)  
> Since: 3.4.0

---

## Shuffle

### <static> Shuffle(array)

**Description:**

Shuffles the contents of the given array using the Fisher-Yates implementation.

The original array is modified directly and returned.

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| array | Array.<T> | No | The array to shuffle. This array is modified in place. |
| --- | --- | --- | --- |

**Returns:** Array.<T> - The shuffled array.

> Source: [src/utils/array/Shuffle.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/array/Shuffle.js#L7)  
> Since: 3.0.0

---

## SortByDigits

### <static> SortByDigits(array)

**Description:**

Takes the given array and runs a numeric sort on it, ignoring any non-digits that

may be in the entries.

You should only run this on arrays containing strings.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| array | Array.<string> | No | The input array of strings. |
| --- | --- | --- | --- |

**Returns:** Array.<string> - The sorted input array.

> Source: [src/utils/array/SortByDigits.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/array/SortByDigits.js#L7)  
> Since: 3.50.0

---

## SpliceOne

### <static> SpliceOne(array, index)

**Description:**

Removes a single item from an array and returns it without creating gc, like the native splice does.

Based on code by Mike Reinstein.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| array | array | No | The array to splice from. |
| --- | --- | --- | --- |
| index | number | No | The index of the item which should be spliced. |

**Returns:** \* - The item which was spliced (removed).

> Source: [src/utils/array/SpliceOne.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/array/SpliceOne.js#L7)  
> Since: 3.0.0

---

## StableSort

### <static> StableSort(array, [compare])

**Description:**

An in-place stable array sort, because `Array#sort()` is not guaranteed stable.

This is an implementation of merge sort, without recursion.

Function based on the Two-Screen/stable sort 0.1.8 from <https://github.com/Two-Screen/stable>

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| array | array | No | The input array to be sorted. |
| --- | --- | --- | --- |
| compare | function | Yes | The comparison function. |

**Returns:** array - The sorted result.

> Source: [src/utils/array/StableSort.js#L142](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/array/StableSort.js#L142)  
> Since: 3.0.0

---

## Swap

### <static> Swap(array, item1, item2)

**Description:**

Swaps the position of two elements in the given array.

The elements must exist in the same array.

The array is modified in-place.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| array | array | No | The input array. |
| --- | --- | --- | --- |
| item1 | \* | No | The first element to swap. |
| item2 | \* | No | The second element to swap. |

**Returns:** array - The input array.

> Source: [src/utils/array/Swap.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/array/Swap.js#L7)  
> Since: 3.4.0

---

# Static functions

* [Matrix](utils-array-matrix.md)

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Static functions](#static-functions)

  + [Add](#add)

    - [<static> Add(array, item, [limit], [callback], [context])](#static-addarray-item-limit-callback-context)
  + [AddAt](#addat)

    - [<static> AddAt(array, item, [index], [limit], [callback], [context])](#static-addatarray-item-index-limit-callback-context)
  + [BringToTop](#bringtotop)

    - [<static> BringToTop(array, item)](#static-bringtotoparray-item)
  + [CountAllMatching](#countallmatching)

    - [<static> CountAllMatching(array, property, value, [startIndex], [endIndex])](#static-countallmatchingarray-property-value-startindex-endindex)
  + [Each](#each)

    - [<static> Each(array, callback, context, [args])](#static-eacharray-callback-context-args)
  + [EachInRange](#eachinrange)

    - [<static> EachInRange(array, callback, context, startIndex, endIndex, [args])](#static-eachinrangearray-callback-context-startindex-endindex-args)
  + [FindClosestInSorted](#findclosestinsorted)

    - [<static> FindClosestInSorted(value, array, [key])](#static-findclosestinsortedvalue-array-key)
  + [Flatten](#flatten)

    - [<static> Flatten(array, [output])](#static-flattenarray-output)
  + [GetAll](#getall)

    - [<static> GetAll(array, [property], [value], [startIndex], [endIndex])](#static-getallarray-property-value-startindex-endindex)
  + [GetFirst](#getfirst)

    - [<static> GetFirst(array, [property], [value], [startIndex], [endIndex])](#static-getfirstarray-property-value-startindex-endindex)
  + [GetRandom](#getrandom)

    - [<static> GetRandom(array, [startIndex], [length])](#static-getrandomarray-startindex-length)
  + [MoveAbove](#moveabove)

    - [<static> MoveAbove(array, item1, item2)](#static-moveabovearray-item1-item2)
  + [MoveBelow](#movebelow)

    - [<static> MoveBelow(array, item1, item2)](#static-movebelowarray-item1-item2)
  + [MoveDown](#movedown)

    - [<static> MoveDown(array, item)](#static-movedownarray-item)
  + [MoveTo](#moveto)

    - [<static> MoveTo(array, item, index)](#static-movetoarray-item-index)
  + [MoveUp](#moveup)

    - [<static> MoveUp(array, item)](#static-moveuparray-item)
  + [NumberArray](#numberarray)

    - [<static> NumberArray(start, end, [prefix], [suffix])](#static-numberarraystart-end-prefix-suffix)
  + [NumberArrayStep](#numberarraystep)

    - [<static> NumberArrayStep([start], [end], [step])](#static-numberarraystepstart-end-step)
  + [QuickSelect](#quickselect)

    - [<static> QuickSelect(arr, k, [left], [right], [compare])](#static-quickselectarr-k-left-right-compare)
  + [Range](#range)

    - [<static> Range(a, b, [options])](#static-rangea-b-options)
  + [Remove](#remove)

    - [<static> Remove(array, item, [callback], [context])](#static-removearray-item-callback-context)
  + [RemoveAt](#removeat)

    - [<static> RemoveAt(array, index, [callback], [context])](#static-removeatarray-index-callback-context)
  + [RemoveBetween](#removebetween)

    - [<static> RemoveBetween(array, startIndex, endIndex, [callback], [context])](#static-removebetweenarray-startindex-endindex-callback-context)
  + [RemoveRandomElement](#removerandomelement)

    - [<static> RemoveRandomElement(array, [start], [length])](#static-removerandomelementarray-start-length)
  + [Replace](#replace)

    - [<static> Replace(array, oldChild, newChild)](#static-replacearray-oldchild-newchild)
  + [RotateLeft](#rotateleft)

    - [<static> RotateLeft(array, [total])](#static-rotateleftarray-total)
  + [RotateRight](#rotateright)

    - [<static> RotateRight(array, [total])](#static-rotaterightarray-total)
  + [SafeRange](#saferange)

    - [<static> SafeRange(array, startIndex, endIndex, [throwError])](#static-saferangearray-startindex-endindex-throwerror)
  + [SendToBack](#sendtoback)

    - [<static> SendToBack(array, item)](#static-sendtobackarray-item)
  + [SetAll](#setall)

    - [<static> SetAll(array, property, value, [startIndex], [endIndex])](#static-setallarray-property-value-startindex-endindex)
  + [Shuffle](#shuffle)

    - [<static> Shuffle(array)](#static-shufflearray)
  + [SortByDigits](#sortbydigits)

    - [<static> SortByDigits(array)](#static-sortbydigitsarray)
  + [SpliceOne](#spliceone)

    - [<static> SpliceOne(array, index)](#static-spliceonearray-index)
  + [StableSort](#stablesort)

    - [<static> StableSort(array, [compare])](#static-stablesortarray-compare)
  + [Swap](#swap)

    - [<static> Swap(array, item1, item2)](#static-swaparray-item1-item2)
* [Static functions](#static-functions-1)

Back to top

©2025[Phaser](https://docs.phaser.io)