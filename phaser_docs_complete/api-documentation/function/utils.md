# Phaser.Utils

# Phaser.Utils.Array

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

# Phaser.Utils.Array.Matrix

## CheckMatrix

### <static> CheckMatrix([matrix])

**Description:**

Checks if an array can be used as a matrix.

A matrix is a two-dimensional array (array of arrays), where all sub-arrays (rows)

have the same length. This is an example matrix:

```
Copy
[

   [ 1, 1, 1, 1, 1, 1 ],

   [ 2, 0, 0, 0, 0, 4 ],

   [ 2, 0, 1, 2, 0, 4 ],

   [ 2, 0, 3, 4, 0, 4 ],

   [ 2, 0, 0, 0, 0, 4 ],

   [ 3, 3, 3, 3, 3, 3 ]

]


```

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| matrix | Array.<Array.<T>> | Yes | The array to check. |
| --- | --- | --- | --- |

**Returns:** boolean - `true` if the given `matrix` array is a valid matrix.

> Source: [src/utils/array/matrix/CheckMatrix.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/array/matrix/CheckMatrix.js#L7)  
> Since: 3.0.0

## MatrixToString

### <static> MatrixToString([matrix])

**Description:**

Generates a string (which you can pass to console.log) from the given Array Matrix.

A matrix is a two-dimensional array (array of arrays), where all sub-arrays (rows)

have the same length. There must be at least two rows. This is an example matrix:

```
Copy
[

   [ 1, 1, 1, 1, 1, 1 ],

   [ 2, 0, 0, 0, 0, 4 ],

   [ 2, 0, 1, 2, 0, 4 ],

   [ 2, 0, 3, 4, 0, 4 ],

   [ 2, 0, 0, 0, 0, 4 ],

   [ 3, 3, 3, 3, 3, 3 ]

]


```

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| matrix | Array.<Array.<T>> | Yes | A 2-dimensional array. |
| --- | --- | --- | --- |

**Returns:** string - A string representing the matrix.

> Source: [src/utils/array/matrix/MatrixToString.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/array/matrix/MatrixToString.js#L10)  
> Since: 3.0.0

## ReverseColumns

### <static> ReverseColumns([matrix])

**Description:**

Reverses the columns in the given Array Matrix.

A matrix is a two-dimensional array (array of arrays), where all sub-arrays (rows)

have the same length. There must be at least two rows. This is an example matrix:

```
Copy
[

   [ 1, 1, 1, 1, 1, 1 ],

   [ 2, 0, 0, 0, 0, 4 ],

   [ 2, 0, 1, 2, 0, 4 ],

   [ 2, 0, 3, 4, 0, 4 ],

   [ 2, 0, 0, 0, 0, 4 ],

   [ 3, 3, 3, 3, 3, 3 ]

]


```

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| matrix | Array.<Array.<T>> | Yes | The array matrix to reverse the columns for. |
| --- | --- | --- | --- |

**Returns:** Array.<Array.<T>> - The column reversed matrix.

> Source: [src/utils/array/matrix/ReverseColumns.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/array/matrix/ReverseColumns.js#L7)  
> Since: 3.0.0

## ReverseRows

### <static> ReverseRows([matrix])

**Description:**

Reverses the rows in the given Array Matrix.

A matrix is a two-dimensional array (array of arrays), where all sub-arrays (rows)

have the same length. There must be at least two rows. This is an example matrix:

```
Copy
[

   [ 1, 1, 1, 1, 1, 1 ],

   [ 2, 0, 0, 0, 0, 4 ],

   [ 2, 0, 1, 2, 0, 4 ],

   [ 2, 0, 3, 4, 0, 4 ],

   [ 2, 0, 0, 0, 0, 4 ],

   [ 3, 3, 3, 3, 3, 3 ]

]


```

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| matrix | Array.<Array.<T>> | Yes | The array matrix to reverse the rows for. |
| --- | --- | --- | --- |

**Returns:** Array.<Array.<T>> - The column reversed matrix.

> Source: [src/utils/array/matrix/ReverseRows.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/array/matrix/ReverseRows.js#L7)  
> Since: 3.0.0

## Rotate180

### <static> Rotate180([matrix])

**Description:**

Rotates the array matrix 180 degrees.

A matrix is a two-dimensional array (array of arrays), where all sub-arrays (rows)

have the same length. There must be at least two rows. This is an example matrix:

```
Copy
[

   [ 1, 1, 1, 1, 1, 1 ],

   [ 2, 0, 0, 0, 0, 4 ],

   [ 2, 0, 1, 2, 0, 4 ],

   [ 2, 0, 3, 4, 0, 4 ],

   [ 2, 0, 0, 0, 0, 4 ],

   [ 3, 3, 3, 3, 3, 3 ]

]


```

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| matrix | Array.<Array.<T>> | Yes | The array to rotate. |
| --- | --- | --- | --- |

**Returns:** Array.<Array.<T>> - The rotated matrix array. The source matrix should be discard for the returned matrix.

> Source: [src/utils/array/matrix/Rotate180.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/array/matrix/Rotate180.js#L9)  
> Since: 3.0.0

## RotateLeft

### <static> RotateLeft([matrix], [amount])

**Description:**

Rotates the array matrix to the left (or 90 degrees)

A matrix is a two-dimensional array (array of arrays), where all sub-arrays (rows)

have the same length. There must be at least two rows. This is an example matrix:

```
Copy
[

   [ 1, 1, 1, 1, 1, 1 ],

   [ 2, 0, 0, 0, 0, 4 ],

   [ 2, 0, 1, 2, 0, 4 ],

   [ 2, 0, 3, 4, 0, 4 ],

   [ 2, 0, 0, 0, 0, 4 ],

   [ 3, 3, 3, 3, 3, 3 ]

]


```

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| matrix | Array.<Array.<T>> | Yes |  | The array to rotate. |
| --- | --- | --- | --- | --- |
| amount | number | Yes | 1 | The number of times to rotate the matrix. |

**Returns:** Array.<Array.<T>> - The rotated matrix array. The source matrix should be discard for the returned matrix.

> Source: [src/utils/array/matrix/RotateLeft.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/array/matrix/RotateLeft.js#L9)  
> Since: 3.0.0

## RotateMatrix

### <static> RotateMatrix([matrix], [direction])

**Description:**

Rotates the array matrix based on the given rotation value.

The value can be given in degrees: 90, -90, 270, -270 or 180,

or a string command: `rotateLeft`, `rotateRight` or `rotate180`.

Based on the routine from <http://jsfiddle.net/MrPolywhirl/NH42z/>.

A matrix is a two-dimensional array (array of arrays), where all sub-arrays (rows)

have the same length. There must be at least two rows. This is an example matrix:

```
Copy
[

   [ 1, 1, 1, 1, 1, 1 ],

   [ 2, 0, 0, 0, 0, 4 ],

   [ 2, 0, 1, 2, 0, 4 ],

   [ 2, 0, 3, 4, 0, 4 ],

   [ 2, 0, 0, 0, 0, 4 ],

   [ 3, 3, 3, 3, 3, 3 ]

]


```

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| matrix | Array.<Array.<T>> | Yes |  | The array to rotate. |
| --- | --- | --- | --- | --- |
| direction | number | string | Yes | 90 | The amount to rotate the matrix by. |

**Returns:** Array.<Array.<T>> - The rotated matrix array. The source matrix should be discard for the returned matrix.

> Source: [src/utils/array/matrix/RotateMatrix.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/array/matrix/RotateMatrix.js#L10)  
> Since: 3.0.0

## RotateRight

### <static> RotateRight([matrix], [amount])

**Description:**

Rotates the array matrix to the left (or -90 degrees)

A matrix is a two-dimensional array (array of arrays), where all sub-arrays (rows)

have the same length. There must be at least two rows. This is an example matrix:

```
Copy
[

   [ 1, 1, 1, 1, 1, 1 ],

   [ 2, 0, 0, 0, 0, 4 ],

   [ 2, 0, 1, 2, 0, 4 ],

   [ 2, 0, 3, 4, 0, 4 ],

   [ 2, 0, 0, 0, 0, 4 ],

   [ 3, 3, 3, 3, 3, 3 ]

]


```

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| matrix | Array.<Array.<T>> | Yes |  | The array to rotate. |
| --- | --- | --- | --- | --- |
| amount | number | Yes | 1 | The number of times to rotate the matrix. |

**Returns:** Array.<Array.<T>> - The rotated matrix array. The source matrix should be discard for the returned matrix.

> Source: [src/utils/array/matrix/RotateRight.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/array/matrix/RotateRight.js#L9)  
> Since: 3.0.0

## Translate

### <static> Translate([matrix], [x], [y])

**Description:**

Translates the given Array Matrix by shifting each column and row the

amount specified.

A matrix is a two-dimensional array (array of arrays), where all sub-arrays (rows)

have the same length. There must be at least two rows. This is an example matrix:

```
Copy
[

   [ 1, 1, 1, 1, 1, 1 ],

   [ 2, 0, 0, 0, 0, 4 ],

   [ 2, 0, 1, 2, 0, 4 ],

   [ 2, 0, 3, 4, 0, 4 ],

   [ 2, 0, 0, 0, 0, 4 ],

   [ 3, 3, 3, 3, 3, 3 ]

]


```

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| matrix | Array.<Array.<T>> | Yes |  | The array matrix to translate. |
| --- | --- | --- | --- | --- |
| x | number | Yes | 0 | The amount to horizontally translate the matrix by. |
| y | number | Yes | 0 | The amount to vertically translate the matrix by. |

**Returns:** Array.<Array.<T>> - The translated matrix.

> Source: [src/utils/array/matrix/TranslateMatrix.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/array/matrix/TranslateMatrix.js#L10)  
> Since: 3.50.0

## TransposeMatrix

### <static> TransposeMatrix([array])

**Description:**

Transposes the elements of the given matrix (array of arrays).

The transpose of a matrix is a new matrix whose rows are the columns of the original.

A matrix is a two-dimensional array (array of arrays), where all sub-arrays (rows)

have the same length. There must be at least two rows. This is an example matrix:

```
Copy
[

   [ 1, 1, 1, 1, 1, 1 ],

   [ 2, 0, 0, 0, 0, 4 ],

   [ 2, 0, 1, 2, 0, 4 ],

   [ 2, 0, 3, 4, 0, 4 ],

   [ 2, 0, 0, 0, 0, 4 ],

   [ 3, 3, 3, 3, 3, 3 ]

]


```

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| array | Array.<Array.<T>> | Yes | The array matrix to transpose. |
| --- | --- | --- | --- |

**Returns:** Array.<Array.<T>> - A new array matrix which is a transposed version of the given array.

> Source: [src/utils/array/matrix/TransposeMatrix.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/array/matrix/TransposeMatrix.js#L7)  
> Since: 3.0.0

# Phaser.Utils.Base64

## ArrayBufferToBase64

### <static> ArrayBufferToBase64(arrayBuffer, [mediaType])

**Description:**

Converts an ArrayBuffer into a base64 string.

The resulting string can optionally be a data uri if the `mediaType` argument is provided.

See <https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Data_URIs> for more details.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| arrayBuffer | ArrayBuffer | No | The Array Buffer to encode. |
| --- | --- | --- | --- |
| mediaType | string | Yes | An optional media type, i.e. `audio/ogg` or `image/jpeg`. If included the resulting string will be a data URI. |

**Returns:** string - The base64 encoded Array Buffer.

> Source: [src/utils/base64/ArrayBufferToBase64.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/base64/ArrayBufferToBase64.js#L10)  
> Since: 3.18.0

## Base64ToArrayBuffer

### <static> Base64ToArrayBuffer(base64)

**Description:**

Converts a base64 string, either with or without a data uri, into an Array Buffer.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| base64 | string | No | The base64 string to be decoded. Can optionally contain a data URI header, which will be stripped out prior to decoding. |
| --- | --- | --- | --- |

**Returns:** ArrayBuffer - An ArrayBuffer decoded from the base64 data.

> Source: [src/utils/base64/Base64ToArrayBuffer.js#L18](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/base64/Base64ToArrayBuffer.js#L18)  
> Since: 3.18.0

## NOOP

### <static> NOOP()

**Description:**

A NOOP (No Operation) callback function.

Used internally by Phaser when it's more expensive to determine if a callback exists

than it is to just invoke an empty function.

> Source: [src/utils/NOOP.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/NOOP.js#L7)  
> Since: 3.0.0

## NULL

### <static> NULL()

**Description:**

A NULL OP callback function.

This function always returns `null`.

Used internally by Phaser when it's more expensive to determine if a callback exists

than it is to just invoke an empty function.

> Source: [src/utils/NULL.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/NULL.js#L7)  
> Since: 3.60.0

# Phaser.Utils.Objects

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

# Phaser.Utils.String

## Format

### <static> Format(string, values)

**Description:**

Takes a string and replaces instances of markers with values in the given array.

The markers take the form of `%1`, `%2`, etc. I.e.:

`Format("The %1 is worth %2 gold", [ 'Sword', 500 ])`

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| string | string | No | The string containing the replacement markers. |
| --- | --- | --- | --- |
| values | array | No | An array containing values that will replace the markers. If no value exists an empty string is inserted instead. |

**Returns:** string - The string containing replaced values.

> Source: [src/utils/string/Format.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/string/Format.js#L7)  
> Since: 3.0.0

## Pad

### <static> Pad(str, [len], [pad], [dir])

**Description:**

Takes the given string and pads it out, to the length required, using the character

specified. For example if you need a string to be 6 characters long, you can call:

`pad('bob', 6, '-', 2)`

This would return: `bob---` as it has padded it out to 6 characters, using the `-` on the right.

You can also use it to pad numbers (they are always returned as strings):

`pad(512, 6, '0', 1)`

Would return: `000512` with the string padded to the left.

If you don't specify a direction it'll pad to both sides:

`pad('c64', 7, '*')`

Would return: `**c64**`

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| str | string | number | object | No |  |
| --- | --- | --- | --- | --- |
| len | number | Yes | 0 | The number of characters to be added. |
| pad | string | Yes | "" "" | The string to pad it out with (defaults to a space). |
| dir | number | Yes | 3 | The direction dir = 1 (left), 2 (right), 3 (both). |

**Returns:** string - The padded string.

> Source: [src/utils/string/Pad.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/string/Pad.js#L7)  
> Since: 3.0.0

## RemoveAt

### <static> RemoveAt(string, index)

**Description:**

Takes a string and removes the character at the given index.

The index is zero based.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| string | string | No | The string to be worked on. |
| --- | --- | --- | --- |
| index | number | No | The index of the character to be removed. This value is zero-based. |

**Returns:** string - The modified string.

> Source: [src/utils/string/RemoveAt.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/string/RemoveAt.js#L7)  
> Since: 3.50.0

## Reverse

### <static> Reverse(string)

**Description:**

Takes the given string and reverses it, returning the reversed string.

For example if given the string `Atari 520ST` it would return `TS025 iratA`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| string | string | No | The string to be reversed. |
| --- | --- | --- | --- |

**Returns:** string - The reversed string.

> Source: [src/utils/string/Reverse.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/string/Reverse.js#L7)  
> Since: 3.0.0

## UppercaseFirst

### <static> UppercaseFirst(str)

**Description:**

Capitalizes the first letter of a string if there is one.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| str | string | No | The string to capitalize. |
| --- | --- | --- | --- |

**Returns:** string - A new string, same as the first, but with the first letter capitalized.

> Source: [src/utils/string/UppercaseFirst.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/string/UppercaseFirst.js#L7)  
> Since: 3.0.0

## UUID

### <static> UUID()

**Description:**

Creates and returns an RFC4122 version 4 compliant UUID.

The string is in the form: `xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx` where each `x` is replaced with a random

hexadecimal digit from 0 to f, and `y` is replaced with a random hexadecimal digit from 8 to b.

**Returns:** string - The UUID string.

> Source: [src/utils/string/UUID.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/string/UUID.js#L7)  
> Since: 3.12.0

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Phaser.Utils.Array](#phaserutilsarray)

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
* [Phaser.Utils.Array.Matrix](#phaserutilsarraymatrix)

  + [CheckMatrix](#checkmatrix)

    - [<static> CheckMatrix([matrix])](#static-checkmatrixmatrix)
  + [MatrixToString](#matrixtostring)

    - [<static> MatrixToString([matrix])](#static-matrixtostringmatrix)
  + [ReverseColumns](#reversecolumns)

    - [<static> ReverseColumns([matrix])](#static-reversecolumnsmatrix)
  + [ReverseRows](#reverserows)

    - [<static> ReverseRows([matrix])](#static-reverserowsmatrix)
  + [Rotate180](#rotate180)

    - [<static> Rotate180([matrix])](#static-rotate180matrix)
  + [RotateLeft](#rotateleft-1)

    - [<static> RotateLeft([matrix], [amount])](#static-rotateleftmatrix-amount)
  + [RotateMatrix](#rotatematrix)

    - [<static> RotateMatrix([matrix], [direction])](#static-rotatematrixmatrix-direction)
  + [RotateRight](#rotateright-1)

    - [<static> RotateRight([matrix], [amount])](#static-rotaterightmatrix-amount)
  + [Translate](#translate)

    - [<static> Translate([matrix], [x], [y])](#static-translatematrix-x-y)
  + [TransposeMatrix](#transposematrix)

    - [<static> TransposeMatrix([array])](#static-transposematrixarray)
* [Phaser.Utils.Base64](#phaserutilsbase64)

  + [ArrayBufferToBase64](#arraybuffertobase64)

    - [<static> ArrayBufferToBase64(arrayBuffer, [mediaType])](#static-arraybuffertobase64arraybuffer-mediatype)
  + [Base64ToArrayBuffer](#base64toarraybuffer)

    - [<static> Base64ToArrayBuffer(base64)](#static-base64toarraybufferbase64)
  + [NOOP](#noop)

    - [<static> NOOP()](#static-noop)
  + [NULL](#null)

    - [<static> NULL()](#static-null)
* [Phaser.Utils.Objects](#phaserutilsobjects)

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
* [Phaser.Utils.String](#phaserutilsstring)

  + [Format](#format)

    - [<static> Format(string, values)](#static-formatstring-values)
  + [Pad](#pad)

    - [<static> Pad(str, [len], [pad], [dir])](#static-padstr-len-pad-dir)
  + [RemoveAt](#removeat-1)

    - [<static> RemoveAt(string, index)](#static-removeatstring-index)
  + [Reverse](#reverse)

    - [<static> Reverse(string)](#static-reversestring)
  + [UppercaseFirst](#uppercasefirst)

    - [<static> UppercaseFirst(str)](#static-uppercasefirststr)
  + [UUID](#uuid)

    - [<static> UUID()](#static-uuid)

Back to top

©2025[Phaser](https://docs.phaser.io)