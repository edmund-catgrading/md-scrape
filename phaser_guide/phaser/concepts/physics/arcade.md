# Arcade Physics

A Guide to the Phaser Arcade Physics for simple, fast physics simulations

Arcade Physics is, as its name implies, meant for more 'arcade' or 'retro' style games, although is not limited just to those. It's a lightweight physics system that can only handle two different types of physics shapes: rectangles and circles. It's not meant for complex physics simulations, but rather for simple things like platformers, top-down games, or puzzle games. It's very fast and easy to use, with lots of helper functions, but due to its nature it does have its limitations.

Arcade Physics must be enabled before it can be used. This can be done via the Game Configuration or on a per-Scene basis. Once enabled, you can then add physics-enabled Game Objects to your game. This will allow you to control the Sprite using the built-in physics functions, such as velocity, acceleration, gravity, etc.

By default a Game Object is not enabled for physics. This is because not all Game Objects need to be. For example, a background image or game logo likely doesn't need to be affected by physics, but a player character does. Therefore, you must enable physics on the Game Objects that you specifically want to be affected by it. We will cover this in detail in later chapters.

Arcade Physics and Matter Physics are two separate systems. An Arcade Physics sprite, for example, cannot collide with a Matter Physics sprite. You cannot add the same Sprite to both systems, you need to pick one or the other. However, although it's unusual to do so, both systems can actually run in parallel in the same Scene. This means that you can have a Sprite that uses Arcade Physics and another that uses Matter Physics, and they will both work at the same time, although they will not interact together.

## Arcade World

The Arcade Physics World is the environment where all physics-based interactions occur within the Arcade Physics system. It manages the simulation of object movement, collisions, and responses to various forces. The Arcade Physics World tracks all the objects within it (referred to as "bodies"), handles their physical interactions, and updates their positions and velocities over time.

### Configuration

The Arcade Physics `config` object defines the behavior of the Arcade Physics system globally.

* Basic configuration object

```
Copyconst config = {
    // ...
    physics: {
        default: 'arcade'
    },
    // ...
};

const game = new Phaser.Game(config);

```

* Full configuration

```
Copyconst config = {
  // ...
  physics: {
    default: "arcade",
    arcade: {
      //    x: 0,
      //    y: 0,
      //    width: scene.sys.scale.width,
      //    height: scene.sys.scale.height,
      //    gravity: {
      //        x: 0,
      //        y: 0
      //    },
      //    checkCollision: {
      //        up: true,
      //        down: true,
      //        left: true,
      //        right: true
      //    },
      //    customUpdate: false,
      //    fixedStep: true,
      //    fps: 60,
      //    timeScale: 1,     // 2.0 = half speed, 0.5 = double speed
      //    customUpdate: false,
      //    overlapBias: 4,
      //    tileBias: 16,
      //    forceX: false,
      //    isPaused: false,
      //    debug: false,
      //    debugShowBody: true,
      //    debugShowStaticBody: true,
      //    debugShowVelocity: true,
      //    debugBodyColor: 0xff00ff,
      //    debugStaticBodyColor: 0x0000ff,
      //    debugVelocityColor: 0x00ff00,
      //    maxEntries: 16,
      //    useTree: true   // set false if amount of dynamic bodies > 5000
    },
  },
  // ...
};
const game = new Phaser.Game(config);

```

### Update

* Default updating : World updating every tick
* Custom updating :

  1. Set `customUpdate` of arcade config to `false`.

     + Enable world updating : `this.physics.enableUpdate()`
     + Disable world updating : `this.physics.disableUpdate()`
  2. Run world updating manually

     ```
     Copythis.physics.world.update(time, delta);

     ```
  3. Enable/disable world updating

     + Enable : `this.physics.enableUpdate()`
     + Disable : `this.physics.disableUpdate()`

#### Step

* Advances the simulation by a single step.

  ```
  Copythis.physics.world.singleStep();

  ```
* Advances the simulation by a time increment.

  ```
  Copythis.physics.world.step(delta);

  ```

### Control

#### Pause

```
Copythis.physics.pause();

```

#### Resume

```
Copythis.physics.resume();

```

#### Duration per frame

* Time scale

  ```
  Copythis.physics.world.timeScale = timeScale;

  ```

  + 1.0 = normal speed
  + 2.0 = half speed
  + 0.5 = double speed
* Frames per second (FPS)

  ```
  Copythis.physics.world.setFPS(framerate);

  ```

#### Tile filter options

```
Copyvar option = this.physics.world.tileFilterOptions;

```

* `option`

  ```
  Copy{
      isColliding: true,
      isNotEmpty: true,
      hasInterestingFace: true
  }

  ```

### Body

#### Enable

```
Copythis.physics.world.enable(gameObject);
// this.physics.world.enable(gameObject, bodyType);

```

* `gameObject` : A game object, or array of game objects, or game objects in a `Group`.
* `bodyType` :
  + `0` : Dynamic body. Default value.
  + `1` : Static body.

Or

```
Copythis.physics.add.existing(gameObject, bodyType);

```

See [arcade-body](#get-physics-body)

#### Disable

```
Copythis.physics.world.disable(gameObject);

```

* `gameObject` : A game object, or array of game objects, or game objects in a `Group`.

#### Add/remove body

* Add body to the local search trees.

  ```
  Copythis.physics.world.add(body);

  ```
* Remove body from the local search trees.

  ```
  Copythis.physics.world.disableBody(body);

  ```

### Collision

#### Set bound

See bound in [body object](#body-collision-bounds), or [game object](#game-object-collision-bounds).

#### Collider & callback

* Add collider

  + Push out

    ```
    Copythis.physics.add.collider(objectsA, objectsB);

    ```
  + Performs a collision check and separation between the two physics enabled objects given.

    ```
    Copyvar collider = this.physics.add.collider(
      objectsA,
      objectsB,
      collideCallback
    );
    // var collider = this.physics.add.collider(objectsA, objectsB, collideCallback, processCallback, callbackContext);

    ```
  + If you don't require separation then use `overlap` instead.

    ```
    Copyvar collider = this.physics.add.overlap(
      objectsA,
      objectsB,
      collideCallback
    );
    // var collider = this.physics.add.overlap(objectsA, objectsB, collideCallback, processCallback, callbackContext);

    ```
  + Parameters

    - `objectsA`, `objectsB` :

      * A game object
      * An array contains Game objects (Add or remove game objects)
      * Physics group/Group (Add or remove game objects)
      * An array contains Physics group/Group
    - `collideCallback` :

      ```
      Copyvar collideCallback = function (gameObject1, gameObject2) {
        // ...
      };

      ```
    - `processCallback` : Fired when gameObject1 intersects gameObject2, optional.

      ```
      Copyvar processCallback = function (gameObject1, gameObject2) {
        return true; // return false will discard remaining collision checking
      };

      ```
* Remove collider

  ```
  Copythis.physics.world.removeCollider(collider);

  ```
* Deactivate collider

  ```
  Copycollider.active = false; // Set true to activate again

  ```
* Name of collider (unused by engine)

  ```
  Copycollider.name = name;

  ```

#### Testing without colliders

* Test overlapping

  ```
  Copyvar isOverlapping = this.physics.world.overlap(object1, object2);

  ```

  or

  ```
  Copyvar isOverlapping = this.physics.world.overlap(
    object1,
    object2,
    collideCallback
  );
  // var isOverlapping = this.physics.world.overlap(object1, object2, collideCallback, processCallback, callbackContext);

  ```
* Test colliding, also push out

  ```
  Copyvar isCollided = this.physics.world.collide(object1, object2);

  ```

  or

  ```
  Copyvar isCollided = this.physics.world.collide(
    object1,
    object2,
    collideCallback
  );
  // var isCollided = this.physics.world.collide(object1, object2, collideCallback, processCallback, callbackContext);

  ```
* A body overlaps with a Tile and has its `onOverlap` property set to `true`.

  ```
  Copythis.physics.world.on("tileoverlap", function (gameObject, tile, body) {
    /* ... */
  });

  ```
* A body overlaps with a Tile and has its `onCollide` property set to `true`.

  ```
  Copythis.physics.world.on("tilecollide", function (gameObject, tile, body) {
    /* ... */
  });

  ```

### Arcade world bounds

#### Enable

* [Body](#arcade-body) : Set `body.setCollideWorldBounds()` to enable worldBounds property.
* World :

  + Set bounds [rectangle](../geometry.md) and enable bounds

    ```
    Copythis.physics.world.setBounds(x, y, width, height);
    // this.physics.world.setBounds(x, y, width, height, checkLeft, checkRight, checkUp, checkDown);

    ```
  + Set bounds [rectangle](../geometry.md)

    ```
    Copythis.physics.world.bounds.setTo(x, y, width, height);

    ```

    or

    ```
    Copythis.physics.world.bounds.x = x;
    this.physics.world.bounds.y = y;
    this.physics.world.bounds.width = width;
    this.physics.world.bounds.height = height;

    ```
  + Enable bounds

    ```
    Copythis.physics.world.setBoundsCollision();
    // this.physics.world.setBoundsCollision(left, right, up, down);

    ```

    or

    ```
    Copythis.physics.world.checkCollision.left = left;
    this.physics.world.checkCollision.right = right;
    this.physics.world.checkCollision.up = up;
    this.physics.world.checkCollision.down = down;

    ```
  + Get bounds [rectangle](../geometry.md)

    ```
    Copyvar top = this.physics.world.bounds.top;
    var bottom = this.physics.world.bounds.bottom;
    var left = this.physics.world.bounds.left;
    var right = this.physics.world.bounds.right;

    ```

### Bodies inside an area

* Overlap a rectangle area

  ```
  Copyvar bodies = this.physics.overlapRect(
    x,
    y,
    width,
    height,
    includeDynamic,
    includeStatic
  );

  ```

  + `includeDynamic` : Set `true` to search Dynamic Bodies
  + `includeStatic` : Set `true` to search Static Bodies
* Overlap a circle area

  ```
  Copyvar bodies = this.physics.overlapCirc(
    x,
    y,
    radius,
    includeDynamic,
    includeStatic
  );

  ```

  + `includeDynamic` : Set `true` to search Dynamic Bodies
  + `includeStatic` : Set `true` to search Static Bodies

### Wrap

```
Copythis.physics.world.wrap(gameObject, padding);

```

* gameObject:
  + game object
  + group
  + array of game objects

### Move to

* Move to position with a steady velocity

  ```
  Copythis.physics.moveTo(gameObject, x, y, speed, maxTime);

  ```
* Move to object with a steady velocity

  ```
  Copythis.physics.moveToObject(gameObject, destination, speed, maxTime);

  ```

### Accelerate to

* Accelerate to position

  ```
  Copythis.physics.accelerateTo(
    gameObject,
    x,
    y,
    acceleration,
    xSpeedMax,
    ySpeedMax
  );

  ```
* Accelerate to object

  ```
  Copythis.physics.accelerateToObject(
    gameObject,
    destination,
    acceleration,
    xSpeedMax,
    ySpeedMax
  );

  ```

### Gravity

* Set

  ```
  Copythis.physics.world.gravity.x = gx;
  this.physics.world.gravity.y = gy;

  ```
* Get

  ```
  Copyvar gx = this.physics.world.gravity.x;
  var gy = this.physics.world.gravity.y;

  ```

Total Gravity = world.gravity + body.gravity

### Bodies

#### Closest/furthest

* Closest

  ```
  Copyvar body = this.physics.closest(point); // point: {x,y}
  // var body = this.physics.closest(point, targets);

  ```

  + `targets` : Array of Arcade Physics Game Object, Body or Static Body.
* Furthest

  ```
  Copyvar body = this.physics.furthest(point); // point: {x,y}
  // var body = this.physics.furthest(point, targets);

  ```

  + `targets` : Array of Arcade Physics Game Object, Body or Static Body.

### Debug

#### Draw body & velocity

* Bounds of dynamic Body

  + Enable drawing body

    ```
    Copythis.physics.world.defaults.debugShowBody = true;

    ```
  + Color

    ```
    Copythis.physics.world.defaults.bodyDebugColor = 0xff00ff;

    ```
* Bounds of static Body

  + Enable drawing body

    ```
    Copythis.physics.world.defaults.debugShowStaticBody = true;

    ```
  + Color

    ```
    Copythis.physics.world.defaults.staticBodyDebugColor = 0x0000ff;

    ```
* Direction and magnitude of velocity

  + Enable drawing body

    ```
    Copythis.physics.world.defaults.debugShowVelocity = true;

    ```
  + Color

    ```
    Copythis.physics.world.defaults.velocityDebugColor = 0x00ff00;

    ```

#### Graphics

Draw debug body & velocity on a [Graphics object](../gameobjects/graphics.md).

```
Copyvar graphics = this.physics.world.debugGraphic;

```

* Set visible

  ```
  Copythis.physics.world.debugGraphic.setVisible();

  ```
* Set invisible

  ```
  Copythis.physics.world.debugGraphic.setVisible(false);

  ```

### Events

* World step

  ```
  Copythis.physics.world.on("worldstep", function (delta) {
    /* ... */
  });

  ```

  + `delta` : The delta time amount of this step, in seconds.
* Pause world

  ```
  Copythis.physics.world.on("pause", function () {
    /* ... */
  });

  ```
* Resume world

  ```
  Copythis.physics.world.on("resume", function () {
    /* ... */
  });

  ```
* Two bodies overlap and at least one of them has their `onOverlap` property set to `true`.

  ```
  Copythis.physics.world.on(
    "overlap",
    function (gameObject1, gameObject2, body1, body2) {
      /* ... */
    }
  );

  ```
* Two bodies overlap and at least one of them has their `onCollide` property set to `true`.

  ```
  Copythis.physics.world.on(
    "collide",
    function (gameObject1, gameObject2, body1, body2) {
      /* ... */
    }
  );

  ```
* A body overlaps with a Tile and has its `onOverlap` property set to `true`.

  ```
  Copythis.physics.world.on("tileoverlap", function (gameObject, tile, body) {
    /* ... */
  });

  ```
* A body overlaps with a Tile and has its `onCollide` property set to `true`.

  ```
  Copythis.physics.world.on("tilecollide", function (gameObject, tile, body) {
    /* ... */
  });

  ```
* World bounds

  ```
  Copythis.physics.world.on(
    "worldbounds",
    function (body, blockedUp, blockedDown, blockedLeft, blockedRight) {
      /* ... */
    }
  );

  ```

### Update loop

1. scene.sys.events: update
   1. Update position & angle of each body
   2. Process each collider
   3. Update final position of each body
   4. Emit `worldstep` event
2. scene.sys.events: postupdate
   1. Draw debug graphics

scene.sys.events: update  
  
Update arcade world  
gameObject.preUpdate()

scene.update()

scene.sys.events: postupdate  
  
Post update arcade world

Render

## Arcade Body

An Arcade Physics Body is associated with a game object and manages its physics properties and behaviors.

### Usage

#### Get physics body

1. [Enable physics world](#configuration)
2. Add existing game object(s) to physics world

   * Add a game object

     ```
     Copyvar gameObject = this.physics.add.existing(gameObject, bodyType);

     ```

     + `bodyType` :
       - `0` : Dynamic body
       - `1` : Static body
   * Add game objects

     ```
     Copythis.physics.world.enable(gameObjects, bodyType);

     ```

     + `gameObjects` : An array of game objects, or a group object
     + `bodyType` :
       - `0` : Dynamic body
       - `1` : Static body
3. Get physics body

   ```
   Copyvar body = gameObject.body;

   ```

#### Enable and disable

Whether this Body is updated by the physics simulation.

* Enable (default)

  ```
  Copybody.setEnable();

  ```

  or

  ```
  Copybody.enable = true;

  ```
* Disable

  ```
  Copybody.setEnable(false);

  ```

  or

  ```
  Copybody.enable = false;

  ```

#### Direct control

Enable `directControl` when game object is controlled by tween or dragging. Default behavior is disable.

* Enable

  ```
  Copybody.setDirectControl(); // default argument is true
  // body.setDirectControl(true);

  ```

  or

  ```
  Copybody.directControl = true;

  ```
* Disable

  ```
  Copybody.setDirectControl(false);

  ```

  or

  ```
  Copybody.directControl = false;

  ```

#### Immovable

Whether this Body can be moved by collisions with another Body.

* Enable

  ```
  Copybody.setImmovable();
  // body.immovable = true;

  ```
* Disable (defalut)

  ```
  Copybody.setImmovable(false);
  // body.immovable = false;

  ```
* Get

  ```
  Copyvar immovable = body.immovable;

  ```

#### Pushable

Sets if this Body can be pushed by another Body.

* Enable (default value of dynamic body)

  ```
  Copybody.pushable = true;

  ```
* Disable, reflect back all of the velocity it is given to the colliding body.

  ```
  Copybody.pushable = false;

  ```
* Get

  ```
  Copyvar pushable = body.pushable;

  ```

#### Moveable

Whether the Body's position and rotation are affected by its velocity, acceleration, drag, and gravity.

* Enable (default)

  ```
  Copybody.moves = true;

  ```
* Disable

  ```
  Copybody.moves = false;

  ```
* Get

  ```
  Copyvar moves = body.moves;

  ```

#### Destroy

Physics body will be destroyed automatically when game object is destroyed.

#### Movement

##### Velocity

* Set

  ```
  Copybody.setVelocity(x, y);

  ```

  or

  ```
  Copybody.setVelocityX(x);
  body.setVelocityY(x);

  ```
* Get

  ```
  Copyvar vx = body.velocity.x;
  var vy = body.velocity.y;

  ```

##### Max speed

* Set

  ```
  Copybody.setMaxSpeed(speed);

  ```
* Get

  ```
  Copyvar speed = body.maxSpeed;

  ```

##### Max velocity

* Set

  ```
  Copybody.setMaxVelocity(x, y);

  ```

  or

  ```
  Copybody.setMaxVelocityX(x);
  body.setMaxVelocityY(y);

  ```
* Get

  ```
  Copyvar vx = body.maxVelocity.x;
  var vy = body.maxVelocity.y;

  ```

##### Acceleration

* Set

  ```
  Copybody.setAcceleration(x, y);

  ```

  or

  ```
  Copybody.setAccelerationX(x);
  body.setAccelerationY(y);

  ```
* Get

  ```
  Copyvar ax = body.acceleration.x;
  var ay = body.acceleration.y;

  ```

##### Gravity

* Set

  ```
  Copybody.setGravity(x, y);

  ```

  or

  ```
  Copybody.setGravityX(x);
  body.setGravityY(y);

  ```
* Get

  ```
  Copyvar gx = body.gravity.x;
  var gy = body.gravity.y;

  ```
* Enables (default)

  ```
  Copybody.setAllowGravity();

  ```
* Disable

  ```
  Copybody.setAllowGravity(false);

  ```

##### Drag

Reduces speed per second.

* Set

  ```
  Copybody.setDrag(x, y);

  ```

  or

  ```
  Copybody.setDragX(x);
  body.setDragY(y);

  ```
* Get

  ```
  Copyvar dx = body.drag.x;
  var dy = body.drag.y;

  ```
* Enables (default)

  ```
  Copybody.setAllowDrag();

  ```
* Disable

  ```
  Copybody.setAllowDrag(false);

  ```
* Enable Damping (default: disable)

  ```
  Copybody.setDamping(true);
  // body.useDamping = true;

  ```

##### Slide factor

The Slide Factor controls how much velocity is preserved when this Body is pushed by another Body.

```
Copybody.slideFactor.set(x, y);

```

* `x`, `y` :
  + `1` : Take on all velocity given in the push. Default value.
  + `0` : Allow this Body to be pushed but then remain completely still after the push ends,
    such as you see in a game like *Sokoban*.
  + Other value between `0` ~ `1` : Keep `x`/`y` of the original velocity when the push ends.
    - Combine this with the `setDrag()` method to create deceleration.

##### Reset position

```
Copybody.reset(x, y);

```

##### Stop

Sets acceleration, velocity, and speed to zero.

```
Copybody.stop();

```

###### Friction

If this Body is `immovable` and in motion, this the proportion of this Body's movement received by the riding body on each axis.

* Set

  ```
  Copybody.setFriction(x, y);

  ```

  or

  ```
  Copybody.setFrictionX(x);
  body.setFrictionY(y);

  ```
* Get

  ```
  Copyvar fx = body.friction.x;
  var fy = body.friction.y;

  ```

##### Speed

* The absolute (non-negative) change in this Body's horizontal/vertical position from the previous step.

  ```
  Copyvar dx = body.deltaAbsX();
  var dy = body.deltaAbsY();

  ```

#### Rotation

##### Allow rotation

Whether this Body's rotation is affected by its angular acceleration and velocity.

* Enable (default)

  ```
  Copybody.setAllowRotation();

  ```
* Disable

  ```
  Copybody.setAllowRotation(false);

  ```
* Get

  ```
  Copyvar allowRotation = body.allowRotation;

  ```

##### Angular velocity

* Set

  ```
  Copybody.setAngularVelocity(v);

  ```
* Get

  ```
  Copyvar av = body.angularVelocity;

  ```

##### Angular acceleration

* Set

  ```
  Copybody.setAngularAcceleration(v);

  ```
* Get

  ```
  Copyvar aa = body.angularAcceleration;

  ```

##### Angular drag

Reduces angular speed per second.

* Set

  ```
  Copybody.setAngularDrag(v);

  ```
* Get

  ```
  Copyvar ad = body.angularDrag;

  ```

#### Collision

##### Collision category

By default all bodies collide with all other bodies. Collision categories define how different physics bodies interact with each other during collisions. It specifies which objects should collide and which should not. Collision categories are typically set using a bitmask, where each category is represented by a unique power of two. A body can collide with multiple collision categories.

* Collision category
  + Get

    ```
    Copyvar collisionCategory = body.collisionCategory;

    ```
  + Set

    ```
    Copybody.setCollisionCategory(category);

    ```

    - `category` :
      * `(1 << 0)`
      * `(1 << 1)`
      * `(1 << 2)`
      * ...
      * `(1 << 31)`
  + Reset collision category, to default behavior (all bodies collide with all others)

    ```
    Copybody.resetCollisionCategory();

    ```

    - Set `collisionCategory` to `1`.
    - Set `collisionMask` to `1`
* Collision mask
  + Get

    ```
    Copyvar collisionMask = body.collisionMask;

    ```
  + Set

    ```
    Copybody.setCollidesWith(categories);

    ```

    - `categories` : A single category value, or an array of them.
  + Add

    ```
    Copybody.addCollidesWith(category):

    ```

    - `category` : A single category value.
  + Remove

    ```
    Copybody.removeCollidesWith(category);

    ```

    - `category` : A single category value.

##### Body collision bounds

Collision bounds define the area used for collision detection.

* Rectangle

  ```
  Copybody.setSize(width, height, center);

  ```

  + `center` : `false` to set body's offset to (0, 0).
    - Not work in [Graphics](../gameobjects/graphics.md) object.
* Circle

  ```
  Copybody.setCircle(radius, offsetX, offsetY);

  ```

##### Collision Offset

Adjusts the position of a physics body's collision bounds relative to the sprite. Used when the sprite visual does not align with the collision area.

```
Copybody.setOffset(x, y);

```

##### Push out

Performs a collision check and separation between two physics enabled objects.

```
Copythis.physics.add.collider(objectsA, objectsB);

```

* `objectsA`, `objectsB` :
  + A game object
  + Game objects in array (Add or remove game objects)
  + Physics group (Add or remove game objects)
  + Group (Add or remove game objects)

##### Callbacks

Callbacks are functions that are called when collisions or overlaps occur between two objects every step.

```
Copyvar collider = this.physics.add.collider(objectsA, objectsB, collideCallback, processCallback, callbackContext);

```

* `collideCallback` : The callback to invoke when the two objects collide.
* `processCallback` : The callback to invoke when the two objects collide. Must return a boolean.
* `callbackContext` : The scope in which to call the callbacks.

##### Point inside

The `hitTest` function checks if a specific point in the game world is colliding with any physics bodies. It returns `true` if a collision has occurred and `false` otherwise.

```
Copyvar hit = body.hitTest(x, y);

```

##### Is colliding

* Is colliding this tick and which direction

  ```
  Copyvar isColliding = body.touching;

  ```

  + `isColliding` :

    ```
    Copy{
        none: true,
        up: true,
        down: true,
        left: true,
        right: true
    }

    ```
* The colliding body's touching value during the previous step.

  ```
  Copyvar wasColliding = body.wasTouching;

  ```

  + `wasColliding` :

    ```
    Copy{
        none: true,
        up: true,
        down: true,
        left: true,
        right: true
    }

    ```

##### Bounce

Defines how the body rebounds after colliding with another object. The bounce value is usually between 0 and 1. 0 stops the body from bouncing and makes it come to a stop upon collision. 1 makes the body will bounce back with the same velocity it had before the collision. A value greater than 1 makes increases the body's velocity after the collision.

* Set

  ```
  Copybody.setBounce(x, y);

  ```

  or

  ```
  Copybody.setBounceX(x); // horizontal bounce
  body.setBounceY(y); // vertical bounce

  ```
* Get

  ```
  Copyvar bx = body.bounce.x;
  var by = body.bounce.y;

  ```

##### Body world bounds

* [Default world bounds](#arcade-world-bounds)
* Custom world bounds :

  ```
  Copybody.setBoundsRectangle(bounds);

  ```

  + `bounds` : A [rectangle object](../../../docs/latest/Phaser.Geom.Rectangle.md).
* Enable

  ```
  Copybody.setCollideWorldBounds();

  ```
* Disable (default)

  ```
  Copybody.setCollideWorldBounds(false);

  ```
* Get world bounds [rectangle](../geometry.md)

  ```
  Copyvar top = body.world.bounds.top;
  var bottom = body.world.bounds.bottom;
  var left = body.world.bounds.left;
  var right = body.world.bounds.right;

  ```

##### Blocked

Check whether this Body is colliding with a tile or the world boundary.

* Blocked when moving down

  ```
  Copyvar onFloor = body.onFloor();
  // var onFloor = body.blocked.down

  ```
* Blocked when moving up

  ```
  Copyvar onCeiling = body.onCeiling();
  // var onCeiling = body.blocked.up

  ```
* Blocked when moving left or right

  ```
  Copyvar onWall = body.onWall();
  // var onLeftWall = body.blocked.left
  // var onRightWall = body.blocked.right

  ```
* State

  ```
  Copyvar blocked = body.blocked;

  ```

  + `blocked` :

    ```
    Copy{
        none: true,
        up: false,
        down: false,
        left: false,
        right: false
    }

    ```

#### Mass

The Body's inertia, relative to a default unit (1). With bounce, this affects the exchange of momentum (velocities) during collisions.

* Set

  ```
  Copybody.setMass(m);

  ```
* Get

  ```
  Copyvar m = body.mass;

  ```

#### Static body

A Static Arcade Physics Body never moves, and isn't automatically synchronized with its parent Game Object. Any changeg made to the parent's origin, position, or scale after creating or adding the body, requires manual update to the Static Body. A Static Body can collide with other Bodies, but is never moved by collisions.

##### Sync

Syncs the Bodies *position* and *size* with its parent Game Object.

```
Copybody.updateFromGameObject();

```

#### Debug

Draws a graphical representation of the StaticBody for visual debugging purposes.

* Bounds of Body

  + Enable drawing body

    ```
    Copybody.debugShowBody = true;

    ```
  + Color

    ```
    Copybody.debugBodyColor = 0xff00ff;

    ```
* Direction and magnitude of velocity

  + Enable drawing body

    ```
    Copybody.debugShowVelocity = true;

    ```

## Arcade Game Object

Game Objects are the building blocks of your game. Common Arcade Game Objects include: Sprites, Images, and Groups.

### Usage

#### Adding Game Objects

##### Image object

* Static object, extends from [Image object](../../../docs/latest/Phaser.Physics.Arcade.Image.md)

  ```
  Copyvar image = this.physics.add.staticImage(x, y, key);

  ```
* Dynamic object, extends from [Image object](../../../docs/latest/Phaser.Physics.Arcade.Image.md)

  ```
  Copyvar image = this.physics.add.image(x, y, key);

  ```

##### Sprite object

* Static object, extends from [Sprite object](../../../docs/latest/Phaser.Physics.Arcade.Sprite.md)

  ```
  Copyvar image = this.physics.add.staticSprite(x, y, key, frame);

  ```
* Dynamic object, extends from [Sprite object](../../../docs/latest/Phaser.Physics.Arcade.Sprite.md)

  ```
  Copyvar image = this.physics.add.sprite(x, y, key, frame);

  ```

##### Group object

* Static sprite objects, extends from [Group object](../../../docs/latest/Phaser.Physics.Arcade.Group.md)

  ```
  Copyvar group = this.physics.add.staticGroup(children, config);
  // var group = this.physics.add.staticGroup(config);

  ```
* Dynamic sprite objects, extends from [Group object](../../../docs/latest/Phaser.Physics.Arcade.Group.md)

  ```
  Copyvar group = this.physics.add.group(children, config);
  // var group = this.physics.add.staticGroup(config);

  ```

  + `config`

    ```
    Copyvar config = {
      classType: ArcadeSprite,
      enable: true,
      collideWorldBounds: false,
      customBoundsRectangle: null,
      accelerationX: 0,
      accelerationY: 0,
      allowDrag: true,
      allowGravity: true,
      allowRotation: true,
      useDamping: false,
      bounceX: 0,
      bounceY: 0,
      dragX: 0,
      dragY: 0,
      gravityX: 0,
      gravityY: 0,
      frictionX: 0,
      frictionY: 0,
      maxSpeed: -1,
      velocityX: 0,
      velocityY: 0,
      maxVelocityX: 10000,
      maxVelocityY: 10000,
      angularVelocity: 0,
      angularAcceleration: 0,
      angularDrag: 0,
      mass: 0,
      immovable: false,

      maxSize: -1,
      runChildUpdate: false,
    };

    ```

##### Enable body

* Enable body

  ```
  CopygameObject.enableBody();
  // gameObject.enableBody(false, 0, 0, enableGameObject, showGameObject);

  ```

  + Enable and reset position

    ```
    CopygameObject.enableBody(true, x, y);
    // gameObject.enableBody(true, x, y, enableGameObject, showGameObject);

    ```
  + `enableGameObject` : Also activate this Game Object.
  + `showGameObject` : Also show this Game Object.
* Disable body

  ```
  CopygameObject.disableBody();
  // gameObject.disableBody(disableGameObject, hideGameObject);

  ```

  + `disableGameObject` : Also deactivate this Game Object.
  + `hideGameObject` : Also hide this Game Object.

#### Movement

##### Velocity

* Set

  ```
  CopygameObject.setVelocity(x, y);

  ```

  or

  ```
  CopygameObject.setVelocityX(x);
  gameObject.setVelocityY(y);

  ```
* Get

  ```
  Copyvar vx = gameObject.body.velocity.x;
  var vy = gameObject.body.velocity.y;

  ```

###### Max velocity

* Set

  ```
  CopygameObject.setMaxVelocity(x, y);

  ```
* Get

  ```
  Copyvar vx = gameObject.body.maxVelocity.x;
  var vy = gameObject.body.maxVelocity.y;

  ```

##### Acceleration

* Set

  ```
  CopygameObject.setAcceleration(x, y);

  ```

  or

  ```
  CopygameObject.setAccelerationX(x);
  gameObject.setAccelerationY(y);

  ```
* Get

  ```
  Copyvar ax = gameObject.body.acceleration.x;
  var ay = gameObject.body.acceleration.y;

  ```

###### Gravity

* Set

  ```
  CopygameObject.setGravity(x, y);

  ```

  or

  ```
  CopygameObject.setGravityX(x);
  gameObject.setGravityY(y);

  ```
* Get

  ```
  Copyvar gx = gameObject.body.gravity.x;
  var gy = gameObject.body.gravity.y;

  ```

##### Drag

* Set

  ```
  CopygameObject.setDrag(x, y);

  ```

  or

  ```
  CopygameObject.setDragX(x);
  gameObject.setDragY(y);

  ```
* Get

  ```
  Copyvar dx = gameObject.body.drag.x;
  var dy = gameObject.body.drag.y;

  ```
* Enable damping

  ```
  CopygameObject.setDamping(value);

  ```

##### Immovable

* Enable

  ```
  CopygameObject.setImmovable();

  ```
* Disable

  ```
  CopygameObject.setImmovable(false);

  ```
* Get

  ```
  Copyvar immovable = gameObject.body.immovable;

  ```

##### Pushable

* Enable

  ```
  CopygameObject.setPushable();

  ```
* Disable

  ```
  CopygameObject.setPushable(false);

  ```
* Get

  ```
  Copyvar pushable = gameObject.body.pushable;

  ```

###### Slide factor

The Slide Factor controls how much velocity is preserved when this Body is pushed by another Body.

```
CopygameObject.setSlideFactor(x, y);

```

* `x`, `y` :
  + `1` : Take on all velocity given in the push. Default value.
  + `0` : Allow this Body to be pushed but then remain completely still after the push ends,
    such as you see in a game like *Sokoban*.
  + Other value between `0` ~ `1` : Keep `x`/`y` of the original velocity when the push ends.
    - Combine this with the `setDrag()` method to create deceleration.

###### Friction

If this Body is `immovable` and in motion, this the proportion of this Body's movement received by the riding body on each axis.

* Set

  ```
  CopygameObject.setFriction(x, y);

  ```

  or

  ```
  CopygameObject.setFrictionX(x);
  gameObject.setFrictionY(y);

  ```
* Get

  ```
  Copyvar fx = gameObject.body.friction.x;
  var fy = gameObject.body.friction.y;

  ```

##### Direct control

Enable `directControl` when game object is controlled by tween or dragging. Default behavior is disable.

* Enable

  ```
  CopygameObject.setDirectControl();
  // gameObject.setDirectControl(true);

  ```
* Disable

  ```
  CopygameObject.setDirectControl(false);

  ```

!!! note "Use case"
Enable `setDirectControl` when game object is controlled by tween or dragging.

#### Rotation

##### Allow rotation

Whether this Body's rotation is affected by its angular acceleration and velocity.

* Enable (default)

  ```
  Copybody.setAllowRotation();

  ```
* Disable

  ```
  Copybody.setAllowRotation(false);

  ```
* Get

  ```
  Copyvar allowRotation = gameObject.body.allowRotation;

  ```

##### Angular velocity

* Set

  ```
  CopygameObject.setAngularVelocity(v);

  ```
* Get

  ```
  Copyvar av = gameObject.body.angularVelocity;

  ```

##### Angular acceleration

* Set

  ```
  CopygameObject.setAngularAcceleration(v);

  ```
* Get

  ```
  Copyvar aa = gameObject.body.angularAcceleration;

  ```

##### Angular drag

* Set

  ```
  CopygameObject.setAngularDrag(v);

  ```
* Get

  ```
  Copyvar ad = gameObject.body.angularDrag;

  ```

#### Collision

##### Collision category

By default all bodies collide with all other bodies. Collision categories define how different physics bodies interact with each other during collisions. It specifies which objects should collide and which should not. Collision categories are typically set using a bitmask, where each category is represented by a unique power of two. A body can collide with multiple collision categories.

* Collision category
  + Get

    ```
    Copyvar collisionCategory = gameObject.body.collisionCategory;

    ```
  + Set

    ```
    CopygameObject.setCollisionCategory(category);

    ```

    - `category` :
      * `(1 << 0)`
      * `(1 << 1)`
      * `(1 << 2)`
      * ...
      * `(1 << 31)`
  + Reset collision category, to default behavior (all bodies collide with all others)

    ```
    CopygameObject.resetCollisionCategory();

    ```

    - Set `collisionCategory` to `1`.
    - Set `collisionMask` to `1`
* Collision mask
  + Get

    ```
    Copyvar collisionMask = gameObject.body.collisionMask;

    ```
  + Set

    ```
    CopygameObject.setCollidesWith(categories);

    ```

    - `categories` : A single category value, or an array of them.
  + Add

    ```
    CopygameObject.addCollidesWith(category):

    ```

    - `category` : A single category value.
  + Remove

    ```
    CopygameObject.removeCollidesWith(category);

    ```

    - `category` : A single category value.

##### Game Object collision bounds

Collision bounds define the area used for collision detection.

* Rectangle

  ```
  CopygameObject.setBodySize(width, height, center);

  ```

  + `center` : `false` to set body's offset to (0, 0)
* Circle

  ```
  CopygameObject.setCircle(radius, offsetX, offsetY);

  ```

###### Offset

```
CopygameObject.setOffset(x, y);

```

##### Push out

Performs a collision check and separation between two physics enabled objects.

```
Copythis.physics.add.collider(objectsA, objectsB);

```

* `objectsA`, `objectsB` :
  + A game object
  + Game objects in array (Add or remove game objects)
  + Physics group (Add or remove game objects)
  + Group (Add or remove game objects)

##### Callbacks

Callbacks are functions that are called when collisions or overlaps occur between two objects every step.

```
Copyvar collider = this.physics.add.collider(objectsA, objectsB, collideCallback, processCallback, callbackContext);

```

* `collideCallback` : The callback to invoke when the two objects collide.
* `processCallback` : The callback to invoke when the two objects collide. Must return a boolean.
* `callbackContext` : The scope in which to call the callbacks.

#### Point inside

The `hitTest` function checks if a specific point in the game world is colliding with any physics bodies. It returns `true` if a collision has occurred and `false` otherwise.

```
Copyvar hit = gameObject.hitTest(x, y);

```

##### Bounce

* Set

  ```
  CopygameObject.setBounce(x, y);

  ```

  or

  ```
  CopygameObject.setBounceX(x);
  gameObject.setBounceY(y);

  ```
* Get

  ```
  Copyvar bx = gameObject.body.bounce.x;
  var by = gameObject.body.bounce.y;

  ```
* Enable bounce when colliding with the world boundary

  ```
  CopygameObject.setCollideWorldBounds();

  ```
* Disable bounce when colliding with the world boundary

  ```
  CopygameObject.setCollideWorldBounds(false);

  ```

#### Mass

The Body's inertia, relative to a default unit (1). With bounce, this affects the exchange of momentum (velocities) during collisions.

* Set

  ```
  CopygameObject.setMass(m);

  ```
* Get

  ```
  Copyvar m = gameObject.body.mass;

  ```

#### Static game object

##### Sync

Syncs the Bodies position and size in static game object.

```
CopygameObject.refreshBody();

```

#### Methods of group

```
Copygroup.setVelocity(x, y, step);

```

```
Copygroup.setVelocityX(value, step);

```

```
Copygroup.setVelocityY(value, step);

```

```
Copygroup.refresh(); // call this method when position of game objects were changed in static object group

```

#### Debug

Draws a graphical representation of the Game Object for visual debugging purposes.

```
CopygameObject.setDebug(showBody, showVelocity, bodyColor);

```

```
CopygameObject.setDebugBodyColor(bodyColor);

```

## Author Credits

Content on this page includes work by:

* [RexRainbow](https://github.com/rexrainbow)

Updated on June 4, 2025, 1:16 PM UTC

---

[Physics](../physics.md)

[Matter Physics](matter.md)

On this page

* [Arcade Physics](#arcade-physics)

  + [Arcade World](#arcade-world)

    - [Configuration](#configuration)
    - [Update](#update)
    - [Control](#control)
    - [Body](#body)
    - [Collision](#collision)
    - [Arcade world bounds](#arcade-world-bounds)
    - [Bodies inside an area](#bodies-inside-an-area)
    - [Wrap](#wrap)
    - [Move to](#move-to)
    - [Accelerate to](#accelerate-to)
    - [Gravity](#gravity)
    - [Bodies](#bodies)
    - [Debug](#debug)
    - [Events](#events)
    - [Update loop](#update-loop)
  + [Arcade Body](#arcade-body)

    - [Usage](#usage)
  + [Arcade Game Object](#arcade-game-object)

    - [Usage](#usage-1)
  + [Author Credits](#author-credits)

Back to top

©2025[Phaser](../../../index.md)



Arcade Physics