# Types.Physics.Matter

Phaser.Types.Physics.Matter

## MatterBody

### <static> MatterBody

**Type**: MatterJS.BodyType | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | [Phaser.Physics.Matter.Image](../class/physics-matter-image.md) | [Phaser.Physics.Matter.Sprite](../class/physics-matter-sprite.md) | [Phaser.Physics.Matter.TileBody](../class/physics-matter-tilebody.md)

**Member of**: Phaser.Types.Physics.Matter

> Source: [src/physics/matter-js/typedefs/MatterBody.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/typedefs/MatterBody.js#L1)  
> Since: 3.22.0

---

## MatterBodyConfig

### <static> MatterBodyConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| label | string | Yes | "'Body'" | An arbitrary string-based name to help identify this body. |
| --- | --- | --- | --- | --- |
| shape | string | [Phaser.Types.Physics.Matter.MatterSetBodyConfig](types-physics-matter.md) | Yes | null | Set this Game Object to create and use a new Body based on the configuration object given. |
| parts | Array.<MatterJS.BodyType> | Yes |  | An array of bodies that make up this body. The first body in the array must always be a self reference to the current body instance. All bodies in the `parts` array together form a single rigid compound body. |
| plugin | any | Yes |  | An object reserved for storing plugin-specific properties. |
| wrapBounds | any | Yes |  | An object for storing wrap boundaries. |
| angle | number | Yes | 0 | A number specifying the angle of the body, in radians. |
| vertices | Array.<[Phaser.Types.Math.Vector2Like](types-math.md)> | Yes | null | An array of `Vector` objects that specify the convex hull of the rigid body. These should be provided about the origin `(0, 0)`. |
| position | [Phaser.Types.Math.Vector2Like](types-math.md) | Yes |  | A `Vector` that specifies the current world-space position of the body. |
| force | [Phaser.Types.Math.Vector2Like](types-math.md) | Yes |  | A `Vector` that specifies the force to apply in the current step. It is zeroed after every `Body.update`. See also `Body.applyForce`. |
| torque | number | Yes | 0 | A `Number` that specifies the torque (turning force) to apply in the current step. It is zeroed after every `Body.update`. |
| isSensor | boolean | Yes | false | A flag that indicates whether a body is a sensor. Sensor triggers collision events, but doesn't react with colliding body physically. |
| isStatic | boolean | Yes | false | A flag that indicates whether a body is considered static. A static body can never change position or angle and is completely fixed. |
| sleepThreshold | number | Yes | 60 | A `Number` that defines the number of updates in which this body must have near-zero velocity before it is set as sleeping by the `Matter.Sleeping` module (if sleeping is enabled by the engine). |
| density | number | Yes | 0.001 | A `Number` that defines the density of the body, that is its mass per unit area. If you pass the density via `Body.create` the `mass` property is automatically calculated for you based on the size (area) of the object. This is generally preferable to simply setting mass and allows for more intuitive definition of materials (e.g. rock has a higher density than wood). |
| restitution | number | Yes | 0 | A `Number` that defines the restitution (elasticity) of the body. The value is always positive and is in the range `(0, 1)`. |
| friction | number | Yes | 0.1 | A `Number` that defines the friction of the body. The value is always positive and is in the range `(0, 1)`. A value of `0` means that the body may slide indefinitely. A value of `1` means the body may come to a stop almost instantly after a force is applied. |
| frictionStatic | number | Yes | 0.5 | A `Number` that defines the static friction of the body (in the Coulomb friction model). A value of `0` means the body will never 'stick' when it is nearly stationary and only dynamic `friction` is used. The higher the value (e.g. `10`), the more force it will take to initially get the body moving when nearly stationary. This value is multiplied with the `friction` property to make it easier to change `friction` and maintain an appropriate amount of static friction. |
| frictionAir | number | Yes | 0.01 | A `Number` that defines the air friction of the body (air resistance). A value of `0` means the body will never slow as it moves through space. The higher the value, the faster a body slows when moving through space. |
| collisionFilter | [Phaser.Types.Physics.Matter.MatterCollisionFilter](types-physics-matter.md) | Yes |  | An `Object` that specifies the collision filtering properties of this body. |
| slop | number | Yes | 0.05 | A `Number` that specifies a tolerance on how far a body is allowed to 'sink' or rotate into other bodies. Avoid changing this value unless you understand the purpose of `slop` in physics engines. The default should generally suffice, although very large bodies may require larger values for stable stacking. |
| timeScale | number | Yes | 1 | A `Number` that allows per-body time scaling, e.g. a force-field where bodies inside are in slow-motion, while others are at full speed. |
| chamfer | number | Array.<number> | [Phaser.Types.Physics.Matter.MatterChamferConfig](types-physics-matter.md) | Yes | null |
| circleRadius | number | Yes | 0 | The radius of this body if a circle. |
| mass | number | Yes | 0 | A `Number` that defines the mass of the body, although it may be more appropriate to specify the `density` property instead. If you modify this value, you must also modify the `body.inverseMass` property (`1 / mass`). |
| inverseMass | number | Yes | 0 | A `Number` that defines the inverse mass of the body (`1 / mass`). If you modify this value, you must also modify the `body.mass` property. |
| scale | [Phaser.Types.Math.Vector2Like](types-math.md) | Yes |  | A `Vector` that specifies the initial scale of the body. |
| gravityScale | [Phaser.Types.Math.Vector2Like](types-math.md) | Yes |  | A `Vector` that scales the influence of World gravity when applied to this body. |
| ignoreGravity | boolean | Yes | false | A boolean that toggles if this body should ignore world gravity or not. |
| ignorePointer | boolean | Yes | false | A boolean that toggles if this body should ignore pointer / mouse constraints or not. |
| render | [Phaser.Types.Physics.Matter.MatterBodyRenderConfig](types-physics-matter.md) | Yes |  | The Debug Render configuration object for this body. |
| onCollideCallback | function | Yes |  | A callback that is invoked when this Body starts colliding with any other Body. You can register callbacks by providing a function of type `( pair: Matter.Pair) => void`. |
| onCollideEndCallback | function | Yes |  | A callback that is invoked when this Body stops colliding with any other Body. You can register callbacks by providing a function of type `( pair: Matter.Pair) => void`. |
| onCollideActiveCallback | function | Yes |  | A callback that is invoked for the duration that this Body is colliding with any other Body. You can register callbacks by providing a function of type `( pair: Matter.Pair) => void`. |
| onCollideWith | any | Yes |  | A collision callback dictionary used by the `Body.setOnCollideWith` function. |

**Type**: object

**Member of**: Phaser.Types.Physics.Matter

> Source: [src/physics/matter-js/typedefs/MatterBodyConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/typedefs/MatterBodyConfig.js#L1)  
> Since: 3.22.0

---

## MatterBodyRenderConfig

### <static> MatterBodyRenderConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| visible | boolean | Yes | true | Should this body be rendered by the Debug Renderer? |
| --- | --- | --- | --- | --- |
| opacity | number | Yes | 1 | The opacity of the body and all parts within it. |
| fillColor | number | Yes |  | The color value of the fill when rendering this body. |
| fillOpacity | number | Yes |  | The opacity of the fill when rendering this body, a value between 0 and 1. |
| lineColor | number | Yes |  | The color value of the line stroke when rendering this body. |
| lineOpacity | number | Yes |  | The opacity of the line when rendering this body, a value between 0 and 1. |
| lineThickness | number | Yes |  | If rendering lines, the thickness of the line. |
| sprite | object | Yes |  | Controls the offset between the body and the parent Game Object, if it has one. |
| sprite.xOffset | number | Yes | 0 | The horizontal offset between the body and the parent Game Object texture, if it has one. |
| sprite.yOffset | number | Yes | 0 | The vertical offset between the body and the parent Game Object texture, if it has one. |

**Type**: object

**Member of**: Phaser.Types.Physics.Matter

> Source: [src/physics/matter-js/typedefs/MatterBodyRenderConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/typedefs/MatterBodyRenderConfig.js#L1)  
> Since: 3.22.0

---

## MatterBodyTileOptions

### <static> MatterBodyTileOptions

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| isStatic | boolean | Yes | true | Whether or not the newly created body should be made static. This defaults to true since typically tiles should not be moved. |
| --- | --- | --- | --- | --- |
| addToWorld | boolean | Yes | true | Whether or not to add the newly created body (or existing body if options.body is used) to the Matter world. |

**Type**: object

**Member of**: Phaser.Types.Physics.Matter

> Source: [src/physics/matter-js/typedefs/MatterBodyTileOptions.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/typedefs/MatterBodyTileOptions.js#L1)  
> Since: 3.0.0

---

## MatterChamferConfig

### <static> MatterChamferConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| radius | number | Array.<number> | Yes | 8 | A single number, or an array, to specify the radius for each vertex. |
| --- | --- | --- | --- | --- |
| quality | number | Yes | -1 | The quality of the chamfering. -1 means 'auto'. |
| qualityMin | number | Yes | 2 | The minimum quality of the chamfering. The higher this value, the more vertices are created. |
| qualityMax | number | Yes | 14 | The maximum quality of the chamfering. The higher this value, the more vertices are created. |

**Type**: object

**Member of**: Phaser.Types.Physics.Matter

> Source: [src/physics/matter-js/typedefs/MatterChamferConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/typedefs/MatterChamferConfig.js#L1)  
> Since: 3.22.0

---

## MatterCollisionData

### <static> MatterCollisionData

| name | type | optional | description |
| --- | --- | --- | --- |
| collided | boolean | No | Have the pair collided or not? |
| --- | --- | --- | --- |
| bodyA | MatterJS.BodyType | No | A reference to the first body involved in the collision. |
| bodyB | MatterJS.BodyType | No | A reference to the second body involved in the collision. |
| axisBody | MatterJS.BodyType | No | A reference to the dominant axis body. |
| axisNumber | number | No | The index of the dominant collision axis vector (edge normal) |
| depth | number | No | The depth of the collision on the minimum overlap. |
| parentA | MatterJS.BodyType | No | A reference to the parent of Body A, or to Body A itself if it has no parent. |
| parentB | MatterJS.BodyType | No | A reference to the parent of Body B, or to Body B itself if it has no parent. |
| normal | MatterJS.Vector | No | The collision normal, facing away from Body A. |
| tangent | MatterJS.Vector | No | The tangent of the collision normal. |
| penetration | MatterJS.Vector | No | The penetration distances between the two bodies. |
| supports | Array.<MatterJS.Vector> | No | An array of support points, either exactly one or two points. |
| inverseMass | number | No | The resulting inverse mass from the collision. |
| friction | number | No | The resulting friction from the collision. |
| frictionStatic | number | No | The resulting static friction from the collision. |
| restitution | number | No | The resulting restitution from the collision. |
| slop | number | No | The resulting slop from the collision. |

**Type**: object

**Member of**: Phaser.Types.Physics.Matter

> Source: [src/physics/matter-js/typedefs/MatterCollisionData.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/typedefs/MatterCollisionData.js#L1)  
> Since: 3.22.0

---

## MatterCollisionFilter

### <static> MatterCollisionFilter

An `Object` that specifies the collision filtering properties of this body.

Collisions between two bodies will obey the following rules:

* If the two bodies have the same non-zero value of `collisionFilter.group`,

  they will always collide if the value is positive, and they will never collide

  if the value is negative.
* If the two bodies have different values of `collisionFilter.group` or if one

  (or both) of the bodies has a value of 0, then the category/mask rules apply as follows:

Each body belongs to a collision category, given by `collisionFilter.category`. This

value is used as a bit field and the category should have only one bit set, meaning that

the value of this property is a power of two in the range [1, 2^31]. Thus, there are 32

different collision categories available.

Each body also defines a collision bitmask, given by `collisionFilter.mask` which specifies

the categories it collides with (the value is the bitwise AND value of all these categories).

Using the category/mask rules, two bodies `A` and `B` collide if each includes the other's

category in its mask, i.e. `(categoryA & maskB) !== 0` and `(categoryB & maskA) !== 0`

are both true.

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| category | number | Yes | "0x0001" | A bit field that specifies the collision category this body belongs to. The category value should have only one bit set, for example `0x0001`. This means there are up to 32 unique collision categories available. |
| --- | --- | --- | --- | --- |
| mask | number | Yes | "0xFFFFFFFF" | A bit mask that specifies the collision categories this body may collide with. |
| group | number | Yes | 0 | An Integer `Number`, that specifies the collision group this body belongs to. |

**Type**: object

**Member of**: Phaser.Types.Physics.Matter

> Source: [src/physics/matter-js/typedefs/MatterCollisionFilter.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/typedefs/MatterCollisionFilter.js#L1)  
> Since: 3.22.0

---

## MatterCollisionPair

### <static> MatterCollisionPair

| name | type | optional | description |
| --- | --- | --- | --- |
| id | string | No | The unique auto-generated collision pair id. A combination of the body A and B IDs. |
| --- | --- | --- | --- |
| bodyA | MatterJS.BodyType | No | A reference to the first body involved in the collision. |
| bodyB | MatterJS.BodyType | No | A reference to the second body involved in the collision. |
| contacts | Array.<MatterJS.Vector> | No | An array containing all of the active contacts between bodies A and B. |
| separation | number | No | The amount of separation that occurred between bodies A and B. |
| isActive | boolean | No | Is the collision still active or not? |
| confirmedActive | boolean | No | Has Matter determined the collision are being active yet? |
| isSensor | boolean | No | Is either body A or B a sensor? |
| timeCreated | number | No | The timestamp when the collision pair was created. |
| timeUpdated | number | No | The timestamp when the collision pair was most recently updated. |
| collision | [Phaser.Types.Physics.Matter.MatterCollisionData](types-physics-matter.md) | No | The collision data object. |
| inverseMass | number | No | The resulting inverse mass from the collision. |
| friction | number | No | The resulting friction from the collision. |
| frictionStatic | number | No | The resulting static friction from the collision. |
| restitution | number | No | The resulting restitution from the collision. |
| slop | number | No | The resulting slop from the collision. |

**Type**: object

**Member of**: Phaser.Types.Physics.Matter

> Source: [src/physics/matter-js/typedefs/MatterCollisionPair.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/typedefs/MatterCollisionPair.js#L1)  
> Since: 3.22.0

---

## MatterConstraintConfig

### <static> MatterConstraintConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| label | string | Yes | "'Constraint'" | An arbitrary string-based name to help identify this constraint. |
| --- | --- | --- | --- | --- |
| bodyA | MatterJS.BodyType | Yes |  | The first possible `Body` that this constraint is attached to. |
| bodyB | MatterJS.BodyType | Yes |  | The second possible `Body` that this constraint is attached to. |
| pointA | [Phaser.Types.Math.Vector2Like](types-math.md) | Yes |  | A `Vector` that specifies the offset of the constraint from center of the `constraint.bodyA` if defined, otherwise a world-space position. |
| pointB | [Phaser.Types.Math.Vector2Like](types-math.md) | Yes |  | A `Vector` that specifies the offset of the constraint from center of the `constraint.bodyB` if defined, otherwise a world-space position. |
| stiffness | number | Yes | 1 | A `Number` that specifies the stiffness of the constraint, i.e. the rate at which it returns to its resting `constraint.length`. A value of `1` means the constraint should be very stiff. A value of `0.2` means the constraint acts like a soft spring. |
| angularStiffness | number | Yes | 0 | A `Number` that specifies the angular stiffness of the constraint. |
| angleA | number | Yes | 0 | The angleA of the constraint. If bodyA is set, the angle of bodyA is used instead. |
| angleB | number | Yes | 0 | The angleB of the constraint. If bodyB is set, the angle of bodyB is used instead. |
| damping | number | Yes | 0 | A `Number` that specifies the damping of the constraint, i.e. the amount of resistance applied to each body based on their velocities to limit the amount of oscillation. Damping will only be apparent when the constraint also has a very low `stiffness`. A value of `0.1` means the constraint will apply heavy damping, resulting in little to no oscillation. A value of `0` means the constraint will apply no damping. |
| length | number | Yes |  | A `Number` that specifies the target resting length of the constraint. It is calculated automatically in `Constraint.create` from initial positions of the `constraint.bodyA` and `constraint.bodyB`. |
| plugin | any | Yes |  | An object reserved for storing plugin-specific properties. |
| render | [Phaser.Types.Physics.Matter.MatterConstraintRenderConfig](types-physics-matter.md) | Yes |  | The Debug Render configuration object for this constraint. |

**Type**: object

**Member of**: Phaser.Types.Physics.Matter

> Source: [src/physics/matter-js/typedefs/MatterConstraintConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/typedefs/MatterConstraintConfig.js#L1)  
> Since: 3.22.0

---

## MatterConstraintRenderConfig

### <static> MatterConstraintRenderConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| visible | boolean | Yes | true | Should this constraint be rendered by the Debug Renderer? |
| --- | --- | --- | --- | --- |
| anchors | boolean | Yes | true | If this constraint has anchors, should they be rendered? Pin constraints never have anchors. |
| lineColor | number | Yes |  | The color value of the line stroke when rendering this constraint. |
| lineOpacity | number | Yes |  | The opacity of the line when rendering this constraint, a value between 0 and 1. |
| lineThickness | number | Yes |  | If rendering lines, the thickness of the line. |
| pinSize | number | Yes | 4 | The size of the circles drawn when rendering pin constraints. |
| anchorSize | number | Yes | 4 | The size of the circles drawn as the constraint anchors. |
| anchorColor | number | Yes | "0xefefef" | The color value of constraint anchors. |

**Type**: object

**Member of**: Phaser.Types.Physics.Matter

> Source: [src/physics/matter-js/typedefs/MatterConstraintRenderConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/typedefs/MatterConstraintRenderConfig.js#L1)  
> Since: 3.22.0

---

## MatterDebugConfig

### <static> MatterDebugConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| showAxes | boolean | Yes | false | Render all of the body axes? |
| --- | --- | --- | --- | --- |
| showAngleIndicator | boolean | Yes | false | Render just a single body axis? |
| angleColor | number | Yes | "0xe81153" | The color of the body angle / axes lines. |
| showBroadphase | boolean | Yes | false | Render the broadphase grid? |
| broadphaseColor | number | Yes | "0xffb400" | The color of the broadphase grid. |
| showBounds | boolean | Yes | false | Render the bounds of the bodies in the world? |
| boundsColor | number | Yes | "0xffffff" | The color of the body bounds. |
| showVelocity | boolean | Yes | false | Render the velocity of the bodies in the world? |
| velocityColor | number | Yes | "0x00aeef" | The color of the body velocity line. |
| showCollisions | boolean | Yes | false | Render the collision points and normals for colliding pairs. |
| collisionColor | number | Yes | "0xf5950c" | The color of the collision points. |
| showSeparation | boolean | Yes | false | Render lines showing the separation between bodies. |
| separationColor | number | Yes | "0xffa500" | The color of the body separation line. |
| showBody | boolean | Yes | true | Render the dynamic bodies in the world to the Graphics object? |
| showStaticBody | boolean | Yes | true | Render the static bodies in the world to the Graphics object? |
| showInternalEdges | boolean | Yes | false | When rendering bodies, render the internal edges as well? |
| renderFill | boolean | Yes | false | Render the bodies using a fill color. |
| renderLine | boolean | Yes | true | Render the bodies using a line stroke. |
| fillColor | number | Yes | "0x106909" | The color value of the fill when rendering dynamic bodies. |
| fillOpacity | number | Yes | 1 | The opacity of the fill when rendering dynamic bodies, a value between 0 and 1. |
| lineColor | number | Yes | "0x28de19" | The color value of the line stroke when rendering dynamic bodies. |
| lineOpacity | number | Yes | 1 | The opacity of the line when rendering dynamic bodies, a value between 0 and 1. |
| lineThickness | number | Yes | 1 | If rendering lines, the thickness of the line. |
| staticFillColor | number | Yes | "0x0d177b" | The color value of the fill when rendering static bodies. |
| staticLineColor | number | Yes | "0x1327e4" | The color value of the line stroke when rendering static bodies. |
| showSleeping | boolean | Yes | false | Render any sleeping bodies (dynamic or static) in the world to the Graphics object? |
| staticBodySleepOpacity | number | Yes | 0.7 | The amount to multiply the opacity of sleeping static bodies by. |
| sleepFillColor | number | Yes | "0x464646" | The color value of the fill when rendering sleeping dynamic bodies. |
| sleepLineColor | number | Yes | "0x999a99" | The color value of the line stroke when rendering sleeping dynamic bodies. |
| showSensors | boolean | Yes | true | Render bodies or body parts that are flagged as being a sensor? |
| sensorFillColor | number | Yes | "0x0d177b" | The fill color when rendering body sensors. |
| sensorLineColor | number | Yes | "0x1327e4" | The line color when rendering body sensors. |
| showPositions | boolean | Yes | true | Render the position of non-static bodies? |
| positionSize | number | Yes | 4 | The size of the rectangle drawn when rendering the body position. |
| positionColor | number | Yes | "0xe042da" | The color value of the rectangle drawn when rendering the body position. |
| showJoint | boolean | Yes | true | Render all world constraints to the Graphics object? |
| jointColor | number | Yes | "0xe0e042" | The color value of joints when `showJoint` is set. |
| jointLineOpacity | number | Yes | 1 | The line opacity when rendering joints, a value between 0 and 1. |
| jointLineThickness | number | Yes | 2 | The line thickness when rendering joints. |
| pinSize | number | Yes | 4 | The size of the circles drawn when rendering pin constraints. |
| pinColor | number | Yes | "0x42e0e0" | The color value of the circles drawn when rendering pin constraints. |
| springColor | number | Yes | "0xe042e0" | The color value of spring constraints. |
| anchorColor | number | Yes | "0xefefef" | The color value of constraint anchors. |
| anchorSize | number | Yes | 4 | The size of the circles drawn as the constraint anchors. |
| showConvexHulls | boolean | Yes | false | When rendering polygon bodies, render the convex hull as well? |
| hullColor | number | Yes | "0xd703d0" | The color value of hulls when `showConvexHulls` is set. |

**Type**: object

**Member of**: Phaser.Types.Physics.Matter

> Source: [src/physics/matter-js/typedefs/MatterDebugConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/typedefs/MatterDebugConfig.js#L1)  
> Since: 3.22.0

---

## MatterRunnerConfig

### <static> MatterRunnerConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| isFixed | boolean | Yes | false | A boolean that specifies if the runner should use a fixed timestep (otherwise it is variable). If timing is fixed, then the apparent simulation speed will change depending on the frame rate (but behaviour will be deterministic). If the timing is variable, then the apparent simulation speed will be constant (approximately, but at the cost of determininism). |
| --- | --- | --- | --- | --- |
| fps | number | Yes | 60 | A number that specifies the frame rate in seconds. If you don't specify this, but do specify `delta`, those values set the fps rate. |
| correction | number | Yes | 1 | A number that specifies the time correction factor to apply to the update. This can help improve the accuracy of the simulation in cases where delta is changing between updates. |
| deltaSampleSize | number | Yes | 60 | The size of the delta smoothing array when `isFixed` is `false`. |
| delta | number | Yes | 16.666 | A number that specifies the time step between updates in milliseconds. If you set the `fps` property, this value is set based on that. If `isFixed` is set to `true`, then `delta` is fixed. If it is `false`, then `delta` can dynamically change to maintain the correct apparent simulation speed. |
| deltaMin | number | Yes | 16.666 | A number that specifies the minimum time step between updates in milliseconds. |
| deltaMax | number | Yes | 33.333 | A number that specifies the maximum time step between updates in milliseconds. |

**Type**: object

**Member of**: Phaser.Types.Physics.Matter

> Source: [src/physics/matter-js/typedefs/MatterRunnerConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/typedefs/MatterRunnerConfig.js#L1)  
> Since: 3.22.0

---

## MatterSetBodyConfig

### <static> MatterSetBodyConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| type | string | Yes | "'rectangle'" | The shape type. Either `rectangle`, `circle`, `trapezoid`, `polygon`, `fromVertices`, `fromVerts` or `fromPhysicsEditor`. |
| --- | --- | --- | --- | --- |
| x | number | Yes |  | The horizontal world position to place the body at. |
| y | number | Yes |  | The vertical world position to place the body at. |
| width | number | Yes |  | The width of the body. |
| height | number | Yes |  | The height of the body. |
| radius | number | Yes |  | The radius of the body. Used by `circle` and `polygon` shapes. |
| maxSides | number | Yes | 25 | The max sizes of the body. Used by the `circle` shape. |
| slope | number | Yes | 0.5 | Used by the `trapezoid` shape. The slope of the trapezoid. 0 creates a rectangle, while 1 creates a triangle. Positive values make the top side shorter, while negative values make the bottom side shorter. |
| sides | number | Yes | 5 | Used by the `polygon` shape. The number of sides the polygon will have. |
| verts | string | array | Yes |  | Used by the `fromVerts` shape. The vertices data. Either a path string or an array of vertices. |
| flagInternal | boolean | Yes | false | Used by the `fromVerts` shape. Flag internal edges (coincident part edges) |
| removeCollinear | number | Yes | 0.01 | Used by the `fromVerts` shape. Whether Matter.js will discard collinear edges (to improve performance). |
| minimumArea | number | Yes | 10 | Used by the `fromVerts` shape. During decomposition discard parts that have an area less than this. |
| addToWorld | boolean | Yes | true | Should the new body be automatically added to the world? |

**Type**: object

**Member of**: Phaser.Types.Physics.Matter

> Source: [src/physics/matter-js/typedefs/MatterSetBodyConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/typedefs/MatterSetBodyConfig.js#L1)  
> Since: 3.22.0

---

## MatterTileOptions

### <static> MatterTileOptions

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| body | MatterJS.BodyType | Yes | null | An existing Matter body to be used instead of creating a new one. |
| --- | --- | --- | --- | --- |
| isStatic | boolean | Yes | true | Whether or not the newly created body should be made static. This defaults to true since typically tiles should not be moved. |
| addToWorld | boolean | Yes | true | Whether or not to add the newly created body (or existing body if options.body is used) to the Matter world. |

**Type**: object

**Member of**: Phaser.Types.Physics.Matter

> Source: [src/physics/matter-js/typedefs/MatterTileOptions.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/typedefs/MatterTileOptions.js#L1)  
> Since: 3.0.0

---

## MatterWalls

### <static> MatterWalls

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| left | MatterJS.BodyType | Yes | null | The left wall for the Matter World. |
| --- | --- | --- | --- | --- |
| right | MatterJS.BodyType | Yes | null | The right wall for the Matter World. |
| top | MatterJS.BodyType | Yes | null | The top wall for the Matter World. |
| bottom | MatterJS.BodyType | Yes | null | The bottom wall for the Matter World. |

**Type**: object

**Member of**: Phaser.Types.Physics.Matter

> Source: [src/physics/matter-js/typedefs/MatterWalls.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/typedefs/MatterWalls.js#L1)  
> Since: 3.0.0

---

## MatterWorldConfig

### <static> MatterWorldConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| gravity | [Phaser.Types.Math.Vector2Like](types-math.md) | Yes |  | Sets {@link Phaser.Physics.Matter.World#gravity}. |
| --- | --- | --- | --- | --- |
| setBounds | object | boolean | Yes |  | Should the world have bounds enabled by default? |
| setBounds.x | number | Yes | 0 | The x coordinate of the world bounds. |
| setBounds.y | number | Yes | 0 | The y coordinate of the world bounds. |
| setBounds.width | number | Yes |  | The width of the world bounds. |
| setBounds.height | number | Yes |  | The height of the world bounds. |
| setBounds.thickness | number | Yes | 64 | The thickness of the walls of the world bounds. |
| setBounds.left | boolean | Yes | true | Should the left-side world bounds wall be created? |
| setBounds.right | boolean | Yes | true | Should the right-side world bounds wall be created? |
| setBounds.top | boolean | Yes | true | Should the top world bounds wall be created? |
| setBounds.bottom | boolean | Yes | true | Should the bottom world bounds wall be created? |
| positionIterations | number | Yes | 6 | The number of position iterations to perform each update. The higher the value, the higher quality the simulation will be at the expense of performance. |
| velocityIterations | number | Yes | 4 | The number of velocity iterations to perform each update. The higher the value, the higher quality the simulation will be at the expense of performance. |
| constraintIterations | number | Yes | 2 | The number of constraint iterations to perform each update. The higher the value, the higher quality the simulation will be at the expense of performance. |
| enableSleeping | boolean | Yes | false | A flag that specifies whether the engine should allow sleeping via the `Matter.Sleeping` module. Sleeping can improve stability and performance, but often at the expense of accuracy. |
| timing.timestamp | number | Yes | 0 | A `Number` that specifies the current simulation-time in milliseconds starting from `0`. It is incremented on every `Engine.update` by the given `delta` argument. |
| timing.timeScale | number | Yes | 1 | A `Number` that specifies the global scaling factor of time for all bodies. A value of `0` freezes the simulation. A value of `0.1` gives a slow-motion effect. A value of `1.2` gives a speed-up effect. |
| enabled | boolean | Yes | true | Toggles if the world is enabled or not. |
| correction | number | Yes | 1 | An optional Number that specifies the time correction factor to apply to the update. |
| getDelta | function | Yes |  | This function is called every time the core game loop steps, which is bound to the Request Animation Frame frequency unless otherwise modified. |
| autoUpdate | boolean | Yes | true | Automatically call Engine.update every time the game steps. |
| restingThresh | number | Yes | 4 | Sets the Resolver resting threshold property. |
| restingThreshTangent | number | Yes | 6 | Sets the Resolver resting threshold tangent property. |
| positionDampen | number | Yes | 0.9 | Sets the Resolver position dampen property. |
| positionWarming | number | Yes | 0.8 | Sets the Resolver position warming property. |
| frictionNormalMultiplier | number | Yes | 5 | Sets the Resolver friction normal multiplier property. |
| debug | boolean | [Phaser.Types.Physics.Matter.MatterDebugConfig](types-physics-matter.md) | Yes | false | Controls the Matter Debug Rendering options. If a boolean it will use the default values, otherwise, specify a Debug Config object. |
| runner | [Phaser.Types.Physics.Matter.MatterRunnerConfig](types-physics-matter.md) | Yes |  | Sets the Matter Runner options. |

**Type**: object

**Member of**: Phaser.Types.Physics.Matter

> Source: [src/physics/matter-js/typedefs/MatterWorldConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/typedefs/MatterWorldConfig.js#L1)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Types.Physics.Matter](#typesphysicsmatter)

  + [MatterBody](#matterbody)

    - [<static> MatterBody](#static-matterbody)
  + [MatterBodyConfig](#matterbodyconfig)

    - [<static> MatterBodyConfig](#static-matterbodyconfig)
  + [MatterBodyRenderConfig](#matterbodyrenderconfig)

    - [<static> MatterBodyRenderConfig](#static-matterbodyrenderconfig)
  + [MatterBodyTileOptions](#matterbodytileoptions)

    - [<static> MatterBodyTileOptions](#static-matterbodytileoptions)
  + [MatterChamferConfig](#matterchamferconfig)

    - [<static> MatterChamferConfig](#static-matterchamferconfig)
  + [MatterCollisionData](#mattercollisiondata)

    - [<static> MatterCollisionData](#static-mattercollisiondata)
  + [MatterCollisionFilter](#mattercollisionfilter)

    - [<static> MatterCollisionFilter](#static-mattercollisionfilter)
  + [MatterCollisionPair](#mattercollisionpair)

    - [<static> MatterCollisionPair](#static-mattercollisionpair)
  + [MatterConstraintConfig](#matterconstraintconfig)

    - [<static> MatterConstraintConfig](#static-matterconstraintconfig)
  + [MatterConstraintRenderConfig](#matterconstraintrenderconfig)

    - [<static> MatterConstraintRenderConfig](#static-matterconstraintrenderconfig)
  + [MatterDebugConfig](#matterdebugconfig)

    - [<static> MatterDebugConfig](#static-matterdebugconfig)
  + [MatterRunnerConfig](#matterrunnerconfig)

    - [<static> MatterRunnerConfig](#static-matterrunnerconfig)
  + [MatterSetBodyConfig](#mattersetbodyconfig)

    - [<static> MatterSetBodyConfig](#static-mattersetbodyconfig)
  + [MatterTileOptions](#mattertileoptions)

    - [<static> MatterTileOptions](#static-mattertileoptions)
  + [MatterWalls](#matterwalls)

    - [<static> MatterWalls](#static-matterwalls)
  + [MatterWorldConfig](#matterworldconfig)

    - [<static> MatterWorldConfig](#static-matterworldconfig)

Back to top

©2025[Phaser](https://docs.phaser.io)



Types.Physics.Matter