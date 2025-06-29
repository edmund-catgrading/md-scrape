# Vector3

Phaser.Math.Vector3

A representation of a vector in 3D space.

A three-component vector.

**Constructor**

`new Vector3([x], [y], [z])`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | Yes | The x component. |
| --- | --- | --- | --- |
| y | number | Yes | The y component. |
| z | number | Yes | The z component. |

---

**Scope**: static

> Source: [src/math/Vector3.js#L12](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L12)  
> Since: 3.0.0

# Public Members

## x

### x: number

**Description:**

The x component of this Vector.

> Source: [src/math/Vector3.js#L33](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L33)  
> Since: 3.0.0

---

## y

### y: number

**Description:**

The y component of this Vector.

> Source: [src/math/Vector3.js#L43](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L43)  
> Since: 3.0.0

---

## z

### z: number

**Description:**

The z component of this Vector.

> Source: [src/math/Vector3.js#L53](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L53)  
> Since: 3.0.0

---

# Public Methods

## add

### <instance> add(v)

**Description:**

Add a given Vector to this Vector. Addition is component-wise.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| v | [Phaser.Math.Vector2](math-vector2.md) | [Phaser.Math.Vector3](math-vector3.md) | No | The Vector to add to this Vector. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Vector3](math-vector3.md) - This Vector3.

> Source: [src/math/Vector3.js#L337](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L337)  
> Since: 3.0.0

---

## addScalar

### <instance> addScalar(s)

**Description:**

Add the given value to each component of this Vector.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| s | number | No | The amount to add to this Vector. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Vector3](math-vector3.md) - This Vector3.

> Source: [src/math/Vector3.js#L356](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L356)  
> Since: 3.50.0

---

## addScale

### <instance> addScale(v, scale)

**Description:**

Add and scale a given Vector to this Vector. Addition is component-wise.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| v | [Phaser.Math.Vector2](math-vector2.md) | [Phaser.Math.Vector3](math-vector3.md) | No | The Vector to add to this Vector. |
| --- | --- | --- | --- |
| scale | number | No | The amount to scale `v` by. |

**Returns:** [Phaser.Math.Vector3](math-vector3.md) - This Vector3.

> Source: [src/math/Vector3.js#L375](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L375)  
> Since: 3.50.0

---

## addVectors

### <instance> addVectors(a, b)

**Description:**

Adds the two given Vector3s and sets the results into this Vector3.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| a | [Phaser.Math.Vector3](math-vector3.md) | No | The first Vector to add. |
| --- | --- | --- | --- |
| b | [Phaser.Math.Vector3](math-vector3.md) | No | The second Vector to add. |

**Returns:** [Phaser.Math.Vector3](math-vector3.md) - This Vector3.

> Source: [src/math/Vector3.js#L147](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L147)  
> Since: 3.50.0

---

## applyMatrix3

### <instance> applyMatrix3(mat3)

**Description:**

Takes a Matrix3 and applies it to this Vector3.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| mat3 | [Phaser.Math.Matrix3](math-matrix3.md) | No | The Matrix3 to apply to this Vector3. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Vector3](math-vector3.md) - This Vector3.

> Source: [src/math/Vector3.js#L671](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L671)  
> Since: 3.50.0

---

## applyMatrix4

### <instance> applyMatrix4(mat4)

**Description:**

Takes a Matrix4 and applies it to this Vector3.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| mat4 | [Phaser.Math.Matrix4](math-matrix4.md) | No | The Matrix4 to apply to this Vector3. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Vector3](math-vector3.md) - This Vector3.

> Source: [src/math/Vector3.js#L695](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L695)  
> Since: 3.50.0

---

## clone

### <instance> clone()

**Description:**

Make a clone of this Vector3.

**Returns:** [Phaser.Math.Vector3](math-vector3.md) - A new Vector3 object containing this Vectors values.

> Source: [src/math/Vector3.js#L134](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L134)  
> Since: 3.0.0

---

## copy

### <instance> copy(src)

**Description:**

Copy the components of a given Vector into this Vector.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| src | [Phaser.Math.Vector2](math-vector2.md) | [Phaser.Math.Vector3](math-vector3.md) | No | The Vector to copy the components from. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Vector3](math-vector3.md) - This Vector3.

> Source: [src/math/Vector3.js#L231](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L231)  
> Since: 3.0.0

---

## cross

### <instance> cross(v)

**Description:**

Calculate the cross (vector) product of this Vector (which will be modified) and the given Vector.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| v | [Phaser.Math.Vector3](math-vector3.md) | No | The Vector to cross product with. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Vector3](math-vector3.md) - This Vector3.

> Source: [src/math/Vector3.js#L617](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L617)  
> Since: 3.0.0

---

## crossVectors

### <instance> crossVectors(a, b)

**Description:**

Calculate the cross (vector) product of two given Vectors.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| a | [Phaser.Math.Vector3](math-vector3.md) | No | The first Vector to multiply. |
| --- | --- | --- | --- |
| b | [Phaser.Math.Vector3](math-vector3.md) | No | The second Vector to multiply. |

**Returns:** [Phaser.Math.Vector3](math-vector3.md) - This Vector3.

> Source: [src/math/Vector3.js#L187](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L187)  
> Since: 3.0.0

---

## distance

### <instance> distance(v)

**Description:**

Calculate the distance between this Vector and the given Vector.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| v | [Phaser.Math.Vector2](math-vector2.md) | [Phaser.Math.Vector3](math-vector3.md) | No | The Vector to calculate the distance to. |
| --- | --- | --- | --- |

**Returns:** number - The distance from this Vector to the given Vector.

> Source: [src/math/Vector3.js#L501](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L501)  
> Since: 3.0.0

---

## distanceSq

### <instance> distanceSq(v)

**Description:**

Calculate the distance between this Vector and the given Vector, squared.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| v | [Phaser.Math.Vector2](math-vector2.md) | [Phaser.Math.Vector3](math-vector3.md) | No | The Vector to calculate the distance to. |
| --- | --- | --- | --- |

**Returns:** number - The distance from this Vector to the given Vector, squared.

> Source: [src/math/Vector3.js#L520](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L520)  
> Since: 3.0.0

---

## divide

### <instance> divide(v)

**Description:**

Perform a component-wise division between this Vector and the given Vector.

Divides this Vector by the given Vector.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| v | [Phaser.Math.Vector2](math-vector2.md) | [Phaser.Math.Vector3](math-vector3.md) | No | The Vector to divide this Vector by. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Vector3](math-vector3.md) - This Vector3.

> Source: [src/math/Vector3.js#L463](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L463)  
> Since: 3.0.0

---

## dot

### <instance> dot(v)

**Description:**

Calculate the dot product of this Vector and the given Vector.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| v | [Phaser.Math.Vector3](math-vector3.md) | No | The Vector3 to dot product with this Vector3. |
| --- | --- | --- | --- |

**Returns:** number - The dot product of this Vector and `v`.

> Source: [src/math/Vector3.js#L602](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L602)  
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
| v | [Phaser.Math.Vector3](math-vector3.md) | No | The Vector3 to compare against. |
| --- | --- | --- | --- |

**Returns:** boolean - True if the two vectors strictly match, otherwise false.

> Source: [src/math/Vector3.js#L214](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L214)  
> Since: 3.0.0

---

## fromArray

### <instance> fromArray(array, [offset])

**Description:**

Sets the components of this Vector3 from the given array, based on the offset.

Vector3.x = array[offset]

Vector3.y = array[offset + 1]

Vector3.z = array[offset + 2]

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| array | Array.<number> | No |  | The array of values to get this Vector from. |
| --- | --- | --- | --- | --- |
| offset | number | Yes | 0 | The offset index into the array. |

**Returns:** [Phaser.Math.Vector3](math-vector3.md) - This Vector3.

> Source: [src/math/Vector3.js#L311](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L311)  
> Since: 3.50.0

---

## length

### <instance> length()

**Description:**

Calculate the length (or magnitude) of this Vector.

**Returns:** number - The length of this Vector.

> Source: [src/math/Vector3.js#L539](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L539)  
> Since: 3.0.0

---

## lengthSq

### <instance> lengthSq()

**Description:**

Calculate the length of this Vector squared.

**Returns:** number - The length of this Vector, squared.

> Source: [src/math/Vector3.js#L556](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L556)  
> Since: 3.0.0

---

## lerp

### <instance> lerp(v, [t])

**Description:**

Linearly interpolate between this Vector and the given Vector.

Interpolates this Vector towards the given Vector.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| v | [Phaser.Math.Vector3](math-vector3.md) | No |  | The Vector3 to interpolate towards. |
| --- | --- | --- | --- | --- |
| t | number | Yes | 0 | The interpolation percentage, between 0 and 1. |

**Returns:** [Phaser.Math.Vector3](math-vector3.md) - This Vector3.

> Source: [src/math/Vector3.js#L643](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L643)  
> Since: 3.0.0

---

## max

### <instance> max(v)

**Description:**

Sets the components of this Vector to be the `Math.max` result from the given vector.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| v | [Phaser.Math.Vector3](math-vector3.md) | No | The Vector3 to check the maximum values against. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Vector3](math-vector3.md) - This Vector3.

> Source: [src/math/Vector3.js#L115](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L115)  
> Since: 3.50.0

---

## min

### <instance> min(v)

**Description:**

Sets the components of this Vector to be the `Math.min` result from the given vector.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| v | [Phaser.Math.Vector3](math-vector3.md) | No | The Vector3 to check the minimum values against. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Vector3](math-vector3.md) - This Vector3.

> Source: [src/math/Vector3.js#L96](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L96)  
> Since: 3.50.0

---

## multiply

### <instance> multiply(v)

**Description:**

Perform a component-wise multiplication between this Vector and the given Vector.

Multiplies this Vector by the given Vector.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| v | [Phaser.Math.Vector2](math-vector2.md) | [Phaser.Math.Vector3](math-vector3.md) | No | The Vector to multiply this Vector by. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Vector3](math-vector3.md) - This Vector3.

> Source: [src/math/Vector3.js#L414](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L414)  
> Since: 3.0.0

---

## negate

### <instance> negate()

**Description:**

Negate the `x`, `y` and `z` components of this Vector.

**Returns:** [Phaser.Math.Vector3](math-vector3.md) - This Vector3.

> Source: [src/math/Vector3.js#L484](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L484)  
> Since: 3.0.0

---

## normalize

### <instance> normalize()

**Description:**

Normalize this Vector.

Makes the vector a unit length vector (magnitude of 1) in the same direction.

**Returns:** [Phaser.Math.Vector3](math-vector3.md) - This Vector3.

> Source: [src/math/Vector3.js#L573](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L573)  
> Since: 3.0.0

---

## project

### <instance> project(mat)

**Description:**

Multiplies this Vector3 by the specified matrix, applying a W divide. This is useful for projection,

e.g. unprojecting a 2D point into 3D space.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| mat | [Phaser.Math.Matrix4](math-matrix4.md) | No | The Matrix4 to multiply this Vector3 with. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Vector3](math-vector3.md) - This Vector3.

> Source: [src/math/Vector3.js#L833](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L833)  
> Since: 3.0.0

---

## projectViewMatrix

### <instance> projectViewMatrix(viewMatrix, projectionMatrix)

**Description:**

Multiplies this Vector3 by the given view and projection matrices.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| viewMatrix | [Phaser.Math.Matrix4](math-matrix4.md) | No | A View Matrix. |
| --- | --- | --- | --- |
| projectionMatrix | [Phaser.Math.Matrix4](math-matrix4.md) | No | A Projection Matrix. |

**Returns:** [Phaser.Math.Vector3](math-vector3.md) - This Vector3.

> Source: [src/math/Vector3.js#L877](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L877)  
> Since: 3.50.0

---

## reset

### <instance> reset()

**Description:**

Make this Vector the zero vector (0, 0, 0).

**Returns:** [Phaser.Math.Vector3](math-vector3.md) - This Vector3.

> Source: [src/math/Vector3.js#L945](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L945)  
> Since: 3.0.0

---

## scale

### <instance> scale(scale)

**Description:**

Scale this Vector by the given value.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| scale | number | No | The value to scale this Vector by. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Vector3](math-vector3.md) - This Vector3.

> Source: [src/math/Vector3.js#L435](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L435)  
> Since: 3.0.0

---

## set

### <instance> set(x, [y], [z])

**Description:**

Set the `x`, `y`, and `z` components of this Vector to the given `x`, `y`, and `z` values.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | object | No | The x value to set for this Vector, or an object containing x, y and z components. |
| --- | --- | --- | --- |
| y | number | Yes | The y value to set for this Vector. |
| z | number | Yes | The z value to set for this Vector. |

**Returns:** [Phaser.Math.Vector3](math-vector3.md) - This Vector3.

> Source: [src/math/Vector3.js#L250](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L250)  
> Since: 3.0.0

---

## setFromMatrixColumn

### <instance> setFromMatrixColumn(mat4, index)

**Description:**

Sets the components of this Vector3 from the Matrix4 column specified.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| mat4 | [Phaser.Math.Matrix4](math-matrix4.md) | No | The Matrix4 to get the column from. |
| --- | --- | --- | --- |
| index | number | No | The column index. |

**Returns:** [Phaser.Math.Vector3](math-vector3.md) - This Vector3.

> Source: [src/math/Vector3.js#L295](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L295)  
> Since: 3.50.0

---

## setFromMatrixPosition

### <instance> setFromMatrixPosition(mat4)

**Description:**

Sets the components of this Vector3 from the position of the given Matrix4.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| mat4 | [Phaser.Math.Matrix4](math-matrix4.md) | No | The Matrix4 to get the position from. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Vector3](math-vector3.md) - This Vector3.

> Source: [src/math/Vector3.js#L280](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L280)  
> Since: 3.50.0

---

## subtract

### <instance> subtract(v)

**Description:**

Subtract the given Vector from this Vector. Subtraction is component-wise.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| v | [Phaser.Math.Vector2](math-vector2.md) | [Phaser.Math.Vector3](math-vector3.md) | No | The Vector to subtract from this Vector. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Vector3](math-vector3.md) - This Vector3.

> Source: [src/math/Vector3.js#L395](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L395)  
> Since: 3.0.0

---

## subVectors

### <instance> subVectors(a, b)

**Description:**

Subtracts the two given Vector3s and sets the results into this Vector3.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| a | [Phaser.Math.Vector3](math-vector3.md) | No | The first Vector to sub. |
| --- | --- | --- | --- |
| b | [Phaser.Math.Vector3](math-vector3.md) | No | The second Vector to sub. |

**Returns:** [Phaser.Math.Vector3](math-vector3.md) - This Vector3.

> Source: [src/math/Vector3.js#L167](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L167)  
> Since: 3.85.0

---

## transformCoordinates

### <instance> transformCoordinates(mat)

**Description:**

Transforms the coordinates of this Vector3 with the given Matrix4.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| mat | [Phaser.Math.Matrix4](math-matrix4.md) | No | The Matrix4 to transform this Vector3 with. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Vector3](math-vector3.md) - This Vector3.

> Source: [src/math/Vector3.js#L769](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L769)  
> Since: 3.0.0

---

## transformMat3

### <instance> transformMat3(mat)

**Description:**

Transform this Vector with the given Matrix.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| mat | [Phaser.Math.Matrix3](math-matrix3.md) | No | The Matrix3 to transform this Vector3 with. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Vector3](math-vector3.md) - This Vector3.

> Source: [src/math/Vector3.js#L721](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L721)  
> Since: 3.0.0

---

## transformMat4

### <instance> transformMat4(mat)

**Description:**

Transform this Vector with the given Matrix4.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| mat | [Phaser.Math.Matrix4](math-matrix4.md) | No | The Matrix4 to transform this Vector3 with. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Vector3](math-vector3.md) - This Vector3.

> Source: [src/math/Vector3.js#L745](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L745)  
> Since: 3.0.0

---

## transformQuat

### <instance> transformQuat(q)

**Description:**

Transform this Vector with the given Quaternion.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| q | [Phaser.Math.Quaternion](math-quaternion.md) | No | The Quaternion to transform this Vector with. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Vector3](math-vector3.md) - This Vector3.

> Source: [src/math/Vector3.js#L798](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L798)  
> Since: 3.0.0

---

## unproject

### <instance> unproject(viewport, invProjectionView)

**Description:**

Unproject this point from 2D space to 3D space.

The point should have its x and y properties set to

2D screen space, and the z either at 0 (near plane)

or 1 (far plane). The provided matrix is assumed to already

be combined, i.e. projection \* view \* model.

After this operation, this vector's (x, y, z) components will

represent the unprojected 3D coordinate.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| viewport | [Phaser.Math.Vector4](math-vector4.md) | No | Screen x, y, width and height in pixels. |
| --- | --- | --- | --- |
| invProjectionView | [Phaser.Math.Matrix4](math-matrix4.md) | No | Combined projection and view matrix. |

**Returns:** [Phaser.Math.Vector3](math-vector3.md) - This Vector3.

> Source: [src/math/Vector3.js#L909](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L909)  
> Since: 3.0.0

---

## unprojectViewMatrix

### <instance> unprojectViewMatrix(projectionMatrix, worldMatrix)

**Description:**

Multiplies this Vector3 by the given inversed projection matrix and world matrix.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| projectionMatrix | [Phaser.Math.Matrix4](math-matrix4.md) | No | An inversed Projection Matrix. |
| --- | --- | --- | --- |
| worldMatrix | [Phaser.Math.Matrix4](math-matrix4.md) | No | A World View Matrix. |

**Returns:** [Phaser.Math.Vector3](math-vector3.md) - This Vector3.

> Source: [src/math/Vector3.js#L893](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L893)  
> Since: 3.50.0

---

## up

### <instance> up()

**Description:**

Set this Vector to point up.

Sets the y component of the vector to 1, and the others to 0.

**Returns:** [Phaser.Math.Vector3](math-vector3.md) - This Vector3.

> Source: [src/math/Vector3.js#L77](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L77)  
> Since: 3.0.0

---

# Constants:

# Public Members

## BACK

### BACK: [Phaser.Math.Vector3](math-vector3.md)

**Description:**

A static back Vector3 for use by reference.

This constant is meant for comparison operations and should not be modified directly.

> Source: [src/math/Vector3.js#L1036](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L1036)  
> Since: 3.16.0

---

## DOWN

### DOWN: [Phaser.Math.Vector3](math-vector3.md)

**Description:**

A static down Vector3 for use by reference.

This constant is meant for comparison operations and should not be modified directly.

> Source: [src/math/Vector3.js#L1012](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L1012)  
> Since: 3.16.0

---

## FORWARD

### FORWARD: [Phaser.Math.Vector3](math-vector3.md)

**Description:**

A static forward Vector3 for use by reference.

This constant is meant for comparison operations and should not be modified directly.

> Source: [src/math/Vector3.js#L1024](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L1024)  
> Since: 3.16.0

---

## LEFT

### LEFT: [Phaser.Math.Vector3](math-vector3.md)

**Description:**

A static left Vector3 for use by reference.

This constant is meant for comparison operations and should not be modified directly.

> Source: [src/math/Vector3.js#L988](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L988)  
> Since: 3.16.0

---

## ONE

### ONE: [Phaser.Math.Vector3](math-vector3.md)

**Description:**

A static one Vector3 for use by reference.

This constant is meant for comparison operations and should not be modified directly.

> Source: [src/math/Vector3.js#L1048](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L1048)  
> Since: 3.16.0

---

## RIGHT

### RIGHT: [Phaser.Math.Vector3](math-vector3.md)

**Description:**

A static right Vector3 for use by reference.

This constant is meant for comparison operations and should not be modified directly.

> Source: [src/math/Vector3.js#L976](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L976)  
> Since: 3.16.0

---

## UP

### UP: [Phaser.Math.Vector3](math-vector3.md)

**Description:**

A static up Vector3 for use by reference.

This constant is meant for comparison operations and should not be modified directly.

> Source: [src/math/Vector3.js#L1000](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L1000)  
> Since: 3.16.0

---

## ZERO

### ZERO: [Phaser.Math.Vector3](math-vector3.md)

**Description:**

A static zero Vector3 for use by reference.

This constant is meant for comparison operations and should not be modified directly.

> Source: [src/math/Vector3.js#L964](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L964)  
> Since: 3.16.0

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
  + [z](#z)

    - [z: number](#z-number)
* [Public Methods](#public-methods)

  + [add](#add)

    - [<instance> add(v)](#instance-addv)
  + [addScalar](#addscalar)

    - [<instance> addScalar(s)](#instance-addscalars)
  + [addScale](#addscale)

    - [<instance> addScale(v, scale)](#instance-addscalev-scale)
  + [addVectors](#addvectors)

    - [<instance> addVectors(a, b)](#instance-addvectorsa-b)
  + [applyMatrix3](#applymatrix3)

    - [<instance> applyMatrix3(mat3)](#instance-applymatrix3mat3)
  + [applyMatrix4](#applymatrix4)

    - [<instance> applyMatrix4(mat4)](#instance-applymatrix4mat4)
  + [clone](#clone)

    - [<instance> clone()](#instance-clone)
  + [copy](#copy)

    - [<instance> copy(src)](#instance-copysrc)
  + [cross](#cross)

    - [<instance> cross(v)](#instance-crossv)
  + [crossVectors](#crossvectors)

    - [<instance> crossVectors(a, b)](#instance-crossvectorsa-b)
  + [distance](#distance)

    - [<instance> distance(v)](#instance-distancev)
  + [distanceSq](#distancesq)

    - [<instance> distanceSq(v)](#instance-distancesqv)
  + [divide](#divide)

    - [<instance> divide(v)](#instance-dividev)
  + [dot](#dot)

    - [<instance> dot(v)](#instance-dotv)
  + [equals](#equals)

    - [<instance> equals(v)](#instance-equalsv)
  + [fromArray](#fromarray)

    - [<instance> fromArray(array, [offset])](#instance-fromarrayarray-offset)
  + [length](#length)

    - [<instance> length()](#instance-length)
  + [lengthSq](#lengthsq)

    - [<instance> lengthSq()](#instance-lengthsq)
  + [lerp](#lerp)

    - [<instance> lerp(v, [t])](#instance-lerpv-t)
  + [max](#max)

    - [<instance> max(v)](#instance-maxv)
  + [min](#min)

    - [<instance> min(v)](#instance-minv)
  + [multiply](#multiply)

    - [<instance> multiply(v)](#instance-multiplyv)
  + [negate](#negate)

    - [<instance> negate()](#instance-negate)
  + [normalize](#normalize)

    - [<instance> normalize()](#instance-normalize)
  + [project](#project)

    - [<instance> project(mat)](#instance-projectmat)
  + [projectViewMatrix](#projectviewmatrix)

    - [<instance> projectViewMatrix(viewMatrix, projectionMatrix)](#instance-projectviewmatrixviewmatrix-projectionmatrix)
  + [reset](#reset)

    - [<instance> reset()](#instance-reset)
  + [scale](#scale)

    - [<instance> scale(scale)](#instance-scalescale)
  + [set](#set)

    - [<instance> set(x, [y], [z])](#instance-setx-y-z)
  + [setFromMatrixColumn](#setfrommatrixcolumn)

    - [<instance> setFromMatrixColumn(mat4, index)](#instance-setfrommatrixcolumnmat4-index)
  + [setFromMatrixPosition](#setfrommatrixposition)

    - [<instance> setFromMatrixPosition(mat4)](#instance-setfrommatrixpositionmat4)
  + [subtract](#subtract)

    - [<instance> subtract(v)](#instance-subtractv)
  + [subVectors](#subvectors)

    - [<instance> subVectors(a, b)](#instance-subvectorsa-b)
  + [transformCoordinates](#transformcoordinates)

    - [<instance> transformCoordinates(mat)](#instance-transformcoordinatesmat)
  + [transformMat3](#transformmat3)

    - [<instance> transformMat3(mat)](#instance-transformmat3mat)
  + [transformMat4](#transformmat4)

    - [<instance> transformMat4(mat)](#instance-transformmat4mat)
  + [transformQuat](#transformquat)

    - [<instance> transformQuat(q)](#instance-transformquatq)
  + [unproject](#unproject)

    - [<instance> unproject(viewport, invProjectionView)](#instance-unprojectviewport-invprojectionview)
  + [unprojectViewMatrix](#unprojectviewmatrix)

    - [<instance> unprojectViewMatrix(projectionMatrix, worldMatrix)](#instance-unprojectviewmatrixprojectionmatrix-worldmatrix)
  + [up](#up)

    - [<instance> up()](#instance-up)
* [Constants:](#constants)
* [Public Members](#public-members-1)

  + [BACK](#back)

    - [BACK: Phaser.Math.Vector3](#back-phasermathvector3)
  + [DOWN](#down)

    - [DOWN: Phaser.Math.Vector3](#down-phasermathvector3)
  + [FORWARD](#forward)

    - [FORWARD: Phaser.Math.Vector3](#forward-phasermathvector3)
  + [LEFT](#left)

    - [LEFT: Phaser.Math.Vector3](#left-phasermathvector3)
  + [ONE](#one)

    - [ONE: Phaser.Math.Vector3](#one-phasermathvector3)
  + [RIGHT](#right)

    - [RIGHT: Phaser.Math.Vector3](#right-phasermathvector3)
  + [UP](#up-1)

    - [UP: Phaser.Math.Vector3](#up-phasermathvector3)
  + [ZERO](#zero)

    - [ZERO: Phaser.Math.Vector3](#zero-phasermathvector3)

Back to top

©2025[Phaser](https://docs.phaser.io)



Vector3