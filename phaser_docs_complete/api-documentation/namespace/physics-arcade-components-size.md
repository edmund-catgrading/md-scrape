# Phaser.Physics.Arcade.Components.Size

Scope:
static

> Source: [src/physics/arcade/components/Size.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/components/Size.js#L7)  
> Since: 3.0.0

# Static functions

## setBodySize

### <instance> setBodySize(width, height, [center])

**Description:**

Sets the size of this physics body. Setting the size does not adjust the dimensions of the parent Game Object.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| width | number | No |  | The new width of the physics body, in pixels. |
| --- | --- | --- | --- | --- |
| height | number | No |  | The new height of the physics body, in pixels. |
| center | boolean | Yes | true | Should the body be re-positioned so its center aligns with the parent Game Object? |

**Returns:** [Phaser.Physics.Arcade.Components.Size](physics-arcade-components-size.md) - This Game Object.

> Source: [src/physics/arcade/components/Size.js#L57](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/components/Size.js#L57)  
> Since: 3.24.0

---

## setCircle

### <instance> setCircle(radius, [offsetX], [offsetY])

**Description:**

Sets this physics body to use a circle for collision instead of a rectangle.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| radius | number | No | The radius of the physics body, in pixels. |
| --- | --- | --- | --- |
| offsetX | number | Yes | The amount to offset the body from the parent Game Object along the x-axis. |
| offsetY | number | Yes | The amount to offset the body from the parent Game Object along the y-axis. |

**Returns:** [Phaser.Physics.Arcade.Components.Size](physics-arcade-components-size.md) - This Game Object.

> Source: [src/physics/arcade/components/Size.js#L76](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/components/Size.js#L76)  
> Since: 3.0.0

---

## setOffset

### <instance> setOffset(x, [y])

**Description:**

Sets the body offset. This allows you to adjust the difference between the center of the body

and the x and y coordinates of the parent Game Object.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | No |  | The amount to offset the body from the parent Game Object along the x-axis. |
| --- | --- | --- | --- | --- |
| y | number | Yes | "x" | The amount to offset the body from the parent Game Object along the y-axis. Defaults to the value given for the x-axis. |

**Returns:** [Phaser.Physics.Arcade.Components.Size](physics-arcade-components-size.md) - This Game Object.

> Source: [src/physics/arcade/components/Size.js#L16](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/components/Size.js#L16)  
> Since: 3.0.0

---

## setSize

### <instance> setSize(width, height, [center])

**Description:**

**DEPRECATED**: Please use `setBodySize` instead.

Sets the size of this physics body. Setting the size does not adjust the dimensions of the parent Game Object.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| width | number | No |  | The new width of the physics body, in pixels. |
| --- | --- | --- | --- | --- |
| height | number | No |  | The new height of the physics body, in pixels. |
| center | boolean | Yes | true | Should the body be re-positioned so its center aligns with the parent Game Object? |

**Returns:** [Phaser.Physics.Arcade.Components.Size](physics-arcade-components-size.md) - This Game Object.

> Source: [src/physics/arcade/components/Size.js#L35](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/components/Size.js#L35)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Static functions](#static-functions)

  + [setBodySize](#setbodysize)

    - [<instance> setBodySize(width, height, [center])](#instance-setbodysizewidth-height-center)
  + [setCircle](#setcircle)

    - [<instance> setCircle(radius, [offsetX], [offsetY])](#instance-setcircleradius-offsetx-offsety)
  + [setOffset](#setoffset)

    - [<instance> setOffset(x, [y])](#instance-setoffsetx-y)
  + [setSize](#setsize)

    - [<instance> setSize(width, height, [center])](#instance-setsizewidth-height-center)

Back to top

©2025[Phaser](https://docs.phaser.io)



Phaser.Physics.Arcade.Components.Size