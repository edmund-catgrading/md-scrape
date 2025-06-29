# World

Phaser.Physics.Arcade.World

The Arcade Physics World.

The World is responsible for creating, managing, colliding and updating all of the bodies within it.

An instance of the World belongs to a Phaser.Scene and is accessed via the property `physics.world`.

**Constructor**

`new World(scene, config)`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| scene | [Phaser.Scene](scene.md) | No | The Scene to which this World instance belongs. |
| --- | --- | --- | --- |
| config | [Phaser.Types.Physics.Arcade.ArcadeWorldConfig](../typedef/types-physics-arcade.md) | No | An Arcade Physics Configuration object. |

---

**Scope**: static

**Extends**

> [Phaser.Events.EventEmitter](events-eventemitter.md)

> Source: [src/physics/arcade/World.js#L39](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/World.js#L39)  
> Since: 3.0.0

# Public Members

## bodies

### bodies: Phaser.Structs.Set.<Phaser.Physics.Arcade.Body>

**Description:**

Dynamic Bodies in this simulation.

> Source: [src/physics/arcade/World.js#L75](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/World.js#L75)  
> Since: 3.0.0

---

## bounds

### bounds: [Phaser.Geom.Rectangle](geom-rectangle.md)

**Description:**

A boundary constraining Bodies.

> Source: [src/physics/arcade/World.js#L120](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/World.js#L120)  
> Since: 3.0.0

---

## checkCollision

### checkCollision: [Phaser.Types.Physics.Arcade.CheckCollisionObject](../typedef/types-physics-arcade.md)

**Description:**

The boundary edges that Bodies can collide with.

> Source: [src/physics/arcade/World.js#L134](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/World.js#L134)  
> Since: 3.0.0

---

## colliders

### colliders: Phaser.Structs.ProcessQueue.<Phaser.Physics.Arcade.Collider>

**Description:**

This simulation's collision processors.

> Source: [src/physics/arcade/World.js#L102](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/World.js#L102)  
> Since: 3.0.0

---

## debugGraphic

### debugGraphic: [Phaser.GameObjects.Graphics](gameobjects-graphics.md)

**Description:**

The graphics object drawing the debug display.

> Source: [src/physics/arcade/World.js#L293](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/World.js#L293)  
> Since: 3.0.0

---

## defaults

### defaults: [Phaser.Types.Physics.Arcade.ArcadeWorldDefaults](../typedef/types-physics-arcade.md)

**Description:**

Default debug display settings for new Bodies.

> Source: [src/physics/arcade/World.js#L302](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/World.js#L302)  
> Since: 3.0.0

---

## drawDebug

### drawDebug: boolean

**Description:**

Enables the debug display.

> Source: [src/physics/arcade/World.js#L283](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/World.js#L283)  
> Since: 3.0.0

---

## fixedStep

### fixedStep: boolean

**Description:**

Should Physics use a fixed update time-step (true) or sync to the render fps (false)?.

False value of this property disables fps and timeScale properties.

> Source: [src/physics/arcade/World.js#L161](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/World.js#L161)  
> Since: 3.23.0

---

## forceX

### forceX: boolean

**Description:**

Always separate overlapping Bodies horizontally before vertically.

False (the default) means Bodies are first separated on the axis of greater gravity, or the vertical axis if neither is greater.

> Source: [src/physics/arcade/World.js#L251](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/World.js#L251)  
> Since: 3.0.0

---

## fps

### fps: number

**Description:**

The number of physics steps to be taken per second.

This property is read-only. Use the `setFPS` method to modify it at run-time.

> Source: [src/physics/arcade/World.js#L148](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/World.js#L148)  
> Since: 3.10.0

---

## gravity

### gravity: [Phaser.Math.Vector2](math-vector2.md)

**Description:**

Acceleration of Bodies due to gravity, in pixels per second.

> Source: [src/physics/arcade/World.js#L111](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/World.js#L111)  
> Since: 3.0.0

---

## isPaused

### isPaused: boolean

**Description:**

Whether the simulation advances with the game loop.

> Source: [src/physics/arcade/World.js#L262](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/World.js#L262)  
> Since: 3.0.0

---

## maxEntries

### maxEntries: number

**Description:**

The maximum number of items per node on the RTree.

This is ignored if `useTree` is `false`. If you have a large number of bodies in

your world then you may find search performance improves by increasing this value,

to allow more items per node and less node division.

> Source: [src/physics/arcade/World.js#L318](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/World.js#L318)  
> Since: 3.0.0

---

## OVERLAP\_BIAS

### OVERLAP\_BIAS: number

**Description:**

The maximum absolute difference of a Body's per-step velocity and its overlap with another Body that will result in separation on *each axis*.

Larger values favor separation.

Smaller values favor no separation.

> Source: [src/physics/arcade/World.js#L226](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/World.js#L226)  
> Since: 3.0.0

---

## pendingDestroy

### pendingDestroy: Phaser.Structs.Set.<(Phaser.Physics.Arcade.Body | [Phaser.Physics.Arcade.StaticBody](physics-arcade-staticbody.md))>

**Description:**

Static Bodies marked for deletion.

> Source: [src/physics/arcade/World.js#L93](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/World.js#L93)  
> Since: 3.1.0

---

## scene

### scene: [Phaser.Scene](scene.md)

**Description:**

The Scene this simulation belongs to.

> Source: [src/physics/arcade/World.js#L66](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/World.js#L66)  
> Since: 3.0.0

---

## staticBodies

### staticBodies: Phaser.Structs.Set.<Phaser.Physics.Arcade.StaticBody>

**Description:**

Static Bodies in this simulation.

> Source: [src/physics/arcade/World.js#L84](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/World.js#L84)  
> Since: 3.0.0

---

## staticTree

### staticTree: [Phaser.Structs.RTree](structs-rtree.md)

**Description:**

The spatial index of Static Bodies.

> Source: [src/physics/arcade/World.js#L365](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/World.js#L365)  
> Since: 3.0.0

---

## stepsLastFrame

### stepsLastFrame: number

**Description:**

The number of steps that took place in the last frame.

> Source: [src/physics/arcade/World.js#L202](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/World.js#L202)  
> Since: 3.10.0

---

## TILE\_BIAS

### TILE\_BIAS: number

**Description:**

The maximum absolute value of a Body's overlap with a tile that will result in separation on *each axis*.

Larger values favor separation.

Smaller values favor no separation.

The optimum value may be similar to the tile size.

> Source: [src/physics/arcade/World.js#L238](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/World.js#L238)  
> Since: 3.0.0

---

## tileFilterOptions

### tileFilterOptions: [Phaser.Types.Tilemaps.FilteringOptions](../typedef/types-tilemaps.md)

**Description:**

The Filtering Options passed to `GetTilesWithinWorldXY` as part of the `collideSpriteVsTilemapLayer` check.

> Source: [src/physics/arcade/World.js#L403](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/World.js#L403)  
> Since: 3.60.0

---

## timeScale

### timeScale: number

**Description:**

Scaling factor applied to the frame rate.

* 1.0 = normal speed
* 2.0 = half speed
* 0.5 = double speed

> Source: [src/physics/arcade/World.js#L212](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/World.js#L212)  
> Since: 3.10.0

---

## tree

### tree: [Phaser.Structs.RTree](structs-rtree.md)

**Description:**

The spatial index of Dynamic Bodies.

> Source: [src/physics/arcade/World.js#L356](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/World.js#L356)  
> Since: 3.0.0

---

## treeMinMax

### treeMinMax: [Phaser.Types.Physics.Arcade.ArcadeWorldTreeMinMax](../typedef/types-physics-arcade.md)

**Description:**

Recycled input for tree searches.

> Source: [src/physics/arcade/World.js#L374](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/World.js#L374)  
> Since: 3.0.0

---

## useTree

### useTree: boolean

**Description:**

Should this Arcade Physics World use an RTree for Dynamic bodies?

An RTree is a fast way of spatially sorting of all the bodies in the world.

However, at certain limits, the cost of clearing and inserting the bodies into the

tree every frame becomes more expensive than the search speed gains it provides.

If you have a large number of dynamic bodies in your world then it may be best to

disable the use of the RTree by setting this property to `false` in the physics config.

The number it can cope with depends on browser and device, but a conservative estimate

of around 5,000 bodies should be considered the max before disabling it.

This only applies to dynamic bodies. Static bodies are always kept in an RTree,

because they don't have to be cleared every frame, so you benefit from the

massive search speeds all the time.

> Source: [src/physics/arcade/World.js#L332](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/World.js#L332)  
> Since: 3.10.0

---

# Private Members

## \_category

### \_category: number

**Description:**

Holds the internal collision filter category.

**Access:** private

> Source: [src/physics/arcade/ArcadePhysics.js#L91](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/ArcadePhysics.js#L91)  
> Since: 3.70.0

---

## \_elapsed

### \_elapsed: number

**Description:**

The amount of elapsed ms since the last frame.

**Access:** private

> Source: [src/physics/arcade/World.js#L172](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/World.js#L172)  
> Since: 3.10.0

---

## \_frameTime

### \_frameTime: number

**Description:**

Internal frame time value.

**Access:** private

> Source: [src/physics/arcade/World.js#L182](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/World.js#L182)  
> Since: 3.10.0

---

## \_frameTimeMS

### \_frameTimeMS: number

**Description:**

Internal frame time ms value.

**Access:** private

> Source: [src/physics/arcade/World.js#L192](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/World.js#L192)  
> Since: 3.10.0

---

## \_tempMatrix

### \_tempMatrix: [Phaser.GameObjects.Components.TransformMatrix](gameobjects-components-transformmatrix.md)

**Description:**

A temporary Transform Matrix used by bodies for calculations without them needing their own local copy.

**Access:** private

> Source: [src/physics/arcade/World.js#L383](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/World.js#L383)  
> Since: 3.12.0

---

## \_tempMatrix2

### \_tempMatrix2: [Phaser.GameObjects.Components.TransformMatrix](gameobjects-components-transformmatrix.md)

**Description:**

A temporary Transform Matrix used by bodies for calculations without them needing their own local copy.

**Access:** private

> Source: [src/physics/arcade/World.js#L393](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/World.js#L393)  
> Since: 3.12.0

---

## \_total

### \_total: number

**Description:**

Temporary total of colliding Bodies.

**Access:** private

> Source: [src/physics/arcade/World.js#L272](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/World.js#L272)  
> Since: 3.0.0

---

# Public Methods

## add

### <instance> add(body)

**Description:**

Adds an existing Arcade Physics Body or StaticBody to the simulation.

The body is enabled and added to the local search trees.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| body | [Phaser.Physics.Arcade.Body](physics-arcade-body.md) | [Phaser.Physics.Arcade.StaticBody](physics-arcade-staticbody.md) | No | The Body to be added to the simulation. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Arcade.Body](physics-arcade-body.md), [Phaser.Physics.Arcade.StaticBody](physics-arcade-staticbody.md) - The Body that was added to the simulation.

> Source: [src/physics/arcade/World.js#L540](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/World.js#L540)  
> Since: 3.10.0

---

## addCollider

### <instance> addCollider(object1, object2, [collideCallback], [processCallback], [callbackContext])

**Description:**

Creates a new Collider object and adds it to the simulation.

A Collider is a way to automatically perform collision checks between two objects,

calling the collide and process callbacks if they occur.

Colliders are run as part of the World update, after all of the Bodies have updated.

By creating a Collider you don't need then call `World.collide` in your `update` loop,

as it will be handled for you automatically.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| object1 | [Phaser.Types.Physics.Arcade.ArcadeColliderType](../typedef/types-physics-arcade.md) | No | The first object to check for collision. |
| --- | --- | --- | --- |
| object2 | [Phaser.Types.Physics.Arcade.ArcadeColliderType](../typedef/types-physics-arcade.md) | No | The second object to check for collision. |
| collideCallback | [Phaser.Types.Physics.Arcade.ArcadePhysicsCallback](../typedef/types-physics-arcade.md) | Yes | The callback to invoke when the two objects collide. |
| processCallback | [Phaser.Types.Physics.Arcade.ArcadePhysicsCallback](../typedef/types-physics-arcade.md) | Yes | The callback to invoke when the two objects collide. Must return a boolean. |
| callbackContext | \* | Yes | The scope in which to call the callbacks. |

**Returns:** [Phaser.Physics.Arcade.Collider](physics-arcade-collider.md) - The Collider that was created.

> Source: [src/physics/arcade/World.js#L801](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/World.js#L801)  
> Since: 3.0.0

---

## addListener

### <instance> addListener(event, fn, [context])

**Description:**

Add a listener for a given event.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| event | string | symbol | No |  | The event name. |
| --- | --- | --- | --- | --- |
| fn | function | No |  | The listener function. |
| context | \* | Yes | "this" | The context to invoke the listener with. |

**Returns:** [Phaser.Physics.Arcade.World](physics-arcade-world.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#addListener](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L111](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L111)  
> Since: 3.0.0

---

## addOverlap

### <instance> addOverlap(object1, object2, [collideCallback], [processCallback], [callbackContext])

**Description:**

Creates a new Overlap Collider object and adds it to the simulation.

A Collider is a way to automatically perform overlap checks between two objects,

calling the collide and process callbacks if they occur.

Colliders are run as part of the World update, after all of the Bodies have updated.

By creating a Collider you don't need then call `World.overlap` in your `update` loop,

as it will be handled for you automatically.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| object1 | [Phaser.Types.Physics.Arcade.ArcadeColliderType](../typedef/types-physics-arcade.md) | No | The first object to check for overlap. |
| --- | --- | --- | --- |
| object2 | [Phaser.Types.Physics.Arcade.ArcadeColliderType](../typedef/types-physics-arcade.md) | No | The second object to check for overlap. |
| collideCallback | [Phaser.Types.Physics.Arcade.ArcadePhysicsCallback](../typedef/types-physics-arcade.md) | Yes | The callback to invoke when the two objects overlap. |
| processCallback | [Phaser.Types.Physics.Arcade.ArcadePhysicsCallback](../typedef/types-physics-arcade.md) | Yes | The callback to invoke when the two objects overlap. Must return a boolean. |
| callbackContext | \* | Yes | The scope in which to call the callbacks. |

**Returns:** [Phaser.Physics.Arcade.Collider](physics-arcade-collider.md) - The Collider that was created.

> Source: [src/physics/arcade/World.js#L837](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/World.js#L837)  
> Since: 3.0.0

---

## canCollide

### <instance> canCollide(body1, body2)

**Description:**

Checks if the two given Arcade Physics bodies will collide, or not,

based on their collision mask and collision categories.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| body1 | [Phaser.Types.Physics.Arcade.ArcadeCollider](../typedef/types-physics-arcade.md) | No | The first body to check. |
| --- | --- | --- | --- |
| body2 | [Phaser.Types.Physics.Arcade.ArcadeCollider](../typedef/types-physics-arcade.md) | No | The second body to check. |

**Returns:** boolean - True if the two bodies will collide, otherwise false.

> Source: [src/physics/arcade/World.js#L1993](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/World.js#L1993)  
> Since: 3.70.0

---

## circleBodyIntersects

### <instance> circleBodyIntersects(circle, body)

**Description:**

Tests if a circular Body intersects with another Body.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| circle | [Phaser.Physics.Arcade.Body](physics-arcade-body.md) | No | The circular body to test. |
| --- | --- | --- | --- |
| body | [Phaser.Physics.Arcade.Body](physics-arcade-body.md) | No | The rectangular body to test. |

**Returns:** boolean - True if the two bodies intersect, otherwise false.

> Source: [src/physics/arcade/World.js#L1731](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/World.js#L1731)  
> Since: 3.0.0

---

## collide

### <instance> collide(object1, [object2], [collideCallback], [processCallback], [callbackContext])

**Description:**

Performs a collision check and separation between the two physics enabled objects given, which can be single

Game Objects, arrays of Game Objects, Physics Groups, arrays of Physics Groups or normal Groups.

If you don't require separation then use [Phaser.Physics.Arcade.World#overlap](physics-arcade-world.md) instead.

If two Groups or arrays are passed, each member of one will be tested against each member of the other.

If **only** one Group is passed (as `object1`), each member of the Group will be collided against the other members.

If **only** one Array is passed, the array is iterated and every element in it is tested against the others.

Two callbacks can be provided; they receive the colliding game objects as arguments.

If an overlap is detected, the `processCallback` is called first. It can cancel the collision by returning false.

Next the objects are separated and `collideCallback` is invoked.

Arcade Physics uses the Projection Method of collision resolution and separation. While it's fast and suitable

for 'arcade' style games it lacks stability when multiple objects are in close proximity or resting upon each other.

The separation that stops two objects penetrating may create a new penetration against a different object. If you

require a high level of stability please consider using an alternative physics system, such as Matter.js.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| object1 | [Phaser.Types.Physics.Arcade.ArcadeColliderType](../typedef/types-physics-arcade.md) | No | The first object or array of objects to check. |
| --- | --- | --- | --- |
| object2 | [Phaser.Types.Physics.Arcade.ArcadeColliderType](../typedef/types-physics-arcade.md) | Yes | The second object or array of objects to check, or `undefined`. |
| collideCallback | [Phaser.Types.Physics.Arcade.ArcadePhysicsCallback](../typedef/types-physics-arcade.md) | Yes | An optional callback function that is called if the objects collide. |
| processCallback | [Phaser.Types.Physics.Arcade.ArcadePhysicsCallback](../typedef/types-physics-arcade.md) | Yes | An optional callback function that lets you perform additional checks against the two objects if they collide. If this is set then `collideCallback` will only be called if this callback returns `true`. |
| callbackContext | any | Yes | The context in which to run the callbacks. |

**Returns:** boolean - `true` if any overlapping Game Objects were separated, otherwise `false`.

> Source: [src/physics/arcade/World.js#L1780](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/World.js#L1780)  
> Since: 3.0.0

---

## collideSpriteVsTilemapLayer

### <instance> collideSpriteVsTilemapLayer(sprite, tilemapLayer, [collideCallback], [processCallback], [callbackContext], [overlapOnly])

**Description:**

Internal handler for Sprite vs. Tilemap collisions.

Please use Phaser.Physics.Arcade.World#collide instead.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| sprite | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No | The first object to check for collision. |
| --- | --- | --- | --- |
| tilemapLayer | [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) | No | The second object to check for collision. |
| collideCallback | [Phaser.Types.Physics.Arcade.ArcadePhysicsCallback](../typedef/types-physics-arcade.md) | Yes | An optional callback function that is called if the objects collide. |
| processCallback | [Phaser.Types.Physics.Arcade.ArcadePhysicsCallback](../typedef/types-physics-arcade.md) | Yes | An optional callback function that lets you perform additional checks against the two objects if they collide. If this is set then `collideCallback` will only be called if this callback returns `true`. |
| callbackContext | any | Yes | The context in which to run the callbacks. |
| overlapOnly | boolean | Yes | Whether this is a collision or overlap check. |

**Returns:** boolean - True if any objects overlap (with `overlapOnly`); or true if any overlapping objects were separated.

**Fires:** [Phaser.Physics.Arcade.Events#event:TILE\_COLLIDE](../event/physics-arcade-events.md), [Phaser.Physics.Arcade.Events#event:TILE\_OVERLAP](../event/physics-arcade-events.md)

> Source: [src/physics/arcade/World.js#L2273](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/World.js#L2273)  
> Since: 3.0.0

---

## collideTiles

### <instance> collideTiles(sprite, tiles, [collideCallback], [processCallback], [callbackContext])

**Description:**

This advanced method is specifically for testing for collision between a single Sprite and an array of Tile objects.

You should generally use the `collide` method instead, with a Sprite vs. a Tilemap Layer, as that will perform

tile filtering and culling for you, as well as handle the interesting face collision automatically.

This method is offered for those who would like to check for collision with specific Tiles in a layer, without

having to set any collision attributes on the tiles in question. This allows you to perform quick dynamic collisions

on small sets of Tiles. As such, no culling or checks are made to the array of Tiles given to this method,

you should filter them before passing them to this method.

Important: Use of this method skips the `interesting faces` system that Tilemap Layers use. This means if you have

say a row or column of tiles, and you jump into, or walk over them, it's possible to get stuck on the edges of the

tiles as the interesting face calculations are skipped. However, for quick-fire small collision set tests on

dynamic maps, this method can prove very useful.

This method does not factor in the Collision Mask or Category.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| sprite | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No | The first object to check for collision. |
| --- | --- | --- | --- |
| tiles | Array.<[Phaser.Tilemaps.Tile](tilemaps-tile.md)> | No | An array of Tiles to check for collision against. |
| collideCallback | [Phaser.Types.Physics.Arcade.ArcadePhysicsCallback](../typedef/types-physics-arcade.md) | Yes | An optional callback function that is called if the objects collide. |
| processCallback | [Phaser.Types.Physics.Arcade.ArcadePhysicsCallback](../typedef/types-physics-arcade.md) | Yes | An optional callback function that lets you perform additional checks against the two objects if they collide. If this is set then `collideCallback` will only be called if this callback returns `true`. |
| callbackContext | any | Yes | The context in which to run the callbacks. |

**Returns:** boolean - True if any objects overlap (with `overlapOnly`); or true if any overlapping objects were separated.

**Fires:** [Phaser.Physics.Arcade.Events#event:TILE\_COLLIDE](../event/physics-arcade-events.md)

> Source: [src/physics/arcade/World.js#L2194](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/World.js#L2194)  
> Since: 3.17.0

---

## computeAngularVelocity

### <instance> computeAngularVelocity(body, delta)

**Description:**

Calculates a Body's angular velocity.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| body | [Phaser.Physics.Arcade.Body](physics-arcade-body.md) | No | The Body to compute the velocity for. |
| --- | --- | --- | --- |
| delta | number | No | The delta value to be used in the calculation, in seconds. |

> Source: [src/physics/arcade/World.js#L1191](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/World.js#L1191)  
> Since: 3.10.0

---

## computeVelocity

### <instance> computeVelocity(body, delta)

**Description:**

Calculates a Body's per-axis velocity.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| body | [Phaser.Physics.Arcade.Body](physics-arcade-body.md) | No | The Body to compute the velocity for. |
| --- | --- | --- | --- |
| delta | number | No | The delta value to be used in the calculation, in seconds. |

> Source: [src/physics/arcade/World.js#L1237](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/World.js#L1237)  
> Since: 3.0.0

---

## createDebugGraphic

### <instance> createDebugGraphic()

**Description:**

Creates a Graphics Game Object that the world will use to render the debug display to.

This is called automatically when the World is instantiated if the `debug` config property

was set to `true`. However, you can call it at any point should you need to display the

debug Graphic from a fixed point.

You can control which objects are drawn to the Graphics object, and the colors they use,

by setting the debug properties in the physics config.

You should not typically use this in a production game. Use it to aid during debugging.

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - The Graphics object that was created for use by the World.

> Source: [src/physics/arcade/World.js#L668](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/World.js#L668)  
> Since: 3.0.0

---

## destroy

### <instance> destroy()

**Description:**

Shuts down the simulation and disconnects it from the current scene.

**Overrides:** Phaser.Events.EventEmitter#destroy

> Source: [src/physics/arcade/World.js#L2510](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/World.js#L2510)  
> Since: 3.0.0

---

## disable

### <instance> disable(object)

**Description:**

Disables the Arcade Physics Body of a Game Object, an array of Game Objects, or the children of a Group.

The difference between this and the `disableBody` method is that you can pass arrays or Groups

to this method.

The body itself is not deleted, it just has its `enable` property set to false, which

means you can re-enable it again at any point by passing it to enable `World.enable` or `World.add`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| object | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | Array.<[Phaser.GameObjects.GameObject](gameobjects-gameobject.md)> | [Phaser.GameObjects.Group](gameobjects-group.md) | Array.<[Phaser.GameObjects.Group](gameobjects-group.md)> |
| --- | --- | --- | --- |

> Source: [src/physics/arcade/World.js#L570](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/World.js#L570)  
> Since: 3.0.0

---

## disableBody

### <instance> disableBody(body)

**Description:**

Disables an existing Arcade Physics Body or StaticBody and removes it from the simulation.

The body is disabled and removed from the local search trees.

The body itself is not deleted, it just has its `enable` property set to false, which

means you can re-enable it again at any point by passing it to enable `World.enable` or `World.add`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| body | [Phaser.Physics.Arcade.Body](physics-arcade-body.md) | [Phaser.Physics.Arcade.StaticBody](physics-arcade-staticbody.md) | No | The Body to be disabled. |
| --- | --- | --- | --- |

> Source: [src/physics/arcade/World.js#L621](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/World.js#L621)  
> Since: 3.0.0

---

## emit

### <instance> emit(event, [args])

**Description:**

Calls each of the listeners registered for a given event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | string | symbol | No | The event name. |
| --- | --- | --- | --- |
| args | \* | Yes | Additional arguments that will be passed to the event handler. |

**Returns:** boolean - `true` if the event had listeners, else `false`.

**Inherits:** [Phaser.Events.EventEmitter#emit](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L86](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L86)  
> Since: 3.0.0

---

## enable

### <instance> enable(object, [bodyType])

**Description:**

Adds an Arcade Physics Body to a Game Object, an array of Game Objects, or the children of a Group.

The difference between this and the `enableBody` method is that you can pass arrays or Groups

to this method.

You can specify if the bodies are to be Dynamic or Static. A dynamic body can move via velocity and

acceleration. A static body remains fixed in place and as such is able to use an optimized search

tree, making it ideal for static elements such as level objects. You can still collide and overlap

with static bodies.

Normally, rather than calling this method directly, you'd use the helper methods available in the

Arcade Physics Factory, such as:

```
Copy
this.physics.add.image(x, y, textureKey);

this.physics.add.sprite(x, y, textureKey);


```

Calling factory methods encapsulates the creation of a Game Object and the creation of its

body at the same time. If you are creating custom classes then you can pass them to this

method to have their bodies created.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| object | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | Array.<[Phaser.GameObjects.GameObject](gameobjects-gameobject.md)> | [Phaser.GameObjects.Group](gameobjects-group.md) | Array.<[Phaser.GameObjects.Group](gameobjects-group.md)> |
| --- | --- | --- | --- |
| bodyType | number | Yes | The type of Body to create. Either `DYNAMIC_BODY` or `STATIC_BODY`. |

> Source: [src/physics/arcade/World.js#L418](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/World.js#L418)  
> Since: 3.0.0

---

## enableBody

### <instance> enableBody(object, [bodyType])

**Description:**

Creates an Arcade Physics Body on a single Game Object.

If the Game Object already has a body, this method will simply add it back into the simulation.

You can specify if the body is Dynamic or Static. A dynamic body can move via velocity and

acceleration. A static body remains fixed in place and as such is able to use an optimized search

tree, making it ideal for static elements such as level objects. You can still collide and overlap

with static bodies.

Normally, rather than calling this method directly, you'd use the helper methods available in the

Arcade Physics Factory, such as:

```
Copy
this.physics.add.image(x, y, textureKey);

this.physics.add.sprite(x, y, textureKey);


```

Calling factory methods encapsulates the creation of a Game Object and the creation of its

body at the same time. If you are creating custom classes then you can pass them to this

method to have their bodies created.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| object | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No | The Game Object on which to create the body. |
| --- | --- | --- | --- |
| bodyType | number | Yes | The type of Body to create. Either `DYNAMIC_BODY` or `STATIC_BODY`. |

**Returns:** [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) - The Game Object on which the body was created.

> Source: [src/physics/arcade/World.js#L486](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/World.js#L486)  
> Since: 3.0.0

---

## eventNames

### <instance> eventNames()

**Description:**

Return an array listing the events for which the emitter has registered listeners.

**Returns:** Array.<(string | symbol)> - undefined

**Inherits:** [Phaser.Events.EventEmitter#eventNames](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L55](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L55)  
> Since: 3.0.0

---

## intersects

### <instance> intersects(body1, body2)

**Description:**

Checks to see if two Bodies intersect at all.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| body1 | [Phaser.Physics.Arcade.Body](physics-arcade-body.md) | No | The first body to check. |
| --- | --- | --- | --- |
| body2 | [Phaser.Physics.Arcade.Body](physics-arcade-body.md) | No | The second body to check. |

**Returns:** boolean - True if the two bodies intersect, otherwise false.

> Source: [src/physics/arcade/World.js#L1683](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/World.js#L1683)  
> Since: 3.0.0

---

## listenerCount

### <instance> listenerCount(event)

**Description:**

Return the number of listeners listening to a given event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | string | symbol | No | The event name. |
| --- | --- | --- | --- |

**Returns:** number - The number of listeners.

**Inherits:** [Phaser.Events.EventEmitter#listenerCount](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L75](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L75)  
> Since: 3.0.0

---

## listeners

### <instance> listeners(event)

**Description:**

Return the listeners registered for a given event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | string | symbol | No | The event name. |
| --- | --- | --- | --- |

**Returns:** Array.<function()> - The registered listeners.

**Inherits:** [Phaser.Events.EventEmitter#listeners](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L64](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L64)  
> Since: 3.0.0

---

## off

### <instance> off(event, [fn], [context], [once])

**Description:**

Remove the listeners of a given event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | string | symbol | No | The event name. |
| --- | --- | --- | --- |
| fn | function | Yes | Only remove the listeners that match this function. |
| context | \* | Yes | Only remove the listeners that have this context. |
| once | boolean | Yes | Only remove one-time listeners. |

**Returns:** [Phaser.Physics.Arcade.World](physics-arcade-world.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#off](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L151](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L151)  
> Since: 3.0.0

---

## on

### <instance> on(event, fn, [context])

**Description:**

Add a listener for a given event.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| event | string | symbol | No |  | The event name. |
| --- | --- | --- | --- | --- |
| fn | function | No |  | The listener function. |
| context | \* | Yes | "this" | The context to invoke the listener with. |

**Returns:** [Phaser.Physics.Arcade.World](physics-arcade-world.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#on](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L98](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L98)  
> Since: 3.0.0

---

## once

### <instance> once(event, fn, [context])

**Description:**

Add a one-time listener for a given event.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| event | string | symbol | No |  | The event name. |
| --- | --- | --- | --- | --- |
| fn | function | No |  | The listener function. |
| context | \* | Yes | "this" | The context to invoke the listener with. |

**Returns:** [Phaser.Physics.Arcade.World](physics-arcade-world.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#once](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L124](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L124)  
> Since: 3.0.0

---

## overlap

### <instance> overlap(object1, [object2], [overlapCallback], [processCallback], [callbackContext])

**Description:**

Tests if Game Objects overlap.

See details in [Phaser.Physics.Arcade.World#collide](physics-arcade-world.md).

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| object1 | [Phaser.Types.Physics.Arcade.ArcadeColliderType](../typedef/types-physics-arcade.md) | No | The first object or array of objects to check. |
| --- | --- | --- | --- |
| object2 | [Phaser.Types.Physics.Arcade.ArcadeColliderType](../typedef/types-physics-arcade.md) | Yes | The second object or array of objects to check, or `undefined`. |
| overlapCallback | [Phaser.Types.Physics.Arcade.ArcadePhysicsCallback](../typedef/types-physics-arcade.md) | Yes | An optional callback function that is called if the objects overlap. |
| processCallback | [Phaser.Types.Physics.Arcade.ArcadePhysicsCallback](../typedef/types-physics-arcade.md) | Yes | An optional callback function that lets you perform additional checks against the two objects if they overlap. If this is set then `overlapCallback` will only be called if this callback returns `true`. |
| callbackContext | \* | Yes | The context in which to run the callbacks. |

**Returns:** boolean - True if at least one Game Object overlaps another.

> Source: [src/physics/arcade/World.js#L1753](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/World.js#L1753)  
> Since: 3.0.0

---

## overlapTiles

### <instance> overlapTiles(sprite, tiles, [collideCallback], [processCallback], [callbackContext])

**Description:**

This advanced method is specifically for testing for overlaps between a single Sprite and an array of Tile objects.

You should generally use the `overlap` method instead, with a Sprite vs. a Tilemap Layer, as that will perform

tile filtering and culling for you, as well as handle the interesting face collision automatically.

This method is offered for those who would like to check for overlaps with specific Tiles in a layer, without

having to set any collision attributes on the tiles in question. This allows you to perform quick dynamic overlap

tests on small sets of Tiles. As such, no culling or checks are made to the array of Tiles given to this method,

you should filter them before passing them to this method.

This method does not factor in the Collision Mask or Category.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| sprite | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No | The first object to check for collision. |
| --- | --- | --- | --- |
| tiles | Array.<[Phaser.Tilemaps.Tile](tilemaps-tile.md)> | No | An array of Tiles to check for collision against. |
| collideCallback | [Phaser.Types.Physics.Arcade.ArcadePhysicsCallback](../typedef/types-physics-arcade.md) | Yes | An optional callback function that is called if the objects overlap. |
| processCallback | [Phaser.Types.Physics.Arcade.ArcadePhysicsCallback](../typedef/types-physics-arcade.md) | Yes | An optional callback function that lets you perform additional checks against the two objects if they collide. If this is set then `collideCallback` will only be called if this callback returns `true`. |
| callbackContext | any | Yes | The context in which to run the callbacks. |

**Returns:** boolean - True if any objects overlap (with `overlapOnly`); or true if any overlapping objects were separated.

**Fires:** [Phaser.Physics.Arcade.Events#event:TILE\_OVERLAP](../event/physics-arcade-events.md)

> Source: [src/physics/arcade/World.js#L2236](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/World.js#L2236)  
> Since: 3.17.0

---

## pause

### <instance> pause()

**Description:**

Pauses the simulation.

A paused simulation does not update any existing bodies, or run any Colliders.

However, you can still enable and disable bodies within it, or manually run collide or overlap

checks.

**Returns:** [Phaser.Physics.Arcade.World](physics-arcade-world.md) - This World object.

**Fires:** [Phaser.Physics.Arcade.Events#event:PAUSE](../event/physics-arcade-events.md)

> Source: [src/physics/arcade/World.js#L760](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/World.js#L760)  
> Since: 3.0.0

---

## postUpdate

### <instance> postUpdate()

**Description:**

Updates bodies, draws the debug display, and handles pending queue operations.

> Source: [src/physics/arcade/World.js#L1077](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/World.js#L1077)  
> Since: 3.0.0

---

## remove

### <instance> remove(body)

**Description:**

Removes an existing Arcade Physics Body or StaticBody from the simulation.

The body is disabled and removed from the local search trees.

The body itself is not deleted, it just has its `enabled` property set to false, which

means you can re-enable it again at any point by passing it to enable `enable` or `add`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| body | [Phaser.Physics.Arcade.Body](physics-arcade-body.md) | [Phaser.Physics.Arcade.StaticBody](physics-arcade-staticbody.md) | No | The body to be removed from the simulation. |
| --- | --- | --- | --- |

> Source: [src/physics/arcade/World.js#L641](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/World.js#L641)  
> Since: 3.0.0

---

## removeAllListeners

### <instance> removeAllListeners([event])

**Description:**

Remove all listeners, or those of the specified event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | string | symbol | Yes | The event name. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Arcade.World](physics-arcade-world.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#removeAllListeners](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L165](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L165)  
> Since: 3.0.0

---

## removeCollider

### <instance> removeCollider(collider)

**Description:**

Removes a Collider from the simulation so it is no longer processed.

This method does not destroy the Collider. If you wish to add it back at a later stage you can call

`World.colliders.add(Collider)`.

If you no longer need the Collider you can call the `Collider.destroy` method instead, which will

automatically clear all of its references and then remove it from the World. If you call destroy on

a Collider you *don't* need to pass it to this method too.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| collider | [Phaser.Physics.Arcade.Collider](physics-arcade-collider.md) | No | The Collider to remove from the simulation. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Arcade.World](physics-arcade-world.md) - This World object.

> Source: [src/physics/arcade/World.js#L872](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/World.js#L872)  
> Since: 3.0.0

---

## removeListener

### <instance> removeListener(event, [fn], [context], [once])

**Description:**

Remove the listeners of a given event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | string | symbol | No | The event name. |
| --- | --- | --- | --- |
| fn | function | Yes | Only remove the listeners that match this function. |
| context | \* | Yes | Only remove the listeners that have this context. |
| once | boolean | Yes | Only remove one-time listeners. |

**Returns:** [Phaser.Physics.Arcade.World](physics-arcade-world.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#removeListener](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L137](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L137)  
> Since: 3.0.0

---

## resume

### <instance> resume()

**Description:**

Resumes the simulation, if paused.

**Returns:** [Phaser.Physics.Arcade.World](physics-arcade-world.md) - This World object.

**Fires:** [Phaser.Physics.Arcade.Events#event:RESUME](../event/physics-arcade-events.md)

> Source: [src/physics/arcade/World.js#L783](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/World.js#L783)  
> Since: 3.0.0

---

## separate

### <instance> separate(body1, body2, [processCallback], [callbackContext], [overlapOnly])

**Description:**

Separates two Bodies.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| body1 | [Phaser.Physics.Arcade.Body](physics-arcade-body.md) | No | The first Body to be separated. |
| --- | --- | --- | --- |
| body2 | [Phaser.Physics.Arcade.Body](physics-arcade-body.md) | No | The second Body to be separated. |
| processCallback | [Phaser.Types.Physics.Arcade.ArcadePhysicsCallback](../typedef/types-physics-arcade.md) | Yes | The process callback. |
| callbackContext | \* | Yes | The context in which to invoke the callback. |
| overlapOnly | boolean | Yes | If this a collide or overlap check? |

**Returns:** boolean - True if separation occurred, otherwise false.

**Fires:** [Phaser.Physics.Arcade.Events#event:COLLIDE](../event/physics-arcade-events.md), [Phaser.Physics.Arcade.Events#event:OVERLAP](../event/physics-arcade-events.md)

> Source: [src/physics/arcade/World.js#L1363](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/World.js#L1363)  
> Since: 3.0.0

---

## separateCircle

### <instance> separateCircle(body1, body2, [overlapOnly])

**Description:**

Separates two Bodies, when both are circular.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| body1 | [Phaser.Physics.Arcade.Body](physics-arcade-body.md) | No | The first Body to be separated. |
| --- | --- | --- | --- |
| body2 | [Phaser.Physics.Arcade.Body](physics-arcade-body.md) | No | The second Body to be separated. |
| overlapOnly | boolean | Yes | If this a collide or overlap check? |

**Returns:** boolean - True if separation occurred, otherwise false.

**Fires:** [Phaser.Physics.Arcade.Events#event:COLLIDE](../event/physics-arcade-events.md), [Phaser.Physics.Arcade.Events#event:OVERLAP](../event/physics-arcade-events.md)

> Source: [src/physics/arcade/World.js#L1478](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/World.js#L1478)  
> Since: 3.0.0

---

## setBounds

### <instance> setBounds(x, y, width, height, [checkLeft], [checkRight], [checkUp], [checkDown])

**Description:**

Sets the position, size and properties of the World boundary.

The World boundary is an invisible rectangle that defines the edges of the World.

If a Body is set to collide with the world bounds then it will automatically stop

when it reaches any of the edges. You can optionally set which edges of the boundary

should be checked against.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The top-left x coordinate of the boundary. |
| --- | --- | --- | --- |
| y | number | No | The top-left y coordinate of the boundary. |
| width | number | No | The width of the boundary. |
| height | number | No | The height of the boundary. |
| checkLeft | boolean | Yes | Should bodies check against the left edge of the boundary? |
| checkRight | boolean | Yes | Should bodies check against the right edge of the boundary? |
| checkUp | boolean | Yes | Should bodies check against the top edge of the boundary? |
| checkDown | boolean | Yes | Should bodies check against the bottom edge of the boundary? |

**Returns:** [Phaser.Physics.Arcade.World](physics-arcade-world.md) - This World object.

> Source: [src/physics/arcade/World.js#L698](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/World.js#L698)  
> Since: 3.0.0

---

## setBoundsCollision

### <instance> setBoundsCollision([left], [right], [up], [down])

**Description:**

Enables or disables collisions on each edge of the World boundary.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| left | boolean | Yes | true | Should bodies check against the left edge of the boundary? |
| --- | --- | --- | --- | --- |
| right | boolean | Yes | true | Should bodies check against the right edge of the boundary? |
| up | boolean | Yes | true | Should bodies check against the top edge of the boundary? |
| down | boolean | Yes | true | Should bodies check against the bottom edge of the boundary? |

**Returns:** [Phaser.Physics.Arcade.World](physics-arcade-world.md) - This World object.

> Source: [src/physics/arcade/World.js#L732](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/World.js#L732)  
> Since: 3.0.0

---

## setFPS

### <instance> setFPS(framerate)

**Description:**

Sets the frame rate to run the simulation at.

The frame rate value is used to simulate a fixed update time step. This fixed

time step allows for a straightforward implementation of a deterministic game state.

This frame rate is independent of the frequency at which the game is rendering. The

higher you set the fps, the more physics simulation steps will occur per game step.

Conversely, the lower you set it, the less will take place.

You can optionally advance the simulation directly yourself by calling the `step` method.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| framerate | number | No | The frame rate to advance the simulation at. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Arcade.World](physics-arcade-world.md) - This World object.

> Source: [src/physics/arcade/World.js#L896](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/World.js#L896)  
> Since: 3.10.0

---

## shutdown

### <instance> shutdown()

**Description:**

Shuts down the simulation, clearing physics data and removing listeners.

**Overrides:** Phaser.Events.EventEmitter#shutdown

> Source: [src/physics/arcade/World.js#L2493](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/World.js#L2493)  
> Since: 3.0.0

---

## singleStep

### <instance> singleStep()

**Description:**

Advances the simulation by a single step.

**Fires:** [Phaser.Physics.Arcade.Events#event:WORLD\_STEP](../event/physics-arcade-events.md)

> Source: [src/physics/arcade/World.js#L1063](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/World.js#L1063)  
> Since: 3.70.0

---

## step

### <instance> step(delta)

**Description:**

Advances the simulation by a time increment.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| delta | number | No | The delta time amount, in seconds, by which to advance the simulation. |
| --- | --- | --- | --- |

**Fires:** [Phaser.Physics.Arcade.Events#event:WORLD\_STEP](../event/physics-arcade-events.md)

> Source: [src/physics/arcade/World.js#L1011](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/World.js#L1011)  
> Since: 3.10.0

---

## update

### <instance> update(time, delta)

**Description:**

Advances the simulation based on the elapsed time and fps rate.

This is called automatically by your Scene and does not need to be invoked directly.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| time | number | No | The current timestamp as generated by the Request Animation Frame or SetTimeout. |
| --- | --- | --- | --- |
| delta | number | No | The delta time, in ms, elapsed since the last frame. |

**Fires:** [Phaser.Physics.Arcade.Events#event:WORLD\_STEP](../event/physics-arcade-events.md)

> Source: [src/physics/arcade/World.js#L924](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/World.js#L924)  
> Since: 3.0.0

---

## updateMotion

### <instance> updateMotion(body, delta)

**Description:**

Calculates a Body's velocity and updates its position.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| body | [Phaser.Physics.Arcade.Body](physics-arcade-body.md) | No | The Body to be updated. |
| --- | --- | --- | --- |
| delta | number | No | The delta value to be used in the motion calculations, in seconds. |

> Source: [src/physics/arcade/World.js#L1172](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/World.js#L1172)  
> Since: 3.0.0

---

## wrap

### <instance> wrap(object, [padding])

**Description:**

Wrap an object's coordinates (or several objects' coordinates) within [Phaser.Physics.Arcade.World#bounds](physics-arcade-world.md).

If the object is outside any boundary edge (left, top, right, bottom), it will be moved to the same offset from the opposite edge (the interior).

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| object | any | No |  | A Game Object, a Group, an object with `x` and `y` coordinates, or an array of such objects. |
| --- | --- | --- | --- | --- |
| padding | number | Yes | 0 | An amount added to each boundary edge during the operation. |

> Source: [src/physics/arcade/World.js#L2428](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/World.js#L2428)  
> Since: 3.3.0

---

## wrapArray

### <instance> wrapArray(objects, [padding])

**Description:**

Wrap each object's coordinates within [Phaser.Physics.Arcade.World#bounds](physics-arcade-world.md).

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| objects | Array.<\*> | No |  | An array of objects to be wrapped. |
| --- | --- | --- | --- | --- |
| padding | number | Yes | 0 | An amount added to the boundary. |

> Source: [src/physics/arcade/World.js#L2459](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/World.js#L2459)  
> Since: 3.3.0

---

## wrapObject

### <instance> wrapObject(object, [padding])

**Description:**

Wrap an object's coordinates within [Phaser.Physics.Arcade.World#bounds](physics-arcade-world.md).

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| object | \* | No |  | A Game Object, a Physics Body, or any object with `x` and `y` coordinates |
| --- | --- | --- | --- | --- |
| padding | number | Yes | 0 | An amount added to the boundary. |

> Source: [src/physics/arcade/World.js#L2476](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/World.js#L2476)  
> Since: 3.3.0

---

# Private Methods

## collideGroupVsGroup

### <instance> collideGroupVsGroup(group1, group2, [collideCallback], [processCallback], [callbackContext], overlapOnly)

**Description:**

Internal helper for Group vs. Group collisions.

Please use Phaser.Physics.Arcade.World#collide instead.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| group1 | [Phaser.GameObjects.Group](gameobjects-group.md) | No | The first object to check for collision. |
| --- | --- | --- | --- |
| group2 | [Phaser.GameObjects.Group](gameobjects-group.md) | No | The second object to check for collision. |
| collideCallback | [Phaser.Types.Physics.Arcade.ArcadePhysicsCallback](../typedef/types-physics-arcade.md) | Yes | An optional callback function that is called if the objects collide. |
| processCallback | [Phaser.Types.Physics.Arcade.ArcadePhysicsCallback](../typedef/types-physics-arcade.md) | Yes | An optional callback function that lets you perform additional checks against the two objects if they collide. If this is set then `collideCallback` will only be called if this callback returns `true`. |
| callbackContext | any | Yes | The context in which to run the callbacks. |
| overlapOnly | boolean | No | Whether this is a collision or overlap check. |

**Returns:** boolean - True if any objects overlap (with `overlapOnly`); or true if any overlapping objects were separated.

> Source: [src/physics/arcade/World.js#L2396](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/World.js#L2396)  
> Since: 3.0.0

---

## collideGroupVsTilemapLayer

### <instance> collideGroupVsTilemapLayer(group, tilemapLayer, collideCallback, processCallback, callbackContext, overlapOnly)

**Description:**

Internal handler for Group vs. Tilemap collisions.

Please use Phaser.Physics.Arcade.World#collide instead.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| group | [Phaser.GameObjects.Group](gameobjects-group.md) | No | The first object to check for collision. |
| --- | --- | --- | --- |
| tilemapLayer | [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) | No | The second object to check for collision. |
| collideCallback | [Phaser.Types.Physics.Arcade.ArcadePhysicsCallback](../typedef/types-physics-arcade.md) | No | An optional callback function that is called if the objects collide. |
| processCallback | [Phaser.Types.Physics.Arcade.ArcadePhysicsCallback](../typedef/types-physics-arcade.md) | No | An optional callback function that lets you perform additional checks against the two objects if they collide. If this is set then `collideCallback` will only be called if this callback returns `true`. |
| callbackContext | any | No | The context in which to run the callbacks. |
| overlapOnly | boolean | No | Whether this is a collision or overlap check. |

**Returns:** boolean - True if any objects overlap (with `overlapOnly`); or true if any overlapping objects were separated.

> Source: [src/physics/arcade/World.js#L2147](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/World.js#L2147)  
> Since: 3.0.0

---

## collideHandler

### <instance> collideHandler(object1, object2, collideCallback, processCallback, callbackContext, overlapOnly)

**Description:**

Internal helper function. Please use Phaser.Physics.Arcade.World#collide and Phaser.Physics.Arcade.World#overlap instead.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| object1 | [Phaser.Types.Physics.Arcade.ArcadeColliderType](../typedef/types-physics-arcade.md) | No | The first object or array of objects to check. |
| --- | --- | --- | --- |
| object2 | [Phaser.Types.Physics.Arcade.ArcadeColliderType](../typedef/types-physics-arcade.md) | No | The second object or array of objects to check, or `undefined`. |
| collideCallback | [Phaser.Types.Physics.Arcade.ArcadePhysicsCallback](../typedef/types-physics-arcade.md) | No | An optional callback function that is called if the objects collide. |
| processCallback | [Phaser.Types.Physics.Arcade.ArcadePhysicsCallback](../typedef/types-physics-arcade.md) | No | An optional callback function that lets you perform additional checks against the two objects if they collide. If this is set then `collideCallback` will only be called if this callback returns `true`. |
| callbackContext | any | No | The context in which to run the callbacks. |
| overlapOnly | boolean | No | Whether this is a collision or overlap check. |

**Returns:** boolean - True if any objects overlap (with `overlapOnly`); or true if any overlapping objects were separated.

> Source: [src/physics/arcade/World.js#L1914](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/World.js#L1914)  
> Since: 3.0.0

---

## collideObjects

### <instance> collideObjects(object1, [object2], collideCallback, processCallback, callbackContext, overlapOnly)

**Description:**

Internal helper function. Please use Phaser.Physics.Arcade.World#collide instead.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| object1 | [Phaser.Types.Physics.Arcade.ArcadeColliderType](../typedef/types-physics-arcade.md) | No | The first object to check for collision. |
| --- | --- | --- | --- |
| object2 | [Phaser.Types.Physics.Arcade.ArcadeColliderType](../typedef/types-physics-arcade.md) | Yes | The second object to check for collision. |
| collideCallback | [Phaser.Types.Physics.Arcade.ArcadePhysicsCallback](../typedef/types-physics-arcade.md) | No | The callback to invoke when the two objects collide. |
| processCallback | [Phaser.Types.Physics.Arcade.ArcadePhysicsCallback](../typedef/types-physics-arcade.md) | No | The callback to invoke when the two objects collide. Must return a boolean. |
| callbackContext | any | No | The scope in which to call the callbacks. |
| overlapOnly | boolean | No | Whether this is a collision or overlap check. |

**Returns:** boolean - True if any objects overlap (with `overlapOnly`); or true if any overlapping objects were separated.

> Source: [src/physics/arcade/World.js#L1821](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/World.js#L1821)  
> Since: 3.0.0

---

## collideSpriteVsGroup

### <instance> collideSpriteVsGroup(sprite, group, collideCallback, processCallback, callbackContext, overlapOnly)

**Description:**

Internal handler for Sprite vs. Group collisions.

Please use Phaser.Physics.Arcade.World#collide instead.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| sprite | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No | The first object to check for collision. |
| --- | --- | --- | --- |
| group | [Phaser.GameObjects.Group](gameobjects-group.md) | No | The second object to check for collision. |
| collideCallback | [Phaser.Types.Physics.Arcade.ArcadePhysicsCallback](../typedef/types-physics-arcade.md) | No | The callback to invoke when the two objects collide. |
| processCallback | [Phaser.Types.Physics.Arcade.ArcadePhysicsCallback](../typedef/types-physics-arcade.md) | No | The callback to invoke when the two objects collide. Must return a boolean. |
| callbackContext | any | No | The scope in which to call the callbacks. |
| overlapOnly | boolean | No | Whether this is a collision or overlap check. |

> Source: [src/physics/arcade/World.js#L2054](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/World.js#L2054)  
> Since: 3.0.0

---

## collideSpriteVsSprite

### <instance> collideSpriteVsSprite(sprite1, sprite2, [collideCallback], [processCallback], [callbackContext], overlapOnly)

**Description:**

Internal handler for Sprite vs. Sprite collisions.

Please use Phaser.Physics.Arcade.World#collide instead.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| sprite1 | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No | The first object to check for collision. |
| --- | --- | --- | --- |
| sprite2 | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No | The second object to check for collision. |
| collideCallback | [Phaser.Types.Physics.Arcade.ArcadePhysicsCallback](../typedef/types-physics-arcade.md) | Yes | An optional callback function that is called if the objects collide. |
| processCallback | [Phaser.Types.Physics.Arcade.ArcadePhysicsCallback](../typedef/types-physics-arcade.md) | Yes | An optional callback function that lets you perform additional checks against the two objects if they collide. If this is set then `collideCallback` will only be called if this callback returns `true`. |
| callbackContext | any | Yes | The context in which to run the callbacks. |
| overlapOnly | boolean | No | Whether this is a collision or overlap check. |

**Returns:** boolean - True if any objects overlap (with `overlapOnly`); or true if any overlapping objects were separated.

> Source: [src/physics/arcade/World.js#L2014](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/World.js#L2014)  
> Since: 3.0.0

---

## collideSpriteVsTilesHandler

### <instance> collideSpriteVsTilesHandler(sprite, tilemapLayer, [collideCallback], [processCallback], [callbackContext], [overlapOnly], [isLayer])

**Description:**

Internal handler for Sprite vs. Tilemap collisions.

Please use Phaser.Physics.Arcade.World#collide instead.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| sprite | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No | The first object to check for collision. |
| --- | --- | --- | --- |
| tilemapLayer | [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) | No | The second object to check for collision. |
| collideCallback | [Phaser.Types.Physics.Arcade.ArcadePhysicsCallback](../typedef/types-physics-arcade.md) | Yes | An optional callback function that is called if the objects collide. |
| processCallback | [Phaser.Types.Physics.Arcade.ArcadePhysicsCallback](../typedef/types-physics-arcade.md) | Yes | An optional callback function that lets you perform additional checks against the two objects if they collide. If this is set then `collideCallback` will only be called if this callback returns `true`. |
| callbackContext | any | Yes | The context in which to run the callbacks. |
| overlapOnly | boolean | Yes | Whether this is a collision or overlap check. |
| isLayer | boolean | Yes | Is this check coming from a TilemapLayer or an array of tiles? |

**Returns:** boolean - True if any objects overlap (with `overlapOnly`); or true if any overlapping objects were separated.

**Fires:** [Phaser.Physics.Arcade.Events#event:TILE\_COLLIDE](../event/physics-arcade-events.md), [Phaser.Physics.Arcade.Events#event:TILE\_OVERLAP](../event/physics-arcade-events.md)

> Source: [src/physics/arcade/World.js#L2324](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/World.js#L2324)  
> Since: 3.17.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [bodies](#bodies)

    - [bodies: Phaser.Structs.Set.<Phaser.Physics.Arcade.Body>](#bodies-phaserstructssetphaserphysicsarcadebody)
  + [bounds](#bounds)

    - [bounds: Phaser.Geom.Rectangle](#bounds-phasergeomrectangle)
  + [checkCollision](#checkcollision)

    - [checkCollision: Phaser.Types.Physics.Arcade.CheckCollisionObject](#checkcollision-phasertypesphysicsarcadecheckcollisionobject)
  + [colliders](#colliders)

    - [colliders: Phaser.Structs.ProcessQueue.<Phaser.Physics.Arcade.Collider>](#colliders-phaserstructsprocessqueuephaserphysicsarcadecollider)
  + [debugGraphic](#debuggraphic)

    - [debugGraphic: Phaser.GameObjects.Graphics](#debuggraphic-phasergameobjectsgraphics)
  + [defaults](#defaults)

    - [defaults: Phaser.Types.Physics.Arcade.ArcadeWorldDefaults](#defaults-phasertypesphysicsarcadearcadeworlddefaults)
  + [drawDebug](#drawdebug)

    - [drawDebug: boolean](#drawdebug-boolean)
  + [fixedStep](#fixedstep)

    - [fixedStep: boolean](#fixedstep-boolean)
  + [forceX](#forcex)

    - [forceX: boolean](#forcex-boolean)
  + [fps](#fps)

    - [fps: number](#fps-number)
  + [gravity](#gravity)

    - [gravity: Phaser.Math.Vector2](#gravity-phasermathvector2)
  + [isPaused](#ispaused)

    - [isPaused: boolean](#ispaused-boolean)
  + [maxEntries](#maxentries)

    - [maxEntries: number](#maxentries-number)
  + [OVERLAP\_BIAS](#overlap_bias)

    - [OVERLAP\_BIAS: number](#overlap_bias-number)
  + [pendingDestroy](#pendingdestroy)

    - [pendingDestroy: Phaser.Structs.Set.<(Phaser.Physics.Arcade.Body | Phaser.Physics.Arcade.StaticBody)>](#pendingdestroy-phaserstructssetphaserphysicsarcadebody--phaserphysicsarcadestaticbody)
  + [scene](#scene)

    - [scene: Phaser.Scene](#scene-phaserscene)
  + [staticBodies](#staticbodies)

    - [staticBodies: Phaser.Structs.Set.<Phaser.Physics.Arcade.StaticBody>](#staticbodies-phaserstructssetphaserphysicsarcadestaticbody)
  + [staticTree](#statictree)

    - [staticTree: Phaser.Structs.RTree](#statictree-phaserstructsrtree)
  + [stepsLastFrame](#stepslastframe)

    - [stepsLastFrame: number](#stepslastframe-number)
  + [TILE\_BIAS](#tile_bias)

    - [TILE\_BIAS: number](#tile_bias-number)
  + [tileFilterOptions](#tilefilteroptions)

    - [tileFilterOptions: Phaser.Types.Tilemaps.FilteringOptions](#tilefilteroptions-phasertypestilemapsfilteringoptions)
  + [timeScale](#timescale)

    - [timeScale: number](#timescale-number)
  + [tree](#tree)

    - [tree: Phaser.Structs.RTree](#tree-phaserstructsrtree)
  + [treeMinMax](#treeminmax)

    - [treeMinMax: Phaser.Types.Physics.Arcade.ArcadeWorldTreeMinMax](#treeminmax-phasertypesphysicsarcadearcadeworldtreeminmax)
  + [useTree](#usetree)

    - [useTree: boolean](#usetree-boolean)
* [Private Members](#private-members)

  + [\_category](#_category)

    - [\_category: number](#_category-number)
  + [\_elapsed](#_elapsed)

    - [\_elapsed: number](#_elapsed-number)
  + [\_frameTime](#_frametime)

    - [\_frameTime: number](#_frametime-number)
  + [\_frameTimeMS](#_frametimems)

    - [\_frameTimeMS: number](#_frametimems-number)
  + [\_tempMatrix](#_tempmatrix)

    - [\_tempMatrix: Phaser.GameObjects.Components.TransformMatrix](#_tempmatrix-phasergameobjectscomponentstransformmatrix)
  + [\_tempMatrix2](#_tempmatrix2)

    - [\_tempMatrix2: Phaser.GameObjects.Components.TransformMatrix](#_tempmatrix2-phasergameobjectscomponentstransformmatrix)
  + [\_total](#_total)

    - [\_total: number](#_total-number)
* [Public Methods](#public-methods)

  + [add](#add)

    - [<instance> add(body)](#instance-addbody)
  + [addCollider](#addcollider)

    - [<instance> addCollider(object1, object2, [collideCallback], [processCallback], [callbackContext])](#instance-addcolliderobject1-object2-collidecallback-processcallback-callbackcontext)
  + [addListener](#addlistener)

    - [<instance> addListener(event, fn, [context])](#instance-addlistenerevent-fn-context)
  + [addOverlap](#addoverlap)

    - [<instance> addOverlap(object1, object2, [collideCallback], [processCallback], [callbackContext])](#instance-addoverlapobject1-object2-collidecallback-processcallback-callbackcontext)
  + [canCollide](#cancollide)

    - [<instance> canCollide(body1, body2)](#instance-cancollidebody1-body2)
  + [circleBodyIntersects](#circlebodyintersects)

    - [<instance> circleBodyIntersects(circle, body)](#instance-circlebodyintersectscircle-body)
  + [collide](#collide)

    - [<instance> collide(object1, [object2], [collideCallback], [processCallback], [callbackContext])](#instance-collideobject1-object2-collidecallback-processcallback-callbackcontext)
  + [collideSpriteVsTilemapLayer](#collidespritevstilemaplayer)

    - [<instance> collideSpriteVsTilemapLayer(sprite, tilemapLayer, [collideCallback], [processCallback], [callbackContext], [overlapOnly])](#instance-collidespritevstilemaplayersprite-tilemaplayer-collidecallback-processcallback-callbackcontext-overlaponly)
  + [collideTiles](#collidetiles)

    - [<instance> collideTiles(sprite, tiles, [collideCallback], [processCallback], [callbackContext])](#instance-collidetilessprite-tiles-collidecallback-processcallback-callbackcontext)
  + [computeAngularVelocity](#computeangularvelocity)

    - [<instance> computeAngularVelocity(body, delta)](#instance-computeangularvelocitybody-delta)
  + [computeVelocity](#computevelocity)

    - [<instance> computeVelocity(body, delta)](#instance-computevelocitybody-delta)
  + [createDebugGraphic](#createdebuggraphic)

    - [<instance> createDebugGraphic()](#instance-createdebuggraphic)
  + [destroy](#destroy)

    - [<instance> destroy()](#instance-destroy)
  + [disable](#disable)

    - [<instance> disable(object)](#instance-disableobject)
  + [disableBody](#disablebody)

    - [<instance> disableBody(body)](#instance-disablebodybody)
  + [emit](#emit)

    - [<instance> emit(event, [args])](#instance-emitevent-args)
  + [enable](#enable)

    - [<instance> enable(object, [bodyType])](#instance-enableobject-bodytype)
  + [enableBody](#enablebody)

    - [<instance> enableBody(object, [bodyType])](#instance-enablebodyobject-bodytype)
  + [eventNames](#eventnames)

    - [<instance> eventNames()](#instance-eventnames)
  + [intersects](#intersects)

    - [<instance> intersects(body1, body2)](#instance-intersectsbody1-body2)
  + [listenerCount](#listenercount)

    - [<instance> listenerCount(event)](#instance-listenercountevent)
  + [listeners](#listeners)

    - [<instance> listeners(event)](#instance-listenersevent)
  + [off](#off)

    - [<instance> off(event, [fn], [context], [once])](#instance-offevent-fn-context-once)
  + [on](#on)

    - [<instance> on(event, fn, [context])](#instance-onevent-fn-context)
  + [once](#once)

    - [<instance> once(event, fn, [context])](#instance-onceevent-fn-context)
  + [overlap](#overlap)

    - [<instance> overlap(object1, [object2], [overlapCallback], [processCallback], [callbackContext])](#instance-overlapobject1-object2-overlapcallback-processcallback-callbackcontext)
  + [overlapTiles](#overlaptiles)

    - [<instance> overlapTiles(sprite, tiles, [collideCallback], [processCallback], [callbackContext])](#instance-overlaptilessprite-tiles-collidecallback-processcallback-callbackcontext)
  + [pause](#pause)

    - [<instance> pause()](#instance-pause)
  + [postUpdate](#postupdate)

    - [<instance> postUpdate()](#instance-postupdate)
  + [remove](#remove)

    - [<instance> remove(body)](#instance-removebody)
  + [removeAllListeners](#removealllisteners)

    - [<instance> removeAllListeners([event])](#instance-removealllistenersevent)
  + [removeCollider](#removecollider)

    - [<instance> removeCollider(collider)](#instance-removecollidercollider)
  + [removeListener](#removelistener)

    - [<instance> removeListener(event, [fn], [context], [once])](#instance-removelistenerevent-fn-context-once)
  + [resume](#resume)

    - [<instance> resume()](#instance-resume)
  + [separate](#separate)

    - [<instance> separate(body1, body2, [processCallback], [callbackContext], [overlapOnly])](#instance-separatebody1-body2-processcallback-callbackcontext-overlaponly)
  + [separateCircle](#separatecircle)

    - [<instance> separateCircle(body1, body2, [overlapOnly])](#instance-separatecirclebody1-body2-overlaponly)
  + [setBounds](#setbounds)

    - [<instance> setBounds(x, y, width, height, [checkLeft], [checkRight], [checkUp], [checkDown])](#instance-setboundsx-y-width-height-checkleft-checkright-checkup-checkdown)
  + [setBoundsCollision](#setboundscollision)

    - [<instance> setBoundsCollision([left], [right], [up], [down])](#instance-setboundscollisionleft-right-up-down)
  + [setFPS](#setfps)

    - [<instance> setFPS(framerate)](#instance-setfpsframerate)
  + [shutdown](#shutdown)

    - [<instance> shutdown()](#instance-shutdown)
  + [singleStep](#singlestep)

    - [<instance> singleStep()](#instance-singlestep)
  + [step](#step)

    - [<instance> step(delta)](#instance-stepdelta)
  + [update](#update)

    - [<instance> update(time, delta)](#instance-updatetime-delta)
  + [updateMotion](#updatemotion)

    - [<instance> updateMotion(body, delta)](#instance-updatemotionbody-delta)
  + [wrap](#wrap)

    - [<instance> wrap(object, [padding])](#instance-wrapobject-padding)
  + [wrapArray](#wraparray)

    - [<instance> wrapArray(objects, [padding])](#instance-wraparrayobjects-padding)
  + [wrapObject](#wrapobject)

    - [<instance> wrapObject(object, [padding])](#instance-wrapobjectobject-padding)
* [Private Methods](#private-methods)

  + [collideGroupVsGroup](#collidegroupvsgroup)

    - [<instance> collideGroupVsGroup(group1, group2, [collideCallback], [processCallback], [callbackContext], overlapOnly)](#instance-collidegroupvsgroupgroup1-group2-collidecallback-processcallback-callbackcontext-overlaponly)
  + [collideGroupVsTilemapLayer](#collidegroupvstilemaplayer)

    - [<instance> collideGroupVsTilemapLayer(group, tilemapLayer, collideCallback, processCallback, callbackContext, overlapOnly)](#instance-collidegroupvstilemaplayergroup-tilemaplayer-collidecallback-processcallback-callbackcontext-overlaponly)
  + [collideHandler](#collidehandler)

    - [<instance> collideHandler(object1, object2, collideCallback, processCallback, callbackContext, overlapOnly)](#instance-collidehandlerobject1-object2-collidecallback-processcallback-callbackcontext-overlaponly)
  + [collideObjects](#collideobjects)

    - [<instance> collideObjects(object1, [object2], collideCallback, processCallback, callbackContext, overlapOnly)](#instance-collideobjectsobject1-object2-collidecallback-processcallback-callbackcontext-overlaponly)
  + [collideSpriteVsGroup](#collidespritevsgroup)

    - [<instance> collideSpriteVsGroup(sprite, group, collideCallback, processCallback, callbackContext, overlapOnly)](#instance-collidespritevsgroupsprite-group-collidecallback-processcallback-callbackcontext-overlaponly)
  + [collideSpriteVsSprite](#collidespritevssprite)

    - [<instance> collideSpriteVsSprite(sprite1, sprite2, [collideCallback], [processCallback], [callbackContext], overlapOnly)](#instance-collidespritevsspritesprite1-sprite2-collidecallback-processcallback-callbackcontext-overlaponly)
  + [collideSpriteVsTilesHandler](#collidespritevstileshandler)

    - [<instance> collideSpriteVsTilesHandler(sprite, tilemapLayer, [collideCallback], [processCallback], [callbackContext], [overlapOnly], [isLayer])](#instance-collidespritevstileshandlersprite-tilemaplayer-collidecallback-processcallback-callbackcontext-overlaponly-islayer)

Back to top

©2025[Phaser](https://docs.phaser.io)



World