# StaticBody

Phaser.Physics.Arcade.StaticBody

A Static Arcade Physics Body.

A Static Body never moves, and isn't automatically synchronized with its parent Game Object.

That means if you make any change to the parent's origin, position, or scale after creating or adding the body, you'll need to update the Static Body manually.

A Static Body can collide with other Bodies, but is never moved by collisions.

Its dynamic counterpart is [Phaser.Physics.Arcade.Body](Phaser.Physics.Arcade.Body.md).

**Constructor**

`new StaticBody(world, [gameObject])`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| world | [Phaser.Physics.Arcade.World](physics-arcade-world.md) | No | The Arcade Physics simulation this Static Body belongs to. |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | Yes | The Game Object this Body belongs to. As of Phaser 3.60 this is now optional. |

---

**Scope**: static

**Extends**

> [Phaser.Physics.Arcade.Components.Collision](../namespace/physics-arcade-components-collision.md)

> Source: [src/physics/arcade/StaticBody.js#L15](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticBody.js#L15)  
> Since: 3.0.0

# Public Members

## allowGravity

### allowGravity: boolean

**Description:**

A constant `false` value expected by the Arcade Physics simulation.

> Source: [src/physics/arcade/StaticBody.js#L233](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticBody.js#L233)  
> Since: 3.0.0

---

## blocked

### blocked: [Phaser.Types.Physics.Arcade.ArcadeBodyCollision](../typedef/types-physics-arcade.md)

**Description:**

This property is kept for compatibility with Dynamic Bodies.

Avoid using it.

> Source: [src/physics/arcade/StaticBody.js#L439](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticBody.js#L439)  
> Since: 3.0.0

---

## bottom

### bottom: number

**Description:**

The lowest y coordinate of the area of the StaticBody. (y + height)

> Source: [src/physics/arcade/StaticBody.js#L1064](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticBody.js#L1064)  
> Since: 3.0.0

---

## bounce

### bounce: [Phaser.Math.Vector2](math-vector2.md)

**Description:**

Rebound, or restitution, following a collision, relative to 1. Always zero for a Static Body.

> Source: [src/physics/arcade/StaticBody.js#L254](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticBody.js#L254)  
> Since: 3.0.0

---

## center

### center: [Phaser.Math.Vector2](math-vector2.md)

**Description:**

The center of the Static Body's boundary.

This is the midpoint of its `position` (top-left corner) and its bottom-right corner.

> Source: [src/physics/arcade/StaticBody.js#L213](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticBody.js#L213)  
> Since: 3.0.0

---

## checkCollision

### checkCollision: [Phaser.Types.Physics.Arcade.ArcadeBodyCollision](../typedef/types-physics-arcade.md)

**Description:**

Whether this StaticBody is checked for collisions and for which directions. You can set `checkCollision.none = false` to disable collision checks.

> Source: [src/physics/arcade/StaticBody.js#L409](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticBody.js#L409)  
> Since: 3.0.0

---

## collideWorldBounds

### collideWorldBounds: boolean

**Description:**

Whether this StaticBody interacts with the world boundary.

Always false for a Static Body. (Static Bodies never collide with the world boundary.)

> Source: [src/physics/arcade/StaticBody.js#L397](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticBody.js#L397)  
> Since: 3.0.0

---

## collisionCategory

### collisionCategory: number

**Description:**

The Arcade Physics Body Collision Category.

This can be set to any valid collision bitfield value.

See the `setCollisionCategory` method for more details.

> Source: [src/physics/arcade/StaticBody.js#L459](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticBody.js#L459)  
> Since: 3.70.0

---

## collisionMask

### collisionMask: number

**Description:**

The Arcade Physics Body Collision Mask.

See the `setCollidesWith` method for more details.

> Source: [src/physics/arcade/StaticBody.js#L472](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticBody.js#L472)  
> Since: 3.70.0

---

## customSeparateX

### customSeparateX: boolean

**Description:**

A flag disabling the default horizontal separation of colliding bodies. Pass your own `collideHandler` to the collider.

> Source: [src/physics/arcade/StaticBody.js#L337](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticBody.js#L337)  
> Since: 3.0.0

---

## customSeparateY

### customSeparateY: boolean

**Description:**

A flag disabling the default vertical separation of colliding bodies. Pass your own `collideHandler` to the collider.

> Source: [src/physics/arcade/StaticBody.js#L347](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticBody.js#L347)  
> Since: 3.0.0

---

## debugBodyColor

### debugBodyColor: number

**Description:**

The color of this Static Body on the debug display.

> Source: [src/physics/arcade/StaticBody.js#L112](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticBody.js#L112)  
> Since: 3.0.0

---

## debugShowBody

### debugShowBody: boolean

**Description:**

Whether the Static Body's boundary is drawn to the debug display.

> Source: [src/physics/arcade/StaticBody.js#L103](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticBody.js#L103)  
> Since: 3.0.0

---

## embedded

### embedded: boolean

**Description:**

Whether this StaticBody has ever overlapped with another while both were not moving.

> Source: [src/physics/arcade/StaticBody.js#L387](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticBody.js#L387)  
> Since: 3.0.0

---

## enable

### enable: boolean

**Description:**

Whether this Static Body is updated by the physics simulation.

> Source: [src/physics/arcade/StaticBody.js#L121](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticBody.js#L121)  
> Since: 3.0.0

---

## gameObject

### gameObject: [Phaser.GameObjects.GameObject](gameobjects-gameobject.md)

**Description:**

The Game Object this Static Body belongs to.

As of Phaser 3.60 this is now optional and can be undefined.

> Source: [src/physics/arcade/StaticBody.js#L82](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticBody.js#L82)  
> Since: 3.0.0

---

## gravity

### gravity: [Phaser.Math.Vector2](math-vector2.md)

**Description:**

Gravitational force applied specifically to this Body. Values are in pixels per second squared. Always zero for a Static Body.

> Source: [src/physics/arcade/StaticBody.js#L244](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticBody.js#L244)  
> Since: 3.0.0

---

## halfHeight

### halfHeight: number

**Description:**

Half the Static Body's height, in pixels.

If the Static Body is circular, this is also the Static Body's radius.

> Source: [src/physics/arcade/StaticBody.js#L203](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticBody.js#L203)  
> Since: 3.0.0

---

## halfWidth

### halfWidth: number

**Description:**

Half the Static Body's width, in pixels.

If the Static Body is circular, this is also the Static Body's radius.

> Source: [src/physics/arcade/StaticBody.js#L193](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticBody.js#L193)  
> Since: 3.0.0

---

## height

### height: number

**Description:**

The height of the Static Body's boundary, in pixels.

If the Static Body is circular, this is also the Static Body's diameter.

> Source: [src/physics/arcade/StaticBody.js#L183](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticBody.js#L183)  
> Since: 3.0.0

---

## immovable

### immovable: boolean

**Description:**

Whether this object can be moved by collisions with another body.

> Source: [src/physics/arcade/StaticBody.js#L308](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticBody.js#L308)  
> Since: 3.0.0

---

## isBody

### isBody: boolean

**Description:**

A quick-test flag that signifies this is a Body, used in the World collision handler.

> Source: [src/physics/arcade/StaticBody.js#L93](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticBody.js#L93)  
> Since: 3.60.0

---

## isCircle

### isCircle: boolean

**Description:**

Whether this Static Body's boundary is circular (`true`) or rectangular (`false`).

> Source: [src/physics/arcade/StaticBody.js#L131](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticBody.js#L131)  
> Since: 3.0.0

---

## left

### left: number

**Description:**

Returns the left-most x coordinate of the area of the StaticBody.

> Source: [src/physics/arcade/StaticBody.js#L1013](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticBody.js#L1013)  
> Since: 3.0.0

---

## mass

### mass: number

**Description:**

The StaticBody's inertia, relative to a default unit (1). With `bounce`, this affects the exchange of momentum (velocities) during collisions.

> Source: [src/physics/arcade/StaticBody.js#L298](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticBody.js#L298)  
> Since: 3.0.0

---

## offset

### offset: [Phaser.Math.Vector2](math-vector2.md)

**Description:**

The offset set by [Phaser.Physics.Arcade.StaticBody#setCircle](physics-arcade-staticbody.md) or [Phaser.Physics.Arcade.StaticBody#setSize](physics-arcade-staticbody.md).

This doesn't affect the Static Body's position, because a Static Body does not follow its Game Object.

> Source: [src/physics/arcade/StaticBody.js#L152](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticBody.js#L152)  
> Since: 3.0.0

---

## onCollide

### onCollide: boolean

**Description:**

Whether the simulation emits a `collide` event when this StaticBody collides with another.

> Source: [src/physics/arcade/StaticBody.js#L278](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticBody.js#L278)  
> Since: 3.0.0

---

## onOverlap

### onOverlap: boolean

**Description:**

Whether the simulation emits an `overlap` event when this StaticBody overlaps with another.

> Source: [src/physics/arcade/StaticBody.js#L288](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticBody.js#L288)  
> Since: 3.0.0

---

## onWorldBounds

### onWorldBounds: boolean

**Description:**

Whether the simulation emits a `worldbounds` event when this StaticBody collides with the world boundary.

Always false for a Static Body. (Static Bodies never collide with the world boundary and never trigger a `worldbounds` event.)

> Source: [src/physics/arcade/StaticBody.js#L266](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticBody.js#L266)  
> Since: 3.0.0

---

## overlapR

### overlapR: number

**Description:**

The amount of overlap (before separation), if this StaticBody is circular and colliding with another circular body.

> Source: [src/physics/arcade/StaticBody.js#L377](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticBody.js#L377)  
> Since: 3.0.0

---

## overlapX

### overlapX: number

**Description:**

The amount of horizontal overlap (before separation), if this Body is colliding with another.

> Source: [src/physics/arcade/StaticBody.js#L357](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticBody.js#L357)  
> Since: 3.0.0

---

## overlapY

### overlapY: number

**Description:**

The amount of vertical overlap (before separation), if this Body is colliding with another.

> Source: [src/physics/arcade/StaticBody.js#L367](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticBody.js#L367)  
> Since: 3.0.0

---

## physicsType

### physicsType: number

**Description:**

The StaticBody's physics type (static by default).

> Source: [src/physics/arcade/StaticBody.js#L449](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticBody.js#L449)  
> Since: 3.0.0

---

## position

### position: [Phaser.Math.Vector2](math-vector2.md)

**Description:**

The position of this Static Body within the simulation.

> Source: [src/physics/arcade/StaticBody.js#L164](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticBody.js#L164)  
> Since: 3.0.0

---

## pushable

### pushable: boolean

**Description:**

Sets if this Body can be pushed by another Body.

A body that cannot be pushed will reflect back all of the velocity it is given to the

colliding body. If that body is also not pushable, then the separation will be split

between them evenly.

If you want your body to never move or seperate at all, see the `setImmovable` method.

By default, Static Bodies are not pushable.

> Source: [src/physics/arcade/StaticBody.js#L318](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticBody.js#L318)  
> Since: 3.50.0

---

## radius

### radius: number

**Description:**

If this Static Body is circular, this is the radius of the boundary, as set by [Phaser.Physics.Arcade.StaticBody#setCircle](physics-arcade-staticbody.md), in pixels.

Equal to `halfWidth`.

> Source: [src/physics/arcade/StaticBody.js#L141](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticBody.js#L141)  
> Since: 3.0.0

---

## right

### right: number

**Description:**

The right-most x coordinate of the area of the StaticBody.

> Source: [src/physics/arcade/StaticBody.js#L1030](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticBody.js#L1030)  
> Since: 3.0.0

---

## top

### top: number

**Description:**

The highest y coordinate of the area of the StaticBody.

> Source: [src/physics/arcade/StaticBody.js#L1047](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticBody.js#L1047)  
> Since: 3.0.0

---

## touching

### touching: [Phaser.Types.Physics.Arcade.ArcadeBodyCollision](../typedef/types-physics-arcade.md)

**Description:**

This property is kept for compatibility with Dynamic Bodies.

Avoid using it.

> Source: [src/physics/arcade/StaticBody.js#L418](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticBody.js#L418)  
> Since: 3.0.0

---

## velocity

### velocity: [Phaser.Math.Vector2](math-vector2.md)

**Description:**

A constant zero velocity used by the Arcade Physics simulation for calculations.

> Source: [src/physics/arcade/StaticBody.js#L223](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticBody.js#L223)  
> Since: 3.0.0

---

## wasTouching

### wasTouching: [Phaser.Types.Physics.Arcade.ArcadeBodyCollision](../typedef/types-physics-arcade.md)

**Description:**

This property is kept for compatibility with Dynamic Bodies.

Avoid using it.

The values are always false for a Static Body.

> Source: [src/physics/arcade/StaticBody.js#L428](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticBody.js#L428)  
> Since: 3.0.0

---

## width

### width: number

**Description:**

The width of the Static Body's boundary, in pixels.

If the Static Body is circular, this is also the Static Body's diameter.

> Source: [src/physics/arcade/StaticBody.js#L173](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticBody.js#L173)  
> Since: 3.0.0

---

## world

### world: [Phaser.Physics.Arcade.World](physics-arcade-world.md)

**Description:**

The Arcade Physics simulation this Static Body belongs to.

> Source: [src/physics/arcade/StaticBody.js#L73](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticBody.js#L73)  
> Since: 3.0.0

---

## x

### x: number

**Description:**

The x coordinate of the StaticBody.

> Source: [src/physics/arcade/StaticBody.js#L963](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticBody.js#L963)  
> Since: 3.0.0

---

## y

### y: number

**Description:**

The y coordinate of the StaticBody.

> Source: [src/physics/arcade/StaticBody.js#L988](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticBody.js#L988)  
> Since: 3.0.0

---

# Private Members

## \_dx

### \_dx: number

**Description:**

The calculated change in the Static Body's horizontal position during the current step.

For a static body this is always zero.

**Access:** private

> Source: [src/physics/arcade/StaticBody.js#L483](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticBody.js#L483)  
> Since: 3.10.0

---

## \_dy

### \_dy: number

**Description:**

The calculated change in the Static Body's vertical position during the current step.

For a static body this is always zero.

**Access:** private

> Source: [src/physics/arcade/StaticBody.js#L495](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticBody.js#L495)  
> Since: 3.10.0

---

# Public Methods

## addCollidesWith

### <instance> addCollidesWith(category)

**Description:**

Adds the given Collision Category to the list of those that this

Arcade Physics Body will collide with.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| category | number | No | The collision category to add. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Arcade.StaticBody](physics-arcade-staticbody.md) - This Game Object.

**Inherits:** [Phaser.Physics.Arcade.Components.Collision#addCollidesWith](../namespace/physics-arcade-components-collision.md)

> Source: [src/physics/arcade/components/Collision.js#L60](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/components/Collision.js#L60)  
> Since: 3.70.0

---

## deltaAbsX

### <instance> deltaAbsX()

**Description:**

The absolute (non-negative) change in this StaticBody's horizontal position from the previous step. Always zero.

**Returns:** number - Always zero for a Static Body.

> Source: [src/physics/arcade/StaticBody.js#L818](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticBody.js#L818)  
> Since: 3.0.0

---

## deltaAbsY

### <instance> deltaAbsY()

**Description:**

The absolute (non-negative) change in this StaticBody's vertical position from the previous step. Always zero.

**Returns:** number - Always zero for a Static Body.

> Source: [src/physics/arcade/StaticBody.js#L831](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticBody.js#L831)  
> Since: 3.0.0

---

## deltaX

### <instance> deltaX()

**Description:**

The change in this StaticBody's horizontal position from the previous step. Always zero.

**Returns:** number - The change in this StaticBody's velocity from the previous step. Always zero.

> Source: [src/physics/arcade/StaticBody.js#L844](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticBody.js#L844)  
> Since: 3.0.0

---

## deltaY

### <instance> deltaY()

**Description:**

The change in this StaticBody's vertical position from the previous step. Always zero.

**Returns:** number - The change in this StaticBody's velocity from the previous step. Always zero.

> Source: [src/physics/arcade/StaticBody.js#L857](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticBody.js#L857)  
> Since: 3.0.0

---

## deltaZ

### <instance> deltaZ()

**Description:**

The change in this StaticBody's rotation from the previous step. Always zero.

**Returns:** number - The change in this StaticBody's rotation from the previous step. Always zero.

> Source: [src/physics/arcade/StaticBody.js#L870](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticBody.js#L870)  
> Since: 3.0.0

---

## destroy

### <instance> destroy()

**Description:**

Disables this Body and marks it for destruction during the next step.

> Source: [src/physics/arcade/StaticBody.js#L883](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticBody.js#L883)  
> Since: 3.0.0

---

## drawDebug

### <instance> drawDebug(graphic)

**Description:**

Draws a graphical representation of the StaticBody for visual debugging purposes.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| graphic | [Phaser.GameObjects.Graphics](gameobjects-graphics.md) | No | The Graphics object to use for the debug drawing of the StaticBody. |
| --- | --- | --- | --- |

> Source: [src/physics/arcade/StaticBody.js#L896](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticBody.js#L896)  
> Since: 3.0.0

---

## getBounds

### <instance> getBounds(obj)

**Description:**

Returns the x and y coordinates of the top left and bottom right points of the StaticBody.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| obj | [Phaser.Types.Physics.Arcade.ArcadeBodyBounds](../typedef/types-physics-arcade.md) | No | The object which will hold the coordinates of the bounds. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Types.Physics.Arcade.ArcadeBodyBounds](../typedef/types-physics-arcade.md) - The same object that was passed with `x`, `y`, `right` and `bottom` values matching the respective values of the StaticBody.

> Source: [src/physics/arcade/StaticBody.js#L772](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticBody.js#L772)  
> Since: 3.0.0

---

## hitTest

### <instance> hitTest(x, y)

**Description:**

Checks to see if a given x,y coordinate is colliding with this Static Body.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The x coordinate to check against this body. |
| --- | --- | --- | --- |
| y | number | No | The y coordinate to check against this body. |

**Returns:** boolean - `true` if the given coordinate lies within this body, otherwise `false`.

> Source: [src/physics/arcade/StaticBody.js#L792](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticBody.js#L792)  
> Since: 3.0.0

---

## postUpdate

### <instance> postUpdate()

**Description:**

NOOP

> Source: [src/physics/arcade/StaticBody.js#L808](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticBody.js#L808)  
> Since: 3.12.0

---

## removeCollidesWith

### <instance> removeCollidesWith(category)

**Description:**

Removes the given Collision Category from the list of those that this

Arcade Physics Body will collide with.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| category | number | No | The collision category to add. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Arcade.StaticBody](physics-arcade-staticbody.md) - This Game Object.

**Inherits:** [Phaser.Physics.Arcade.Components.Collision#removeCollidesWith](../namespace/physics-arcade-components-collision.md)

> Source: [src/physics/arcade/components/Collision.js#L80](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/components/Collision.js#L80)  
> Since: 3.70.0

---

## reset

### <instance> reset([x], [y])

**Description:**

Resets this Static Body to its parent Game Object's position.

If `x` and `y` are given, the parent Game Object is placed there and this Static Body is centered on it.

Otherwise this Static Body is centered on the Game Object's current position.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | Yes | The x coordinate to reset the body to. If not given will use the parent Game Object's coordinate. |
| --- | --- | --- | --- |
| y | number | Yes | The y coordinate to reset the body to. If not given will use the parent Game Object's coordinate. |

> Source: [src/physics/arcade/StaticBody.js#L726](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticBody.js#L726)  
> Since: 3.0.0

---

## resetCollisionCategory

### <instance> resetCollisionCategory()

**Description:**

Resets the Collision Category and Mask back to the defaults,

which is to collide with everything.

**Returns:** [Phaser.Physics.Arcade.StaticBody](physics-arcade-staticbody.md) - This Game Object.

**Inherits:** [Phaser.Physics.Arcade.Components.Collision#resetCollisionCategory](../namespace/physics-arcade-components-collision.md)

> Source: [src/physics/arcade/components/Collision.js#L130](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/components/Collision.js#L130)  
> Since: 3.70.0

---

## setCircle

### <instance> setCircle(radius, [offsetX], [offsetY])

**Description:**

Sets this Static Body to have a circular body and sets its size and position.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| radius | number | No | The radius of the StaticBody, in pixels. |
| --- | --- | --- | --- |
| offsetX | number | Yes | The horizontal offset of the StaticBody from its Game Object, in pixels. |
| offsetY | number | Yes | The vertical offset of the StaticBody from its Game Object, in pixels. |

**Returns:** [Phaser.Physics.Arcade.StaticBody](physics-arcade-staticbody.md) - This Static Body object.

> Source: [src/physics/arcade/StaticBody.js#L670](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticBody.js#L670)  
> Since: 3.0.0

---

## setCollidesWith

### <instance> setCollidesWith(categories)

**Description:**

Sets all of the Collision Categories that this Arcade Physics Body

will collide with. You can either pass a single category value, or

an array of them.

Calling this method will reset all of the collision categories,

so only those passed to this method are enabled.

If you wish to add a new category to the existing mask, call

the `addCollisionCategory` method.

If you wish to reset the collision category and mask, call

the `resetCollisionCategory` method.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| categories | number | Array.<number> | No | The collision category to collide with, or an array of them. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Arcade.StaticBody](physics-arcade-staticbody.md) - This Game Object.

**Inherits:** [Phaser.Physics.Arcade.Components.Collision#setCollidesWith](../namespace/physics-arcade-components-collision.md)

> Source: [src/physics/arcade/components/Collision.js#L100](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/components/Collision.js#L100)  
> Since: 3.70.0

---

## setCollisionCategory

### <instance> setCollisionCategory(category)

**Description:**

Sets the Collision Category that this Arcade Physics Body

will use in order to determine what it can collide with.

It can only have one single category assigned to it.

If you wish to reset the collision category and mask, call

the `resetCollisionCategory` method.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| category | number | No | The collision category. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Arcade.StaticBody](physics-arcade-staticbody.md) - This Game Object.

**Inherits:** [Phaser.Physics.Arcade.Components.Collision#setCollisionCategory](../namespace/physics-arcade-components-collision.md)

> Source: [src/physics/arcade/components/Collision.js#L17](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/components/Collision.js#L17)  
> Since: 3.70.0

---

## setGameObject

### <instance> setGameObject(gameObject, [update])

**Description:**

Changes the Game Object this Body is bound to.

First it removes its reference from the old Game Object, then sets the new one.

You can optionally update the position and dimensions of this Body to reflect that of the new Game Object.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No |  | The new Game Object that will own this Body. |
| --- | --- | --- | --- | --- |
| update | boolean | Yes | true | Reposition and resize this Body to match the new Game Object? |

**Returns:** [Phaser.Physics.Arcade.StaticBody](physics-arcade-staticbody.md) - This Static Body object.

> Source: [src/physics/arcade/StaticBody.js#L508](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticBody.js#L508)  
> Since: 3.1.0

---

## setMass

### <instance> setMass(value)

**Description:**

Sets the Mass of the StaticBody. Will set the Mass to 0.1 if the value passed is less than or equal to zero.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The value to set the Mass to. Values of zero or less are changed to 0.1. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Arcade.StaticBody](physics-arcade-staticbody.md) - This Static Body object.

> Source: [src/physics/arcade/StaticBody.js#L940](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticBody.js#L940)  
> Since: 3.0.0

---

## setOffset

### <instance> setOffset(x, y)

**Description:**

Positions the Static Body at an offset from its Game Object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The horizontal offset of the Static Body from the Game Object's `x`. |
| --- | --- | --- | --- |
| y | number | No | The vertical offset of the Static Body from the Game Object's `y`. |

**Returns:** [Phaser.Physics.Arcade.StaticBody](physics-arcade-staticbody.md) - This Static Body object.

> Source: [src/physics/arcade/StaticBody.js#L573](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticBody.js#L573)  
> Since: 3.4.0

---

## setSize

### <instance> setSize([width], [height], [center])

**Description:**

Sets the size of the Static Body.

When `center` is true, also repositions it.

Resets the width and height to match current frame, if no width and height provided and a frame is found.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| width | number | Yes |  | The width of the Static Body in pixels. Cannot be zero. If not given, and the parent Game Object has a frame, it will use the frame width. |
| --- | --- | --- | --- | --- |
| height | number | Yes |  | The height of the Static Body in pixels. Cannot be zero. If not given, and the parent Game Object has a frame, it will use the frame height. |
| center | boolean | Yes | true | Place the Static Body's center on its Game Object's center. Only works if the Game Object has the `getCenter` method. |

**Returns:** [Phaser.Physics.Arcade.StaticBody](physics-arcade-staticbody.md) - This Static Body object.

> Source: [src/physics/arcade/StaticBody.js#L605](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticBody.js#L605)  
> Since: 3.0.0

---

## stop

### <instance> stop()

**Description:**

NOOP function. A Static Body cannot be stopped.

**Returns:** [Phaser.Physics.Arcade.StaticBody](physics-arcade-staticbody.md) - This Static Body object.

> Source: [src/physics/arcade/StaticBody.js#L759](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticBody.js#L759)  
> Since: 3.0.0

---

## updateCenter

### <instance> updateCenter()

**Description:**

Updates the StaticBody's `center` from its `position` and dimensions.

> Source: [src/physics/arcade/StaticBody.js#L715](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticBody.js#L715)  
> Since: 3.0.0

---

## updateFromGameObject

### <instance> updateFromGameObject()

**Description:**

Syncs the Static Body's position and size with its parent Game Object.

**Returns:** [Phaser.Physics.Arcade.StaticBody](physics-arcade-staticbody.md) - This Static Body object.

> Source: [src/physics/arcade/StaticBody.js#L544](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticBody.js#L544)  
> Since: 3.1.0

---

## willCollideWith

### <instance> willCollideWith(category)

**Description:**

Checks to see if the given Collision Category will collide with

this Arcade Physics object or not.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| category | number | No | Collision category value to test. |
| --- | --- | --- | --- |

**Returns:** boolean - `true` if the given category will collide with this object, otherwise `false`.

**Inherits:** [Phaser.Physics.Arcade.Components.Collision#willCollideWith](../namespace/physics-arcade-components-collision.md)

> Source: [src/physics/arcade/components/Collision.js#L42](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/components/Collision.js#L42)  
> Since: 3.70.0

---

## willDrawDebug

### <instance> willDrawDebug()

**Description:**

Indicates whether the StaticBody is going to be showing a debug visualization during postUpdate.

**Returns:** boolean - Whether or not the StaticBody is going to show the debug visualization during postUpdate.

> Source: [src/physics/arcade/StaticBody.js#L927](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticBody.js#L927)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [allowGravity](#allowgravity)

    - [allowGravity: boolean](#allowgravity-boolean)
  + [blocked](#blocked)

    - [blocked: Phaser.Types.Physics.Arcade.ArcadeBodyCollision](#blocked-phasertypesphysicsarcadearcadebodycollision)
  + [bottom](#bottom)

    - [bottom: number](#bottom-number)
  + [bounce](#bounce)

    - [bounce: Phaser.Math.Vector2](#bounce-phasermathvector2)
  + [center](#center)

    - [center: Phaser.Math.Vector2](#center-phasermathvector2)
  + [checkCollision](#checkcollision)

    - [checkCollision: Phaser.Types.Physics.Arcade.ArcadeBodyCollision](#checkcollision-phasertypesphysicsarcadearcadebodycollision)
  + [collideWorldBounds](#collideworldbounds)

    - [collideWorldBounds: boolean](#collideworldbounds-boolean)
  + [collisionCategory](#collisioncategory)

    - [collisionCategory: number](#collisioncategory-number)
  + [collisionMask](#collisionmask)

    - [collisionMask: number](#collisionmask-number)
  + [customSeparateX](#customseparatex)

    - [customSeparateX: boolean](#customseparatex-boolean)
  + [customSeparateY](#customseparatey)

    - [customSeparateY: boolean](#customseparatey-boolean)
  + [debugBodyColor](#debugbodycolor)

    - [debugBodyColor: number](#debugbodycolor-number)
  + [debugShowBody](#debugshowbody)

    - [debugShowBody: boolean](#debugshowbody-boolean)
  + [embedded](#embedded)

    - [embedded: boolean](#embedded-boolean)
  + [enable](#enable)

    - [enable: boolean](#enable-boolean)
  + [gameObject](#gameobject)

    - [gameObject: Phaser.GameObjects.GameObject](#gameobject-phasergameobjectsgameobject)
  + [gravity](#gravity)

    - [gravity: Phaser.Math.Vector2](#gravity-phasermathvector2)
  + [halfHeight](#halfheight)

    - [halfHeight: number](#halfheight-number)
  + [halfWidth](#halfwidth)

    - [halfWidth: number](#halfwidth-number)
  + [height](#height)

    - [height: number](#height-number)
  + [immovable](#immovable)

    - [immovable: boolean](#immovable-boolean)
  + [isBody](#isbody)

    - [isBody: boolean](#isbody-boolean)
  + [isCircle](#iscircle)

    - [isCircle: boolean](#iscircle-boolean)
  + [left](#left)

    - [left: number](#left-number)
  + [mass](#mass)

    - [mass: number](#mass-number)
  + [offset](#offset)

    - [offset: Phaser.Math.Vector2](#offset-phasermathvector2)
  + [onCollide](#oncollide)

    - [onCollide: boolean](#oncollide-boolean)
  + [onOverlap](#onoverlap)

    - [onOverlap: boolean](#onoverlap-boolean)
  + [onWorldBounds](#onworldbounds)

    - [onWorldBounds: boolean](#onworldbounds-boolean)
  + [overlapR](#overlapr)

    - [overlapR: number](#overlapr-number)
  + [overlapX](#overlapx)

    - [overlapX: number](#overlapx-number)
  + [overlapY](#overlapy)

    - [overlapY: number](#overlapy-number)
  + [physicsType](#physicstype)

    - [physicsType: number](#physicstype-number)
  + [position](#position)

    - [position: Phaser.Math.Vector2](#position-phasermathvector2)
  + [pushable](#pushable)

    - [pushable: boolean](#pushable-boolean)
  + [radius](#radius)

    - [radius: number](#radius-number)
  + [right](#right)

    - [right: number](#right-number)
  + [top](#top)

    - [top: number](#top-number)
  + [touching](#touching)

    - [touching: Phaser.Types.Physics.Arcade.ArcadeBodyCollision](#touching-phasertypesphysicsarcadearcadebodycollision)
  + [velocity](#velocity)

    - [velocity: Phaser.Math.Vector2](#velocity-phasermathvector2)
  + [wasTouching](#wastouching)

    - [wasTouching: Phaser.Types.Physics.Arcade.ArcadeBodyCollision](#wastouching-phasertypesphysicsarcadearcadebodycollision)
  + [width](#width)

    - [width: number](#width-number)
  + [world](#world)

    - [world: Phaser.Physics.Arcade.World](#world-phaserphysicsarcadeworld)
  + [x](#x)

    - [x: number](#x-number)
  + [y](#y)

    - [y: number](#y-number)
* [Private Members](#private-members)

  + [\_dx](#_dx)

    - [\_dx: number](#_dx-number)
  + [\_dy](#_dy)

    - [\_dy: number](#_dy-number)
* [Public Methods](#public-methods)

  + [addCollidesWith](#addcollideswith)

    - [<instance> addCollidesWith(category)](#instance-addcollideswithcategory)
  + [deltaAbsX](#deltaabsx)

    - [<instance> deltaAbsX()](#instance-deltaabsx)
  + [deltaAbsY](#deltaabsy)

    - [<instance> deltaAbsY()](#instance-deltaabsy)
  + [deltaX](#deltax)

    - [<instance> deltaX()](#instance-deltax)
  + [deltaY](#deltay)

    - [<instance> deltaY()](#instance-deltay)
  + [deltaZ](#deltaz)

    - [<instance> deltaZ()](#instance-deltaz)
  + [destroy](#destroy)

    - [<instance> destroy()](#instance-destroy)
  + [drawDebug](#drawdebug)

    - [<instance> drawDebug(graphic)](#instance-drawdebuggraphic)
  + [getBounds](#getbounds)

    - [<instance> getBounds(obj)](#instance-getboundsobj)
  + [hitTest](#hittest)

    - [<instance> hitTest(x, y)](#instance-hittestx-y)
  + [postUpdate](#postupdate)

    - [<instance> postUpdate()](#instance-postupdate)
  + [removeCollidesWith](#removecollideswith)

    - [<instance> removeCollidesWith(category)](#instance-removecollideswithcategory)
  + [reset](#reset)

    - [<instance> reset([x], [y])](#instance-resetx-y)
  + [resetCollisionCategory](#resetcollisioncategory)

    - [<instance> resetCollisionCategory()](#instance-resetcollisioncategory)
  + [setCircle](#setcircle)

    - [<instance> setCircle(radius, [offsetX], [offsetY])](#instance-setcircleradius-offsetx-offsety)
  + [setCollidesWith](#setcollideswith)

    - [<instance> setCollidesWith(categories)](#instance-setcollideswithcategories)
  + [setCollisionCategory](#setcollisioncategory)

    - [<instance> setCollisionCategory(category)](#instance-setcollisioncategorycategory)
  + [setGameObject](#setgameobject)

    - [<instance> setGameObject(gameObject, [update])](#instance-setgameobjectgameobject-update)
  + [setMass](#setmass)

    - [<instance> setMass(value)](#instance-setmassvalue)
  + [setOffset](#setoffset)

    - [<instance> setOffset(x, y)](#instance-setoffsetx-y)
  + [setSize](#setsize)

    - [<instance> setSize([width], [height], [center])](#instance-setsizewidth-height-center)
  + [stop](#stop)

    - [<instance> stop()](#instance-stop)
  + [updateCenter](#updatecenter)

    - [<instance> updateCenter()](#instance-updatecenter)
  + [updateFromGameObject](#updatefromgameobject)

    - [<instance> updateFromGameObject()](#instance-updatefromgameobject)
  + [willCollideWith](#willcollidewith)

    - [<instance> willCollideWith(category)](#instance-willcollidewithcategory)
  + [willDrawDebug](#willdrawdebug)

    - [<instance> willDrawDebug()](#instance-willdrawdebug)

Back to top

©2025[Phaser](https://docs.phaser.io)



StaticBody