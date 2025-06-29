# Phaser.Geom

# Phaser.Geom.Circle

## Area

### <static> Area(circle)

**Description:**

Calculates the area of the circle.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| circle | [Phaser.Geom.Circle](../class/geom-circle.md) | No | The Circle to get the area of. |
| --- | --- | --- | --- |

**Returns:** number - The area of the Circle.

> Source: [src/geom/circle/Area.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/circle/Area.js#L7)  
> Since: 3.0.0

## Circumference

### <static> Circumference(circle)

**Description:**

Returns the circumference of the given Circle.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| circle | [Phaser.Geom.Circle](../class/geom-circle.md) | No | The Circle to get the circumference of. |
| --- | --- | --- | --- |

**Returns:** number - The circumference of the Circle.

> Source: [src/geom/circle/Circumference.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/circle/Circumference.js#L7)  
> Since: 3.0.0

## CircumferencePoint

### <static> CircumferencePoint(circle, angle, [out])

**Description:**

Returns a Point object containing the coordinates of a point on the circumference of the Circle based on the given angle.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| circle | [Phaser.Geom.Circle](../class/geom-circle.md) | No | The Circle to get the circumference point on. |
| --- | --- | --- | --- |
| angle | number | No | The angle from the center of the Circle to the circumference to return the point from. Given in radians. |
| out | [Phaser.Geom.Point](../class/geom-point.md) | object | Yes | A Point, or point-like object, to store the results in. If not given a Point will be created. |

**Returns:** [Phaser.Geom.Point](../class/geom-point.md), object - A Point object where the `x` and `y` properties are the point on the circumference.

> Source: [src/geom/circle/CircumferencePoint.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/circle/CircumferencePoint.js#L9)  
> Since: 3.0.0

## Clone

### <static> Clone(source)

**Description:**

Creates a new Circle instance based on the values contained in the given source.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| source | [Phaser.Geom.Circle](../class/geom-circle.md) | object | No | The Circle to be cloned. Can be an instance of a Circle or a circle-like object, with x, y and radius properties. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Geom.Circle](../class/geom-circle.md) - A clone of the source Circle.

> Source: [src/geom/circle/Clone.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/circle/Clone.js#L9)  
> Since: 3.0.0

## Contains

### <static> Contains(circle, x, y)

**Description:**

Check to see if the Circle contains the given x / y coordinates.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| circle | [Phaser.Geom.Circle](../class/geom-circle.md) | No | The Circle to check. |
| --- | --- | --- | --- |
| x | number | No | The x coordinate to check within the circle. |
| y | number | No | The y coordinate to check within the circle. |

**Returns:** boolean - True if the coordinates are within the circle, otherwise false.

> Source: [src/geom/circle/Contains.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/circle/Contains.js#L7)  
> Since: 3.0.0

## ContainsPoint

### <static> ContainsPoint(circle, point)

**Description:**

Check to see if the Circle contains the given Point object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| circle | [Phaser.Geom.Circle](../class/geom-circle.md) | No | The Circle to check. |
| --- | --- | --- | --- |
| point | [Phaser.Geom.Point](../class/geom-point.md) | object | No | The Point object to check if it's within the Circle or not. |

**Returns:** boolean - True if the Point coordinates are within the circle, otherwise false.

> Source: [src/geom/circle/ContainsPoint.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/circle/ContainsPoint.js#L9)  
> Since: 3.0.0

## ContainsRect

### <static> ContainsRect(circle, rect)

**Description:**

Check to see if the Circle contains all four points of the given Rectangle object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| circle | [Phaser.Geom.Circle](../class/geom-circle.md) | No | The Circle to check. |
| --- | --- | --- | --- |
| rect | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | object | No | The Rectangle object to check if it's within the Circle or not. |

**Returns:** boolean - True if all of the Rectangle coordinates are within the circle, otherwise false.

> Source: [src/geom/circle/ContainsRect.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/circle/ContainsRect.js#L9)  
> Since: 3.0.0

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
| source | [Phaser.Geom.Circle](../class/geom-circle.md) | No | The source Circle to copy the values from. |
| --- | --- | --- | --- |
| dest | [Phaser.Geom.Circle](../class/geom-circle.md) | No | The destination Circle to copy the values to. |

**Returns:** [Phaser.Geom.Circle](../class/geom-circle.md) - The destination Circle.

> Source: [src/geom/circle/CopyFrom.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/circle/CopyFrom.js#L7)  
> Since: 3.0.0

## Equals

### <static> Equals(circle, toCompare)

**Description:**

Compares the `x`, `y` and `radius` properties of the two given Circles.

Returns `true` if they all match, otherwise returns `false`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| circle | [Phaser.Geom.Circle](../class/geom-circle.md) | No | The first Circle to compare. |
| --- | --- | --- | --- |
| toCompare | [Phaser.Geom.Circle](../class/geom-circle.md) | No | The second Circle to compare. |

**Returns:** boolean - `true` if the two Circles equal each other, otherwise `false`.

> Source: [src/geom/circle/Equals.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/circle/Equals.js#L7)  
> Since: 3.0.0

## GetBounds

### <static> GetBounds(circle, [out])

**Description:**

Returns the bounds of the Circle object.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| circle | [Phaser.Geom.Circle](../class/geom-circle.md) | No | The Circle to get the bounds from. |
| --- | --- | --- | --- |
| out | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | object | Yes | A Rectangle, or rectangle-like object, to store the circle bounds in. If not given a new Rectangle will be created. |

**Returns:** [Phaser.Geom.Rectangle](../class/geom-rectangle.md), object - The Rectangle object containing the Circles bounds.

> Source: [src/geom/circle/GetBounds.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/circle/GetBounds.js#L9)  
> Since: 3.0.0

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
| circle | [Phaser.Geom.Circle](../class/geom-circle.md) | No | The Circle to get the circumference point on. |
| --- | --- | --- | --- |
| position | number | No | A value between 0 and 1, where 0 equals 0 degrees, 0.5 equals 180 degrees and 1 equals 360 around the circle. |
| out | [Phaser.Geom.Point](../class/geom-point.md) | object | Yes | An object to store the return values in. If not given a Point object will be created. |

**Returns:** [Phaser.Geom.Point](../class/geom-point.md), object - A Point, or point-like object, containing the coordinates of the point around the circle.

> Source: [src/geom/circle/GetPoint.js#L12](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/circle/GetPoint.js#L12)  
> Since: 3.0.0

## GetPoints

### <static> GetPoints(circle, quantity, [stepRate], [output])

**Description:**

Returns an array of Point objects containing the coordinates of the points around the circumference of the Circle,

based on the given quantity or stepRate values.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| circle | [Phaser.Geom.Circle](../class/geom-circle.md) | No | The Circle to get the points from. |
| --- | --- | --- | --- |
| quantity | number | No | The amount of points to return. If a falsey value the quantity will be derived from the `stepRate` instead. |
| stepRate | number | Yes | Sets the quantity by getting the circumference of the circle and dividing it by the stepRate. |
| output | array | Yes | An array to insert the points in to. If not provided a new array will be created. |

**Returns:** Array.<[Phaser.Geom.Point](../class/geom-point.md)> - An array of Point objects pertaining to the points around the circumference of the circle.

> Source: [src/geom/circle/GetPoints.js#L12](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/circle/GetPoints.js#L12)  
> Since: 3.0.0

## Offset

### <static> Offset(circle, x, y)

**Description:**

Offsets the Circle by the values given.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| circle | [Phaser.Geom.Circle](../class/geom-circle.md) | No | The Circle to be offset (translated.) |
| --- | --- | --- | --- |
| x | number | No | The amount to horizontally offset the Circle by. |
| y | number | No | The amount to vertically offset the Circle by. |

**Returns:** [Phaser.Geom.Circle](../class/geom-circle.md) - The Circle that was offset.

> Source: [src/geom/circle/Offset.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/circle/Offset.js#L7)  
> Since: 3.0.0

## OffsetPoint

### <static> OffsetPoint(circle, point)

**Description:**

Offsets the Circle by the values given in the `x` and `y` properties of the Point object.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| circle | [Phaser.Geom.Circle](../class/geom-circle.md) | No | The Circle to be offset (translated.) |
| --- | --- | --- | --- |
| point | [Phaser.Geom.Point](../class/geom-point.md) | object | No | The Point object containing the values to offset the Circle by. |

**Returns:** [Phaser.Geom.Circle](../class/geom-circle.md) - The Circle that was offset.

> Source: [src/geom/circle/OffsetPoint.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/circle/OffsetPoint.js#L7)  
> Since: 3.0.0

## Random

### <static> Random(circle, [out])

**Description:**

Returns a uniformly distributed random point from anywhere within the given Circle.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| circle | [Phaser.Geom.Circle](../class/geom-circle.md) | No | The Circle to get a random point from. |
| --- | --- | --- | --- |
| out | [Phaser.Geom.Point](../class/geom-point.md) | object | Yes | A Point or point-like object to set the random `x` and `y` values in. |

**Returns:** [Phaser.Geom.Point](../class/geom-point.md), object - A Point object with the random values set in the `x` and `y` properties.

> Source: [src/geom/circle/Random.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/circle/Random.js#L9)  
> Since: 3.0.0

# Phaser.Geom.Ellipse

## Area

### <static> Area(ellipse)

**Description:**

Calculates the area of the Ellipse.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| ellipse | [Phaser.Geom.Ellipse](../class/geom-ellipse.md) | No | The Ellipse to get the area of. |
| --- | --- | --- | --- |

**Returns:** number - The area of the Ellipse.

> Source: [src/geom/ellipse/Area.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/ellipse/Area.js#L7)  
> Since: 3.0.0

## Circumference

### <static> Circumference(ellipse)

**Description:**

Returns the circumference of the given Ellipse.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| ellipse | [Phaser.Geom.Ellipse](../class/geom-ellipse.md) | No | The Ellipse to get the circumference of. |
| --- | --- | --- | --- |

**Returns:** number - The circumference of th Ellipse.

> Source: [src/geom/ellipse/Circumference.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/ellipse/Circumference.js#L7)  
> Since: 3.0.0

## CircumferencePoint

### <static> CircumferencePoint(ellipse, angle, [out])

**Description:**

Returns a Point object containing the coordinates of a point on the circumference of the Ellipse based on the given angle.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| ellipse | [Phaser.Geom.Ellipse](../class/geom-ellipse.md) | No | The Ellipse to get the circumference point on. |
| --- | --- | --- | --- |
| angle | number | No | The angle from the center of the Ellipse to the circumference to return the point from. Given in radians. |
| out | [Phaser.Geom.Point](../class/geom-point.md) | object | Yes | A Point, or point-like object, to store the results in. If not given a Point will be created. |

**Returns:** [Phaser.Geom.Point](../class/geom-point.md), object - A Point object where the `x` and `y` properties are the point on the circumference.

> Source: [src/geom/ellipse/CircumferencePoint.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/ellipse/CircumferencePoint.js#L9)  
> Since: 3.0.0

## Clone

### <static> Clone(source)

**Description:**

Creates a new Ellipse instance based on the values contained in the given source.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| source | [Phaser.Geom.Ellipse](../class/geom-ellipse.md) | No | The Ellipse to be cloned. Can be an instance of an Ellipse or a ellipse-like object, with x, y, width and height properties. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Geom.Ellipse](../class/geom-ellipse.md) - A clone of the source Ellipse.

> Source: [src/geom/ellipse/Clone.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/ellipse/Clone.js#L9)  
> Since: 3.0.0

## Contains

### <static> Contains(ellipse, x, y)

**Description:**

Check to see if the Ellipse contains the given x / y coordinates.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| ellipse | [Phaser.Geom.Ellipse](../class/geom-ellipse.md) | No | The Ellipse to check. |
| --- | --- | --- | --- |
| x | number | No | The x coordinate to check within the ellipse. |
| y | number | No | The y coordinate to check within the ellipse. |

**Returns:** boolean - True if the coordinates are within the ellipse, otherwise false.

> Source: [src/geom/ellipse/Contains.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/ellipse/Contains.js#L7)  
> Since: 3.0.0

## ContainsPoint

### <static> ContainsPoint(ellipse, point)

**Description:**

Check to see if the Ellipse contains the given Point object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| ellipse | [Phaser.Geom.Ellipse](../class/geom-ellipse.md) | No | The Ellipse to check. |
| --- | --- | --- | --- |
| point | [Phaser.Geom.Point](../class/geom-point.md) | object | No | The Point object to check if it's within the Circle or not. |

**Returns:** boolean - True if the Point coordinates are within the circle, otherwise false.

> Source: [src/geom/ellipse/ContainsPoint.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/ellipse/ContainsPoint.js#L9)  
> Since: 3.0.0

## ContainsRect

### <static> ContainsRect(ellipse, rect)

**Description:**

Check to see if the Ellipse contains all four points of the given Rectangle object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| ellipse | [Phaser.Geom.Ellipse](../class/geom-ellipse.md) | No | The Ellipse to check. |
| --- | --- | --- | --- |
| rect | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | object | No | The Rectangle object to check if it's within the Ellipse or not. |

**Returns:** boolean - True if all of the Rectangle coordinates are within the ellipse, otherwise false.

> Source: [src/geom/ellipse/ContainsRect.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/ellipse/ContainsRect.js#L9)  
> Since: 3.0.0

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
| source | [Phaser.Geom.Ellipse](../class/geom-ellipse.md) | No | The source Ellipse to copy the values from. |
| --- | --- | --- | --- |
| dest | [Phaser.Geom.Ellipse](../class/geom-ellipse.md) | No | The destination Ellipse to copy the values to. |

**Returns:** [Phaser.Geom.Ellipse](../class/geom-ellipse.md) - The destination Ellipse.

> Source: [src/geom/ellipse/CopyFrom.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/ellipse/CopyFrom.js#L7)  
> Since: 3.0.0

## Equals

### <static> Equals(ellipse, toCompare)

**Description:**

Compares the `x`, `y`, `width` and `height` properties of the two given Ellipses.

Returns `true` if they all match, otherwise returns `false`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| ellipse | [Phaser.Geom.Ellipse](../class/geom-ellipse.md) | No | The first Ellipse to compare. |
| --- | --- | --- | --- |
| toCompare | [Phaser.Geom.Ellipse](../class/geom-ellipse.md) | No | The second Ellipse to compare. |

**Returns:** boolean - `true` if the two Ellipse equal each other, otherwise `false`.

> Source: [src/geom/ellipse/Equals.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/ellipse/Equals.js#L7)  
> Since: 3.0.0

## GetBounds

### <static> GetBounds(ellipse, [out])

**Description:**

Returns the bounds of the Ellipse object.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| ellipse | [Phaser.Geom.Ellipse](../class/geom-ellipse.md) | No | The Ellipse to get the bounds from. |
| --- | --- | --- | --- |
| out | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | object | Yes | A Rectangle, or rectangle-like object, to store the ellipse bounds in. If not given a new Rectangle will be created. |

**Returns:** [Phaser.Geom.Rectangle](../class/geom-rectangle.md), object - The Rectangle object containing the Ellipse bounds.

> Source: [src/geom/ellipse/GetBounds.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/ellipse/GetBounds.js#L9)  
> Since: 3.0.0

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
| ellipse | [Phaser.Geom.Ellipse](../class/geom-ellipse.md) | No | The Ellipse to get the circumference point on. |
| --- | --- | --- | --- |
| position | number | No | A value between 0 and 1, where 0 equals 0 degrees, 0.5 equals 180 degrees and 1 equals 360 around the ellipse. |
| out | [Phaser.Geom.Point](../class/geom-point.md) | object | Yes | An object to store the return values in. If not given a Point object will be created. |

**Returns:** [Phaser.Geom.Point](../class/geom-point.md), object - A Point, or point-like object, containing the coordinates of the point around the ellipse.

> Source: [src/geom/ellipse/GetPoint.js#L12](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/ellipse/GetPoint.js#L12)  
> Since: 3.0.0

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
| ellipse | [Phaser.Geom.Ellipse](../class/geom-ellipse.md) | No | The Ellipse to get the points from. |
| --- | --- | --- | --- |
| quantity | number | No | The amount of points to return. If a falsey value the quantity will be derived from the `stepRate` instead. |
| stepRate | number | Yes | Sets the quantity by getting the circumference of the ellipse and dividing it by the stepRate. |
| out | array | Array.<[Phaser.Geom.Point](../class/geom-point.md)> | Yes | An array to insert the points in to. If not provided a new array will be created. |

**Returns:** array, Array.<[Phaser.Geom.Point](../class/geom-point.md)> - An array of Point objects pertaining to the points around the circumference of the ellipse.

> Source: [src/geom/ellipse/GetPoints.js#L12](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/ellipse/GetPoints.js#L12)  
> Since: 3.0.0

## Offset

### <static> Offset(ellipse, x, y)

**Description:**

Offsets the Ellipse by the values given.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| ellipse | [Phaser.Geom.Ellipse](../class/geom-ellipse.md) | No | The Ellipse to be offset (translated.) |
| --- | --- | --- | --- |
| x | number | No | The amount to horizontally offset the Ellipse by. |
| y | number | No | The amount to vertically offset the Ellipse by. |

**Returns:** [Phaser.Geom.Ellipse](../class/geom-ellipse.md) - The Ellipse that was offset.

> Source: [src/geom/ellipse/Offset.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/ellipse/Offset.js#L7)  
> Since: 3.0.0

## OffsetPoint

### <static> OffsetPoint(ellipse, point)

**Description:**

Offsets the Ellipse by the values given in the `x` and `y` properties of the Point object.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| ellipse | [Phaser.Geom.Ellipse](../class/geom-ellipse.md) | No | The Ellipse to be offset (translated.) |
| --- | --- | --- | --- |
| point | [Phaser.Geom.Point](../class/geom-point.md) | object | No | The Point object containing the values to offset the Ellipse by. |

**Returns:** [Phaser.Geom.Ellipse](../class/geom-ellipse.md) - The Ellipse that was offset.

> Source: [src/geom/ellipse/OffsetPoint.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/ellipse/OffsetPoint.js#L7)  
> Since: 3.0.0

## Random

### <static> Random(ellipse, [out])

**Description:**

Returns a uniformly distributed random point from anywhere within the given Ellipse.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| ellipse | [Phaser.Geom.Ellipse](../class/geom-ellipse.md) | No | The Ellipse to get a random point from. |
| --- | --- | --- | --- |
| out | [Phaser.Geom.Point](../class/geom-point.md) | object | Yes | A Point or point-like object to set the random `x` and `y` values in. |

**Returns:** [Phaser.Geom.Point](../class/geom-point.md), object - A Point object with the random values set in the `x` and `y` properties.

> Source: [src/geom/ellipse/Random.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/ellipse/Random.js#L9)  
> Since: 3.0.0

# Phaser.Geom.Intersects

## CircleToCircle

### <static> CircleToCircle(circleA, circleB)

**Description:**

Checks if two Circles intersect.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| circleA | [Phaser.Geom.Circle](../class/geom-circle.md) | No | The first Circle to check for intersection. |
| --- | --- | --- | --- |
| circleB | [Phaser.Geom.Circle](../class/geom-circle.md) | No | The second Circle to check for intersection. |

**Returns:** boolean - `true` if the two Circles intersect, otherwise `false`.

> Source: [src/geom/intersects/CircleToCircle.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/intersects/CircleToCircle.js#L9)  
> Since: 3.0.0

## CircleToRectangle

### <static> CircleToRectangle(circle, rect)

**Description:**

Checks for intersection between a circle and a rectangle.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| circle | [Phaser.Geom.Circle](../class/geom-circle.md) | No | The circle to be checked. |
| --- | --- | --- | --- |
| rect | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | No | The rectangle to be checked. |

**Returns:** boolean - `true` if the two objects intersect, otherwise `false`.

> Source: [src/geom/intersects/CircleToRectangle.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/intersects/CircleToRectangle.js#L7)  
> Since: 3.0.0

## GetCircleToCircle

### <static> GetCircleToCircle(circleA, circleB, [out])

**Description:**

Checks if two Circles intersect and returns the intersection points as a Point object array.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| circleA | [Phaser.Geom.Circle](../class/geom-circle.md) | No | The first Circle to check for intersection. |
| --- | --- | --- | --- |
| circleB | [Phaser.Geom.Circle](../class/geom-circle.md) | No | The second Circle to check for intersection. |
| out | array | Yes | An optional array in which to store the points of intersection. |

**Returns:** array - An array with the points of intersection if objects intersect, otherwise an empty array.

> Source: [src/geom/intersects/GetCircleToCircle.js#L11](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/intersects/GetCircleToCircle.js#L11)  
> Since: 3.0.0

## GetCircleToRectangle

### <static> GetCircleToRectangle(circle, rect, [out])

**Description:**

Checks for intersection between a circle and a rectangle,

and returns the intersection points as a Point object array.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| circle | [Phaser.Geom.Circle](../class/geom-circle.md) | No | The circle to be checked. |
| --- | --- | --- | --- |
| rect | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | No | The rectangle to be checked. |
| out | array | Yes | An optional array in which to store the points of intersection. |

**Returns:** array - An array with the points of intersection if objects intersect, otherwise an empty array.

> Source: [src/geom/intersects/GetCircleToRectangle.js#L11](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/intersects/GetCircleToRectangle.js#L11)  
> Since: 3.0.0

## GetLineToCircle

### <static> GetLineToCircle(line, circle, [out])

**Description:**

Checks for intersection between the line segment and circle,

and returns the intersection points as a Point object array.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| line | [Phaser.Geom.Line](../class/geom-line.md) | No | The line segment to check. |
| --- | --- | --- | --- |
| circle | [Phaser.Geom.Circle](../class/geom-circle.md) | No | The circle to check against the line. |
| out | array | Yes | An optional array in which to store the points of intersection. |

**Returns:** array - An array with the points of intersection if objects intersect, otherwise an empty array.

> Source: [src/geom/intersects/GetLineToCircle.js#L11](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/intersects/GetLineToCircle.js#L11)  
> Since: 3.0.0

## GetLineToLine

### <static> GetLineToLine(line1, line2, [isRay], [out])

**Description:**

Checks for intersection between the two line segments, or a ray and a line segment,

and returns the intersection point as a Vector3, or `null` if the lines are parallel, or do not intersect.

The `z` property of the Vector3 contains the intersection distance, which can be used to find

the closest intersecting point from a group of line segments.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| line1 | [Phaser.Geom.Line](../class/geom-line.md) | No |  | The first line segment, or a ray, to check. |
| --- | --- | --- | --- | --- |
| line2 | [Phaser.Geom.Line](../class/geom-line.md) | No |  | The second line segment to check. |
| isRay | boolean | Yes | false | Is `line1` a ray or a line segment? |
| out | [Phaser.Math.Vector3](../class/math-vector3.md) | Yes |  | A Vector3 to store the intersection results in. |

**Returns:** [Phaser.Math.Vector3](../class/math-vector3.md) - A Vector3 containing the intersection results, or `null`.

> Source: [src/geom/intersects/GetLineToLine.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/intersects/GetLineToLine.js#L9)  
> Since: 3.50.0

## GetLineToPoints

### <static> GetLineToPoints(line, points, [isRay], [out])

**Description:**

Checks for the closest point of intersection between a line segment and an array of points, where each pair

of points are converted to line segments for the intersection tests.

If no intersection is found, this function returns `null`.

If intersection was found, a Vector3 is returned with the following properties:

The `x` and `y` components contain the point of the intersection.

The `z` component contains the closest distance.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| line | [Phaser.Geom.Line](../class/geom-line.md) | No |  | The line segment, or ray, to check. If a ray, set the `isRay` parameter to `true`. |
| --- | --- | --- | --- | --- |
| points | Array.<[Phaser.Math.Vector2](../class/math-vector2.md)> | Array.<[Phaser.Geom.Point](../class/geom-point.md)> | No |  | An array of points to check. |
| isRay | boolean | Yes | false | Is `line` a ray or a line segment? |
| out | [Phaser.Math.Vector3](../class/math-vector3.md) | Yes |  | A Vector3 to store the intersection results in. |

**Returns:** [Phaser.Math.Vector3](../class/math-vector3.md) - A Vector3 containing the intersection results, or `null`.

> Source: [src/geom/intersects/GetLineToPoints.js#L17](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/intersects/GetLineToPoints.js#L17)  
> Since: 3.50.0

## GetLineToPolygon

### <static> GetLineToPolygon(line, polygons, [isRay], [out])

**Description:**

Checks for the closest point of intersection between a line segment and an array of polygons.

If no intersection is found, this function returns `null`.

If intersection was found, a Vector4 is returned with the following properties:

The `x` and `y` components contain the point of the intersection.

The `z` component contains the closest distance.

The `w` component contains the index of the polygon, in the given array, that triggered the intersection.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| line | [Phaser.Geom.Line](../class/geom-line.md) | No |  | The line segment, or ray, to check. If a ray, set the `isRay` parameter to `true`. |
| --- | --- | --- | --- | --- |
| polygons | [Phaser.Geom.Polygon](../class/geom-polygon.md) | Array.<[Phaser.Geom.Polygon](../class/geom-polygon.md)> | No |  | A single polygon, or array of polygons, to check. |
| isRay | boolean | Yes | false | Is `line` a ray or a line segment? |
| out | [Phaser.Math.Vector4](../class/math-vector4.md) | Yes |  | A Vector4 to store the intersection results in. |

**Returns:** [Phaser.Math.Vector4](../class/math-vector4.md) - A Vector4 containing the intersection results, or `null`.

> Source: [src/geom/intersects/GetLineToPolygon.js#L14](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/intersects/GetLineToPolygon.js#L14)  
> Since: 3.50.0

## GetLineToRectangle

### <static> GetLineToRectangle(line, rect, [out])

**Description:**

Checks for intersection between the Line and a Rectangle shape,

and returns the intersection points as a Point object array.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| line | [Phaser.Geom.Line](../class/geom-line.md) | No | The Line to check for intersection. |
| --- | --- | --- | --- |
| rect | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | object | No | The Rectangle to check for intersection. |
| out | array | Yes | An optional array in which to store the points of intersection. |

**Returns:** array - An array with the points of intersection if objects intersect, otherwise an empty array.

> Source: [src/geom/intersects/GetLineToRectangle.js#L12](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/intersects/GetLineToRectangle.js#L12)  
> Since: 3.0.0

## GetRaysFromPointToPolygon

### <static> GetRaysFromPointToPolygon(x, y, polygons)

**Description:**

Projects rays out from the given point to each line segment of the polygons.

If the rays intersect with the polygons, the points of intersection are returned in an array.

If no intersections are found, the returned array will be empty.

Each Vector4 intersection result has the following properties:

The `x` and `y` components contain the point of the intersection.

The `z` component contains the angle of intersection.

The `w` component contains the index of the polygon, in the given array, that triggered the intersection.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The x coordinate to project the rays from. |
| --- | --- | --- | --- |
| y | number | No | The y coordinate to project the rays from. |
| polygons | [Phaser.Geom.Polygon](../class/geom-polygon.md) | Array.<[Phaser.Geom.Polygon](../class/geom-polygon.md)> | No | A single polygon, or array of polygons, to check against the rays. |

**Returns:** Array.<[Phaser.Math.Vector4](../class/math-vector4.md)> - An array containing all intersections in Vector4s.

> Source: [src/geom/intersects/GetRaysFromPointToPolygon.js#L40](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/intersects/GetRaysFromPointToPolygon.js#L40)  
> Since: 3.50.0

## GetRectangleIntersection

### <static> GetRectangleIntersection(rectA, rectB, [output])

**Description:**

Checks if two Rectangle shapes intersect and returns the area of this intersection as Rectangle object.

If optional `output` parameter is omitted, new Rectangle object is created and returned. If there is intersection, it will contain intersection area. If there is no intersection, it wil be empty Rectangle (all values set to zero).

If Rectangle object is passed as `output` and there is intersection, then intersection area data will be loaded into it and it will be returned. If there is no intersection, it will be returned without any change.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| rectA | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | No | The first Rectangle object. |
| --- | --- | --- | --- |
| rectB | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | No | The second Rectangle object. |
| output | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | Yes | Optional Rectangle object. If given, the intersection data will be loaded into it (in case of no intersection, it will be left unchanged). Otherwise, new Rectangle object will be created and returned with either intersection data or empty (all values set to zero), if there is no intersection. |

**Returns:** [Phaser.Geom.Rectangle](../class/geom-rectangle.md) - A rectangle object with intersection data.

> Source: [src/geom/intersects/GetRectangleIntersection.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/intersects/GetRectangleIntersection.js#L10)  
> Since: 3.0.0

## GetRectangleToRectangle

### <static> GetRectangleToRectangle(rectA, rectB, [out])

**Description:**

Checks if two Rectangles intersect and returns the intersection points as a Point object array.

A Rectangle intersects another Rectangle if any part of its bounds is within the other Rectangle's bounds. As such, the two Rectangles are considered "solid". A Rectangle with no width or no height will never intersect another Rectangle.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| rectA | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | No | The first Rectangle to check for intersection. |
| --- | --- | --- | --- |
| rectB | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | No | The second Rectangle to check for intersection. |
| out | array | Yes | An optional array in which to store the points of intersection. |

**Returns:** array - An array with the points of intersection if objects intersect, otherwise an empty array.

> Source: [src/geom/intersects/GetRectangleToRectangle.js#L11](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/intersects/GetRectangleToRectangle.js#L11)  
> Since: 3.0.0

## GetRectangleToTriangle

### <static> GetRectangleToTriangle(rect, triangle, [out])

**Description:**

Checks for intersection between Rectangle shape and Triangle shape,

and returns the intersection points as a Point object array.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| rect | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | No | Rectangle object to test. |
| --- | --- | --- | --- |
| triangle | [Phaser.Geom.Triangle](../class/geom-triangle.md) | No | Triangle object to test. |
| out | array | Yes | An optional array in which to store the points of intersection. |

**Returns:** array - An array with the points of intersection if objects intersect, otherwise an empty array.

> Source: [src/geom/intersects/GetRectangleToTriangle.js#L11](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/intersects/GetRectangleToTriangle.js#L11)  
> Since: 3.0.0

## GetTriangleToCircle

### <static> GetTriangleToCircle(triangle, circle, [out])

**Description:**

Checks if a Triangle and a Circle intersect, and returns the intersection points as a Point object array.

A Circle intersects a Triangle if its center is located within it or if any of the Triangle's sides intersect the Circle. As such, the Triangle and the Circle are considered "solid" for the intersection.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| triangle | [Phaser.Geom.Triangle](../class/geom-triangle.md) | No | The Triangle to check for intersection. |
| --- | --- | --- | --- |
| circle | [Phaser.Geom.Circle](../class/geom-circle.md) | No | The Circle to check for intersection. |
| out | array | Yes | An optional array in which to store the points of intersection. |

**Returns:** array - An array with the points of intersection if objects intersect, otherwise an empty array.

> Source: [src/geom/intersects/GetTriangleToCircle.js#L11](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/intersects/GetTriangleToCircle.js#L11)  
> Since: 3.0.0

## GetTriangleToLine

### <static> GetTriangleToLine(triangle, line, [out])

**Description:**

Checks if a Triangle and a Line intersect, and returns the intersection points as a Point object array.

The Line intersects the Triangle if it starts inside of it, ends inside of it, or crosses any of the Triangle's sides. Thus, the Triangle is considered "solid".

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| triangle | [Phaser.Geom.Triangle](../class/geom-triangle.md) | No | The Triangle to check with. |
| --- | --- | --- | --- |
| line | [Phaser.Geom.Line](../class/geom-line.md) | No | The Line to check with. |
| out | array | Yes | An optional array in which to store the points of intersection. |

**Returns:** array - An array with the points of intersection if objects intersect, otherwise an empty array.

> Source: [src/geom/intersects/GetTriangleToLine.js#L12](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/intersects/GetTriangleToLine.js#L12)  
> Since: 3.0.0

## GetTriangleToTriangle

### <static> GetTriangleToTriangle(triangleA, triangleB, [out])

**Description:**

Checks if two Triangles intersect, and returns the intersection points as a Point object array.

A Triangle intersects another Triangle if any pair of their lines intersects or if any point of one Triangle is within the other Triangle. Thus, the Triangles are considered "solid".

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| triangleA | [Phaser.Geom.Triangle](../class/geom-triangle.md) | No | The first Triangle to check for intersection. |
| --- | --- | --- | --- |
| triangleB | [Phaser.Geom.Triangle](../class/geom-triangle.md) | No | The second Triangle to check for intersection. |
| out | array | Yes | An optional array in which to store the points of intersection. |

**Returns:** array - An array with the points of intersection if objects intersect, otherwise an empty array.

> Source: [src/geom/intersects/GetTriangleToTriangle.js#L11](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/intersects/GetTriangleToTriangle.js#L11)  
> Since: 3.0.0

## LineToCircle

### <static> LineToCircle(line, circle, [nearest])

**Description:**

Checks for intersection between the line segment and circle.

Based on code by [Matt DesLauriers](https://github.com/mattdesl/line-circle-collision/blob/master/LICENSE.md).

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| line | [Phaser.Geom.Line](../class/geom-line.md) | No | The line segment to check. |
| --- | --- | --- | --- |
| circle | [Phaser.Geom.Circle](../class/geom-circle.md) | No | The circle to check against the line. |
| nearest | [Phaser.Geom.Point](../class/geom-point.md) | any | Yes | An optional Point-like object. If given the closest point on the Line where the circle intersects will be stored in this object. |

**Returns:** boolean - `true` if the two objects intersect, otherwise `false`.

> Source: [src/geom/intersects/LineToCircle.js#L12](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/intersects/LineToCircle.js#L12)  
> Since: 3.0.0

## LineToLine

### <static> LineToLine(line1, line2, [out])

**Description:**

Checks if two Lines intersect. If the Lines are identical, they will be treated as parallel and thus non-intersecting.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| line1 | [Phaser.Geom.Line](../class/geom-line.md) | No | The first Line to check. |
| --- | --- | --- | --- |
| line2 | [Phaser.Geom.Line](../class/geom-line.md) | No | The second Line to check. |
| out | [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) | Yes | An optional point-like object in which to store the coordinates of intersection, if needed. |

**Returns:** boolean - `true` if the two Lines intersect, and the `out` object will be populated, if given. Otherwise, `false`.

> Source: [src/geom/intersects/LineToLine.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/intersects/LineToLine.js#L10)  
> Since: 3.0.0

## LineToRectangle

### <static> LineToRectangle(line, rect)

**Description:**

Checks for intersection between the Line and a Rectangle shape, or a rectangle-like

object, with public `x`, `y`, `right` and `bottom` properties, such as a Sprite or Body.

An intersection is considered valid if:

The line starts within, or ends within, the Rectangle.

The line segment intersects one of the 4 rectangle edges.

The for the purposes of this function rectangles are considered 'solid'.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| line | [Phaser.Geom.Line](../class/geom-line.md) | No | The Line to check for intersection. |
| --- | --- | --- | --- |
| rect | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | object | No | The Rectangle to check for intersection. |

**Returns:** boolean - `true` if the Line and the Rectangle intersect, `false` otherwise.

> Source: [src/geom/intersects/LineToRectangle.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/intersects/LineToRectangle.js#L7)  
> Since: 3.0.0

## PointToLine

### <static> PointToLine(point, line, [lineThickness])

**Description:**

Checks if the a Point falls between the two end-points of a Line, based on the given line thickness.

Assumes that the line end points are circular, not square.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| point | [Phaser.Geom.Point](../class/geom-point.md) | any | No |  | The point, or point-like object to check. |
| --- | --- | --- | --- | --- |
| line | [Phaser.Geom.Line](../class/geom-line.md) | No |  | The line segment to test for intersection on. |
| lineThickness | number | Yes | 1 | The line thickness. Assumes that the line end points are circular. |

**Returns:** boolean - `true` if the Point falls on the Line, otherwise `false`.

> Source: [src/geom/intersects/PointToLine.js#L8](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/intersects/PointToLine.js#L8)  
> Since: 3.0.0

## PointToLineSegment

### <static> PointToLineSegment(point, line)

**Description:**

Checks if a Point is located on the given line segment.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| point | [Phaser.Geom.Point](../class/geom-point.md) | No | The Point to check for intersection. |
| --- | --- | --- | --- |
| line | [Phaser.Geom.Line](../class/geom-line.md) | No | The line segment to check for intersection. |

**Returns:** boolean - `true` if the Point is on the given line segment, otherwise `false`.

> Source: [src/geom/intersects/PointToLineSegment.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/intersects/PointToLineSegment.js#L9)  
> Since: 3.0.0

## RectangleToRectangle

### <static> RectangleToRectangle(rectA, rectB)

**Description:**

Checks if two Rectangles intersect.

A Rectangle intersects another Rectangle if any part of its bounds is within the other Rectangle's bounds.

As such, the two Rectangles are considered "solid".

A Rectangle with no width or no height will never intersect another Rectangle.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| rectA | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | No | The first Rectangle to check for intersection. |
| --- | --- | --- | --- |
| rectB | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | No | The second Rectangle to check for intersection. |

**Returns:** boolean - `true` if the two Rectangles intersect, otherwise `false`.

> Source: [src/geom/intersects/RectangleToRectangle.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/intersects/RectangleToRectangle.js#L7)  
> Since: 3.0.0

## RectangleToTriangle

### <static> RectangleToTriangle(rect, triangle)

**Description:**

Checks for intersection between Rectangle shape and Triangle shape.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| rect | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | No | Rectangle object to test. |
| --- | --- | --- | --- |
| triangle | [Phaser.Geom.Triangle](../class/geom-triangle.md) | No | Triangle object to test. |

**Returns:** boolean - A value of `true` if objects intersect; otherwise `false`.

> Source: [src/geom/intersects/RectangleToTriangle.js#L12](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/intersects/RectangleToTriangle.js#L12)  
> Since: 3.0.0

## RectangleToValues

### <static> RectangleToValues(rect, left, right, top, bottom, [tolerance])

**Description:**

Check if rectangle intersects with values.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| rect | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | No |  | The rectangle object |
| --- | --- | --- | --- | --- |
| left | number | No |  | The x coordinate of the left of the Rectangle. |
| right | number | No |  | The x coordinate of the right of the Rectangle. |
| top | number | No |  | The y coordinate of the top of the Rectangle. |
| bottom | number | No |  | The y coordinate of the bottom of the Rectangle. |
| tolerance | number | Yes | 0 | Tolerance allowed in the calculation, expressed in pixels. |

**Returns:** boolean - Returns true if there is an intersection.

> Source: [src/geom/intersects/RectangleToValues.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/intersects/RectangleToValues.js#L7)  
> Since: 3.0.0

## TriangleToCircle

### <static> TriangleToCircle(triangle, circle)

**Description:**

Checks if a Triangle and a Circle intersect.

A Circle intersects a Triangle if its center is located within it or if any of the Triangle's sides intersect the Circle. As such, the Triangle and the Circle are considered "solid" for the intersection.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| triangle | [Phaser.Geom.Triangle](../class/geom-triangle.md) | No | The Triangle to check for intersection. |
| --- | --- | --- | --- |
| circle | [Phaser.Geom.Circle](../class/geom-circle.md) | No | The Circle to check for intersection. |

**Returns:** boolean - `true` if the Triangle and the `Circle` intersect, otherwise `false`.

> Source: [src/geom/intersects/TriangleToCircle.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/intersects/TriangleToCircle.js#L10)  
> Since: 3.0.0

## TriangleToLine

### <static> TriangleToLine(triangle, line)

**Description:**

Checks if a Triangle and a Line intersect.

The Line intersects the Triangle if it starts inside of it, ends inside of it, or crosses any of the Triangle's sides. Thus, the Triangle is considered "solid".

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| triangle | [Phaser.Geom.Triangle](../class/geom-triangle.md) | No | The Triangle to check with. |
| --- | --- | --- | --- |
| line | [Phaser.Geom.Line](../class/geom-line.md) | No | The Line to check with. |

**Returns:** boolean - `true` if the Triangle and the Line intersect, otherwise `false`.

> Source: [src/geom/intersects/TriangleToLine.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/intersects/TriangleToLine.js#L9)  
> Since: 3.0.0

## TriangleToTriangle

### <static> TriangleToTriangle(triangleA, triangleB)

**Description:**

Checks if two Triangles intersect.

A Triangle intersects another Triangle if any pair of their lines intersects or if any point of one Triangle is within the other Triangle. Thus, the Triangles are considered "solid".

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| triangleA | [Phaser.Geom.Triangle](../class/geom-triangle.md) | No | The first Triangle to check for intersection. |
| --- | --- | --- | --- |
| triangleB | [Phaser.Geom.Triangle](../class/geom-triangle.md) | No | The second Triangle to check for intersection. |

**Returns:** boolean - `true` if the Triangles intersect, otherwise `false`.

> Source: [src/geom/intersects/TriangleToTriangle.js#L11](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/intersects/TriangleToTriangle.js#L11)  
> Since: 3.0.0

# Phaser.Geom.Line

## Angle

### <static> Angle(line)

**Description:**

Calculate the angle of the line in radians.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| line | [Phaser.Geom.Line](../class/geom-line.md) | No | The line to calculate the angle of. |
| --- | --- | --- | --- |

**Returns:** number - The angle of the line, in radians.

> Source: [src/geom/line/Angle.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/line/Angle.js#L7)  
> Since: 3.0.0

## BresenhamPoints

### <static> BresenhamPoints(line, [stepRate], [results])

**Description:**

Using Bresenham's line algorithm this will return an array of all coordinates on this line.

The `start` and `end` points are rounded before this runs as the algorithm works on integers.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| line | [Phaser.Geom.Line](../class/geom-line.md) | No |  | The line. |
| --- | --- | --- | --- | --- |
| stepRate | number | Yes | 1 | The optional step rate for the points on the line. |
| results | Array.<[Phaser.Types.Math.Vector2Like](../typedef/types-math.md)> | Yes |  | An optional array to push the resulting coordinates into. |

**Returns:** Array.<[Phaser.Types.Math.Vector2Like](../typedef/types-math.md)> - The array of coordinates on the line.

> Source: [src/geom/line/BresenhamPoints.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/line/BresenhamPoints.js#L7)  
> Since: 3.0.0

## CenterOn

### <static> CenterOn(line, x, y)

**Description:**

Center a line on the given coordinates.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| line | [Phaser.Geom.Line](../class/geom-line.md) | No | The line to center. |
| --- | --- | --- | --- |
| x | number | No | The horizontal coordinate to center the line on. |
| y | number | No | The vertical coordinate to center the line on. |

**Returns:** [Phaser.Geom.Line](../class/geom-line.md) - The centered line.

> Source: [src/geom/line/CenterOn.js#L8](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/line/CenterOn.js#L8)  
> Since: 3.0.0

## Clone

### <static> Clone(source)

**Description:**

Clone the given line.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| source | [Phaser.Geom.Line](../class/geom-line.md) | No | The source line to clone. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Geom.Line](../class/geom-line.md) - The cloned line.

> Source: [src/geom/line/Clone.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/line/Clone.js#L9)  
> Since: 3.0.0

## CopyFrom

### <static> CopyFrom(source, dest)

**Description:**

Copy the values of one line to a destination line.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| source | [Phaser.Geom.Line](../class/geom-line.md) | No | The source line to copy the values from. |
| --- | --- | --- | --- |
| dest | [Phaser.Geom.Line](../class/geom-line.md) | No | The destination line to copy the values to. |

**Returns:** [Phaser.Geom.Line](../class/geom-line.md) - The destination line.

> Source: [src/geom/line/CopyFrom.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/line/CopyFrom.js#L7)  
> Since: 3.0.0

## Equals

### <static> Equals(line, toCompare)

**Description:**

Compare two lines for strict equality.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| line | [Phaser.Geom.Line](../class/geom-line.md) | No | The first line to compare. |
| --- | --- | --- | --- |
| toCompare | [Phaser.Geom.Line](../class/geom-line.md) | No | The second line to compare. |

**Returns:** boolean - Whether the two lines are equal.

> Source: [src/geom/line/Equals.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/line/Equals.js#L7)  
> Since: 3.0.0

## Extend

### <static> Extend(line, left, [right])

**Description:**

Extends the start and end points of a Line by the given amounts.

The amounts can be positive or negative. Positive points will increase the length of the line,

while negative ones will decrease it.

If no `right` value is provided it will extend the length of the line equally in both directions.

Pass a value of zero to leave the start or end point unchanged.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| line | [Phaser.Geom.Line](../class/geom-line.md) | No | The line instance to extend. |
| --- | --- | --- | --- |
| left | number | No | The amount to extend the start of the line by. |
| right | number | Yes | The amount to extend the end of the line by. If not given it will be set to the `left` value. |

**Returns:** [Phaser.Geom.Line](../class/geom-line.md) - The modified Line instance.

> Source: [src/geom/line/Extend.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/line/Extend.js#L9)  
> Since: 3.16.0

## GetEasedPoints

### <static> GetEasedPoints(line, ease, quantity, [collinearThreshold], [easeParams])

**Description:**

Returns an array of `quantity` Points where each point is taken from the given Line,

spaced out according to the ease function specified.

```
Copy
const line = new Phaser.Geom.Line(100, 300, 700, 300);

const points = Phaser.Geom.Line.GetEasedPoints(line, 'sine.out', 32)


```

In the above example, the `points` array will contain 32 points spread-out across

the length of `line`, where the position of each point is determined by the `Sine.out`

ease function.

You can optionally provide a collinear threshold. In this case, the resulting points

are checked against each other, and if they are `< collinearThreshold` distance apart,

they are dropped from the results. This can help avoid lots of clustered points at

far ends of the line with tightly-packed eases such as Quartic. Leave the value set

to zero to skip this check.

Note that if you provide a collinear threshold, the resulting array may not always

contain `quantity` points.

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| line | [Phaser.Geom.Line](../class/geom-line.md) | No |  | The Line object. |
| --- | --- | --- | --- | --- |
| ease | string | function | No |  | The ease to use. This can be either a string from the EaseMap, or a custom function. |
| quantity | number | No |  | The number of points to return. Note that if you provide a `collinearThreshold`, the resulting array may not always contain this number of points. |
| collinearThreshold | number | Yes | 0 | An optional threshold. The final array is reduced so that each point is spaced out at least this distance apart. This helps reduce clustering in noisey eases. |
| easeParams | Array.<number> | Yes |  | An optional array of ease parameters to go with the ease. |

**Returns:** Array.<[Phaser.Geom.Point](../class/geom-point.md)> - An array of Geom.Points containing the coordinates of the points on the line.

> Source: [src/geom/line/GetEasedPoints.js#L11](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/line/GetEasedPoints.js#L11)  
> Since: 3.23.0

## GetMidPoint

### <static> GetMidPoint(line, [out])

**Description:**

Get the midpoint of the given line.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| line | [Phaser.Geom.Line](../class/geom-line.md) | No | The line to get the midpoint of. |
| --- | --- | --- | --- |
| out | [Phaser.Geom.Point](../class/geom-point.md) | object | Yes | An optional point object to store the midpoint in. |

**Returns:** [Phaser.Geom.Point](../class/geom-point.md), object - The midpoint of the Line.

> Source: [src/geom/line/GetMidPoint.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/line/GetMidPoint.js#L9)  
> Since: 3.0.0

## GetNearestPoint

### <static> GetNearestPoint(line, point, [out])

**Description:**

Get the nearest point on a line perpendicular to the given point.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| line | [Phaser.Geom.Line](../class/geom-line.md) | No | The line to get the nearest point on. |
| --- | --- | --- | --- |
| point | [Phaser.Geom.Point](../class/geom-point.md) | object | No | The point to get the nearest point to. |
| out | [Phaser.Geom.Point](../class/geom-point.md) | object | Yes | An optional point, or point-like object, to store the coordinates of the nearest point on the line. |

**Returns:** [Phaser.Geom.Point](../class/geom-point.md), object - The nearest point on the line.

> Source: [src/geom/line/GetNearestPoint.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/line/GetNearestPoint.js#L10)  
> Since: 3.16.0

## GetNormal

### <static> GetNormal(line, [out])

**Description:**

Calculate the normal of the given line.

The normal of a line is a vector that points perpendicular from it.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| line | [Phaser.Geom.Line](../class/geom-line.md) | No | The line to calculate the normal of. |
| --- | --- | --- | --- |
| out | [Phaser.Geom.Point](../class/geom-point.md) | object | Yes | An optional point object to store the normal in. |

**Returns:** [Phaser.Geom.Point](../class/geom-point.md), object - The normal of the Line.

> Source: [src/geom/line/GetNormal.js#L11](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/line/GetNormal.js#L11)  
> Since: 3.0.0

## GetPoint

### <static> GetPoint(line, position, [out])

**Description:**

Get a point on a line that's a given percentage along its length.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| line | [Phaser.Geom.Line](../class/geom-line.md) | No | The line. |
| --- | --- | --- | --- |
| position | number | No | A value between 0 and 1, where 0 is the start, 0.5 is the middle and 1 is the end of the line. |
| out | [Phaser.Geom.Point](../class/geom-point.md) | object | Yes | An optional point, or point-like object, to store the coordinates of the point on the line. |

**Returns:** [Phaser.Geom.Point](../class/geom-point.md), object - The point on the line.

> Source: [src/geom/line/GetPoint.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/line/GetPoint.js#L9)  
> Since: 3.0.0

## GetPoints

### <static> GetPoints(line, quantity, [stepRate], [out])

**Description:**

Get a number of points along a line's length.

Provide a `quantity` to get an exact number of points along the line.

Provide a `stepRate` to ensure a specific distance between each point on the line. Set `quantity` to `0` when

providing a `stepRate`.

See also `GetEasedPoints` for a way to distribute the points across the line according to an ease type or input function.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| line | [Phaser.Geom.Line](../class/geom-line.md) | No | The line. |
| --- | --- | --- | --- |
| quantity | number | No | The number of points to place on the line. Set to `0` to use `stepRate` instead. |
| stepRate | number | Yes | The distance between each point on the line. When set, `quantity` is implied and should be set to `0`. |
| out | array | Array.<[Phaser.Geom.Point](../class/geom-point.md)> | Yes | An optional array of Points, or point-like objects, to store the coordinates of the points on the line. |

**Returns:** array, Array.<[Phaser.Geom.Point](../class/geom-point.md)> - An array of Points, or point-like objects, containing the coordinates of the points on the line.

> Source: [src/geom/line/GetPoints.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/line/GetPoints.js#L10)  
> Since: 3.0.0

## GetShortestDistance

### <static> GetShortestDistance(line, point)

**Description:**

Get the shortest distance from a Line to the given Point.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| line | [Phaser.Geom.Line](../class/geom-line.md) | No | The line to get the distance from. |
| --- | --- | --- | --- |
| point | [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) | No | The point to get the shortest distance to. |

**Returns:** boolean, number - The shortest distance from the line to the point, or `false`.

> Source: [src/geom/line/GetShortestDistance.js#L8](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/line/GetShortestDistance.js#L8)  
> Since: 3.16.0

## Height

### <static> Height(line)

**Description:**

Calculate the height of the given line.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| line | [Phaser.Geom.Line](../class/geom-line.md) | No | The line to calculate the height of. |
| --- | --- | --- | --- |

**Returns:** number - The height of the line.

> Source: [src/geom/line/Height.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/line/Height.js#L7)  
> Since: 3.0.0

## Length

### <static> Length(line)

**Description:**

Calculate the length of the given line.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| line | [Phaser.Geom.Line](../class/geom-line.md) | No | The line to calculate the length of. |
| --- | --- | --- | --- |

**Returns:** number - The length of the line.

> Source: [src/geom/line/Length.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/line/Length.js#L7)  
> Since: 3.0.0

## NormalAngle

### <static> NormalAngle(line)

**Description:**

Get the angle of the normal of the given line in radians.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| line | [Phaser.Geom.Line](../class/geom-line.md) | No | The line to calculate the angle of the normal of. |
| --- | --- | --- | --- |

**Returns:** number - The angle of the normal of the line in radians.

> Source: [src/geom/line/NormalAngle.js#L11](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/line/NormalAngle.js#L11)  
> Since: 3.0.0

## NormalX

### <static> NormalX(line)

**Description:**

Returns the x component of the normal vector of the given line.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| line | [Phaser.Geom.Line](../class/geom-line.md) | No | The Line object to get the normal value from. |
| --- | --- | --- | --- |

**Returns:** number - The x component of the normal vector of the line.

> Source: [src/geom/line/NormalX.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/line/NormalX.js#L10)  
> Since: 3.0.0

## NormalY

### <static> NormalY(line)

**Description:**

The Y value of the normal of the given line.

The normal of a line is a vector that points perpendicular from it.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| line | [Phaser.Geom.Line](../class/geom-line.md) | No | The line to calculate the normal of. |
| --- | --- | --- | --- |

**Returns:** number - The Y value of the normal of the Line.

> Source: [src/geom/line/NormalY.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/line/NormalY.js#L10)  
> Since: 3.0.0

## Offset

### <static> Offset(line, x, y)

**Description:**

Offset a line by the given amount.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| line | [Phaser.Geom.Line](../class/geom-line.md) | No | The line to offset. |
| --- | --- | --- | --- |
| x | number | No | The horizontal offset to add to the line. |
| y | number | No | The vertical offset to add to the line. |

**Returns:** [Phaser.Geom.Line](../class/geom-line.md) - The offset line.

> Source: [src/geom/line/Offset.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/line/Offset.js#L7)  
> Since: 3.0.0

## PerpSlope

### <static> PerpSlope(line)

**Description:**

Calculate the perpendicular slope of the given line.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| line | [Phaser.Geom.Line](../class/geom-line.md) | No | The line to calculate the perpendicular slope of. |
| --- | --- | --- | --- |

**Returns:** number - The perpendicular slope of the line.

> Source: [src/geom/line/PerpSlope.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/line/PerpSlope.js#L7)  
> Since: 3.0.0

## Random

### <static> Random(line, [out])

**Description:**

Returns a random point on a given Line.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| line | [Phaser.Geom.Line](../class/geom-line.md) | No | The Line to calculate the random Point on. |
| --- | --- | --- | --- |
| out | [Phaser.Geom.Point](../class/geom-point.md) | object | Yes | An instance of a Point to be modified. |

**Returns:** [Phaser.Geom.Point](../class/geom-point.md), object - A random Point on the Line.

> Source: [src/geom/line/Random.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/line/Random.js#L9)  
> Since: 3.0.0

## ReflectAngle

### <static> ReflectAngle(lineA, lineB)

**Description:**

Calculate the reflected angle between two lines.

This is the outgoing angle based on the angle of Line 1 and the normalAngle of Line 2.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| lineA | [Phaser.Geom.Line](../class/geom-line.md) | No | The first line. |
| --- | --- | --- | --- |
| lineB | [Phaser.Geom.Line](../class/geom-line.md) | No | The second line. |

**Returns:** number - The reflected angle between each line.

> Source: [src/geom/line/ReflectAngle.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/line/ReflectAngle.js#L10)  
> Since: 3.0.0

## Rotate

### <static> Rotate(line, angle)

**Description:**

Rotate a line around its midpoint by the given angle in radians.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| line | [Phaser.Geom.Line](../class/geom-line.md) | No | The line to rotate. |
| --- | --- | --- | --- |
| angle | number | No | The angle of rotation in radians. |

**Returns:** [Phaser.Geom.Line](../class/geom-line.md) - The rotated line.

> Source: [src/geom/line/Rotate.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/line/Rotate.js#L9)  
> Since: 3.0.0

## RotateAroundPoint

### <static> RotateAroundPoint(line, point, angle)

**Description:**

Rotate a line around a point by the given angle in radians.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| line | [Phaser.Geom.Line](../class/geom-line.md) | No | The line to rotate. |
| --- | --- | --- | --- |
| point | [Phaser.Geom.Point](../class/geom-point.md) | object | No | The point to rotate the line around. |
| angle | number | No | The angle of rotation in radians. |

**Returns:** [Phaser.Geom.Line](../class/geom-line.md) - The rotated line.

> Source: [src/geom/line/RotateAroundPoint.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/line/RotateAroundPoint.js#L9)  
> Since: 3.0.0

## RotateAroundXY

### <static> RotateAroundXY(line, x, y, angle)

**Description:**

Rotate a line around the given coordinates by the given angle in radians.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| line | [Phaser.Geom.Line](../class/geom-line.md) | No | The line to rotate. |
| --- | --- | --- | --- |
| x | number | No | The horizontal coordinate to rotate the line around. |
| y | number | No | The vertical coordinate to rotate the line around. |
| angle | number | No | The angle of rotation in radians. |

**Returns:** [Phaser.Geom.Line](../class/geom-line.md) - The rotated line.

> Source: [src/geom/line/RotateAroundXY.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/line/RotateAroundXY.js#L7)  
> Since: 3.0.0

## SetToAngle

### <static> SetToAngle(line, x, y, angle, length)

**Description:**

Set a line to a given position, angle and length.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| line | [Phaser.Geom.Line](../class/geom-line.md) | No | The line to set. |
| --- | --- | --- | --- |
| x | number | No | The horizontal start position of the line. |
| y | number | No | The vertical start position of the line. |
| angle | number | No | The angle of the line in radians. |
| length | number | No | The length of the line. |

**Returns:** [Phaser.Geom.Line](../class/geom-line.md) - The updated line.

> Source: [src/geom/line/SetToAngle.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/line/SetToAngle.js#L7)  
> Since: 3.0.0

## Slope

### <static> Slope(line)

**Description:**

Calculate the slope of the given line.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| line | [Phaser.Geom.Line](../class/geom-line.md) | No | The line to calculate the slope of. |
| --- | --- | --- | --- |

**Returns:** number - The slope of the line.

> Source: [src/geom/line/Slope.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/line/Slope.js#L7)  
> Since: 3.0.0

## Width

### <static> Width(line)

**Description:**

Calculate the width of the given line.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| line | [Phaser.Geom.Line](../class/geom-line.md) | No | The line to calculate the width of. |
| --- | --- | --- | --- |

**Returns:** number - The width of the line.

> Source: [src/geom/line/Width.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/line/Width.js#L7)  
> Since: 3.0.0

# Phaser.Geom.Mesh

## GenerateGridVerts

### <static> GenerateGridVerts(config)

**Description:**

Creates a grid of vertices based on the given configuration object and optionally adds it to a Mesh.

The size of the grid is given in pixels. An example configuration may be:

`{ width: 256, height: 256, widthSegments: 2, heightSegments: 2, tile: true }`

This will create a grid 256 x 256 pixels in size, split into 2 x 2 segments, with

the texture tiling across the cells.

You can split the grid into segments both vertically and horizontally. This will

generate two faces per grid segment as a result.

The `tile` parameter allows you to control if the tile will repeat across the grid

segments, or be displayed in full.

If adding this grid to a Mesh you can offset the grid via the `x` and `y` properties.

UV coordinates are generated based on the given texture and frame in the config. For

example, no frame is given, the UVs will be in the range 0 to 1. If a frame is given,

such as from a texture atlas, the UVs will be generated within the range of that frame.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| config | [Phaser.Types.Geom.Mesh.GenerateGridConfig](../typedef/types-geom-mesh.md) | No | A Grid configuration object. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Types.Geom.Mesh.GenerateGridVertsResult](../typedef/types-geom-mesh.md) - A Grid Result object, containing the generated vertices and indicies.

> Source: [src/geom/mesh/GenerateGridVerts.js#L17](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/mesh/GenerateGridVerts.js#L17)  
> Since: 3.50.0

## GenerateObjVerts

### <static> GenerateObjVerts(data, [mesh], [scale], [x], [y], [z], [rotateX], [rotateY], [rotateZ], [zIsUp])

**Description:**

This method will return an object containing Face and Vertex instances, generated

from the parsed triangulated OBJ Model data given to this function.

The obj data should have been parsed in advance via the ParseObj function:

```
Copy
var data = Phaser.Geom.Mesh.ParseObj(rawData, flipUV);



var results = GenerateObjVerts(data);


```

Alternatively, you can parse obj files loaded via the OBJFile loader:

```
Copy
preload ()

{

  this.load.obj('alien', 'assets/3d/alien.obj);

}



var results = GenerateObjVerts(this.cache.obj.get('alien));


```

Make sure your 3D package has triangulated the model data prior to exporting it.

You can use the data returned by this function to populate the vertices of a Mesh Game Object.

You may add multiple models to a single Mesh, although they will act as one when

moved or rotated. You can scale the model data, should it be too small (or large) to visualize.

You can also offset the model via the `x`, `y` and `z` parameters.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| data | [Phaser.Types.Geom.Mesh.OBJData](../typedef/types-geom-mesh.md) | No |  | The parsed OBJ model data. |
| --- | --- | --- | --- | --- |
| mesh | [Phaser.GameObjects.Mesh](../class/gameobjects-mesh.md) | Yes |  | An optional Mesh Game Object. If given, the generated Faces will be automatically added to this Mesh. Set to `null` to skip. |
| scale | number | Yes | 1 | An amount to scale the model data by. Use this if the model has exported too small, or large, to see. |
| x | number | Yes | 0 | Translate the model x position by this amount. |
| y | number | Yes | 0 | Translate the model y position by this amount. |
| z | number | Yes | 0 | Translate the model z position by this amount. |
| rotateX | number | Yes | 0 | Rotate the model on the x axis by this amount, in radians. |
| rotateY | number | Yes | 0 | Rotate the model on the y axis by this amount, in radians. |
| rotateZ | number | Yes | 0 | Rotate the model on the z axis by this amount, in radians. |
| zIsUp | boolean | Yes | true | Is the z axis up (true), or is y axis up (false)? |

**Returns:** [Phaser.Types.Geom.Mesh.GenerateVertsResult](../typedef/types-geom-mesh.md) - The parsed Face and Vertex objects.

> Source: [src/geom/mesh/GenerateObjVerts.js#L16](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/mesh/GenerateObjVerts.js#L16)  
> Since: 3.50.0

## GenerateVerts

### <static> GenerateVerts(vertices, uvs, [indicies], [containsZ], [normals], [colors], [alphas], [flipUV])

**Description:**

Generates a set of Face and Vertex objects by parsing the given data.

This method will take vertex data in one of two formats, based on the `containsZ` parameter.

If your vertex data are `x`, `y` pairs, then `containsZ` should be `false` (this is the default)

If your vertex data is groups of `x`, `y` and `z` values, then the `containsZ` parameter must be true.

The `uvs` parameter is a numeric array consisting of `u` and `v` pairs.

The `normals` parameter is a numeric array consisting of `x`, `y` vertex normal values and, if `containsZ` is true, `z` values as well.

The `indicies` parameter is an optional array that, if given, is an indexed list of vertices to be added.

The `colors` parameter is an optional array, or single value, that if given sets the color of each vertex created.

The `alphas` parameter is an optional array, or single value, that if given sets the alpha of each vertex created.

When providing indexed data it is assumed that *all* of the arrays are indexed, not just the vertices.

The following example will create a 256 x 256 sized quad using an index array:

```
Copy
const vertices = [

  -128, 128,

  128, 128,

  -128, -128,

  128, -128

];



const uvs = [

  0, 1,

  1, 1,

  0, 0,

  1, 0

];



const indices = [ 0, 2, 1, 2, 3, 1 ];



GenerateVerts(vertices, uvs, indicies);


```

If the data is not indexed, it's assumed that the arrays all contain sequential data.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| vertices | Array.<number> | No |  | The vertices array. Either `xy` pairs, or `xyz` if the `containsZ` parameter is `true`. |
| --- | --- | --- | --- | --- |
| uvs | Array.<number> | No |  | The UVs pairs array. |
| indicies | Array.<number> | Yes |  | Optional vertex indicies array. If you don't have one, pass `null` or an empty array. |
| containsZ | boolean | Yes | false | Does the vertices data include a `z` component? |
| normals | Array.<number> | Yes |  | Optional vertex normals array. If you don't have one, pass `null` or an empty array. |
| colors | number | Array.<number> | Yes | "0xffffff" | An array of colors, one per vertex, or a single color value applied to all vertices. |
| alphas | number | Array.<number> | Yes | 1 | An array of alpha values, one per vertex, or a single alpha value applied to all vertices. |
| flipUV | boolean | Yes | false | Flip the UV coordinates? |

**Returns:** [Phaser.Types.Geom.Mesh.GenerateVertsResult](../typedef/types-geom-mesh.md) - The parsed Face and Vertex objects.

> Source: [src/geom/mesh/GenerateVerts.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/mesh/GenerateVerts.js#L10)  
> Since: 3.50.0

## ParseObj

### <static> ParseObj(data, [flipUV])

**Description:**

Parses a Wavefront OBJ File, extracting the models from it and returning them in an array.

The model data *must* be triangulated for a Mesh Game Object to be able to render it.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| data | string | No |  | The OBJ File data as a raw string. |
| --- | --- | --- | --- | --- |
| flipUV | boolean | Yes | true | Flip the UV coordinates? |

**Returns:** [Phaser.Types.Geom.Mesh.OBJData](../typedef/types-geom-mesh.md) - The parsed model and material data.

> Source: [src/geom/mesh/ParseObj.js#L226](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/mesh/ParseObj.js#L226)  
> Since: 3.50.0

## ParseObjMaterial

### <static> ParseObjMaterial(mtl)

**Description:**

Takes a Wavefront Material file and extracts the diffuse reflectivity of the named

materials, converts them to integer color values and returns them.

This is used internally by the `addOBJ` and `addModel` methods, but is exposed for

public consumption as well.

Note this only works with diffuse values, specified in the `Kd r g b` format, where

`g` and `b` are optional, but `r` is required. It does not support spectral rfl files,

or any other material statement (such as `Ka` or `Ks`)

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| mtl | string | No | The OBJ MTL file as a raw string, i.e. loaded via `this.load.text`. |
| --- | --- | --- | --- |

**Returns:** object - The parsed material colors, where each property of the object matches the material name.

> Source: [src/geom/mesh/ParseObjMaterial.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/mesh/ParseObjMaterial.js#L9)  
> Since: 3.50.0

## RotateFace

### <static> RotateFace(face, angle, [cx], [cy])

**Description:**

Rotates the vertices of a Face to the given angle.

The actual vertex positions are adjusted, not their transformed positions.

Therefore, this updates the vertex data directly.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| face | [Phaser.Geom.Mesh.Face](../class/geom-mesh-face.md) | No | The Face to rotate. |
| --- | --- | --- | --- |
| angle | number | No | The angle to rotate to, in radians. |
| cx | number | Yes | An optional center of rotation. If not given, the Face in-center is used. |
| cy | number | Yes | An optional center of rotation. If not given, the Face in-center is used. |

> Source: [src/geom/mesh/RotateFace.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/mesh/RotateFace.js#L7)  
> Since: 3.50.0

# Phaser.Geom.Point

## Ceil

### <static> Ceil(point)

**Description:**

Apply `Math.ceil()` to each coordinate of the given Point.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| point | [Phaser.Geom.Point](../class/geom-point.md) | No | The Point to ceil. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Geom.Point](../class/geom-point.md) - The Point with `Math.ceil()` applied to its coordinates.

> Source: [src/geom/point/Ceil.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/point/Ceil.js#L7)  
> Since: 3.0.0

## Clone

### <static> Clone(source)

**Description:**

Clone the given Point.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| source | [Phaser.Geom.Point](../class/geom-point.md) | No | The source Point to clone. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Geom.Point](../class/geom-point.md) - The cloned Point.

> Source: [src/geom/point/Clone.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/point/Clone.js#L9)  
> Since: 3.0.0

## CopyFrom

### <static> CopyFrom(source, dest)

**Description:**

Copy the values of one Point to a destination Point.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| source | [Phaser.Geom.Point](../class/geom-point.md) | No | The source Point to copy the values from. |
| --- | --- | --- | --- |
| dest | [Phaser.Geom.Point](../class/geom-point.md) | No | The destination Point to copy the values to. |

**Returns:** [Phaser.Geom.Point](../class/geom-point.md) - The destination Point.

> Source: [src/geom/point/CopyFrom.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/point/CopyFrom.js#L7)  
> Since: 3.0.0

## Equals

### <static> Equals(point, toCompare)

**Description:**

A comparison of two `Point` objects to see if they are equal.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| point | [Phaser.Geom.Point](../class/geom-point.md) | No | The original `Point` to compare against. |
| --- | --- | --- | --- |
| toCompare | [Phaser.Geom.Point](../class/geom-point.md) | No | The second `Point` to compare. |

**Returns:** boolean - Returns true if the both `Point` objects are equal.

> Source: [src/geom/point/Equals.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/point/Equals.js#L7)  
> Since: 3.0.0

## Floor

### <static> Floor(point)

**Description:**

Apply `Math.ceil()` to each coordinate of the given Point.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| point | [Phaser.Geom.Point](../class/geom-point.md) | No | The Point to floor. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Geom.Point](../class/geom-point.md) - The Point with `Math.floor()` applied to its coordinates.

> Source: [src/geom/point/Floor.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/point/Floor.js#L7)  
> Since: 3.0.0

## GetCentroid

### <static> GetCentroid(points, [out])

**Description:**

Get the centroid or geometric center of a plane figure (the arithmetic mean position of all the points in the figure).

Informally, it is the point at which a cutout of the shape could be perfectly balanced on the tip of a pin.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| points | Array.<[Phaser.Types.Math.Vector2Like](../typedef/types-math.md)> | No | An array of Vector2Like objects to get the geometric center of. |
| --- | --- | --- | --- |
| out | [Phaser.Geom.Point](../class/geom-point.md) | Yes | A Point object to store the output coordinates in. If not given, a new Point instance is created. |

**Returns:** [Phaser.Geom.Point](../class/geom-point.md) - A Point object representing the geometric center of the given points.

> Source: [src/geom/point/GetCentroid.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/point/GetCentroid.js#L9)  
> Since: 3.0.0

## GetMagnitude

### <static> GetMagnitude(point)

**Description:**

Calculate the magnitude of the point, which equivalent to the length of the line from the origin to this point.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| point | [Phaser.Geom.Point](../class/geom-point.md) | No | The point to calculate the magnitude for |
| --- | --- | --- | --- |

**Returns:** number - The resulting magnitude

> Source: [src/geom/point/GetMagnitude.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/point/GetMagnitude.js#L7)  
> Since: 3.0.0

## GetMagnitudeSq

### <static> GetMagnitudeSq(point)

**Description:**

Calculates the square of magnitude of given point.(Can be used for fast magnitude calculation of point)

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| point | [Phaser.Geom.Point](../class/geom-point.md) | No | Returns square of the magnitude/length of given point. |
| --- | --- | --- | --- |

**Returns:** number - Returns square of the magnitude of given point.

> Source: [src/geom/point/GetMagnitudeSq.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/point/GetMagnitudeSq.js#L7)  
> Since: 3.0.0

## GetRectangleFromPoints

### <static> GetRectangleFromPoints(points, [out])

**Description:**

Calculates the Axis Aligned Bounding Box (or aabb) from an array of points.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| points | Array.<[Phaser.Types.Math.Vector2Like](../typedef/types-math.md)> | No | An array of Vector2Like objects to get the AABB from. |
| --- | --- | --- | --- |
| out | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | Yes | A Rectangle object to store the results in. If not given, a new Rectangle instance is created. |

**Returns:** [Phaser.Geom.Rectangle](../class/geom-rectangle.md) - A Rectangle object holding the AABB values for the given points.

> Source: [src/geom/point/GetRectangleFromPoints.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/point/GetRectangleFromPoints.js#L9)  
> Since: 3.0.0

## Interpolate

### <static> Interpolate(pointA, pointB, [t], [out])

**Description:**

Returns the linear interpolation point between the two given points, based on `t`.

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| pointA | [Phaser.Geom.Point](../class/geom-point.md) | No |  | The starting `Point` for the interpolation. |
| --- | --- | --- | --- | --- |
| pointB | [Phaser.Geom.Point](../class/geom-point.md) | No |  | The target `Point` for the interpolation. |
| t | number | Yes | 0 | The amount to interpolate between the two points. Generally, a value between 0 (returns the starting `Point`) and 1 (returns the target `Point`). If omitted, 0 is used. |
| out | [Phaser.Geom.Point](../class/geom-point.md) | object | Yes |  | An optional `Point` object whose `x` and `y` values will be set to the result of the interpolation (can also be any object with `x` and `y` properties). If omitted, a new `Point` created and returned. |

**Returns:** [Phaser.Geom.Point](../class/geom-point.md), object - Either the object from the `out` argument with the properties `x` and `y` set to the result of the interpolation or a newly created `Point` object.

> Source: [src/geom/point/Interpolate.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/point/Interpolate.js#L9)  
> Since: 3.0.0

## Invert

### <static> Invert(point)

**Description:**

Swaps the X and the Y coordinate of a point.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| point | [Phaser.Geom.Point](../class/geom-point.md) | No | The Point to modify. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Geom.Point](../class/geom-point.md) - The modified `point`.

> Source: [src/geom/point/Invert.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/point/Invert.js#L7)  
> Since: 3.0.0

## Negative

### <static> Negative(point, [out])

**Description:**

Inverts a Point's coordinates.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| point | [Phaser.Geom.Point](../class/geom-point.md) | No | The Point to invert. |
| --- | --- | --- | --- |
| out | [Phaser.Geom.Point](../class/geom-point.md) | Yes | The Point to return the inverted coordinates in. |

**Returns:** [Phaser.Geom.Point](../class/geom-point.md) - The modified `out` Point, or a new Point if none was provided.

> Source: [src/geom/point/Negative.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/point/Negative.js#L9)  
> Since: 3.0.0

## Project

### <static> Project(pointA, pointB, [out])

**Description:**

Calculates the vector projection of `pointA` onto the nonzero `pointB`. This is the

orthogonal projection of `pointA` onto a straight line parallel to `pointB`.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pointA | [Phaser.Geom.Point](../class/geom-point.md) | No | Point A, to be projected onto Point B. |
| --- | --- | --- | --- |
| pointB | [Phaser.Geom.Point](../class/geom-point.md) | No | Point B, to have Point A projected upon it. |
| out | [Phaser.Geom.Point](../class/geom-point.md) | Yes | The Point object to store the position in. If not given, a new Point instance is created. |

**Returns:** [Phaser.Geom.Point](../class/geom-point.md) - A Point object holding the coordinates of the vector projection of `pointA` onto `pointB`.

> Source: [src/geom/point/Project.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/point/Project.js#L10)  
> Since: 3.0.0

## ProjectUnit

### <static> ProjectUnit(pointA, pointB, [out])

**Description:**

Calculates the vector projection of `pointA` onto the nonzero `pointB`. This is the

orthogonal projection of `pointA` onto a straight line paralle to `pointB`.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pointA | [Phaser.Geom.Point](../class/geom-point.md) | No | Point A, to be projected onto Point B. Must be a normalized point with a magnitude of 1. |
| --- | --- | --- | --- |
| pointB | [Phaser.Geom.Point](../class/geom-point.md) | No | Point B, to have Point A projected upon it. |
| out | [Phaser.Geom.Point](../class/geom-point.md) | Yes | The Point object to store the position in. If not given, a new Point instance is created. |

**Returns:** [Phaser.Geom.Point](../class/geom-point.md) - A unit Point object holding the coordinates of the vector projection of `pointA` onto `pointB`.

> Source: [src/geom/point/ProjectUnit.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/point/ProjectUnit.js#L9)  
> Since: 3.0.0

## SetMagnitude

### <static> SetMagnitude(point, magnitude)

**Description:**

Changes the magnitude (length) of a two-dimensional vector without changing its direction.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| point | [Phaser.Geom.Point](../class/geom-point.md) | No | The Point to treat as the end point of the vector. |
| --- | --- | --- | --- |
| magnitude | number | No | The new magnitude of the vector. |

**Returns:** [Phaser.Geom.Point](../class/geom-point.md) - The modified Point.

> Source: [src/geom/point/SetMagnitude.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/point/SetMagnitude.js#L9)  
> Since: 3.0.0

# Phaser.Geom.Polygon

## Clone

### <static> Clone(polygon)

**Description:**

Create a new polygon which is a copy of the specified polygon

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| polygon | [Phaser.Geom.Polygon](../class/geom-polygon.md) | No | The polygon to create a clone of |
| --- | --- | --- | --- |

**Returns:** [Phaser.Geom.Polygon](../class/geom-polygon.md) - A new separate Polygon cloned from the specified polygon, based on the same points.

> Source: [src/geom/polygon/Clone.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/polygon/Clone.js#L9)  
> Since: 3.0.0

## Contains

### <static> Contains(polygon, x, y)

**Description:**

Checks if a point is within the bounds of a Polygon.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| polygon | [Phaser.Geom.Polygon](../class/geom-polygon.md) | No | The Polygon to check against. |
| --- | --- | --- | --- |
| x | number | No | The X coordinate of the point to check. |
| y | number | No | The Y coordinate of the point to check. |

**Returns:** boolean - `true` if the point is within the bounds of the Polygon, otherwise `false`.

> Source: [src/geom/polygon/Contains.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/polygon/Contains.js#L10)  
> Since: 3.0.0

## ContainsPoint

### <static> ContainsPoint(polygon, point)

**Description:**

Checks the given Point again the Polygon to see if the Point lays within its vertices.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| polygon | [Phaser.Geom.Polygon](../class/geom-polygon.md) | No | The Polygon to check. |
| --- | --- | --- | --- |
| point | [Phaser.Geom.Point](../class/geom-point.md) | No | The Point to check if it's within the Polygon. |

**Returns:** boolean - `true` if the Point is within the Polygon, otherwise `false`.

> Source: [src/geom/polygon/ContainsPoint.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/polygon/ContainsPoint.js#L9)  
> Since: 3.0.0

## Earcut

### <static> Earcut(data, [holeIndices], [dimensions])

**Description:**

This module implements a modified ear slicing algorithm, optimized by z-order curve hashing and extended to

handle holes, twisted polygons, degeneracies and self-intersections in a way that doesn't guarantee correctness

of triangulation, but attempts to always produce acceptable results for practical data.

Example:

```
Copy
const triangles = Phaser.Geom.Polygon.Earcut([10,0, 0,50, 60,60, 70,10]); // returns [1,0,3, 3,2,1]


```

Each group of three vertex indices in the resulting array forms a triangle.

```
Copy
// triangulating a polygon with a hole

earcut([0,0, 100,0, 100,100, 0,100,  20,20, 80,20, 80,80, 20,80], [4]);

// [3,0,4, 5,4,0, 3,4,7, 5,0,1, 2,3,7, 6,5,1, 2,7,6, 6,1,2]



// triangulating a polygon with 3d coords

earcut([10,0,1, 0,50,2, 60,60,3, 70,10,4], null, 3);

// [1,0,3, 3,2,1]


```

If you pass a single vertex as a hole, Earcut treats it as a Steiner point.

If your input is a multi-dimensional array (e.g. GeoJSON Polygon), you can convert it to the format

expected by Earcut with `Phaser.Geom.Polygon.Earcut.flatten`:

```
Copy
var data = earcut.flatten(geojson.geometry.coordinates);

var triangles = earcut(data.vertices, data.holes, data.dimensions);


```

After getting a triangulation, you can verify its correctness with `Phaser.Geom.Polygon.Earcut.deviation`:

```
Copy
var deviation = earcut.deviation(vertices, holes, dimensions, triangles);


```

Returns the relative difference between the total area of triangles and the area of the input polygon.

0 means the triangulation is fully correct.

For more information see <https://github.com/mapbox/earcut>

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| data | Array.<number> | No |  | A flat array of vertex coordinate, like [x0,y0, x1,y1, x2,y2, ...] |
| --- | --- | --- | --- | --- |
| holeIndices | Array.<number> | Yes |  | An array of hole indices if any (e.g. [5, 8] for a 12-vertex input would mean one hole with vertices 5–7 and another with 8–11). |
| dimensions | number | Yes | 2 | The number of coordinates per vertex in the input array (2 by default). |

**Returns:** Array.<number> - An array of triangulated data.

> Source: [src/geom/polygon/Earcut.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/polygon/Earcut.js#L7)  
> Since: 3.50.0

## GetAABB

### <static> GetAABB(polygon, [out])

**Description:**

Calculates the bounding AABB rectangle of a polygon.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| polygon | [Phaser.Geom.Polygon](../class/geom-polygon.md) | No | The polygon that should be calculated. |
| --- | --- | --- | --- |
| out | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | object | Yes | The rectangle or object that has x, y, width, and height properties to store the result. Optional. |

**Returns:** [Phaser.Geom.Rectangle](../class/geom-rectangle.md), object - The resulting rectangle or object that is passed in with position and dimensions of the polygon's AABB.

> Source: [src/geom/polygon/GetAABB.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/polygon/GetAABB.js#L9)  
> Since: 3.0.0

## GetNumberArray

### <static> GetNumberArray(polygon, [output])

**Description:**

Stores all of the points of a Polygon into a flat array of numbers following the sequence [ x,y, x,y, x,y ],

i.e. each point of the Polygon, in the order it's defined, corresponds to two elements of the resultant

array for the point's X and Y coordinate.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| polygon | [Phaser.Geom.Polygon](../class/geom-polygon.md) | No | The Polygon whose points to export. |
| --- | --- | --- | --- |
| output | array | Array.<number> | Yes | An array to which the points' coordinates should be appended. |

**Returns:** array, Array.<number> - The modified `output` array, or a new array if none was given.

> Source: [src/geom/polygon/GetNumberArray.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/polygon/GetNumberArray.js#L9)  
> Since: 3.0.0

## GetPoints

### <static> GetPoints(polygon, quantity, [stepRate], [output])

**Description:**

Returns an array of Point objects containing the coordinates of the points around the perimeter of the Polygon,

based on the given quantity or stepRate values.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| polygon | [Phaser.Geom.Polygon](../class/geom-polygon.md) | No | The Polygon to get the points from. |
| --- | --- | --- | --- |
| quantity | number | No | The amount of points to return. If a falsey value the quantity will be derived from the `stepRate` instead. |
| stepRate | number | Yes | Sets the quantity by getting the perimeter of the Polygon and dividing it by the stepRate. |
| output | array | Yes | An array to insert the points in to. If not provided a new array will be created. |

**Returns:** Array.<[Phaser.Geom.Point](../class/geom-point.md)> - An array of Point objects pertaining to the points around the perimeter of the Polygon.

> Source: [src/geom/polygon/GetPoints.js#L11](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/polygon/GetPoints.js#L11)  
> Since: 3.12.0

## Perimeter

### <static> Perimeter(polygon)

**Description:**

Returns the perimeter of the given Polygon.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| polygon | [Phaser.Geom.Polygon](../class/geom-polygon.md) | No | The Polygon to get the perimeter of. |
| --- | --- | --- | --- |

**Returns:** number - The perimeter of the Polygon.

> Source: [src/geom/polygon/Perimeter.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/polygon/Perimeter.js#L10)  
> Since: 3.12.0

## Reverse

### <static> Reverse(polygon)

**Description:**

Reverses the order of the points of a Polygon.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| polygon | [Phaser.Geom.Polygon](../class/geom-polygon.md) | No | The Polygon to modify. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Geom.Polygon](../class/geom-polygon.md) - The modified Polygon.

> Source: [src/geom/polygon/Reverse.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/polygon/Reverse.js#L7)  
> Since: 3.0.0

## Simplify

### <static> Simplify(polygon, [tolerance], [highestQuality])

**Description:**

Takes a Polygon object and simplifies the points by running them through a combination of

Douglas-Peucker and Radial Distance algorithms. Simplification dramatically reduces the number of

points in a polygon while retaining its shape, giving a huge performance boost when processing

it and also reducing visual noise.

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| polygon | [Phaser.Geom.Polygon](../class/geom-polygon.md) | No |  | The polygon to be simplified. The polygon will be modified in-place and returned. |
| --- | --- | --- | --- | --- |
| tolerance | number | Yes | 1 | Affects the amount of simplification (in the same metric as the point coordinates). |
| highestQuality | boolean | Yes | false | Excludes distance-based preprocessing step which leads to highest quality simplification but runs ~10-20 times slower. |

**Returns:** [Phaser.Geom.Polygon](../class/geom-polygon.md) - The input polygon.

> Source: [src/geom/polygon/Simplify.js#L160](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/polygon/Simplify.js#L160)  
> Since: 3.50.0

## Smooth

### <static> Smooth(polygon)

**Description:**

Takes a Polygon object and applies Chaikin's smoothing algorithm on its points.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| polygon | [Phaser.Geom.Polygon](../class/geom-polygon.md) | No | The polygon to be smoothed. The polygon will be modified in-place and returned. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Geom.Polygon](../class/geom-polygon.md) - The input polygon.

> Source: [src/geom/polygon/Smooth.js#L19](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/polygon/Smooth.js#L19)  
> Since: 3.13.0

## Translate

### <static> Translate(polygon, x, y)

**Description:**

Tranlates the points of the given Polygon.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| polygon | [Phaser.Geom.Polygon](../class/geom-polygon.md) | No | The Polygon to modify. |
| --- | --- | --- | --- |
| x | number | No | The amount to horizontally translate the points by. |
| y | number | No | The amount to vertically translate the points by. |

**Returns:** [Phaser.Geom.Polygon](../class/geom-polygon.md) - The modified Polygon.

> Source: [src/geom/polygon/Translate.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/polygon/Translate.js#L7)  
> Since: 3.50.0

# Phaser.Geom.Rectangle

## Area

### <static> Area(rect)

**Description:**

Calculates the area of the given Rectangle object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| rect | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | No | The rectangle to calculate the area of. |
| --- | --- | --- | --- |

**Returns:** number - The area of the Rectangle object.

> Source: [src/geom/rectangle/Area.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/Area.js#L7)  
> Since: 3.0.0

## Ceil

### <static> Ceil(rect)

**Description:**

Rounds a Rectangle's position up to the smallest integer greater than or equal to each current coordinate.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| rect | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | No | The Rectangle to adjust. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Geom.Rectangle](../class/geom-rectangle.md) - The adjusted Rectangle.

> Source: [src/geom/rectangle/Ceil.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/Ceil.js#L7)  
> Since: 3.0.0

## CeilAll

### <static> CeilAll(rect)

**Description:**

Rounds a Rectangle's position and size up to the smallest integer greater than or equal to each respective value.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| rect | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | No | The Rectangle to modify. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Geom.Rectangle](../class/geom-rectangle.md) - The modified Rectangle.

> Source: [src/geom/rectangle/CeilAll.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/CeilAll.js#L7)  
> Since: 3.0.0

## CenterOn

### <static> CenterOn(rect, x, y)

**Description:**

Moves the top-left corner of a Rectangle so that its center is at the given coordinates.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| rect | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | No | The Rectangle to be centered. |
| --- | --- | --- | --- |
| x | number | No | The X coordinate of the Rectangle's center. |
| y | number | No | The Y coordinate of the Rectangle's center. |

**Returns:** [Phaser.Geom.Rectangle](../class/geom-rectangle.md) - The centered rectangle.

> Source: [src/geom/rectangle/CenterOn.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/CenterOn.js#L7)  
> Since: 3.0.0

## Clone

### <static> Clone(source)

**Description:**

Creates a new Rectangle which is identical to the given one.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| source | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | No | The Rectangle to clone. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Geom.Rectangle](../class/geom-rectangle.md) - The newly created Rectangle, which is separate from the given one.

> Source: [src/geom/rectangle/Clone.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/Clone.js#L9)  
> Since: 3.0.0

## Contains

### <static> Contains(rect, x, y)

**Description:**

Checks if a given point is inside a Rectangle's bounds.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| rect | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | No | The Rectangle to check. |
| --- | --- | --- | --- |
| x | number | No | The X coordinate of the point to check. |
| y | number | No | The Y coordinate of the point to check. |

**Returns:** boolean - `true` if the point is within the Rectangle's bounds, otherwise `false`.

> Source: [src/geom/rectangle/Contains.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/Contains.js#L7)  
> Since: 3.0.0

## ContainsPoint

### <static> ContainsPoint(rect, point)

**Description:**

Determines whether the specified point is contained within the rectangular region defined by this Rectangle object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| rect | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | No | The Rectangle object. |
| --- | --- | --- | --- |
| point | [Phaser.Geom.Point](../class/geom-point.md) | No | The point object to be checked. Can be a Phaser Point object or any object with x and y values. |

**Returns:** boolean - A value of true if the Rectangle object contains the specified point, otherwise false.

> Source: [src/geom/rectangle/ContainsPoint.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/ContainsPoint.js#L9)  
> Since: 3.0.0

## ContainsRect

### <static> ContainsRect(rectA, rectB)

**Description:**

Tests if one rectangle fully contains another.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| rectA | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | No | The first rectangle. |
| --- | --- | --- | --- |
| rectB | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | No | The second rectangle. |

**Returns:** boolean - True only if rectA fully contains rectB.

> Source: [src/geom/rectangle/ContainsRect.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/ContainsRect.js#L7)  
> Since: 3.0.0

## CopyFrom

### <static> CopyFrom(source, dest)

**Description:**

Copy the values of one Rectangle to a destination Rectangle.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| source | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | No | The source Rectangle to copy the values from. |
| --- | --- | --- | --- |
| dest | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | No | The destination Rectangle to copy the values to. |

**Returns:** [Phaser.Geom.Rectangle](../class/geom-rectangle.md) - The destination Rectangle.

> Source: [src/geom/rectangle/CopyFrom.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/CopyFrom.js#L7)  
> Since: 3.0.0

## Decompose

### <static> Decompose(rect, [out])

**Description:**

Create an array of points for each corner of a Rectangle

If an array is specified, each point object will be added to the end of the array, otherwise a new array will be created.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| rect | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | No | The Rectangle object to be decomposed. |
| --- | --- | --- | --- |
| out | array | Yes | If provided, each point will be added to this array. |

**Returns:** array - Will return the array you specified or a new array containing the points of the Rectangle.

> Source: [src/geom/rectangle/Decompose.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/Decompose.js#L7)  
> Since: 3.0.0

## Equals

### <static> Equals(rect, toCompare)

**Description:**

Compares the `x`, `y`, `width` and `height` properties of two rectangles.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| rect | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | No | Rectangle A |
| --- | --- | --- | --- |
| toCompare | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | No | Rectangle B |

**Returns:** boolean - `true` if the rectangles' properties are an exact match, otherwise `false`.

> Source: [src/geom/rectangle/Equals.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/Equals.js#L7)  
> Since: 3.0.0

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
| target | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | No | The target rectangle to adjust. |
| --- | --- | --- | --- |
| source | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | No | The source rectangle to envelop the target in. |

**Returns:** [Phaser.Geom.Rectangle](../class/geom-rectangle.md) - The modified target rectangle instance.

> Source: [src/geom/rectangle/FitInside.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/FitInside.js#L9)  
> Since: 3.0.0

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
| target | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | No | The target rectangle to adjust. |
| --- | --- | --- | --- |
| source | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | No | The source rectangle to envelope the target in. |

**Returns:** [Phaser.Geom.Rectangle](../class/geom-rectangle.md) - The modified target rectangle instance.

> Source: [src/geom/rectangle/FitOutside.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/FitOutside.js#L9)  
> Since: 3.0.0

## Floor

### <static> Floor(rect)

**Description:**

Rounds down (floors) the top left X and Y coordinates of the given Rectangle to the largest integer less than or equal to them

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| rect | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | No | The rectangle to floor the top left X and Y coordinates of |
| --- | --- | --- | --- |

**Returns:** [Phaser.Geom.Rectangle](../class/geom-rectangle.md) - The rectangle that was passed to this function with its coordinates floored.

> Source: [src/geom/rectangle/Floor.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/Floor.js#L7)  
> Since: 3.0.0

## FloorAll

### <static> FloorAll(rect)

**Description:**

Rounds a Rectangle's position and size down to the largest integer less than or equal to each current coordinate or dimension.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| rect | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | No | The Rectangle to adjust. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Geom.Rectangle](../class/geom-rectangle.md) - The adjusted Rectangle.

> Source: [src/geom/rectangle/FloorAll.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/FloorAll.js#L7)  
> Since: 3.0.0

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
| out | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | Yes | Optional Rectangle to adjust. |

**Returns:** [Phaser.Geom.Rectangle](../class/geom-rectangle.md) - The adjusted `out` Rectangle, or a new Rectangle if none was provided.

> Source: [src/geom/rectangle/FromPoints.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/FromPoints.js#L10)  
> Since: 3.0.0

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
| out | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | Yes | Optional Rectangle to adjust. |

**Returns:** [Phaser.Geom.Rectangle](../class/geom-rectangle.md) - The adjusted `out` Rectangle, or a new Rectangle if none was provided.

> Source: [src/geom/rectangle/FromXY.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/FromXY.js#L9)  
> Since: 3.23.0

## GetAspectRatio

### <static> GetAspectRatio(rect)

**Description:**

Calculates the width/height ratio of a rectangle.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| rect | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | No | The rectangle. |
| --- | --- | --- | --- |

**Returns:** number - The width/height ratio of the rectangle.

> Source: [src/geom/rectangle/GetAspectRatio.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/GetAspectRatio.js#L7)  
> Since: 3.0.0

## GetCenter

### <static> GetCenter(rect, [out])

**Description:**

Returns the center of a Rectangle as a Point.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| rect | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | No | The Rectangle to get the center of. |
| --- | --- | --- | --- |
| out | [Phaser.Geom.Point](../class/geom-point.md) | object | Yes | Optional point-like object to update with the center coordinates. |

**Returns:** [Phaser.Geom.Point](../class/geom-point.md), object - The modified `out` object, or a new Point if none was provided.

> Source: [src/geom/rectangle/GetCenter.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/GetCenter.js#L9)  
> Since: 3.0.0

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
| rectangle | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | No | The Rectangle to get the perimeter point from. |
| --- | --- | --- | --- |
| position | number | No | The normalized distance into the Rectangle's perimeter to return. |
| out | [Phaser.Geom.Point](../class/geom-point.md) | object | Yes | An object to update with the `x` and `y` coordinates of the point. |

**Returns:** [Phaser.Geom.Point](../class/geom-point.md) - The updated `output` object, or a new Point if no `output` object was given.

> Source: [src/geom/rectangle/GetPoint.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/GetPoint.js#L10)  
> Since: 3.0.0

## GetPoints

### <static> GetPoints(rectangle, step, quantity, [out])

**Description:**

Return an array of points from the perimeter of the rectangle, each spaced out based on the quantity or step required.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| rectangle | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | No | The Rectangle object to get the points from. |
| --- | --- | --- | --- |
| step | number | No | Step between points. Used to calculate the number of points to return when quantity is falsey. Ignored if quantity is positive. |
| quantity | number | No | The number of evenly spaced points from the rectangles perimeter to return. If falsey, step param will be used to calculate the number of points. |
| out | array | Array.<[Phaser.Geom.Point](../class/geom-point.md)> | Yes | An optional array to store the points in. |

**Returns:** array, Array.<[Phaser.Geom.Point](../class/geom-point.md)> - An array of Points from the perimeter of the rectangle.

> Source: [src/geom/rectangle/GetPoints.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/GetPoints.js#L10)  
> Since: 3.0.0

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
| rect | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | No | The Rectangle to get the size from. |
| --- | --- | --- | --- |
| out | [Phaser.Geom.Point](../class/geom-point.md) | object | Yes | The Point object to store the size in. If not given, a new Point instance is created. |

**Returns:** [Phaser.Geom.Point](../class/geom-point.md), object - A Point object where `x` holds the width and `y` holds the height of the Rectangle.

> Source: [src/geom/rectangle/GetSize.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/GetSize.js#L9)  
> Since: 3.0.0

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
| rect | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | No | The Rectangle to inflate. |
| --- | --- | --- | --- |
| x | number | No | How many pixels the left and the right side should be moved by horizontally. |
| y | number | No | How many pixels the top and the bottom side should be moved by vertically. |

**Returns:** [Phaser.Geom.Rectangle](../class/geom-rectangle.md) - The inflated Rectangle.

> Source: [src/geom/rectangle/Inflate.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/Inflate.js#L9)  
> Since: 3.0.0

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
| rectA | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | No | The first Rectangle to get the intersection from. |
| --- | --- | --- | --- |
| rectB | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | No | The second Rectangle to get the intersection from. |
| out | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | Yes | A Rectangle to store the intersection results in. |

**Returns:** [Phaser.Geom.Rectangle](../class/geom-rectangle.md) - The intersection result. If the width and height are zero, no intersection occurred.

> Source: [src/geom/rectangle/Intersection.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/Intersection.js#L10)  
> Since: 3.11.0

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
| rect | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | No | The Rectangle to get the perimeter points from. |
| --- | --- | --- | --- |
| step | number | Yes | The distance between each point of the perimeter. Set to `null` if you wish to use the `quantity` parameter instead. |
| quantity | number | Yes | The total number of points to return. The step is then calculated based on the length of the Rectangle, divided by this value. |
| out | array | Array.<[Phaser.Geom.Point](../class/geom-point.md)> | Yes | An array in which the perimeter points will be stored. If not given, a new array instance is created. |

**Returns:** array, Array.<[Phaser.Geom.Point](../class/geom-point.md)> - An array containing the perimeter points from the Rectangle.

> Source: [src/geom/rectangle/MarchingAnts.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/MarchingAnts.js#L10)  
> Since: 3.0.0

## MergePoints

### <static> MergePoints(target, points)

**Description:**

Merges a Rectangle with a list of points by repositioning and/or resizing it such that all points are located on or within its bounds.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| target | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | No | The Rectangle which should be merged. |
| --- | --- | --- | --- |
| points | Array.<[Phaser.Geom.Point](../class/geom-point.md)> | No | An array of Points (or any object with public `x` and `y` properties) which should be merged with the Rectangle. |

**Returns:** [Phaser.Geom.Rectangle](../class/geom-rectangle.md) - The modified Rectangle.

> Source: [src/geom/rectangle/MergePoints.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/MergePoints.js#L7)  
> Since: 3.0.0

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
| target | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | No | Target rectangle. Will be modified to include source rectangle. |
| --- | --- | --- | --- |
| source | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | No | Rectangle that will be merged into target rectangle. |

**Returns:** [Phaser.Geom.Rectangle](../class/geom-rectangle.md) - Modified target rectangle that contains source rectangle.

> Source: [src/geom/rectangle/MergeRect.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/MergeRect.js#L7)  
> Since: 3.0.0

## MergeXY

### <static> MergeXY(target, x, y)

**Description:**

Merges a Rectangle with a point by repositioning and/or resizing it so that the point is on or within its bounds.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| target | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | No | The Rectangle which should be merged and modified. |
| --- | --- | --- | --- |
| x | number | No | The X coordinate of the point which should be merged. |
| y | number | No | The Y coordinate of the point which should be merged. |

**Returns:** [Phaser.Geom.Rectangle](../class/geom-rectangle.md) - The modified `target` Rectangle.

> Source: [src/geom/rectangle/MergeXY.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/MergeXY.js#L7)  
> Since: 3.0.0

## Offset

### <static> Offset(rect, x, y)

**Description:**

Nudges (translates) the top left corner of a Rectangle by a given offset.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| rect | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | No | The Rectangle to adjust. |
| --- | --- | --- | --- |
| x | number | No | The distance to move the Rectangle horizontally. |
| y | number | No | The distance to move the Rectangle vertically. |

**Returns:** [Phaser.Geom.Rectangle](../class/geom-rectangle.md) - The adjusted Rectangle.

> Source: [src/geom/rectangle/Offset.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/Offset.js#L7)  
> Since: 3.0.0

## OffsetPoint

### <static> OffsetPoint(rect, point)

**Description:**

Nudges (translates) the top-left corner of a Rectangle by the coordinates of a point (translation vector).

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| rect | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | No | The Rectangle to adjust. |
| --- | --- | --- | --- |
| point | [Phaser.Geom.Point](../class/geom-point.md) | [Phaser.Math.Vector2](../class/math-vector2.md) | No | The point whose coordinates should be used as an offset. |

**Returns:** [Phaser.Geom.Rectangle](../class/geom-rectangle.md) - The adjusted Rectangle.

> Source: [src/geom/rectangle/OffsetPoint.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/OffsetPoint.js#L7)  
> Since: 3.0.0

## Overlaps

### <static> Overlaps(rectA, rectB)

**Description:**

Checks if two Rectangles overlap. If a Rectangle is within another Rectangle, the two will be considered overlapping. Thus, the Rectangles are treated as "solid".

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| rectA | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | No | The first Rectangle to check. |
| --- | --- | --- | --- |
| rectB | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | No | The second Rectangle to check. |

**Returns:** boolean - `true` if the two Rectangles overlap, `false` otherwise.

> Source: [src/geom/rectangle/Overlaps.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/Overlaps.js#L7)  
> Since: 3.0.0

## Perimeter

### <static> Perimeter(rect)

**Description:**

Calculates the perimeter of a Rectangle.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| rect | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | No | The Rectangle to use. |
| --- | --- | --- | --- |

**Returns:** number - The perimeter of the Rectangle, equal to `(width * 2) + (height * 2)`.

> Source: [src/geom/rectangle/Perimeter.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/Perimeter.js#L7)  
> Since: 3.0.0

## PerimeterPoint

### <static> PerimeterPoint(rectangle, angle, [out])

**Description:**

Returns a Point from the perimeter of a Rectangle based on the given angle.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| rectangle | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | No | The Rectangle to get the perimeter point from. |
| --- | --- | --- | --- |
| angle | number | No | The angle of the point, in degrees. |
| out | [Phaser.Geom.Point](../class/geom-point.md) | Yes | The Point object to store the position in. If not given, a new Point instance is created. |

**Returns:** [Phaser.Geom.Point](../class/geom-point.md) - A Point object holding the coordinates of the Rectangle perimeter.

> Source: [src/geom/rectangle/PerimeterPoint.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/PerimeterPoint.js#L10)  
> Since: 3.0.0

## Random

### <static> Random(rect, out)

**Description:**

Returns a random point within a Rectangle.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| rect | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | No | The Rectangle to return a point from. |
| --- | --- | --- | --- |
| out | [Phaser.Geom.Point](../class/geom-point.md) | No | The object to update with the point's coordinates. |

**Returns:** [Phaser.Geom.Point](../class/geom-point.md) - The modified `out` object, or a new Point if none was provided.

> Source: [src/geom/rectangle/Random.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/Random.js#L9)  
> Since: 3.0.0

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
| outer | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | No | The outer Rectangle to get the random point within. |
| --- | --- | --- | --- |
| inner | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | No | The inner Rectangle to exclude from the returned point. |
| out | [Phaser.Geom.Point](../class/geom-point.md) | Yes | A Point, or Point-like object to store the result in. If not specified, a new Point will be created. |

**Returns:** [Phaser.Geom.Point](../class/geom-point.md) - A Point object containing the random values in its `x` and `y` properties.

> Source: [src/geom/rectangle/RandomOutside.js#L11](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/RandomOutside.js#L11)  
> Since: 3.10.0

## SameDimensions

### <static> SameDimensions(rect, toCompare)

**Description:**

Determines if the two objects (either Rectangles or Rectangle-like) have the same width and height values under strict equality.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| rect | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | No | The first Rectangle object. |
| --- | --- | --- | --- |
| toCompare | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | No | The second Rectangle object. |

**Returns:** boolean - `true` if the objects have equivalent values for the `width` and `height` properties, otherwise `false`.

> Source: [src/geom/rectangle/SameDimensions.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/SameDimensions.js#L7)  
> Since: 3.15.0

## Scale

### <static> Scale(rect, x, y)

**Description:**

Scales the width and height of this Rectangle by the given amounts.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| rect | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | No | The `Rectangle` object that will be scaled by the specified amount(s). |
| --- | --- | --- | --- |
| x | number | No | The factor by which to scale the rectangle horizontally. |
| y | number | No | The amount by which to scale the rectangle vertically. If this is not specified, the rectangle will be scaled by the factor `x` in both directions. |

**Returns:** [Phaser.Geom.Rectangle](../class/geom-rectangle.md) - The rectangle object with updated `width` and `height` properties as calculated from the scaling factor(s).

> Source: [src/geom/rectangle/Scale.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/Scale.js#L7)  
> Since: 3.0.0

## Union

### <static> Union(rectA, rectB, [out])

**Description:**

Creates a new Rectangle or repositions and/or resizes an existing Rectangle so that it encompasses the two given Rectangles, i.e. calculates their union.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| rectA | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | No | The first Rectangle to use. |
| --- | --- | --- | --- |
| rectB | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | No | The second Rectangle to use. |
| out | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | Yes | The Rectangle to store the union in. |

**Returns:** [Phaser.Geom.Rectangle](../class/geom-rectangle.md) - The modified `out` Rectangle, or a new Rectangle if none was provided.

> Source: [src/geom/rectangle/Union.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/rectangle/Union.js#L9)  
> Since: 3.0.0

# Phaser.Geom.Triangle

## Area

### <static> Area(triangle)

**Description:**

Returns the area of a Triangle.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| triangle | [Phaser.Geom.Triangle](../class/geom-triangle.md) | No | The Triangle to use. |
| --- | --- | --- | --- |

**Returns:** number - The area of the Triangle, always non-negative.

> Source: [src/geom/triangle/Area.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/triangle/Area.js#L9)  
> Since: 3.0.0

## BuildEquilateral

### <static> BuildEquilateral(x, y, length)

**Description:**

Builds an equilateral triangle. In the equilateral triangle, all the sides are the same length (congruent) and all the angles are the same size (congruent).

The x/y specifies the top-middle of the triangle (x1/y1) and length is the length of each side.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | x coordinate of the top point of the triangle. |
| --- | --- | --- | --- |
| y | number | No | y coordinate of the top point of the triangle. |
| length | number | No | Length of each side of the triangle. |

**Returns:** [Phaser.Geom.Triangle](../class/geom-triangle.md) - The Triangle object of the given size.

> Source: [src/geom/triangle/BuildEquilateral.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/triangle/BuildEquilateral.js#L9)  
> Since: 3.0.0

## BuildFromPolygon

### <static> BuildFromPolygon(data, [holes], [scaleX], [scaleY], [out])

**Description:**

Takes an array of vertex coordinates, and optionally an array of hole indices, then returns an array

of Triangle instances, where the given vertices have been decomposed into a series of triangles.

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| data | array | No |  | A flat array of vertex coordinates like [x0,y0, x1,y1, x2,y2, ...] |
| --- | --- | --- | --- | --- |
| holes | array | Yes | null | An array of hole indices if any (e.g. [5, 8] for a 12-vertex input would mean one hole with vertices 5–7 and another with 8–11). |
| scaleX | number | Yes | 1 | Horizontal scale factor to multiply the resulting points by. |
| scaleY | number | Yes | 1 | Vertical scale factor to multiply the resulting points by. |
| out | array | Array.<[Phaser.Geom.Triangle](../class/geom-triangle.md)> | Yes |  | An array to store the resulting Triangle instances in. If not provided, a new array is created. |

**Returns:** array, Array.<[Phaser.Geom.Triangle](../class/geom-triangle.md)> - An array of Triangle instances, where each triangle is based on the decomposed vertices data.

> Source: [src/geom/triangle/BuildFromPolygon.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/triangle/BuildFromPolygon.js#L10)  
> Since: 3.0.0

## BuildRight

### <static> BuildRight(x, y, width, height)

**Description:**

Builds a right triangle, i.e. one which has a 90-degree angle and two acute angles.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The X coordinate of the right angle, which will also be the first X coordinate of the constructed Triangle. |
| --- | --- | --- | --- |
| y | number | No | The Y coordinate of the right angle, which will also be the first Y coordinate of the constructed Triangle. |
| width | number | No | The length of the side which is to the left or to the right of the right angle. |
| height | number | No | The length of the side which is above or below the right angle. |

**Returns:** [Phaser.Geom.Triangle](../class/geom-triangle.md) - The constructed right Triangle.

> Source: [src/geom/triangle/BuildRight.js#L13](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/triangle/BuildRight.js#L13)  
> Since: 3.0.0

## CenterOn

### <static> CenterOn(triangle, x, y, [centerFunc])

**Description:**

Positions the Triangle so that it is centered on the given coordinates.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| triangle | [Phaser.Geom.Triangle](../class/geom-triangle.md) | No | The triangle to be positioned. |
| --- | --- | --- | --- |
| x | number | No | The horizontal coordinate to center on. |
| y | number | No | The vertical coordinate to center on. |
| centerFunc | CenterFunction | Yes | The function used to center the triangle. Defaults to Centroid centering. |

**Returns:** [Phaser.Geom.Triangle](../class/geom-triangle.md) - The Triangle that was centered.

> Source: [src/geom/triangle/CenterOn.js#L18](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/triangle/CenterOn.js#L18)  
> Since: 3.0.0

## Centroid

### <static> Centroid(triangle, [out])

**Description:**

Calculates the position of a Triangle's centroid, which is also its center of mass (center of gravity).

The centroid is the point in a Triangle at which its three medians (the lines drawn from the vertices to the bisectors of the opposite sides) meet. It divides each one in a 2:1 ratio.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| triangle | [Phaser.Geom.Triangle](../class/geom-triangle.md) | No | The Triangle to use. |
| --- | --- | --- | --- |
| out | [Phaser.Geom.Point](../class/geom-point.md) | object | Yes | An object to store the coordinates in. |

**Returns:** [Phaser.Geom.Point](../class/geom-point.md), object - The `out` object with modified `x` and `y` properties, or a new Point if none was provided.

> Source: [src/geom/triangle/Centroid.js#L13](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/triangle/Centroid.js#L13)  
> Since: 3.0.0

## CircumCenter

### <static> CircumCenter(triangle, [out])

**Description:**

Computes the circumcentre of a triangle. The circumcentre is the centre of

the circumcircle, the smallest circle which encloses the triangle. It is also

the common intersection point of the perpendicular bisectors of the sides of

the triangle, and is the only point which has equal distance to all three

vertices of the triangle.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| triangle | [Phaser.Geom.Triangle](../class/geom-triangle.md) | No | The Triangle to get the circumcenter of. |
| --- | --- | --- | --- |
| out | [Phaser.Math.Vector2](../class/math-vector2.md) | Yes | The Vector2 object to store the position in. If not given, a new Vector2 instance is created. |

**Returns:** [Phaser.Math.Vector2](../class/math-vector2.md) - A Vector2 object holding the coordinates of the circumcenter of the Triangle.

> Source: [src/geom/triangle/CircumCenter.js#L30](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/triangle/CircumCenter.js#L30)  
> Since: 3.0.0

## CircumCircle

### <static> CircumCircle(triangle, [out])

**Description:**

Finds the circumscribed circle (circumcircle) of a Triangle object. The circumcircle is the circle which touches all of the triangle's vertices.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| triangle | [Phaser.Geom.Triangle](../class/geom-triangle.md) | No | The Triangle to use as input. |
| --- | --- | --- | --- |
| out | [Phaser.Geom.Circle](../class/geom-circle.md) | Yes | An optional Circle to store the result in. |

**Returns:** [Phaser.Geom.Circle](../class/geom-circle.md) - The updated `out` Circle, or a new Circle if none was provided.

> Source: [src/geom/triangle/CircumCircle.js#L11](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/triangle/CircumCircle.js#L11)  
> Since: 3.0.0

## Clone

### <static> Clone(source)

**Description:**

Clones a Triangle object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| source | [Phaser.Geom.Triangle](../class/geom-triangle.md) | No | The Triangle to clone. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Geom.Triangle](../class/geom-triangle.md) - A new Triangle identical to the given one but separate from it.

> Source: [src/geom/triangle/Clone.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/triangle/Clone.js#L9)  
> Since: 3.0.0

## Contains

### <static> Contains(triangle, x, y)

**Description:**

Checks if a point (as a pair of coordinates) is inside a Triangle's bounds.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| triangle | [Phaser.Geom.Triangle](../class/geom-triangle.md) | No | The Triangle to check. |
| --- | --- | --- | --- |
| x | number | No | The X coordinate of the point to check. |
| y | number | No | The Y coordinate of the point to check. |

**Returns:** boolean - `true` if the point is inside the Triangle, otherwise `false`.

> Source: [src/geom/triangle/Contains.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/triangle/Contains.js#L9)  
> Since: 3.0.0

## ContainsArray

### <static> ContainsArray(triangle, points, [returnFirst], [out])

**Description:**

Filters an array of point-like objects to only those contained within a triangle.

If `returnFirst` is true, will return an array containing only the first point in the provided array that is within the triangle (or an empty array if there are no such points).

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| triangle | [Phaser.Geom.Triangle](../class/geom-triangle.md) | No |  | The triangle that the points are being checked in. |
| --- | --- | --- | --- | --- |
| points | Array.<[Phaser.Geom.Point](../class/geom-point.md)> | No |  | An array of point-like objects (objects that have an `x` and `y` property) |
| returnFirst | boolean | Yes | false | If `true`, return an array containing only the first point found that is within the triangle. |
| out | array | Yes |  | If provided, the points that are within the triangle will be appended to this array instead of being added to a new array. If `returnFirst` is true, only the first point found within the triangle will be appended. This array will also be returned by this function. |

**Returns:** Array.<[Phaser.Geom.Point](../class/geom-point.md)> - An array containing all the points from `points` that are within the triangle, if an array was provided as `out`, points will be appended to that array and it will also be returned here.

> Source: [src/geom/triangle/ContainsArray.js#L13](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/triangle/ContainsArray.js#L13)  
> Since: 3.0.0

## ContainsPoint

### <static> ContainsPoint(triangle, point)

**Description:**

Tests if a triangle contains a point.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| triangle | [Phaser.Geom.Triangle](../class/geom-triangle.md) | No | The triangle. |
| --- | --- | --- | --- |
| point | [Phaser.Geom.Point](../class/geom-point.md) | [Phaser.Math.Vector2](../class/math-vector2.md) | any | No |

**Returns:** boolean - `true` if the point is within the triangle, otherwise `false`.

> Source: [src/geom/triangle/ContainsPoint.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/triangle/ContainsPoint.js#L9)  
> Since: 3.0.0

## CopyFrom

### <static> CopyFrom(source, dest)

**Description:**

Copy the values of one Triangle to a destination Triangle.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| source | [Phaser.Geom.Triangle](../class/geom-triangle.md) | No | The source Triangle to copy the values from. |
| --- | --- | --- | --- |
| dest | [Phaser.Geom.Triangle](../class/geom-triangle.md) | No | The destination Triangle to copy the values to. |

**Returns:** [Phaser.Geom.Triangle](../class/geom-triangle.md) - The destination Triangle.

> Source: [src/geom/triangle/CopyFrom.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/triangle/CopyFrom.js#L7)  
> Since: 3.0.0

## Decompose

### <static> Decompose(triangle, [out])

**Description:**

Decomposes a Triangle into an array of its points.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| triangle | [Phaser.Geom.Triangle](../class/geom-triangle.md) | No | The Triangle to decompose. |
| --- | --- | --- | --- |
| out | array | Yes | An array to store the points into. |

**Returns:** array - The provided `out` array, or a new array if none was provided, with three objects with `x` and `y` properties representing each point of the Triangle appended to it.

> Source: [src/geom/triangle/Decompose.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/triangle/Decompose.js#L7)  
> Since: 3.0.0

## Equals

### <static> Equals(triangle, toCompare)

**Description:**

Returns true if two triangles have the same coordinates.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| triangle | [Phaser.Geom.Triangle](../class/geom-triangle.md) | No | The first triangle to check. |
| --- | --- | --- | --- |
| toCompare | [Phaser.Geom.Triangle](../class/geom-triangle.md) | No | The second triangle to check. |

**Returns:** boolean - `true` if the two given triangles have the exact same coordinates, otherwise `false`.

> Source: [src/geom/triangle/Equals.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/triangle/Equals.js#L7)  
> Since: 3.0.0

## GetPoint

### <static> GetPoint(triangle, position, [out])

**Description:**

Returns a Point from around the perimeter of a Triangle.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| triangle | [Phaser.Geom.Triangle](../class/geom-triangle.md) | No | The Triangle to get the point on its perimeter from. |
| --- | --- | --- | --- |
| position | number | No | The position along the perimeter of the triangle. A value between 0 and 1. |
| out | [Phaser.Geom.Point](../class/geom-point.md) | object | Yes | An option Point, or Point-like object to store the value in. If not given a new Point will be created. |

**Returns:** [Phaser.Geom.Point](../class/geom-point.md), object - A Point object containing the given position from the perimeter of the triangle.

> Source: [src/geom/triangle/GetPoint.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/triangle/GetPoint.js#L10)  
> Since: 3.0.0

## GetPoints

### <static> GetPoints(triangle, quantity, stepRate, [out])

**Description:**

Returns an array of evenly spaced points on the perimeter of a Triangle.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| triangle | [Phaser.Geom.Triangle](../class/geom-triangle.md) | No | The Triangle to get the points from. |
| --- | --- | --- | --- |
| quantity | number | No | The number of evenly spaced points to return. Set to 0 to return an arbitrary number of points based on the `stepRate`. |
| stepRate | number | No | If `quantity` is 0, the distance between each returned point. |
| out | array | Array.<[Phaser.Geom.Point](../class/geom-point.md)> | Yes | An array to which the points should be appended. |

**Returns:** array, Array.<[Phaser.Geom.Point](../class/geom-point.md)> - The modified `out` array, or a new array if none was provided.

> Source: [src/geom/triangle/GetPoints.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/triangle/GetPoints.js#L10)  
> Since: 3.0.0

## InCenter

### <static> InCenter(triangle, [out])

**Description:**

Calculates the position of the incenter of a Triangle object. This is the point where its three angle bisectors meet and it's also the center of the incircle, which is the circle inscribed in the triangle.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| triangle | [Phaser.Geom.Triangle](../class/geom-triangle.md) | No | The Triangle to find the incenter of. |
| --- | --- | --- | --- |
| out | [Phaser.Geom.Point](../class/geom-point.md) | Yes | An optional Point in which to store the coordinates. |

**Returns:** [Phaser.Geom.Point](../class/geom-point.md) - Point (x, y) of the center pixel of the triangle.

> Source: [src/geom/triangle/InCenter.js#L21](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/triangle/InCenter.js#L21)  
> Since: 3.0.0

## Offset

### <static> Offset(triangle, x, y)

**Description:**

Moves each point (vertex) of a Triangle by a given offset, thus moving the entire Triangle by that offset.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| triangle | [Phaser.Geom.Triangle](../class/geom-triangle.md) | No | The Triangle to move. |
| --- | --- | --- | --- |
| x | number | No | The horizontal offset (distance) by which to move each point. Can be positive or negative. |
| y | number | No | The vertical offset (distance) by which to move each point. Can be positive or negative. |

**Returns:** [Phaser.Geom.Triangle](../class/geom-triangle.md) - The modified Triangle.

> Source: [src/geom/triangle/Offset.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/triangle/Offset.js#L7)  
> Since: 3.0.0

## Perimeter

### <static> Perimeter(triangle)

**Description:**

Gets the length of the perimeter of the given triangle.

Calculated by adding together the length of each of the three sides.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| triangle | [Phaser.Geom.Triangle](../class/geom-triangle.md) | No | The Triangle to get the length from. |
| --- | --- | --- | --- |

**Returns:** number - The length of the Triangle.

> Source: [src/geom/triangle/Perimeter.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/triangle/Perimeter.js#L9)  
> Since: 3.0.0

## Random

### <static> Random(triangle, [out])

**Description:**

Returns a random Point from within the area of the given Triangle.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| triangle | [Phaser.Geom.Triangle](../class/geom-triangle.md) | No | The Triangle to get a random point from. |
| --- | --- | --- | --- |
| out | [Phaser.Geom.Point](../class/geom-point.md) | Yes | The Point object to store the position in. If not given, a new Point instance is created. |

**Returns:** [Phaser.Geom.Point](../class/geom-point.md) - A Point object holding the coordinates of a random position within the Triangle.

> Source: [src/geom/triangle/Random.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/triangle/Random.js#L9)  
> Since: 3.0.0

## Rotate

### <static> Rotate(triangle, angle)

**Description:**

Rotates a Triangle about its incenter, which is the point at which its three angle bisectors meet.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| triangle | [Phaser.Geom.Triangle](../class/geom-triangle.md) | No | The Triangle to rotate. |
| --- | --- | --- | --- |
| angle | number | No | The angle by which to rotate the Triangle, in radians. |

**Returns:** [Phaser.Geom.Triangle](../class/geom-triangle.md) - The rotated Triangle.

> Source: [src/geom/triangle/Rotate.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/triangle/Rotate.js#L10)  
> Since: 3.0.0

## RotateAroundPoint

### <static> RotateAroundPoint(triangle, point, angle)

**Description:**

Rotates a Triangle at a certain angle about a given Point or object with public `x` and `y` properties.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| triangle | [Phaser.Geom.Triangle](../class/geom-triangle.md) | No | The Triangle to rotate. |
| --- | --- | --- | --- |
| point | [Phaser.Geom.Point](../class/geom-point.md) | No | The Point to rotate the Triangle about. |
| angle | number | No | The angle by which to rotate the Triangle, in radians. |

**Returns:** [Phaser.Geom.Triangle](../class/geom-triangle.md) - The rotated Triangle.

> Source: [src/geom/triangle/RotateAroundPoint.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/triangle/RotateAroundPoint.js#L9)  
> Since: 3.0.0

## RotateAroundXY

### <static> RotateAroundXY(triangle, x, y, angle)

**Description:**

Rotates an entire Triangle at a given angle about a specific point.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| triangle | [Phaser.Geom.Triangle](../class/geom-triangle.md) | No | The Triangle to rotate. |
| --- | --- | --- | --- |
| x | number | No | The X coordinate of the point to rotate the Triangle about. |
| y | number | No | The Y coordinate of the point to rotate the Triangle about. |
| angle | number | No | The angle by which to rotate the Triangle, in radians. |

**Returns:** [Phaser.Geom.Triangle](../class/geom-triangle.md) - The rotated Triangle.

> Source: [src/geom/triangle/RotateAroundXY.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/triangle/RotateAroundXY.js#L7)  
> Since: 3.0.0

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Phaser.Geom.Circle](#phasergeomcircle)

  + [Area](#area)

    - [<static> Area(circle)](#static-areacircle)
  + [Circumference](#circumference)

    - [<static> Circumference(circle)](#static-circumferencecircle)
  + [CircumferencePoint](#circumferencepoint)

    - [<static> CircumferencePoint(circle, angle, [out])](#static-circumferencepointcircle-angle-out)
  + [Clone](#clone)

    - [<static> Clone(source)](#static-clonesource)
  + [Contains](#contains)

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
  + [GetPoint](#getpoint)

    - [<static> GetPoint(circle, position, [out])](#static-getpointcircle-position-out)
  + [GetPoints](#getpoints)

    - [<static> GetPoints(circle, quantity, [stepRate], [output])](#static-getpointscircle-quantity-steprate-output)
  + [Offset](#offset)

    - [<static> Offset(circle, x, y)](#static-offsetcircle-x-y)
  + [OffsetPoint](#offsetpoint)

    - [<static> OffsetPoint(circle, point)](#static-offsetpointcircle-point)
  + [Random](#random)

    - [<static> Random(circle, [out])](#static-randomcircle-out)
* [Phaser.Geom.Ellipse](#phasergeomellipse)

  + [Area](#area-1)

    - [<static> Area(ellipse)](#static-areaellipse)
  + [Circumference](#circumference-1)

    - [<static> Circumference(ellipse)](#static-circumferenceellipse)
  + [CircumferencePoint](#circumferencepoint-1)

    - [<static> CircumferencePoint(ellipse, angle, [out])](#static-circumferencepointellipse-angle-out)
  + [Clone](#clone-1)

    - [<static> Clone(source)](#static-clonesource-1)
  + [Contains](#contains-1)

    - [<static> Contains(ellipse, x, y)](#static-containsellipse-x-y)
  + [ContainsPoint](#containspoint-1)

    - [<static> ContainsPoint(ellipse, point)](#static-containspointellipse-point)
  + [ContainsRect](#containsrect-1)

    - [<static> ContainsRect(ellipse, rect)](#static-containsrectellipse-rect)
  + [CopyFrom](#copyfrom-1)

    - [<static> CopyFrom(source, dest)](#static-copyfromsource-dest-1)
  + [Equals](#equals-1)

    - [<static> Equals(ellipse, toCompare)](#static-equalsellipse-tocompare)
  + [GetBounds](#getbounds-1)

    - [<static> GetBounds(ellipse, [out])](#static-getboundsellipse-out)
  + [GetPoint](#getpoint-1)

    - [<static> GetPoint(ellipse, position, [out])](#static-getpointellipse-position-out)
  + [GetPoints](#getpoints-1)

    - [<static> GetPoints(ellipse, quantity, [stepRate], [out])](#static-getpointsellipse-quantity-steprate-out)
  + [Offset](#offset-1)

    - [<static> Offset(ellipse, x, y)](#static-offsetellipse-x-y)
  + [OffsetPoint](#offsetpoint-1)

    - [<static> OffsetPoint(ellipse, point)](#static-offsetpointellipse-point)
  + [Random](#random-1)

    - [<static> Random(ellipse, [out])](#static-randomellipse-out)
* [Phaser.Geom.Intersects](#phasergeomintersects)

  + [CircleToCircle](#circletocircle)

    - [<static> CircleToCircle(circleA, circleB)](#static-circletocirclecirclea-circleb)
  + [CircleToRectangle](#circletorectangle)

    - [<static> CircleToRectangle(circle, rect)](#static-circletorectanglecircle-rect)
  + [GetCircleToCircle](#getcircletocircle)

    - [<static> GetCircleToCircle(circleA, circleB, [out])](#static-getcircletocirclecirclea-circleb-out)
  + [GetCircleToRectangle](#getcircletorectangle)

    - [<static> GetCircleToRectangle(circle, rect, [out])](#static-getcircletorectanglecircle-rect-out)
  + [GetLineToCircle](#getlinetocircle)

    - [<static> GetLineToCircle(line, circle, [out])](#static-getlinetocircleline-circle-out)
  + [GetLineToLine](#getlinetoline)

    - [<static> GetLineToLine(line1, line2, [isRay], [out])](#static-getlinetolineline1-line2-isray-out)
  + [GetLineToPoints](#getlinetopoints)

    - [<static> GetLineToPoints(line, points, [isRay], [out])](#static-getlinetopointsline-points-isray-out)
  + [GetLineToPolygon](#getlinetopolygon)

    - [<static> GetLineToPolygon(line, polygons, [isRay], [out])](#static-getlinetopolygonline-polygons-isray-out)
  + [GetLineToRectangle](#getlinetorectangle)

    - [<static> GetLineToRectangle(line, rect, [out])](#static-getlinetorectangleline-rect-out)
  + [GetRaysFromPointToPolygon](#getraysfrompointtopolygon)

    - [<static> GetRaysFromPointToPolygon(x, y, polygons)](#static-getraysfrompointtopolygonx-y-polygons)
  + [GetRectangleIntersection](#getrectangleintersection)

    - [<static> GetRectangleIntersection(rectA, rectB, [output])](#static-getrectangleintersectionrecta-rectb-output)
  + [GetRectangleToRectangle](#getrectangletorectangle)

    - [<static> GetRectangleToRectangle(rectA, rectB, [out])](#static-getrectangletorectanglerecta-rectb-out)
  + [GetRectangleToTriangle](#getrectangletotriangle)

    - [<static> GetRectangleToTriangle(rect, triangle, [out])](#static-getrectangletotrianglerect-triangle-out)
  + [GetTriangleToCircle](#gettriangletocircle)

    - [<static> GetTriangleToCircle(triangle, circle, [out])](#static-gettriangletocircletriangle-circle-out)
  + [GetTriangleToLine](#gettriangletoline)

    - [<static> GetTriangleToLine(triangle, line, [out])](#static-gettriangletolinetriangle-line-out)
  + [GetTriangleToTriangle](#gettriangletotriangle)

    - [<static> GetTriangleToTriangle(triangleA, triangleB, [out])](#static-gettriangletotriangletrianglea-triangleb-out)
  + [LineToCircle](#linetocircle)

    - [<static> LineToCircle(line, circle, [nearest])](#static-linetocircleline-circle-nearest)
  + [LineToLine](#linetoline)

    - [<static> LineToLine(line1, line2, [out])](#static-linetolineline1-line2-out)
  + [LineToRectangle](#linetorectangle)

    - [<static> LineToRectangle(line, rect)](#static-linetorectangleline-rect)
  + [PointToLine](#pointtoline)

    - [<static> PointToLine(point, line, [lineThickness])](#static-pointtolinepoint-line-linethickness)
  + [PointToLineSegment](#pointtolinesegment)

    - [<static> PointToLineSegment(point, line)](#static-pointtolinesegmentpoint-line)
  + [RectangleToRectangle](#rectangletorectangle)

    - [<static> RectangleToRectangle(rectA, rectB)](#static-rectangletorectanglerecta-rectb)
  + [RectangleToTriangle](#rectangletotriangle)

    - [<static> RectangleToTriangle(rect, triangle)](#static-rectangletotrianglerect-triangle)
  + [RectangleToValues](#rectangletovalues)

    - [<static> RectangleToValues(rect, left, right, top, bottom, [tolerance])](#static-rectangletovaluesrect-left-right-top-bottom-tolerance)
  + [TriangleToCircle](#triangletocircle)

    - [<static> TriangleToCircle(triangle, circle)](#static-triangletocircletriangle-circle)
  + [TriangleToLine](#triangletoline)

    - [<static> TriangleToLine(triangle, line)](#static-triangletolinetriangle-line)
  + [TriangleToTriangle](#triangletotriangle)

    - [<static> TriangleToTriangle(triangleA, triangleB)](#static-triangletotriangletrianglea-triangleb)
* [Phaser.Geom.Line](#phasergeomline)

  + [Angle](#angle)

    - [<static> Angle(line)](#static-angleline)
  + [BresenhamPoints](#bresenhampoints)

    - [<static> BresenhamPoints(line, [stepRate], [results])](#static-bresenhampointsline-steprate-results)
  + [CenterOn](#centeron)

    - [<static> CenterOn(line, x, y)](#static-centeronline-x-y)
  + [Clone](#clone-2)

    - [<static> Clone(source)](#static-clonesource-2)
  + [CopyFrom](#copyfrom-2)

    - [<static> CopyFrom(source, dest)](#static-copyfromsource-dest-2)
  + [Equals](#equals-2)

    - [<static> Equals(line, toCompare)](#static-equalsline-tocompare)
  + [Extend](#extend)

    - [<static> Extend(line, left, [right])](#static-extendline-left-right)
  + [GetEasedPoints](#geteasedpoints)

    - [<static> GetEasedPoints(line, ease, quantity, [collinearThreshold], [easeParams])](#static-geteasedpointsline-ease-quantity-collinearthreshold-easeparams)
  + [GetMidPoint](#getmidpoint)

    - [<static> GetMidPoint(line, [out])](#static-getmidpointline-out)
  + [GetNearestPoint](#getnearestpoint)

    - [<static> GetNearestPoint(line, point, [out])](#static-getnearestpointline-point-out)
  + [GetNormal](#getnormal)

    - [<static> GetNormal(line, [out])](#static-getnormalline-out)
  + [GetPoint](#getpoint-2)

    - [<static> GetPoint(line, position, [out])](#static-getpointline-position-out)
  + [GetPoints](#getpoints-2)

    - [<static> GetPoints(line, quantity, [stepRate], [out])](#static-getpointsline-quantity-steprate-out)
  + [GetShortestDistance](#getshortestdistance)

    - [<static> GetShortestDistance(line, point)](#static-getshortestdistanceline-point)
  + [Height](#height)

    - [<static> Height(line)](#static-heightline)
  + [Length](#length)

    - [<static> Length(line)](#static-lengthline)
  + [NormalAngle](#normalangle)

    - [<static> NormalAngle(line)](#static-normalangleline)
  + [NormalX](#normalx)

    - [<static> NormalX(line)](#static-normalxline)
  + [NormalY](#normaly)

    - [<static> NormalY(line)](#static-normalyline)
  + [Offset](#offset-2)

    - [<static> Offset(line, x, y)](#static-offsetline-x-y)
  + [PerpSlope](#perpslope)

    - [<static> PerpSlope(line)](#static-perpslopeline)
  + [Random](#random-2)

    - [<static> Random(line, [out])](#static-randomline-out)
  + [ReflectAngle](#reflectangle)

    - [<static> ReflectAngle(lineA, lineB)](#static-reflectanglelinea-lineb)
  + [Rotate](#rotate)

    - [<static> Rotate(line, angle)](#static-rotateline-angle)
  + [RotateAroundPoint](#rotatearoundpoint)

    - [<static> RotateAroundPoint(line, point, angle)](#static-rotatearoundpointline-point-angle)
  + [RotateAroundXY](#rotatearoundxy)

    - [<static> RotateAroundXY(line, x, y, angle)](#static-rotatearoundxyline-x-y-angle)
  + [SetToAngle](#settoangle)

    - [<static> SetToAngle(line, x, y, angle, length)](#static-settoangleline-x-y-angle-length)
  + [Slope](#slope)

    - [<static> Slope(line)](#static-slopeline)
  + [Width](#width)

    - [<static> Width(line)](#static-widthline)
* [Phaser.Geom.Mesh](#phasergeommesh)

  + [GenerateGridVerts](#generategridverts)

    - [<static> GenerateGridVerts(config)](#static-generategridvertsconfig)
  + [GenerateObjVerts](#generateobjverts)

    - [<static> GenerateObjVerts(data, [mesh], [scale], [x], [y], [z], [rotateX], [rotateY], [rotateZ], [zIsUp])](#static-generateobjvertsdata-mesh-scale-x-y-z-rotatex-rotatey-rotatez-zisup)
  + [GenerateVerts](#generateverts)

    - [<static> GenerateVerts(vertices, uvs, [indicies], [containsZ], [normals], [colors], [alphas], [flipUV])](#static-generatevertsvertices-uvs-indicies-containsz-normals-colors-alphas-flipuv)
  + [ParseObj](#parseobj)

    - [<static> ParseObj(data, [flipUV])](#static-parseobjdata-flipuv)
  + [ParseObjMaterial](#parseobjmaterial)

    - [<static> ParseObjMaterial(mtl)](#static-parseobjmaterialmtl)
  + [RotateFace](#rotateface)

    - [<static> RotateFace(face, angle, [cx], [cy])](#static-rotatefaceface-angle-cx-cy)
* [Phaser.Geom.Point](#phasergeompoint)

  + [Ceil](#ceil)

    - [<static> Ceil(point)](#static-ceilpoint)
  + [Clone](#clone-3)

    - [<static> Clone(source)](#static-clonesource-3)
  + [CopyFrom](#copyfrom-3)

    - [<static> CopyFrom(source, dest)](#static-copyfromsource-dest-3)
  + [Equals](#equals-3)

    - [<static> Equals(point, toCompare)](#static-equalspoint-tocompare)
  + [Floor](#floor)

    - [<static> Floor(point)](#static-floorpoint)
  + [GetCentroid](#getcentroid)

    - [<static> GetCentroid(points, [out])](#static-getcentroidpoints-out)
  + [GetMagnitude](#getmagnitude)

    - [<static> GetMagnitude(point)](#static-getmagnitudepoint)
  + [GetMagnitudeSq](#getmagnitudesq)

    - [<static> GetMagnitudeSq(point)](#static-getmagnitudesqpoint)
  + [GetRectangleFromPoints](#getrectanglefrompoints)

    - [<static> GetRectangleFromPoints(points, [out])](#static-getrectanglefrompointspoints-out)
  + [Interpolate](#interpolate)

    - [<static> Interpolate(pointA, pointB, [t], [out])](#static-interpolatepointa-pointb-t-out)
  + [Invert](#invert)

    - [<static> Invert(point)](#static-invertpoint)
  + [Negative](#negative)

    - [<static> Negative(point, [out])](#static-negativepoint-out)
  + [Project](#project)

    - [<static> Project(pointA, pointB, [out])](#static-projectpointa-pointb-out)
  + [ProjectUnit](#projectunit)

    - [<static> ProjectUnit(pointA, pointB, [out])](#static-projectunitpointa-pointb-out)
  + [SetMagnitude](#setmagnitude)

    - [<static> SetMagnitude(point, magnitude)](#static-setmagnitudepoint-magnitude)
* [Phaser.Geom.Polygon](#phasergeompolygon)

  + [Clone](#clone-4)

    - [<static> Clone(polygon)](#static-clonepolygon)
  + [Contains](#contains-2)

    - [<static> Contains(polygon, x, y)](#static-containspolygon-x-y)
  + [ContainsPoint](#containspoint-2)

    - [<static> ContainsPoint(polygon, point)](#static-containspointpolygon-point)
  + [Earcut](#earcut)

    - [<static> Earcut(data, [holeIndices], [dimensions])](#static-earcutdata-holeindices-dimensions)
  + [GetAABB](#getaabb)

    - [<static> GetAABB(polygon, [out])](#static-getaabbpolygon-out)
  + [GetNumberArray](#getnumberarray)

    - [<static> GetNumberArray(polygon, [output])](#static-getnumberarraypolygon-output)
  + [GetPoints](#getpoints-3)

    - [<static> GetPoints(polygon, quantity, [stepRate], [output])](#static-getpointspolygon-quantity-steprate-output)
  + [Perimeter](#perimeter)

    - [<static> Perimeter(polygon)](#static-perimeterpolygon)
  + [Reverse](#reverse)

    - [<static> Reverse(polygon)](#static-reversepolygon)
  + [Simplify](#simplify)

    - [<static> Simplify(polygon, [tolerance], [highestQuality])](#static-simplifypolygon-tolerance-highestquality)
  + [Smooth](#smooth)

    - [<static> Smooth(polygon)](#static-smoothpolygon)
  + [Translate](#translate)

    - [<static> Translate(polygon, x, y)](#static-translatepolygon-x-y)
* [Phaser.Geom.Rectangle](#phasergeomrectangle)

  + [Area](#area-2)

    - [<static> Area(rect)](#static-arearect)
  + [Ceil](#ceil-1)

    - [<static> Ceil(rect)](#static-ceilrect)
  + [CeilAll](#ceilall)

    - [<static> CeilAll(rect)](#static-ceilallrect)
  + [CenterOn](#centeron-1)

    - [<static> CenterOn(rect, x, y)](#static-centeronrect-x-y)
  + [Clone](#clone-5)

    - [<static> Clone(source)](#static-clonesource-4)
  + [Contains](#contains-3)

    - [<static> Contains(rect, x, y)](#static-containsrect-x-y)
  + [ContainsPoint](#containspoint-3)

    - [<static> ContainsPoint(rect, point)](#static-containspointrect-point)
  + [ContainsRect](#containsrect-2)

    - [<static> ContainsRect(rectA, rectB)](#static-containsrectrecta-rectb)
  + [CopyFrom](#copyfrom-4)

    - [<static> CopyFrom(source, dest)](#static-copyfromsource-dest-4)
  + [Decompose](#decompose)

    - [<static> Decompose(rect, [out])](#static-decomposerect-out)
  + [Equals](#equals-4)

    - [<static> Equals(rect, toCompare)](#static-equalsrect-tocompare)
  + [FitInside](#fitinside)

    - [<static> FitInside(target, source)](#static-fitinsidetarget-source)
  + [FitOutside](#fitoutside)

    - [<static> FitOutside(target, source)](#static-fitoutsidetarget-source)
  + [Floor](#floor-1)

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
  + [GetPoint](#getpoint-3)

    - [<static> GetPoint(rectangle, position, [out])](#static-getpointrectangle-position-out)
  + [GetPoints](#getpoints-4)

    - [<static> GetPoints(rectangle, step, quantity, [out])](#static-getpointsrectangle-step-quantity-out)
  + [GetSize](#getsize)

    - [<static> GetSize(rect, [out])](#static-getsizerect-out)
  + [Inflate](#inflate)

    - [<static> Inflate(rect, x, y)](#static-inflaterect-x-y)
  + [Intersection](#intersection)

    - [<static> Intersection(rectA, rectB, [out])](#static-intersectionrecta-rectb-out)
  + [MarchingAnts](#marchingants)

    - [<static> MarchingAnts(rect, [step], [quantity], [out])](#static-marchingantsrect-step-quantity-out)
  + [MergePoints](#mergepoints)

    - [<static> MergePoints(target, points)](#static-mergepointstarget-points)
  + [MergeRect](#mergerect)

    - [<static> MergeRect(target, source)](#static-mergerecttarget-source)
  + [MergeXY](#mergexy)

    - [<static> MergeXY(target, x, y)](#static-mergexytarget-x-y)
  + [Offset](#offset-3)

    - [<static> Offset(rect, x, y)](#static-offsetrect-x-y)
  + [OffsetPoint](#offsetpoint-2)

    - [<static> OffsetPoint(rect, point)](#static-offsetpointrect-point)
  + [Overlaps](#overlaps)

    - [<static> Overlaps(rectA, rectB)](#static-overlapsrecta-rectb)
  + [Perimeter](#perimeter-1)

    - [<static> Perimeter(rect)](#static-perimeterrect)
  + [PerimeterPoint](#perimeterpoint)

    - [<static> PerimeterPoint(rectangle, angle, [out])](#static-perimeterpointrectangle-angle-out)
  + [Random](#random-3)

    - [<static> Random(rect, out)](#static-randomrect-out)
  + [RandomOutside](#randomoutside)

    - [<static> RandomOutside(outer, inner, [out])](#static-randomoutsideouter-inner-out)
  + [SameDimensions](#samedimensions)

    - [<static> SameDimensions(rect, toCompare)](#static-samedimensionsrect-tocompare)
  + [Scale](#scale)

    - [<static> Scale(rect, x, y)](#static-scalerect-x-y)
  + [Union](#union)

    - [<static> Union(rectA, rectB, [out])](#static-unionrecta-rectb-out)
* [Phaser.Geom.Triangle](#phasergeomtriangle)

  + [Area](#area-3)

    - [<static> Area(triangle)](#static-areatriangle)
  + [BuildEquilateral](#buildequilateral)

    - [<static> BuildEquilateral(x, y, length)](#static-buildequilateralx-y-length)
  + [BuildFromPolygon](#buildfrompolygon)

    - [<static> BuildFromPolygon(data, [holes], [scaleX], [scaleY], [out])](#static-buildfrompolygondata-holes-scalex-scaley-out)
  + [BuildRight](#buildright)

    - [<static> BuildRight(x, y, width, height)](#static-buildrightx-y-width-height)
  + [CenterOn](#centeron-2)

    - [<static> CenterOn(triangle, x, y, [centerFunc])](#static-centerontriangle-x-y-centerfunc)
  + [Centroid](#centroid)

    - [<static> Centroid(triangle, [out])](#static-centroidtriangle-out)
  + [CircumCenter](#circumcenter)

    - [<static> CircumCenter(triangle, [out])](#static-circumcentertriangle-out)
  + [CircumCircle](#circumcircle)

    - [<static> CircumCircle(triangle, [out])](#static-circumcircletriangle-out)
  + [Clone](#clone-6)

    - [<static> Clone(source)](#static-clonesource-5)
  + [Contains](#contains-4)

    - [<static> Contains(triangle, x, y)](#static-containstriangle-x-y)
  + [ContainsArray](#containsarray)

    - [<static> ContainsArray(triangle, points, [returnFirst], [out])](#static-containsarraytriangle-points-returnfirst-out)
  + [ContainsPoint](#containspoint-4)

    - [<static> ContainsPoint(triangle, point)](#static-containspointtriangle-point)
  + [CopyFrom](#copyfrom-5)

    - [<static> CopyFrom(source, dest)](#static-copyfromsource-dest-5)
  + [Decompose](#decompose-1)

    - [<static> Decompose(triangle, [out])](#static-decomposetriangle-out)
  + [Equals](#equals-5)

    - [<static> Equals(triangle, toCompare)](#static-equalstriangle-tocompare)
  + [GetPoint](#getpoint-4)

    - [<static> GetPoint(triangle, position, [out])](#static-getpointtriangle-position-out)
  + [GetPoints](#getpoints-5)

    - [<static> GetPoints(triangle, quantity, stepRate, [out])](#static-getpointstriangle-quantity-steprate-out)
  + [InCenter](#incenter)

    - [<static> InCenter(triangle, [out])](#static-incentertriangle-out)
  + [Offset](#offset-4)

    - [<static> Offset(triangle, x, y)](#static-offsettriangle-x-y)
  + [Perimeter](#perimeter-2)

    - [<static> Perimeter(triangle)](#static-perimetertriangle)
  + [Random](#random-4)

    - [<static> Random(triangle, [out])](#static-randomtriangle-out)
  + [Rotate](#rotate-1)

    - [<static> Rotate(triangle, angle)](#static-rotatetriangle-angle)
  + [RotateAroundPoint](#rotatearoundpoint-1)

    - [<static> RotateAroundPoint(triangle, point, angle)](#static-rotatearoundpointtriangle-point-angle)
  + [RotateAroundXY](#rotatearoundxy-1)

    - [<static> RotateAroundXY(triangle, x, y, angle)](#static-rotatearoundxytriangle-x-y-angle)

Back to top

©2025[Phaser](https://docs.phaser.io)