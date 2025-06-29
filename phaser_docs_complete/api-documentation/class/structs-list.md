# List

Phaser.Structs.List

List is a generic implementation of an ordered list which contains utility methods for retrieving, manipulating, and iterating items.

**Constructor**

`new List(parent)`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| parent | \* | No | The parent of this list. |
| --- | --- | --- | --- |

---

**Scope**: static

> Source: [src/structs/List.js#L19](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/List.js#L19)  
> Since: 3.0.0

# Public Members

## \_sortKey

### \_sortKey: string

**Description:**

The property key to sort by.

> Source: [src/structs/List.js#L89](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/List.js#L89)  
> Since: 3.4.0

---

## addCallback

### addCallback: function

**Description:**

A callback that is invoked every time a child is added to this list.

> Source: [src/structs/List.js#L71](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/List.js#L71)  
> Since: 3.4.0

---

## first

### first: \*

**Description:**

The first item in the List or `null` for an empty List.

**Tags:**

* genericUse

> Source: [src/structs/List.js#L725](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/List.js#L725)  
> Since: 3.0.0

---

## last

### last: \*

**Description:**

The last item in the List, or `null` for an empty List.

**Tags:**

* genericUse

> Source: [src/structs/List.js#L752](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/List.js#L752)  
> Since: 3.0.0

---

## length

### length: number

**Description:**

The number of items inside the List.

> Source: [src/structs/List.js#L708](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/List.js#L708)  
> Since: 3.0.0

---

## list

### list: Array.<\*>

**Description:**

The objects that belong to this collection.

**Tags:**

* genericUse

> Source: [src/structs/List.js#L47](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/List.js#L47)  
> Since: 3.0.0

---

## next

### next: \*

**Description:**

The next item in the List, or `null` if the entire List has been traversed.

This property can be read successively after reading <#first> or manually setting the <#position> to iterate the List.

**Tags:**

* genericUse

> Source: [src/structs/List.js#L779](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/List.js#L779)  
> Since: 3.0.0

---

## parent

### parent: \*

**Description:**

The parent of this list.

> Source: [src/structs/List.js#L38](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/List.js#L38)  
> Since: 3.0.0

---

## position

### position: number

**Description:**

The index of the current element.

This is used internally when iterating through the list with the <#first>, <#last>, <#get>, and <#previous> properties.

> Source: [src/structs/List.js#L59](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/List.js#L59)  
> Since: 3.0.0

---

## previous

### previous: \*

**Description:**

The previous item in the List, or `null` if the entire List has been traversed.

This property can be read successively after reading <#last> or manually setting the <#position> to iterate the List backwards.

**Tags:**

* genericUse

> Source: [src/structs/List.js#L808](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/List.js#L808)  
> Since: 3.0.0

---

## removeCallback

### removeCallback: function

**Description:**

A callback that is invoked every time a child is removed from this list.

> Source: [src/structs/List.js#L80](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/List.js#L80)  
> Since: 3.4.0

---

# Public Methods

## add

### <instance> add(child, [skipCallback])

**Description:**

Adds the given item to the end of the list. Each item must be unique.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| child | \* | Array.<\*> | No |  | The item, or array of items, to add to the list. |
| --- | --- | --- | --- | --- |
| skipCallback | boolean | Yes | false | Skip calling the List.addCallback if this child is added successfully. |

**Returns:** \* - The list's underlying array.

> Source: [src/structs/List.js#L99](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/List.js#L99)  
> Since: 3.0.0

---

## addAt

### <instance> addAt(child, [index], [skipCallback])

**Description:**

Adds an item to list, starting at a specified index. Each item must be unique within the list.

**Tags:**

* genericUse

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| child | \* | No |  | The item, or array of items, to add to the list. |
| --- | --- | --- | --- | --- |
| index | number | Yes | 0 | The index in the list at which the element(s) will be inserted. |
| skipCallback | boolean | Yes | false | Skip calling the List.addCallback if this child is added successfully. |

**Returns:** \* - The List's underlying array.

> Source: [src/structs/List.js#L122](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/List.js#L122)  
> Since: 3.0.0

---

## bringToTop

### <instance> bringToTop(child)

**Description:**

Brings the given child to the top of this List.

**Tags:**

* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| child | \* | No | The item to bring to the top of the List. |
| --- | --- | --- | --- |

**Returns:** \* - The item which was moved.

> Source: [src/structs/List.js#L490](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/List.js#L490)  
> Since: 3.0.0

---

## count

### <instance> count(property, value)

**Description:**

Returns the total number of items in the List which have a property matching the given value.

**Tags:**

* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| property | string | No | The property to test on each item. |
| --- | --- | --- | --- |
| value | \* | No | The value to test the property against. |

**Returns:** number - The total number of matching elements.

> Source: [src/structs/List.js#L306](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/List.js#L306)  
> Since: 3.0.0

---

## destroy

### <instance> destroy()

**Description:**

Destroys this List.

> Source: [src/structs/List.js#L693](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/List.js#L693)  
> Since: 3.0.0

---

## each

### <instance> each(callback, [context], [args])

**Description:**

Passes all children to the given callback.

**Tags:**

* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| callback | EachListCallback | No | The function to call. |
| --- | --- | --- | --- |
| context | \* | Yes | Value to use as `this` when executing callback. |
| args | \* | Yes | Additional arguments that will be passed to the callback, after the child. |

> Source: [src/structs/List.js#L651](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/List.js#L651)  
> Since: 3.0.0

---

## exists

### <instance> exists(child)

**Description:**

Checks if an item exists within the List.

**Tags:**

* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| child | \* | No | The item to check for the existence of. |
| --- | --- | --- | --- |

**Returns:** boolean - `true` if the item is found in the list, otherwise `false`.

> Source: [src/structs/List.js#L614](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/List.js#L614)  
> Since: 3.0.0

---

## getAll

### <instance> getAll([property], [value], [startIndex], [endIndex])

**Description:**

Returns all children in this List.

You can optionally specify a matching criteria using the `property` and `value` arguments.

For example: `getAll('parent')` would return only children that have a property called `parent`.

You can also specify a value to compare the property to:

`getAll('visible', true)` would return only children that have their visible property set to `true`.

Optionally you can specify a start and end index. For example if this List had 100 children,

and you set `startIndex` to 0 and `endIndex` to 50, it would return matches from only

the first 50 children in the List.

**Tags:**

* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| property | string | Yes | An optional property to test against the value argument. |
| --- | --- | --- | --- |
| value | any | Yes | If property is set then Child.property must strictly equal this value to be included in the results. |
| startIndex | number | Yes | The first child index to start the search from. |
| endIndex | number | Yes | The last child index to search up until. |

**Returns:** Array.<\*> - All items of the List which match the given criterion, if any.

> Source: [src/structs/List.js#L274](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/List.js#L274)  
> Since: 3.0.0

---

## getAt

### <instance> getAt(index)

**Description:**

Retrieves the item at a given position inside the List.

**Tags:**

* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| index | number | No | The index of the item. |
| --- | --- | --- | --- |

**Returns:** \* - The retrieved item, or `undefined` if it's outside the List's bounds.

> Source: [src/structs/List.js#L148](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/List.js#L148)  
> Since: 3.0.0

---

## getByName

### <instance> getByName(name)

**Description:**

Searches for the first instance of a child with its `name`

property matching the given argument. Should more than one child have

the same name only the first is returned.

**Tags:**

* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| name | string | No | The name to search for. |
| --- | --- | --- | --- |

**Returns:** \* - The first child with a matching name, or null if none were found.

> Source: [src/structs/List.js#L217](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/List.js#L217)  
> Since: 3.0.0

---

## getFirst

### <instance> getFirst(property, value, [startIndex], [endIndex])

**Description:**

Returns the first element in a given part of the List which matches a specific criterion.

**Tags:**

* genericUse

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| property | string | No |  | The name of the property to test or a falsey value to have no criterion. |
| --- | --- | --- | --- | --- |
| value | \* | No |  | The value to test the `property` against, or `undefined` to allow any value and only check for existence. |
| startIndex | number | Yes | 0 | The position in the List to start the search at. |
| endIndex | number | Yes |  | The position in the List to optionally stop the search at. It won't be checked. |

**Returns:** \* - The first item which matches the given criterion, or `null` if no such item exists.

> Source: [src/structs/List.js#L254](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/List.js#L254)  
> Since: 3.0.0

---

## getIndex

### <instance> getIndex(child)

**Description:**

Locates an item within the List and returns its index.

**Tags:**

* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| child | \* | No | The item to locate. |
| --- | --- | --- | --- |

**Returns:** number - The index of the item within the List, or -1 if it's not in the List.

> Source: [src/structs/List.js#L165](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/List.js#L165)  
> Since: 3.0.0

---

## getRandom

### <instance> getRandom([startIndex], [length])

**Description:**

Returns a random child from the group.

**Tags:**

* genericUse

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| startIndex | number | Yes | 0 | Offset from the front of the group (lowest child). |
| --- | --- | --- | --- | --- |
| length | number | Yes | "(to top)" | Restriction on the number of values you want to randomly select from. |

**Returns:** \* - A random child of this Group.

> Source: [src/structs/List.js#L236](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/List.js#L236)  
> Since: 3.0.0

---

## moveAbove

### <instance> moveAbove(child1, child2)

**Description:**

Moves an item above another one in the List.

If the given item is already above the other, it isn't moved.

Above means toward the end of the List.

**Tags:**

* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| child1 | \* | No | The element to move above base element. |
| --- | --- | --- | --- |
| child2 | \* | No | The base element. |

> Source: [src/structs/List.js#L358](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/List.js#L358)  
> Since: 3.55.0

---

## moveBelow

### <instance> moveBelow(child1, child2)

**Description:**

Moves an item below another one in the List.

If the given item is already below the other, it isn't moved.

Below means toward the start of the List.

**Tags:**

* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| child1 | \* | No | The element to move below base element. |
| --- | --- | --- | --- |
| child2 | \* | No | The base element. |

> Source: [src/structs/List.js#L376](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/List.js#L376)  
> Since: 3.55.0

---

## moveDown

### <instance> moveDown(child)

**Description:**

Moves the given child down one place in this group unless it's already at the bottom.

**Tags:**

* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| child | \* | No | The item to move down. |
| --- | --- | --- | --- |

**Returns:** \* - The item which was moved.

> Source: [src/structs/List.js#L543](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/List.js#L543)  
> Since: 3.0.0

---

## moveTo

### <instance> moveTo(child, index)

**Description:**

Moves an item in the List to a new position.

**Tags:**

* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| child | \* | No | The item to move. |
| --- | --- | --- | --- |
| index | number | No | Moves an item in the List to a new position. |

**Returns:** \* - The item that was moved.

> Source: [src/structs/List.js#L340](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/List.js#L340)  
> Since: 3.0.0

---

## moveUp

### <instance> moveUp(child)

**Description:**

Moves the given child up one place in this group unless it's already at the top.

**Tags:**

* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| child | \* | No | The item to move up. |
| --- | --- | --- | --- |

**Returns:** \* - The item which was moved.

> Source: [src/structs/List.js#L524](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/List.js#L524)  
> Since: 3.0.0

---

## remove

### <instance> remove(child, [skipCallback])

**Description:**

Removes one or many items from the List.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| child | \* | No |  | The item, or array of items, to remove. |
| --- | --- | --- | --- | --- |
| skipCallback | boolean | Yes | false | Skip calling the List.removeCallback. |

**Returns:** \* - The item, or array of items, which were successfully removed from the List.

> Source: [src/structs/List.js#L394](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/List.js#L394)  
> Since: 3.0.0

---

## removeAll

### <instance> removeAll([skipCallback])

**Description:**

Removes all the items.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| skipCallback | boolean | Yes | false | Skip calling the List.removeCallback. |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.Structs.List](structs-list.md) - This List object.

> Source: [src/structs/List.js#L468](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/List.js#L468)  
> Since: 3.0.0

---

## removeAt

### <instance> removeAt(index, [skipCallback])

**Description:**

Removes the item at the given position in the List.

**Tags:**

* genericUse

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| index | number | No |  | The position to remove the item from. |
| --- | --- | --- | --- | --- |
| skipCallback | boolean | Yes | false | Skip calling the List.removeCallback. |

**Returns:** \* - The item that was removed.

> Source: [src/structs/List.js#L417](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/List.js#L417)  
> Since: 3.0.0

---

## removeBetween

### <instance> removeBetween([startIndex], [endIndex], [skipCallback])

**Description:**

Removes the items within the given range in the List.

**Tags:**

* genericUse

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| startIndex | number | Yes | 0 | The index to start removing from. |
| --- | --- | --- | --- | --- |
| endIndex | number | Yes |  | The position to stop removing at. The item at this position won't be removed. |
| skipCallback | boolean | Yes | false | Skip calling the List.removeCallback. |

**Returns:** Array.<\*> - An array of the items which were removed.

> Source: [src/structs/List.js#L442](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/List.js#L442)  
> Since: 3.0.0

---

## replace

### <instance> replace(oldChild, newChild)

**Description:**

Replaces a child of this List with the given newChild. The newChild cannot be a member of this List.

**Tags:**

* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| oldChild | \* | No | The child in this List that will be replaced. |
| --- | --- | --- | --- |
| newChild | \* | No | The child to be inserted into this List. |

**Returns:** \* - Returns the oldChild that was replaced within this group.

> Source: [src/structs/List.js#L596](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/List.js#L596)  
> Since: 3.0.0

---

## reverse

### <instance> reverse()

**Description:**

Reverses the order of all children in this List.

**Tags:**

* genericUse

**Returns:** [Phaser.Structs.List](structs-list.md) - This List object.

> Source: [src/structs/List.js#L562](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/List.js#L562)  
> Since: 3.0.0

---

## sendToBack

### <instance> sendToBack(child)

**Description:**

Sends the given child to the bottom of this List.

**Tags:**

* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| child | \* | No | The item to send to the back of the list. |
| --- | --- | --- | --- |

**Returns:** \* - The item which was moved.

> Source: [src/structs/List.js#L507](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/List.js#L507)  
> Since: 3.0.0

---

## setAll

### <instance> setAll(property, value, [startIndex], [endIndex])

**Description:**

Sets the property `key` to the given value on all members of this List.

**Tags:**

* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| property | string | No | The name of the property to set. |
| --- | --- | --- | --- |
| value | \* | No | The value to set the property to. |
| startIndex | number | Yes | The first child index to start the search from. |
| endIndex | number | Yes | The last child index to search up until. |

> Source: [src/structs/List.js#L631](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/List.js#L631)  
> Since: 3.0.0

---

## shuffle

### <instance> shuffle()

**Description:**

Shuffles the items in the list.

**Tags:**

* genericUse

**Returns:** [Phaser.Structs.List](structs-list.md) - This List object.

> Source: [src/structs/List.js#L579](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/List.js#L579)  
> Since: 3.0.0

---

## shutdown

### <instance> shutdown()

**Description:**

Clears the List and recreates its internal array.

> Source: [src/structs/List.js#L680](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/List.js#L680)  
> Since: 3.0.0

---

## sort

### <instance> sort(property, [handler])

**Description:**

Sort the contents of this List so the items are in order based on the given property.

For example, `sort('alpha')` would sort the List contents based on the value of their `alpha` property.

**Tags:**

* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| property | string | No | The property to lexically sort by. |
| --- | --- | --- | --- |
| handler | function | Yes | Provide your own custom handler function. Will receive 2 children which it should compare and return a boolean. |

**Returns:** [Phaser.Structs.List](structs-list.md) - This List object.

> Source: [src/structs/List.js#L183](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/List.js#L183)  
> Since: 3.0.0

---

## swap

### <instance> swap(child1, child2)

**Description:**

Swaps the positions of two items in the list.

**Tags:**

* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| child1 | \* | No | The first item to swap. |
| --- | --- | --- | --- |
| child2 | \* | No | The second item to swap. |

> Source: [src/structs/List.js#L324](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/List.js#L324)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [\_sortKey](#_sortkey)

    - [\_sortKey: string](#_sortkey-string)
  + [addCallback](#addcallback)

    - [addCallback: function](#addcallback-function)
  + [first](#first)

    - [first: \*](#first-)
  + [last](#last)

    - [last: \*](#last-)
  + [length](#length)

    - [length: number](#length-number)
  + [list](#list)

    - [list: Array.<\*>](#list-array)
  + [next](#next)

    - [next: \*](#next-)
  + [parent](#parent)

    - [parent: \*](#parent-)
  + [position](#position)

    - [position: number](#position-number)
  + [previous](#previous)

    - [previous: \*](#previous-)
  + [removeCallback](#removecallback)

    - [removeCallback: function](#removecallback-function)
* [Public Methods](#public-methods)

  + [add](#add)

    - [<instance> add(child, [skipCallback])](#instance-addchild-skipcallback)
  + [addAt](#addat)

    - [<instance> addAt(child, [index], [skipCallback])](#instance-addatchild-index-skipcallback)
  + [bringToTop](#bringtotop)

    - [<instance> bringToTop(child)](#instance-bringtotopchild)
  + [count](#count)

    - [<instance> count(property, value)](#instance-countproperty-value)
  + [destroy](#destroy)

    - [<instance> destroy()](#instance-destroy)
  + [each](#each)

    - [<instance> each(callback, [context], [args])](#instance-eachcallback-context-args)
  + [exists](#exists)

    - [<instance> exists(child)](#instance-existschild)
  + [getAll](#getall)

    - [<instance> getAll([property], [value], [startIndex], [endIndex])](#instance-getallproperty-value-startindex-endindex)
  + [getAt](#getat)

    - [<instance> getAt(index)](#instance-getatindex)
  + [getByName](#getbyname)

    - [<instance> getByName(name)](#instance-getbynamename)
  + [getFirst](#getfirst)

    - [<instance> getFirst(property, value, [startIndex], [endIndex])](#instance-getfirstproperty-value-startindex-endindex)
  + [getIndex](#getindex)

    - [<instance> getIndex(child)](#instance-getindexchild)
  + [getRandom](#getrandom)

    - [<instance> getRandom([startIndex], [length])](#instance-getrandomstartindex-length)
  + [moveAbove](#moveabove)

    - [<instance> moveAbove(child1, child2)](#instance-moveabovechild1-child2)
  + [moveBelow](#movebelow)

    - [<instance> moveBelow(child1, child2)](#instance-movebelowchild1-child2)
  + [moveDown](#movedown)

    - [<instance> moveDown(child)](#instance-movedownchild)
  + [moveTo](#moveto)

    - [<instance> moveTo(child, index)](#instance-movetochild-index)
  + [moveUp](#moveup)

    - [<instance> moveUp(child)](#instance-moveupchild)
  + [remove](#remove)

    - [<instance> remove(child, [skipCallback])](#instance-removechild-skipcallback)
  + [removeAll](#removeall)

    - [<instance> removeAll([skipCallback])](#instance-removeallskipcallback)
  + [removeAt](#removeat)

    - [<instance> removeAt(index, [skipCallback])](#instance-removeatindex-skipcallback)
  + [removeBetween](#removebetween)

    - [<instance> removeBetween([startIndex], [endIndex], [skipCallback])](#instance-removebetweenstartindex-endindex-skipcallback)
  + [replace](#replace)

    - [<instance> replace(oldChild, newChild)](#instance-replaceoldchild-newchild)
  + [reverse](#reverse)

    - [<instance> reverse()](#instance-reverse)
  + [sendToBack](#sendtoback)

    - [<instance> sendToBack(child)](#instance-sendtobackchild)
  + [setAll](#setall)

    - [<instance> setAll(property, value, [startIndex], [endIndex])](#instance-setallproperty-value-startindex-endindex)
  + [shuffle](#shuffle)

    - [<instance> shuffle()](#instance-shuffle)
  + [shutdown](#shutdown)

    - [<instance> shutdown()](#instance-shutdown)
  + [sort](#sort)

    - [<instance> sort(property, [handler])](#instance-sortproperty-handler)
  + [swap](#swap)

    - [<instance> swap(child1, child2)](#instance-swapchild1-child2)

Back to top

©2025[Phaser](https://docs.phaser.io)