# Circle

Phaser.Geom.Circle

A Circle object.

This is a geometry object, containing numerical values and related methods to inspect and modify them.

It is not a Game Object, in that you cannot add it to the display list, and it has no texture.

To render a Circle you should look at the capabilities of the Graphics class.

**Constructor**

`new Circle([x], [y], [radius])`

**Parameters**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | Yes | 0 | The x position of the center of the circle. |
| --- | --- | --- | --- | --- |
| y | number | Yes | 0 | The y position of the center of the circle. |
| radius | number | Yes | 0 | The radius of the circle. |

---

**Scope**: static

> Source: [src/geom/circle/Circle.js#L14](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/circle/Circle.js#L14)  
> Since: 3.0.0

# Public Methods

## Area

### <static> Area(circle)

**Description:**

Calculates the area of the circle.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| circle | [Phaser.Geom.Circle](geom-circle.md) | No | The Circle to get the area of. |
| --- | --- | --- | --- |

**Returns:** number - The area of the Circle.

> Source: [src/geom/circle/Area.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/circle/Area.js#L7)  
> Since: 3.0.0

---

## Circumference

### <static> Circumference(circle)

**Description:**

Returns the circumference of the given Circle.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| circle | [Phaser.Geom.Circle](geom-circle.md) | No | The Circle to get the circumference of. |
| --- | --- | --- | --- |

**Returns:** number - The circumference of the Circle.

> Source: [src/geom/circle/Circumference.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/circle/Circumference.js#L7)  
> Since: 3.0.0

---

## CircumferencePoint

### <static> CircumferencePoint(circle, angle, [out])

**Description:**

Returns a Point object containing the coordinates of a point on the circumference of the Circle based on the given angle.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| circle | [Phaser.Geom.Circle](geom-circle.md) | No | The Circle to get the circumference point on. |
| --- | --- | --- | --- |
| angle | number | No | The angle from the center of the Circle to the circumference to return the point from. Given in radians. |
| out | [Phaser.Geom.Point](geom-point.md) | object | Yes | A Point, or point-like object, to store the results in. If not given a Point will be created. |

**Returns:** [Phaser.Geom.Point](geom-point.md), object - A Point object where the `x` and `y` properties are the point on the circumference.

> Source: [src/geom/circle/CircumferencePoint.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/circle/CircumferencePoint.js#L9)  
> Since: 3.0.0

---

## Clone

### <static> Clone(source)

**Description:**

Creates a new Circle instance based on the values contained in the given source.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| source | [Phaser.Geom.Circle](geom-circle.md) | object | No | The Circle to be cloned. Can be an instance of a Circle or a circle-like object, with x, y and radius properties. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Geom.Circle](geom-circle.md) - A clone of the source Circle.

> Source: [src/geom/circle/Clone.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/circle/Clone.js#L9)  
> Since: 3.0.0

---

## contains

### <instance> contains(x, y)

**Description:**

Check to see if the Circle contains the given x / y coordinates.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The x coordinate to check within the circle. |
| --- | --- | --- | --- |
| y | number | No | The y coordinate to check within the circle. |

**Returns:** boolean - True if the coordinates are within the circle, otherwise false.

> Source: [src/geom/circle/Circle.js#L93](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/circle/Circle.js#L93)  
> Since: 3.0.0

---

## Contains

### <static> Contains(circle, x, y)

**Description:**

Check to see if the Circle contains the given x / y coordinates.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| circle | [Phaser.Geom.Circle](geom-circle.md) | No | The Circle to check. |
| --- | --- | --- | --- |
| x | number | No | The x coordinate to check within the circle. |
| y | number | No | The y coordinate to check within the circle. |

**Returns:** boolean - True if the coordinates are within the circle, otherwise false.

> Source: [src/geom/circle/Contains.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/circle/Contains.js#L7)  
> Since: 3.0.0

---

## ContainsPoint

### <static> ContainsPoint(circle, point)

**Description:**

Check to see if the Circle contains the given Point object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| circle | [Phaser.Geom.Circle](geom-circle.md) | No | The Circle to check. |
| --- | --- | --- | --- |
| point | [Phaser.Geom.Point](geom-point.md) | object | No | The Point object to check if it's within the Circle or not. |

**Returns:** boolean - True if the Point coordinates are within the circle, otherwise false.

> Source: [src/geom/circle/ContainsPoint.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/circle/ContainsPoint.js#L9)  
> Since: 3.0.0

---

## ContainsRect

### <static> ContainsRect(circle, rect)

**Description:**

Check to see if the Circle contains all four points of the given Rectangle object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| circle | [Phaser.Geom.Circle](geom-circle.md) | No | The Circle to check. |
| --- | --- | --- | --- |
| rect | [Phaser.Geom.Rectangle](geom-rectangle.md) | object | No | The Rectangle object to check if it's within the Circle or not. |

**Returns:** boolean - True if all of the Rectangle coordinates are within the circle, otherwise false.

> Source: [src/geom/circle/ContainsRect.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/circle/ContainsRect.js#L9)  
> Since: 3.0.0

---

## CopyFrom

### <static> CopyFrom(source, dest)

**Description:**

Copies the `x`, `y` and `radius` properties from the `source` Circle

into the given `dest` Circle, then returns the `dest` Circle.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| source | [Phaser.Geom.Circle](geom-circle.md) | No | The source Circle to copy the values from. |
| --- | --- | --- | --- |
| dest | [Phaser.Geom.Circle](geom-circle.md) | No | The destination Circle to copy the values to. |

**Returns:** [Phaser.Geom.Circle](geom-circle.md) - The destination Circle.

> Source: [src/geom/circle/CopyFrom.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/circle/CopyFrom.js#L7)  
> Since: 3.0.0

---

## Equals

### <static> Equals(circle, toCompare)

**Description:**

Compares the `x`, `y` and `radius` properties of the two given Circles.

Returns `true` if they all match, otherwise returns `false`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| circle | [Phaser.Geom.Circle](geom-circle.md) | No | The first Circle to compare. |
| --- | --- | --- | --- |
| toCompare | [Phaser.Geom.Circle](geom-circle.md) | No | The second Circle to compare. |

**Returns:** boolean - `true` if the two Circles equal each other, otherwise `false`.

> Source: [src/geom/circle/Equals.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/circle/Equals.js#L7)  
> Since: 3.0.0

---

## GetBounds

### <static> GetBounds(circle, [out])

**Description:**

Returns the bounds of the Circle object.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| circle | [Phaser.Geom.Circle](geom-circle.md) | No | The Circle to get the bounds from. |
| --- | --- | --- | --- |
| out | [Phaser.Geom.Rectangle](geom-rectangle.md) | object | Yes | A Rectangle, or rectangle-like object, to store the circle bounds in. If not given a new Rectangle will be created. |

**Returns:** [Phaser.Geom.Rectangle](geom-rectangle.md), object - The Rectangle object containing the Circles bounds.

> Source: [src/geom/circle/GetBounds.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/circle/GetBounds.js#L9)  
> Since: 3.0.0

---

## getPoint

### <instance> getPoint(position, [out])

**Description:**

Returns a Point object containing the coordinates of a point on the circumference of the Circle

based on the given angle normalized to the range 0 to 1. I.e. a value of 0.5 will give the point

at 180 degrees around the circle.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| position | number | No | A value between 0 and 1, where 0 equals 0 degrees, 0.5 equals 180 degrees and 1 equals 360 around the circle. |
| --- | --- | --- | --- |
| out | [Phaser.Geom.Point](geom-point.md) | object | Yes | An object to store the return values in. If not given a Point object will be created. |

**Returns:** [Phaser.Geom.Point](geom-point.md), object - A Point, or point-like object, containing the coordinates of the point around the circle.

> Source: [src/geom/circle/Circle.js#L109](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/circle/Circle.js#L109)  
> Since: 3.0.0

---

## GetPoint

### <static> GetPoint(circle, position, [out])

**Description:**

Returns a Point object containing the coordinates of a point on the circumference of the Circle

based on the given angle normalized to the range 0 to 1. I.e. a value of 0.5 will give the point

at 180 degrees around the circle.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| circle | [Phaser.Geom.Circle](geom-circle.md) | No | The Circle to get the circumference point on. |
| --- | --- | --- | --- |
| position | number | No | A value between 0 and 1, where 0 equals 0 degrees, 0.5 equals 180 degrees and 1 equals 360 around the circle. |
| out | [Phaser.Geom.Point](geom-point.md) | object | Yes | An object to store the return values in. If not given a Point object will be created. |

**Returns:** [Phaser.Geom.Point](geom-point.md), object - A Point, or point-like object, containing the coordinates of the point around the circle.

> Source: [src/geom/circle/GetPoint.js#L12](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/circle/GetPoint.js#L12)  
> Since: 3.0.0

---

## getPoints

### <instance> getPoints(quantity, [stepRate], [output])

**Description:**

Returns an array of Point objects containing the coordinates of the points around the circumference of the Circle,

based on the given quantity or stepRate values.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| quantity | number | No | The amount of points to return. If a falsey value the quantity will be derived from the `stepRate` instead. |
| --- | --- | --- | --- |
| stepRate | number | Yes | Sets the quantity by getting the circumference of the circle and dividing it by the stepRate. |
| output | array | Array.<[Phaser.Geom.Point](geom-point.md)> | Yes | An array to insert the points in to. If not provided a new array will be created. |

**Returns:** array, Array.<[Phaser.Geom.Point](geom-point.md)> - An array of Point objects pertaining to the points around the circumference of the circle.

> Source: [src/geom/circle/Circle.js#L129](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/circle/Circle.js#L129)  
> Since: 3.0.0

---

## GetPoints

### <static> GetPoints(circle, quantity, [stepRate], [output])

**Description:**

Returns an array of Point objects containing the coordinates of the points around the circumference of the Circle,

based on the given quantity or stepRate values.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| circle | [Phaser.Geom.Circle](geom-circle.md) | No | The Circle to get the points from. |
| --- | --- | --- | --- |
| quantity | number | No | The amount of points to return. If a falsey value the quantity will be derived from the `stepRate` instead. |
| stepRate | number | Yes | Sets the quantity by getting the circumference of the circle and dividing it by the stepRate. |
| output | array | Yes | An array to insert the points in to. If not provided a new array will be created. |

**Returns:** Array.<[Phaser.Geom.Point](geom-point.md)> - An array of Point objects pertaining to the points around the circumference of the circle.

> Source: [src/geom/circle/GetPoints.js#L12](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/circle/GetPoints.js#L12)  
> Since: 3.0.0

---

## getRandomPoint

### <instance> getRandomPoint([point])

**Description:**

Returns a uniformly distributed random point from anywhere within the Circle.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| point | [Phaser.Geom.Point](geom-point.md) | object | Yes | A Point or point-like object to set the random `x` and `y` values in. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Geom.Point](geom-point.md), object - A Point object with the random values set in the `x` and `y` properties.

> Source: [src/geom/circle/Circle.js#L149](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/circle/Circle.js#L149)  
> Since: 3.0.0

---

## isEmpty

### <instance> isEmpty()

**Description:**

Checks to see if the Circle is empty: has a radius of zero.

**Returns:** boolean - True if the Circle is empty, otherwise false.

> Source: [src/geom/circle/Circle.js#L226](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/circle/Circle.js#L226)  
> Since: 3.0.0

---

## Offset

### <static> Offset(circle, x, y)

**Description:**

Offsets the Circle by the values given.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| circle | [Phaser.Geom.Circle](geom-circle.md) | No | The Circle to be offset (translated.) |
| --- | --- | --- | --- |
| x | number | No | The amount to horizontally offset the Circle by. |
| y | number | No | The amount to vertically offset the Circle by. |

**Returns:** [Phaser.Geom.Circle](geom-circle.md) - The Circle that was offset.

> Source: [src/geom/circle/Offset.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/circle/Offset.js#L7)  
> Since: 3.0.0

---

## OffsetPoint

### <static> OffsetPoint(circle, point)

**Description:**

Offsets the Circle by the values given in the `x` and `y` properties of the Point object.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| circle | [Phaser.Geom.Circle](geom-circle.md) | No | The Circle to be offset (translated.) |
| --- | --- | --- | --- |
| point | [Phaser.Geom.Point](geom-point.md) | object | No | The Point object containing the values to offset the Circle by. |

**Returns:** [Phaser.Geom.Circle](geom-circle.md) - The Circle that was offset.

> Source: [src/geom/circle/OffsetPoint.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/circle/OffsetPoint.js#L7)  
> Since: 3.0.0

---

## Random

### <static> Random(circle, [out])

**Description:**

Returns a uniformly distributed random point from anywhere within the given Circle.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| circle | [Phaser.Geom.Circle](geom-circle.md) | No | The Circle to get a random point from. |
| --- | --- | --- | --- |
| out | [Phaser.Geom.Point](geom-point.md) | object | Yes | A Point or point-like object to set the random `x` and `y` values in. |

**Returns:** [Phaser.Geom.Point](geom-point.md), object - A Point object with the random values set in the `x` and `y` properties.

> Source: [src/geom/circle/Random.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/circle/Random.js#L9)  
> Since: 3.0.0

---

## setEmpty

### <instance> setEmpty()

**Description:**

Sets this Circle to be empty with a radius of zero.

Does not change its position.

**Returns:** [Phaser.Geom.Circle](geom-circle.md) - This Circle object.

> Source: [src/geom/circle/Circle.js#L188](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/circle/Circle.js#L188)  
> Since: 3.0.0

---

## setPosition

### <instance> setPosition([x], [y])

**Description:**

Sets the position of this Circle.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | Yes | 0 | The x position of the center of the circle. |
| --- | --- | --- | --- | --- |
| y | number | Yes | 0 | The y position of the center of the circle. |

**Returns:** [Phaser.Geom.Circle](geom-circle.md) - This Circle object.

> Source: [src/geom/circle/Circle.js#L205](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/circle/Circle.js#L205)  
> Since: 3.0.0

---

## setTo

### <instance> setTo([x], [y], [radius])

**Description:**

Sets the x, y and radius of this circle.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | Yes | 0 | The x position of the center of the circle. |
| --- | --- | --- | --- | --- |
| y | number | Yes | 0 | The y position of the center of the circle. |
| radius | number | Yes | 0 | The radius of the circle. |

**Returns:** [Phaser.Geom.Circle](geom-circle.md) - This Circle object.

> Source: [src/geom/circle/Circle.js#L166](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/circle/Circle.js#L166)  
> Since: 3.0.0

---

# Public Members

## bottom

### bottom: number

**Description:**

The bottom position of the Circle.

> Source: [src/geom/circle/Circle.js#L346](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/circle/Circle.js#L346)  
> Since: 3.0.0

---

## diameter

### diameter: number

**Description:**

The diameter of the Circle.

> Source: [src/geom/circle/Circle.js#L261](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/circle/Circle.js#L261)  
> Since: 3.0.0

---

## left

### left: number

**Description:**

The left position of the Circle.

> Source: [src/geom/circle/Circle.js#L283](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/circle/Circle.js#L283)  
> Since: 3.0.0

---

## radius

### radius: number

**Description:**

The radius of the Circle.

> Source: [src/geom/circle/Circle.js#L239](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/circle/Circle.js#L239)  
> Since: 3.0.0

---

## right

### right: number

**Description:**

The right position of the Circle.

> Source: [src/geom/circle/Circle.js#L304](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/circle/Circle.js#L304)  
> Since: 3.0.0

---

## top

### top: number

**Description:**

The top position of the Circle.

> Source: [src/geom/circle/Circle.js#L325](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/circle/Circle.js#L325)  
> Since: 3.0.0

---

## type

### type: number

**Description:**

The geometry constant type of this object: `GEOM_CONST.CIRCLE`.

Used for fast type comparisons.

> Source: [src/geom/circle/Circle.js#L41](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/circle/Circle.js#L41)  
> Since: 3.19.0

---

## x

### x: number

**Description:**

The x position of the center of the circle.

> Source: [src/geom/circle/Circle.js#L52](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/circle/Circle.js#L52)  
> Since: 3.0.0

---

## y

### y: number

**Description:**

The y position of the center of the circle.

> Source: [src/geom/circle/Circle.js#L62](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/circle/Circle.js#L62)  
> Since: 3.0.0

---

# Private Members

## \_diameter

### \_diameter: number

**Description:**

The internal diameter of the circle.

**Access:** private

> Source: [src/geom/circle/Circle.js#L82](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/circle/Circle.js#L82)  
> Since: 3.0.0

---

## \_radius

### \_radius: number

**Description:**

The internal radius of the circle.

**Access:** private

> Source: [src/geom/circle/Circle.js#L72](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/circle/Circle.js#L72)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Methods](#public-methods)

  + [Area](#area)

    - [<static> Area(circle)](#static-areacircle)
  + [Circumference](#circumference)

    - [<static> Circumference(circle)](#static-circumferencecircle)
  + [CircumferencePoint](#circumferencepoint)

    - [<static> CircumferencePoint(circle, angle, [out])](#static-circumferencepointcircle-angle-out)
  + [Clone](#clone)

    - [<static> Clone(source)](#static-clonesource)
  + [contains](#contains)

    - [<instance> contains(x, y)](#instance-containsx-y)
  + [Contains](#contains-1)

    - [<static> Contains(circle, x, y)](#static-containscircle-x-y)
  + [ContainsPoint](#containspoint)

    - [<static> ContainsPoint(circle, point)](#static-containspointcircle-point)
  + [ContainsRect](#containsrect)

    - [<static> ContainsRect(circle, rect)](#static-containsrectcircle-rect)
  + [CopyFrom](#copyfrom)

    - [<static> CopyFrom(source, dest)](#static-copyfromsource-dest)
  + [Equals](#equals)

    - [<static> Equals(circle, toCompare)](#static-equalscircle-tocompare)
  + [GetBounds](#getbounds)

    - [<static> GetBounds(circle, [out])](#static-getboundscircle-out)
  + [getPoint](#getpoint)

    - [<instance> getPoint(position, [out])](#instance-getpointposition-out)
  + [GetPoint](#getpoint-1)

    - [<static> GetPoint(circle, position, [out])](#static-getpointcircle-position-out)
  + [getPoints](#getpoints)

    - [<instance> getPoints(quantity, [stepRate], [output])](#instance-getpointsquantity-steprate-output)
  + [GetPoints](#getpoints-1)

    - [<static> GetPoints(circle, quantity, [stepRate], [output])](#static-getpointscircle-quantity-steprate-output)
  + [getRandomPoint](#getrandompoint)

    - [<instance> getRandomPoint([point])](#instance-getrandompointpoint)
  + [isEmpty](#isempty)

    - [<instance> isEmpty()](#instance-isempty)
  + [Offset](#offset)

    - [<static> Offset(circle, x, y)](#static-offsetcircle-x-y)
  + [OffsetPoint](#offsetpoint)

    - [<static> OffsetPoint(circle, point)](#static-offsetpointcircle-point)
  + [Random](#random)

    - [<static> Random(circle, [out])](#static-randomcircle-out)
  + [setEmpty](#setempty)

    - [<instance> setEmpty()](#instance-setempty)
  + [setPosition](#setposition)

    - [<instance> setPosition([x], [y])](#instance-setpositionx-y)
  + [setTo](#setto)

    - [<instance> setTo([x], [y], [radius])](#instance-settox-y-radius)
* [Public Members](#public-members)

  + [bottom](#bottom)

    - [bottom: number](#bottom-number)
  + [diameter](#diameter)

    - [diameter: number](#diameter-number)
  + [left](#left)

    - [left: number](#left-number)
  + [radius](#radius)

    - [radius: number](#radius-number)
  + [right](#right)

    - [right: number](#right-number)
  + [top](#top)

    - [top: number](#top-number)
  + [type](#type)

    - [type: number](#type-number)
  + [x](#x)

    - [x: number](#x-number)
  + [y](#y)

    - [y: number](#y-number)
* [Private Members](#private-members)

  + [\_diameter](#_diameter)

    - [\_diameter: number](#_diameter-number)
  + [\_radius](#_radius)

    - [\_radius: number](#_radius-number)

Back to top

©2025[Phaser](https://docs.phaser.io)



Circle