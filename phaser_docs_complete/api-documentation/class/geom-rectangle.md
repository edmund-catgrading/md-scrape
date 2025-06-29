# Rectangle

Phaser.Geom.Rectangle

Encapsulates a 2D rectangle defined by its corner point in the top-left and its extends in x (width) and y (height)

**Constructor**

`new Rectangle([x], [y], [width], [height])`

**Parameters**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | Yes | 0 | The X coordinate of the top left corner of the Rectangle. |
| --- | --- | --- | --- | --- |
| y | number | Yes | 0 | The Y coordinate of the top left corner of the Rectangle. |
| width | number | Yes | 0 | The width of the Rectangle. |
| height | number | Yes | 0 | The height of the Rectangle. |

---

**Scope**: static

> Source: [src/geom/rectangle/Rectangle.js#L15](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/Rectangle.js#L15)  
> Since: 3.0.0

# Public Methods

## Area

### <static> Area(rect)

**Description:**

Calculates the area of the given Rectangle object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| rect | [Phaser.Geom.Rectangle](geom-rectangle.md) | No | The rectangle to calculate the area of. |
| --- | --- | --- | --- |

**Returns:** number - The area of the Rectangle object.

> Source: [src/geom/rectangle/Area.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/Area.js#L7)  
> Since: 3.0.0

---

## Ceil

### <static> Ceil(rect)

**Description:**

Rounds a Rectangle's position up to the smallest integer greater than or equal to each current coordinate.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| rect | [Phaser.Geom.Rectangle](geom-rectangle.md) | No | The Rectangle to adjust. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Geom.Rectangle](geom-rectangle.md) - The adjusted Rectangle.

> Source: [src/geom/rectangle/Ceil.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/Ceil.js#L7)  
> Since: 3.0.0

---

## CeilAll

### <static> CeilAll(rect)

**Description:**

Rounds a Rectangle's position and size up to the smallest integer greater than or equal to each respective value.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| rect | [Phaser.Geom.Rectangle](geom-rectangle.md) | No | The Rectangle to modify. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Geom.Rectangle](geom-rectangle.md) - The modified Rectangle.

> Source: [src/geom/rectangle/CeilAll.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/CeilAll.js#L7)  
> Since: 3.0.0

---

## CenterOn

### <static> CenterOn(rect, x, y)

**Description:**

Moves the top-left corner of a Rectangle so that its center is at the given coordinates.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| rect | [Phaser.Geom.Rectangle](geom-rectangle.md) | No | The Rectangle to be centered. |
| --- | --- | --- | --- |
| x | number | No | The X coordinate of the Rectangle's center. |
| y | number | No | The Y coordinate of the Rectangle's center. |

**Returns:** [Phaser.Geom.Rectangle](geom-rectangle.md) - The centered rectangle.

> Source: [src/geom/rectangle/CenterOn.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/CenterOn.js#L7)  
> Since: 3.0.0

---

## Clone

### <static> Clone(source)

**Description:**

Creates a new Rectangle which is identical to the given one.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| source | [Phaser.Geom.Rectangle](geom-rectangle.md) | No | The Rectangle to clone. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Geom.Rectangle](geom-rectangle.md) - The newly created Rectangle, which is separate from the given one.

> Source: [src/geom/rectangle/Clone.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/Clone.js#L9)  
> Since: 3.0.0

---

## contains

### <instance> contains(x, y)

**Description:**

Checks if the given point is inside the Rectangle's bounds.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The X coordinate of the point to check. |
| --- | --- | --- | --- |
| y | number | No | The Y coordinate of the point to check. |

**Returns:** boolean - `true` if the point is within the Rectangle's bounds, otherwise `false`.

> Source: [src/geom/rectangle/Rectangle.js#L92](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/Rectangle.js#L92)  
> Since: 3.0.0

---

## Contains

### <static> Contains(rect, x, y)

**Description:**

Checks if a given point is inside a Rectangle's bounds.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| rect | [Phaser.Geom.Rectangle](geom-rectangle.md) | No | The Rectangle to check. |
| --- | --- | --- | --- |
| x | number | No | The X coordinate of the point to check. |
| y | number | No | The Y coordinate of the point to check. |

**Returns:** boolean - `true` if the point is within the Rectangle's bounds, otherwise `false`.

> Source: [src/geom/rectangle/Contains.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/Contains.js#L7)  
> Since: 3.0.0

---

## ContainsPoint

### <static> ContainsPoint(rect, point)

**Description:**

Determines whether the specified point is contained within the rectangular region defined by this Rectangle object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| rect | [Phaser.Geom.Rectangle](geom-rectangle.md) | No | The Rectangle object. |
| --- | --- | --- | --- |
| point | [Phaser.Geom.Point](geom-point.md) | No | The point object to be checked. Can be a Phaser Point object or any object with x and y values. |

**Returns:** boolean - A value of true if the Rectangle object contains the specified point, otherwise false.

> Source: [src/geom/rectangle/ContainsPoint.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/ContainsPoint.js#L9)  
> Since: 3.0.0

---

## ContainsRect

### <static> ContainsRect(rectA, rectB)

**Description:**

Tests if one rectangle fully contains another.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| rectA | [Phaser.Geom.Rectangle](geom-rectangle.md) | No | The first rectangle. |
| --- | --- | --- | --- |
| rectB | [Phaser.Geom.Rectangle](geom-rectangle.md) | No | The second rectangle. |

**Returns:** boolean - True only if rectA fully contains rectB.

> Source: [src/geom/rectangle/ContainsRect.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/ContainsRect.js#L7)  
> Since: 3.0.0

---

## CopyFrom

### <static> CopyFrom(source, dest)

**Description:**

Copy the values of one Rectangle to a destination Rectangle.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| source | [Phaser.Geom.Rectangle](geom-rectangle.md) | No | The source Rectangle to copy the values from. |
| --- | --- | --- | --- |
| dest | [Phaser.Geom.Rectangle](geom-rectangle.md) | No | The destination Rectangle to copy the values to. |

**Returns:** [Phaser.Geom.Rectangle](geom-rectangle.md) - The destination Rectangle.

> Source: [src/geom/rectangle/CopyFrom.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/CopyFrom.js#L7)  
> Since: 3.0.0

---

## Decompose

### <static> Decompose(rect, [out])

**Description:**

Create an array of points for each corner of a Rectangle

If an array is specified, each point object will be added to the end of the array, otherwise a new array will be created.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| rect | [Phaser.Geom.Rectangle](geom-rectangle.md) | No | The Rectangle object to be decomposed. |
| --- | --- | --- | --- |
| out | array | Yes | If provided, each point will be added to this array. |

**Returns:** array - Will return the array you specified or a new array containing the points of the Rectangle.

> Source: [src/geom/rectangle/Decompose.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/Decompose.js#L7)  
> Since: 3.0.0

---

## Equals

### <static> Equals(rect, toCompare)

**Description:**

Compares the `x`, `y`, `width` and `height` properties of two rectangles.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| rect | [Phaser.Geom.Rectangle](geom-rectangle.md) | No | Rectangle A |
| --- | --- | --- | --- |
| toCompare | [Phaser.Geom.Rectangle](geom-rectangle.md) | No | Rectangle B |

**Returns:** boolean - `true` if the rectangles' properties are an exact match, otherwise `false`.

> Source: [src/geom/rectangle/Equals.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/Equals.js#L7)  
> Since: 3.0.0

---

## FitInside

### <static> FitInside(target, source)

**Description:**

Adjusts the target rectangle, changing its width, height and position,

so that it fits inside the area of the source rectangle, while maintaining its original

aspect ratio.

Unlike the `FitOutside` function, there may be some space inside the source area not covered.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| target | [Phaser.Geom.Rectangle](geom-rectangle.md) | No | The target rectangle to adjust. |
| --- | --- | --- | --- |
| source | [Phaser.Geom.Rectangle](geom-rectangle.md) | No | The source rectangle to envelop the target in. |

**Returns:** [Phaser.Geom.Rectangle](geom-rectangle.md) - The modified target rectangle instance.

> Source: [src/geom/rectangle/FitInside.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/FitInside.js#L9)  
> Since: 3.0.0

---

## FitOutside

### <static> FitOutside(target, source)

**Description:**

Adjusts the target rectangle, changing its width, height and position,

so that it fully covers the area of the source rectangle, while maintaining its original

aspect ratio.

Unlike the `FitInside` function, the target rectangle may extend further out than the source.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| target | [Phaser.Geom.Rectangle](geom-rectangle.md) | No | The target rectangle to adjust. |
| --- | --- | --- | --- |
| source | [Phaser.Geom.Rectangle](geom-rectangle.md) | No | The source rectangle to envelope the target in. |

**Returns:** [Phaser.Geom.Rectangle](geom-rectangle.md) - The modified target rectangle instance.

> Source: [src/geom/rectangle/FitOutside.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/FitOutside.js#L9)  
> Since: 3.0.0

---

## Floor

### <static> Floor(rect)

**Description:**

Rounds down (floors) the top left X and Y coordinates of the given Rectangle to the largest integer less than or equal to them

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| rect | [Phaser.Geom.Rectangle](geom-rectangle.md) | No | The rectangle to floor the top left X and Y coordinates of |
| --- | --- | --- | --- |

**Returns:** [Phaser.Geom.Rectangle](geom-rectangle.md) - The rectangle that was passed to this function with its coordinates floored.

> Source: [src/geom/rectangle/Floor.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/Floor.js#L7)  
> Since: 3.0.0

---

## FloorAll

### <static> FloorAll(rect)

**Description:**

Rounds a Rectangle's position and size down to the largest integer less than or equal to each current coordinate or dimension.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| rect | [Phaser.Geom.Rectangle](geom-rectangle.md) | No | The Rectangle to adjust. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Geom.Rectangle](geom-rectangle.md) - The adjusted Rectangle.

> Source: [src/geom/rectangle/FloorAll.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/FloorAll.js#L7)  
> Since: 3.0.0

---

## FromPoints

### <static> FromPoints(points, [out])

**Description:**

Constructs new Rectangle or repositions and resizes an existing Rectangle so that all of the given points are on or within its bounds.

The `points` parameter is an array of Point-like objects:

```
Copy
const points = [

    [100, 200],

    [200, 400],

    { x: 30, y: 60 }

]


```

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| points | array | No | An array of points (either arrays with two elements corresponding to the X and Y coordinate or an object with public `x` and `y` properties) which should be surrounded by the Rectangle. |
| --- | --- | --- | --- |
| out | [Phaser.Geom.Rectangle](geom-rectangle.md) | Yes | Optional Rectangle to adjust. |

**Returns:** [Phaser.Geom.Rectangle](geom-rectangle.md) - The adjusted `out` Rectangle, or a new Rectangle if none was provided.

> Source: [src/geom/rectangle/FromPoints.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/FromPoints.js#L10)  
> Since: 3.0.0

---

## FromXY

### <static> FromXY(x1, y1, x2, y2, [out])

**Description:**

Create the smallest Rectangle containing two coordinate pairs.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x1 | number | No | The X coordinate of the first point. |
| --- | --- | --- | --- |
| y1 | number | No | The Y coordinate of the first point. |
| x2 | number | No | The X coordinate of the second point. |
| y2 | number | No | The Y coordinate of the second point. |
| out | [Phaser.Geom.Rectangle](geom-rectangle.md) | Yes | Optional Rectangle to adjust. |

**Returns:** [Phaser.Geom.Rectangle](geom-rectangle.md) - The adjusted `out` Rectangle, or a new Rectangle if none was provided.

> Source: [src/geom/rectangle/FromXY.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/FromXY.js#L9)  
> Since: 3.23.0

---

## GetAspectRatio

### <static> GetAspectRatio(rect)

**Description:**

Calculates the width/height ratio of a rectangle.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| rect | [Phaser.Geom.Rectangle](geom-rectangle.md) | No | The rectangle. |
| --- | --- | --- | --- |

**Returns:** number - The width/height ratio of the rectangle.

> Source: [src/geom/rectangle/GetAspectRatio.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/GetAspectRatio.js#L7)  
> Since: 3.0.0

---

## GetCenter

### <static> GetCenter(rect, [out])

**Description:**

Returns the center of a Rectangle as a Point.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| rect | [Phaser.Geom.Rectangle](geom-rectangle.md) | No | The Rectangle to get the center of. |
| --- | --- | --- | --- |
| out | [Phaser.Geom.Point](geom-point.md) | object | Yes | Optional point-like object to update with the center coordinates. |

**Returns:** [Phaser.Geom.Point](geom-point.md), object - The modified `out` object, or a new Point if none was provided.

> Source: [src/geom/rectangle/GetCenter.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/GetCenter.js#L9)  
> Since: 3.0.0

---

## getLineA

### <instance> getLineA([line])

**Description:**

Returns a Line object that corresponds to the top of this Rectangle.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| line | [Phaser.Geom.Line](geom-line.md) | Yes | A Line object to set the results in. If `undefined` a new Line will be created. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Geom.Line](geom-line.md) - A Line object that corresponds to the top of this Rectangle.

> Source: [src/geom/rectangle/Rectangle.js#L257](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/Rectangle.js#L257)  
> Since: 3.0.0

---

## getLineB

### <instance> getLineB([line])

**Description:**

Returns a Line object that corresponds to the right of this Rectangle.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| line | [Phaser.Geom.Line](geom-line.md) | Yes | A Line object to set the results in. If `undefined` a new Line will be created. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Geom.Line](geom-line.md) - A Line object that corresponds to the right of this Rectangle.

> Source: [src/geom/rectangle/Rectangle.js#L278](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/Rectangle.js#L278)  
> Since: 3.0.0

---

## getLineC

### <instance> getLineC([line])

**Description:**

Returns a Line object that corresponds to the bottom of this Rectangle.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| line | [Phaser.Geom.Line](geom-line.md) | Yes | A Line object to set the results in. If `undefined` a new Line will be created. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Geom.Line](geom-line.md) - A Line object that corresponds to the bottom of this Rectangle.

> Source: [src/geom/rectangle/Rectangle.js#L299](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/Rectangle.js#L299)  
> Since: 3.0.0

---

## getLineD

### <instance> getLineD([line])

**Description:**

Returns a Line object that corresponds to the left of this Rectangle.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| line | [Phaser.Geom.Line](geom-line.md) | Yes | A Line object to set the results in. If `undefined` a new Line will be created. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Geom.Line](geom-line.md) - A Line object that corresponds to the left of this Rectangle.

> Source: [src/geom/rectangle/Rectangle.js#L320](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/Rectangle.js#L320)  
> Since: 3.0.0

---

## getPoint

### <instance> getPoint(position, [output])

**Description:**

Calculates the coordinates of a point at a certain `position` on the Rectangle's perimeter.

The `position` is a fraction between 0 and 1 which defines how far into the perimeter the point is.

A value of 0 or 1 returns the point at the top left corner of the rectangle, while a value of 0.5 returns the point at the bottom right corner of the rectangle. Values between 0 and 0.5 are on the top or the right side and values between 0.5 and 1 are on the bottom or the left side.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| position | number | No | The normalized distance into the Rectangle's perimeter to return. |
| --- | --- | --- | --- |
| output | [Phaser.Geom.Point](geom-point.md) | object | Yes | An object to update with the `x` and `y` coordinates of the point. |

**Returns:** [Phaser.Geom.Point](geom-point.md), object - The updated `output` object, or a new Point if no `output` object was given.

> Source: [src/geom/rectangle/Rectangle.js#L108](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/Rectangle.js#L108)  
> Since: 3.0.0

---

## GetPoint

### <static> GetPoint(rectangle, position, [out])

**Description:**

Calculates the coordinates of a point at a certain `position` on the Rectangle's perimeter.

The `position` is a fraction between 0 and 1 which defines how far into the perimeter the point is.

A value of 0 or 1 returns the point at the top left corner of the rectangle, while a value of 0.5 returns the point at the bottom right corner of the rectangle. Values between 0 and 0.5 are on the top or the right side and values between 0.5 and 1 are on the bottom or the left side.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| rectangle | [Phaser.Geom.Rectangle](geom-rectangle.md) | No | The Rectangle to get the perimeter point from. |
| --- | --- | --- | --- |
| position | number | No | The normalized distance into the Rectangle's perimeter to return. |
| out | [Phaser.Geom.Point](geom-point.md) | object | Yes | An object to update with the `x` and `y` coordinates of the point. |

**Returns:** [Phaser.Geom.Point](geom-point.md) - The updated `output` object, or a new Point if no `output` object was given.

> Source: [src/geom/rectangle/GetPoint.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/GetPoint.js#L10)  
> Since: 3.0.0

---

## getPoints

### <instance> getPoints(quantity, [stepRate], [output])

**Description:**

Returns an array of points from the perimeter of the Rectangle, each spaced out based on the quantity or step required.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| quantity | number | No | The number of points to return. Set to `false` or 0 to return an arbitrary number of points (`perimeter / stepRate`) evenly spaced around the Rectangle based on the `stepRate`. |
| --- | --- | --- | --- |
| stepRate | number | Yes | If `quantity` is 0, determines the normalized distance between each returned point. |
| output | array | Array.<[Phaser.Geom.Point](geom-point.md)> | Yes | An array to which to append the points. |

**Returns:** array, Array.<[Phaser.Geom.Point](geom-point.md)> - The modified `output` array, or a new array if none was provided.

> Source: [src/geom/rectangle/Rectangle.js#L130](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/Rectangle.js#L130)  
> Since: 3.0.0

---

## GetPoints

### <static> GetPoints(rectangle, step, quantity, [out])

**Description:**

Return an array of points from the perimeter of the rectangle, each spaced out based on the quantity or step required.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| rectangle | [Phaser.Geom.Rectangle](geom-rectangle.md) | No | The Rectangle object to get the points from. |
| --- | --- | --- | --- |
| step | number | No | Step between points. Used to calculate the number of points to return when quantity is falsey. Ignored if quantity is positive. |
| quantity | number | No | The number of evenly spaced points from the rectangles perimeter to return. If falsey, step param will be used to calculate the number of points. |
| out | array | Array.<[Phaser.Geom.Point](geom-point.md)> | Yes | An optional array to store the points in. |

**Returns:** array, Array.<[Phaser.Geom.Point](geom-point.md)> - An array of Points from the perimeter of the rectangle.

> Source: [src/geom/rectangle/GetPoints.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/GetPoints.js#L10)  
> Since: 3.0.0

---

## getRandomPoint

### <instance> getRandomPoint([point])

**Description:**

Returns a random point within the Rectangle's bounds.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| point | [Phaser.Geom.Point](geom-point.md) | Yes | The object in which to store the `x` and `y` coordinates of the point. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Geom.Point](geom-point.md) - The updated `point`, or a new Point if none was provided.

> Source: [src/geom/rectangle/Rectangle.js#L149](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/Rectangle.js#L149)  
> Since: 3.0.0

---

## GetSize

### <static> GetSize(rect, [out])

**Description:**

Returns the size of the Rectangle, expressed as a Point object.

With the value of the `width` as the `x` property and the `height` as the `y` property.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| rect | [Phaser.Geom.Rectangle](geom-rectangle.md) | No | The Rectangle to get the size from. |
| --- | --- | --- | --- |
| out | [Phaser.Geom.Point](geom-point.md) | object | Yes | The Point object to store the size in. If not given, a new Point instance is created. |

**Returns:** [Phaser.Geom.Point](geom-point.md), object - A Point object where `x` holds the width and `y` holds the height of the Rectangle.

> Source: [src/geom/rectangle/GetSize.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/GetSize.js#L9)  
> Since: 3.0.0

---

## Inflate

### <static> Inflate(rect, x, y)

**Description:**

Increases the size of a Rectangle by a specified amount.

The center of the Rectangle stays the same. The amounts are added to each side, so the actual increase in width or height is two times bigger than the respective argument.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| rect | [Phaser.Geom.Rectangle](geom-rectangle.md) | No | The Rectangle to inflate. |
| --- | --- | --- | --- |
| x | number | No | How many pixels the left and the right side should be moved by horizontally. |
| y | number | No | How many pixels the top and the bottom side should be moved by vertically. |

**Returns:** [Phaser.Geom.Rectangle](geom-rectangle.md) - The inflated Rectangle.

> Source: [src/geom/rectangle/Inflate.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/Inflate.js#L9)  
> Since: 3.0.0

---

## Intersection

### <static> Intersection(rectA, rectB, [out])

**Description:**

Takes two Rectangles and first checks to see if they intersect.

If they intersect it will return the area of intersection in the `out` Rectangle.

If they do not intersect, the `out` Rectangle will have a width and height of zero.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| rectA | [Phaser.Geom.Rectangle](geom-rectangle.md) | No | The first Rectangle to get the intersection from. |
| --- | --- | --- | --- |
| rectB | [Phaser.Geom.Rectangle](geom-rectangle.md) | No | The second Rectangle to get the intersection from. |
| out | [Phaser.Geom.Rectangle](geom-rectangle.md) | Yes | A Rectangle to store the intersection results in. |

**Returns:** [Phaser.Geom.Rectangle](geom-rectangle.md) - The intersection result. If the width and height are zero, no intersection occurred.

> Source: [src/geom/rectangle/Intersection.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/Intersection.js#L10)  
> Since: 3.11.0

---

## isEmpty

### <instance> isEmpty()

**Description:**

Determines if the Rectangle is empty. A Rectangle is empty if its width or height is less than or equal to 0.

**Returns:** boolean - `true` if the Rectangle is empty. A Rectangle object is empty if its width or height is less than or equal to 0.

> Source: [src/geom/rectangle/Rectangle.js#L244](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/Rectangle.js#L244)  
> Since: 3.0.0

---

## MarchingAnts

### <static> MarchingAnts(rect, [step], [quantity], [out])

**Description:**

Returns an array of points from the perimeter of the Rectangle, where each point is spaced out based

on either the `step` value, or the `quantity`.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| rect | [Phaser.Geom.Rectangle](geom-rectangle.md) | No | The Rectangle to get the perimeter points from. |
| --- | --- | --- | --- |
| step | number | Yes | The distance between each point of the perimeter. Set to `null` if you wish to use the `quantity` parameter instead. |
| quantity | number | Yes | The total number of points to return. The step is then calculated based on the length of the Rectangle, divided by this value. |
| out | array | Array.<[Phaser.Geom.Point](geom-point.md)> | Yes | An array in which the perimeter points will be stored. If not given, a new array instance is created. |

**Returns:** array, Array.<[Phaser.Geom.Point](geom-point.md)> - An array containing the perimeter points from the Rectangle.

> Source: [src/geom/rectangle/MarchingAnts.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/MarchingAnts.js#L10)  
> Since: 3.0.0

---

## MergePoints

### <static> MergePoints(target, points)

**Description:**

Merges a Rectangle with a list of points by repositioning and/or resizing it such that all points are located on or within its bounds.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| target | [Phaser.Geom.Rectangle](geom-rectangle.md) | No | The Rectangle which should be merged. |
| --- | --- | --- | --- |
| points | Array.<[Phaser.Geom.Point](geom-point.md)> | No | An array of Points (or any object with public `x` and `y` properties) which should be merged with the Rectangle. |

**Returns:** [Phaser.Geom.Rectangle](geom-rectangle.md) - The modified Rectangle.

> Source: [src/geom/rectangle/MergePoints.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/MergePoints.js#L7)  
> Since: 3.0.0

---

## MergeRect

### <static> MergeRect(target, source)

**Description:**

Merges the source rectangle into the target rectangle and returns the target.

Neither rectangle should have a negative width or height.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| target | [Phaser.Geom.Rectangle](geom-rectangle.md) | No | Target rectangle. Will be modified to include source rectangle. |
| --- | --- | --- | --- |
| source | [Phaser.Geom.Rectangle](geom-rectangle.md) | No | Rectangle that will be merged into target rectangle. |

**Returns:** [Phaser.Geom.Rectangle](geom-rectangle.md) - Modified target rectangle that contains source rectangle.

> Source: [src/geom/rectangle/MergeRect.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/MergeRect.js#L7)  
> Since: 3.0.0

---

## MergeXY

### <static> MergeXY(target, x, y)

**Description:**

Merges a Rectangle with a point by repositioning and/or resizing it so that the point is on or within its bounds.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| target | [Phaser.Geom.Rectangle](geom-rectangle.md) | No | The Rectangle which should be merged and modified. |
| --- | --- | --- | --- |
| x | number | No | The X coordinate of the point which should be merged. |
| y | number | No | The Y coordinate of the point which should be merged. |

**Returns:** [Phaser.Geom.Rectangle](geom-rectangle.md) - The modified `target` Rectangle.

> Source: [src/geom/rectangle/MergeXY.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/MergeXY.js#L7)  
> Since: 3.0.0

---

## Offset

### <static> Offset(rect, x, y)

**Description:**

Nudges (translates) the top left corner of a Rectangle by a given offset.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| rect | [Phaser.Geom.Rectangle](geom-rectangle.md) | No | The Rectangle to adjust. |
| --- | --- | --- | --- |
| x | number | No | The distance to move the Rectangle horizontally. |
| y | number | No | The distance to move the Rectangle vertically. |

**Returns:** [Phaser.Geom.Rectangle](geom-rectangle.md) - The adjusted Rectangle.

> Source: [src/geom/rectangle/Offset.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/Offset.js#L7)  
> Since: 3.0.0

---

## OffsetPoint

### <static> OffsetPoint(rect, point)

**Description:**

Nudges (translates) the top-left corner of a Rectangle by the coordinates of a point (translation vector).

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| rect | [Phaser.Geom.Rectangle](geom-rectangle.md) | No | The Rectangle to adjust. |
| --- | --- | --- | --- |
| point | [Phaser.Geom.Point](geom-point.md) | [Phaser.Math.Vector2](math-vector2.md) | No | The point whose coordinates should be used as an offset. |

**Returns:** [Phaser.Geom.Rectangle](geom-rectangle.md) - The adjusted Rectangle.

> Source: [src/geom/rectangle/OffsetPoint.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/OffsetPoint.js#L7)  
> Since: 3.0.0

---

## Overlaps

### <static> Overlaps(rectA, rectB)

**Description:**

Checks if two Rectangles overlap. If a Rectangle is within another Rectangle, the two will be considered overlapping. Thus, the Rectangles are treated as "solid".

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| rectA | [Phaser.Geom.Rectangle](geom-rectangle.md) | No | The first Rectangle to check. |
| --- | --- | --- | --- |
| rectB | [Phaser.Geom.Rectangle](geom-rectangle.md) | No | The second Rectangle to check. |

**Returns:** boolean - `true` if the two Rectangles overlap, `false` otherwise.

> Source: [src/geom/rectangle/Overlaps.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/Overlaps.js#L7)  
> Since: 3.0.0

---

## Perimeter

### <static> Perimeter(rect)

**Description:**

Calculates the perimeter of a Rectangle.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| rect | [Phaser.Geom.Rectangle](geom-rectangle.md) | No | The Rectangle to use. |
| --- | --- | --- | --- |

**Returns:** number - The perimeter of the Rectangle, equal to `(width * 2) + (height * 2)`.

> Source: [src/geom/rectangle/Perimeter.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/Perimeter.js#L7)  
> Since: 3.0.0

---

## PerimeterPoint

### <static> PerimeterPoint(rectangle, angle, [out])

**Description:**

Returns a Point from the perimeter of a Rectangle based on the given angle.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| rectangle | [Phaser.Geom.Rectangle](geom-rectangle.md) | No | The Rectangle to get the perimeter point from. |
| --- | --- | --- | --- |
| angle | number | No | The angle of the point, in degrees. |
| out | [Phaser.Geom.Point](geom-point.md) | Yes | The Point object to store the position in. If not given, a new Point instance is created. |

**Returns:** [Phaser.Geom.Point](geom-point.md) - A Point object holding the coordinates of the Rectangle perimeter.

> Source: [src/geom/rectangle/PerimeterPoint.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/PerimeterPoint.js#L10)  
> Since: 3.0.0

---

## Random

### <static> Random(rect, out)

**Description:**

Returns a random point within a Rectangle.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| rect | [Phaser.Geom.Rectangle](geom-rectangle.md) | No | The Rectangle to return a point from. |
| --- | --- | --- | --- |
| out | [Phaser.Geom.Point](geom-point.md) | No | The object to update with the point's coordinates. |

**Returns:** [Phaser.Geom.Point](geom-point.md) - The modified `out` object, or a new Point if none was provided.

> Source: [src/geom/rectangle/Random.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/Random.js#L9)  
> Since: 3.0.0

---

## RandomOutside

### <static> RandomOutside(outer, inner, [out])

**Description:**

Calculates a random point that lies within the `outer` Rectangle, but outside of the `inner` Rectangle.

The inner Rectangle must be fully contained within the outer rectangle.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| outer | [Phaser.Geom.Rectangle](geom-rectangle.md) | No | The outer Rectangle to get the random point within. |
| --- | --- | --- | --- |
| inner | [Phaser.Geom.Rectangle](geom-rectangle.md) | No | The inner Rectangle to exclude from the returned point. |
| out | [Phaser.Geom.Point](geom-point.md) | Yes | A Point, or Point-like object to store the result in. If not specified, a new Point will be created. |

**Returns:** [Phaser.Geom.Point](geom-point.md) - A Point object containing the random values in its `x` and `y` properties.

> Source: [src/geom/rectangle/RandomOutside.js#L11](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/RandomOutside.js#L11)  
> Since: 3.10.0

---

## SameDimensions

### <static> SameDimensions(rect, toCompare)

**Description:**

Determines if the two objects (either Rectangles or Rectangle-like) have the same width and height values under strict equality.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| rect | [Phaser.Geom.Rectangle](geom-rectangle.md) | No | The first Rectangle object. |
| --- | --- | --- | --- |
| toCompare | [Phaser.Geom.Rectangle](geom-rectangle.md) | No | The second Rectangle object. |

**Returns:** boolean - `true` if the objects have equivalent values for the `width` and `height` properties, otherwise `false`.

> Source: [src/geom/rectangle/SameDimensions.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/SameDimensions.js#L7)  
> Since: 3.15.0

---

## Scale

### <static> Scale(rect, x, y)

**Description:**

Scales the width and height of this Rectangle by the given amounts.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| rect | [Phaser.Geom.Rectangle](geom-rectangle.md) | No | The `Rectangle` object that will be scaled by the specified amount(s). |
| --- | --- | --- | --- |
| x | number | No | The factor by which to scale the rectangle horizontally. |
| y | number | No | The amount by which to scale the rectangle vertically. If this is not specified, the rectangle will be scaled by the factor `x` in both directions. |

**Returns:** [Phaser.Geom.Rectangle](geom-rectangle.md) - The rectangle object with updated `width` and `height` properties as calculated from the scaling factor(s).

> Source: [src/geom/rectangle/Scale.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/Scale.js#L7)  
> Since: 3.0.0

---

## setEmpty

### <instance> setEmpty()

**Description:**

Resets the position, width, and height of the Rectangle to 0.

**Returns:** [Phaser.Geom.Rectangle](geom-rectangle.md) - This Rectangle object.

> Source: [src/geom/rectangle/Rectangle.js#L189](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/Rectangle.js#L189)  
> Since: 3.0.0

---

## setPosition

### <instance> setPosition(x, [y])

**Description:**

Sets the position of the Rectangle.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | No |  | The X coordinate of the top left corner of the Rectangle. |
| --- | --- | --- | --- | --- |
| y | number | Yes | "x" | The Y coordinate of the top left corner of the Rectangle. |

**Returns:** [Phaser.Geom.Rectangle](geom-rectangle.md) - This Rectangle object.

> Source: [src/geom/rectangle/Rectangle.js#L202](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/Rectangle.js#L202)  
> Since: 3.0.0

---

## setSize

### <instance> setSize(width, [height])

**Description:**

Sets the width and height of the Rectangle.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| width | number | No |  | The width to set the Rectangle to. |
| --- | --- | --- | --- | --- |
| height | number | Yes | "width" | The height to set the Rectangle to. |

**Returns:** [Phaser.Geom.Rectangle](geom-rectangle.md) - This Rectangle object.

> Source: [src/geom/rectangle/Rectangle.js#L223](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/Rectangle.js#L223)  
> Since: 3.0.0

---

## setTo

### <instance> setTo(x, y, width, height)

**Description:**

Sets the position, width, and height of the Rectangle.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The X coordinate of the top left corner of the Rectangle. |
| --- | --- | --- | --- |
| y | number | No | The Y coordinate of the top left corner of the Rectangle. |
| width | number | No | The width of the Rectangle. |
| height | number | No | The height of the Rectangle. |

**Returns:** [Phaser.Geom.Rectangle](geom-rectangle.md) - This Rectangle object.

> Source: [src/geom/rectangle/Rectangle.js#L166](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/Rectangle.js#L166)  
> Since: 3.0.0

---

## Union

### <static> Union(rectA, rectB, [out])

**Description:**

Creates a new Rectangle or repositions and/or resizes an existing Rectangle so that it encompasses the two given Rectangles, i.e. calculates their union.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| rectA | [Phaser.Geom.Rectangle](geom-rectangle.md) | No | The first Rectangle to use. |
| --- | --- | --- | --- |
| rectB | [Phaser.Geom.Rectangle](geom-rectangle.md) | No | The second Rectangle to use. |
| out | [Phaser.Geom.Rectangle](geom-rectangle.md) | Yes | The Rectangle to store the union in. |

**Returns:** [Phaser.Geom.Rectangle](geom-rectangle.md) - The modified `out` Rectangle, or a new Rectangle if none was provided.

> Source: [src/geom/rectangle/Union.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/Union.js#L9)  
> Since: 3.0.0

---

# Public Members

## bottom

### bottom: number

**Description:**

The sum of the y and height properties.

Changing the bottom property of a Rectangle object has no effect on the x, y and width properties, but does change the height property.

> Source: [src/geom/rectangle/Rectangle.js#L432](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/Rectangle.js#L432)  
> Since: 3.0.0

---

## centerX

### centerX: number

**Description:**

The x coordinate of the center of the Rectangle.

> Source: [src/geom/rectangle/Rectangle.js#L461](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/Rectangle.js#L461)  
> Since: 3.0.0

---

## centerY

### centerY: number

**Description:**

The y coordinate of the center of the Rectangle.

> Source: [src/geom/rectangle/Rectangle.js#L482](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/Rectangle.js#L482)  
> Since: 3.0.0

---

## height

### height: number

**Description:**

The height of the Rectangle, i.e. the distance between its top side (defined by `y`) and its bottom side.

> Source: [src/geom/rectangle/Rectangle.js#L81](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/Rectangle.js#L81)  
> Since: 3.0.0

---

## left

### left: number

**Description:**

The x coordinate of the left of the Rectangle.

Changing the left property of a Rectangle object has no effect on the y and height properties. However it does affect the width property, whereas changing the x value does not affect the width property.

> Source: [src/geom/rectangle/Rectangle.js#L341](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/Rectangle.js#L341)  
> Since: 3.0.0

---

## right

### right: number

**Description:**

The sum of the x and width properties.

Changing the right property of a Rectangle object has no effect on the x, y and height properties, however it does affect the width property.

> Source: [src/geom/rectangle/Rectangle.js#L372](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/Rectangle.js#L372)  
> Since: 3.0.0

---

## top

### top: number

**Description:**

The y coordinate of the top of the Rectangle. Changing the top property of a Rectangle object has no effect on the x and width properties.

However it does affect the height property, whereas changing the y value does not affect the height property.

> Source: [src/geom/rectangle/Rectangle.js#L401](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/Rectangle.js#L401)  
> Since: 3.0.0

---

## type

### type: number

**Description:**

The geometry constant type of this object: `GEOM_CONST.RECTANGLE`.

Used for fast type comparisons.

> Source: [src/geom/rectangle/Rectangle.js#L40](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/Rectangle.js#L40)  
> Since: 3.19.0

---

## width

### width: number

**Description:**

The width of the Rectangle, i.e. the distance between its left side (defined by `x`) and its right side.

> Source: [src/geom/rectangle/Rectangle.js#L71](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/Rectangle.js#L71)  
> Since: 3.0.0

---

## x

### x: number

**Description:**

The X coordinate of the top left corner of the Rectangle.

> Source: [src/geom/rectangle/Rectangle.js#L51](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/Rectangle.js#L51)  
> Since: 3.0.0

---

## y

### y: number

**Description:**

The Y coordinate of the top left corner of the Rectangle.

> Source: [src/geom/rectangle/Rectangle.js#L61](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/Rectangle.js#L61)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Methods](#public-methods)

  + [Area](#area)

    - [<static> Area(rect)](#static-arearect)
  + [Ceil](#ceil)

    - [<static> Ceil(rect)](#static-ceilrect)
  + [CeilAll](#ceilall)

    - [<static> CeilAll(rect)](#static-ceilallrect)
  + [CenterOn](#centeron)

    - [<static> CenterOn(rect, x, y)](#static-centeronrect-x-y)
  + [Clone](#clone)

    - [<static> Clone(source)](#static-clonesource)
  + [contains](#contains)

    - [<instance> contains(x, y)](#instance-containsx-y)
  + [Contains](#contains-1)

    - [<static> Contains(rect, x, y)](#static-containsrect-x-y)
  + [ContainsPoint](#containspoint)

    - [<static> ContainsPoint(rect, point)](#static-containspointrect-point)
  + [ContainsRect](#containsrect)

    - [<static> ContainsRect(rectA, rectB)](#static-containsrectrecta-rectb)
  + [CopyFrom](#copyfrom)

    - [<static> CopyFrom(source, dest)](#static-copyfromsource-dest)
  + [Decompose](#decompose)

    - [<static> Decompose(rect, [out])](#static-decomposerect-out)
  + [Equals](#equals)

    - [<static> Equals(rect, toCompare)](#static-equalsrect-tocompare)
  + [FitInside](#fitinside)

    - [<static> FitInside(target, source)](#static-fitinsidetarget-source)
  + [FitOutside](#fitoutside)

    - [<static> FitOutside(target, source)](#static-fitoutsidetarget-source)
  + [Floor](#floor)

    - [<static> Floor(rect)](#static-floorrect)
  + [FloorAll](#floorall)

    - [<static> FloorAll(rect)](#static-floorallrect)
  + [FromPoints](#frompoints)

    - [<static> FromPoints(points, [out])](#static-frompointspoints-out)
  + [FromXY](#fromxy)

    - [<static> FromXY(x1, y1, x2, y2, [out])](#static-fromxyx1-y1-x2-y2-out)
  + [GetAspectRatio](#getaspectratio)

    - [<static> GetAspectRatio(rect)](#static-getaspectratiorect)
  + [GetCenter](#getcenter)

    - [<static> GetCenter(rect, [out])](#static-getcenterrect-out)
  + [getLineA](#getlinea)

    - [<instance> getLineA([line])](#instance-getlinealine)
  + [getLineB](#getlineb)

    - [<instance> getLineB([line])](#instance-getlinebline)
  + [getLineC](#getlinec)

    - [<instance> getLineC([line])](#instance-getlinecline)
  + [getLineD](#getlined)

    - [<instance> getLineD([line])](#instance-getlinedline)
  + [getPoint](#getpoint)

    - [<instance> getPoint(position, [output])](#instance-getpointposition-output)
  + [GetPoint](#getpoint-1)

    - [<static> GetPoint(rectangle, position, [out])](#static-getpointrectangle-position-out)
  + [getPoints](#getpoints)

    - [<instance> getPoints(quantity, [stepRate], [output])](#instance-getpointsquantity-steprate-output)
  + [GetPoints](#getpoints-1)

    - [<static> GetPoints(rectangle, step, quantity, [out])](#static-getpointsrectangle-step-quantity-out)
  + [getRandomPoint](#getrandompoint)

    - [<instance> getRandomPoint([point])](#instance-getrandompointpoint)
  + [GetSize](#getsize)

    - [<static> GetSize(rect, [out])](#static-getsizerect-out)
  + [Inflate](#inflate)

    - [<static> Inflate(rect, x, y)](#static-inflaterect-x-y)
  + [Intersection](#intersection)

    - [<static> Intersection(rectA, rectB, [out])](#static-intersectionrecta-rectb-out)
  + [isEmpty](#isempty)

    - [<instance> isEmpty()](#instance-isempty)
  + [MarchingAnts](#marchingants)

    - [<static> MarchingAnts(rect, [step], [quantity], [out])](#static-marchingantsrect-step-quantity-out)
  + [MergePoints](#mergepoints)

    - [<static> MergePoints(target, points)](#static-mergepointstarget-points)
  + [MergeRect](#mergerect)

    - [<static> MergeRect(target, source)](#static-mergerecttarget-source)
  + [MergeXY](#mergexy)

    - [<static> MergeXY(target, x, y)](#static-mergexytarget-x-y)
  + [Offset](#offset)

    - [<static> Offset(rect, x, y)](#static-offsetrect-x-y)
  + [OffsetPoint](#offsetpoint)

    - [<static> OffsetPoint(rect, point)](#static-offsetpointrect-point)
  + [Overlaps](#overlaps)

    - [<static> Overlaps(rectA, rectB)](#static-overlapsrecta-rectb)
  + [Perimeter](#perimeter)

    - [<static> Perimeter(rect)](#static-perimeterrect)
  + [PerimeterPoint](#perimeterpoint)

    - [<static> PerimeterPoint(rectangle, angle, [out])](#static-perimeterpointrectangle-angle-out)
  + [Random](#random)

    - [<static> Random(rect, out)](#static-randomrect-out)
  + [RandomOutside](#randomoutside)

    - [<static> RandomOutside(outer, inner, [out])](#static-randomoutsideouter-inner-out)
  + [SameDimensions](#samedimensions)

    - [<static> SameDimensions(rect, toCompare)](#static-samedimensionsrect-tocompare)
  + [Scale](#scale)

    - [<static> Scale(rect, x, y)](#static-scalerect-x-y)
  + [setEmpty](#setempty)

    - [<instance> setEmpty()](#instance-setempty)
  + [setPosition](#setposition)

    - [<instance> setPosition(x, [y])](#instance-setpositionx-y)
  + [setSize](#setsize)

    - [<instance> setSize(width, [height])](#instance-setsizewidth-height)
  + [setTo](#setto)

    - [<instance> setTo(x, y, width, height)](#instance-settox-y-width-height)
  + [Union](#union)

    - [<static> Union(rectA, rectB, [out])](#static-unionrecta-rectb-out)
* [Public Members](#public-members)

  + [bottom](#bottom)

    - [bottom: number](#bottom-number)
  + [centerX](#centerx)

    - [centerX: number](#centerx-number)
  + [centerY](#centery)

    - [centerY: number](#centery-number)
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