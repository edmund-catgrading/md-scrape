# Factory

Phaser.Physics.Matter.Factory

The Matter Factory is responsible for quickly creating a variety of different types of

bodies, constraints and Game Objects and adding them into the physics world.

You access the factory from within a Scene using `add`:

```
Copy
this.matter.add.rectangle(x, y, width, height);


```

Use of the Factory is optional. All of the objects it creates can also be created

directly via your own code or constructors. It is provided as a means to keep your

code concise.

**Constructor**

`new Factory(world)`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| world | [Phaser.Physics.Matter.World](physics-matter-world.md) | No | The Matter World which this Factory adds to. |
| --- | --- | --- | --- |

---

**Scope**: static

> Source: [src/physics/matter-js/Factory.js#L21](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/Factory.js#L21)  
> Since: 3.0.0

# Public Members

## scene

### scene: [Phaser.Scene](scene.md)

**Description:**

The Scene which this Factory's Matter World belongs to.

> Source: [src/physics/matter-js/Factory.js#L58](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/Factory.js#L58)  
> Since: 3.0.0

---

## sys

### sys: [Phaser.Scenes.Systems](scenes-systems.md)

**Description:**

A reference to the Scene.Systems this Matter Physics instance belongs to.

> Source: [src/physics/matter-js/Factory.js#L67](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/Factory.js#L67)  
> Since: 3.0.0

---

## world

### world: [Phaser.Physics.Matter.World](physics-matter-world.md)

**Description:**

The Matter World which this Factory adds to.

> Source: [src/physics/matter-js/Factory.js#L49](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/Factory.js#L49)  
> Since: 3.0.0

---

# Public Methods

## car

### <instance> car(x, y, width, height, wheelSize)

**Description:**

Creates a composite with simple car setup of bodies and constraints.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The horizontal position of the car in the world. |
| --- | --- | --- | --- |
| y | number | No | The vertical position of the car in the world. |
| width | number | No | The width of the car chasis. |
| height | number | No | The height of the car chasis. |
| wheelSize | number | No | The radius of the car wheels. |

**Returns:** MatterJS.CompositeType - A new composite car body.

> Source: [src/physics/matter-js/Factory.js#L534](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/Factory.js#L534)  
> Since: 3.0.0

---

## chain

### <instance> chain(composite, xOffsetA, yOffsetA, xOffsetB, yOffsetB, [options])

**Description:**

Chains all bodies in the given composite together using constraints.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| composite | MatterJS.CompositeType | No | The composite in which all bodies will be chained together sequentially. |
| --- | --- | --- | --- |
| xOffsetA | number | No | The horizontal offset of the BodyA constraint. This is a percentage based on the body size, not a world position. |
| yOffsetA | number | No | The vertical offset of the BodyA constraint. This is a percentage based on the body size, not a world position. |
| xOffsetB | number | No | The horizontal offset of the BodyB constraint. This is a percentage based on the body size, not a world position. |
| yOffsetB | number | No | The vertical offset of the BodyB constraint. This is a percentage based on the body size, not a world position. |
| options | [Phaser.Types.Physics.Matter.MatterConstraintConfig](../typedef/types-physics-matter.md) | Yes | An optional Constraint configuration object that is used to set initial Constraint properties on creation. |

**Returns:** MatterJS.CompositeType - The original composite that was passed to this method.

> Source: [src/physics/matter-js/Factory.js#L472](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/Factory.js#L472)  
> Since: 3.0.0

---

## circle

### <instance> circle(x, y, radius, [options], [maxSides])

**Description:**

Creates a new rigid circular Body and adds it to the World.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The X coordinate of the center of the Body. |
| --- | --- | --- | --- |
| y | number | No | The Y coordinate of the center of the Body. |
| radius | number | No | The radius of the circle. |
| options | [Phaser.Types.Physics.Matter.MatterBodyConfig](../typedef/types-physics-matter.md) | Yes | An optional Body configuration object that is used to set initial Body properties on creation. |
| maxSides | number | Yes | The maximum amount of sides to use for the polygon which will approximate this circle. |

**Returns:** MatterJS.BodyType - A Matter JS Body.

> Source: [src/physics/matter-js/Factory.js#L124](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/Factory.js#L124)  
> Since: 3.0.0

---

## constraint

### <instance> constraint(bodyA, bodyB, [length], [stiffness], [options])

**Description:**

Constraints (or joints) are used for specifying that a fixed distance must be maintained

between two bodies, or a body and a fixed world-space position.

The stiffness of constraints can be modified to create springs or elastic.

To simulate a revolute constraint (or pin joint) set `length: 0` and a high `stiffness`

value (e.g. `0.7` or above).

If the constraint is unstable, try lowering the `stiffness` value and / or increasing

`constraintIterations` within the Matter Config.

For compound bodies, constraints must be applied to the parent body and not one of its parts.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| bodyA | MatterJS.BodyType | No |  | The first possible `Body` that this constraint is attached to. |
| --- | --- | --- | --- | --- |
| bodyB | MatterJS.BodyType | No |  | The second possible `Body` that this constraint is attached to. |
| length | number | Yes |  | A Number that specifies the target resting length of the constraint. If not given it is calculated automatically in `Constraint.create` from initial positions of the `constraint.bodyA` and `constraint.bodyB`. |
| stiffness | number | Yes | 1 | A Number that specifies the stiffness of the constraint, i.e. the rate at which it returns to its resting `constraint.length`. A value of `1` means the constraint should be very stiff. A value of `0.2` means the constraint acts as a soft spring. |
| options | [Phaser.Types.Physics.Matter.MatterConstraintConfig](../typedef/types-physics-matter.md) | Yes |  | An optional Constraint configuration object that is used to set initial Constraint properties on creation. |

**Returns:** MatterJS.ConstraintType - A Matter JS Constraint.

> Source: [src/physics/matter-js/Factory.js#L649](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/Factory.js#L649)  
> Since: 3.0.0

---

## destroy

### <instance> destroy()

**Description:**

Destroys this Factory.

> Source: [src/physics/matter-js/Factory.js#L909](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/Factory.js#L909)  
> Since: 3.5.0

---

## fromJSON

### <instance> fromJSON(x, y, config, [options], [addToWorld])

**Description:**

Creates a body using the supplied physics data, as provided by a JSON file.

The data file should be loaded as JSON:

```
Copy
preload ()

{

  this.load.json('ninjas', 'assets/ninjas.json);

}



create ()

{

  const ninjaShapes = this.cache.json.get('ninjas');



  this.matter.add.fromJSON(400, 300, ninjaShapes.shinobi);

}


```

Do not pass the entire JSON file to this method, but instead pass one of the shapes contained within it.

If you pas in an `options` object, any settings in there will override those in the config object.

The structure of the JSON file is as follows:

```
Copy
{

  'generator_info': // The name of the application that created the JSON data

  'shapeName': {

    'type': // The type of body

    'label': // Optional body label

    'vertices': // An array, or an array of arrays, containing the vertex data in x/y object pairs

  }

}


```

At the time of writing, only the Phaser Physics Tracer App exports in this format.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | No |  | The X coordinate of the body. |
| --- | --- | --- | --- | --- |
| y | number | No |  | The Y coordinate of the body. |
| config | any | No |  | The JSON physics data. |
| options | [Phaser.Types.Physics.Matter.MatterBodyConfig](../typedef/types-physics-matter.md) | Yes |  | An optional Body configuration object that is used to set initial Body properties on creation. |
| addToWorld | boolean | Yes | true | Should the newly created body be immediately added to the World? |

**Returns:** MatterJS.BodyType - A Matter JS Body.

> Source: [src/physics/matter-js/Factory.js#L311](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/Factory.js#L311)  
> Since: 3.22.0

---

## fromPhysicsEditor

### <instance> fromPhysicsEditor(x, y, config, [options], [addToWorld])

**Description:**

Creates a body using data exported from the application PhysicsEditor (<https://www.codeandweb.com/physicseditor>)

The PhysicsEditor file should be loaded as JSON:

```
Copy
preload ()

{

  this.load.json('vehicles', 'assets/vehicles.json);

}



create ()

{

  const vehicleShapes = this.cache.json.get('vehicles');

  this.matter.add.fromPhysicsEditor(400, 300, vehicleShapes.truck);

}


```

Do not pass the entire JSON file to this method, but instead pass one of the shapes contained within it.

If you pas in an `options` object, any settings in there will override those in the PhysicsEditor config object.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | No |  | The horizontal world location of the body. |
| --- | --- | --- | --- | --- |
| y | number | No |  | The vertical world location of the body. |
| config | any | No |  | The JSON data exported from PhysicsEditor. |
| options | [Phaser.Types.Physics.Matter.MatterBodyConfig](../typedef/types-physics-matter.md) | Yes |  | An optional Body configuration object that is used to set initial Body properties on creation. |
| addToWorld | boolean | Yes | true | Should the newly created body be immediately added to the World? |

**Returns:** MatterJS.BodyType - A Matter JS Body.

> Source: [src/physics/matter-js/Factory.js#L201](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/Factory.js#L201)  
> Since: 3.22.0

---

## fromSVG

### <instance> fromSVG(x, y, xml, [scale], [options], [addToWorld])

**Description:**

Creates a body using the path data from an SVG file.

SVG Parsing requires the pathseg polyfill from <https://github.com/progers/pathseg>

The SVG file should be loaded as XML, as this method requires the ability to extract

the path data from it. I.e.:

```
Copy
preload ()

{

  this.load.xml('face', 'assets/face.svg);

}



create ()

{

  this.matter.add.fromSVG(400, 300, this.cache.xml.get('face'));

}


```

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | No |  | The X coordinate of the body. |
| --- | --- | --- | --- | --- |
| y | number | No |  | The Y coordinate of the body. |
| xml | object | No |  | The SVG Path data. |
| scale | number | Yes | 1 | Scale the vertices by this amount after creation. |
| options | [Phaser.Types.Physics.Matter.MatterBodyConfig](../typedef/types-physics-matter.md) | Yes |  | An optional Body configuration object that is used to set initial Body properties on creation. |
| addToWorld | boolean | Yes | true | Should the newly created body be immediately added to the World? |

**Returns:** MatterJS.BodyType - A Matter JS Body.

> Source: [src/physics/matter-js/Factory.js#L248](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/Factory.js#L248)  
> Since: 3.22.0

---

## fromVertices

### <instance> fromVertices(x, y, vertexSets, [options], [flagInternal], [removeCollinear], [minimumArea])

**Description:**

Creates a body using the supplied vertices (or an array containing multiple sets of vertices) and adds it to the World.

If the vertices are convex, they will pass through as supplied. Otherwise, if the vertices are concave, they will be decomposed. Note that this process is not guaranteed to support complex sets of vertices, e.g. ones with holes.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | No |  | The X coordinate of the center of the Body. |
| --- | --- | --- | --- | --- |
| y | number | No |  | The Y coordinate of the center of the Body. |
| vertexSets | string | array | No |  | The vertices data. Either a path string or an array of vertices. |
| options | [Phaser.Types.Physics.Matter.MatterBodyConfig](../typedef/types-physics-matter.md) | Yes |  | An optional Body configuration object that is used to set initial Body properties on creation. |
| flagInternal | boolean | Yes | false | Flag internal edges (coincident part edges) |
| removeCollinear | number | Yes | 0.01 | Whether Matter.js will discard collinear edges (to improve performance). |
| minimumArea | number | Yes | 10 | During decomposition discard parts that have an area less than this. |

**Returns:** MatterJS.BodyType - A Matter JS Body.

> Source: [src/physics/matter-js/Factory.js#L170](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/Factory.js#L170)  
> Since: 3.0.0

---

## gameObject

### <instance> gameObject(gameObject, [options], [addToWorld])

**Description:**

Takes an existing Game Object and injects all of the Matter Components into it.

This enables you to use component methods such as `setVelocity` or `isSensor` directly from

this Game Object.

You can also pass in either a Matter Body Configuration object, or a Matter Body instance

to link with this Game Object.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No |  | The Game Object to inject the Matter Components in to. |
| --- | --- | --- | --- | --- |
| options | [Phaser.Types.Physics.Matter.MatterBodyConfig](../typedef/types-physics-matter.md) | MatterJS.Body | Yes |  | A Matter Body configuration object, or an instance of a Matter Body. |
| addToWorld | boolean | Yes | true | Add this Matter Body to the World? |

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md), [Phaser.Physics.Matter.Sprite](physics-matter-sprite.md), [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) - The Game Object that had the Matter Components injected into it.

> Source: [src/physics/matter-js/Factory.js#L886](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/Factory.js#L886)  
> Since: 3.3.0

---

## image

### <instance> image(x, y, key, [frame], [options])

**Description:**

Creates a Matter Physics Image Game Object.

An Image is a light-weight Game Object useful for the display of static images in your game,

such as logos, backgrounds, scenery or other non-animated elements. Images can have input

events and physics bodies, or be tweened, tinted or scrolled. The main difference between an

Image and a Sprite is that you cannot animate an Image as they do not have the Animation component.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The horizontal position of this Game Object in the world. |
| --- | --- | --- | --- |
| y | number | No | The vertical position of this Game Object in the world. |
| key | string | No | The key of the Texture this Game Object will use to render with, as stored in the Texture Manager. |
| frame | string | number | Yes | An optional frame from the Texture this Game Object is rendering with. Set to `null` to skip this value. |
| options | [Phaser.Types.Physics.Matter.MatterBodyConfig](../typedef/types-physics-matter.md) | Yes | An optional Body configuration object that is used to set initial Body properties on creation. |

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - The Matter Image Game Object.

> Source: [src/physics/matter-js/Factory.js#L801](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/Factory.js#L801)  
> Since: 3.0.0

---

## imageStack

### <instance> imageStack(key, frame, x, y, columns, rows, [columnGap], [rowGap], [options])

**Description:**

Create a new composite containing Matter Image objects created in a grid arrangement.

This function uses the body bounds to prevent overlaps.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | string | No |  | The key of the Texture this Game Object will use to render with, as stored in the Texture Manager. |
| --- | --- | --- | --- | --- |
| frame | string | number | No |  | An optional frame from the Texture this Game Object is rendering with. Set to `null` to skip this value. |
| x | number | No |  | The horizontal position of this composite in the world. |
| y | number | No |  | The vertical position of this composite in the world. |
| columns | number | No |  | The number of columns in the grid. |
| rows | number | No |  | The number of rows in the grid. |
| columnGap | number | Yes | 0 | The distance between each column. |
| rowGap | number | Yes | 0 | The distance between each row. |
| options | [Phaser.Types.Physics.Matter.MatterBodyConfig](../typedef/types-physics-matter.md) | Yes |  | An optional Body configuration object that is used to set initial Body properties on creation. |

**Returns:** MatterJS.CompositeType - A Matter JS Composite Stack.

> Source: [src/physics/matter-js/Factory.js#L375](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/Factory.js#L375)  
> Since: 3.0.0

---

## joint

### <instance> joint(bodyA, bodyB, [length], [stiffness], [options])

**Description:**

This method is an alias for `Factory.constraint`.

Constraints (or joints) are used for specifying that a fixed distance must be maintained

between two bodies, or a body and a fixed world-space position.

The stiffness of constraints can be modified to create springs or elastic.

To simulate a revolute constraint (or pin joint) set `length: 0` and a high `stiffness`

value (e.g. `0.7` or above).

If the constraint is unstable, try lowering the `stiffness` value and / or increasing

`constraintIterations` within the Matter Config.

For compound bodies, constraints must be applied to the parent body and not one of its parts.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| bodyA | MatterJS.BodyType | No |  | The first possible `Body` that this constraint is attached to. |
| --- | --- | --- | --- | --- |
| bodyB | MatterJS.BodyType | No |  | The second possible `Body` that this constraint is attached to. |
| length | number | Yes |  | A Number that specifies the target resting length of the constraint. If not given it is calculated automatically in `Constraint.create` from initial positions of the `constraint.bodyA` and `constraint.bodyB`. |
| stiffness | number | Yes | 1 | A Number that specifies the stiffness of the constraint, i.e. the rate at which it returns to its resting `constraint.length`. A value of `1` means the constraint should be very stiff. A value of `0.2` means the constraint acts as a soft spring. |
| options | [Phaser.Types.Physics.Matter.MatterConstraintConfig](../typedef/types-physics-matter.md) | Yes |  | An optional Constraint configuration object that is used to set initial Constraint properties on creation. |

**Returns:** MatterJS.ConstraintType - A Matter JS Constraint.

> Source: [src/physics/matter-js/Factory.js#L585](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/Factory.js#L585)  
> Since: 3.0.0

---

## mesh

### <instance> mesh(composite, columns, rows, crossBrace, [options])

**Description:**

Connects bodies in the composite with constraints in a grid pattern, with optional cross braces.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| composite | MatterJS.CompositeType | No | The composite in which all bodies will be chained together. |
| --- | --- | --- | --- |
| columns | number | No | The number of columns in the mesh. |
| rows | number | No | The number of rows in the mesh. |
| crossBrace | boolean | No | Create cross braces for the mesh as well? |
| options | [Phaser.Types.Physics.Matter.MatterConstraintConfig](../typedef/types-physics-matter.md) | Yes | An optional Constraint configuration object that is used to set initial Constraint properties on creation. |

**Returns:** MatterJS.CompositeType - The original composite that was passed to this method.

> Source: [src/physics/matter-js/Factory.js#L492](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/Factory.js#L492)  
> Since: 3.0.0

---

## mouseSpring

### <instance> mouseSpring([options])

**Description:**

This method is an alias for `Factory.pointerConstraint`.

A Pointer Constraint is a special type of constraint that allows you to click

and drag bodies in a Matter World. It monitors the active Pointers in a Scene,

and when one is pressed down it checks to see if that hit any part of any active

body in the world. If it did, and the body has input enabled, it will begin to

drag it until either released, or you stop it via the `stopDrag` method.

You can adjust the stiffness, length and other properties of the constraint via

the `options` object on creation.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| options | [Phaser.Types.Physics.Matter.MatterConstraintConfig](../typedef/types-physics-matter.md) | Yes | An optional Constraint configuration object that is used to set initial Constraint properties on creation. |
| --- | --- | --- | --- |

**Returns:** MatterJS.ConstraintType - A Matter JS Constraint.

> Source: [src/physics/matter-js/Factory.js#L744](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/Factory.js#L744)  
> Since: 3.0.0

---

## newtonsCradle

### <instance> newtonsCradle(x, y, number, size, length)

**Description:**

Creates a composite with a Newton's Cradle setup of bodies and constraints.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The horizontal position of the start of the cradle. |
| --- | --- | --- | --- |
| y | number | No | The vertical position of the start of the cradle. |
| number | number | No | The number of balls in the cradle. |
| size | number | No | The radius of each ball in the cradle. |
| length | number | No | The length of the 'string' the balls hang from. |

**Returns:** MatterJS.CompositeType - A Newton's cradle composite.

> Source: [src/physics/matter-js/Factory.js#L511](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/Factory.js#L511)  
> Since: 3.0.0

---

## pointerConstraint

### <instance> pointerConstraint([options])

**Description:**

A Pointer Constraint is a special type of constraint that allows you to click

and drag bodies in a Matter World. It monitors the active Pointers in a Scene,

and when one is pressed down it checks to see if that hit any part of any active

body in the world. If it did, and the body has input enabled, it will begin to

drag it until either released, or you stop it via the `stopDrag` method.

You can adjust the stiffness, length and other properties of the constraint via

the `options` object on creation.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| options | [Phaser.Types.Physics.Matter.MatterConstraintConfig](../typedef/types-physics-matter.md) | Yes | An optional Constraint configuration object that is used to set initial Constraint properties on creation. |
| --- | --- | --- | --- |

**Returns:** MatterJS.ConstraintType - A Matter JS Constraint.

> Source: [src/physics/matter-js/Factory.js#L768](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/Factory.js#L768)  
> Since: 3.0.0

---

## polygon

### <instance> polygon(x, y, sides, radius, [options])

**Description:**

Creates a new rigid polygonal Body and adds it to the World.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The X coordinate of the center of the Body. |
| --- | --- | --- | --- |
| y | number | No | The Y coordinate of the center of the Body. |
| sides | number | No | The number of sides the polygon will have. |
| radius | number | No | The "radius" of the polygon, i.e. the distance from its center to any vertex. This is also the radius of its circumcircle. |
| options | [Phaser.Types.Physics.Matter.MatterBodyConfig](../typedef/types-physics-matter.md) | Yes | An optional Body configuration object that is used to set initial Body properties on creation. |

**Returns:** MatterJS.BodyType - A Matter JS Body.

> Source: [src/physics/matter-js/Factory.js#L147](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/Factory.js#L147)  
> Since: 3.0.0

---

## pyramid

### <instance> pyramid(x, y, columns, rows, columnGap, rowGap, callback)

**Description:**

Create a new composite containing bodies created in the callback in a pyramid arrangement.

This function uses the body bounds to prevent overlaps.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The horizontal position of this composite in the world. |
| --- | --- | --- | --- |
| y | number | No | The vertical position of this composite in the world. |
| columns | number | No | The number of columns in the pyramid. |
| rows | number | No | The number of rows in the pyramid. |
| columnGap | number | No | The distance between each column. |
| rowGap | number | No | The distance between each row. |
| callback | function | No | The callback function to be invoked. |

**Returns:** MatterJS.CompositeType - A Matter JS Composite pyramid.

> Source: [src/physics/matter-js/Factory.js#L446](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/Factory.js#L446)  
> Since: 3.0.0

---

## rectangle

### <instance> rectangle(x, y, width, height, [options])

**Description:**

Creates a new rigid rectangular Body and adds it to the World.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The X coordinate of the center of the Body. |
| --- | --- | --- | --- |
| y | number | No | The Y coordinate of the center of the Body. |
| width | number | No | The width of the Body. |
| height | number | No | The height of the Body. |
| options | [Phaser.Types.Physics.Matter.MatterBodyConfig](../typedef/types-physics-matter.md) | Yes | An optional Body configuration object that is used to set initial Body properties on creation. |

**Returns:** MatterJS.BodyType - A Matter JS Body.

> Source: [src/physics/matter-js/Factory.js#L77](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/Factory.js#L77)  
> Since: 3.0.0

---

## softBody

### <instance> softBody(x, y, columns, rows, columnGap, rowGap, crossBrace, particleRadius, [particleOptions], [constraintOptions])

**Description:**

Creates a simple soft body like object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The horizontal position of this composite in the world. |
| --- | --- | --- | --- |
| y | number | No | The vertical position of this composite in the world. |
| columns | number | No | The number of columns in the Composite. |
| rows | number | No | The number of rows in the Composite. |
| columnGap | number | No | The distance between each column. |
| rowGap | number | No | The distance between each row. |
| crossBrace | boolean | No | `true` to create cross braces between the bodies, or `false` to create just straight braces. |
| particleRadius | number | No | The radius of this circlular composite. |
| particleOptions | [Phaser.Types.Physics.Matter.MatterBodyConfig](../typedef/types-physics-matter.md) | Yes | An optional Body configuration object that is used to set initial Body properties on creation. |
| constraintOptions | [Phaser.Types.Physics.Matter.MatterConstraintConfig](../typedef/types-physics-matter.md) | Yes | An optional Constraint configuration object that is used to set initial Constraint properties on creation. |

**Returns:** MatterJS.CompositeType - A new composite simple soft body.

> Source: [src/physics/matter-js/Factory.js#L557](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/Factory.js#L557)  
> Since: 3.0.0

---

## spring

### <instance> spring(bodyA, bodyB, [length], [stiffness], [options])

**Description:**

This method is an alias for `Factory.constraint`.

Constraints (or joints) are used for specifying that a fixed distance must be maintained

between two bodies, or a body and a fixed world-space position.

The stiffness of constraints can be modified to create springs or elastic.

To simulate a revolute constraint (or pin joint) set `length: 0` and a high `stiffness`

value (e.g. `0.7` or above).

If the constraint is unstable, try lowering the `stiffness` value and / or increasing

`constraintIterations` within the Matter Config.

For compound bodies, constraints must be applied to the parent body and not one of its parts.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| bodyA | MatterJS.BodyType | No |  | The first possible `Body` that this constraint is attached to. |
| --- | --- | --- | --- | --- |
| bodyB | MatterJS.BodyType | No |  | The second possible `Body` that this constraint is attached to. |
| length | number | Yes |  | A Number that specifies the target resting length of the constraint. If not given it is calculated automatically in `Constraint.create` from initial positions of the `constraint.bodyA` and `constraint.bodyB`. |
| stiffness | number | Yes | 1 | A Number that specifies the stiffness of the constraint, i.e. the rate at which it returns to its resting `constraint.length`. A value of `1` means the constraint should be very stiff. A value of `0.2` means the constraint acts as a soft spring. |
| options | [Phaser.Types.Physics.Matter.MatterConstraintConfig](../typedef/types-physics-matter.md) | Yes |  | An optional Constraint configuration object that is used to set initial Constraint properties on creation. |

**Returns:** MatterJS.ConstraintType - A Matter JS Constraint.

> Source: [src/physics/matter-js/Factory.js#L617](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/Factory.js#L617)  
> Since: 3.0.0

---

## sprite

### <instance> sprite(x, y, key, [frame], [options])

**Description:**

Creates a Matter Physics Sprite Game Object.

A Sprite Game Object is used for the display of both static and animated images in your game.

Sprites can have input events and physics bodies. They can also be tweened, tinted, scrolled

and animated.

The main difference between a Sprite and an Image Game Object is that you cannot animate Images.

As such, Sprites take a fraction longer to process and have a larger API footprint due to the Animation

Component. If you do not require animation then you can safely use Images to replace Sprites in all cases.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The horizontal position of this Game Object in the world. |
| --- | --- | --- | --- |
| y | number | No | The vertical position of this Game Object in the world. |
| key | string | No | The key of the Texture this Game Object will use to render with, as stored in the Texture Manager. |
| frame | string | number | Yes | An optional frame from the Texture this Game Object is rendering with. Set to `null` to skip this value. |
| options | [Phaser.Types.Physics.Matter.MatterBodyConfig](../typedef/types-physics-matter.md) | Yes | An optional Body configuration object that is used to set initial Body properties on creation. |

**Returns:** [Phaser.Physics.Matter.Sprite](physics-matter-sprite.md) - The Matter Sprite Game Object.

> Source: [src/physics/matter-js/Factory.js#L854](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/Factory.js#L854)  
> Since: 3.0.0

---

## stack

### <instance> stack(x, y, columns, rows, columnGap, rowGap, callback)

**Description:**

Create a new composite containing bodies created in the callback in a grid arrangement.

This function uses the body bounds to prevent overlaps.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The horizontal position of this composite in the world. |
| --- | --- | --- | --- |
| y | number | No | The vertical position of this composite in the world. |
| columns | number | No | The number of columns in the grid. |
| rows | number | No | The number of rows in the grid. |
| columnGap | number | No | The distance between each column. |
| rowGap | number | No | The distance between each row. |
| callback | function | No | The callback that creates the stack. |

**Returns:** MatterJS.CompositeType - A new composite containing objects created in the callback.

> Source: [src/physics/matter-js/Factory.js#L419](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/Factory.js#L419)  
> Since: 3.0.0

---

## tileBody

### <instance> tileBody(tile, [options])

**Description:**

Creates a wrapper around a Tile that provides access to a corresponding Matter body. A tile can only

have one Matter body associated with it. You can either pass in an existing Matter body for

the tile or allow the constructor to create the corresponding body for you. If the Tile has a

collision group (defined in Tiled), those shapes will be used to create the body. If not, the

tile's rectangle bounding box will be used.

The corresponding body will be accessible on the Tile itself via Tile.physics.matterBody.

Note: not all Tiled collision shapes are supported. See

Phaser.Physics.Matter.TileBody#setFromTileCollision for more information.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tile | [Phaser.Tilemaps.Tile](tilemaps-tile.md) | No | The target tile that should have a Matter body. |
| --- | --- | --- | --- |
| options | [Phaser.Types.Physics.Matter.MatterTileOptions](../typedef/types-physics-matter.md) | Yes | Options to be used when creating the Matter body. |

**Returns:** [Phaser.Physics.Matter.TileBody](physics-matter-tilebody.md) - The Matter Tile Body Game Object.

> Source: [src/physics/matter-js/Factory.js#L829](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/Factory.js#L829)  
> Since: 3.0.0

---

## trapezoid

### <instance> trapezoid(x, y, width, height, slope, [options])

**Description:**

Creates a new rigid trapezoidal Body and adds it to the World.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The X coordinate of the center of the Body. |
| --- | --- | --- | --- |
| y | number | No | The Y coordinate of the center of the Body. |
| width | number | No | The width of the trapezoid Body. |
| height | number | No | The height of the trapezoid Body. |
| slope | number | No | The slope of the trapezoid. 0 creates a rectangle, while 1 creates a triangle. Positive values make the top side shorter, while negative values make the bottom side shorter. |
| options | [Phaser.Types.Physics.Matter.MatterBodyConfig](../typedef/types-physics-matter.md) | Yes | An optional Body configuration object that is used to set initial Body properties on creation. |

**Returns:** MatterJS.BodyType - A Matter JS Body.

> Source: [src/physics/matter-js/Factory.js#L100](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/Factory.js#L100)  
> Since: 3.0.0

---

## worldConstraint

### <instance> worldConstraint(body, [length], [stiffness], [options])

**Description:**

Constraints (or joints) are used for specifying that a fixed distance must be maintained

between two bodies, or a body and a fixed world-space position.

A world constraint has only one body, you should specify a `pointA` position in

the constraint options parameter to attach the constraint to the world.

The stiffness of constraints can be modified to create springs or elastic.

To simulate a revolute constraint (or pin joint) set `length: 0` and a high `stiffness`

value (e.g. `0.7` or above).

If the constraint is unstable, try lowering the `stiffness` value and / or increasing

`constraintIterations` within the Matter Config.

For compound bodies, constraints must be applied to the parent body and not one of its parts.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| body | MatterJS.BodyType | No |  | The Matter `Body` that this constraint is attached to. |
| --- | --- | --- | --- | --- |
| length | number | Yes |  | A number that specifies the target resting length of the constraint. If not given it is calculated automatically in `Constraint.create` from initial positions of the `constraint.bodyA` and `constraint.bodyB`. |
| stiffness | number | Yes | 1 | A Number that specifies the stiffness of the constraint, i.e. the rate at which it returns to its resting `constraint.length`. A value of `1` means the constraint should be very stiff. A value of `0.2` means the constraint acts as a soft spring. |
| options | [Phaser.Types.Physics.Matter.MatterConstraintConfig](../typedef/types-physics-matter.md) | Yes |  | An optional Constraint configuration object that is used to set initial Constraint properties on creation. |

**Returns:** MatterJS.ConstraintType - A Matter JS Constraint.

> Source: [src/physics/matter-js/Factory.js#L696](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/Factory.js#L696)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [scene](#scene)

    - [scene: Phaser.Scene](#scene-phaserscene)
  + [sys](#sys)

    - [sys: Phaser.Scenes.Systems](#sys-phaserscenessystems)
  + [world](#world)

    - [world: Phaser.Physics.Matter.World](#world-phaserphysicsmatterworld)
* [Public Methods](#public-methods)

  + [car](#car)

    - [<instance> car(x, y, width, height, wheelSize)](#instance-carx-y-width-height-wheelsize)
  + [chain](#chain)

    - [<instance> chain(composite, xOffsetA, yOffsetA, xOffsetB, yOffsetB, [options])](#instance-chaincomposite-xoffseta-yoffseta-xoffsetb-yoffsetb-options)
  + [circle](#circle)

    - [<instance> circle(x, y, radius, [options], [maxSides])](#instance-circlex-y-radius-options-maxsides)
  + [constraint](#constraint)

    - [<instance> constraint(bodyA, bodyB, [length], [stiffness], [options])](#instance-constraintbodya-bodyb-length-stiffness-options)
  + [destroy](#destroy)

    - [<instance> destroy()](#instance-destroy)
  + [fromJSON](#fromjson)

    - [<instance> fromJSON(x, y, config, [options], [addToWorld])](#instance-fromjsonx-y-config-options-addtoworld)
  + [fromPhysicsEditor](#fromphysicseditor)

    - [<instance> fromPhysicsEditor(x, y, config, [options], [addToWorld])](#instance-fromphysicseditorx-y-config-options-addtoworld)
  + [fromSVG](#fromsvg)

    - [<instance> fromSVG(x, y, xml, [scale], [options], [addToWorld])](#instance-fromsvgx-y-xml-scale-options-addtoworld)
  + [fromVertices](#fromvertices)

    - [<instance> fromVertices(x, y, vertexSets, [options], [flagInternal], [removeCollinear], [minimumArea])](#instance-fromverticesx-y-vertexsets-options-flaginternal-removecollinear-minimumarea)
  + [gameObject](#gameobject)

    - [<instance> gameObject(gameObject, [options], [addToWorld])](#instance-gameobjectgameobject-options-addtoworld)
  + [image](#image)

    - [<instance> image(x, y, key, [frame], [options])](#instance-imagex-y-key-frame-options)
  + [imageStack](#imagestack)

    - [<instance> imageStack(key, frame, x, y, columns, rows, [columnGap], [rowGap], [options])](#instance-imagestackkey-frame-x-y-columns-rows-columngap-rowgap-options)
  + [joint](#joint)

    - [<instance> joint(bodyA, bodyB, [length], [stiffness], [options])](#instance-jointbodya-bodyb-length-stiffness-options)
  + [mesh](#mesh)

    - [<instance> mesh(composite, columns, rows, crossBrace, [options])](#instance-meshcomposite-columns-rows-crossbrace-options)
  + [mouseSpring](#mousespring)

    - [<instance> mouseSpring([options])](#instance-mousespringoptions)
  + [newtonsCradle](#newtonscradle)

    - [<instance> newtonsCradle(x, y, number, size, length)](#instance-newtonscradlex-y-number-size-length)
  + [pointerConstraint](#pointerconstraint)

    - [<instance> pointerConstraint([options])](#instance-pointerconstraintoptions)
  + [polygon](#polygon)

    - [<instance> polygon(x, y, sides, radius, [options])](#instance-polygonx-y-sides-radius-options)
  + [pyramid](#pyramid)

    - [<instance> pyramid(x, y, columns, rows, columnGap, rowGap, callback)](#instance-pyramidx-y-columns-rows-columngap-rowgap-callback)
  + [rectangle](#rectangle)

    - [<instance> rectangle(x, y, width, height, [options])](#instance-rectanglex-y-width-height-options)
  + [softBody](#softbody)

    - [<instance> softBody(x, y, columns, rows, columnGap, rowGap, crossBrace, particleRadius, [particleOptions], [constraintOptions])](#instance-softbodyx-y-columns-rows-columngap-rowgap-crossbrace-particleradius-particleoptions-constraintoptions)
  + [spring](#spring)

    - [<instance> spring(bodyA, bodyB, [length], [stiffness], [options])](#instance-springbodya-bodyb-length-stiffness-options)
  + [sprite](#sprite)

    - [<instance> sprite(x, y, key, [frame], [options])](#instance-spritex-y-key-frame-options)
  + [stack](#stack)

    - [<instance> stack(x, y, columns, rows, columnGap, rowGap, callback)](#instance-stackx-y-columns-rows-columngap-rowgap-callback)
  + [tileBody](#tilebody)

    - [<instance> tileBody(tile, [options])](#instance-tilebodytile-options)
  + [trapezoid](#trapezoid)

    - [<instance> trapezoid(x, y, width, height, slope, [options])](#instance-trapezoidx-y-width-height-slope-options)
  + [worldConstraint](#worldconstraint)

    - [<instance> worldConstraint(body, [length], [stiffness], [options])](#instance-worldconstraintbody-length-stiffness-options)

Back to top

©2025[Phaser](https://docs.phaser.io)