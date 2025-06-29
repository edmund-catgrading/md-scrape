# MatterPhysics

Phaser.Physics.Matter.MatterPhysics

The Phaser Matter plugin provides the ability to use the Matter JS Physics Engine within your Phaser games.

Unlike Arcade Physics, the other physics system provided with Phaser, Matter JS is a full-body physics system.

It features:

* Rigid bodies
* Compound bodies
* Composite bodies
* Concave and convex hulls
* Physical properties (mass, area, density etc.)
* Restitution (elastic and inelastic collisions)
* Collisions (broad-phase, mid-phase and narrow-phase)
* Stable stacking and resting
* Conservation of momentum
* Friction and resistance
* Constraints
* Gravity
* Sleeping and static bodies
* Rounded corners (chamfering)
* Views (translate, zoom)
* Collision queries (raycasting, region tests)
* Time scaling (slow-mo, speed-up)

Configuration of Matter is handled via the Matter World Config object, which can be passed in either the

Phaser Game Config, or Phaser Scene Config. Here is a basic example:

```
Copy
physics: {

    default: 'matter',

    matter: {

        enableSleeping: true,

        gravity: {

            y: 0

        },

        debug: {

            showBody: true,

            showStaticBody: true

        }

    }

}


```

This class acts as an interface between a Phaser Scene and a single instance of the Matter Engine.

Use it to access the most common Matter features and helper functions.

You can find details, documentation and examples on the Matter JS website: <https://brm.io/matter-js/>

**Constructor**

`new MatterPhysics(scene)`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| scene | [Phaser.Scene](scene.md) | No | The Phaser Scene that owns this Matter Physics instance. |
| --- | --- | --- | --- |

---

**Scope**: static

> Source: [src/physics/matter-js/MatterPhysics.js#L38](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/MatterPhysics.js#L38)  
> Since: 3.0.0

# Public Members

## add

### add: [Phaser.Physics.Matter.Factory](physics-matter-factory.md)

**Description:**

An instance of the Matter Factory. This class provides lots of functions for creating a

wide variety of physics objects and adds them automatically to the Matter World.

You can use this class to cut-down on the amount of code required in your game, however,

use of the Factory is entirely optional and should be seen as a development aid. It's

perfectly possible to create and add components to the Matter world without using it.

> Source: [src/physics/matter-js/MatterPhysics.js#L138](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/MatterPhysics.js#L138)  
> Since: 3.0.0

---

## axes

### axes: MatterJS.AxesFactory

**Description:**

A reference to the `Matter.Axes` module.

The `Matter.Axes` module contains methods for creating and manipulating sets of axes.

> Source: [src/physics/matter-js/MatterPhysics.js#L304](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/MatterPhysics.js#L304)  
> Since: 3.22.0

---

## bodies

### bodies: MatterJS.BodiesFactory

**Description:**

A reference to the `Matter.Bodies` module.

The `Matter.Bodies` module contains factory methods for creating rigid bodies

with commonly used body configurations (such as rectangles, circles and other polygons).

> Source: [src/physics/matter-js/MatterPhysics.js#L278](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/MatterPhysics.js#L278)  
> Since: 3.18.0

---

## body

### body: MatterJS.BodyFactory

**Description:**

A reference to the `Matter.Body` module.

The `Matter.Body` module contains methods for creating and manipulating body models.

A `Matter.Body` is a rigid body that can be simulated by a `Matter.Engine`.

Factories for commonly used body configurations (such as rectangles, circles and other polygons) can be found in the `Bodies` module.

> Source: [src/physics/matter-js/MatterPhysics.js#L164](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/MatterPhysics.js#L164)  
> Since: 3.18.0

---

## bodyBounds

### bodyBounds: [Phaser.Physics.Matter.BodyBounds](physics-matter-bodybounds.md)

**Description:**

An instance of the Body Bounds class. This class contains functions used for getting the

world position from various points around the bounds of a physics body.

> Source: [src/physics/matter-js/MatterPhysics.js#L152](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/MatterPhysics.js#L152)  
> Since: 3.22.0

---

## bounds

### bounds: MatterJS.BoundsFactory

**Description:**

A reference to the `Matter.Bounds` module.

The `Matter.Bounds` module contains methods for creating and manipulating axis-aligned bounding boxes (AABB).

> Source: [src/physics/matter-js/MatterPhysics.js#L315](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/MatterPhysics.js#L315)  
> Since: 3.22.0

---

## collision

### collision: MatterJS.Collision

**Description:**

A reference to the `Matter.Collision` module.

The `Matter.Collision` module contains methods for detecting collisions between a given pair of bodies.

For efficient detection between a list of bodies, see `Matter.Detector` and `Matter.Query`.

> Source: [src/physics/matter-js/MatterPhysics.js#L193](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/MatterPhysics.js#L193)  
> Since: 3.60.0

---

## composite

### composite: MatterJS.CompositeFactory

**Description:**

A reference to the `Matter.Composite` module.

The `Matter.Composite` module contains methods for creating and manipulating composite bodies.

A composite body is a collection of `Matter.Body`, `Matter.Constraint` and other `Matter.Composite`, therefore composites form a tree structure.

It is important to use the functions in this module to modify composites, rather than directly modifying their properties.

Note that the `Matter.World` object is also a type of `Matter.Composite` and as such all composite methods here can also operate on a `Matter.World`.

> Source: [src/physics/matter-js/MatterPhysics.js#L177](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/MatterPhysics.js#L177)  
> Since: 3.22.0

---

## composites

### composites: MatterJS.CompositesFactory

**Description:**

A reference to the `Matter.Composites` module.

The `Matter.Composites` module contains factory methods for creating composite bodies

with commonly used configurations (such as stacks and chains).

> Source: [src/physics/matter-js/MatterPhysics.js#L290](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/MatterPhysics.js#L290)  
> Since: 3.22.0

---

## config

### config: [Phaser.Types.Physics.Matter.MatterWorldConfig](../typedef/types-physics-matter.md)

**Description:**

The parsed Matter Configuration object.

> Source: [src/physics/matter-js/MatterPhysics.js#L119](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/MatterPhysics.js#L119)  
> Since: 3.0.0

---

## constraint

### constraint: MatterJS.ConstraintFactory

**Description:**

A reference to the `Matter.Constraint` module.

The `Matter.Constraint` module contains methods for creating and manipulating constraints.

Constraints are used for specifying that a fixed distance must be maintained between two bodies (or a body and a fixed world-space position).

The stiffness of constraints can be modified to create springs or elastic.

> Source: [src/physics/matter-js/MatterPhysics.js#L263](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/MatterPhysics.js#L263)  
> Since: 3.22.0

---

## detector

### detector: MatterJS.DetectorFactory

**Description:**

A reference to the `Matter.Detector` module.

The `Matter.Detector` module contains methods for detecting collisions given a set of pairs.

> Source: [src/physics/matter-js/MatterPhysics.js#L206](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/MatterPhysics.js#L206)  
> Since: 3.22.0

---

## pair

### pair: MatterJS.PairFactory

**Description:**

A reference to the `Matter.Pair` module.

The `Matter.Pair` module contains methods for creating and manipulating collision pairs.

> Source: [src/physics/matter-js/MatterPhysics.js#L217](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/MatterPhysics.js#L217)  
> Since: 3.22.0

---

## pairs

### pairs: MatterJS.PairsFactory

**Description:**

A reference to the `Matter.Pairs` module.

The `Matter.Pairs` module contains methods for creating and manipulating collision pair sets.

> Source: [src/physics/matter-js/MatterPhysics.js#L228](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/MatterPhysics.js#L228)  
> Since: 3.22.0

---

## query

### query: MatterJS.QueryFactory

**Description:**

A reference to the `Matter.Query` module.

The `Matter.Query` module contains methods for performing collision queries.

> Source: [src/physics/matter-js/MatterPhysics.js#L239](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/MatterPhysics.js#L239)  
> Since: 3.22.0

---

## resolver

### resolver: MatterJS.ResolverFactory

**Description:**

A reference to the `Matter.Resolver` module.

The `Matter.Resolver` module contains methods for resolving collision pairs.

> Source: [src/physics/matter-js/MatterPhysics.js#L250](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/MatterPhysics.js#L250)  
> Since: 3.22.0

---

## scene

### scene: [Phaser.Scene](scene.md)

**Description:**

The Phaser Scene that owns this Matter Physics instance

> Source: [src/physics/matter-js/MatterPhysics.js#L101](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/MatterPhysics.js#L101)  
> Since: 3.0.0

---

## svg

### svg: MatterJS.SvgFactory

**Description:**

A reference to the `Matter.Svg` module.

The `Matter.Svg` module contains methods for converting SVG images into an array of vector points.

To use this module you also need the SVGPathSeg polyfill: <https://github.com/progers/pathseg>

> Source: [src/physics/matter-js/MatterPhysics.js#L326](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/MatterPhysics.js#L326)  
> Since: 3.22.0

---

## systems

### systems: [Phaser.Scenes.Systems](scenes-systems.md)

**Description:**

A reference to the Scene Systems that belong to the Scene owning this Matter Physics instance.

> Source: [src/physics/matter-js/MatterPhysics.js#L110](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/MatterPhysics.js#L110)  
> Since: 3.0.0

---

## vector

### vector: MatterJS.VectorFactory

**Description:**

A reference to the `Matter.Vector` module.

The `Matter.Vector` module contains methods for creating and manipulating vectors.

Vectors are the basis of all the geometry related operations in the engine.

A `Matter.Vector` object is of the form `{ x: 0, y: 0 }`.

> Source: [src/physics/matter-js/MatterPhysics.js#L339](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/MatterPhysics.js#L339)  
> Since: 3.22.0

---

## vertices

### vertices: MatterJS.VerticesFactory

**Description:**

A reference to the `Matter.Vertices` module.

The `Matter.Vertices` module contains methods for creating and manipulating sets of vertices.

A set of vertices is an array of `Matter.Vector` with additional indexing properties inserted by `Vertices.create`.

A `Matter.Body` maintains a set of vertices to represent the shape of the object (its convex hull).

> Source: [src/physics/matter-js/MatterPhysics.js#L352](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/MatterPhysics.js#L352)  
> Since: 3.22.0

---

## verts

### verts: MatterJS.VerticesFactory

**Description:**

A reference to the `Matter.Vertices` module.

The `Matter.Vertices` module contains methods for creating and manipulating sets of vertices.

A set of vertices is an array of `Matter.Vector` with additional indexing properties inserted by `Vertices.create`.

A `Matter.Body` maintains a set of vertices to represent the shape of the object (its convex hull).

> Source: [src/physics/matter-js/MatterPhysics.js#L365](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/MatterPhysics.js#L365)  
> Since: 3.14.0

---

## world

### world: [Phaser.Physics.Matter.World](physics-matter-world.md)

**Description:**

An instance of the Matter World class. This class is responsible for the updating of the

Matter Physics world, as well as handling debug drawing functions.

> Source: [src/physics/matter-js/MatterPhysics.js#L128](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/MatterPhysics.js#L128)  
> Since: 3.0.0

---

# Private Members

## \_tempVec2

### \_tempVec2: MatterJS.Vector

**Description:**

An internal temp vector used for velocity and force calculations.

**Access:** private

> Source: [src/physics/matter-js/MatterPhysics.js#L378](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/MatterPhysics.js#L378)  
> Since: 3.22.0

---

# Public Methods

## alignBody

### <instance> alignBody(body, x, y, align)

**Description:**

Aligns a Body, or Matter Game Object, against the given coordinates.

The alignment takes place using the body bounds, which take into consideration things

like body scale and rotation.

Although a Body has a `position` property, it is based on the center of mass for the body,

not a dimension based center. This makes aligning bodies difficult, especially if they have

rotated or scaled. This method will derive the correct position based on the body bounds and

its center of mass offset, in order to align the body with the given coordinate.

For example, if you wanted to align a body so it sat in the bottom-center of the

Scene, and the world was 800 x 600 in size:

```
Copy
this.matter.alignBody(body, 400, 600, Phaser.Display.Align.BOTTOM_CENTER);


```

You pass in 400 for the x coordinate, because that is the center of the world, and 600 for

the y coordinate, as that is the base of the world.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| body | [Phaser.Types.Physics.Matter.MatterBody](../typedef/types-physics-matter.md) | No | The Body to align. |
| --- | --- | --- | --- |
| x | number | No | The horizontal position to align the body to. |
| y | number | No | The vertical position to align the body to. |
| align | number | No | One of the `Phaser.Display.Align` constants, such as `Phaser.Display.Align.TOP_LEFT`. |

**Returns:** [Phaser.Physics.Matter.MatterPhysics](physics-matter-matterphysics.md) - This Matter Physics instance.

> Source: [src/physics/matter-js/MatterPhysics.js#L1202](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/MatterPhysics.js#L1202)  
> Since: 3.22.0

---

## applyForce

### <instance> applyForce(bodies, force)

**Description:**

Applies a force to a body, at the bodies current position, including resulting torque.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| bodies | [Phaser.Types.Physics.Matter.MatterBody](../typedef/types-physics-matter.md) | Array.<[Phaser.Types.Physics.Matter.MatterBody](../typedef/types-physics-matter.md)> | No | Either a single Body, or an array of bodies to update. If falsey it will use all bodies in the world. |
| --- | --- | --- | --- |
| force | [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) | No | A Vector that specifies the force to apply. |

**Returns:** [Phaser.Physics.Matter.MatterPhysics](physics-matter-matterphysics.md) - This Matter Physics instance.

> Source: [src/physics/matter-js/MatterPhysics.js#L1067](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/MatterPhysics.js#L1067)  
> Since: 3.22.0

---

## applyForceFromAngle

### <instance> applyForceFromAngle(bodies, speed, [angle])

**Description:**

Apply a force to a body based on the given angle and speed.

If no angle is given, the current body angle is used.

Use very small speed values, such as 0.1, depending on the mass and required velocity.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| bodies | [Phaser.Types.Physics.Matter.MatterBody](../typedef/types-physics-matter.md) | Array.<[Phaser.Types.Physics.Matter.MatterBody](../typedef/types-physics-matter.md)> | No | Either a single Body, or an array of bodies to update. If falsey it will use all bodies in the world. |
| --- | --- | --- | --- |
| speed | number | No | A speed value to be applied to a directional force. |
| angle | number | Yes | The angle, in radians, to apply the force from. Leave undefined to use the current body angle. |

**Returns:** [Phaser.Physics.Matter.MatterPhysics](physics-matter-matterphysics.md) - This Matter Physics instance.

> Source: [src/physics/matter-js/MatterPhysics.js#L1133](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/MatterPhysics.js#L1133)  
> Since: 3.22.0

---

## applyForceFromPosition

### <instance> applyForceFromPosition(bodies, position, speed, [angle])

**Description:**

Applies a force to a body, from the given world position, including resulting torque.

If no angle is given, the current body angle is used.

Use very small speed values, such as 0.1, depending on the mass and required velocity.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| bodies | [Phaser.Types.Physics.Matter.MatterBody](../typedef/types-physics-matter.md) | Array.<[Phaser.Types.Physics.Matter.MatterBody](../typedef/types-physics-matter.md)> | No | Either a single Body, or an array of bodies to update. If falsey it will use all bodies in the world. |
| --- | --- | --- | --- |
| position | [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) | No | A Vector that specifies the world-space position to apply the force at. |
| speed | number | No | A speed value to be applied to a directional force. |
| angle | number | Yes | The angle, in radians, to apply the force from. Leave undefined to use the current body angle. |

**Returns:** [Phaser.Physics.Matter.MatterPhysics](physics-matter-matterphysics.md) - This Matter Physics instance.

> Source: [src/physics/matter-js/MatterPhysics.js#L1095](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/MatterPhysics.js#L1095)  
> Since: 3.22.0

---

## containsPoint

### <instance> containsPoint(body, x, y)

**Description:**

Checks if the vertices of the given body, or an array of bodies, contains the given point, or not.

You can pass in either a single body, or an array of bodies to be checked. This method will

return `true` if *any* of the bodies in the array contain the point. See the `intersectPoint` method if you need

to get a list of intersecting bodies.

The point should be transformed into the Matter World coordinate system in advance. This happens by

default with Input Pointers, but if you wish to use points from another system you may need to

transform them before passing them.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| body | [Phaser.Types.Physics.Matter.MatterBody](../typedef/types-physics-matter.md) | Array.<[Phaser.Types.Physics.Matter.MatterBody](../typedef/types-physics-matter.md)> | No | The body, or an array of bodies, to check against the point. |
| --- | --- | --- | --- |
| x | number | No | The horizontal coordinate of the point. |
| y | number | No | The vertical coordinate of the point. |

**Returns:** boolean - `true` if the point is within one of the bodies given, otherwise `false`.

> Source: [src/physics/matter-js/MatterPhysics.js#L555](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/MatterPhysics.js#L555)  
> Since: 3.22.0

---

## getConfig

### <instance> getConfig()

**Description:**

This internal method is called when this class starts and retrieves the final Matter World Config.

**Returns:** [Phaser.Types.Physics.Matter.MatterWorldConfig](../typedef/types-physics-matter.md) - The Matter World Config.

> Source: [src/physics/matter-js/MatterPhysics.js#L439](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/MatterPhysics.js#L439)  
> Since: 3.0.0

---

## getConstraintLength

### <instance> getConstraintLength(constraint)

**Description:**

Returns the length of the given constraint, which is the distance between the two points.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| constraint | MatterJS.ConstraintType | No | The constraint to get the length from. |
| --- | --- | --- | --- |

**Returns:** number - The length of the constraint.

> Source: [src/physics/matter-js/MatterPhysics.js#L1170](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/MatterPhysics.js#L1170)  
> Since: 3.22.0

---

## getMatterBodies

### <instance> getMatterBodies([bodies])

**Description:**

Takes an array and returns a new array made from all of the Matter Bodies found in the original array.

For example, passing in Matter Game Objects, such as a bunch of Matter Sprites, to this method, would

return an array containing all of their native Matter Body objects.

If the `bodies` argument is falsey, it will return all bodies in the world.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| bodies | array | Yes | An array of objects to extract the bodies from. If falsey, it will return all bodies in the world. |
| --- | --- | --- | --- |

**Returns:** Array.<MatterJS.BodyType> - An array of native Matter Body objects.

> Source: [src/physics/matter-js/MatterPhysics.js#L917](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/MatterPhysics.js#L917)  
> Since: 3.22.0

---

## intersectBody

### <instance> intersectBody(body, [bodies])

**Description:**

Checks the given Matter Body to see if it intersects with any of the given bodies.

If no bodies are provided it will check against all bodies in the Matter World.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| body | [Phaser.Types.Physics.Matter.MatterBody](../typedef/types-physics-matter.md) | No | The target body. |
| --- | --- | --- | --- |
| bodies | Array.<[Phaser.Types.Physics.Matter.MatterBody](../typedef/types-physics-matter.md)> | Yes | An array of bodies to check the target body against. If not provided it will search all bodies in the world. |

**Returns:** Array.<[Phaser.Types.Physics.Matter.MatterBody](../typedef/types-physics-matter.md)> - An array of bodies whos vertices intersect with target body.

> Source: [src/physics/matter-js/MatterPhysics.js#L706](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/MatterPhysics.js#L706)  
> Since: 3.22.0

---

## intersectPoint

### <instance> intersectPoint(x, y, [bodies])

**Description:**

Checks the given coordinates to see if any vertices of the given bodies contain it.

If no bodies are provided it will search all bodies in the Matter World, including within Composites.

The coordinates should be transformed into the Matter World coordinate system in advance. This happens by

default with Input Pointers, but if you wish to use coordinates from another system you may need to

transform them before passing them.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The horizontal coordinate of the point. |
| --- | --- | --- | --- |
| y | number | No | The vertical coordinate of the point. |
| bodies | Array.<[Phaser.Types.Physics.Matter.MatterBody](../typedef/types-physics-matter.md)> | Yes | An array of bodies to check. If not provided it will search all bodies in the world. |

**Returns:** Array.<[Phaser.Types.Physics.Matter.MatterBody](../typedef/types-physics-matter.md)> - An array of bodies which contain the given point.

> Source: [src/physics/matter-js/MatterPhysics.js#L586](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/MatterPhysics.js#L586)  
> Since: 3.22.0

---

## intersectRay

### <instance> intersectRay(x1, y1, x2, y2, [rayWidth], [bodies])

**Description:**

Checks the given ray segment to see if any vertices of the given bodies intersect with it.

If no bodies are provided it will search all bodies in the Matter World.

The width of the ray can be specified via the `rayWidth` parameter.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x1 | number | No |  | The horizontal coordinate of the start of the ray segment. |
| --- | --- | --- | --- | --- |
| y1 | number | No |  | The vertical coordinate of the start of the ray segment. |
| x2 | number | No |  | The horizontal coordinate of the end of the ray segment. |
| y2 | number | No |  | The vertical coordinate of the end of the ray segment. |
| rayWidth | number | Yes | 1 | The width of the ray segment. |
| bodies | Array.<[Phaser.Types.Physics.Matter.MatterBody](../typedef/types-physics-matter.md)> | Yes |  | An array of bodies to check. If not provided it will search all bodies in the world. |

**Returns:** Array.<[Phaser.Types.Physics.Matter.MatterBody](../typedef/types-physics-matter.md)> - An array of bodies whos vertices intersect with the ray segment.

> Source: [src/physics/matter-js/MatterPhysics.js#L670](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/MatterPhysics.js#L670)  
> Since: 3.22.0

---

## intersectRect

### <instance> intersectRect(x, y, width, height, [outside], [bodies])

**Description:**

Checks the given rectangular area to see if any vertices of the given bodies intersect with it.

Or, if the `outside` parameter is set to `true`, it checks to see which bodies do not

intersect with it.

If no bodies are provided it will search all bodies in the Matter World, including within Composites.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | No |  | The horizontal coordinate of the top-left of the area. |
| --- | --- | --- | --- | --- |
| y | number | No |  | The vertical coordinate of the top-left of the area. |
| width | number | No |  | The width of the area. |
| height | number | No |  | The height of the area. |
| outside | boolean | Yes | false | If `false` it checks for vertices inside the area, if `true` it checks for vertices outside the area. |
| bodies | Array.<[Phaser.Types.Physics.Matter.MatterBody](../typedef/types-physics-matter.md)> | Yes |  | An array of bodies to check. If not provided it will search all bodies in the world. |

**Returns:** Array.<[Phaser.Types.Physics.Matter.MatterBody](../typedef/types-physics-matter.md)> - An array of bodies that intersect with the given area.

> Source: [src/physics/matter-js/MatterPhysics.js#L625](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/MatterPhysics.js#L625)  
> Since: 3.22.0

---

## overlap

### <instance> overlap(target, [bodies], [overlapCallback], [processCallback], [callbackContext])

**Description:**

Checks to see if the target body, or an array of target bodies, intersects with any of the given bodies.

If intersection occurs this method will return `true` and, if provided, invoke the callbacks.

If no bodies are provided for the second parameter the target will check against all bodies in the Matter World.

**Note that bodies can only overlap if they are in non-colliding collision groups or categories.**

If you provide a `processCallback` then the two bodies that overlap are sent to it. This callback

must return a boolean and is used to allow you to perform additional processing tests before a final

outcome is decided. If it returns `true` then the bodies are finally passed to the `overlapCallback`, if set.

If you provide an `overlapCallback` then the matching pairs of overlapping bodies will be sent to it.

Both callbacks have the following signature: `function (bodyA, bodyB, collisionInfo)` where `bodyA` is always

the target body. The `collisionInfo` object contains additional data, such as the angle and depth of penetration.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| target | [Phaser.Types.Physics.Matter.MatterBody](../typedef/types-physics-matter.md) | Array.<[Phaser.Types.Physics.Matter.MatterBody](../typedef/types-physics-matter.md)> | No | The target body, or array of target bodies, to check. |
| --- | --- | --- | --- |
| bodies | Array.<[Phaser.Types.Physics.Matter.MatterBody](../typedef/types-physics-matter.md)> | Yes | The second body, or array of bodies, to check. If falsey it will check against all bodies in the world. |
| overlapCallback | [Phaser.Types.Physics.Arcade.ArcadePhysicsCallback](../typedef/types-physics-arcade.md) | Yes | An optional callback function that is called if the bodies overlap. |
| processCallback | [Phaser.Types.Physics.Arcade.ArcadePhysicsCallback](../typedef/types-physics-arcade.md) | Yes | An optional callback function that lets you perform additional checks against the two bodies if they overlap. If this is set then `overlapCallback` will only be invoked if this callback returns `true`. |
| callbackContext | \* | Yes | The context, or scope, in which to run the callbacks. |

**Returns:** boolean - `true` if the target body intersects with *any* of the bodies given, otherwise `false`.

> Source: [src/physics/matter-js/MatterPhysics.js#L743](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/MatterPhysics.js#L743)  
> Since: 3.22.0

---

## pause

### <instance> pause()

**Description:**

Pauses the Matter World instance and sets `enabled` to `false`.

A paused world will not run any simulations for the duration it is paused.

**Returns:** [Phaser.Physics.Matter.World](physics-matter-world.md) - The Matter World object.

**Fires:** [Phaser.Physics.Matter.Events#event:PAUSE](../event/physics-matter-events.md)

> Source: [src/physics/matter-js/MatterPhysics.js#L460](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/MatterPhysics.js#L460)  
> Since: 3.0.0

---

## resume

### <instance> resume()

**Description:**

Resumes this Matter World instance from a paused state and sets `enabled` to `true`.

**Returns:** [Phaser.Physics.Matter.World](physics-matter-world.md) - The Matter World object.

> Source: [src/physics/matter-js/MatterPhysics.js#L476](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/MatterPhysics.js#L476)  
> Since: 3.0.0

---

## set30Hz

### <instance> set30Hz()

**Description:**

Sets the Matter Engine to run at fixed timestep of 30Hz and enables `autoUpdate`.

If you have set a custom `getDelta` function then this will override it.

**Returns:** [Phaser.Physics.Matter.MatterPhysics](physics-matter-matterphysics.md) - This Matter Physics instance.

> Source: [src/physics/matter-js/MatterPhysics.js#L506](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/MatterPhysics.js#L506)  
> Since: 3.4.0

---

## set60Hz

### <instance> set60Hz()

**Description:**

Sets the Matter Engine to run at fixed timestep of 60Hz and enables `autoUpdate`.

If you have set a custom `getDelta` function then this will override it.

**Returns:** [Phaser.Physics.Matter.MatterPhysics](physics-matter-matterphysics.md) - This Matter Physics instance.

> Source: [src/physics/matter-js/MatterPhysics.js#L489](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/MatterPhysics.js#L489)  
> Since: 3.4.0

---

## setAngularVelocity

### <instance> setAngularVelocity(bodies, value)

**Description:**

Sets the angular velocity of the bodies instantly.

Position, angle, force etc. are unchanged.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| bodies | [Phaser.Types.Physics.Matter.MatterBody](../typedef/types-physics-matter.md) | Array.<[Phaser.Types.Physics.Matter.MatterBody](../typedef/types-physics-matter.md)> | No | Either a single Body, or an array of bodies to update. If falsey it will use all bodies in the world. |
| --- | --- | --- | --- |
| value | number | No | The angular velocity. |

**Returns:** [Phaser.Physics.Matter.MatterPhysics](physics-matter-matterphysics.md) - This Matter Physics instance.

> Source: [src/physics/matter-js/MatterPhysics.js#L1043](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/MatterPhysics.js#L1043)  
> Since: 3.22.0

---

## setCollidesWith

### <instance> setCollidesWith(bodies, categories)

**Description:**

Sets the collision filter mask of all given Matter Bodies to the given value.

Two Matter Bodies with different collision groups will only collide if each one includes the others

category in its mask based on a bitwise AND operation: `(categoryA & maskB) !== 0` and

`(categoryB & maskA) !== 0` are both true.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| bodies | Array.<[Phaser.Types.Physics.Matter.MatterBody](../typedef/types-physics-matter.md)> | No | An array of bodies to update. If falsey it will use all bodies in the world. |
| --- | --- | --- | --- |
| categories | number | Array.<number> | No | A unique category bitfield, or an array of them. |

**Returns:** [Phaser.Physics.Matter.MatterPhysics](physics-matter-matterphysics.md) - This Matter Physics instance.

> Source: [src/physics/matter-js/MatterPhysics.js#L876](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/MatterPhysics.js#L876)  
> Since: 3.22.0

---

## setCollisionCategory

### <instance> setCollisionCategory(bodies, value)

**Description:**

Sets the collision filter category of all given Matter Bodies to the given value.

This number must be a power of two between 2^0 (= 1) and 2^31.

Bodies with different collision groups (see <#setCollisionGroup>) will only collide if their collision

categories are included in their collision masks (see <#setCollidesWith>).

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| bodies | Array.<[Phaser.Types.Physics.Matter.MatterBody](../typedef/types-physics-matter.md)> | No | An array of bodies to update. If falsey it will use all bodies in the world. |
| --- | --- | --- | --- |
| value | number | No | Unique category bitfield. |

**Returns:** [Phaser.Physics.Matter.MatterPhysics](physics-matter-matterphysics.md) - This Matter Physics instance.

> Source: [src/physics/matter-js/MatterPhysics.js#L819](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/MatterPhysics.js#L819)  
> Since: 3.22.0

---

## setCollisionGroup

### <instance> setCollisionGroup(bodies, value)

**Description:**

Sets the collision filter group of all given Matter Bodies to the given value.

If the group value is zero, or if two Matter Bodies have different group values,

they will collide according to the usual collision filter rules (see <#setCollisionCategory> and <#setCollisionGroup>).

If two Matter Bodies have the same positive group value, they will always collide;

if they have the same negative group value they will never collide.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| bodies | Array.<[Phaser.Types.Physics.Matter.MatterBody](../typedef/types-physics-matter.md)> | No | An array of bodies to update. If falsey it will use all bodies in the world. |
| --- | --- | --- | --- |
| value | number | No | Unique group index. |

**Returns:** [Phaser.Physics.Matter.MatterPhysics](physics-matter-matterphysics.md) - This Matter Physics instance.

> Source: [src/physics/matter-js/MatterPhysics.js#L847](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/MatterPhysics.js#L847)  
> Since: 3.22.0

---

## setVelocity

### <instance> setVelocity(bodies, x, y)

**Description:**

Sets both the horizontal and vertical linear velocity of the physics bodies.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| bodies | [Phaser.Types.Physics.Matter.MatterBody](../typedef/types-physics-matter.md) | Array.<[Phaser.Types.Physics.Matter.MatterBody](../typedef/types-physics-matter.md)> | No | Either a single Body, or an array of bodies to update. If falsey it will use all bodies in the world. |
| --- | --- | --- | --- |
| x | number | No | The horizontal linear velocity value. |
| y | number | No | The vertical linear velocity value. |

**Returns:** [Phaser.Physics.Matter.MatterPhysics](physics-matter-matterphysics.md) - This Matter Physics instance.

> Source: [src/physics/matter-js/MatterPhysics.js#L956](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/MatterPhysics.js#L956)  
> Since: 3.22.0

---

## setVelocityX

### <instance> setVelocityX(bodies, x)

**Description:**

Sets just the horizontal linear velocity of the physics bodies.

The vertical velocity of the body is unchanged.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| bodies | [Phaser.Types.Physics.Matter.MatterBody](../typedef/types-physics-matter.md) | Array.<[Phaser.Types.Physics.Matter.MatterBody](../typedef/types-physics-matter.md)> | No | Either a single Body, or an array of bodies to update. If falsey it will use all bodies in the world. |
| --- | --- | --- | --- |
| x | number | No | The horizontal linear velocity value. |

**Returns:** [Phaser.Physics.Matter.MatterPhysics](physics-matter-matterphysics.md) - This Matter Physics instance.

> Source: [src/physics/matter-js/MatterPhysics.js#L985](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/MatterPhysics.js#L985)  
> Since: 3.22.0

---

## setVelocityY

### <instance> setVelocityY(bodies, y)

**Description:**

Sets just the vertical linear velocity of the physics bodies.

The horizontal velocity of the body is unchanged.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| bodies | [Phaser.Types.Physics.Matter.MatterBody](../typedef/types-physics-matter.md) | Array.<[Phaser.Types.Physics.Matter.MatterBody](../typedef/types-physics-matter.md)> | No | Either a single Body, or an array of bodies to update. If falsey it will use all bodies in the world. |
| --- | --- | --- | --- |
| y | number | No | The vertical linear velocity value. |

**Returns:** [Phaser.Physics.Matter.MatterPhysics](physics-matter-matterphysics.md) - This Matter Physics instance.

> Source: [src/physics/matter-js/MatterPhysics.js#L1014](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/MatterPhysics.js#L1014)  
> Since: 3.22.0

---

## step

### <instance> step([delta], [correction])

**Description:**

Manually advances the physics simulation by one iteration.

You can optionally pass in the `delta` and `correction` values to be used by Engine.update.

If undefined they use the Matter defaults of 60Hz and no correction.

Calling `step` directly bypasses any checks of `enabled` or `autoUpdate`.

It also ignores any custom `getDelta` functions, as you should be passing the delta

value in to this call.

You can adjust the number of iterations that Engine.update performs internally.

Use the Scene Matter Physics config object to set the following properties:

positionIterations (defaults to 6)

velocityIterations (defaults to 4)

constraintIterations (defaults to 2)

Adjusting these values can help performance in certain situations, depending on the physics requirements

of your game.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| delta | number | Yes | 16.666 | The delta value. |
| --- | --- | --- | --- | --- |
| correction | number | Yes | 1 | Optional delta correction value. |

> Source: [src/physics/matter-js/MatterPhysics.js#L523](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/MatterPhysics.js#L523)  
> Since: 3.4.0

---

# Private Methods

## boot

### <instance> boot()

**Description:**

This method is called automatically, only once, when the Scene is first created.

Do not invoke it directly.

**Access:** private

> Source: [src/physics/matter-js/MatterPhysics.js#L398](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/MatterPhysics.js#L398)  
> Since: 3.5.1

---

## destroy

### <instance> destroy()

**Description:**

The Scene that owns this plugin is being destroyed.

We need to shutdown and then kill off all external references.

**Access:** private

> Source: [src/physics/matter-js/MatterPhysics.js#L1324](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/MatterPhysics.js#L1324)  
> Since: 3.0.0

---

## shutdown

### <instance> shutdown()

**Description:**

The Scene that owns this plugin is shutting down.

We need to kill and reset all internal properties as well as stop listening to Scene events.

**Access:** private

> Source: [src/physics/matter-js/MatterPhysics.js#L1290](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/MatterPhysics.js#L1290)  
> Since: 3.0.0

---

## start

### <instance> start()

**Description:**

This method is called automatically by the Scene when it is starting up.

It is responsible for creating local systems, properties and listening for Scene events.

Do not invoke it directly.

**Access:** private

> Source: [src/physics/matter-js/MatterPhysics.js#L415](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/MatterPhysics.js#L415)  
> Since: 3.5.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [add](#add)

    - [add: Phaser.Physics.Matter.Factory](#add-phaserphysicsmatterfactory)
  + [axes](#axes)

    - [axes: MatterJS.AxesFactory](#axes-matterjsaxesfactory)
  + [bodies](#bodies)

    - [bodies: MatterJS.BodiesFactory](#bodies-matterjsbodiesfactory)
  + [body](#body)

    - [body: MatterJS.BodyFactory](#body-matterjsbodyfactory)
  + [bodyBounds](#bodybounds)

    - [bodyBounds: Phaser.Physics.Matter.BodyBounds](#bodybounds-phaserphysicsmatterbodybounds)
  + [bounds](#bounds)

    - [bounds: MatterJS.BoundsFactory](#bounds-matterjsboundsfactory)
  + [collision](#collision)

    - [collision: MatterJS.Collision](#collision-matterjscollision)
  + [composite](#composite)

    - [composite: MatterJS.CompositeFactory](#composite-matterjscompositefactory)
  + [composites](#composites)

    - [composites: MatterJS.CompositesFactory](#composites-matterjscompositesfactory)
  + [config](#config)

    - [config: Phaser.Types.Physics.Matter.MatterWorldConfig](#config-phasertypesphysicsmattermatterworldconfig)
  + [constraint](#constraint)

    - [constraint: MatterJS.ConstraintFactory](#constraint-matterjsconstraintfactory)
  + [detector](#detector)

    - [detector: MatterJS.DetectorFactory](#detector-matterjsdetectorfactory)
  + [pair](#pair)

    - [pair: MatterJS.PairFactory](#pair-matterjspairfactory)
  + [pairs](#pairs)

    - [pairs: MatterJS.PairsFactory](#pairs-matterjspairsfactory)
  + [query](#query)

    - [query: MatterJS.QueryFactory](#query-matterjsqueryfactory)
  + [resolver](#resolver)

    - [resolver: MatterJS.ResolverFactory](#resolver-matterjsresolverfactory)
  + [scene](#scene)

    - [scene: Phaser.Scene](#scene-phaserscene)
  + [svg](#svg)

    - [svg: MatterJS.SvgFactory](#svg-matterjssvgfactory)
  + [systems](#systems)

    - [systems: Phaser.Scenes.Systems](#systems-phaserscenessystems)
  + [vector](#vector)

    - [vector: MatterJS.VectorFactory](#vector-matterjsvectorfactory)
  + [vertices](#vertices)

    - [vertices: MatterJS.VerticesFactory](#vertices-matterjsverticesfactory)
  + [verts](#verts)

    - [verts: MatterJS.VerticesFactory](#verts-matterjsverticesfactory)
  + [world](#world)

    - [world: Phaser.Physics.Matter.World](#world-phaserphysicsmatterworld)
* [Private Members](#private-members)

  + [\_tempVec2](#_tempvec2)

    - [\_tempVec2: MatterJS.Vector](#_tempvec2-matterjsvector)
* [Public Methods](#public-methods)

  + [alignBody](#alignbody)

    - [<instance> alignBody(body, x, y, align)](#instance-alignbodybody-x-y-align)
  + [applyForce](#applyforce)

    - [<instance> applyForce(bodies, force)](#instance-applyforcebodies-force)
  + [applyForceFromAngle](#applyforcefromangle)

    - [<instance> applyForceFromAngle(bodies, speed, [angle])](#instance-applyforcefromanglebodies-speed-angle)
  + [applyForceFromPosition](#applyforcefromposition)

    - [<instance> applyForceFromPosition(bodies, position, speed, [angle])](#instance-applyforcefrompositionbodies-position-speed-angle)
  + [containsPoint](#containspoint)

    - [<instance> containsPoint(body, x, y)](#instance-containspointbody-x-y)
  + [getConfig](#getconfig)

    - [<instance> getConfig()](#instance-getconfig)
  + [getConstraintLength](#getconstraintlength)

    - [<instance> getConstraintLength(constraint)](#instance-getconstraintlengthconstraint)
  + [getMatterBodies](#getmatterbodies)

    - [<instance> getMatterBodies([bodies])](#instance-getmatterbodiesbodies)
  + [intersectBody](#intersectbody)

    - [<instance> intersectBody(body, [bodies])](#instance-intersectbodybody-bodies)
  + [intersectPoint](#intersectpoint)

    - [<instance> intersectPoint(x, y, [bodies])](#instance-intersectpointx-y-bodies)
  + [intersectRay](#intersectray)

    - [<instance> intersectRay(x1, y1, x2, y2, [rayWidth], [bodies])](#instance-intersectrayx1-y1-x2-y2-raywidth-bodies)
  + [intersectRect](#intersectrect)

    - [<instance> intersectRect(x, y, width, height, [outside], [bodies])](#instance-intersectrectx-y-width-height-outside-bodies)
  + [overlap](#overlap)

    - [<instance> overlap(target, [bodies], [overlapCallback], [processCallback], [callbackContext])](#instance-overlaptarget-bodies-overlapcallback-processcallback-callbackcontext)
  + [pause](#pause)

    - [<instance> pause()](#instance-pause)
  + [resume](#resume)

    - [<instance> resume()](#instance-resume)
  + [set30Hz](#set30hz)

    - [<instance> set30Hz()](#instance-set30hz)
  + [set60Hz](#set60hz)

    - [<instance> set60Hz()](#instance-set60hz)
  + [setAngularVelocity](#setangularvelocity)

    - [<instance> setAngularVelocity(bodies, value)](#instance-setangularvelocitybodies-value)
  + [setCollidesWith](#setcollideswith)

    - [<instance> setCollidesWith(bodies, categories)](#instance-setcollideswithbodies-categories)
  + [setCollisionCategory](#setcollisioncategory)

    - [<instance> setCollisionCategory(bodies, value)](#instance-setcollisioncategorybodies-value)
  + [setCollisionGroup](#setcollisiongroup)

    - [<instance> setCollisionGroup(bodies, value)](#instance-setcollisiongroupbodies-value)
  + [setVelocity](#setvelocity)

    - [<instance> setVelocity(bodies, x, y)](#instance-setvelocitybodies-x-y)
  + [setVelocityX](#setvelocityx)

    - [<instance> setVelocityX(bodies, x)](#instance-setvelocityxbodies-x)
  + [setVelocityY](#setvelocityy)

    - [<instance> setVelocityY(bodies, y)](#instance-setvelocityybodies-y)
  + [step](#step)

    - [<instance> step([delta], [correction])](#instance-stepdelta-correction)
* [Private Methods](#private-methods)

  + [boot](#boot)

    - [<instance> boot()](#instance-boot)
  + [destroy](#destroy)

    - [<instance> destroy()](#instance-destroy)
  + [shutdown](#shutdown)

    - [<instance> shutdown()](#instance-shutdown)
  + [start](#start)

    - [<instance> start()](#instance-start)

Back to top

©2025[Phaser](https://docs.phaser.io)