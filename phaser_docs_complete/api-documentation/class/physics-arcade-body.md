# Body

Phaser.Physics.Arcade.Body

A Dynamic Arcade Body.

Its static counterpart is [Phaser.Physics.Arcade.StaticBody](Phaser.Physics.Arcade.StaticBody.md).

**Constructor**

`new Body(world, [gameObject])`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| world | [Phaser.Physics.Arcade.World](physics-arcade-world.md) | No | The Arcade Physics simulation this Body belongs to. |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | Yes | The Game Object this Body belongs to. As of Phaser 3.60 this is now optional. |

---

**Scope**: static

**Extends**

> [Phaser.Physics.Arcade.Components.Collision](../namespace/physics-arcade-components-collision.md)

> Source: [src/physics/arcade/Body.js#L17](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L17)  
> Since: 3.0.0

# Public Members

## acceleration

### acceleration: [Phaser.Math.Vector2](math-vector2.md)

**Description:**

The Body's change in velocity, in pixels per second squared.

> Source: [src/physics/arcade/Body.js#L359](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L359)  
> Since: 3.0.0

---

## allowDrag

### allowDrag: boolean

**Description:**

Whether this Body's velocity is affected by its `drag`.

> Source: [src/physics/arcade/Body.js#L368](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L368)  
> Since: 3.0.0

---

## allowGravity

### allowGravity: boolean

**Description:**

Whether this Body's position is affected by gravity (local or world).

> Source: [src/physics/arcade/Body.js#L398](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L398)  
> Since: 3.0.0

---

## allowRotation

### allowRotation: boolean

**Description:**

Whether this Body's `rotation` is affected by its angular acceleration and angular velocity.

> Source: [src/physics/arcade/Body.js#L217](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L217)  
> Since: 3.0.0

---

## angle

### angle: number

**Description:**

The calculated angle of this Body's velocity vector, in radians, during the last step.

> Source: [src/physics/arcade/Body.js#L596](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L596)  
> Since: 3.0.0

---

## angularAcceleration

### angularAcceleration: number

**Description:**

The Body's angular acceleration (change in angular velocity), in degrees per second squared.

> Source: [src/physics/arcade/Body.js#L553](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L553)  
> Since: 3.0.0

---

## angularDrag

### angularDrag: number

**Description:**

Loss of angular velocity due to angular movement, in degrees per second.

Angular drag is applied only when angular acceleration is zero.

> Source: [src/physics/arcade/Body.js#L563](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L563)  
> Since: 3.0.0

---

## angularVelocity

### angularVelocity: number

**Description:**

The rate of change of this Body's `rotation`, in degrees per second.

> Source: [src/physics/arcade/Body.js#L543](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L543)  
> Since: 3.0.0

---

## blocked

### blocked: [Phaser.Types.Physics.Arcade.ArcadeBodyCollision](../typedef/types-physics-arcade.md)

**Description:**

Whether this Body is colliding with a Static Body, a tile, or the world boundary.

In a collision with a Static Body, if this Body has zero velocity then `embedded` will be set instead.

> Source: [src/physics/arcade/Body.js#L802](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L802)  
> Since: 3.0.0

---

## bottom

### bottom: number

**Description:**

The bottom edge of this Body.

> Source: [src/physics/arcade/Body.js#L2770](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L2770)  
> Since: 3.0.0

---

## bounce

### bounce: [Phaser.Math.Vector2](math-vector2.md)

**Description:**

Rebound following a collision, relative to 1.

> Source: [src/physics/arcade/Body.js#L421](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L421)  
> Since: 3.0.0

---

## center

### center: [Phaser.Math.Vector2](math-vector2.md)

**Description:**

The center of the Body.

The midpoint of its `position` (top-left corner) and its bottom-right corner.

> Source: [src/physics/arcade/Body.js#L319](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L319)  
> Since: 3.0.0

---

## checkCollision

### checkCollision: [Phaser.Types.Physics.Arcade.ArcadeBodyCollision](../typedef/types-physics-arcade.md)

**Description:**

Whether this Body is checked for collisions and for which directions.

You can set `checkCollision.none = true` to disable collision checks.

> Source: [src/physics/arcade/Body.js#L768](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L768)  
> Since: 3.0.0

---

## collideWorldBounds

### collideWorldBounds: boolean

**Description:**

Whether this Body interacts with the world boundary.

> Source: [src/physics/arcade/Body.js#L758](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L758)  
> Since: 3.0.0

---

## collisionCategory

### collisionCategory: number

**Description:**

The Arcade Physics Body Collision Category.

This can be set to any valid collision bitfield value.

See the `setCollisionCategory` method for more details.

> Source: [src/physics/arcade/Body.js#L837](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L837)  
> Since: 3.70.0

---

## collisionMask

### collisionMask: number

**Description:**

The Arcade Physics Body Collision Mask.

See the `setCollidesWith` method for more details.

> Source: [src/physics/arcade/Body.js#L850](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L850)  
> Since: 3.70.0

---

## customBoundsRectangle

### customBoundsRectangle: [Phaser.Geom.Rectangle](geom-rectangle.md)

**Description:**

The rectangle used for world boundary collisions.

By default it is set to the world boundary rectangle. Or, if this Body was

created by a Physics Group, then whatever rectangle that Group defined.

You can also change it by using the `Body.setBoundsRectangle` method.

> Source: [src/physics/arcade/Body.js#L441](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L441)  
> Since: 3.20

---

## customSeparateX

### customSeparateX: boolean

**Description:**

A flag disabling the default horizontal separation of colliding bodies.

Pass your own `collideCallback` to the collider.

> Source: [src/physics/arcade/Body.js#L696](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L696)  
> Since: 3.0.0

---

## customSeparateY

### customSeparateY: boolean

**Description:**

A flag disabling the default vertical separation of colliding bodies.

Pass your own `collideCallback` to the collider.

> Source: [src/physics/arcade/Body.js#L707](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L707)  
> Since: 3.0.0

---

## debugBodyColor

### debugBodyColor: number

**Description:**

The color of this Body on the debug display.

> Source: [src/physics/arcade/Body.js#L135](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L135)  
> Since: 3.0.0

---

## debugShowBody

### debugShowBody: boolean

**Description:**

Whether the Body is drawn to the debug display.

> Source: [src/physics/arcade/Body.js#L117](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L117)  
> Since: 3.0.0

---

## debugShowVelocity

### debugShowVelocity: boolean

**Description:**

Whether the Body's velocity is drawn to the debug display.

> Source: [src/physics/arcade/Body.js#L126](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L126)  
> Since: 3.0.0

---

## deltaMax

### deltaMax: [Phaser.Math.Vector2](math-vector2.md)

**Description:**

The Body's absolute maximum change in position, in pixels per step.

> Source: [src/physics/arcade/Body.js#L350](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L350)  
> Since: 3.0.0

---

## directControl

### directControl: boolean

**Description:**

Is this Body under direct control, outside of the physics engine? For example,

are you trying to move it via a Tween? Or have it follow a path? If so then

you can enable this boolean so that the Body will calculate its velocity based

purely on its change in position each frame. This allows you to then tween

the position and still have it collide with other objects. However, setting

the velocity will have no impact on this Body while this is set.

> Source: [src/physics/arcade/Body.js#L935](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L935)  
> Since: 3.70.0

---

## drag

### drag: [Phaser.Math.Vector2](math-vector2.md)

**Description:**

When `useDamping` is false (the default), this is absolute loss of velocity due to movement, in pixels per second squared.

When `useDamping` is true, this is a damping multiplier between 0 and 1.

A value of 0 means the Body stops instantly.

A value of 0.01 mean the Body keeps 1% of its velocity per second, losing 99%.

A value of 0.1 means the Body keeps 10% of its velocity per second, losing 90%.

A value of 1 means the Body loses no velocity.

You can use very small values (e.g., 0.001) to stop the Body quickly.

The x and y components are applied separately.

Drag is applied only when `acceleration` is zero.

> Source: [src/physics/arcade/Body.js#L378](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L378)  
> Since: 3.0.0

---

## embedded

### embedded: boolean

**Description:**

Whether this Body is overlapped with another and both are not moving, on at least one axis.

> Source: [src/physics/arcade/Body.js#L748](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L748)  
> Since: 3.0.0

---

## enable

### enable: boolean

**Description:**

Whether this Body is updated by the physics simulation.

> Source: [src/physics/arcade/Body.js#L144](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L144)  
> Since: 3.0.0

---

## facing

### facing: number

**Description:**

The direction of the Body's velocity, as calculated during the last step.

This is a numeric constant value (FACING\_UP, FACING\_DOWN, FACING\_LEFT, FACING\_RIGHT).

If the Body is moving on both axes, this describes motion on the vertical axis only.

> Source: [src/physics/arcade/Body.js#L616](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L616)  
> Since: 3.0.0

---

## friction

### friction: [Phaser.Math.Vector2](math-vector2.md)

**Description:**

If this Body is `immovable` and in motion, `friction` is the proportion of this Body's motion received by the riding Body on each axis, relative to 1.

The horizontal component (x) is applied only when two colliding Bodies are separated vertically.

The vertical component (y) is applied only when two colliding Bodies are separated horizontally.

The default value (1, 0) moves the riding Body horizontally in equal proportion to this Body and vertically not at all.

> Source: [src/physics/arcade/Body.js#L513](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L513)  
> Since: 3.0.0

---

## gameObject

### gameObject: [Phaser.GameObjects.GameObject](gameobjects-gameobject.md)

**Description:**

The Game Object this Body belongs to.

As of Phaser 3.60 this is now optional and can be undefined.

> Source: [src/physics/arcade/Body.js#L79](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L79)  
> Since: 3.0.0

---

## gravity

### gravity: [Phaser.Math.Vector2](math-vector2.md)

**Description:**

Acceleration due to gravity (specific to this Body), in pixels per second squared.

Total gravity is the sum of this vector and the simulation's `gravity`.

> Source: [src/physics/arcade/Body.js#L410](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L410)  
> Since: 3.0.0

---

## halfHeight

### halfHeight: number

**Description:**

Half the Body's height, in pixels.

> Source: [src/physics/arcade/Body.js#L310](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L310)  
> Since: 3.0.0

---

## halfWidth

### halfWidth: number

**Description:**

Half the Body's width, in pixels.

> Source: [src/physics/arcade/Body.js#L301](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L301)  
> Since: 3.0.0

---

## height

### height: number

**Description:**

The height of the Body, in pixels.

If the Body is circular, this is also the diameter.

If you wish to change the height use the `Body.setSize` method.

> Source: [src/physics/arcade/Body.js#L260](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L260)  
> Since: 3.0.0

---

## immovable

### immovable: boolean

**Description:**

Whether this Body can be moved by collisions with another Body.

> Source: [src/physics/arcade/Body.js#L632](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L632)  
> Since: 3.0.0

---

## isBody

### isBody: boolean

**Description:**

A quick-test flag that signifies this is a Body, used in the World collision handler.

> Source: [src/physics/arcade/Body.js#L90](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L90)  
> Since: 3.60.0

---

## isCircle

### isCircle: boolean

**Description:**

Whether this Body is circular (true) or rectangular (false).

> Source: [src/physics/arcade/Body.js#L154](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L154)  
> Since: 3.0.0

---

## left

### left: number

**Description:**

The left edge of the Body. Identical to x.

> Source: [src/physics/arcade/Body.js#L2719](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L2719)  
> Since: 3.0.0

---

## mass

### mass: number

**Description:**

The Body's inertia, relative to a default unit (1).

With `bounce`, this affects the exchange of momentum (velocities) during collisions.

> Source: [src/physics/arcade/Body.js#L585](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L585)  
> Since: 3.0.0

---

## maxAngular

### maxAngular: number

**Description:**

The Body's maximum angular velocity, in degrees per second.

> Source: [src/physics/arcade/Body.js#L575](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L575)  
> Since: 3.0.0

---

## maxSpeed

### maxSpeed: number

**Description:**

The maximum speed this Body is allowed to reach, in pixels per second.

If not negative it limits the scalar value of speed.

Any negative value means no maximum is being applied (the default).

> Source: [src/physics/arcade/Body.js#L499](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L499)  
> Since: 3.16.0

---

## maxVelocity

### maxVelocity: [Phaser.Math.Vector2](math-vector2.md)

**Description:**

The absolute maximum velocity of this body, in pixels per second.

The horizontal and vertical components are applied separately.

> Source: [src/physics/arcade/Body.js#L489](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L489)  
> Since: 3.0.0

---

## moves

### moves: boolean

**Description:**

Whether the Body's position and rotation are affected by its velocity, acceleration, drag, and gravity.

> Source: [src/physics/arcade/Body.js#L686](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L686)  
> Since: 3.0.0

---

## newVelocity

### newVelocity: [Phaser.Math.Vector2](math-vector2.md)

**Description:**

The Body's change in position (due to velocity) at the last step, in pixels.

The size of this value depends on the simulation's step rate.

> Source: [src/physics/arcade/Body.js#L338](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L338)  
> Since: 3.0.0

---

## offset

### offset: [Phaser.Math.Vector2](math-vector2.md)

**Description:**

The offset of this Body's position from its Game Object's position, in source pixels.

> Source: [src/physics/arcade/Body.js#L177](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L177)  
> Since: 3.0.0

---

## onCollide

### onCollide: boolean

**Description:**

Whether the simulation emits a `collide` event when this Body collides with another.

> Source: [src/physics/arcade/Body.js#L467](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L467)  
> Since: 3.0.0

---

## onOverlap

### onOverlap: boolean

**Description:**

Whether the simulation emits an `overlap` event when this Body overlaps with another.

> Source: [src/physics/arcade/Body.js#L478](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L478)  
> Since: 3.0.0

---

## onWorldBounds

### onWorldBounds: boolean

**Description:**

Whether the simulation emits a `worldbounds` event when this Body collides with the world boundary

(and `collideWorldBounds` is also true).

> Source: [src/physics/arcade/Body.js#L455](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L455)  
> Since: 3.0.0

---

## overlapR

### overlapR: number

**Description:**

The amount of overlap (before separation), if this Body is circular and colliding with another circular body.

> Source: [src/physics/arcade/Body.js#L738](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L738)  
> Since: 3.0.0

---

## overlapX

### overlapX: number

**Description:**

The amount of horizontal overlap (before separation), if this Body is colliding with another.

> Source: [src/physics/arcade/Body.js#L718](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L718)  
> Since: 3.0.0

---

## overlapY

### overlapY: number

**Description:**

The amount of vertical overlap (before separation), if this Body is colliding with another.

> Source: [src/physics/arcade/Body.js#L728](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L728)  
> Since: 3.0.0

---

## physicsType

### physicsType: number

**Description:**

The Body's physics type (dynamic or static).

> Source: [src/physics/arcade/Body.js#L826](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L826)  
> Since: 3.0.0

---

## position

### position: [Phaser.Math.Vector2](math-vector2.md)

**Description:**

The position of this Body within the simulation.

> Source: [src/physics/arcade/Body.js#L187](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L187)  
> Since: 3.0.0

---

## preRotation

### preRotation: number

**Description:**

The Body rotation, in degrees, during the previous step.

> Source: [src/physics/arcade/Body.js#L238](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L238)  
> Since: 3.0.0

---

## prev

### prev: [Phaser.Math.Vector2](math-vector2.md)

**Description:**

The position of this Body during the previous step.

> Source: [src/physics/arcade/Body.js#L199](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L199)  
> Since: 3.0.0

---

## prevFrame

### prevFrame: [Phaser.Math.Vector2](math-vector2.md)

**Description:**

The position of this Body during the previous frame.

> Source: [src/physics/arcade/Body.js#L208](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L208)  
> Since: 3.20.0

---

## pushable

### pushable: boolean

**Description:**

Sets if this Body can be pushed by another Body.

A body that cannot be pushed will reflect back all of the velocity it is given to the

colliding body. If that body is also not pushable, then the separation will be split

between them evenly.

If you want your body to never move or seperate at all, see the `setImmovable` method.

By default, Dynamic Bodies are always pushable.

> Source: [src/physics/arcade/Body.js#L642](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L642)  
> Since: 3.50.0

---

## radius

### radius: number

**Description:**

If this Body is circular, this is the unscaled radius of the Body, as set by setCircle(), in source pixels.

The true radius is equal to `halfWidth`.

> Source: [src/physics/arcade/Body.js#L165](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L165)  
> Since: 3.0.0

---

## right

### right: number

**Description:**

The right edge of the Body.

> Source: [src/physics/arcade/Body.js#L2736](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L2736)  
> Since: 3.0.0

---

## rotation

### rotation: number

**Description:**

This body's rotation, in degrees, based on its angular acceleration and angular velocity.

The Body's rotation controls the `angle` of its Game Object.

It doesn't rotate the Body's own geometry, which is always an axis-aligned rectangle or a circle.

> Source: [src/physics/arcade/Body.js#L227](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L227)  
> Since: 3.0.0

---

## slideFactor

### slideFactor: [Phaser.Math.Vector2](math-vector2.md)

**Description:**

The Slide Factor of this Body.

The Slide Factor controls how much velocity is preserved when

this Body is pushed by another Body.

The default value is 1, which means that it will take on all

velocity given in the push. You can adjust this value to control

how much velocity is retained by this Body when the push ends.

A value of 0, for example, will allow this Body to be pushed

but then remain completely still after the push ends, such as

you see in a game like Sokoban.

Or you can set a mid-point, such as 0.25 which will allow it

to keep 25% of the original velocity when the push ends. You

can combine this with the `setDrag()` method to create deceleration.

> Source: [src/physics/arcade/Body.js#L661](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L661)  
> Since: 3.70.0

---

## sourceHeight

### sourceHeight: number

**Description:**

The unscaled height of the Body, in source pixels, as set by setSize().

The default is the height of the Body's Game Object's texture frame.

> Source: [src/physics/arcade/Body.js#L284](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L284)  
> Since: 3.0.0

---

## sourceWidth

### sourceWidth: number

**Description:**

The unscaled width of the Body, in source pixels, as set by setSize().

The default is the width of the Body's Game Object's texture frame.

> Source: [src/physics/arcade/Body.js#L273](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L273)  
> Since: 3.0.0

---

## speed

### speed: number

**Description:**

The calculated magnitude of the Body's velocity, in pixels per second, during the last step.

> Source: [src/physics/arcade/Body.js#L606](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L606)  
> Since: 3.0.0

---

## syncBounds

### syncBounds: boolean

**Description:**

Whether to automatically synchronize this Body's dimensions to the dimensions of its Game Object's visual bounds.

> Source: [src/physics/arcade/Body.js#L815](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L815)  
> Since: 3.0.0

---

## top

### top: number

**Description:**

The top edge of the Body. Identical to y.

> Source: [src/physics/arcade/Body.js#L2753](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L2753)  
> Since: 3.0.0

---

## touching

### touching: [Phaser.Types.Physics.Arcade.ArcadeBodyCollision](../typedef/types-physics-arcade.md)

**Description:**

Whether this Body is colliding with a Body or Static Body and in which direction.

In a collision where both bodies have zero velocity, `embedded` will be set instead.

> Source: [src/physics/arcade/Body.js#L778](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L778)  
> Since: 3.0.0

---

## transform

### transform: object

**Description:**

Transformations applied to this Body.

> Source: [src/physics/arcade/Body.js#L100](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L100)  
> Since: 3.4.0

---

## useDamping

### useDamping: boolean

**Description:**

If this Body is using `drag` for deceleration this property controls how the drag is applied.

If set to `true` drag will use a damping effect rather than a linear approach. If you are

creating a game where the Body moves freely at any angle (i.e. like the way the ship moves in

the game Asteroids) then you will get a far smoother and more visually correct deceleration

by using damping, avoiding the axis-drift that is prone with linear deceleration.

If you enable this property then you should use far smaller `drag` values than with linear, as

they are used as a multiplier on the velocity. Values such as 0.05 will give a nice slow

deceleration.

> Source: [src/physics/arcade/Body.js#L525](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L525)  
> Since: 3.10.0

---

## velocity

### velocity: [Phaser.Math.Vector2](math-vector2.md)

**Description:**

The Body's velocity, in pixels per second.

> Source: [src/physics/arcade/Body.js#L329](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L329)  
> Since: 3.0.0

---

## wasTouching

### wasTouching: [Phaser.Types.Physics.Arcade.ArcadeBodyCollision](../typedef/types-physics-arcade.md)

**Description:**

This Body's `touching` value during the previous step.

> Source: [src/physics/arcade/Body.js#L791](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L791)  
> Since: 3.0.0

---

## width

### width: number

**Description:**

The width of the Body, in pixels.

If the Body is circular, this is also the diameter.

If you wish to change the width use the `Body.setSize` method.

> Source: [src/physics/arcade/Body.js#L247](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L247)  
> Since: 3.0.0

---

## world

### world: [Phaser.Physics.Arcade.World](physics-arcade-world.md)

**Description:**

The Arcade Physics simulation this Body belongs to.

> Source: [src/physics/arcade/Body.js#L70](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L70)  
> Since: 3.0.0

---

## worldBounce

### worldBounce: [Phaser.Math.Vector2](math-vector2.md)

**Description:**

Rebound following a collision with the world boundary, relative to 1.

If null, `bounce` is used instead.

> Source: [src/physics/arcade/Body.js#L430](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L430)  
> Since: 3.0.0

---

## x

### x: number

**Description:**

The Bodys horizontal position (left edge).

> Source: [src/physics/arcade/Body.js#L2677](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L2677)  
> Since: 3.0.0

---

## y

### y: number

**Description:**

The Bodys vertical position (top edge).

> Source: [src/physics/arcade/Body.js#L2698](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L2698)  
> Since: 3.0.0

---

# Private Members

## \_bounds

### \_bounds: [Phaser.Geom.Rectangle](geom-rectangle.md)

**Description:**

Stores the Game Object's bounds.

**Access:** private

> Source: [src/physics/arcade/Body.js#L925](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L925)  
> Since: 3.0.0

---

## \_dx

### \_dx: number

**Description:**

The calculated change in the Body's horizontal position during the last step.

**Access:** private

> Source: [src/physics/arcade/Body.js#L881](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L881)  
> Since: 3.0.0

---

## \_dy

### \_dy: number

**Description:**

The calculated change in the Body's vertical position during the last step.

**Access:** private

> Source: [src/physics/arcade/Body.js#L892](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L892)  
> Since: 3.0.0

---

## \_sx

### \_sx: number

**Description:**

Cached horizontal scale of the Body's Game Object.

**Access:** private

> Source: [src/physics/arcade/Body.js#L861](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L861)  
> Since: 3.0.0

---

## \_sy

### \_sy: number

**Description:**

Cached vertical scale of the Body's Game Object.

**Access:** private

> Source: [src/physics/arcade/Body.js#L871](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L871)  
> Since: 3.0.0

---

## \_tx

### \_tx: number

**Description:**

The final calculated change in the Body's horizontal position as of `postUpdate`.

**Access:** private

> Source: [src/physics/arcade/Body.js#L903](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L903)  
> Since: 3.22.0

---

## \_ty

### \_ty: number

**Description:**

The final calculated change in the Body's vertical position as of `postUpdate`.

**Access:** private

> Source: [src/physics/arcade/Body.js#L914](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L914)  
> Since: 3.22.0

---

## autoFrame

### autoFrame: [Phaser.Math.Vector2](math-vector2.md)

**Description:**

Stores the previous position of the Game Object when directControl is enabled.

**Access:** private

> Source: [src/physics/arcade/Body.js#L949](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L949)  
> Since: 3.70.0

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

**Returns:** [Phaser.Physics.Arcade.Body](physics-arcade-body.md) - This Game Object.

**Inherits:** [Phaser.Physics.Arcade.Components.Collision#addCollidesWith](../namespace/physics-arcade-components-collision.md)

> Source: [src/physics/arcade/components/Collision.js#L60](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/components/Collision.js#L60)  
> Since: 3.70.0

---

## checkWorldBounds

### <instance> checkWorldBounds()

**Description:**

Checks for collisions between this Body and the world boundary and separates them.

**Returns:** boolean - True if this Body is colliding with the world boundary.

> Source: [src/physics/arcade/Body.js#L1328](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L1328)  
> Since: 3.0.0

---

## deltaAbsX

### <instance> deltaAbsX()

**Description:**

The absolute (non-negative) change in this Body's horizontal position from the previous step.

**Returns:** number - The delta value.

> Source: [src/physics/arcade/Body.js#L1722](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L1722)  
> Since: 3.0.0

---

## deltaAbsY

### <instance> deltaAbsY()

**Description:**

The absolute (non-negative) change in this Body's vertical position from the previous step.

**Returns:** number - The delta value.

> Source: [src/physics/arcade/Body.js#L1735](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L1735)  
> Since: 3.0.0

---

## deltaX

### <instance> deltaX()

**Description:**

The change in this Body's horizontal position from the previous step.

This value is set during the Body's update phase.

As a Body can update multiple times per step this may not hold the final

delta value for the Body. In this case, please see the `deltaXFinal` method.

**Returns:** number - The delta value.

> Source: [src/physics/arcade/Body.js#L1748](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L1748)  
> Since: 3.0.0

---

## deltaXFinal

### <instance> deltaXFinal()

**Description:**

The change in this Body's horizontal position from the previous game update.

This value is set during the `postUpdate` phase and takes into account the

`deltaMax` and final position of the Body.

Because this value is not calculated until `postUpdate`, you must listen for it

during a Scene `POST_UPDATE` or `RENDER` event, and not in `update`, as it will

not be calculated by that point. If you *do* use these values in `update` they

will represent the delta from the *previous* game frame.

**Returns:** number - The final delta x value.

> Source: [src/physics/arcade/Body.js#L1782](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L1782)  
> Since: 3.22.0

---

## deltaY

### <instance> deltaY()

**Description:**

The change in this Body's vertical position from the previous step.

This value is set during the Body's update phase.

As a Body can update multiple times per step this may not hold the final

delta value for the Body. In this case, please see the `deltaYFinal` method.

**Returns:** number - The delta value.

> Source: [src/physics/arcade/Body.js#L1765](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L1765)  
> Since: 3.0.0

---

## deltaYFinal

### <instance> deltaYFinal()

**Description:**

The change in this Body's vertical position from the previous game update.

This value is set during the `postUpdate` phase and takes into account the

`deltaMax` and final position of the Body.

Because this value is not calculated until `postUpdate`, you must listen for it

during a Scene `POST_UPDATE` or `RENDER` event, and not in `update`, as it will

not be calculated by that point. If you *do* use these values in `update` they

will represent the delta from the *previous* game frame.

**Returns:** number - The final delta y value.

> Source: [src/physics/arcade/Body.js#L1803](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L1803)  
> Since: 3.22.0

---

## deltaZ

### <instance> deltaZ()

**Description:**

The change in this Body's rotation from the previous step, in degrees.

**Returns:** number - The delta value.

> Source: [src/physics/arcade/Body.js#L1824](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L1824)  
> Since: 3.0.0

---

## destroy

### <instance> destroy()

**Description:**

Disables this Body and marks it for deletion by the simulation.

> Source: [src/physics/arcade/Body.js#L1837](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L1837)  
> Since: 3.0.0

---

## drawDebug

### <instance> drawDebug(graphic)

**Description:**

Draws this Body and its velocity, if enabled.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| graphic | [Phaser.GameObjects.Graphics](gameobjects-graphics.md) | No | The Graphics object to draw on. |
| --- | --- | --- | --- |

> Source: [src/physics/arcade/Body.js#L1853](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L1853)  
> Since: 3.0.0

---

## getBounds

### <instance> getBounds(obj)

**Description:**

Copies the coordinates of this Body's edges into an object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| obj | [Phaser.Types.Physics.Arcade.ArcadeBodyBounds](../typedef/types-physics-arcade.md) | No | An object to copy the values into. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Types.Physics.Arcade.ArcadeBodyBounds](../typedef/types-physics-arcade.md) - - An object with {x, y, right, bottom}.

> Source: [src/physics/arcade/Body.js#L1630](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L1630)  
> Since: 3.0.0

---

## hitTest

### <instance> hitTest(x, y)

**Description:**

Tests if the coordinates are within this Body.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The horizontal coordinate. |
| --- | --- | --- | --- |
| y | number | No | The vertical coordinate. |

**Returns:** boolean - True if (x, y) is within this Body.

> Source: [src/physics/arcade/Body.js#L1650](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L1650)  
> Since: 3.0.0

---

## onCeiling

### <instance> onCeiling()

**Description:**

Whether this Body is touching a tile or the world boundary while moving up.

**Returns:** boolean - True if touching.

> Source: [src/physics/arcade/Body.js#L1694](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L1694)  
> Since: 3.0.0

---

## onFloor

### <instance> onFloor()

**Description:**

Whether this Body is touching a tile or the world boundary while moving down.

**Returns:** boolean - True if touching.

> Source: [src/physics/arcade/Body.js#L1680](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L1680)  
> Since: 3.0.0

---

## onWall

### <instance> onWall()

**Description:**

Whether this Body is touching a tile or the world boundary while moving left or right.

**Returns:** boolean - True if touching.

> Source: [src/physics/arcade/Body.js#L1708](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L1708)  
> Since: 3.0.0

---

## postUpdate

### <instance> postUpdate()

**Description:**

Feeds the Body results back into the parent Game Object.

This method is called every game frame, regardless if the world steps or not.

> Source: [src/physics/arcade/Body.js#L1228](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L1228)  
> Since: 3.0.0

---

## preUpdate

### <instance> preUpdate(willStep, delta)

**Description:**

Syncs the position body position with the parent Game Object.

This method is called every game frame, regardless if the world steps or not.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| willStep | boolean | No | Will this Body run an update as well? |
| --- | --- | --- | --- |
| delta | number | No | The delta time, in seconds, elapsed since the last frame. |

> Source: [src/physics/arcade/Body.js#L1111](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L1111)  
> Since: 3.17.0

---

## processX

### <instance> processX(x, [vx], [left], [right])

**Description:**

This is an internal handler, called by the `ProcessX` function as part

of the collision step. You should almost never call this directly.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The amount to add to the Body position. |
| --- | --- | --- | --- |
| vx | number | Yes | The amount to add to the Body velocity. |
| left | boolean | Yes | Set the blocked.left value? |
| right | boolean | Yes | Set the blocked.right value? |

> Source: [src/physics/arcade/Body.js#L2601](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L2601)  
> Since: 3.50.0

---

## processY

### <instance> processY(y, [vy], [up], [down])

**Description:**

This is an internal handler, called by the `ProcessY` function as part

of the collision step. You should almost never call this directly.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| y | number | No | The amount to add to the Body position. |
| --- | --- | --- | --- |
| vy | number | Yes | The amount to add to the Body velocity. |
| up | boolean | Yes | Set the blocked.up value? |
| down | boolean | Yes | Set the blocked.down value? |

> Source: [src/physics/arcade/Body.js#L2639](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L2639)  
> Since: 3.50.0

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

**Returns:** [Phaser.Physics.Arcade.Body](physics-arcade-body.md) - This Game Object.

**Inherits:** [Phaser.Physics.Arcade.Components.Collision#removeCollidesWith](../namespace/physics-arcade-components-collision.md)

> Source: [src/physics/arcade/components/Collision.js#L80](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/components/Collision.js#L80)  
> Since: 3.70.0

---

## reset

### <instance> reset(x, y)

**Description:**

Sets this Body's parent Game Object to the given coordinates and resets this Body at the new coordinates.

If the Body had any velocity or acceleration it is lost as a result of calling this.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The horizontal position to place the Game Object. |
| --- | --- | --- | --- |
| y | number | No | The vertical position to place the Game Object. |

> Source: [src/physics/arcade/Body.js#L1557](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L1557)  
> Since: 3.0.0

---

## resetCollisionCategory

### <instance> resetCollisionCategory()

**Description:**

Resets the Collision Category and Mask back to the defaults,

which is to collide with everything.

**Returns:** [Phaser.Physics.Arcade.Body](physics-arcade-body.md) - This Game Object.

**Inherits:** [Phaser.Physics.Arcade.Components.Collision#resetCollisionCategory](../namespace/physics-arcade-components-collision.md)

> Source: [src/physics/arcade/components/Collision.js#L130](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/components/Collision.js#L130)  
> Since: 3.70.0

---

## resetFlags

### <instance> resetFlags([clear])

**Description:**

Prepares the Body for a physics step by resetting the `wasTouching`, `touching` and `blocked` states.

This method is only called if the physics world is going to run a step this frame.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| clear | boolean | Yes | false | Set the `wasTouching` values to their defaults. |
| --- | --- | --- | --- | --- |

> Source: [src/physics/arcade/Body.js#L1066](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L1066)  
> Since: 3.18.0

---

## setAcceleration

### <instance> setAcceleration(x, [y])

**Description:**

Sets the Body's acceleration.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | No |  | The horizontal component, in pixels per second squared. |
| --- | --- | --- | --- | --- |
| y | number | Yes | "x" | The vertical component, in pixels per second squared. |

**Returns:** [Phaser.Physics.Arcade.Body](physics-arcade-body.md) - This Body object.

> Source: [src/physics/arcade/Body.js#L2202](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L2202)  
> Since: 3.0.0

---

## setAccelerationX

### <instance> setAccelerationX(value)

**Description:**

Sets the Body's horizontal acceleration.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The acceleration, in pixels per second squared. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Arcade.Body](physics-arcade-body.md) - This Body object.

> Source: [src/physics/arcade/Body.js#L2220](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L2220)  
> Since: 3.0.0

---

## setAccelerationY

### <instance> setAccelerationY(value)

**Description:**

Sets the Body's vertical acceleration.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The acceleration, in pixels per second squared. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Arcade.Body](physics-arcade-body.md) - This Body object.

> Source: [src/physics/arcade/Body.js#L2237](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L2237)  
> Since: 3.0.0

---

## setAllowDrag

### <instance> setAllowDrag([value])

**Description:**

Enables or disables drag.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| value | boolean | Yes | true | `true` to allow drag on this body, or `false` to disable it. |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Arcade.Body](physics-arcade-body.md) - This Body object.

> Source: [src/physics/arcade/Body.js#L2254](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L2254)  
> Since: 3.9.0

---

## setAllowGravity

### <instance> setAllowGravity([value])

**Description:**

Enables or disables gravity's effect on this Body.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| value | boolean | Yes | true | `true` to allow gravity on this body, or `false` to disable it. |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Arcade.Body](physics-arcade-body.md) - This Body object.

> Source: [src/physics/arcade/Body.js#L2274](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L2274)  
> Since: 3.9.0

---

## setAllowRotation

### <instance> setAllowRotation([value])

**Description:**

Enables or disables rotation.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| value | boolean | Yes | true | `true` to allow rotation on this body, or `false` to disable it. |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Arcade.Body](physics-arcade-body.md) - This Body object.

> Source: [src/physics/arcade/Body.js#L2294](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L2294)  
> Since: 3.9.0

---

## setAngularAcceleration

### <instance> setAngularAcceleration(value)

**Description:**

Sets the Body's angular acceleration.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The acceleration, in degrees per second squared. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Arcade.Body](physics-arcade-body.md) - This Body object.

> Source: [src/physics/arcade/Body.js#L2512](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L2512)  
> Since: 3.0.0

---

## setAngularDrag

### <instance> setAngularDrag(value)

**Description:**

Sets the Body's angular drag.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The drag, in degrees per second squared. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Arcade.Body](physics-arcade-body.md) - This Body object.

> Source: [src/physics/arcade/Body.js#L2529](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L2529)  
> Since: 3.0.0

---

## setAngularVelocity

### <instance> setAngularVelocity(value)

**Description:**

Sets the Body's angular velocity.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The velocity, in degrees per second. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Arcade.Body](physics-arcade-body.md) - This Body object.

> Source: [src/physics/arcade/Body.js#L2495](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L2495)  
> Since: 3.0.0

---

## setBounce

### <instance> setBounce(x, [y])

**Description:**

Sets the Body's bounce.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | No |  | The horizontal bounce, relative to 1. |
| --- | --- | --- | --- | --- |
| y | number | Yes | "x" | The vertical bounce, relative to 1. |

**Returns:** [Phaser.Physics.Arcade.Body](physics-arcade-body.md) - This Body object.

> Source: [src/physics/arcade/Body.js#L2150](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L2150)  
> Since: 3.0.0

---

## setBounceX

### <instance> setBounceX(value)

**Description:**

Sets the Body's horizontal bounce.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The bounce, relative to 1. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Arcade.Body](physics-arcade-body.md) - This Body object.

> Source: [src/physics/arcade/Body.js#L2168](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L2168)  
> Since: 3.0.0

---

## setBounceY

### <instance> setBounceY(value)

**Description:**

Sets the Body's vertical bounce.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The bounce, relative to 1. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Arcade.Body](physics-arcade-body.md) - This Body object.

> Source: [src/physics/arcade/Body.js#L2185](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L2185)  
> Since: 3.0.0

---

## setBoundsRectangle

### <instance> setBoundsRectangle([bounds])

**Description:**

Sets a custom collision boundary rectangle. Use if you want to have a custom

boundary instead of the world boundaries.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| bounds | [Phaser.Geom.Rectangle](geom-rectangle.md) | Yes | The new boundary rectangle. Pass `null` to use the World bounds. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Arcade.Body](physics-arcade-body.md) - This Body object.

> Source: [src/physics/arcade/Body.js#L1310](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L1310)  
> Since: 3.20

---

## setCircle

### <instance> setCircle(radius, [offsetX], [offsetY])

**Description:**

Sizes and positions this Body, as a circle.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| radius | number | No | The radius of the Body, in source pixels. |
| --- | --- | --- | --- |
| offsetX | number | Yes | The horizontal offset of the Body from its Game Object, in source pixels. |
| offsetY | number | Yes | The vertical offset of the Body from its Game Object, in source pixels. |

**Returns:** [Phaser.Physics.Arcade.Body](physics-arcade-body.md) - This Body object.

> Source: [src/physics/arcade/Body.js#L1514](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L1514)  
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

**Returns:** [Phaser.Physics.Arcade.Body](physics-arcade-body.md) - This Game Object.

**Inherits:** [Phaser.Physics.Arcade.Components.Collision#setCollidesWith](../namespace/physics-arcade-components-collision.md)

> Source: [src/physics/arcade/components/Collision.js#L100](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/components/Collision.js#L100)  
> Since: 3.70.0

---

## setCollideWorldBounds

### <instance> setCollideWorldBounds([value], [bounceX], [bounceY], [onWorldBounds])

**Description:**

Sets whether this Body collides with the world boundary.

Optionally also sets the World Bounce and `onWorldBounds` values.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| value | boolean | Yes | true | `true` if the Body should collide with the world bounds, otherwise `false`. |
| --- | --- | --- | --- | --- |
| bounceX | number | Yes |  | If given this replaces the Body's `worldBounce.x` value. |
| bounceY | number | Yes |  | If given this replaces the Body's `worldBounce.y` value. |
| onWorldBounds | boolean | Yes |  | If given this replaces the Body's `onWorldBounds` value. |

**Returns:** [Phaser.Physics.Arcade.Body](physics-arcade-body.md) - This Body object.

> Source: [src/physics/arcade/Body.js#L1945](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L1945)  
> Since: 3.0.0

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

**Returns:** [Phaser.Physics.Arcade.Body](physics-arcade-body.md) - This Game Object.

**Inherits:** [Phaser.Physics.Arcade.Components.Collision#setCollisionCategory](../namespace/physics-arcade-components-collision.md)

> Source: [src/physics/arcade/components/Collision.js#L17](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/components/Collision.js#L17)  
> Since: 3.70.0

---

## setDamping

### <instance> setDamping(value)

**Description:**

If this Body is using `drag` for deceleration this property controls how the drag is applied.

If set to `true` drag will use a damping effect rather than a linear approach. If you are

creating a game where the Body moves freely at any angle (i.e. like the way the ship moves in

the game Asteroids) then you will get a far smoother and more visually correct deceleration

by using damping, avoiding the axis-drift that is prone with linear deceleration.

If you enable this property then you should use far smaller `drag` values than with linear, as

they are used as a multiplier on the velocity. Values such as 0.95 will give a nice slow

deceleration, where-as smaller values, such as 0.5 will stop an object almost immediately.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | boolean | No | `true` to use damping, or `false` to use drag. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Arcade.Body](physics-arcade-body.md) - This Body object.

> Source: [src/physics/arcade/Body.js#L2332](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L2332)  
> Since: 3.50.0

---

## setDirectControl

### <instance> setDirectControl([value])

**Description:**

Sets whether this Body should calculate its velocity based on its change in

position every frame. The default, which is to not do this, means that you

make this Body move by setting the velocity directly. However, if you are

trying to move this Body via a Tween, or have it follow a Path, then you

should enable this instead. This will allow it to still collide with other

bodies, something that isn't possible if you're just changing its position directly.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| value | boolean | Yes | true | `true` if the Body calculate velocity based on changes in position, otherwise `false`. |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Arcade.Body](physics-arcade-body.md) - This Body object.

> Source: [src/physics/arcade/Body.js#L1921](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L1921)  
> Since: 3.70.0

---

## setDrag

### <instance> setDrag(x, [y])

**Description:**

Sets the Body's drag.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | No |  | The horizontal component, in pixels per second squared. |
| --- | --- | --- | --- | --- |
| y | number | Yes | "x" | The vertical component, in pixels per second squared. |

**Returns:** [Phaser.Physics.Arcade.Body](physics-arcade-body.md) - This Body object.

> Source: [src/physics/arcade/Body.js#L2314](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L2314)  
> Since: 3.0.0

---

## setDragX

### <instance> setDragX(value)

**Description:**

Sets the Body's horizontal drag.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The drag, in pixels per second squared. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Arcade.Body](physics-arcade-body.md) - This Body object.

> Source: [src/physics/arcade/Body.js#L2357](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L2357)  
> Since: 3.0.0

---

## setDragY

### <instance> setDragY(value)

**Description:**

Sets the Body's vertical drag.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The drag, in pixels per second squared. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Arcade.Body](physics-arcade-body.md) - This Body object.

> Source: [src/physics/arcade/Body.js#L2374](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L2374)  
> Since: 3.0.0

---

## setEnable

### <instance> setEnable([value])

**Description:**

Sets the Body's `enable` property.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| value | boolean | Yes | true | The value to assign to `enable`. |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Arcade.Body](physics-arcade-body.md) - This Body object.

> Source: [src/physics/arcade/Body.js#L2582](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L2582)  
> Since: 3.15.0

---

## setFriction

### <instance> setFriction(x, [y])

**Description:**

Sets the Body's friction.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | No |  | The horizontal component, relative to 1. |
| --- | --- | --- | --- | --- |
| y | number | Yes | "x" | The vertical component, relative to 1. |

**Returns:** [Phaser.Physics.Arcade.Body](physics-arcade-body.md) - This Body object.

> Source: [src/physics/arcade/Body.js#L2443](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L2443)  
> Since: 3.0.0

---

## setFrictionX

### <instance> setFrictionX(value)

**Description:**

Sets the Body's horizontal friction.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The friction value, relative to 1. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Arcade.Body](physics-arcade-body.md) - This Body object.

> Source: [src/physics/arcade/Body.js#L2461](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L2461)  
> Since: 3.0.0

---

## setFrictionY

### <instance> setFrictionY(value)

**Description:**

Sets the Body's vertical friction.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The friction value, relative to 1. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Arcade.Body](physics-arcade-body.md) - This Body object.

> Source: [src/physics/arcade/Body.js#L2478](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L2478)  
> Since: 3.0.0

---

## setGameObject

### <instance> setGameObject(gameObject, [enable])

**Description:**

Assign this Body to a new Game Object.

Removes this body from the Physics World, assigns to the new Game Object, calls `setSize` and then

adds this body back into the World again, setting it enabled, unless the `enable` argument is set to `false`.

If this body already has a Game Object, then it will remove itself from that Game Object first.

Only if the given `gameObject` has a `body` property will this Body be assigned to it.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No |  | The Game Object this Body belongs to. |
| --- | --- | --- | --- | --- |
| enable | boolean | Yes | true | Automatically enable this Body for physics. |

**Returns:** [Phaser.Physics.Arcade.Body](physics-arcade-body.md) - This Body object.

> Source: [src/physics/arcade/Body.js#L1409](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L1409)  
> Since: 3.60.0

---

## setGravity

### <instance> setGravity(x, [y])

**Description:**

Sets the Body's gravity.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | No |  | The horizontal component, in pixels per second squared. |
| --- | --- | --- | --- | --- |
| y | number | Yes | "x" | The vertical component, in pixels per second squared. |

**Returns:** [Phaser.Physics.Arcade.Body](physics-arcade-body.md) - This Body object.

> Source: [src/physics/arcade/Body.js#L2391](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L2391)  
> Since: 3.0.0

---

## setGravityX

### <instance> setGravityX(value)

**Description:**

Sets the Body's horizontal gravity.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The gravity, in pixels per second squared. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Arcade.Body](physics-arcade-body.md) - This Body object.

> Source: [src/physics/arcade/Body.js#L2409](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L2409)  
> Since: 3.0.0

---

## setGravityY

### <instance> setGravityY(value)

**Description:**

Sets the Body's vertical gravity.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The gravity, in pixels per second squared. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Arcade.Body](physics-arcade-body.md) - This Body object.

> Source: [src/physics/arcade/Body.js#L2426](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L2426)  
> Since: 3.0.0

---

## setImmovable

### <instance> setImmovable([value])

**Description:**

Sets the Body's `immovable` property.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| value | boolean | Yes | true | The value to assign to `immovable`. |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Arcade.Body](physics-arcade-body.md) - This Body object.

> Source: [src/physics/arcade/Body.js#L2563](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L2563)  
> Since: 3.0.0

---

## setMass

### <instance> setMass(value)

**Description:**

Sets the Body's mass.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The mass value, relative to 1. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Arcade.Body](physics-arcade-body.md) - This Body object.

> Source: [src/physics/arcade/Body.js#L2546](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L2546)  
> Since: 3.0.0

---

## setMaxSpeed

### <instance> setMaxSpeed(value)

**Description:**

Sets the maximum speed the Body can move.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The maximum speed value, in pixels per second. Set to a negative value to disable. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Arcade.Body](physics-arcade-body.md) - This Body object.

> Source: [src/physics/arcade/Body.js#L2100](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L2100)  
> Since: 3.16.0

---

## setMaxVelocity

### <instance> setMaxVelocity(x, [y])

**Description:**

Sets the Body's maximum velocity.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | No |  | The horizontal velocity, in pixels per second. |
| --- | --- | --- | --- | --- |
| y | number | Yes | "x" | The vertical velocity, in pixels per second. |

**Returns:** [Phaser.Physics.Arcade.Body](physics-arcade-body.md) - This Body object.

> Source: [src/physics/arcade/Body.js#L2048](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L2048)  
> Since: 3.10.0

---

## setMaxVelocityX

### <instance> setMaxVelocityX(value)

**Description:**

Sets the Body's maximum horizontal velocity.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The maximum horizontal velocity, in pixels per second. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Arcade.Body](physics-arcade-body.md) - This Body object.

> Source: [src/physics/arcade/Body.js#L2066](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L2066)  
> Since: 3.50.0

---

## setMaxVelocityY

### <instance> setMaxVelocityY(value)

**Description:**

Sets the Body's maximum vertical velocity.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The maximum vertical velocity, in pixels per second. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Arcade.Body](physics-arcade-body.md) - This Body object.

> Source: [src/physics/arcade/Body.js#L2083](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L2083)  
> Since: 3.50.0

---

## setOffset

### <instance> setOffset(x, [y])

**Description:**

Sets the offset of the Body's position from its Game Object's position.

The Body's `position` isn't changed until the next `preUpdate`.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | No |  | The horizontal offset, in source pixels. |
| --- | --- | --- | --- | --- |
| y | number | Yes | "x" | The vertical offset, in source pixels. |

**Returns:** [Phaser.Physics.Arcade.Body](physics-arcade-body.md) - This Body object.

> Source: [src/physics/arcade/Body.js#L1388](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L1388)  
> Since: 3.0.0

---

## setSize

### <instance> setSize([width], [height], [center])

**Description:**

Sizes and positions this Body, as a rectangle.

Modifies the Body `offset` if `center` is true (the default).

Resets the width and height to match current frame, if no width and height provided and a frame is found.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| width | number | Yes |  | The width of the Body in pixels. Cannot be zero. If not given, and the parent Game Object has a frame, it will use the frame width. |
| --- | --- | --- | --- | --- |
| height | number | Yes |  | The height of the Body in pixels. Cannot be zero. If not given, and the parent Game Object has a frame, it will use the frame height. |
| center | boolean | Yes | true | Modify the Body's `offset`, placing the Body's center on its Game Object's center. Only works if the Game Object has the `getCenter` method. |

**Returns:** [Phaser.Physics.Arcade.Body](physics-arcade-body.md) - This Body object.

> Source: [src/physics/arcade/Body.js#L1456](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L1456)  
> Since: 3.0.0

---

## setSlideFactor

### <instance> setSlideFactor(x, [y])

**Description:**

Sets the Slide Factor of this Body.

The Slide Factor controls how much velocity is preserved when

this Body is pushed by another Body.

The default value is 1, which means that it will take on all

velocity given in the push. You can adjust this value to control

how much velocity is retained by this Body when the push ends.

A value of 0, for example, will allow this Body to be pushed

but then remain completely still after the push ends, such as

you see in a game like Sokoban.

Or you can set a mid-point, such as 0.25 which will allow it

to keep 25% of the original velocity when the push ends. You

can combine this with the `setDrag()` method to create deceleration.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | No |  | The horizontal slide factor. A value between 0 and 1. |
| --- | --- | --- | --- | --- |
| y | number | Yes | "x" | The vertical slide factor. A value between 0 and 1. |

**Returns:** [Phaser.Physics.Arcade.Body](physics-arcade-body.md) - This Body object.

> Source: [src/physics/arcade/Body.js#L2117](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L2117)  
> Since: 3.70.0

---

## setVelocity

### <instance> setVelocity(x, [y])

**Description:**

Sets the Body's velocity.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | No |  | The horizontal velocity, in pixels per second. |
| --- | --- | --- | --- | --- |
| y | number | Yes | "x" | The vertical velocity, in pixels per second. |

**Returns:** [Phaser.Physics.Arcade.Body](physics-arcade-body.md) - This Body object.

> Source: [src/physics/arcade/Body.js#L1995](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L1995)  
> Since: 3.0.0

---

## setVelocityX

### <instance> setVelocityX(value)

**Description:**

Sets the Body's horizontal velocity.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The velocity, in pixels per second. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Arcade.Body](physics-arcade-body.md) - This Body object.

> Source: [src/physics/arcade/Body.js#L2018](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L2018)  
> Since: 3.0.0

---

## setVelocityY

### <instance> setVelocityY(value)

**Description:**

Sets the Body's vertical velocity.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The velocity, in pixels per second. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Arcade.Body](physics-arcade-body.md) - This Body object.

> Source: [src/physics/arcade/Body.js#L2033](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L2033)  
> Since: 3.0.0

---

## stop

### <instance> stop()

**Description:**

Sets acceleration, velocity, and speed to zero.

**Returns:** [Phaser.Physics.Arcade.Body](physics-arcade-body.md) - This Body object.

> Source: [src/physics/arcade/Body.js#L1611](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L1611)  
> Since: 3.0.0

---

## update

### <instance> update(delta)

**Description:**

Performs a single physics step and updates the body velocity, angle, speed and other properties.

This method can be called multiple times per game frame, depending on the physics step rate.

The results are synced back to the Game Object in `postUpdate`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| delta | number | No | The delta time, in seconds, elapsed since the last frame. |
| --- | --- | --- | --- |

**Fires:** [Phaser.Physics.Arcade.Events#event:WORLD\_BOUNDS](../event/physics-arcade-events.md)

> Source: [src/physics/arcade/Body.js#L1154](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L1154)  
> Since: 3.0.0

---

## updateBounds

### <instance> updateBounds()

**Description:**

Updates the Body's `transform`, `width`, `height`, and `center` from its Game Object.

The Body's `position` isn't changed.

> Source: [src/physics/arcade/Body.js#L960](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L960)  
> Since: 3.0.0

---

## updateCenter

### <instance> updateCenter()

**Description:**

Updates the Body's `center` from its `position`, `width`, and `height`.

> Source: [src/physics/arcade/Body.js#L1031](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L1031)  
> Since: 3.0.0

---

## updateFromGameObject

### <instance> updateFromGameObject()

**Description:**

Updates the Body's `position`, `width`, `height`, and `center` from its Game Object and `offset`.

You don't need to call this for Dynamic Bodies, as it happens automatically during the physics step.

But you could use it if you have modified the Body offset or Game Object transform and need to immediately

read the Body's new `position` or `center`.

To resynchronize the Body with its Game Object, use `reset()` instead.

> Source: [src/physics/arcade/Body.js#L1042](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L1042)  
> Since: 3.24.0

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

Whether this Body will be drawn to the debug display.

**Returns:** boolean - True if either `debugShowBody` or `debugShowVelocity` are enabled.

> Source: [src/physics/arcade/Body.js#L1908](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/Body.js#L1908)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [acceleration](#acceleration)

    - [acceleration: Phaser.Math.Vector2](#acceleration-phasermathvector2)
  + [allowDrag](#allowdrag)

    - [allowDrag: boolean](#allowdrag-boolean)
  + [allowGravity](#allowgravity)

    - [allowGravity: boolean](#allowgravity-boolean)
  + [allowRotation](#allowrotation)

    - [allowRotation: boolean](#allowrotation-boolean)
  + [angle](#angle)

    - [angle: number](#angle-number)
  + [angularAcceleration](#angularacceleration)

    - [angularAcceleration: number](#angularacceleration-number)
  + [angularDrag](#angulardrag)

    - [angularDrag: number](#angulardrag-number)
  + [angularVelocity](#angularvelocity)

    - [angularVelocity: number](#angularvelocity-number)
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
  + [customBoundsRectangle](#customboundsrectangle)

    - [customBoundsRectangle: Phaser.Geom.Rectangle](#customboundsrectangle-phasergeomrectangle)
  + [customSeparateX](#customseparatex)

    - [customSeparateX: boolean](#customseparatex-boolean)
  + [customSeparateY](#customseparatey)

    - [customSeparateY: boolean](#customseparatey-boolean)
  + [debugBodyColor](#debugbodycolor)

    - [debugBodyColor: number](#debugbodycolor-number)
  + [debugShowBody](#debugshowbody)

    - [debugShowBody: boolean](#debugshowbody-boolean)
  + [debugShowVelocity](#debugshowvelocity)

    - [debugShowVelocity: boolean](#debugshowvelocity-boolean)
  + [deltaMax](#deltamax)

    - [deltaMax: Phaser.Math.Vector2](#deltamax-phasermathvector2)
  + [directControl](#directcontrol)

    - [directControl: boolean](#directcontrol-boolean)
  + [drag](#drag)

    - [drag: Phaser.Math.Vector2](#drag-phasermathvector2)
  + [embedded](#embedded)

    - [embedded: boolean](#embedded-boolean)
  + [enable](#enable)

    - [enable: boolean](#enable-boolean)
  + [facing](#facing)

    - [facing: number](#facing-number)
  + [friction](#friction)

    - [friction: Phaser.Math.Vector2](#friction-phasermathvector2)
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
  + [maxAngular](#maxangular)

    - [maxAngular: number](#maxangular-number)
  + [maxSpeed](#maxspeed)

    - [maxSpeed: number](#maxspeed-number)
  + [maxVelocity](#maxvelocity)

    - [maxVelocity: Phaser.Math.Vector2](#maxvelocity-phasermathvector2)
  + [moves](#moves)

    - [moves: boolean](#moves-boolean)
  + [newVelocity](#newvelocity)

    - [newVelocity: Phaser.Math.Vector2](#newvelocity-phasermathvector2)
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
  + [preRotation](#prerotation)

    - [preRotation: number](#prerotation-number)
  + [prev](#prev)

    - [prev: Phaser.Math.Vector2](#prev-phasermathvector2)
  + [prevFrame](#prevframe)

    - [prevFrame: Phaser.Math.Vector2](#prevframe-phasermathvector2)
  + [pushable](#pushable)

    - [pushable: boolean](#pushable-boolean)
  + [radius](#radius)

    - [radius: number](#radius-number)
  + [right](#right)

    - [right: number](#right-number)
  + [rotation](#rotation)

    - [rotation: number](#rotation-number)
  + [slideFactor](#slidefactor)

    - [slideFactor: Phaser.Math.Vector2](#slidefactor-phasermathvector2)
  + [sourceHeight](#sourceheight)

    - [sourceHeight: number](#sourceheight-number)
  + [sourceWidth](#sourcewidth)

    - [sourceWidth: number](#sourcewidth-number)
  + [speed](#speed)

    - [speed: number](#speed-number)
  + [syncBounds](#syncbounds)

    - [syncBounds: boolean](#syncbounds-boolean)
  + [top](#top)

    - [top: number](#top-number)
  + [touching](#touching)

    - [touching: Phaser.Types.Physics.Arcade.ArcadeBodyCollision](#touching-phasertypesphysicsarcadearcadebodycollision)
  + [transform](#transform)

    - [transform: object](#transform-object)
  + [useDamping](#usedamping)

    - [useDamping: boolean](#usedamping-boolean)
  + [velocity](#velocity)

    - [velocity: Phaser.Math.Vector2](#velocity-phasermathvector2)
  + [wasTouching](#wastouching)

    - [wasTouching: Phaser.Types.Physics.Arcade.ArcadeBodyCollision](#wastouching-phasertypesphysicsarcadearcadebodycollision)
  + [width](#width)

    - [width: number](#width-number)
  + [world](#world)

    - [world: Phaser.Physics.Arcade.World](#world-phaserphysicsarcadeworld)
  + [worldBounce](#worldbounce)

    - [worldBounce: Phaser.Math.Vector2](#worldbounce-phasermathvector2)
  + [x](#x)

    - [x: number](#x-number)
  + [y](#y)

    - [y: number](#y-number)
* [Private Members](#private-members)

  + [\_bounds](#_bounds)

    - [\_bounds: Phaser.Geom.Rectangle](#_bounds-phasergeomrectangle)
  + [\_dx](#_dx)

    - [\_dx: number](#_dx-number)
  + [\_dy](#_dy)

    - [\_dy: number](#_dy-number)
  + [\_sx](#_sx)

    - [\_sx: number](#_sx-number)
  + [\_sy](#_sy)

    - [\_sy: number](#_sy-number)
  + [\_tx](#_tx)

    - [\_tx: number](#_tx-number)
  + [\_ty](#_ty)

    - [\_ty: number](#_ty-number)
  + [autoFrame](#autoframe)

    - [autoFrame: Phaser.Math.Vector2](#autoframe-phasermathvector2)
* [Public Methods](#public-methods)

  + [addCollidesWith](#addcollideswith)

    - [<instance> addCollidesWith(category)](#instance-addcollideswithcategory)
  + [checkWorldBounds](#checkworldbounds)

    - [<instance> checkWorldBounds()](#instance-checkworldbounds)
  + [deltaAbsX](#deltaabsx)

    - [<instance> deltaAbsX()](#instance-deltaabsx)
  + [deltaAbsY](#deltaabsy)

    - [<instance> deltaAbsY()](#instance-deltaabsy)
  + [deltaX](#deltax)

    - [<instance> deltaX()](#instance-deltax)
  + [deltaXFinal](#deltaxfinal)

    - [<instance> deltaXFinal()](#instance-deltaxfinal)
  + [deltaY](#deltay)

    - [<instance> deltaY()](#instance-deltay)
  + [deltaYFinal](#deltayfinal)

    - [<instance> deltaYFinal()](#instance-deltayfinal)
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
  + [onCeiling](#onceiling)

    - [<instance> onCeiling()](#instance-onceiling)
  + [onFloor](#onfloor)

    - [<instance> onFloor()](#instance-onfloor)
  + [onWall](#onwall)

    - [<instance> onWall()](#instance-onwall)
  + [postUpdate](#postupdate)

    - [<instance> postUpdate()](#instance-postupdate)
  + [preUpdate](#preupdate)

    - [<instance> preUpdate(willStep, delta)](#instance-preupdatewillstep-delta)
  + [processX](#processx)

    - [<instance> processX(x, [vx], [left], [right])](#instance-processxx-vx-left-right)
  + [processY](#processy)

    - [<instance> processY(y, [vy], [up], [down])](#instance-processyy-vy-up-down)
  + [removeCollidesWith](#removecollideswith)

    - [<instance> removeCollidesWith(category)](#instance-removecollideswithcategory)
  + [reset](#reset)

    - [<instance> reset(x, y)](#instance-resetx-y)
  + [resetCollisionCategory](#resetcollisioncategory)

    - [<instance> resetCollisionCategory()](#instance-resetcollisioncategory)
  + [resetFlags](#resetflags)

    - [<instance> resetFlags([clear])](#instance-resetflagsclear)
  + [setAcceleration](#setacceleration)

    - [<instance> setAcceleration(x, [y])](#instance-setaccelerationx-y)
  + [setAccelerationX](#setaccelerationx)

    - [<instance> setAccelerationX(value)](#instance-setaccelerationxvalue)
  + [setAccelerationY](#setaccelerationy)

    - [<instance> setAccelerationY(value)](#instance-setaccelerationyvalue)
  + [setAllowDrag](#setallowdrag)

    - [<instance> setAllowDrag([value])](#instance-setallowdragvalue)
  + [setAllowGravity](#setallowgravity)

    - [<instance> setAllowGravity([value])](#instance-setallowgravityvalue)
  + [setAllowRotation](#setallowrotation)

    - [<instance> setAllowRotation([value])](#instance-setallowrotationvalue)
  + [setAngularAcceleration](#setangularacceleration)

    - [<instance> setAngularAcceleration(value)](#instance-setangularaccelerationvalue)
  + [setAngularDrag](#setangulardrag)

    - [<instance> setAngularDrag(value)](#instance-setangulardragvalue)
  + [setAngularVelocity](#setangularvelocity)

    - [<instance> setAngularVelocity(value)](#instance-setangularvelocityvalue)
  + [setBounce](#setbounce)

    - [<instance> setBounce(x, [y])](#instance-setbouncex-y)
  + [setBounceX](#setbouncex)

    - [<instance> setBounceX(value)](#instance-setbouncexvalue)
  + [setBounceY](#setbouncey)

    - [<instance> setBounceY(value)](#instance-setbounceyvalue)
  + [setBoundsRectangle](#setboundsrectangle)

    - [<instance> setBoundsRectangle([bounds])](#instance-setboundsrectanglebounds)
  + [setCircle](#setcircle)

    - [<instance> setCircle(radius, [offsetX], [offsetY])](#instance-setcircleradius-offsetx-offsety)
  + [setCollidesWith](#setcollideswith)

    - [<instance> setCollidesWith(categories)](#instance-setcollideswithcategories)
  + [setCollideWorldBounds](#setcollideworldbounds)

    - [<instance> setCollideWorldBounds([value], [bounceX], [bounceY], [onWorldBounds])](#instance-setcollideworldboundsvalue-bouncex-bouncey-onworldbounds)
  + [setCollisionCategory](#setcollisioncategory)

    - [<instance> setCollisionCategory(category)](#instance-setcollisioncategorycategory)
  + [setDamping](#setdamping)

    - [<instance> setDamping(value)](#instance-setdampingvalue)
  + [setDirectControl](#setdirectcontrol)

    - [<instance> setDirectControl([value])](#instance-setdirectcontrolvalue)
  + [setDrag](#setdrag)

    - [<instance> setDrag(x, [y])](#instance-setdragx-y)
  + [setDragX](#setdragx)

    - [<instance> setDragX(value)](#instance-setdragxvalue)
  + [setDragY](#setdragy)

    - [<instance> setDragY(value)](#instance-setdragyvalue)
  + [setEnable](#setenable)

    - [<instance> setEnable([value])](#instance-setenablevalue)
  + [setFriction](#setfriction)

    - [<instance> setFriction(x, [y])](#instance-setfrictionx-y)
  + [setFrictionX](#setfrictionx)

    - [<instance> setFrictionX(value)](#instance-setfrictionxvalue)
  + [setFrictionY](#setfrictiony)

    - [<instance> setFrictionY(value)](#instance-setfrictionyvalue)
  + [setGameObject](#setgameobject)

    - [<instance> setGameObject(gameObject, [enable])](#instance-setgameobjectgameobject-enable)
  + [setGravity](#setgravity)

    - [<instance> setGravity(x, [y])](#instance-setgravityx-y)
  + [setGravityX](#setgravityx)

    - [<instance> setGravityX(value)](#instance-setgravityxvalue)
  + [setGravityY](#setgravityy)

    - [<instance> setGravityY(value)](#instance-setgravityyvalue)
  + [setImmovable](#setimmovable)

    - [<instance> setImmovable([value])](#instance-setimmovablevalue)
  + [setMass](#setmass)

    - [<instance> setMass(value)](#instance-setmassvalue)
  + [setMaxSpeed](#setmaxspeed)

    - [<instance> setMaxSpeed(value)](#instance-setmaxspeedvalue)
  + [setMaxVelocity](#setmaxvelocity)

    - [<instance> setMaxVelocity(x, [y])](#instance-setmaxvelocityx-y)
  + [setMaxVelocityX](#setmaxvelocityx)

    - [<instance> setMaxVelocityX(value)](#instance-setmaxvelocityxvalue)
  + [setMaxVelocityY](#setmaxvelocityy)

    - [<instance> setMaxVelocityY(value)](#instance-setmaxvelocityyvalue)
  + [setOffset](#setoffset)

    - [<instance> setOffset(x, [y])](#instance-setoffsetx-y)
  + [setSize](#setsize)

    - [<instance> setSize([width], [height], [center])](#instance-setsizewidth-height-center)
  + [setSlideFactor](#setslidefactor)

    - [<instance> setSlideFactor(x, [y])](#instance-setslidefactorx-y)
  + [setVelocity](#setvelocity)

    - [<instance> setVelocity(x, [y])](#instance-setvelocityx-y)
  + [setVelocityX](#setvelocityx)

    - [<instance> setVelocityX(value)](#instance-setvelocityxvalue)
  + [setVelocityY](#setvelocityy)

    - [<instance> setVelocityY(value)](#instance-setvelocityyvalue)
  + [stop](#stop)

    - [<instance> stop()](#instance-stop)
  + [update](#update)

    - [<instance> update(delta)](#instance-updatedelta)
  + [updateBounds](#updatebounds)

    - [<instance> updateBounds()](#instance-updatebounds)
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