# Ellipse

Phaser.Geom.Ellipse

An Ellipse object.

This is a geometry object, containing numerical values and related methods to inspect and modify them.

It is not a Game Object, in that you cannot add it to the display list, and it has no texture.

To render an Ellipse you should look at the capabilities of the Graphics class.

**Constructor**

`new Ellipse([x], [y], [width], [height])`

**Parameters**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | Yes | 0 | The x position of the center of the ellipse. |
| --- | --- | --- | --- | --- |
| y | number | Yes | 0 | The y position of the center of the ellipse. |
| width | number | Yes | 0 | The width of the ellipse. |
| height | number | Yes | 0 | The height of the ellipse. |

---

**Scope**: static

> Source: [src/geom/ellipse/Ellipse.js#L14](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/ellipse/Ellipse.js#L14)  
> Since: 3.0.0

# Public Methods

## Area

### <static> Area(ellipse)

**Description:**

Calculates the area of the Ellipse.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| ellipse | [Phaser.Geom.Ellipse](geom-ellipse.md) | No | The Ellipse to get the area of. |
| --- | --- | --- | --- |

**Returns:** number - The area of the Ellipse.

> Source: [src/geom/ellipse/Area.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/ellipse/Area.js#L7)  
> Since: 3.0.0

---

## Circumference

### <static> Circumference(ellipse)

**Description:**

Returns the circumference of the given Ellipse.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| ellipse | [Phaser.Geom.Ellipse](geom-ellipse.md) | No | The Ellipse to get the circumference of. |
| --- | --- | --- | --- |

**Returns:** number - The circumference of th Ellipse.

> Source: [src/geom/ellipse/Circumference.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/ellipse/Circumference.js#L7)  
> Since: 3.0.0

---

## CircumferencePoint

### <static> CircumferencePoint(ellipse, angle, [out])

**Description:**

Returns a Point object containing the coordinates of a point on the circumference of the Ellipse based on the given angle.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| ellipse | [Phaser.Geom.Ellipse](geom-ellipse.md) | No | The Ellipse to get the circumference point on. |
| --- | --- | --- | --- |
| angle | number | No | The angle from the center of the Ellipse to the circumference to return the point from. Given in radians. |
| out | [Phaser.Geom.Point](geom-point.md) | object | Yes | A Point, or point-like object, to store the results in. If not given a Point will be created. |

**Returns:** [Phaser.Geom.Point](geom-point.md), object - A Point object where the `x` and `y` properties are the point on the circumference.

> Source: [src/geom/ellipse/CircumferencePoint.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/ellipse/CircumferencePoint.js#L9)  
> Since: 3.0.0

---

## Clone

### <static> Clone(source)

**Description:**

Creates a new Ellipse instance based on the values contained in the given source.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| source | [Phaser.Geom.Ellipse](geom-ellipse.md) | No | The Ellipse to be cloned. Can be an instance of an Ellipse or a ellipse-like object, with x, y, width and height properties. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Geom.Ellipse](geom-ellipse.md) - A clone of the source Ellipse.

> Source: [src/geom/ellipse/Clone.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/ellipse/Clone.js#L9)  
> Since: 3.0.0

---

## contains

### <instance> contains(x, y)

**Description:**

Check to see if the Ellipse contains the given x / y coordinates.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The x coordinate to check within the ellipse. |
| --- | --- | --- | --- |
| y | number | No | The y coordinate to check within the ellipse. |

**Returns:** boolean - True if the coordinates are within the ellipse, otherwise false.

> Source: [src/geom/ellipse/Ellipse.js#L95](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/ellipse/Ellipse.js#L95)  
> Since: 3.0.0

---

## Contains

### <static> Contains(ellipse, x, y)

**Description:**

Check to see if the Ellipse contains the given x / y coordinates.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| ellipse | [Phaser.Geom.Ellipse](geom-ellipse.md) | No | The Ellipse to check. |
| --- | --- | --- | --- |
| x | number | No | The x coordinate to check within the ellipse. |
| y | number | No | The y coordinate to check within the ellipse. |

**Returns:** boolean - True if the coordinates are within the ellipse, otherwise false.

> Source: [src/geom/ellipse/Contains.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/ellipse/Contains.js#L7)  
> Since: 3.0.0

---

## ContainsPoint

### <static> ContainsPoint(ellipse, point)

**Description:**

Check to see if the Ellipse contains the given Point object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| ellipse | [Phaser.Geom.Ellipse](geom-ellipse.md) | No | The Ellipse to check. |
| --- | --- | --- | --- |
| point | [Phaser.Geom.Point](geom-point.md) | object | No | The Point object to check if it's within the Circle or not. |

**Returns:** boolean - True if the Point coordinates are within the circle, otherwise false.

> Source: [src/geom/ellipse/ContainsPoint.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/ellipse/ContainsPoint.js#L9)  
> Since: 3.0.0

---

## ContainsRect

### <static> ContainsRect(ellipse, rect)

**Description:**

Check to see if the Ellipse contains all four points of the given Rectangle object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| ellipse | [Phaser.Geom.Ellipse](geom-ellipse.md) | No | The Ellipse to check. |
| --- | --- | --- | --- |
| rect | [Phaser.Geom.Rectangle](geom-rectangle.md) | object | No | The Rectangle object to check if it's within the Ellipse or not. |

**Returns:** boolean - True if all of the Rectangle coordinates are within the ellipse, otherwise false.

> Source: [src/geom/ellipse/ContainsRect.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/ellipse/ContainsRect.js#L9)  
> Since: 3.0.0

---

## CopyFrom

### <static> CopyFrom(source, dest)

**Description:**

Copies the `x`, `y`, `width` and `height` properties from the `source` Ellipse

into the given `dest` Ellipse, then returns the `dest` Ellipse.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| source | [Phaser.Geom.Ellipse](geom-ellipse.md) | No | The source Ellipse to copy the values from. |
| --- | --- | --- | --- |
| dest | [Phaser.Geom.Ellipse](geom-ellipse.md) | No | The destination Ellipse to copy the values to. |

**Returns:** [Phaser.Geom.Ellipse](geom-ellipse.md) - The destination Ellipse.

> Source: [src/geom/ellipse/CopyFrom.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/ellipse/CopyFrom.js#L7)  
> Since: 3.0.0

---

## Equals

### <static> Equals(ellipse, toCompare)

**Description:**

Compares the `x`, `y`, `width` and `height` properties of the two given Ellipses.

Returns `true` if they all match, otherwise returns `false`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| ellipse | [Phaser.Geom.Ellipse](geom-ellipse.md) | No | The first Ellipse to compare. |
| --- | --- | --- | --- |
| toCompare | [Phaser.Geom.Ellipse](geom-ellipse.md) | No | The second Ellipse to compare. |

**Returns:** boolean - `true` if the two Ellipse equal each other, otherwise `false`.

> Source: [src/geom/ellipse/Equals.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/ellipse/Equals.js#L7)  
> Since: 3.0.0

---

## GetBounds

### <static> GetBounds(ellipse, [out])

**Description:**

Returns the bounds of the Ellipse object.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| ellipse | [Phaser.Geom.Ellipse](geom-ellipse.md) | No | The Ellipse to get the bounds from. |
| --- | --- | --- | --- |
| out | [Phaser.Geom.Rectangle](geom-rectangle.md) | object | Yes | A Rectangle, or rectangle-like object, to store the ellipse bounds in. If not given a new Rectangle will be created. |

**Returns:** [Phaser.Geom.Rectangle](geom-rectangle.md), object - The Rectangle object containing the Ellipse bounds.

> Source: [src/geom/ellipse/GetBounds.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/ellipse/GetBounds.js#L9)  
> Since: 3.0.0

---

## getMajorRadius

### <instance> getMajorRadius()

**Description:**

Returns the major radius of the ellipse. Also known as the Semi Major Axis.

**Returns:** number - The major radius.

> Source: [src/geom/ellipse/Ellipse.js#L277](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/ellipse/Ellipse.js#L277)  
> Since: 3.0.0

---

## getMinorRadius

### <instance> getMinorRadius()

**Description:**

Returns the minor radius of the ellipse. Also known as the Semi Minor Axis.

**Returns:** number - The minor radius.

> Source: [src/geom/ellipse/Ellipse.js#L264](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/ellipse/Ellipse.js#L264)  
> Since: 3.0.0

---

## getPoint

### <instance> getPoint(position, [out])

**Description:**

Returns a Point object containing the coordinates of a point on the circumference of the Ellipse

based on the given angle normalized to the range 0 to 1. I.e. a value of 0.5 will give the point

at 180 degrees around the circle.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| position | number | No | A value between 0 and 1, where 0 equals 0 degrees, 0.5 equals 180 degrees and 1 equals 360 around the ellipse. |
| --- | --- | --- | --- |
| out | [Phaser.Geom.Point](geom-point.md) | object | Yes | An object to store the return values in. If not given a Point object will be created. |

**Returns:** [Phaser.Geom.Point](geom-point.md), object - A Point, or point-like object, containing the coordinates of the point around the ellipse.

> Source: [src/geom/ellipse/Ellipse.js#L111](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/ellipse/Ellipse.js#L111)  
> Since: 3.0.0

---

## GetPoint

### <static> GetPoint(ellipse, position, [out])

**Description:**

Returns a Point object containing the coordinates of a point on the circumference of the Ellipse

based on the given angle normalized to the range 0 to 1. I.e. a value of 0.5 will give the point

at 180 degrees around the circle.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| ellipse | [Phaser.Geom.Ellipse](geom-ellipse.md) | No | The Ellipse to get the circumference point on. |
| --- | --- | --- | --- |
| position | number | No | A value between 0 and 1, where 0 equals 0 degrees, 0.5 equals 180 degrees and 1 equals 360 around the ellipse. |
| out | [Phaser.Geom.Point](geom-point.md) | object | Yes | An object to store the return values in. If not given a Point object will be created. |

**Returns:** [Phaser.Geom.Point](geom-point.md), object - A Point, or point-like object, containing the coordinates of the point around the ellipse.

> Source: [src/geom/ellipse/GetPoint.js#L12](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/ellipse/GetPoint.js#L12)  
> Since: 3.0.0

---

## getPoints

### <instance> getPoints(quantity, [stepRate], [output])

**Description:**

Returns an array of Point objects containing the coordinates of the points around the circumference of the Ellipse,

based on the given quantity or stepRate values.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| quantity | number | No | The amount of points to return. If a falsey value the quantity will be derived from the `stepRate` instead. |
| --- | --- | --- | --- |
| stepRate | number | Yes | Sets the quantity by getting the circumference of the ellipse and dividing it by the stepRate. |
| output | array | Array.<[Phaser.Geom.Point](geom-point.md)> | Yes | An array to insert the points in to. If not provided a new array will be created. |

**Returns:** array, Array.<[Phaser.Geom.Point](geom-point.md)> - An array of Point objects pertaining to the points around the circumference of the ellipse.

> Source: [src/geom/ellipse/Ellipse.js#L131](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/ellipse/Ellipse.js#L131)  
> Since: 3.0.0

---

## GetPoints

### <static> GetPoints(ellipse, quantity, [stepRate], [out])

**Description:**

Returns an array of Point objects containing the coordinates of the points around the circumference of the Ellipse,

based on the given quantity or stepRate values.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| ellipse | [Phaser.Geom.Ellipse](geom-ellipse.md) | No | The Ellipse to get the points from. |
| --- | --- | --- | --- |
| quantity | number | No | The amount of points to return. If a falsey value the quantity will be derived from the `stepRate` instead. |
| stepRate | number | Yes | Sets the quantity by getting the circumference of the ellipse and dividing it by the stepRate. |
| out | array | Array.<[Phaser.Geom.Point](geom-point.md)> | Yes | An array to insert the points in to. If not provided a new array will be created. |

**Returns:** array, Array.<[Phaser.Geom.Point](geom-point.md)> - An array of Point objects pertaining to the points around the circumference of the ellipse.

> Source: [src/geom/ellipse/GetPoints.js#L12](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/ellipse/GetPoints.js#L12)  
> Since: 3.0.0

---

## getRandomPoint

### <instance> getRandomPoint([point])

**Description:**

Returns a uniformly distributed random point from anywhere within the given Ellipse.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| point | [Phaser.Geom.Point](geom-point.md) | object | Yes | A Point or point-like object to set the random `x` and `y` values in. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Geom.Point](geom-point.md), object - A Point object with the random values set in the `x` and `y` properties.

> Source: [src/geom/ellipse/Ellipse.js#L151](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/ellipse/Ellipse.js#L151)  
> Since: 3.0.0

---

## isEmpty

### <instance> isEmpty()

**Description:**

Checks to see if the Ellipse is empty: has a width or height equal to zero.

**Returns:** boolean - True if the Ellipse is empty, otherwise false.

> Source: [src/geom/ellipse/Ellipse.js#L251](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/ellipse/Ellipse.js#L251)  
> Since: 3.0.0

---

## Offset

### <static> Offset(ellipse, x, y)

**Description:**

Offsets the Ellipse by the values given.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| ellipse | [Phaser.Geom.Ellipse](geom-ellipse.md) | No | The Ellipse to be offset (translated.) |
| --- | --- | --- | --- |
| x | number | No | The amount to horizontally offset the Ellipse by. |
| y | number | No | The amount to vertically offset the Ellipse by. |

**Returns:** [Phaser.Geom.Ellipse](geom-ellipse.md) - The Ellipse that was offset.

> Source: [src/geom/ellipse/Offset.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/ellipse/Offset.js#L7)  
> Since: 3.0.0

---

## OffsetPoint

### <static> OffsetPoint(ellipse, point)

**Description:**

Offsets the Ellipse by the values given in the `x` and `y` properties of the Point object.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| ellipse | [Phaser.Geom.Ellipse](geom-ellipse.md) | No | The Ellipse to be offset (translated.) |
| --- | --- | --- | --- |
| point | [Phaser.Geom.Point](geom-point.md) | object | No | The Point object containing the values to offset the Ellipse by. |

**Returns:** [Phaser.Geom.Ellipse](geom-ellipse.md) - The Ellipse that was offset.

> Source: [src/geom/ellipse/OffsetPoint.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/ellipse/OffsetPoint.js#L7)  
> Since: 3.0.0

---

## Random

### <static> Random(ellipse, [out])

**Description:**

Returns a uniformly distributed random point from anywhere within the given Ellipse.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| ellipse | [Phaser.Geom.Ellipse](geom-ellipse.md) | No | The Ellipse to get a random point from. |
| --- | --- | --- | --- |
| out | [Phaser.Geom.Point](geom-point.md) | object | Yes | A Point or point-like object to set the random `x` and `y` values in. |

**Returns:** [Phaser.Geom.Point](geom-point.md), object - A Point object with the random values set in the `x` and `y` properties.

> Source: [src/geom/ellipse/Random.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/ellipse/Random.js#L9)  
> Since: 3.0.0

---

## setEmpty

### <instance> setEmpty()

**Description:**

Sets this Ellipse to be empty with a width and height of zero.

Does not change its position.

**Returns:** [Phaser.Geom.Ellipse](geom-ellipse.md) - This Ellipse object.

> Source: [src/geom/ellipse/Ellipse.js#L191](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/ellipse/Ellipse.js#L191)  
> Since: 3.0.0

---

## setPosition

### <instance> setPosition(x, y)

**Description:**

Sets the position of this Ellipse.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The x position of the center of the ellipse. |
| --- | --- | --- | --- |
| y | number | No | The y position of the center of the ellipse. |

**Returns:** [Phaser.Geom.Ellipse](geom-ellipse.md) - This Ellipse object.

> Source: [src/geom/ellipse/Ellipse.js#L208](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/ellipse/Ellipse.js#L208)  
> Since: 3.0.0

---

## setSize

### <instance> setSize(width, [height])

**Description:**

Sets the size of this Ellipse.

Does not change its position.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| width | number | No |  | The width of the ellipse. |
| --- | --- | --- | --- | --- |
| height | number | Yes | "width" | The height of the ellipse. |

**Returns:** [Phaser.Geom.Ellipse](geom-ellipse.md) - This Ellipse object.

> Source: [src/geom/ellipse/Ellipse.js#L229](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/ellipse/Ellipse.js#L229)  
> Since: 3.0.0

---

## setTo

### <instance> setTo(x, y, width, height)

**Description:**

Sets the x, y, width and height of this ellipse.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The x position of the center of the ellipse. |
| --- | --- | --- | --- |
| y | number | No | The y position of the center of the ellipse. |
| width | number | No | The width of the ellipse. |
| height | number | No | The height of the ellipse. |

**Returns:** [Phaser.Geom.Ellipse](geom-ellipse.md) - This Ellipse object.

> Source: [src/geom/ellipse/Ellipse.js#L168](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/ellipse/Ellipse.js#L168)  
> Since: 3.0.0

---

# Public Members

## bottom

### bottom: number

**Description:**

The bottom position of the Ellipse.

> Source: [src/geom/ellipse/Ellipse.js#L353](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/ellipse/Ellipse.js#L353)  
> Since: 3.0.0

---

## height

### height: number

**Description:**

The height of the ellipse.

> Source: [src/geom/ellipse/Ellipse.js#L84](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/ellipse/Ellipse.js#L84)  
> Since: 3.0.0

---

## left

### left: number

**Description:**

The left position of the Ellipse.

> Source: [src/geom/ellipse/Ellipse.js#L290](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/ellipse/Ellipse.js#L290)  
> Since: 3.0.0

---

## right

### right: number

**Description:**

The right position of the Ellipse.

> Source: [src/geom/ellipse/Ellipse.js#L311](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/ellipse/Ellipse.js#L311)  
> Since: 3.0.0

---

## top

### top: number

**Description:**

The top position of the Ellipse.

> Source: [src/geom/ellipse/Ellipse.js#L332](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/ellipse/Ellipse.js#L332)  
> Since: 3.0.0

---

## type

### type: number

**Description:**

The geometry constant type of this object: `GEOM_CONST.ELLIPSE`.

Used for fast type comparisons.

> Source: [src/geom/ellipse/Ellipse.js#L43](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/ellipse/Ellipse.js#L43)  
> Since: 3.19.0

---

## width

### width: number

**Description:**

The width of the ellipse.

> Source: [src/geom/ellipse/Ellipse.js#L74](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/ellipse/Ellipse.js#L74)  
> Since: 3.0.0

---

## x

### x: number

**Description:**

The x position of the center of the ellipse.

> Source: [src/geom/ellipse/Ellipse.js#L54](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/ellipse/Ellipse.js#L54)  
> Since: 3.0.0

---

## y

### y: number

**Description:**

The y position of the center of the ellipse.

> Source: [src/geom/ellipse/Ellipse.js#L64](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/ellipse/Ellipse.js#L64)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Methods](#public-methods)

  + [Area](#area)

    - [<static> Area(ellipse)](#static-areaellipse)
  + [Circumference](#circumference)

    - [<static> Circumference(ellipse)](#static-circumferenceellipse)
  + [CircumferencePoint](#circumferencepoint)

    - [<static> CircumferencePoint(ellipse, angle, [out])](#static-circumferencepointellipse-angle-out)
  + [Clone](#clone)

    - [<static> Clone(source)](#static-clonesource)
  + [contains](#contains)

    - [<instance> contains(x, y)](#instance-containsx-y)
  + [Contains](#contains-1)

    - [<static> Contains(ellipse, x, y)](#static-containsellipse-x-y)
  + [ContainsPoint](#containspoint)

    - [<static> ContainsPoint(ellipse, point)](#static-containspointellipse-point)
  + [ContainsRect](#containsrect)

    - [<static> ContainsRect(ellipse, rect)](#static-containsrectellipse-rect)
  + [CopyFrom](#copyfrom)

    - [<static> CopyFrom(source, dest)](#static-copyfromsource-dest)
  + [Equals](#equals)

    - [<static> Equals(ellipse, toCompare)](#static-equalsellipse-tocompare)
  + [GetBounds](#getbounds)

    - [<static> GetBounds(ellipse, [out])](#static-getboundsellipse-out)
  + [getMajorRadius](#getmajorradius)

    - [<instance> getMajorRadius()](#instance-getmajorradius)
  + [getMinorRadius](#getminorradius)

    - [<instance> getMinorRadius()](#instance-getminorradius)
  + [getPoint](#getpoint)

    - [<instance> getPoint(position, [out])](#instance-getpointposition-out)
  + [GetPoint](#getpoint-1)

    - [<static> GetPoint(ellipse, position, [out])](#static-getpointellipse-position-out)
  + [getPoints](#getpoints)

    - [<instance> getPoints(quantity, [stepRate], [output])](#instance-getpointsquantity-steprate-output)
  + [GetPoints](#getpoints-1)

    - [<static> GetPoints(ellipse, quantity, [stepRate], [out])](#static-getpointsellipse-quantity-steprate-out)
  + [getRandomPoint](#getrandompoint)

    - [<instance> getRandomPoint([point])](#instance-getrandompointpoint)
  + [isEmpty](#isempty)

    - [<instance> isEmpty()](#instance-isempty)
  + [Offset](#offset)

    - [<static> Offset(ellipse, x, y)](#static-offsetellipse-x-y)
  + [OffsetPoint](#offsetpoint)

    - [<static> OffsetPoint(ellipse, point)](#static-offsetpointellipse-point)
  + [Random](#random)

    - [<static> Random(ellipse, [out])](#static-randomellipse-out)
  + [setEmpty](#setempty)

    - [<instance> setEmpty()](#instance-setempty)
  + [setPosition](#setposition)

    - [<instance> setPosition(x, y)](#instance-setpositionx-y)
  + [setSize](#setsize)

    - [<instance> setSize(width, [height])](#instance-setsizewidth-height)
  + [setTo](#setto)

    - [<instance> setTo(x, y, width, height)](#instance-settox-y-width-height)
* [Public Members](#public-members)

  + [bottom](#bottom)

    - [bottom: number](#bottom-number)
  + [height](#height)

    - [height: number](#height-number)
  + [left](#left)

    - [left: number](#left-number)
  + [right](#right)

    - [right: number](#right-number)
  + [top](#top)

    - [top: number](#top-number)
  + [type](#type)

    - [type: number](#type-number)
  + [width](#width)

    - [width: number](#width-number)
  + [x](#x)

    - [x: number](#x-number)
  + [y](#y)

    - [y: number](#y-number)

Back to top

©2025[Phaser](https://docs.phaser.io)