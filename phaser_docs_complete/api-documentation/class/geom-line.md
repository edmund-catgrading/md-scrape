# Line

Phaser.Geom.Line

Defines a Line segment, a part of a line between two endpoints.

**Constructor**

`new Line([x1], [y1], [x2], [y2])`

**Parameters**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x1 | number | Yes | 0 | The x coordinate of the lines starting point. |
| --- | --- | --- | --- | --- |
| y1 | number | Yes | 0 | The y coordinate of the lines starting point. |
| x2 | number | Yes | 0 | The x coordinate of the lines ending point. |
| y2 | number | Yes | 0 | The y coordinate of the lines ending point. |

---

**Scope**: static

> Source: [src/geom/line/Line.js#L14](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/line/Line.js#L14)  
> Since: 3.0.0

# Public Methods

## Angle

### <static> Angle(line)

**Description:**

Calculate the angle of the line in radians.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| line | [Phaser.Geom.Line](geom-line.md) | No | The line to calculate the angle of. |
| --- | --- | --- | --- |

**Returns:** number - The angle of the line, in radians.

> Source: [src/geom/line/Angle.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/line/Angle.js#L7)  
> Since: 3.0.0

---

## BresenhamPoints

### <static> BresenhamPoints(line, [stepRate], [results])

**Description:**

Using Bresenham's line algorithm this will return an array of all coordinates on this line.

The `start` and `end` points are rounded before this runs as the algorithm works on integers.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| line | [Phaser.Geom.Line](geom-line.md) | No |  | The line. |
| --- | --- | --- | --- | --- |
| stepRate | number | Yes | 1 | The optional step rate for the points on the line. |
| results | Array.<[Phaser.Types.Math.Vector2Like](../typedef/types-math.md)> | Yes |  | An optional array to push the resulting coordinates into. |

**Returns:** Array.<[Phaser.Types.Math.Vector2Like](../typedef/types-math.md)> - The array of coordinates on the line.

> Source: [src/geom/line/BresenhamPoints.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/line/BresenhamPoints.js#L7)  
> Since: 3.0.0

---

## CenterOn

### <static> CenterOn(line, x, y)

**Description:**

Center a line on the given coordinates.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| line | [Phaser.Geom.Line](geom-line.md) | No | The line to center. |
| --- | --- | --- | --- |
| x | number | No | The horizontal coordinate to center the line on. |
| y | number | No | The vertical coordinate to center the line on. |

**Returns:** [Phaser.Geom.Line](geom-line.md) - The centered line.

> Source: [src/geom/line/CenterOn.js#L8](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/line/CenterOn.js#L8)  
> Since: 3.0.0

---

## Clone

### <static> Clone(source)

**Description:**

Clone the given line.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| source | [Phaser.Geom.Line](geom-line.md) | No | The source line to clone. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Geom.Line](geom-line.md) - The cloned line.

> Source: [src/geom/line/Clone.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/line/Clone.js#L9)  
> Since: 3.0.0

---

## CopyFrom

### <static> CopyFrom(source, dest)

**Description:**

Copy the values of one line to a destination line.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| source | [Phaser.Geom.Line](geom-line.md) | No | The source line to copy the values from. |
| --- | --- | --- | --- |
| dest | [Phaser.Geom.Line](geom-line.md) | No | The destination line to copy the values to. |

**Returns:** [Phaser.Geom.Line](geom-line.md) - The destination line.

> Source: [src/geom/line/CopyFrom.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/line/CopyFrom.js#L7)  
> Since: 3.0.0

---

## Equals

### <static> Equals(line, toCompare)

**Description:**

Compare two lines for strict equality.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| line | [Phaser.Geom.Line](geom-line.md) | No | The first line to compare. |
| --- | --- | --- | --- |
| toCompare | [Phaser.Geom.Line](geom-line.md) | No | The second line to compare. |

**Returns:** boolean - Whether the two lines are equal.

> Source: [src/geom/line/Equals.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/line/Equals.js#L7)  
> Since: 3.0.0

---

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
| line | [Phaser.Geom.Line](geom-line.md) | No | The line instance to extend. |
| --- | --- | --- | --- |
| left | number | No | The amount to extend the start of the line by. |
| right | number | Yes | The amount to extend the end of the line by. If not given it will be set to the `left` value. |

**Returns:** [Phaser.Geom.Line](geom-line.md) - The modified Line instance.

> Source: [src/geom/line/Extend.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/line/Extend.js#L9)  
> Since: 3.16.0

---

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
| line | [Phaser.Geom.Line](geom-line.md) | No |  | The Line object. |
| --- | --- | --- | --- | --- |
| ease | string | function | No |  | The ease to use. This can be either a string from the EaseMap, or a custom function. |
| quantity | number | No |  | The number of points to return. Note that if you provide a `collinearThreshold`, the resulting array may not always contain this number of points. |
| collinearThreshold | number | Yes | 0 | An optional threshold. The final array is reduced so that each point is spaced out at least this distance apart. This helps reduce clustering in noisey eases. |
| easeParams | Array.<number> | Yes |  | An optional array of ease parameters to go with the ease. |

**Returns:** Array.<[Phaser.Geom.Point](geom-point.md)> - An array of Geom.Points containing the coordinates of the points on the line.

> Source: [src/geom/line/GetEasedPoints.js#L11](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/line/GetEasedPoints.js#L11)  
> Since: 3.23.0

---

## GetMidPoint

### <static> GetMidPoint(line, [out])

**Description:**

Get the midpoint of the given line.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| line | [Phaser.Geom.Line](geom-line.md) | No | The line to get the midpoint of. |
| --- | --- | --- | --- |
| out | [Phaser.Geom.Point](geom-point.md) | object | Yes | An optional point object to store the midpoint in. |

**Returns:** [Phaser.Geom.Point](geom-point.md), object - The midpoint of the Line.

> Source: [src/geom/line/GetMidPoint.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/line/GetMidPoint.js#L9)  
> Since: 3.0.0

---

## GetNearestPoint

### <static> GetNearestPoint(line, point, [out])

**Description:**

Get the nearest point on a line perpendicular to the given point.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| line | [Phaser.Geom.Line](geom-line.md) | No | The line to get the nearest point on. |
| --- | --- | --- | --- |
| point | [Phaser.Geom.Point](geom-point.md) | object | No | The point to get the nearest point to. |
| out | [Phaser.Geom.Point](geom-point.md) | object | Yes | An optional point, or point-like object, to store the coordinates of the nearest point on the line. |

**Returns:** [Phaser.Geom.Point](geom-point.md), object - The nearest point on the line.

> Source: [src/geom/line/GetNearestPoint.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/line/GetNearestPoint.js#L10)  
> Since: 3.16.0

---

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
| line | [Phaser.Geom.Line](geom-line.md) | No | The line to calculate the normal of. |
| --- | --- | --- | --- |
| out | [Phaser.Geom.Point](geom-point.md) | object | Yes | An optional point object to store the normal in. |

**Returns:** [Phaser.Geom.Point](geom-point.md), object - The normal of the Line.

> Source: [src/geom/line/GetNormal.js#L11](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/line/GetNormal.js#L11)  
> Since: 3.0.0

---

## getPoint

### <instance> getPoint(position, [output])

**Description:**

Get a point on a line that's a given percentage along its length.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| position | number | No | A value between 0 and 1, where 0 is the start, 0.5 is the middle and 1 is the end of the line. |
| --- | --- | --- | --- |
| output | [Phaser.Geom.Point](geom-point.md) | object | Yes | An optional point, or point-like object, to store the coordinates of the point on the line. |

**Returns:** [Phaser.Geom.Point](geom-point.md), object - A Point, or point-like object, containing the coordinates of the point on the line.

> Source: [src/geom/line/Line.js#L87](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/line/Line.js#L87)  
> Since: 3.0.0

---

## GetPoint

### <static> GetPoint(line, position, [out])

**Description:**

Get a point on a line that's a given percentage along its length.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| line | [Phaser.Geom.Line](geom-line.md) | No | The line. |
| --- | --- | --- | --- |
| position | number | No | A value between 0 and 1, where 0 is the start, 0.5 is the middle and 1 is the end of the line. |
| out | [Phaser.Geom.Point](geom-point.md) | object | Yes | An optional point, or point-like object, to store the coordinates of the point on the line. |

**Returns:** [Phaser.Geom.Point](geom-point.md), object - The point on the line.

> Source: [src/geom/line/GetPoint.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/line/GetPoint.js#L9)  
> Since: 3.0.0

---

## getPointA

### <instance> getPointA([vec2])

**Description:**

Returns a Vector2 object that corresponds to the start of this Line.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| vec2 | [Phaser.Math.Vector2](math-vector2.md) | Yes | A Vector2 object to set the results in. If `undefined` a new Vector2 will be created. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Vector2](math-vector2.md) - A Vector2 object that corresponds to the start of this Line.

> Source: [src/geom/line/Line.js#L197](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/line/Line.js#L197)  
> Since: 3.0.0

---

## getPointB

### <instance> getPointB([vec2])

**Description:**

Returns a Vector2 object that corresponds to the end of this Line.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| vec2 | [Phaser.Math.Vector2](math-vector2.md) | Yes | A Vector2 object to set the results in. If `undefined` a new Vector2 will be created. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Vector2](math-vector2.md) - A Vector2 object that corresponds to the end of this Line.

> Source: [src/geom/line/Line.js#L218](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/line/Line.js#L218)  
> Since: 3.0.0

---

## getPoints

### <instance> getPoints(quantity, [stepRate], [output])

**Description:**

Get a number of points along a line's length.

Provide a `quantity` to get an exact number of points along the line.

Provide a `stepRate` to ensure a specific distance between each point on the line. Set `quantity` to `0` when

providing a `stepRate`.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| quantity | number | No | The number of points to place on the line. Set to `0` to use `stepRate` instead. |
| --- | --- | --- | --- |
| stepRate | number | Yes | The distance between each point on the line. When set, `quantity` is implied and should be set to `0`. |
| output | array | Array.<[Phaser.Geom.Point](geom-point.md)> | Yes | An optional array of Points, or point-like objects, to store the coordinates of the points on the line. |

**Returns:** array, Array.<[Phaser.Geom.Point](geom-point.md)> - An array of Points, or point-like objects, containing the coordinates of the points on the line.

> Source: [src/geom/line/Line.js#L105](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/line/Line.js#L105)  
> Since: 3.0.0

---

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
| line | [Phaser.Geom.Line](geom-line.md) | No | The line. |
| --- | --- | --- | --- |
| quantity | number | No | The number of points to place on the line. Set to `0` to use `stepRate` instead. |
| stepRate | number | Yes | The distance between each point on the line. When set, `quantity` is implied and should be set to `0`. |
| out | array | Array.<[Phaser.Geom.Point](geom-point.md)> | Yes | An optional array of Points, or point-like objects, to store the coordinates of the points on the line. |

**Returns:** array, Array.<[Phaser.Geom.Point](geom-point.md)> - An array of Points, or point-like objects, containing the coordinates of the points on the line.

> Source: [src/geom/line/GetPoints.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/line/GetPoints.js#L10)  
> Since: 3.0.0

---

## getRandomPoint

### <instance> getRandomPoint([point])

**Description:**

Get a random Point on the Line.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| point | [Phaser.Geom.Point](geom-point.md) | object | Yes | An instance of a Point to be modified. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Geom.Point](geom-point.md) - A random Point on the Line.

> Source: [src/geom/line/Line.js#L129](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/line/Line.js#L129)  
> Since: 3.0.0

---

## GetShortestDistance

### <static> GetShortestDistance(line, point)

**Description:**

Get the shortest distance from a Line to the given Point.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| line | [Phaser.Geom.Line](geom-line.md) | No | The line to get the distance from. |
| --- | --- | --- | --- |
| point | [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) | No | The point to get the shortest distance to. |

**Returns:** boolean, number - The shortest distance from the line to the point, or `false`.

> Source: [src/geom/line/GetShortestDistance.js#L8](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/line/GetShortestDistance.js#L8)  
> Since: 3.16.0

---

## Height

### <static> Height(line)

**Description:**

Calculate the height of the given line.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| line | [Phaser.Geom.Line](geom-line.md) | No | The line to calculate the height of. |
| --- | --- | --- | --- |

**Returns:** number - The height of the line.

> Source: [src/geom/line/Height.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/line/Height.js#L7)  
> Since: 3.0.0

---

## Length

### <static> Length(line)

**Description:**

Calculate the length of the given line.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| line | [Phaser.Geom.Line](geom-line.md) | No | The line to calculate the length of. |
| --- | --- | --- | --- |

**Returns:** number - The length of the line.

> Source: [src/geom/line/Length.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/line/Length.js#L7)  
> Since: 3.0.0

---

## NormalAngle

### <static> NormalAngle(line)

**Description:**

Get the angle of the normal of the given line in radians.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| line | [Phaser.Geom.Line](geom-line.md) | No | The line to calculate the angle of the normal of. |
| --- | --- | --- | --- |

**Returns:** number - The angle of the normal of the line in radians.

> Source: [src/geom/line/NormalAngle.js#L11](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/line/NormalAngle.js#L11)  
> Since: 3.0.0

---

## NormalX

### <static> NormalX(line)

**Description:**

Returns the x component of the normal vector of the given line.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| line | [Phaser.Geom.Line](geom-line.md) | No | The Line object to get the normal value from. |
| --- | --- | --- | --- |

**Returns:** number - The x component of the normal vector of the line.

> Source: [src/geom/line/NormalX.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/line/NormalX.js#L10)  
> Since: 3.0.0

---

## NormalY

### <static> NormalY(line)

**Description:**

The Y value of the normal of the given line.

The normal of a line is a vector that points perpendicular from it.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| line | [Phaser.Geom.Line](geom-line.md) | No | The line to calculate the normal of. |
| --- | --- | --- | --- |

**Returns:** number - The Y value of the normal of the Line.

> Source: [src/geom/line/NormalY.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/line/NormalY.js#L10)  
> Since: 3.0.0

---

## Offset

### <static> Offset(line, x, y)

**Description:**

Offset a line by the given amount.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| line | [Phaser.Geom.Line](geom-line.md) | No | The line to offset. |
| --- | --- | --- | --- |
| x | number | No | The horizontal offset to add to the line. |
| y | number | No | The vertical offset to add to the line. |

**Returns:** [Phaser.Geom.Line](geom-line.md) - The offset line.

> Source: [src/geom/line/Offset.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/line/Offset.js#L7)  
> Since: 3.0.0

---

## PerpSlope

### <static> PerpSlope(line)

**Description:**

Calculate the perpendicular slope of the given line.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| line | [Phaser.Geom.Line](geom-line.md) | No | The line to calculate the perpendicular slope of. |
| --- | --- | --- | --- |

**Returns:** number - The perpendicular slope of the line.

> Source: [src/geom/line/PerpSlope.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/line/PerpSlope.js#L7)  
> Since: 3.0.0

---

## Random

### <static> Random(line, [out])

**Description:**

Returns a random point on a given Line.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| line | [Phaser.Geom.Line](geom-line.md) | No | The Line to calculate the random Point on. |
| --- | --- | --- | --- |
| out | [Phaser.Geom.Point](geom-point.md) | object | Yes | An instance of a Point to be modified. |

**Returns:** [Phaser.Geom.Point](geom-point.md), object - A random Point on the Line.

> Source: [src/geom/line/Random.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/line/Random.js#L9)  
> Since: 3.0.0

---

## ReflectAngle

### <static> ReflectAngle(lineA, lineB)

**Description:**

Calculate the reflected angle between two lines.

This is the outgoing angle based on the angle of Line 1 and the normalAngle of Line 2.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| lineA | [Phaser.Geom.Line](geom-line.md) | No | The first line. |
| --- | --- | --- | --- |
| lineB | [Phaser.Geom.Line](geom-line.md) | No | The second line. |

**Returns:** number - The reflected angle between each line.

> Source: [src/geom/line/ReflectAngle.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/line/ReflectAngle.js#L10)  
> Since: 3.0.0

---

## Rotate

### <static> Rotate(line, angle)

**Description:**

Rotate a line around its midpoint by the given angle in radians.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| line | [Phaser.Geom.Line](geom-line.md) | No | The line to rotate. |
| --- | --- | --- | --- |
| angle | number | No | The angle of rotation in radians. |

**Returns:** [Phaser.Geom.Line](geom-line.md) - The rotated line.

> Source: [src/geom/line/Rotate.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/line/Rotate.js#L9)  
> Since: 3.0.0

---

## RotateAroundPoint

### <static> RotateAroundPoint(line, point, angle)

**Description:**

Rotate a line around a point by the given angle in radians.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| line | [Phaser.Geom.Line](geom-line.md) | No | The line to rotate. |
| --- | --- | --- | --- |
| point | [Phaser.Geom.Point](geom-point.md) | object | No | The point to rotate the line around. |
| angle | number | No | The angle of rotation in radians. |

**Returns:** [Phaser.Geom.Line](geom-line.md) - The rotated line.

> Source: [src/geom/line/RotateAroundPoint.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/line/RotateAroundPoint.js#L9)  
> Since: 3.0.0

---

## RotateAroundXY

### <static> RotateAroundXY(line, x, y, angle)

**Description:**

Rotate a line around the given coordinates by the given angle in radians.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| line | [Phaser.Geom.Line](geom-line.md) | No | The line to rotate. |
| --- | --- | --- | --- |
| x | number | No | The horizontal coordinate to rotate the line around. |
| y | number | No | The vertical coordinate to rotate the line around. |
| angle | number | No | The angle of rotation in radians. |

**Returns:** [Phaser.Geom.Line](geom-line.md) - The rotated line.

> Source: [src/geom/line/RotateAroundXY.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/line/RotateAroundXY.js#L7)  
> Since: 3.0.0

---

## setFromObjects

### <instance> setFromObjects(start, end)

**Description:**

Sets this Line to match the x/y coordinates of the two given Vector2Like objects.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| start | [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) | No | Any object with public `x` and `y` properties, whose values will be assigned to the x1/y1 components of this Line. |
| --- | --- | --- | --- |
| end | [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) | No | Any object with public `x` and `y` properties, whose values will be assigned to the x2/y2 components of this Line. |

**Returns:** [Phaser.Geom.Line](geom-line.md) - This Line object.

> Source: [src/geom/line/Line.js#L175](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/line/Line.js#L175)  
> Since: 3.70.0

---

## setTo

### <instance> setTo([x1], [y1], [x2], [y2])

**Description:**

Set new coordinates for the line endpoints.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x1 | number | Yes | 0 | The x coordinate of the lines starting point. |
| --- | --- | --- | --- | --- |
| y1 | number | Yes | 0 | The y coordinate of the lines starting point. |
| x2 | number | Yes | 0 | The x coordinate of the lines ending point. |
| y2 | number | Yes | 0 | The y coordinate of the lines ending point. |

**Returns:** [Phaser.Geom.Line](geom-line.md) - This Line object.

> Source: [src/geom/line/Line.js#L146](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/line/Line.js#L146)  
> Since: 3.0.0

---

## SetToAngle

### <static> SetToAngle(line, x, y, angle, length)

**Description:**

Set a line to a given position, angle and length.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| line | [Phaser.Geom.Line](geom-line.md) | No | The line to set. |
| --- | --- | --- | --- |
| x | number | No | The horizontal start position of the line. |
| y | number | No | The vertical start position of the line. |
| angle | number | No | The angle of the line in radians. |
| length | number | No | The length of the line. |

**Returns:** [Phaser.Geom.Line](geom-line.md) - The updated line.

> Source: [src/geom/line/SetToAngle.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/line/SetToAngle.js#L7)  
> Since: 3.0.0

---

## Slope

### <static> Slope(line)

**Description:**

Calculate the slope of the given line.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| line | [Phaser.Geom.Line](geom-line.md) | No | The line to calculate the slope of. |
| --- | --- | --- | --- |

**Returns:** number - The slope of the line.

> Source: [src/geom/line/Slope.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/line/Slope.js#L7)  
> Since: 3.0.0

---

## Width

### <static> Width(line)

**Description:**

Calculate the width of the given line.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| line | [Phaser.Geom.Line](geom-line.md) | No | The line to calculate the width of. |
| --- | --- | --- | --- |

**Returns:** number - The width of the line.

> Source: [src/geom/line/Width.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/line/Width.js#L7)  
> Since: 3.0.0

---

# Public Members

## bottom

### bottom: number

**Description:**

The bottom position of the Line.

> Source: [src/geom/line/Line.js#L323](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/line/Line.js#L323)  
> Since: 3.0.0

---

## left

### left: number

**Description:**

The left position of the Line.

> Source: [src/geom/line/Line.js#L239](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/line/Line.js#L239)  
> Since: 3.0.0

---

## right

### right: number

**Description:**

The right position of the Line.

> Source: [src/geom/line/Line.js#L267](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/line/Line.js#L267)  
> Since: 3.0.0

---

## top

### top: number

**Description:**

The top position of the Line.

> Source: [src/geom/line/Line.js#L295](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/line/Line.js#L295)  
> Since: 3.0.0

---

## type

### type: number

**Description:**

The geometry constant type of this object: `GEOM_CONST.LINE`.

Used for fast type comparisons.

> Source: [src/geom/line/Line.js#L39](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/line/Line.js#L39)  
> Since: 3.19.0

---

## x1

### x1: number

**Description:**

The x coordinate of the lines starting point.

> Source: [src/geom/line/Line.js#L50](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/line/Line.js#L50)  
> Since: 3.0.0

---

## x2

### x2: number

**Description:**

The x coordinate of the lines ending point.

> Source: [src/geom/line/Line.js#L68](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/line/Line.js#L68)  
> Since: 3.0.0

---

## y1

### y1: number

**Description:**

The y coordinate of the lines starting point.

> Source: [src/geom/line/Line.js#L59](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/line/Line.js#L59)  
> Since: 3.0.0

---

## y2

### y2: number

**Description:**

The y coordinate of the lines ending point.

> Source: [src/geom/line/Line.js#L77](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/line/Line.js#L77)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Methods](#public-methods)

  + [Angle](#angle)

    - [<static> Angle(line)](#static-angleline)
  + [BresenhamPoints](#bresenhampoints)

    - [<static> BresenhamPoints(line, [stepRate], [results])](#static-bresenhampointsline-steprate-results)
  + [CenterOn](#centeron)

    - [<static> CenterOn(line, x, y)](#static-centeronline-x-y)
  + [Clone](#clone)

    - [<static> Clone(source)](#static-clonesource)
  + [CopyFrom](#copyfrom)

    - [<static> CopyFrom(source, dest)](#static-copyfromsource-dest)
  + [Equals](#equals)

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
  + [getPoint](#getpoint)

    - [<instance> getPoint(position, [output])](#instance-getpointposition-output)
  + [GetPoint](#getpoint-1)

    - [<static> GetPoint(line, position, [out])](#static-getpointline-position-out)
  + [getPointA](#getpointa)

    - [<instance> getPointA([vec2])](#instance-getpointavec2)
  + [getPointB](#getpointb)

    - [<instance> getPointB([vec2])](#instance-getpointbvec2)
  + [getPoints](#getpoints)

    - [<instance> getPoints(quantity, [stepRate], [output])](#instance-getpointsquantity-steprate-output)
  + [GetPoints](#getpoints-1)

    - [<static> GetPoints(line, quantity, [stepRate], [out])](#static-getpointsline-quantity-steprate-out)
  + [getRandomPoint](#getrandompoint)

    - [<instance> getRandomPoint([point])](#instance-getrandompointpoint)
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
  + [Offset](#offset)

    - [<static> Offset(line, x, y)](#static-offsetline-x-y)
  + [PerpSlope](#perpslope)

    - [<static> PerpSlope(line)](#static-perpslopeline)
  + [Random](#random)

    - [<static> Random(line, [out])](#static-randomline-out)
  + [ReflectAngle](#reflectangle)

    - [<static> ReflectAngle(lineA, lineB)](#static-reflectanglelinea-lineb)
  + [Rotate](#rotate)

    - [<static> Rotate(line, angle)](#static-rotateline-angle)
  + [RotateAroundPoint](#rotatearoundpoint)

    - [<static> RotateAroundPoint(line, point, angle)](#static-rotatearoundpointline-point-angle)
  + [RotateAroundXY](#rotatearoundxy)

    - [<static> RotateAroundXY(line, x, y, angle)](#static-rotatearoundxyline-x-y-angle)
  + [setFromObjects](#setfromobjects)

    - [<instance> setFromObjects(start, end)](#instance-setfromobjectsstart-end)
  + [setTo](#setto)

    - [<instance> setTo([x1], [y1], [x2], [y2])](#instance-settox1-y1-x2-y2)
  + [SetToAngle](#settoangle)

    - [<static> SetToAngle(line, x, y, angle, length)](#static-settoangleline-x-y-angle-length)
  + [Slope](#slope)

    - [<static> Slope(line)](#static-slopeline)
  + [Width](#width)

    - [<static> Width(line)](#static-widthline)
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
  + [y1](#y1)

    - [y1: number](#y1-number)
  + [y2](#y2)

    - [y2: number](#y2-number)

Back to top

©2025[Phaser](https://docs.phaser.io)