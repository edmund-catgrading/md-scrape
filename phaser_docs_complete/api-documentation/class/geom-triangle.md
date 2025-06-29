# Triangle

Phaser.Geom.Triangle

A triangle is a plane created by connecting three points.

The first two arguments specify the first point, the middle two arguments

specify the second point, and the last two arguments specify the third point.

**Constructor**

`new Triangle([x1], [y1], [x2], [y2], [x3], [y3])`

**Parameters**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x1 | number | Yes | 0 | `x` coordinate of the first point. |
| --- | --- | --- | --- | --- |
| y1 | number | Yes | 0 | `y` coordinate of the first point. |
| x2 | number | Yes | 0 | `x` coordinate of the second point. |
| y2 | number | Yes | 0 | `y` coordinate of the second point. |
| x3 | number | Yes | 0 | `x` coordinate of the third point. |
| y3 | number | Yes | 0 | `y` coordinate of the third point. |

---

**Scope**: static

> Source: [src/geom/triangle/Triangle.js#L15](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/triangle/Triangle.js#L15)  
> Since: 3.0.0

# Public Methods

## Area

### <static> Area(triangle)

**Description:**

Returns the area of a Triangle.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| triangle | [Phaser.Geom.Triangle](geom-triangle.md) | No | The Triangle to use. |
| --- | --- | --- | --- |

**Returns:** number - The area of the Triangle, always non-negative.

> Source: [src/geom/triangle/Area.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/triangle/Area.js#L9)  
> Since: 3.0.0

---

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

**Returns:** [Phaser.Geom.Triangle](geom-triangle.md) - The Triangle object of the given size.

> Source: [src/geom/triangle/BuildEquilateral.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/triangle/BuildEquilateral.js#L9)  
> Since: 3.0.0

---

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
| out | array | Array.<[Phaser.Geom.Triangle](geom-triangle.md)> | Yes |  | An array to store the resulting Triangle instances in. If not provided, a new array is created. |

**Returns:** array, Array.<[Phaser.Geom.Triangle](geom-triangle.md)> - An array of Triangle instances, where each triangle is based on the decomposed vertices data.

> Source: [src/geom/triangle/BuildFromPolygon.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/triangle/BuildFromPolygon.js#L10)  
> Since: 3.0.0

---

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

**Returns:** [Phaser.Geom.Triangle](geom-triangle.md) - The constructed right Triangle.

> Source: [src/geom/triangle/BuildRight.js#L13](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/triangle/BuildRight.js#L13)  
> Since: 3.0.0

---

## CenterOn

### <static> CenterOn(triangle, x, y, [centerFunc])

**Description:**

Positions the Triangle so that it is centered on the given coordinates.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| triangle | [Phaser.Geom.Triangle](geom-triangle.md) | No | The triangle to be positioned. |
| --- | --- | --- | --- |
| x | number | No | The horizontal coordinate to center on. |
| y | number | No | The vertical coordinate to center on. |
| centerFunc | CenterFunction | Yes | The function used to center the triangle. Defaults to Centroid centering. |

**Returns:** [Phaser.Geom.Triangle](geom-triangle.md) - The Triangle that was centered.

> Source: [src/geom/triangle/CenterOn.js#L18](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/triangle/CenterOn.js#L18)  
> Since: 3.0.0

---

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
| triangle | [Phaser.Geom.Triangle](geom-triangle.md) | No | The Triangle to use. |
| --- | --- | --- | --- |
| out | [Phaser.Geom.Point](geom-point.md) | object | Yes | An object to store the coordinates in. |

**Returns:** [Phaser.Geom.Point](geom-point.md), object - The `out` object with modified `x` and `y` properties, or a new Point if none was provided.

> Source: [src/geom/triangle/Centroid.js#L13](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/triangle/Centroid.js#L13)  
> Since: 3.0.0

---

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
| triangle | [Phaser.Geom.Triangle](geom-triangle.md) | No | The Triangle to get the circumcenter of. |
| --- | --- | --- | --- |
| out | [Phaser.Math.Vector2](math-vector2.md) | Yes | The Vector2 object to store the position in. If not given, a new Vector2 instance is created. |

**Returns:** [Phaser.Math.Vector2](math-vector2.md) - A Vector2 object holding the coordinates of the circumcenter of the Triangle.

> Source: [src/geom/triangle/CircumCenter.js#L30](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/triangle/CircumCenter.js#L30)  
> Since: 3.0.0

---

## CircumCircle

### <static> CircumCircle(triangle, [out])

**Description:**

Finds the circumscribed circle (circumcircle) of a Triangle object. The circumcircle is the circle which touches all of the triangle's vertices.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| triangle | [Phaser.Geom.Triangle](geom-triangle.md) | No | The Triangle to use as input. |
| --- | --- | --- | --- |
| out | [Phaser.Geom.Circle](geom-circle.md) | Yes | An optional Circle to store the result in. |

**Returns:** [Phaser.Geom.Circle](geom-circle.md) - The updated `out` Circle, or a new Circle if none was provided.

> Source: [src/geom/triangle/CircumCircle.js#L11](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/triangle/CircumCircle.js#L11)  
> Since: 3.0.0

---

## Clone

### <static> Clone(source)

**Description:**

Clones a Triangle object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| source | [Phaser.Geom.Triangle](geom-triangle.md) | No | The Triangle to clone. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Geom.Triangle](geom-triangle.md) - A new Triangle identical to the given one but separate from it.

> Source: [src/geom/triangle/Clone.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/triangle/Clone.js#L9)  
> Since: 3.0.0

---

## contains

### <instance> contains(x, y)

**Description:**

Checks whether a given points lies within the triangle.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The x coordinate of the point to check. |
| --- | --- | --- | --- |
| y | number | No | The y coordinate of the point to check. |

**Returns:** boolean - `true` if the coordinate pair is within the triangle, otherwise `false`.

> Source: [src/geom/triangle/Triangle.js#L118](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/triangle/Triangle.js#L118)  
> Since: 3.0.0

---

## Contains

### <static> Contains(triangle, x, y)

**Description:**

Checks if a point (as a pair of coordinates) is inside a Triangle's bounds.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| triangle | [Phaser.Geom.Triangle](geom-triangle.md) | No | The Triangle to check. |
| --- | --- | --- | --- |
| x | number | No | The X coordinate of the point to check. |
| y | number | No | The Y coordinate of the point to check. |

**Returns:** boolean - `true` if the point is inside the Triangle, otherwise `false`.

> Source: [src/geom/triangle/Contains.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/triangle/Contains.js#L9)  
> Since: 3.0.0

---

## ContainsArray

### <static> ContainsArray(triangle, points, [returnFirst], [out])

**Description:**

Filters an array of point-like objects to only those contained within a triangle.

If `returnFirst` is true, will return an array containing only the first point in the provided array that is within the triangle (or an empty array if there are no such points).

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| triangle | [Phaser.Geom.Triangle](geom-triangle.md) | No |  | The triangle that the points are being checked in. |
| --- | --- | --- | --- | --- |
| points | Array.<[Phaser.Geom.Point](geom-point.md)> | No |  | An array of point-like objects (objects that have an `x` and `y` property) |
| returnFirst | boolean | Yes | false | If `true`, return an array containing only the first point found that is within the triangle. |
| out | array | Yes |  | If provided, the points that are within the triangle will be appended to this array instead of being added to a new array. If `returnFirst` is true, only the first point found within the triangle will be appended. This array will also be returned by this function. |

**Returns:** Array.<[Phaser.Geom.Point](geom-point.md)> - An array containing all the points from `points` that are within the triangle, if an array was provided as `out`, points will be appended to that array and it will also be returned here.

> Source: [src/geom/triangle/ContainsArray.js#L13](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/triangle/ContainsArray.js#L13)  
> Since: 3.0.0

---

## ContainsPoint

### <static> ContainsPoint(triangle, point)

**Description:**

Tests if a triangle contains a point.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| triangle | [Phaser.Geom.Triangle](geom-triangle.md) | No | The triangle. |
| --- | --- | --- | --- |
| point | [Phaser.Geom.Point](geom-point.md) | [Phaser.Math.Vector2](math-vector2.md) | any | No |

**Returns:** boolean - `true` if the point is within the triangle, otherwise `false`.

> Source: [src/geom/triangle/ContainsPoint.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/triangle/ContainsPoint.js#L9)  
> Since: 3.0.0

---

## CopyFrom

### <static> CopyFrom(source, dest)

**Description:**

Copy the values of one Triangle to a destination Triangle.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| source | [Phaser.Geom.Triangle](geom-triangle.md) | No | The source Triangle to copy the values from. |
| --- | --- | --- | --- |
| dest | [Phaser.Geom.Triangle](geom-triangle.md) | No | The destination Triangle to copy the values to. |

**Returns:** [Phaser.Geom.Triangle](geom-triangle.md) - The destination Triangle.

> Source: [src/geom/triangle/CopyFrom.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/triangle/CopyFrom.js#L7)  
> Since: 3.0.0

---

## Decompose

### <static> Decompose(triangle, [out])

**Description:**

Decomposes a Triangle into an array of its points.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| triangle | [Phaser.Geom.Triangle](geom-triangle.md) | No | The Triangle to decompose. |
| --- | --- | --- | --- |
| out | array | Yes | An array to store the points into. |

**Returns:** array - The provided `out` array, or a new array if none was provided, with three objects with `x` and `y` properties representing each point of the Triangle appended to it.

> Source: [src/geom/triangle/Decompose.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/triangle/Decompose.js#L7)  
> Since: 3.0.0

---

## Equals

### <static> Equals(triangle, toCompare)

**Description:**

Returns true if two triangles have the same coordinates.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| triangle | [Phaser.Geom.Triangle](geom-triangle.md) | No | The first triangle to check. |
| --- | --- | --- | --- |
| toCompare | [Phaser.Geom.Triangle](geom-triangle.md) | No | The second triangle to check. |

**Returns:** boolean - `true` if the two given triangles have the exact same coordinates, otherwise `false`.

> Source: [src/geom/triangle/Equals.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/triangle/Equals.js#L7)  
> Since: 3.0.0

---

## getLineA

### <instance> getLineA([line])

**Description:**

Returns a Line object that corresponds to Line A of this Triangle.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| line | [Phaser.Geom.Line](geom-line.md) | Yes | A Line object to set the results in. If `undefined` a new Line will be created. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Geom.Line](geom-line.md) - A Line object that corresponds to line A of this Triangle.

> Source: [src/geom/triangle/Triangle.js#L224](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/triangle/Triangle.js#L224)  
> Since: 3.0.0

---

## getLineB

### <instance> getLineB([line])

**Description:**

Returns a Line object that corresponds to Line B of this Triangle.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| line | [Phaser.Geom.Line](geom-line.md) | Yes | A Line object to set the results in. If `undefined` a new Line will be created. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Geom.Line](geom-line.md) - A Line object that corresponds to line B of this Triangle.

> Source: [src/geom/triangle/Triangle.js#L245](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/triangle/Triangle.js#L245)  
> Since: 3.0.0

---

## getLineC

### <instance> getLineC([line])

**Description:**

Returns a Line object that corresponds to Line C of this Triangle.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| line | [Phaser.Geom.Line](geom-line.md) | Yes | A Line object to set the results in. If `undefined` a new Line will be created. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Geom.Line](geom-line.md) - A Line object that corresponds to line C of this Triangle.

> Source: [src/geom/triangle/Triangle.js#L266](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/triangle/Triangle.js#L266)  
> Since: 3.0.0

---

## getPoint

### <instance> getPoint(position, [output])

**Description:**

Returns a specific point on the triangle.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| position | number | No | Position as float within `0` and `1`. `0` equals the first point. |
| --- | --- | --- | --- |
| output | [Phaser.Geom.Point](geom-point.md) | object | Yes | Optional Point, or point-like object, that the calculated point will be written to. |

**Returns:** [Phaser.Geom.Point](geom-point.md), object - Calculated `Point` that represents the requested position. It is the same as `output` when this parameter has been given.

> Source: [src/geom/triangle/Triangle.js#L134](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/triangle/Triangle.js#L134)  
> Since: 3.0.0

---

## GetPoint

### <static> GetPoint(triangle, position, [out])

**Description:**

Returns a Point from around the perimeter of a Triangle.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| triangle | [Phaser.Geom.Triangle](geom-triangle.md) | No | The Triangle to get the point on its perimeter from. |
| --- | --- | --- | --- |
| position | number | No | The position along the perimeter of the triangle. A value between 0 and 1. |
| out | [Phaser.Geom.Point](geom-point.md) | object | Yes | An option Point, or Point-like object to store the value in. If not given a new Point will be created. |

**Returns:** [Phaser.Geom.Point](geom-point.md), object - A Point object containing the given position from the perimeter of the triangle.

> Source: [src/geom/triangle/GetPoint.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/triangle/GetPoint.js#L10)  
> Since: 3.0.0

---

## getPoints

### <instance> getPoints(quantity, [stepRate], [output])

**Description:**

Calculates a list of evenly distributed points on the triangle. It is either possible to pass an amount of points to be generated (`quantity`) or the distance between two points (`stepRate`).

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| quantity | number | No | Number of points to be generated. Can be falsey when `stepRate` should be used. All points have the same distance along the triangle. |
| --- | --- | --- | --- |
| stepRate | number | Yes | Distance between two points. Will only be used when `quantity` is falsey. |
| output | array | Array.<[Phaser.Geom.Point](geom-point.md)> | Yes | Optional Array for writing the calculated points into. Otherwise a new array will be created. |

**Returns:** array, Array.<[Phaser.Geom.Point](geom-point.md)> - Returns a list of calculated `Point` instances or the filled array passed as parameter `output`.

> Source: [src/geom/triangle/Triangle.js#L152](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/triangle/Triangle.js#L152)  
> Since: 3.0.0

---

## GetPoints

### <static> GetPoints(triangle, quantity, stepRate, [out])

**Description:**

Returns an array of evenly spaced points on the perimeter of a Triangle.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| triangle | [Phaser.Geom.Triangle](geom-triangle.md) | No | The Triangle to get the points from. |
| --- | --- | --- | --- |
| quantity | number | No | The number of evenly spaced points to return. Set to 0 to return an arbitrary number of points based on the `stepRate`. |
| stepRate | number | No | If `quantity` is 0, the distance between each returned point. |
| out | array | Array.<[Phaser.Geom.Point](geom-point.md)> | Yes | An array to which the points should be appended. |

**Returns:** array, Array.<[Phaser.Geom.Point](geom-point.md)> - The modified `out` array, or a new array if none was provided.

> Source: [src/geom/triangle/GetPoints.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/triangle/GetPoints.js#L10)  
> Since: 3.0.0

---

## getRandomPoint

### <instance> getRandomPoint([point])

**Description:**

Returns a random point along the triangle.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| point | [Phaser.Geom.Point](geom-point.md) | Yes | Optional `Point` that should be modified. Otherwise a new one will be created. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Geom.Point](geom-point.md) - Random `Point`. When parameter `point` has been provided it will be returned.

> Source: [src/geom/triangle/Triangle.js#L171](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/triangle/Triangle.js#L171)  
> Since: 3.0.0

---

## InCenter

### <static> InCenter(triangle, [out])

**Description:**

Calculates the position of the incenter of a Triangle object. This is the point where its three angle bisectors meet and it's also the center of the incircle, which is the circle inscribed in the triangle.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| triangle | [Phaser.Geom.Triangle](geom-triangle.md) | No | The Triangle to find the incenter of. |
| --- | --- | --- | --- |
| out | [Phaser.Geom.Point](geom-point.md) | Yes | An optional Point in which to store the coordinates. |

**Returns:** [Phaser.Geom.Point](geom-point.md) - Point (x, y) of the center pixel of the triangle.

> Source: [src/geom/triangle/InCenter.js#L21](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/triangle/InCenter.js#L21)  
> Since: 3.0.0

---

## Offset

### <static> Offset(triangle, x, y)

**Description:**

Moves each point (vertex) of a Triangle by a given offset, thus moving the entire Triangle by that offset.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| triangle | [Phaser.Geom.Triangle](geom-triangle.md) | No | The Triangle to move. |
| --- | --- | --- | --- |
| x | number | No | The horizontal offset (distance) by which to move each point. Can be positive or negative. |
| y | number | No | The vertical offset (distance) by which to move each point. Can be positive or negative. |

**Returns:** [Phaser.Geom.Triangle](geom-triangle.md) - The modified Triangle.

> Source: [src/geom/triangle/Offset.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/triangle/Offset.js#L7)  
> Since: 3.0.0

---

## Perimeter

### <static> Perimeter(triangle)

**Description:**

Gets the length of the perimeter of the given triangle.

Calculated by adding together the length of each of the three sides.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| triangle | [Phaser.Geom.Triangle](geom-triangle.md) | No | The Triangle to get the length from. |
| --- | --- | --- | --- |

**Returns:** number - The length of the Triangle.

> Source: [src/geom/triangle/Perimeter.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/triangle/Perimeter.js#L9)  
> Since: 3.0.0

---

## Random

### <static> Random(triangle, [out])

**Description:**

Returns a random Point from within the area of the given Triangle.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| triangle | [Phaser.Geom.Triangle](geom-triangle.md) | No | The Triangle to get a random point from. |
| --- | --- | --- | --- |
| out | [Phaser.Geom.Point](geom-point.md) | Yes | The Point object to store the position in. If not given, a new Point instance is created. |

**Returns:** [Phaser.Geom.Point](geom-point.md) - A Point object holding the coordinates of a random position within the Triangle.

> Source: [src/geom/triangle/Random.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/triangle/Random.js#L9)  
> Since: 3.0.0

---

## Rotate

### <static> Rotate(triangle, angle)

**Description:**

Rotates a Triangle about its incenter, which is the point at which its three angle bisectors meet.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| triangle | [Phaser.Geom.Triangle](geom-triangle.md) | No | The Triangle to rotate. |
| --- | --- | --- | --- |
| angle | number | No | The angle by which to rotate the Triangle, in radians. |

**Returns:** [Phaser.Geom.Triangle](geom-triangle.md) - The rotated Triangle.

> Source: [src/geom/triangle/Rotate.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/triangle/Rotate.js#L10)  
> Since: 3.0.0

---

## RotateAroundPoint

### <static> RotateAroundPoint(triangle, point, angle)

**Description:**

Rotates a Triangle at a certain angle about a given Point or object with public `x` and `y` properties.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| triangle | [Phaser.Geom.Triangle](geom-triangle.md) | No | The Triangle to rotate. |
| --- | --- | --- | --- |
| point | [Phaser.Geom.Point](geom-point.md) | No | The Point to rotate the Triangle about. |
| angle | number | No | The angle by which to rotate the Triangle, in radians. |

**Returns:** [Phaser.Geom.Triangle](geom-triangle.md) - The rotated Triangle.

> Source: [src/geom/triangle/RotateAroundPoint.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/triangle/RotateAroundPoint.js#L9)  
> Since: 3.0.0

---

## RotateAroundXY

### <static> RotateAroundXY(triangle, x, y, angle)

**Description:**

Rotates an entire Triangle at a given angle about a specific point.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| triangle | [Phaser.Geom.Triangle](geom-triangle.md) | No | The Triangle to rotate. |
| --- | --- | --- | --- |
| x | number | No | The X coordinate of the point to rotate the Triangle about. |
| y | number | No | The Y coordinate of the point to rotate the Triangle about. |
| angle | number | No | The angle by which to rotate the Triangle, in radians. |

**Returns:** [Phaser.Geom.Triangle](geom-triangle.md) - The rotated Triangle.

> Source: [src/geom/triangle/RotateAroundXY.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/triangle/RotateAroundXY.js#L7)  
> Since: 3.0.0

---

## setTo

### <instance> setTo([x1], [y1], [x2], [y2], [x3], [y3])

**Description:**

Sets all three points of the triangle. Leaving out any coordinate sets it to be `0`.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x1 | number | Yes | 0 | `x` coordinate of the first point. |
| --- | --- | --- | --- | --- |
| y1 | number | Yes | 0 | `y` coordinate of the first point. |
| x2 | number | Yes | 0 | `x` coordinate of the second point. |
| y2 | number | Yes | 0 | `y` coordinate of the second point. |
| x3 | number | Yes | 0 | `x` coordinate of the third point. |
| y3 | number | Yes | 0 | `y` coordinate of the third point. |

**Returns:** [Phaser.Geom.Triangle](geom-triangle.md) - This Triangle object.

> Source: [src/geom/triangle/Triangle.js#L188](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/triangle/Triangle.js#L188)  
> Since: 3.0.0

---

# Public Members

## bottom

### bottom: number

**Description:**

Bottom most Y coordinate of the triangle. Setting it moves the triangle on the Y axis accordingly.

> Source: [src/geom/triangle/Triangle.js#L401](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/triangle/Triangle.js#L401)  
> Since: 3.0.0

---

## left

### left: number

**Description:**

Left most X coordinate of the triangle. Setting it moves the triangle on the X axis accordingly.

> Source: [src/geom/triangle/Triangle.js#L287](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/triangle/Triangle.js#L287)  
> Since: 3.0.0

---

## right

### right: number

**Description:**

Right most X coordinate of the triangle. Setting it moves the triangle on the X axis accordingly.

> Source: [src/geom/triangle/Triangle.js#L325](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/triangle/Triangle.js#L325)  
> Since: 3.0.0

---

## top

### top: number

**Description:**

Top most Y coordinate of the triangle. Setting it moves the triangle on the Y axis accordingly.

> Source: [src/geom/triangle/Triangle.js#L363](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/triangle/Triangle.js#L363)  
> Since: 3.0.0

---

## type

### type: number

**Description:**

The geometry constant type of this object: `GEOM_CONST.TRIANGLE`.

Used for fast type comparisons.

> Source: [src/geom/triangle/Triangle.js#L46](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/triangle/Triangle.js#L46)  
> Since: 3.19.0

---

## x1

### x1: number

**Description:**

`x` coordinate of the first point.

> Source: [src/geom/triangle/Triangle.js#L57](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/triangle/Triangle.js#L57)  
> Since: 3.0.0

---

## x2

### x2: number

**Description:**

`x` coordinate of the second point.

> Source: [src/geom/triangle/Triangle.js#L77](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/triangle/Triangle.js#L77)  
> Since: 3.0.0

---

## x3

### x3: number

**Description:**

`x` coordinate of the third point.

> Source: [src/geom/triangle/Triangle.js#L97](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/triangle/Triangle.js#L97)  
> Since: 3.0.0

---

## y1

### y1: number

**Description:**

`y` coordinate of the first point.

> Source: [src/geom/triangle/Triangle.js#L67](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/triangle/Triangle.js#L67)  
> Since: 3.0.0

---

## y2

### y2: number

**Description:**

`y` coordinate of the second point.

> Source: [src/geom/triangle/Triangle.js#L87](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/triangle/Triangle.js#L87)  
> Since: 3.0.0

---

## y3

### y3: number

**Description:**

`y` coordinate of the third point.

> Source: [src/geom/triangle/Triangle.js#L107](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/triangle/Triangle.js#L107)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Methods](#public-methods)

  + [Area](#area)

    - [<static> Area(triangle)](#static-areatriangle)
  + [BuildEquilateral](#buildequilateral)

    - [<static> BuildEquilateral(x, y, length)](#static-buildequilateralx-y-length)
  + [BuildFromPolygon](#buildfrompolygon)

    - [<static> BuildFromPolygon(data, [holes], [scaleX], [scaleY], [out])](#static-buildfrompolygondata-holes-scalex-scaley-out)
  + [BuildRight](#buildright)

    - [<static> BuildRight(x, y, width, height)](#static-buildrightx-y-width-height)
  + [CenterOn](#centeron)

    - [<static> CenterOn(triangle, x, y, [centerFunc])](#static-centerontriangle-x-y-centerfunc)
  + [Centroid](#centroid)

    - [<static> Centroid(triangle, [out])](#static-centroidtriangle-out)
  + [CircumCenter](#circumcenter)

    - [<static> CircumCenter(triangle, [out])](#static-circumcentertriangle-out)
  + [CircumCircle](#circumcircle)

    - [<static> CircumCircle(triangle, [out])](#static-circumcircletriangle-out)
  + [Clone](#clone)

    - [<static> Clone(source)](#static-clonesource)
  + [contains](#contains)

    - [<instance> contains(x, y)](#instance-containsx-y)
  + [Contains](#contains-1)

    - [<static> Contains(triangle, x, y)](#static-containstriangle-x-y)
  + [ContainsArray](#containsarray)

    - [<static> ContainsArray(triangle, points, [returnFirst], [out])](#static-containsarraytriangle-points-returnfirst-out)
  + [ContainsPoint](#containspoint)

    - [<static> ContainsPoint(triangle, point)](#static-containspointtriangle-point)
  + [CopyFrom](#copyfrom)

    - [<static> CopyFrom(source, dest)](#static-copyfromsource-dest)
  + [Decompose](#decompose)

    - [<static> Decompose(triangle, [out])](#static-decomposetriangle-out)
  + [Equals](#equals)

    - [<static> Equals(triangle, toCompare)](#static-equalstriangle-tocompare)
  + [getLineA](#getlinea)

    - [<instance> getLineA([line])](#instance-getlinealine)
  + [getLineB](#getlineb)

    - [<instance> getLineB([line])](#instance-getlinebline)
  + [getLineC](#getlinec)

    - [<instance> getLineC([line])](#instance-getlinecline)
  + [getPoint](#getpoint)

    - [<instance> getPoint(position, [output])](#instance-getpointposition-output)
  + [GetPoint](#getpoint-1)

    - [<static> GetPoint(triangle, position, [out])](#static-getpointtriangle-position-out)
  + [getPoints](#getpoints)

    - [<instance> getPoints(quantity, [stepRate], [output])](#instance-getpointsquantity-steprate-output)
  + [GetPoints](#getpoints-1)

    - [<static> GetPoints(triangle, quantity, stepRate, [out])](#static-getpointstriangle-quantity-steprate-out)
  + [getRandomPoint](#getrandompoint)

    - [<instance> getRandomPoint([point])](#instance-getrandompointpoint)
  + [InCenter](#incenter)

    - [<static> InCenter(triangle, [out])](#static-incentertriangle-out)
  + [Offset](#offset)

    - [<static> Offset(triangle, x, y)](#static-offsettriangle-x-y)
  + [Perimeter](#perimeter)

    - [<static> Perimeter(triangle)](#static-perimetertriangle)
  + [Random](#random)

    - [<static> Random(triangle, [out])](#static-randomtriangle-out)
  + [Rotate](#rotate)

    - [<static> Rotate(triangle, angle)](#static-rotatetriangle-angle)
  + [RotateAroundPoint](#rotatearoundpoint)

    - [<static> RotateAroundPoint(triangle, point, angle)](#static-rotatearoundpointtriangle-point-angle)
  + [RotateAroundXY](#rotatearoundxy)

    - [<static> RotateAroundXY(triangle, x, y, angle)](#static-rotatearoundxytriangle-x-y-angle)
  + [setTo](#setto)

    - [<instance> setTo([x1], [y1], [x2], [y2], [x3], [y3])](#instance-settox1-y1-x2-y2-x3-y3)
* [Public Members](#public-members)

  + [bottom](#bottom)

    - [bottom: number](#bottom-number)
  + [left](#left)

    - [left: number](#left-number)
  + [right](#right)

    - [right: number](#right-number)
  + [top](#top)

    - [top: number](#top-number)
  + [type](#type)

    - [type: number](#type-number)
  + [x1](#x1)

    - [x1: number](#x1-number)
  + [x2](#x2)

    - [x2: number](#x2-number)
  + [x3](#x3)

    - [x3: number](#x3-number)
  + [y1](#y1)

    - [y1: number](#y1-number)
  + [y2](#y2)

    - [y2: number](#y2-number)
  + [y3](#y3)

    - [y3: number](#y3-number)

Back to top

©2025[Phaser](https://docs.phaser.io)