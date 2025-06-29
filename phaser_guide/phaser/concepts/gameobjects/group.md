# Group

A Guide to the Phaser Group to manage Game Objects collections

A Group is a way for you to create, manipulate, or recycle similar Game Objects. Group membership is non-exclusive. A Game Object can belong to several groups, one group, or none.

Groups themselves aren't displayable, and can't be positioned, rotated, scaled, or hidden.

## Add group object

```
Copyvar group = this.add.group(config);
// var group = this.add.group(gameObjects, config);  // Add game objects into group

```

* `config`

  ```
  Copy{
      classType: Phaser.GameObjects.Sprite,
      defaultKey: null,
      defaultFrame: null,
      active: true,
      maxSize: -1,
      runChildUpdate: false,
      createCallback: null,
      removeCallback: null,
      createMultipleCallback: null
  }

  ```

  + `classType` :

    - [Sprite](sprite.md) : `Phaser.GameObjects.Sprite`
    - [Image](image.md) : `Phaser.GameObjects.Image`
  + `runChildUpdate` : Set `true` to run `gameObject.update()` every tick.
  + `createCallback` : A function to be called when adding or creating group members.

    ```
    Copyvar callback = function(gameObject) {
    }

    ```
  + `removeCallback` : A function to be called when removing group members.

    ```
    Copyvar callback = function(gameObject) {
    }

    ```
  + `createMultipleCallback` : A function to be called when creating several group members at once.

    ```
    Copyvar callback = function(gameObjects) {
    }

    ```

## Add game object

```
Copygroup.add(gameObject);
// group.add(gameObject, true);  // add this game object to display and update list of scene

```

```
Copygroup.addMultiple(gameObjects);   // array of game objects
// group.addMultiple(gameObjects, true);

```

* Game object will only be added once.
* Game object will be removed automatically when destroyed.

## Remove game object

```
Copygroup.remove(gameObject);
// group.remove(gameObject, true);  // also remove this game object from display and update list of scene

```

Remove all game objects

```
Copygroup.clear();
// group.clear(removeFromScene, destroyChild);

```

## Get game objects

* Get all game objects.

  ```
  Copyvar gameObjects = group.getChildren();  // array of game objects

  ```
* Get all matching game objects

  ```
  Copyvar gameObjects = group.getMatching(property, value);
  // var gameObjects = group.getMatching(property, value, startIndex, endIndex);

  ```
* Amount of game objects.

  ```
  Copyvar len = group.getLength();

  ```
* Group is full. Maximun size is set in `maxSize`.

  ```
  Copyvar isFull = group.isFull();

  ```
* Game object is in group.

  ```
  Copyvar isInGroup = group.contains(child);

  ```

## Group actions

### Property

* Set property

  ```
  Copygroup.propertyValueSet(key, value);
  // group.propertyValueSet(key, value, step, index, direction);

  ```

  + `direction` :
    - `1` : From beginning to end
    - `-1` : From end to beginning
* Increase property

  ```
  Copygroup.propertyValueInc(key, value);
  // group.propertyValueInc(key, value, step, index, direction);

  ```

  + `direction` :
    - `1` : From beginning to end
    - `-1` : From end to beginning

### Position

* Set Position

  ```
  Copygroup.setX(value);
  // group.setX(value, step);
  group.setX(value);
  // group.setY(value, step);
  group.setXY(x, y);
  // group.setXY(x, y, stepX, stepY);

  ```
* Increase Position

  ```
  Copygroup.incX(value);
  // group.incX(value, step);
  group.incY(value);
  // group.incY(value, step);
  group.incXY(x, y);
  // group.incXY(x, y, stepX, stepY);

  ```
* Shift position

  ```
  Copygroup.shiftPosition(x, y);
  // group.shiftPosition(x, y, direction);

  ```

  + `direction` :
    - `0` : First to last
    - `1` : Last to first

### Angle

* Set angle

  ```
  Copygroup.angle(value);
  // group.angle(value, step);

  ```

  or

  ```
  Copygroup.rotate(value);
  // group.rotate(value, step);

  ```
* Rotate around

  ```
  Copygroup.rotateAround(point, angle);

  ```

  or

  ```
  Copygroup.rotateAroundDistance(point, angle, distance);

  ```

### Visible

* Set visible

  ```
  Copygroup.setVisible(value);
  // group.setVisible(value, index, direction);

  ```

  + `index` : An optional offset to start searching from within the items array.
  + `direction` : The direction to iterate through the array.
    - `1` : From beginning to end
    - `-1` : From end to beginning
* Toggle visible

  ```
  Copygroup.toggleVisible();

  ```

### Alpha

* Set alpha

  ```
  Copygroup.setAlpha(value);
  // group.setAlpha(value, step);

  ```

### Tint

* Set tint

  ```
  Copygroup.setTint(value);
  // group.setTint(topLeft, topRight, bottomLeft, bottomRight);

  ```

### Blend mode

* Set [blend mode](../display.md)

  ```
  Copygroup.setBlendMode(value);

  ```

### Scale

* Set scale

  ```
  Copygroup.scaleX(value);
  // group.scaleX(value, step);
  group.scaleY(value);
  // group.scaleY(value, step);
  group.scaleXY(scaleX, scaleY);
  // group.scaleXY(scaleX, scaleY, stepX, stepY);

  ```

### Origin

* Set origin

  ```
  Copygroup.setOrigin(originX, originY);
  // group.setOrigin(originX, originY, stepX, stepY);

  ```

### Depth

* Set depth

  ```
  Copygroup.setDepth(value, step);

  ```

### Animation

* Play animation

  ```
  Copygroup.playAnimation(key, startFrame);

  ```

### Hit area

* Set hit-area

  ```
  Copygroup.setHitArea();
  // group.setHitArea(hitArea, hitAreaCallback);

  ```

### Shuffle

* Shuffle array

  ```
  Copygroup.shuffle();

  ```

## Active/inactive game objects

* Set inactive

  ```
  Copygroup.kill(gameObject);         // gameObject.setActive(false)
  group.killAndHide(gameObject);  // gameObject.setActive(false).setVisible(false)

  ```
* Amount of active game objects

  ```
  Copyvar activeCount = group.countActive();

  ```

  or

  ```
  Copyvar activeCount = group.getTotalUsed();

  ```
* Amount of active game objects

  ```
  Copyvar inactiveCount = group.countActive(false);

  ```
* Amount of free (maxSize - activeCount) game objects

  ```
  Copyvar freeCount = group.getTotalFree();  // group.maxSize - group.getTotalUsed()

  ```
* Get first active/inactive game object,

  + Return `null` if no game object picked.

    ```
    Copyvar gameObject = group.getFirst(active);  // active = true/false
    var gameObject = group.getFirstAlive(); // Equal to group.getFirst(true, ...)
    var gameObject = group.getFirstDead(); // Equal to group.getFirst(false, ...)

    ```
  + Create one if no game object picked.

    ```
    Copyvar gameObject = group.getFirst(active, true, x, y, key, frame, visible);  // active = true/false
    var gameObject = group.getFirstAlive(true, x, y, key, frame, visible); // Equal to group.getFirst(true, ...)
    var gameObject = group.getFirstDead(true, x, y, key, frame, visible); // Equal to group.getFirst(false, ...)
    var gameObject = group.get(x, y, key, frame, visible); // Equal to group.getFirst(false, true, ...)

    ```

    - Use (`x`, `y`, `key`, `frame`) to create [Image](image.md)/[Sprite](sprite.md) game object.

    ```
    Copyvar newGameObject = new GameObjectClass(x, y, key, frame);

    ```

## Create game objects

```
Copyvar gameObjects = group.createFromConfig(config);
var gameObjects = group.createMultiple(config);    // config in array

```

* `config`

  ```
  Copy{
      classType: this.classType,
      key: undefined,             // Required
      frame: null,
      visible: true,
      active: true,
      repeat: 0,                  // Create (1 + repeat) game objects
      createCallback: undefined,  // Override this.createCallback if not undefined

      // Position
      setXY: {
          x:0,
          y:0,
          stepX:0,
          stepY:0
      },
      // Actions.SetXY(gameObjects, x, y, stepX, stepY)
      gridAlign: false,
      // {
      //     width: -1,
      //     height: -1,
      //     cellWidth: 1,
      //     cellHeight: 1,
      //     position: Phaser.Display.Align.TOP_LEFT,
      //     x: 0,
      //     y: 0
      // }
      // Actions.GridAlign(gameObjects, gridAlign)

      // Angle
      setRotation: {
          value: 0,
          step:
      },
      // Actions.SetRotation(gameObjects, value, step)

      // Scale
      setScale: {
          x:0,
          y:0,
          stepX:0,
          stepY:0
      },
      // Actions.SetScale(gameObjects, x, y, stepX, stepY)

      // Alpha
      setAlpha: {
          value: 0,
          step:
      },
      // Actions.SetAlpha(gameObjects, value, step)

      setOrigin: {
          x:0,
          y:0,
          stepX:0, 
          stepY:0
      },

      // Input
      hitArea: null,
      hitAreaCallback: null,
      // Actions.SetHitArea(gameObjects, hitArea, hitAreaCallback)
  }

  ```

  + `classType` :
    - [Sprite](sprite.md): `Phaser.GameObjects.Sprite`
    - [Image](image.md): `Phaser.GameObjects.Image`

## Destroy

* Destroy group only

  ```
  Copygroup.destroy();

  ```
* Destroy group and children

  ```
  Copygroup.destroy(true);

  ```

## Author Credits

Content on this page includes work by:

* [RexRainbow](https://github.com/rexrainbow)

Updated on June 4, 2025, 1:16 PM UTC

---

[Graphics](graphics.md)

[Image](image.md)

On this page

* [Group](#group)

  + [Add group object](#add-group-object)
  + [Add game object](#add-game-object)
  + [Remove game object](#remove-game-object)
  + [Get game objects](#get-game-objects)
  + [Group actions](#group-actions)

    - [Property](#property)
    - [Position](#position)
    - [Angle](#angle)
    - [Visible](#visible)
    - [Alpha](#alpha)
    - [Tint](#tint)
    - [Blend mode](#blend-mode)
    - [Scale](#scale)
    - [Origin](#origin)
    - [Depth](#depth)
    - [Animation](#animation)
    - [Hit area](#hit-area)
    - [Shuffle](#shuffle)
  + [Active/inactive game objects](#activeinactive-game-objects)
  + [Create game objects](#create-game-objects)
  + [Destroy](#destroy)
  + [Author Credits](#author-credits)

Back to top

©2025[Phaser](../../../index.md)