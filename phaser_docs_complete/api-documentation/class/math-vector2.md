# Vector2

Phaser.Math.Vector2

A representation of a vector in 2D space.

A two-component vector.

**Constructor**

`new Vector2([x], [y])`

**Parameters**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) | Yes | 0 | The x component, or an object with `x` and `y` properties. |
| --- | --- | --- | --- | --- |
| y | number | Yes | "x" | The y component. |

---

**Scope**: static

> Source: [src/math/Vector2.js#L13](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector2.js#L13)  
> Since: 3.0.0

# Public Members

## x

### x: number

**Description:**

The x component of this Vector.

> Source: [src/math/Vector2.js#L33](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector2.js#L33)  
> Since: 3.0.0

---

## y

### y: number

**Description:**

The y component of this Vector.

> Source: [src/math/Vector2.js#L43](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector2.js#L43)  
> Since: 3.0.0

---

# Public Methods

## add

### <instance> add(src)

**Description:**

Add a given Vector to this Vector. Addition is component-wise.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| src | [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) | No | The Vector to add to this Vector. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Vector2](math-vector2.md) - This Vector2.

> Source: [src/math/Vector2.js#L244](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector2.js#L244)  
> Since: 3.0.0

---

## angle

### <instance> angle()

**Description:**

Calculate the angle between this Vector and the positive x-axis, in radians.

**Returns:** number - The angle between this Vector, and the positive x-axis, given in radians.

> Source: [src/math/Vector2.js#L207](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector2.js#L207)  
> Since: 3.0.0

---

## clone

### <instance> clone()

**Description:**

Make a clone of this Vector2.

**Returns:** [Phaser.Math.Vector2](math-vector2.md) - A clone of this Vector2.

> Source: [src/math/Vector2.js#L67](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector2.js#L67)  
> Since: 3.0.0

---

## copy

### <instance> copy(src)

**Description:**

Copy the components of a given Vector into this Vector.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| src | [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) | No | The Vector to copy the components from. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Vector2](math-vector2.md) - This Vector2.

> Source: [src/math/Vector2.js#L80](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector2.js#L80)  
> Since: 3.0.0

---

## cross

### <instance> cross(src)

**Description:**

Calculate the cross product of this Vector and the given Vector.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| src | [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) | No | The Vector2 to cross with this Vector2. |
| --- | --- | --- | --- |

**Returns:** number - The cross product of this Vector and the given Vector.

> Source: [src/math/Vector2.js#L523](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector2.js#L523)  
> Since: 3.0.0

---

## distance

### <instance> distance(src)

**Description:**

Calculate the distance between this Vector and the given Vector.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| src | [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) | No | The Vector to calculate the distance to. |
| --- | --- | --- | --- |

**Returns:** number - The distance from this Vector to the given Vector.

> Source: [src/math/Vector2.js#L362](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector2.js#L362)  
> Since: 3.0.0

---

## distanceSq

### <instance> distanceSq(src)

**Description:**

Calculate the distance between this Vector and the given Vector, squared.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| src | [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) | No | The Vector to calculate the distance to. |
| --- | --- | --- | --- |

**Returns:** number - The distance from this Vector to the given Vector, squared.

> Source: [src/math/Vector2.js#L380](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector2.js#L380)  
> Since: 3.0.0

---

## divide

### <instance> divide(src)

**Description:**

Perform a component-wise division between this Vector and the given Vector.

Divides this Vector by the given Vector.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| src | [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) | No | The Vector to divide this Vector by. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Vector2](math-vector2.md) - This Vector2.

> Source: [src/math/Vector2.js#L326](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector2.js#L326)  
> Since: 3.0.0

---

## dot

### <instance> dot(src)

**Description:**

Calculate the dot product of this Vector and the given Vector.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| src | [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) | No | The Vector2 to dot product with this Vector2. |
| --- | --- | --- | --- |

**Returns:** number - The dot product of this Vector and the given Vector.

> Source: [src/math/Vector2.js#L508](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector2.js#L508)  
> Since: 3.0.0

---

## equals

### <instance> equals(v)

**Description:**

Check whether this Vector is equal to a given Vector.

Performs a strict equality check against each Vector's components.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| v | [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) | No | The vector to compare with this Vector. |
| --- | --- | --- | --- |

**Returns:** boolean - Whether the given Vector is equal to this Vector.

> Source: [src/math/Vector2.js#L174](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector2.js#L174)  
> Since: 3.0.0

---

## fuzzyEquals

### <instance> fuzzyEquals(v, [epsilon])

**Description:**

Check whether this Vector is approximately equal to a given Vector.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| v | [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) | No |  | The vector to compare with this Vector. |
| --- | --- | --- | --- | --- |
| epsilon | number | Yes | 0.0001 | The tolerance value. |

**Returns:** boolean - Whether both absolute differences of the x and y components are smaller than `epsilon`.

> Source: [src/math/Vector2.js#L191](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector2.js#L191)  
> Since: 3.23.0

---

## length

### <instance> length()

**Description:**

Calculate the length (or magnitude) of this Vector.

**Returns:** number - The length of this Vector.

> Source: [src/math/Vector2.js#L398](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector2.js#L398)  
> Since: 3.0.0

---

## lengthSq

### <instance> lengthSq()

**Description:**

Calculate the length of this Vector squared.

**Returns:** number - The length of this Vector, squared.

> Source: [src/math/Vector2.js#L429](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector2.js#L429)  
> Since: 3.0.0

---

## lerp

### <instance> lerp(src, [t])

**Description:**

Linearly interpolate between this Vector and the given Vector.

Interpolates this Vector towards the given Vector.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| src | [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) | No |  | The Vector2 to interpolate towards. |
| --- | --- | --- | --- | --- |
| t | number | Yes | 0 | The interpolation percentage, between 0 and 1. |

**Returns:** [Phaser.Math.Vector2](math-vector2.md) - This Vector2.

> Source: [src/math/Vector2.js#L538](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector2.js#L538)  
> Since: 3.0.0

---

## limit

### <instance> limit(max)

**Description:**

Limit the length (or magnitude) of this Vector.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| max | number | No | The maximum length. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Vector2](math-vector2.md) - This Vector2.

> Source: [src/math/Vector2.js#L624](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector2.js#L624)  
> Since: 3.23.0

---

## mirror

### <instance> mirror(axis)

**Description:**

Reflect this Vector across another.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| axis | [Phaser.Math.Vector2](math-vector2.md) | No | A vector to reflect across. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Vector2](math-vector2.md) - This Vector2.

> Source: [src/math/Vector2.js#L663](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector2.js#L663)  
> Since: 3.23.0

---

## multiply

### <instance> multiply(src)

**Description:**

Perform a component-wise multiplication between this Vector and the given Vector.

Multiplies this Vector by the given Vector.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| src | [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) | No | The Vector to multiply this Vector by. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Vector2](math-vector2.md) - This Vector2.

> Source: [src/math/Vector2.js#L280](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector2.js#L280)  
> Since: 3.0.0

---

## negate

### <instance> negate()

**Description:**

Negate the `x` and `y` components of this Vector.

**Returns:** [Phaser.Math.Vector2](math-vector2.md) - This Vector2.

> Source: [src/math/Vector2.js#L346](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector2.js#L346)  
> Since: 3.0.0

---

## normalize

### <instance> normalize()

**Description:**

Normalize this Vector.

Makes the vector a unit length vector (magnitude of 1) in the same direction.

**Returns:** [Phaser.Math.Vector2](math-vector2.md) - This Vector2.

> Source: [src/math/Vector2.js#L445](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector2.js#L445)  
> Since: 3.0.0

---

## normalizeLeftHand

### <instance> normalizeLeftHand()

**Description:**

Rotate this Vector to its perpendicular, in the negative direction.

**Returns:** [Phaser.Math.Vector2](math-vector2.md) - This Vector2.

> Source: [src/math/Vector2.js#L490](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector2.js#L490)  
> Since: 3.23.0

---

## normalizeRightHand

### <instance> normalizeRightHand()

**Description:**

Rotate this Vector to its perpendicular, in the positive direction.

**Returns:** [Phaser.Math.Vector2](math-vector2.md) - This Vector2.

> Source: [src/math/Vector2.js#L472](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector2.js#L472)  
> Since: 3.0.0

---

## project

### <instance> project(src)

**Description:**

Project this Vector onto another.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| src | [Phaser.Math.Vector2](math-vector2.md) | No | The vector to project onto. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Vector2](math-vector2.md) - This Vector2.

> Source: [src/math/Vector2.js#L696](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector2.js#L696)  
> Since: 3.60.0

---

## reflect

### <instance> reflect(normal)

**Description:**

Reflect this Vector off a line defined by a normal.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| normal | [Phaser.Math.Vector2](math-vector2.md) | No | A vector perpendicular to the line. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Vector2](math-vector2.md) - This Vector2.

> Source: [src/math/Vector2.js#L646](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector2.js#L646)  
> Since: 3.23.0

---

## reset

### <instance> reset()

**Description:**

Make this Vector the zero vector (0, 0).

**Returns:** [Phaser.Math.Vector2](math-vector2.md) - This Vector2.

> Source: [src/math/Vector2.js#L608](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector2.js#L608)  
> Since: 3.0.0

---

## rotate

### <instance> rotate(delta)

**Description:**

Rotate this Vector by an angle amount.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| delta | number | No | The angle to rotate by, in radians. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Vector2](math-vector2.md) - This Vector2.

> Source: [src/math/Vector2.js#L678](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector2.js#L678)  
> Since: 3.23.0

---

## scale

### <instance> scale(value)

**Description:**

Scale this Vector by the given value.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The value to scale this Vector by. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Vector2](math-vector2.md) - This Vector2.

> Source: [src/math/Vector2.js#L300](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector2.js#L300)  
> Since: 3.0.0

---

## set

### <instance> set(x, [y])

**Description:**

Set the `x` and `y` components of the this Vector to the given `x` and `y` values.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | No |  | The x value to set for this Vector. |
| --- | --- | --- | --- | --- |
| y | number | Yes | "x" | The y value to set for this Vector. |

**Returns:** [Phaser.Math.Vector2](math-vector2.md) - This Vector2.

> Source: [src/math/Vector2.js#L116](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector2.js#L116)  
> Since: 3.0.0

---

## setAngle

### <instance> setAngle(angle)

**Description:**

Set the angle of this Vector.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| angle | number | No | The angle, in radians. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Vector2](math-vector2.md) - This Vector2.

> Source: [src/math/Vector2.js#L229](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector2.js#L229)  
> Since: 3.23.0

---

## setFromObject

### <instance> setFromObject(obj)

**Description:**

Set the component values of this Vector from a given Vector2Like object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| obj | [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) | No | The object containing the component values to set for this Vector. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Vector2](math-vector2.md) - This Vector2.

> Source: [src/math/Vector2.js#L98](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector2.js#L98)  
> Since: 3.0.0

---

## setLength

### <instance> setLength(length)

**Description:**

Set the length (or magnitude) of this Vector.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| length | number | No | No description provided |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Vector2](math-vector2.md) - This Vector2.

> Source: [src/math/Vector2.js#L414](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector2.js#L414)  
> Since: 3.23.0

---

## setTo

### <instance> setTo(x, [y])

**Description:**

This method is an alias for `Vector2.set`.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | No |  | The x value to set for this Vector. |
| --- | --- | --- | --- | --- |
| y | number | Yes | "x" | The y value to set for this Vector. |

**Returns:** [Phaser.Math.Vector2](math-vector2.md) - This Vector2.

> Source: [src/math/Vector2.js#L137](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector2.js#L137)  
> Since: 3.4.0

---

## setToPolar

### <instance> setToPolar(azimuth, [radius])

**Description:**

Sets the `x` and `y` values of this object from a given polar coordinate.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| azimuth | number | No |  | The angular coordinate, in radians. |
| --- | --- | --- | --- | --- |
| radius | number | Yes | 1 | The radial coordinate (length). |

**Returns:** [Phaser.Math.Vector2](math-vector2.md) - This Vector2.

> Source: [src/math/Vector2.js#L153](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector2.js#L153)  
> Since: 3.0.0

---

## subtract

### <instance> subtract(src)

**Description:**

Subtract the given Vector from this Vector. Subtraction is component-wise.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| src | [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) | No | The Vector to subtract from this Vector. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Vector2](math-vector2.md) - This Vector2.

> Source: [src/math/Vector2.js#L262](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector2.js#L262)  
> Since: 3.0.0

---

## transformMat3

### <instance> transformMat3(mat)

**Description:**

Transform this Vector with the given Matrix.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| mat | [Phaser.Math.Matrix3](math-matrix3.md) | No | The Matrix3 to transform this Vector2 with. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Vector2](math-vector2.md) - This Vector2.

> Source: [src/math/Vector2.js#L564](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector2.js#L564)  
> Since: 3.0.0

---

## transformMat4

### <instance> transformMat4(mat)

**Description:**

Transform this Vector with the given Matrix.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| mat | [Phaser.Math.Matrix4](math-matrix4.md) | No | The Matrix4 to transform this Vector2 with. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Vector2](math-vector2.md) - This Vector2.

> Source: [src/math/Vector2.js#L586](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector2.js#L586)  
> Since: 3.0.0

---

# Constants:

# Public Members

## DOWN

### DOWN: [Phaser.Math.Vector2](math-vector2.md)

**Description:**

A static down Vector2 for use by reference.

This constant is meant for comparison operations and should not be modified directly.

> Source: [src/math/Vector2.js#L763](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector2.js#L763)  
> Since: 3.16.0

---

## LEFT

### LEFT: [Phaser.Math.Vector2](math-vector2.md)

**Description:**

A static left Vector2 for use by reference.

This constant is meant for comparison operations and should not be modified directly.

> Source: [src/math/Vector2.js#L739](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector2.js#L739)  
> Since: 3.16.0

---

## ONE

### ONE: [Phaser.Math.Vector2](math-vector2.md)

**Description:**

A static one Vector2 for use by reference.

This constant is meant for comparison operations and should not be modified directly.

> Source: [src/math/Vector2.js#L775](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector2.js#L775)  
> Since: 3.16.0

---

## RIGHT

### RIGHT: [Phaser.Math.Vector2](math-vector2.md)

**Description:**

A static right Vector2 for use by reference.

This constant is meant for comparison operations and should not be modified directly.

> Source: [src/math/Vector2.js#L727](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector2.js#L727)  
> Since: 3.16.0

---

## UP

### UP: [Phaser.Math.Vector2](math-vector2.md)

**Description:**

A static up Vector2 for use by reference.

This constant is meant for comparison operations and should not be modified directly.

> Source: [src/math/Vector2.js#L751](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector2.js#L751)  
> Since: 3.16.0

---

## ZERO

### ZERO: [Phaser.Math.Vector2](math-vector2.md)

**Description:**

A static zero Vector2 for use by reference.

This constant is meant for comparison operations and should not be modified directly.

> Source: [src/math/Vector2.js#L715](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector2.js#L715)  
> Since: 3.1.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [x](#x)

    - [x: number](#x-number)
  + [y](#y)

    - [y: number](#y-number)
* [Public Methods](#public-methods)

  + [add](#add)

    - [<instance> add(src)](#instance-addsrc)
  + [angle](#angle)

    - [<instance> angle()](#instance-angle)
  + [clone](#clone)

    - [<instance> clone()](#instance-clone)
  + [copy](#copy)

    - [<instance> copy(src)](#instance-copysrc)
  + [cross](#cross)

    - [<instance> cross(src)](#instance-crosssrc)
  + [distance](#distance)

    - [<instance> distance(src)](#instance-distancesrc)
  + [distanceSq](#distancesq)

    - [<instance> distanceSq(src)](#instance-distancesqsrc)
  + [divide](#divide)

    - [<instance> divide(src)](#instance-dividesrc)
  + [dot](#dot)

    - [<instance> dot(src)](#instance-dotsrc)
  + [equals](#equals)

    - [<instance> equals(v)](#instance-equalsv)
  + [fuzzyEquals](#fuzzyequals)

    - [<instance> fuzzyEquals(v, [epsilon])](#instance-fuzzyequalsv-epsilon)
  + [length](#length)

    - [<instance> length()](#instance-length)
  + [lengthSq](#lengthsq)

    - [<instance> lengthSq()](#instance-lengthsq)
  + [lerp](#lerp)

    - [<instance> lerp(src, [t])](#instance-lerpsrc-t)
  + [limit](#limit)

    - [<instance> limit(max)](#instance-limitmax)
  + [mirror](#mirror)

    - [<instance> mirror(axis)](#instance-mirroraxis)
  + [multiply](#multiply)

    - [<instance> multiply(src)](#instance-multiplysrc)
  + [negate](#negate)

    - [<instance> negate()](#instance-negate)
  + [normalize](#normalize)

    - [<instance> normalize()](#instance-normalize)
  + [normalizeLeftHand](#normalizelefthand)

    - [<instance> normalizeLeftHand()](#instance-normalizelefthand)
  + [normalizeRightHand](#normalizerighthand)

    - [<instance> normalizeRightHand()](#instance-normalizerighthand)
  + [project](#project)

    - [<instance> project(src)](#instance-projectsrc)
  + [reflect](#reflect)

    - [<instance> reflect(normal)](#instance-reflectnormal)
  + [reset](#reset)

    - [<instance> reset()](#instance-reset)
  + [rotate](#rotate)

    - [<instance> rotate(delta)](#instance-rotatedelta)
  + [scale](#scale)

    - [<instance> scale(value)](#instance-scalevalue)
  + [set](#set)

    - [<instance> set(x, [y])](#instance-setx-y)
  + [setAngle](#setangle)

    - [<instance> setAngle(angle)](#instance-setangleangle)
  + [setFromObject](#setfromobject)

    - [<instance> setFromObject(obj)](#instance-setfromobjectobj)
  + [setLength](#setlength)

    - [<instance> setLength(length)](#instance-setlengthlength)
  + [setTo](#setto)

    - [<instance> setTo(x, [y])](#instance-settox-y)
  + [setToPolar](#settopolar)

    - [<instance> setToPolar(azimuth, [radius])](#instance-settopolarazimuth-radius)
  + [subtract](#subtract)

    - [<instance> subtract(src)](#instance-subtractsrc)
  + [transformMat3](#transformmat3)

    - [<instance> transformMat3(mat)](#instance-transformmat3mat)
  + [transformMat4](#transformmat4)

    - [<instance> transformMat4(mat)](#instance-transformmat4mat)
* [Constants:](#constants)
* [Public Members](#public-members-1)

  + [DOWN](#down)

    - [DOWN: Phaser.Math.Vector2](#down-phasermathvector2)
  + [LEFT](#left)

    - [LEFT: Phaser.Math.Vector2](#left-phasermathvector2)
  + [ONE](#one)

    - [ONE: Phaser.Math.Vector2](#one-phasermathvector2)
  + [RIGHT](#right)

    - [RIGHT: Phaser.Math.Vector2](#right-phasermathvector2)
  + [UP](#up)

    - [UP: Phaser.Math.Vector2](#up-phasermathvector2)
  + [ZERO](#zero)

    - [ZERO: Phaser.Math.Vector2](#zero-phasermathvector2)

Back to top

©2025[Phaser](https://docs.phaser.io)