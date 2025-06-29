# Phaser.Geom.Intersects

Scope:
static

> Source: [src/geom/intersects/index.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/intersects/index.js#L7)

# Static functions

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

---

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

---

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

---

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

---

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

---

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

---

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

---

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

---

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

---

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

---

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

---

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

---

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

---

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

---

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

---

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

---

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

---

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

---

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

---

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

---

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

---

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

---

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

---

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

---

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

---

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

---

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

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Static functions](#static-functions)

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

Back to top

©2025[Phaser](https://docs.phaser.io)