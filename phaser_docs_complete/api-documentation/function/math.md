# Phaser.Math

# Phaser.Math.Angle

## Between

### <static> Between(x1, y1, x2, y2)

**Description:**

Find the angle of a segment from (x1, y1) -> (x2, y2).

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x1 | number | No | The x coordinate of the first point. |
| --- | --- | --- | --- |
| y1 | number | No | The y coordinate of the first point. |
| x2 | number | No | The x coordinate of the second point. |
| y2 | number | No | The y coordinate of the second point. |

**Returns:** number - The angle in radians.

> Source: [src/math/angle/Between.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/angle/Between.js#L7)  
> Since: 3.0.0

## BetweenPoints

### <static> BetweenPoints(point1, point2)

**Description:**

Find the angle of a segment from (point1.x, point1.y) -> (point2.x, point2.y).

Calculates the angle of the vector from the first point to the second point.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| point1 | [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) | No | The first point. |
| --- | --- | --- | --- |
| point2 | [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) | No | The second point. |

**Returns:** number - The angle in radians.

> Source: [src/math/angle/BetweenPoints.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/angle/BetweenPoints.js#L7)  
> Since: 3.0.0

## BetweenPointsY

### <static> BetweenPointsY(point1, point2)

**Description:**

Find the angle of a segment from (point1.x, point1.y) -> (point2.x, point2.y).

The difference between this method and [Phaser.Math.Angle.BetweenPoints](../namespace/math-angle.md) is that this assumes the y coordinate

travels down the screen.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| point1 | [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) | No | The first point. |
| --- | --- | --- | --- |
| point2 | [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) | No | The second point. |

**Returns:** number - The angle in radians.

> Source: [src/math/angle/BetweenPointsY.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/angle/BetweenPointsY.js#L7)  
> Since: 3.0.0

## BetweenY

### <static> BetweenY(x1, y1, x2, y2)

**Description:**

Find the angle of a segment from (x1, y1) -> (x2, y2).

The difference between this method and [Phaser.Math.Angle.Between](../namespace/math-angle.md) is that this assumes the y coordinate

travels down the screen.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x1 | number | No | The x coordinate of the first point. |
| --- | --- | --- | --- |
| y1 | number | No | The y coordinate of the first point. |
| x2 | number | No | The x coordinate of the second point. |
| y2 | number | No | The y coordinate of the second point. |

**Returns:** number - The angle in radians.

> Source: [src/math/angle/BetweenY.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/angle/BetweenY.js#L7)  
> Since: 3.0.0

## CounterClockwise

### <static> CounterClockwise(angle)

**Description:**

Takes an angle in Phasers default clockwise format and converts it so that

0 is North, 90 is West, 180 is South and 270 is East,

therefore running counter-clockwise instead of clockwise.

You can pass in the angle from a Game Object using:

```
Copy
var converted = CounterClockwise(gameobject.rotation);


```

All values for this function are in radians.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| angle | number | No | The angle to convert, in radians. |
| --- | --- | --- | --- |

**Returns:** number - The converted angle, in radians.

> Source: [src/math/angle/CounterClockwise.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/angle/CounterClockwise.js#L9)  
> Since: 3.16.0

## Normalize

### <static> Normalize(angle)

**Description:**

Normalize an angle to the [0, 2pi] range.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| angle | number | No | The angle to normalize, in radians. |
| --- | --- | --- | --- |

**Returns:** number - The normalized angle, in radians.

> Source: [src/math/angle/Normalize.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/angle/Normalize.js#L7)  
> Since: 3.0.0

## Random

### <static> Random()

**Description:**

Returns a random angle in the range [-pi, pi].

**Returns:** number - The angle, in radians.

> Source: [src/math/angle/Random.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/angle/Random.js#L10)  
> Since: 3.23.0

## RandomDegrees

### <static> RandomDegrees()

**Description:**

Returns a random angle in the range [-180, 180].

**Returns:** number - The angle, in degrees.

> Source: [src/math/angle/RandomDegrees.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/angle/RandomDegrees.js#L10)  
> Since: 3.23.0

## Reverse

### <static> Reverse(angle)

**Description:**

Reverse the given angle.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| angle | number | No | The angle to reverse, in radians. |
| --- | --- | --- | --- |

**Returns:** number - The reversed angle, in radians.

> Source: [src/math/angle/Reverse.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/angle/Reverse.js#L9)  
> Since: 3.0.0

## RotateTo

### <static> RotateTo(currentAngle, targetAngle, [lerp])

**Description:**

Rotates `currentAngle` towards `targetAngle`, taking the shortest rotation distance. The `lerp` argument is the amount to rotate by in this call.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| currentAngle | number | No |  | The current angle, in radians. |
| --- | --- | --- | --- | --- |
| targetAngle | number | No |  | The target angle to rotate to, in radians. |
| lerp | number | Yes | 0.05 | The lerp value to add to the current angle. |

**Returns:** number - The adjusted angle.

> Source: [src/math/angle/RotateTo.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/angle/RotateTo.js#L9)  
> Since: 3.0.0

## ShortestBetween

### <static> ShortestBetween(angle1, angle2)

**Description:**

Gets the shortest angle between `angle1` and `angle2`.

Both angles must be in the range -180 to 180, which is the same clamped

range that `sprite.angle` uses, so you can pass in two sprite angles to

this method and get the shortest angle back between the two of them.

The angle returned will be in the same range. If the returned angle is

greater than 0 then it's a counter-clockwise rotation, if < 0 then it's

a clockwise rotation.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| angle1 | number | No | The first angle in the range -180 to 180. |
| --- | --- | --- | --- |
| angle2 | number | No | The second angle in the range -180 to 180. |

**Returns:** number - The shortest angle, in degrees. If greater than zero it's a counter-clockwise rotation.

> Source: [src/math/angle/ShortestBetween.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/angle/ShortestBetween.js#L7)  
> Since: 3.0.0

## Wrap

### <static> Wrap(angle)

**Description:**

Wrap an angle.

Wraps the angle to a value in the range of -PI to PI.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| angle | number | No | The angle to wrap, in radians. |
| --- | --- | --- | --- |

**Returns:** number - The wrapped angle, in radians.

> Source: [src/math/angle/Wrap.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/angle/Wrap.js#L9)  
> Since: 3.0.0

## WrapDegrees

### <static> WrapDegrees(angle)

**Description:**

Wrap an angle in degrees.

Wraps the angle to a value in the range of -180 to 180.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| angle | number | No | The angle to wrap, in degrees. |
| --- | --- | --- | --- |

**Returns:** number - The wrapped angle, in degrees.

> Source: [src/math/angle/WrapDegrees.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/angle/WrapDegrees.js#L9)  
> Since: 3.0.0

## Average

### <static> Average(values)

**Description:**

Calculate the mean average of the given values.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| values | Array.<number> | No | The values to average. |
| --- | --- | --- | --- |

**Returns:** number - The average value.

> Source: [src/math/Average.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Average.js#L7)  
> Since: 3.0.0

## Bernstein

### <static> Bernstein(n, i)

**Description:**

Calculates the Bernstein basis from the three factorial coefficients.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| n | number | No | The first value. |
| --- | --- | --- | --- |
| i | number | No | The second value. |

**Returns:** number - The Bernstein basis of Factorial(n) / Factorial(i) / Factorial(n - i)

> Source: [src/math/Bernstein.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Bernstein.js#L9)  
> Since: 3.0.0

## Between

### <static> Between(min, max)

**Description:**

Compute a random integer between the `min` and `max` values, inclusive.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| min | number | No | The minimum value. |
| --- | --- | --- | --- |
| max | number | No | The maximum value. |

**Returns:** number - The random integer.

> Source: [src/math/Between.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Between.js#L7)  
> Since: 3.0.0

## CatmullRom

### <static> CatmullRom(t, p0, p1, p2, p3)

**Description:**

Calculates a Catmull-Rom value from the given points, based on an alpha of 0.5.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| t | number | No | The amount to interpolate by. |
| --- | --- | --- | --- |
| p0 | number | No | The first control point. |
| p1 | number | No | The second control point. |
| p2 | number | No | The third control point. |
| p3 | number | No | The fourth control point. |

**Returns:** number - The Catmull-Rom value.

> Source: [src/math/CatmullRom.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/CatmullRom.js#L7)  
> Since: 3.0.0

## CeilTo

### <static> CeilTo(value, [place], [base])

**Description:**

Ceils to some place comparative to a `base`, default is 10 for decimal place.

The `place` is represented by the power applied to `base` to get that place.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| value | number | No |  | The value to round. |
| --- | --- | --- | --- | --- |
| place | number | Yes | 0 | The place to round to. |
| base | number | Yes | 10 | The base to round in. Default is 10 for decimal. |

**Returns:** number - The rounded value.

> Source: [src/math/CeilTo.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/CeilTo.js#L7)  
> Since: 3.0.0

## Clamp

### <static> Clamp(value, min, max)

**Description:**

Force a value within the boundaries by clamping it to the range `min`, `max`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The value to be clamped. |
| --- | --- | --- | --- |
| min | number | No | The minimum bounds. |
| max | number | No | The maximum bounds. |

**Returns:** number - The clamped value.

> Source: [src/math/Clamp.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Clamp.js#L7)  
> Since: 3.0.0

## DegToRad

### <static> DegToRad(degrees)

**Description:**

Convert the given angle from degrees, to the equivalent angle in radians.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| degrees | number | No | The angle (in degrees) to convert to radians. |
| --- | --- | --- | --- |

**Returns:** number - The given angle converted to radians.

> Source: [src/math/DegToRad.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/DegToRad.js#L9)  
> Since: 3.0.0

## Difference

### <static> Difference(a, b)

**Description:**

Calculates the positive difference of two given numbers.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| a | number | No | The first number in the calculation. |
| --- | --- | --- | --- |
| b | number | No | The second number in the calculation. |

**Returns:** number - The positive difference of the two given numbers.

> Source: [src/math/Difference.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Difference.js#L7)  
> Since: 3.0.0

## Factorial

### <static> Factorial(value)

**Description:**

Calculates the factorial of a given number for integer values greater than 0.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | A positive integer to calculate the factorial of. |
| --- | --- | --- | --- |

**Returns:** number - The factorial of the given number.

> Source: [src/math/Factorial.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Factorial.js#L7)  
> Since: 3.0.0

## FloatBetween

### <static> FloatBetween(min, max)

**Description:**

Generate a random floating point number between the two given bounds, minimum inclusive, maximum exclusive.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| min | number | No | The lower bound for the float, inclusive. |
| --- | --- | --- | --- |
| max | number | No | The upper bound for the float exclusive. |

**Returns:** number - A random float within the given range.

> Source: [src/math/FloatBetween.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/FloatBetween.js#L7)  
> Since: 3.0.0

## FloorTo

### <static> FloorTo(value, [place], [base])

**Description:**

Floors to some place comparative to a `base`, default is 10 for decimal place.

The `place` is represented by the power applied to `base` to get that place.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| value | number | No |  | The value to round. |
| --- | --- | --- | --- | --- |
| place | number | Yes | 0 | The place to round to. |
| base | number | Yes | 10 | The base to round in. Default is 10 for decimal. |

**Returns:** number - The rounded value.

> Source: [src/math/FloorTo.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/FloorTo.js#L7)  
> Since: 3.0.0

## FromPercent

### <static> FromPercent(percent, min, [max])

**Description:**

Return a value based on the range between `min` and `max` and the percentage given.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| percent | number | No | A value between 0 and 1 representing the percentage. |
| --- | --- | --- | --- |
| min | number | No | The minimum value. |
| max | number | Yes | The maximum value. |

**Returns:** number - The value that is `percent` percent between `min` and `max`.

> Source: [src/math/FromPercent.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/FromPercent.js#L9)  
> Since: 3.0.0

## GetSpeed

### <static> GetSpeed(distance, time)

**Description:**

Calculate a per-ms speed from a distance and time (given in seconds).

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| distance | number | No | The distance. |
| --- | --- | --- | --- |
| time | number | No | The time, in seconds. |

**Returns:** number - The speed, in distance per ms.

> Source: [src/math/GetSpeed.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/GetSpeed.js#L7)  
> Since: 3.0.0

## IsEven

### <static> IsEven(value)

**Description:**

Check if a given value is an even number.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The number to perform the check with. |
| --- | --- | --- | --- |

**Returns:** boolean - Whether the number is even or not.

> Source: [src/math/IsEven.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/IsEven.js#L7)  
> Since: 3.0.0

## IsEvenStrict

### <static> IsEvenStrict(value)

**Description:**

Check if a given value is an even number using a strict type check.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The number to perform the check with. |
| --- | --- | --- | --- |

**Returns:** boolean - Whether the number is even or not.

> Source: [src/math/IsEvenStrict.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/IsEvenStrict.js#L7)  
> Since: 3.0.0

## Linear

### <static> Linear(p0, p1, t)

**Description:**

Calculates a linear (interpolation) value over t.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| p0 | number | No | The first point. |
| --- | --- | --- | --- |
| p1 | number | No | The second point. |
| t | number | No | The percentage between p0 and p1 to return, represented as a number between 0 and 1. |

**Returns:** number - The step t% of the way between p0 and p1.

> Source: [src/math/Linear.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Linear.js#L7)  
> Since: 3.0.0

## LinearXY

### <static> LinearXY(vector1, vector2, [t])

**Description:**

Interpolates two given Vectors and returns a new Vector between them.

Does not modify either of the passed Vectors.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| vector1 | [Phaser.Math.Vector2](../class/math-vector2.md) | No |  | Starting vector |
| --- | --- | --- | --- | --- |
| vector2 | [Phaser.Math.Vector2](../class/math-vector2.md) | No |  | Ending vector |
| t | number | Yes | 0 | The percentage between vector1 and vector2 to return, represented as a number between 0 and 1. |

**Returns:** [Phaser.Math.Vector2](../class/math-vector2.md) - The step t% of the way between vector1 and vector2.

> Source: [src/math/LinearXY.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/LinearXY.js#L7)  
> Since: 3.60.0

## MaxAdd

### <static> MaxAdd(value, amount, max)

**Description:**

Add an `amount` to a `value`, limiting the maximum result to `max`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The value to add to. |
| --- | --- | --- | --- |
| amount | number | No | The amount to add. |
| max | number | No | The maximum value to return. |

**Returns:** number - The resulting value.

> Source: [src/math/MaxAdd.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/MaxAdd.js#L7)  
> Since: 3.0.0

## Median

### <static> Median(values)

**Description:**

Calculate the median of the given values. The values are sorted and the middle value is returned.

In case of an even number of values, the average of the two middle values is returned.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| values | Array.<number> | No | The values to average. |
| --- | --- | --- | --- |

**Returns:** number - The median value.

> Source: [src/math/Median.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Median.js#L7)  
> Since: 3.54.0

## MinSub

### <static> MinSub(value, amount, min)

**Description:**

Subtract an `amount` from `value`, limiting the minimum result to `min`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The value to subtract from. |
| --- | --- | --- | --- |
| amount | number | No | The amount to subtract. |
| min | number | No | The minimum value to return. |

**Returns:** number - The resulting value.

> Source: [src/math/MinSub.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/MinSub.js#L7)  
> Since: 3.0.0

## Percent

### <static> Percent(value, min, [max], [upperMax])

**Description:**

Work out what percentage `value` is of the range between `min` and `max`.

If `max` isn't given then it will return the percentage of `value` to `min`.

You can optionally specify an `upperMax` value, which is a mid-way point in the range that represents 100%, after which the % starts to go down to zero again.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The value to determine the percentage of. |
| --- | --- | --- | --- |
| min | number | No | The minimum value. |
| max | number | Yes | The maximum value. |
| upperMax | number | Yes | The mid-way point in the range that represents 100%. |

**Returns:** number - A value between 0 and 1 representing the percentage.

> Source: [src/math/Percent.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Percent.js#L7)  
> Since: 3.0.0

## RadToDeg

### <static> RadToDeg(radians)

**Description:**

Convert the given angle in radians, to the equivalent angle in degrees.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| radians | number | No | The angle in radians to convert ot degrees. |
| --- | --- | --- | --- |

**Returns:** number - The given angle converted to degrees.

> Source: [src/math/RadToDeg.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/RadToDeg.js#L9)  
> Since: 3.0.0

## RandomXY

### <static> RandomXY(vector, [scale])

**Description:**

Compute a random unit vector.

Computes random values for the given vector between -1 and 1 that can be used to represent a direction.

Optionally accepts a scale value to scale the resulting vector by.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| vector | [Phaser.Math.Vector2](../class/math-vector2.md) | No |  | The Vector to compute random values for. |
| --- | --- | --- | --- | --- |
| scale | number | Yes | 1 | The scale of the random values. |

**Returns:** [Phaser.Math.Vector2](../class/math-vector2.md) - The given Vector.

> Source: [src/math/RandomXY.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/RandomXY.js#L7)  
> Since: 3.0.0

## RandomXYZ

### <static> RandomXYZ(vec3, [radius])

**Description:**

Compute a random position vector in a spherical area, optionally defined by the given radius.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| vec3 | [Phaser.Math.Vector3](../class/math-vector3.md) | No |  | The Vector to compute random values for. |
| --- | --- | --- | --- | --- |
| radius | number | Yes | 1 | The radius. |

**Returns:** [Phaser.Math.Vector3](../class/math-vector3.md) - The given Vector.

> Source: [src/math/RandomXYZ.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/RandomXYZ.js#L7)  
> Since: 3.0.0

## RandomXYZW

### <static> RandomXYZW(vec4, [scale])

**Description:**

Compute a random four-dimensional vector.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| vec4 | [Phaser.Math.Vector4](../class/math-vector4.md) | No |  | The Vector to compute random values for. |
| --- | --- | --- | --- | --- |
| scale | number | Yes | 1 | The scale of the random values. |

**Returns:** [Phaser.Math.Vector4](../class/math-vector4.md) - The given Vector.

> Source: [src/math/RandomXYZW.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/RandomXYZW.js#L7)  
> Since: 3.0.0

## Rotate

### <static> Rotate(point, angle)

**Description:**

Rotate a given point by a given angle around the origin (0, 0), in an anti-clockwise direction.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| point | [Phaser.Geom.Point](../class/geom-point.md) | object | No | The point to be rotated. |
| --- | --- | --- | --- |
| angle | number | No | The angle to be rotated by in an anticlockwise direction. |

**Returns:** [Phaser.Geom.Point](../class/geom-point.md) - The given point, rotated by the given angle in an anticlockwise direction.

> Source: [src/math/Rotate.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Rotate.js#L7)  
> Since: 3.0.0

## RotateAround

### <static> RotateAround(point, x, y, angle)

**Description:**

Rotate a `point` around `x` and `y` to the given `angle`, at the same distance.

In polar notation, this maps a point from (r, t) to (r, angle), vs. the origin (x, y).

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| point | [Phaser.Geom.Point](../class/geom-point.md) | object | No | The point to be rotated. |
| --- | --- | --- | --- |
| x | number | No | The horizontal coordinate to rotate around. |
| y | number | No | The vertical coordinate to rotate around. |
| angle | number | No | The angle of rotation in radians. |

**Returns:** [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) - The given point.

> Source: [src/math/RotateAround.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/RotateAround.js#L7)  
> Since: 3.0.0

## RotateAroundDistance

### <static> RotateAroundDistance(point, x, y, angle, distance)

**Description:**

Rotate a `point` around `x` and `y` by the given `angle` and `distance`.

In polar notation, this maps a point from (r, t) to (distance, t + angle), vs. the origin (x, y).

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| point | [Phaser.Geom.Point](../class/geom-point.md) | object | No | The point to be rotated. |
| --- | --- | --- | --- |
| x | number | No | The horizontal coordinate to rotate around. |
| y | number | No | The vertical coordinate to rotate around. |
| angle | number | No | The angle of rotation in radians. |
| distance | number | No | The distance from (x, y) to place the point at. |

**Returns:** [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) - The given point.

> Source: [src/math/RotateAroundDistance.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/RotateAroundDistance.js#L7)  
> Since: 3.0.0

## RotateTo

### <static> RotateTo(point, x, y, angle, distance)

**Description:**

Position a `point` at the given `angle` and `distance` to (`x`, `y`).

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| point | [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) | No | The point to be positioned. |
| --- | --- | --- | --- |
| x | number | No | The horizontal coordinate to position from. |
| y | number | No | The vertical coordinate to position from. |
| angle | number | No | The angle of rotation in radians. |
| distance | number | No | The distance from (x, y) to place the point at. |

**Returns:** [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) - The given point.

> Source: [src/math/RotateTo.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/RotateTo.js#L7)  
> Since: 3.24.0

## RotateVec3

### <static> RotateVec3(vec, axis, radians)

**Description:**

Rotates a vector in place by axis angle.

This is the same as transforming a point by an

axis-angle quaternion, but it has higher precision.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| vec | [Phaser.Math.Vector3](../class/math-vector3.md) | No | The vector to be rotated. |
| --- | --- | --- | --- |
| axis | [Phaser.Math.Vector3](../class/math-vector3.md) | No | The axis to rotate around. |
| radians | number | No | The angle of rotation in radians. |

**Returns:** [Phaser.Math.Vector3](../class/math-vector3.md) - The given vector.

> Source: [src/math/RotateVec3.js#L15](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/RotateVec3.js#L15)  
> Since: 3.0.0

## RoundAwayFromZero

### <static> RoundAwayFromZero(value)

**Description:**

Round a given number so it is further away from zero. That is, positive numbers are rounded up, and negative numbers are rounded down.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The number to round. |
| --- | --- | --- | --- |

**Returns:** number - The rounded number, rounded away from zero.

> Source: [src/math/RoundAwayFromZero.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/RoundAwayFromZero.js#L7)  
> Since: 3.0.0

## RoundTo

### <static> RoundTo(value, [place], [base])

**Description:**

Round a value to the given precision.

For example:

```
Copy
RoundTo(123.456, 0) = 123

RoundTo(123.456, 1) = 120

RoundTo(123.456, 2) = 100


```

To round the decimal, i.e. to round to precision, pass in a negative `place`:

```
Copy
RoundTo(123.456789, 0) = 123

RoundTo(123.456789, -1) = 123.5

RoundTo(123.456789, -2) = 123.46

RoundTo(123.456789, -3) = 123.457


```

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| value | number | No |  | The value to round. |
| --- | --- | --- | --- | --- |
| place | number | Yes | 0 | The place to round to. Positive to round the units, negative to round the decimal. |
| base | number | Yes | 10 | The base to round in. Default is 10 for decimal. |

**Returns:** number - The rounded value.

> Source: [src/math/RoundTo.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/RoundTo.js#L7)  
> Since: 3.0.0

## SinCosTableGenerator

### <static> SinCosTableGenerator(length, [sinAmp], [cosAmp], [frequency])

**Description:**

Generate a series of sine and cosine values.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| length | number | No |  | The number of values to generate. |
| --- | --- | --- | --- | --- |
| sinAmp | number | Yes | 1 | The sine value amplitude. |
| cosAmp | number | Yes | 1 | The cosine value amplitude. |
| frequency | number | Yes | 1 | The frequency of the values. |

**Returns:** [Phaser.Types.Math.SinCosTable](../typedef/types-math.md) - The generated values.

> Source: [src/math/SinCosTableGenerator.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/SinCosTableGenerator.js#L7)  
> Since: 3.0.0

## SmootherStep

### <static> SmootherStep(x, min, max)

**Description:**

Calculate a smoother interpolation percentage of `x` between `min` and `max`.

The function receives the number `x` as an argument and returns 0 if `x` is less than or equal to the left edge,

1 if `x` is greater than or equal to the right edge, and smoothly interpolates, using a Hermite polynomial,

between 0 and 1 otherwise.

Produces an even smoother interpolation than [Phaser.Math.SmoothStep](../namespace/math.md).

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The input value. |
| --- | --- | --- | --- |
| min | number | No | The minimum value, also known as the 'left edge', assumed smaller than the 'right edge'. |
| max | number | No | The maximum value, also known as the 'right edge', assumed greater than the 'left edge'. |

**Returns:** number - The percentage of interpolation, between 0 and 1.

> Source: [src/math/SmootherStep.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/SmootherStep.js#L7)  
> Since: 3.0.0

## SmoothStep

### <static> SmoothStep(x, min, max)

**Description:**

Calculate a smooth interpolation percentage of `x` between `min` and `max`.

The function receives the number `x` as an argument and returns 0 if `x` is less than or equal to the left edge,

1 if `x` is greater than or equal to the right edge, and smoothly interpolates, using a Hermite polynomial,

between 0 and 1 otherwise.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The input value. |
| --- | --- | --- | --- |
| min | number | No | The minimum value, also known as the 'left edge', assumed smaller than the 'right edge'. |
| max | number | No | The maximum value, also known as the 'right edge', assumed greater than the 'left edge'. |

**Returns:** number - The percentage of interpolation, between 0 and 1.

> Source: [src/math/SmoothStep.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/SmoothStep.js#L7)  
> Since: 3.0.0

## ToXY

### <static> ToXY(index, width, height, [out])

**Description:**

Returns a Vector2 containing the x and y position of the given index in a `width` x `height` sized grid.

For example, in a 6 x 4 grid, index 16 would equal x: 4 y: 2.

If the given index is out of range an empty Vector2 is returned.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| index | number | No | The position within the grid to get the x/y value for. |
| --- | --- | --- | --- |
| width | number | No | The width of the grid. |
| height | number | No | The height of the grid. |
| out | [Phaser.Math.Vector2](../class/math-vector2.md) | Yes | An optional Vector2 to store the result in. If not given, a new Vector2 instance will be created. |

**Returns:** [Phaser.Math.Vector2](../class/math-vector2.md) - A Vector2 where the x and y properties contain the given grid index.

> Source: [src/math/ToXY.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/ToXY.js#L9)  
> Since: 3.19.0

## TransformXY

### <static> TransformXY(x, y, positionX, positionY, rotation, scaleX, scaleY, [output])

**Description:**

Takes the `x` and `y` coordinates and transforms them into the same space as

defined by the position, rotation and scale values.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The x coordinate to be transformed. |
| --- | --- | --- | --- |
| y | number | No | The y coordinate to be transformed. |
| positionX | number | No | Horizontal position of the transform point. |
| positionY | number | No | Vertical position of the transform point. |
| rotation | number | No | Rotation of the transform point, in radians. |
| scaleX | number | No | Horizontal scale of the transform point. |
| scaleY | number | No | Vertical scale of the transform point. |
| output | [Phaser.Math.Vector2](../class/math-vector2.md) | [Phaser.Geom.Point](../class/geom-point.md) | object | Yes |

**Returns:** [Phaser.Math.Vector2](../class/math-vector2.md), [Phaser.Geom.Point](../class/geom-point.md), object - The translated point.

> Source: [src/math/TransformXY.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/TransformXY.js#L9)  
> Since: 3.0.0

## Within

### <static> Within(a, b, tolerance)

**Description:**

Checks if the two values are within the given `tolerance` of each other.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| a | number | No | The first value to use in the calculation. |
| --- | --- | --- | --- |
| b | number | No | The second value to use in the calculation. |
| tolerance | number | No | The tolerance. Anything equal to or less than this value is considered as being within range. |

**Returns:** boolean - Returns `true` if `a` is less than or equal to the tolerance of `b`.

> Source: [src/math/Within.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Within.js#L7)  
> Since: 3.0.0

## Wrap

### <static> Wrap(value, min, max)

**Description:**

Wrap the given `value` between `min` and `max`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The value to wrap. |
| --- | --- | --- | --- |
| min | number | No | The minimum value. |
| max | number | No | The maximum value. |

**Returns:** number - The wrapped value.

> Source: [src/math/Wrap.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Wrap.js#L7)  
> Since: 3.0.0

# Phaser.Math.Distance

## Between

### <static> Between(x1, y1, x2, y2)

**Description:**

Calculate the distance between two sets of coordinates (points).

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x1 | number | No | The x coordinate of the first point. |
| --- | --- | --- | --- |
| y1 | number | No | The y coordinate of the first point. |
| x2 | number | No | The x coordinate of the second point. |
| y2 | number | No | The y coordinate of the second point. |

**Returns:** number - The distance between each point.

> Source: [src/math/distance/DistanceBetween.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/distance/DistanceBetween.js#L7)  
> Since: 3.0.0

## BetweenPoints

### <static> BetweenPoints(a, b)

**Description:**

Calculate the distance between two points.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| a | [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) | No | The first point. |
| --- | --- | --- | --- |
| b | [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) | No | The second point. |

**Returns:** number - The distance between the points.

> Source: [src/math/distance/DistanceBetweenPoints.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/distance/DistanceBetweenPoints.js#L7)  
> Since: 3.22.0

## BetweenPointsSquared

### <static> BetweenPointsSquared(a, b)

**Description:**

Calculate the squared distance between two points.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| a | [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) | No | The first point. |
| --- | --- | --- | --- |
| b | [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) | No | The second point. |

**Returns:** number - The squared distance between the points.

> Source: [src/math/distance/DistanceBetweenPointsSquared.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/distance/DistanceBetweenPointsSquared.js#L7)  
> Since: 3.22.0

## Chebyshev

### <static> Chebyshev(x1, y1, x2, y2)

**Description:**

Calculate the Chebyshev distance between two sets of coordinates (points).

Chebyshev distance (or chessboard distance) is the maximum of the horizontal and vertical distances.

It's the effective distance when movement can be horizontal, vertical, or diagonal.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x1 | number | No | The x coordinate of the first point. |
| --- | --- | --- | --- |
| y1 | number | No | The y coordinate of the first point. |
| x2 | number | No | The x coordinate of the second point. |
| y2 | number | No | The y coordinate of the second point. |

**Returns:** number - The distance between each point.

> Source: [src/math/distance/DistanceChebyshev.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/distance/DistanceChebyshev.js#L7)  
> Since: 3.22.0

## Power

### <static> Power(x1, y1, x2, y2, pow)

**Description:**

Calculate the distance between two sets of coordinates (points) to the power of `pow`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x1 | number | No | The x coordinate of the first point. |
| --- | --- | --- | --- |
| y1 | number | No | The y coordinate of the first point. |
| x2 | number | No | The x coordinate of the second point. |
| y2 | number | No | The y coordinate of the second point. |
| pow | number | No | The exponent. |

**Returns:** number - The distance between each point.

> Source: [src/math/distance/DistancePower.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/distance/DistancePower.js#L7)  
> Since: 3.0.0

## Snake

### <static> Snake(x1, y1, x2, y2)

**Description:**

Calculate the snake distance between two sets of coordinates (points).

Snake distance (rectilinear distance, Manhattan distance) is the sum of the horizontal and vertical distances.

It's the effective distance when movement is allowed only horizontally or vertically (but not both).

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x1 | number | No | The x coordinate of the first point. |
| --- | --- | --- | --- |
| y1 | number | No | The y coordinate of the first point. |
| x2 | number | No | The x coordinate of the second point. |
| y2 | number | No | The y coordinate of the second point. |

**Returns:** number - The distance between each point.

> Source: [src/math/distance/DistanceSnake.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/distance/DistanceSnake.js#L7)  
> Since: 3.22.0

## Squared

### <static> Squared(x1, y1, x2, y2)

**Description:**

Calculate the distance between two sets of coordinates (points), squared.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x1 | number | No | The x coordinate of the first point. |
| --- | --- | --- | --- |
| y1 | number | No | The y coordinate of the first point. |
| x2 | number | No | The x coordinate of the second point. |
| y2 | number | No | The y coordinate of the second point. |

**Returns:** number - The distance between each point, squared.

> Source: [src/math/distance/DistanceSquared.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/distance/DistanceSquared.js#L7)  
> Since: 3.0.0

# Phaser.Math.Easing.Back

## In

### <static> In(v, [overshoot])

**Description:**

Back ease-in.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| v | number | No |  | The value to be tweened. |
| --- | --- | --- | --- | --- |
| overshoot | number | Yes | 1.70158 | The overshoot amount. |

**Returns:** number - The tweened value.

> Source: [src/math/easing/back/In.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/easing/back/In.js#L7)  
> Since: 3.0.0

## InOut

### <static> InOut(v, [overshoot])

**Description:**

Back ease-in/out.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| v | number | No |  | The value to be tweened. |
| --- | --- | --- | --- | --- |
| overshoot | number | Yes | 1.70158 | The overshoot amount. |

**Returns:** number - The tweened value.

> Source: [src/math/easing/back/InOut.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/easing/back/InOut.js#L7)  
> Since: 3.0.0

## Out

### <static> Out(v, [overshoot])

**Description:**

Back ease-out.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| v | number | No |  | The value to be tweened. |
| --- | --- | --- | --- | --- |
| overshoot | number | Yes | 1.70158 | The overshoot amount. |

**Returns:** number - The tweened value.

> Source: [src/math/easing/back/Out.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/easing/back/Out.js#L7)  
> Since: 3.0.0

# Phaser.Math.Easing.Bounce

## In

### <static> In(v)

**Description:**

Bounce ease-in.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| v | number | No | The value to be tweened. |
| --- | --- | --- | --- |

**Returns:** number - The tweened value.

> Source: [src/math/easing/bounce/In.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/easing/bounce/In.js#L7)  
> Since: 3.0.0

## InOut

### <static> InOut(v)

**Description:**

Bounce ease-in/out.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| v | number | No | The value to be tweened. |
| --- | --- | --- | --- |

**Returns:** number - The tweened value.

> Source: [src/math/easing/bounce/InOut.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/easing/bounce/InOut.js#L7)  
> Since: 3.0.0

## Out

### <static> Out(v)

**Description:**

Bounce ease-out.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| v | number | No | The value to be tweened. |
| --- | --- | --- | --- |

**Returns:** number - The tweened value.

> Source: [src/math/easing/bounce/Out.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/easing/bounce/Out.js#L7)  
> Since: 3.0.0

# Phaser.Math.Easing.Circular

## In

### <static> In(v)

**Description:**

Circular ease-in.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| v | number | No | The value to be tweened. |
| --- | --- | --- | --- |

**Returns:** number - The tweened value.

> Source: [src/math/easing/circular/In.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/easing/circular/In.js#L7)  
> Since: 3.0.0

## InOut

### <static> InOut(v)

**Description:**

Circular ease-in/out.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| v | number | No | The value to be tweened. |
| --- | --- | --- | --- |

**Returns:** number - The tweened value.

> Source: [src/math/easing/circular/InOut.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/easing/circular/InOut.js#L7)  
> Since: 3.0.0

## Out

### <static> Out(v)

**Description:**

Circular ease-out.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| v | number | No | The value to be tweened. |
| --- | --- | --- | --- |

**Returns:** number - The tweened value.

> Source: [src/math/easing/circular/Out.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/easing/circular/Out.js#L7)  
> Since: 3.0.0

# Phaser.Math.Easing.Cubic

## In

### <static> In(v)

**Description:**

Cubic ease-in.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| v | number | No | The value to be tweened. |
| --- | --- | --- | --- |

**Returns:** number - The tweened value.

> Source: [src/math/easing/cubic/In.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/easing/cubic/In.js#L7)  
> Since: 3.0.0

## InOut

### <static> InOut(v)

**Description:**

Cubic ease-in/out.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| v | number | No | The value to be tweened. |
| --- | --- | --- | --- |

**Returns:** number - The tweened value.

> Source: [src/math/easing/cubic/InOut.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/easing/cubic/InOut.js#L7)  
> Since: 3.0.0

## Out

### <static> Out(v)

**Description:**

Cubic ease-out.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| v | number | No | The value to be tweened. |
| --- | --- | --- | --- |

**Returns:** number - The tweened value.

> Source: [src/math/easing/cubic/Out.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/easing/cubic/Out.js#L7)  
> Since: 3.0.0

# Phaser.Math.Easing.Elastic

## In

### <static> In(v, [amplitude], [period])

**Description:**

Elastic ease-in.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| v | number | No |  | The value to be tweened. |
| --- | --- | --- | --- | --- |
| amplitude | number | Yes | 0.1 | The amplitude of the elastic ease. |
| period | number | Yes | 0.1 | Sets how tight the sine-wave is, where smaller values are tighter waves, which result in more cycles. |

**Returns:** number - The tweened value.

> Source: [src/math/easing/elastic/In.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/easing/elastic/In.js#L7)  
> Since: 3.0.0

## InOut

### <static> InOut(v, [amplitude], [period])

**Description:**

Elastic ease-in/out.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| v | number | No |  | The value to be tweened. |
| --- | --- | --- | --- | --- |
| amplitude | number | Yes | 0.1 | The amplitude of the elastic ease. |
| period | number | Yes | 0.1 | Sets how tight the sine-wave is, where smaller values are tighter waves, which result in more cycles. |

**Returns:** number - The tweened value.

> Source: [src/math/easing/elastic/InOut.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/easing/elastic/InOut.js#L7)  
> Since: 3.0.0

## Out

### <static> Out(v, [amplitude], [period])

**Description:**

Elastic ease-out.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| v | number | No |  | The value to be tweened. |
| --- | --- | --- | --- | --- |
| amplitude | number | Yes | 0.1 | The amplitude of the elastic ease. |
| period | number | Yes | 0.1 | Sets how tight the sine-wave is, where smaller values are tighter waves, which result in more cycles. |

**Returns:** number - The tweened value.

> Source: [src/math/easing/elastic/Out.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/easing/elastic/Out.js#L7)  
> Since: 3.0.0

# Phaser.Math.Easing.Expo

## In

### <static> In(v)

**Description:**

Exponential ease-in.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| v | number | No | The value to be tweened. |
| --- | --- | --- | --- |

**Returns:** number - The tweened value.

> Source: [src/math/easing/expo/In.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/easing/expo/In.js#L7)  
> Since: 3.0.0

## InOut

### <static> InOut(v)

**Description:**

Exponential ease-in/out.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| v | number | No | The value to be tweened. |
| --- | --- | --- | --- |

**Returns:** number - The tweened value.

> Source: [src/math/easing/expo/InOut.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/easing/expo/InOut.js#L7)  
> Since: 3.0.0

## Out

### <static> Out(v)

**Description:**

Exponential ease-out.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| v | number | No | The value to be tweened. |
| --- | --- | --- | --- |

**Returns:** number - The tweened value.

> Source: [src/math/easing/expo/Out.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/easing/expo/Out.js#L7)  
> Since: 3.0.0

# Phaser.Math.Easing

## Linear

### <static> Linear(v)

**Description:**

Linear easing (no variation).

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| v | number | No | The value to be tweened. |
| --- | --- | --- | --- |

**Returns:** number - The tweened value.

> Source: [src/math/easing/linear/Linear.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/easing/linear/Linear.js#L7)  
> Since: 3.0.0

## Stepped

### <static> Stepped(v, [steps])

**Description:**

Stepped easing.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| v | number | No |  | The value to be tweened. |
| --- | --- | --- | --- | --- |
| steps | number | Yes | 1 | The number of steps in the ease. |

**Returns:** number - The tweened value.

> Source: [src/math/easing/stepped/Stepped.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/easing/stepped/Stepped.js#L7)  
> Since: 3.0.0

# Phaser.Math.Easing.Quadratic

## In

### <static> In(v)

**Description:**

Quadratic ease-in.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| v | number | No | The value to be tweened. |
| --- | --- | --- | --- |

**Returns:** number - The tweened value.

> Source: [src/math/easing/quadratic/In.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/easing/quadratic/In.js#L7)  
> Since: 3.0.0

## InOut

### <static> InOut(v)

**Description:**

Quadratic ease-in/out.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| v | number | No | The value to be tweened. |
| --- | --- | --- | --- |

**Returns:** number - The tweened value.

> Source: [src/math/easing/quadratic/InOut.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/easing/quadratic/InOut.js#L7)  
> Since: 3.0.0

## Out

### <static> Out(v)

**Description:**

Quadratic ease-out.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| v | number | No | The value to be tweened. |
| --- | --- | --- | --- |

**Returns:** number - The tweened value.

> Source: [src/math/easing/quadratic/Out.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/easing/quadratic/Out.js#L7)  
> Since: 3.0.0

# Phaser.Math.Easing.Quartic

## In

### <static> In(v)

**Description:**

Quartic ease-in.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| v | number | No | The value to be tweened. |
| --- | --- | --- | --- |

**Returns:** number - The tweened value.

> Source: [src/math/easing/quartic/In.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/easing/quartic/In.js#L7)  
> Since: 3.0.0

## InOut

### <static> InOut(v)

**Description:**

Quartic ease-in/out.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| v | number | No | The value to be tweened. |
| --- | --- | --- | --- |

**Returns:** number - The tweened value.

> Source: [src/math/easing/quartic/InOut.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/easing/quartic/InOut.js#L7)  
> Since: 3.0.0

## Out

### <static> Out(v)

**Description:**

Quartic ease-out.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| v | number | No | The value to be tweened. |
| --- | --- | --- | --- |

**Returns:** number - The tweened value.

> Source: [src/math/easing/quartic/Out.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/easing/quartic/Out.js#L7)  
> Since: 3.0.0

# Phaser.Math.Easing.Quintic

## In

### <static> In(v)

**Description:**

Quintic ease-in.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| v | number | No | The value to be tweened. |
| --- | --- | --- | --- |

**Returns:** number - The tweened value.

> Source: [src/math/easing/quintic/In.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/easing/quintic/In.js#L7)  
> Since: 3.0.0

## InOut

### <static> InOut(v)

**Description:**

Quintic ease-in/out.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| v | number | No | The value to be tweened. |
| --- | --- | --- | --- |

**Returns:** number - The tweened value.

> Source: [src/math/easing/quintic/InOut.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/easing/quintic/InOut.js#L7)  
> Since: 3.0.0

## Out

### <static> Out(v)

**Description:**

Quintic ease-out.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| v | number | No | The value to be tweened. |
| --- | --- | --- | --- |

**Returns:** number - The tweened value.

> Source: [src/math/easing/quintic/Out.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/easing/quintic/Out.js#L7)  
> Since: 3.0.0

# Phaser.Math.Easing.Sine

## In

### <static> In(v)

**Description:**

Sinusoidal ease-in.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| v | number | No | The value to be tweened. |
| --- | --- | --- | --- |

**Returns:** number - The tweened value.

> Source: [src/math/easing/sine/In.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/easing/sine/In.js#L7)  
> Since: 3.0.0

## InOut

### <static> InOut(v)

**Description:**

Sinusoidal ease-in/out.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| v | number | No | The value to be tweened. |
| --- | --- | --- | --- |

**Returns:** number - The tweened value.

> Source: [src/math/easing/sine/InOut.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/easing/sine/InOut.js#L7)  
> Since: 3.0.0

## Out

### <static> Out(v)

**Description:**

Sinusoidal ease-out.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| v | number | No | The value to be tweened. |
| --- | --- | --- | --- |

**Returns:** number - The tweened value.

> Source: [src/math/easing/sine/Out.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/easing/sine/Out.js#L7)  
> Since: 3.0.0

# Phaser.Math.Fuzzy

## Ceil

### <static> Ceil(value, [epsilon])

**Description:**

Calculate the fuzzy ceiling of the given value.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| value | number | No |  | The value. |
| --- | --- | --- | --- | --- |
| epsilon | number | Yes | 0.0001 | The epsilon. |

**Returns:** number - The fuzzy ceiling of the value.

> Source: [src/math/fuzzy/Ceil.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/fuzzy/Ceil.js#L7)  
> Since: 3.0.0

## Equal

### <static> Equal(a, b, [epsilon])

**Description:**

Check whether the given values are fuzzily equal.

Two numbers are fuzzily equal if their difference is less than `epsilon`.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| a | number | No |  | The first value. |
| --- | --- | --- | --- | --- |
| b | number | No |  | The second value. |
| epsilon | number | Yes | 0.0001 | The epsilon. |

**Returns:** boolean - `true` if the values are fuzzily equal, otherwise `false`.

> Source: [src/math/fuzzy/Equal.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/fuzzy/Equal.js#L7)  
> Since: 3.0.0

## Floor

### <static> Floor(value, [epsilon])

**Description:**

Calculate the fuzzy floor of the given value.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| value | number | No |  | The value. |
| --- | --- | --- | --- | --- |
| epsilon | number | Yes | 0.0001 | The epsilon. |

**Returns:** number - The floor of the value.

> Source: [src/math/fuzzy/Floor.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/fuzzy/Floor.js#L7)  
> Since: 3.0.0

## GreaterThan

### <static> GreaterThan(a, b, [epsilon])

**Description:**

Check whether `a` is fuzzily greater than `b`.

`a` is fuzzily greater than `b` if it is more than `b - epsilon`.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| a | number | No |  | The first value. |
| --- | --- | --- | --- | --- |
| b | number | No |  | The second value. |
| epsilon | number | Yes | 0.0001 | The epsilon. |

**Returns:** boolean - `true` if `a` is fuzzily greater than than `b`, otherwise `false`.

> Source: [src/math/fuzzy/GreaterThan.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/fuzzy/GreaterThan.js#L7)  
> Since: 3.0.0

## LessThan

### <static> LessThan(a, b, [epsilon])

**Description:**

Check whether `a` is fuzzily less than `b`.

`a` is fuzzily less than `b` if it is less than `b + epsilon`.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| a | number | No |  | The first value. |
| --- | --- | --- | --- | --- |
| b | number | No |  | The second value. |
| epsilon | number | Yes | 0.0001 | The epsilon. |

**Returns:** boolean - `true` if `a` is fuzzily less than `b`, otherwise `false`.

> Source: [src/math/fuzzy/LessThan.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/fuzzy/LessThan.js#L7)  
> Since: 3.0.0

# Phaser.Math.Interpolation

## Bezier

### <static> Bezier(v, k)

**Description:**

A bezier interpolation method.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| v | Array.<number> | No | The input array of values to interpolate between. |
| --- | --- | --- | --- |
| k | number | No | The percentage of interpolation, between 0 and 1. |

**Returns:** number - The interpolated value.

> Source: [src/math/interpolation/BezierInterpolation.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/interpolation/BezierInterpolation.js#L9)  
> Since: 3.0.0

## CatmullRom

### <static> CatmullRom(v, k)

**Description:**

A Catmull-Rom interpolation method.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| v | Array.<number> | No | The input array of values to interpolate between. |
| --- | --- | --- | --- |
| k | number | No | The percentage of interpolation, between 0 and 1. |

**Returns:** number - The interpolated value.

> Source: [src/math/interpolation/CatmullRomInterpolation.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/interpolation/CatmullRomInterpolation.js#L9)  
> Since: 3.0.0

## CubicBezier

### <static> CubicBezier(t, p0, p1, p2, p3)

**Description:**

A cubic bezier interpolation method.

<https://medium.com/@adrian_cooney/bezier-interpolation-13b68563313a>

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| t | number | No | The percentage of interpolation, between 0 and 1. |
| --- | --- | --- | --- |
| p0 | number | No | The start point. |
| p1 | number | No | The first control point. |
| p2 | number | No | The second control point. |
| p3 | number | No | The end point. |

**Returns:** number - The interpolated value.

> Source: [src/math/interpolation/CubicBezierInterpolation.js#L43](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/interpolation/CubicBezierInterpolation.js#L43)  
> Since: 3.0.0

## Linear

### <static> Linear(v, k)

**Description:**

A linear interpolation method.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| v | Array.<number> | No | The input array of values to interpolate between. |
| --- | --- | --- | --- |
| k | number | No | The percentage of interpolation, between 0 and 1. |

**Returns:** number - The interpolated value.

> Source: [src/math/interpolation/LinearInterpolation.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/interpolation/LinearInterpolation.js#L9)  
> Since: 3.0.0

## QuadraticBezier

### <static> QuadraticBezier(t, p0, p1, p2)

**Description:**

A quadratic bezier interpolation method.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| t | number | No | The percentage of interpolation, between 0 and 1. |
| --- | --- | --- | --- |
| p0 | number | No | The start point. |
| p1 | number | No | The control point. |
| p2 | number | No | The end point. |

**Returns:** number - The interpolated value.

> Source: [src/math/interpolation/QuadraticBezierInterpolation.js#L35](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/interpolation/QuadraticBezierInterpolation.js#L35)  
> Since: 3.2.0

## SmootherStep

### <static> SmootherStep(t, min, max)

**Description:**

A Smoother Step interpolation method.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| t | number | No | The percentage of interpolation, between 0 and 1. |
| --- | --- | --- | --- |
| min | number | No | The minimum value, also known as the 'left edge', assumed smaller than the 'right edge'. |
| max | number | No | The maximum value, also known as the 'right edge', assumed greater than the 'left edge'. |

**Returns:** number - The interpolated value.

> Source: [src/math/interpolation/SmootherStepInterpolation.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/interpolation/SmootherStepInterpolation.js#L9)  
> Since: 3.9.0

## SmoothStep

### <static> SmoothStep(t, min, max)

**Description:**

A Smooth Step interpolation method.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| t | number | No | The percentage of interpolation, between 0 and 1. |
| --- | --- | --- | --- |
| min | number | No | The minimum value, also known as the 'left edge', assumed smaller than the 'right edge'. |
| max | number | No | The maximum value, also known as the 'right edge', assumed greater than the 'left edge'. |

**Returns:** number - The interpolated value.

> Source: [src/math/interpolation/SmoothStepInterpolation.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/interpolation/SmoothStepInterpolation.js#L9)  
> Since: 3.9.0

# Phaser.Math.Pow2

## GetNext

### <static> GetNext(value)

**Description:**

Returns the nearest power of 2 to the given `value`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The value. |
| --- | --- | --- | --- |

**Returns:** number - The nearest power of 2 to `value`.

> Source: [src/math/pow2/GetPowerOfTwo.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/pow2/GetPowerOfTwo.js#L7)  
> Since: 3.0.0

## IsSize

### <static> IsSize(width, height)

**Description:**

Checks if the given `width` and `height` are a power of two.

Useful for checking texture dimensions.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| width | number | No | The width. |
| --- | --- | --- | --- |
| height | number | No | The height. |

**Returns:** boolean - `true` if `width` and `height` are a power of two, otherwise `false`.

> Source: [src/math/pow2/IsSizePowerOfTwo.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/pow2/IsSizePowerOfTwo.js#L7)  
> Since: 3.0.0

## IsValue

### <static> IsValue(value)

**Description:**

Tests the value and returns `true` if it is a power of two.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The value to check if it's a power of two. |
| --- | --- | --- | --- |

**Returns:** boolean - Returns `true` if `value` is a power of two, otherwise `false`.

> Source: [src/math/pow2/IsValuePowerOfTwo.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/pow2/IsValuePowerOfTwo.js#L7)  
> Since: 3.0.0

# Phaser.Math.Snap

## Ceil

### <static> Ceil(value, gap, [start], [divide])

**Description:**

Snap a value to nearest grid slice, using ceil.

Example: if you have an interval gap of `5` and a position of `12`... you will snap to `15`.

As will `14` snap to `15`... but `16` will snap to `20`.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| value | number | No |  | The value to snap. |
| --- | --- | --- | --- | --- |
| gap | number | No |  | The interval gap of the grid. |
| start | number | Yes | 0 | Optional starting offset for gap. |
| divide | boolean | Yes | false | If `true` it will divide the snapped value by the gap before returning. |

**Returns:** number - The snapped value.

> Source: [src/math/snap/SnapCeil.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/snap/SnapCeil.js#L7)  
> Since: 3.0.0

## Floor

### <static> Floor(value, gap, [start], [divide])

**Description:**

Snap a value to nearest grid slice, using floor.

Example: if you have an interval gap of `5` and a position of `12`... you will snap to `10`.

As will `14` snap to `10`... but `16` will snap to `15`.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| value | number | No |  | The value to snap. |
| --- | --- | --- | --- | --- |
| gap | number | No |  | The interval gap of the grid. |
| start | number | Yes | 0 | Optional starting offset for gap. |
| divide | boolean | Yes | false | If `true` it will divide the snapped value by the gap before returning. |

**Returns:** number - The snapped value.

> Source: [src/math/snap/SnapFloor.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/snap/SnapFloor.js#L7)  
> Since: 3.0.0

## To

### <static> To(value, gap, [start], [divide])

**Description:**

Snap a value to nearest grid slice, using rounding.

Example: if you have an interval gap of `5` and a position of `12`... you will snap to `10` whereas `14` will snap to `15`.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| value | number | No |  | The value to snap. |
| --- | --- | --- | --- | --- |
| gap | number | No |  | The interval gap of the grid. |
| start | number | Yes | 0 | Optional starting offset for gap. |
| divide | boolean | Yes | false | If `true` it will divide the snapped value by the gap before returning. |

**Returns:** number - The snapped value.

> Source: [src/math/snap/SnapTo.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/snap/SnapTo.js#L7)  
> Since: 3.0.0

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Phaser.Math.Angle](#phasermathangle)

  + [Between](#between)

    - [<static> Between(x1, y1, x2, y2)](#static-betweenx1-y1-x2-y2)
  + [BetweenPoints](#betweenpoints)

    - [<static> BetweenPoints(point1, point2)](#static-betweenpointspoint1-point2)
  + [BetweenPointsY](#betweenpointsy)

    - [<static> BetweenPointsY(point1, point2)](#static-betweenpointsypoint1-point2)
  + [BetweenY](#betweeny)

    - [<static> BetweenY(x1, y1, x2, y2)](#static-betweenyx1-y1-x2-y2)
  + [CounterClockwise](#counterclockwise)

    - [<static> CounterClockwise(angle)](#static-counterclockwiseangle)
  + [Normalize](#normalize)

    - [<static> Normalize(angle)](#static-normalizeangle)
  + [Random](#random)

    - [<static> Random()](#static-random)
  + [RandomDegrees](#randomdegrees)

    - [<static> RandomDegrees()](#static-randomdegrees)
  + [Reverse](#reverse)

    - [<static> Reverse(angle)](#static-reverseangle)
  + [RotateTo](#rotateto)

    - [<static> RotateTo(currentAngle, targetAngle, [lerp])](#static-rotatetocurrentangle-targetangle-lerp)
  + [ShortestBetween](#shortestbetween)

    - [<static> ShortestBetween(angle1, angle2)](#static-shortestbetweenangle1-angle2)
  + [Wrap](#wrap)

    - [<static> Wrap(angle)](#static-wrapangle)
  + [WrapDegrees](#wrapdegrees)

    - [<static> WrapDegrees(angle)](#static-wrapdegreesangle)
  + [Average](#average)

    - [<static> Average(values)](#static-averagevalues)
  + [Bernstein](#bernstein)

    - [<static> Bernstein(n, i)](#static-bernsteinn-i)
  + [Between](#between-1)

    - [<static> Between(min, max)](#static-betweenmin-max)
  + [CatmullRom](#catmullrom)

    - [<static> CatmullRom(t, p0, p1, p2, p3)](#static-catmullromt-p0-p1-p2-p3)
  + [CeilTo](#ceilto)

    - [<static> CeilTo(value, [place], [base])](#static-ceiltovalue-place-base)
  + [Clamp](#clamp)

    - [<static> Clamp(value, min, max)](#static-clampvalue-min-max)
  + [DegToRad](#degtorad)

    - [<static> DegToRad(degrees)](#static-degtoraddegrees)
  + [Difference](#difference)

    - [<static> Difference(a, b)](#static-differencea-b)
  + [Factorial](#factorial)

    - [<static> Factorial(value)](#static-factorialvalue)
  + [FloatBetween](#floatbetween)

    - [<static> FloatBetween(min, max)](#static-floatbetweenmin-max)
  + [FloorTo](#floorto)

    - [<static> FloorTo(value, [place], [base])](#static-floortovalue-place-base)
  + [FromPercent](#frompercent)

    - [<static> FromPercent(percent, min, [max])](#static-frompercentpercent-min-max)
  + [GetSpeed](#getspeed)

    - [<static> GetSpeed(distance, time)](#static-getspeeddistance-time)
  + [IsEven](#iseven)

    - [<static> IsEven(value)](#static-isevenvalue)
  + [IsEvenStrict](#isevenstrict)

    - [<static> IsEvenStrict(value)](#static-isevenstrictvalue)
  + [Linear](#linear)

    - [<static> Linear(p0, p1, t)](#static-linearp0-p1-t)
  + [LinearXY](#linearxy)

    - [<static> LinearXY(vector1, vector2, [t])](#static-linearxyvector1-vector2-t)
  + [MaxAdd](#maxadd)

    - [<static> MaxAdd(value, amount, max)](#static-maxaddvalue-amount-max)
  + [Median](#median)

    - [<static> Median(values)](#static-medianvalues)
  + [MinSub](#minsub)

    - [<static> MinSub(value, amount, min)](#static-minsubvalue-amount-min)
  + [Percent](#percent)

    - [<static> Percent(value, min, [max], [upperMax])](#static-percentvalue-min-max-uppermax)
  + [RadToDeg](#radtodeg)

    - [<static> RadToDeg(radians)](#static-radtodegradians)
  + [RandomXY](#randomxy)

    - [<static> RandomXY(vector, [scale])](#static-randomxyvector-scale)
  + [RandomXYZ](#randomxyz)

    - [<static> RandomXYZ(vec3, [radius])](#static-randomxyzvec3-radius)
  + [RandomXYZW](#randomxyzw)

    - [<static> RandomXYZW(vec4, [scale])](#static-randomxyzwvec4-scale)
  + [Rotate](#rotate)

    - [<static> Rotate(point, angle)](#static-rotatepoint-angle)
  + [RotateAround](#rotatearound)

    - [<static> RotateAround(point, x, y, angle)](#static-rotatearoundpoint-x-y-angle)
  + [RotateAroundDistance](#rotatearounddistance)

    - [<static> RotateAroundDistance(point, x, y, angle, distance)](#static-rotatearounddistancepoint-x-y-angle-distance)
  + [RotateTo](#rotateto-1)

    - [<static> RotateTo(point, x, y, angle, distance)](#static-rotatetopoint-x-y-angle-distance)
  + [RotateVec3](#rotatevec3)

    - [<static> RotateVec3(vec, axis, radians)](#static-rotatevec3vec-axis-radians)
  + [RoundAwayFromZero](#roundawayfromzero)

    - [<static> RoundAwayFromZero(value)](#static-roundawayfromzerovalue)
  + [RoundTo](#roundto)

    - [<static> RoundTo(value, [place], [base])](#static-roundtovalue-place-base)
  + [SinCosTableGenerator](#sincostablegenerator)

    - [<static> SinCosTableGenerator(length, [sinAmp], [cosAmp], [frequency])](#static-sincostablegeneratorlength-sinamp-cosamp-frequency)
  + [SmootherStep](#smootherstep)

    - [<static> SmootherStep(x, min, max)](#static-smootherstepx-min-max)
  + [SmoothStep](#smoothstep)

    - [<static> SmoothStep(x, min, max)](#static-smoothstepx-min-max)
  + [ToXY](#toxy)

    - [<static> ToXY(index, width, height, [out])](#static-toxyindex-width-height-out)
  + [TransformXY](#transformxy)

    - [<static> TransformXY(x, y, positionX, positionY, rotation, scaleX, scaleY, [output])](#static-transformxyx-y-positionx-positiony-rotation-scalex-scaley-output)
  + [Within](#within)

    - [<static> Within(a, b, tolerance)](#static-withina-b-tolerance)
  + [Wrap](#wrap-1)

    - [<static> Wrap(value, min, max)](#static-wrapvalue-min-max)
* [Phaser.Math.Distance](#phasermathdistance)

  + [Between](#between-2)

    - [<static> Between(x1, y1, x2, y2)](#static-betweenx1-y1-x2-y2-1)
  + [BetweenPoints](#betweenpoints-1)

    - [<static> BetweenPoints(a, b)](#static-betweenpointsa-b)
  + [BetweenPointsSquared](#betweenpointssquared)

    - [<static> BetweenPointsSquared(a, b)](#static-betweenpointssquareda-b)
  + [Chebyshev](#chebyshev)

    - [<static> Chebyshev(x1, y1, x2, y2)](#static-chebyshevx1-y1-x2-y2)
  + [Power](#power)

    - [<static> Power(x1, y1, x2, y2, pow)](#static-powerx1-y1-x2-y2-pow)
  + [Snake](#snake)

    - [<static> Snake(x1, y1, x2, y2)](#static-snakex1-y1-x2-y2)
  + [Squared](#squared)

    - [<static> Squared(x1, y1, x2, y2)](#static-squaredx1-y1-x2-y2)
* [Phaser.Math.Easing.Back](#phasermatheasingback)

  + [In](#in)

    - [<static> In(v, [overshoot])](#static-inv-overshoot)
  + [InOut](#inout)

    - [<static> InOut(v, [overshoot])](#static-inoutv-overshoot)
  + [Out](#out)

    - [<static> Out(v, [overshoot])](#static-outv-overshoot)
* [Phaser.Math.Easing.Bounce](#phasermatheasingbounce)

  + [In](#in-1)

    - [<static> In(v)](#static-inv)
  + [InOut](#inout-1)

    - [<static> InOut(v)](#static-inoutv)
  + [Out](#out-1)

    - [<static> Out(v)](#static-outv)
* [Phaser.Math.Easing.Circular](#phasermatheasingcircular)

  + [In](#in-2)

    - [<static> In(v)](#static-inv-1)
  + [InOut](#inout-2)

    - [<static> InOut(v)](#static-inoutv-1)
  + [Out](#out-2)

    - [<static> Out(v)](#static-outv-1)
* [Phaser.Math.Easing.Cubic](#phasermatheasingcubic)

  + [In](#in-3)

    - [<static> In(v)](#static-inv-2)
  + [InOut](#inout-3)

    - [<static> InOut(v)](#static-inoutv-2)
  + [Out](#out-3)

    - [<static> Out(v)](#static-outv-2)
* [Phaser.Math.Easing.Elastic](#phasermatheasingelastic)

  + [In](#in-4)

    - [<static> In(v, [amplitude], [period])](#static-inv-amplitude-period)
  + [InOut](#inout-4)

    - [<static> InOut(v, [amplitude], [period])](#static-inoutv-amplitude-period)
  + [Out](#out-4)

    - [<static> Out(v, [amplitude], [period])](#static-outv-amplitude-period)
* [Phaser.Math.Easing.Expo](#phasermatheasingexpo)

  + [In](#in-5)

    - [<static> In(v)](#static-inv-3)
  + [InOut](#inout-5)

    - [<static> InOut(v)](#static-inoutv-3)
  + [Out](#out-5)

    - [<static> Out(v)](#static-outv-3)
* [Phaser.Math.Easing](#phasermatheasing)

  + [Linear](#linear-1)

    - [<static> Linear(v)](#static-linearv)
  + [Stepped](#stepped)

    - [<static> Stepped(v, [steps])](#static-steppedv-steps)
* [Phaser.Math.Easing.Quadratic](#phasermatheasingquadratic)

  + [In](#in-6)

    - [<static> In(v)](#static-inv-4)
  + [InOut](#inout-6)

    - [<static> InOut(v)](#static-inoutv-4)
  + [Out](#out-6)

    - [<static> Out(v)](#static-outv-4)
* [Phaser.Math.Easing.Quartic](#phasermatheasingquartic)

  + [In](#in-7)

    - [<static> In(v)](#static-inv-5)
  + [InOut](#inout-7)

    - [<static> InOut(v)](#static-inoutv-5)
  + [Out](#out-7)

    - [<static> Out(v)](#static-outv-5)
* [Phaser.Math.Easing.Quintic](#phasermatheasingquintic)

  + [In](#in-8)

    - [<static> In(v)](#static-inv-6)
  + [InOut](#inout-8)

    - [<static> InOut(v)](#static-inoutv-6)
  + [Out](#out-8)

    - [<static> Out(v)](#static-outv-6)
* [Phaser.Math.Easing.Sine](#phasermatheasingsine)

  + [In](#in-9)

    - [<static> In(v)](#static-inv-7)
  + [InOut](#inout-9)

    - [<static> InOut(v)](#static-inoutv-7)
  + [Out](#out-9)

    - [<static> Out(v)](#static-outv-7)
* [Phaser.Math.Fuzzy](#phasermathfuzzy)

  + [Ceil](#ceil)

    - [<static> Ceil(value, [epsilon])](#static-ceilvalue-epsilon)
  + [Equal](#equal)

    - [<static> Equal(a, b, [epsilon])](#static-equala-b-epsilon)
  + [Floor](#floor)

    - [<static> Floor(value, [epsilon])](#static-floorvalue-epsilon)
  + [GreaterThan](#greaterthan)

    - [<static> GreaterThan(a, b, [epsilon])](#static-greaterthana-b-epsilon)
  + [LessThan](#lessthan)

    - [<static> LessThan(a, b, [epsilon])](#static-lessthana-b-epsilon)
* [Phaser.Math.Interpolation](#phasermathinterpolation)

  + [Bezier](#bezier)

    - [<static> Bezier(v, k)](#static-bezierv-k)
  + [CatmullRom](#catmullrom-1)

    - [<static> CatmullRom(v, k)](#static-catmullromv-k)
  + [CubicBezier](#cubicbezier)

    - [<static> CubicBezier(t, p0, p1, p2, p3)](#static-cubicbeziert-p0-p1-p2-p3)
  + [Linear](#linear-2)

    - [<static> Linear(v, k)](#static-linearv-k)
  + [QuadraticBezier](#quadraticbezier)

    - [<static> QuadraticBezier(t, p0, p1, p2)](#static-quadraticbeziert-p0-p1-p2)
  + [SmootherStep](#smootherstep-1)

    - [<static> SmootherStep(t, min, max)](#static-smootherstept-min-max)
  + [SmoothStep](#smoothstep-1)

    - [<static> SmoothStep(t, min, max)](#static-smoothstept-min-max)
* [Phaser.Math.Pow2](#phasermathpow2)

  + [GetNext](#getnext)

    - [<static> GetNext(value)](#static-getnextvalue)
  + [IsSize](#issize)

    - [<static> IsSize(width, height)](#static-issizewidth-height)
  + [IsValue](#isvalue)

    - [<static> IsValue(value)](#static-isvaluevalue)
* [Phaser.Math.Snap](#phasermathsnap)

  + [Ceil](#ceil-1)

    - [<static> Ceil(value, gap, [start], [divide])](#static-ceilvalue-gap-start-divide)
  + [Floor](#floor-1)

    - [<static> Floor(value, gap, [start], [divide])](#static-floorvalue-gap-start-divide)
  + [To](#to)

    - [<static> To(value, gap, [start], [divide])](#static-tovalue-gap-start-divide)

Back to top

©2025[Phaser](https://docs.phaser.io)