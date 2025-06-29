# Container

A Guide to the Phaser Container Game Object

A Container, as the name implies, can 'contain' other types of Game Object. When a Game Object is added to a Container, the Container becomes responsible for the rendering of it. By default it will be removed from the Display List and instead added to the Containers own internal list.

The position of the Game Object automatically becomes relative to the position of the Container.

The transform point of a Container is [0, 0] (local space) and that cannot be changed. The children you add to the Container should be positioned with this value in mind. I.e. you should treat [0, 0] as being the *center* of the Container, and position children positively and negative around it as required.

When the Container is rendered, all of its children are rendered as well, in the order in which they exist within the Container. Container children can be repositioned using methods such as MoveUp, MoveDown and SendToBack.

If you modify a transform property of the Container, such as Container.x or Container.rotation then it will automatically influence all children as well.

Containers can include other Containers for deeply nested transforms.

Containers can have masks set on them and can be used as a mask too. However, Container children cannot be masked. The masks do not 'stack up'. Only a Container on the root of the display list will use its mask.

Containers can be enabled for input. Because they do not have a texture you need to provide a shape for them to use as their hit area. Container children can also be enabled for input, independent of the Container.

If input enabling a child you should not set both the origin and a negative scale factor on the child, or the input area will become misaligned.

Containers can be given a physics body for either Arcade Physics, Impact Physics or Matter Physics. However, if Container children are enabled for physics you may get unexpected results, such as offset bodies, if the Container itself, or any of its ancestors, is positioned anywhere other than at 0 x 0. Container children with physics do not factor in the Container due to the excessive extra calculations needed. Please structure your game to work around this.

It's important to understand the impact of using Containers. They add additional processing overhead into every one of their children. The deeper you nest them, the more the cost escalates. This is especially true for input events. You also loose the ability to set the display depth of Container children in the same flexible manner as those not within them. In short, don't use them for the sake of it. You pay a small cost every time you create one, try to structure your game around avoiding that where possible.

## Add container

```
Copyvar container = this.add.container(x, y);
// var container = this.add.container(x, y, children); // children: an array of game object

```

## Custom class

* Define class

  ```
  Copyclass MyContainer extends Phaser.GameObjects.Container {
      constructor(scene, x, y, children) {
          super(scene, x, y, children);
          // ...
          this.add.existing(this);
      }
      // ...

      // preUpdate(time, delta) {}
  }

  ```

  + `this.add.existing(gameObject)` : Adds an existing Game Object to this Scene.
    - If the Game Object renders, it will be added to the Display List.
    - If it has a `preUpdate` method, it will be added to the Update List.
* Create instance

  ```
  Copyvar container = new MyContainer(scene, x, y, children);

  ```

## Destroy container

```
Copycontainer.destroy();

```

Also destroy all children game objects.

## Set properties

Reference [game object](../gameobjects.md), to set position, angle, visible, alpha, etc...

## Set size

```
Copycontainer.setSize(width, height);

```

Default `width` and `height` is 0.

## Set scroll factor

```
Copycontainer.setScrollFactor(x, y);

```

Apply this scrollFactor to all Container children.

```
Copycontainer.setScrollFactor(x, y, true);

```

## Hit area

```
Copycontainer.setInteractive(new Phaser.Geom.Circle(0, 0, radius), Phaser.Geom.Circle.Contains);
// container.setInteractive(false); // disable

```

Assign hit area with a circle shape.

## Non-exclusive

```
Copycontainer.setExclusive(false);

```

Allows a game object added to container many times.

## Children

### Add child

```
Copycontainer.add(child);  // child: a game object or an array of game objects

```

```
Copycontainer.addAt(child, index);

```

### Child exists in container

```
Copyvar hasChild = container.exists(child);

```

### Get child

```
Copyvar firstChild = container.first;
var nextChild = container.next;
var prevChild = container.previous;
var lastChild = container.last;

```

```
Copyvar child = container.getByName(name);

```

```
Copyvar child = container.getRandom(startIndex, length);

```

```
Copyvar child = container.getFirst(property, value, startIndex, endIndex);
// value: the value to test the property against. Must pass a strict (`===`) comparison check.

```

```
Copyvar children = container.getAll(property, value, startIndex, endIndex);
// value: the value to test the property against. Must pass a strict (`===`) comparison check.

```

```
Copyvar amount = container.count(property, value, startIndex, endIndex);
// value: the value to test the property against. Must pass a strict (`===`) comparison check.

```

### Sort children

Sort the contents of this Container so the items are in order based on the given property. For example: `sort('alpha')` would sort the elements based on the value of their alpha property.

```
Copycontainer.sort(property);

```

```
Copycontainer.sort(property, function(childA, childB){
    return 0; // 0, 1, -1
});

```

### Remove child

```
Copycontainer.remove(child);
// container.remove(child, true);  // remove child object and destroy it

```

```
Copycontainer.removeAt(index);
// container.removeAt(index, true);  // remove child object and destroy it

```

```
Copycontainer.removeBetween(startIndex, endIndex);
// container.removeBetween(startIndex, endIndex, true);  // remove children objects and destroy them

```

```
Copycontainer.removeAll();
// container.removeAll(true);  // remove all children objects and destroy them

```

Removing child from container without destroying will put back into scene's display list.

### Order of child

```
Copycontainer.moveTo(child, index);

```

```
Copycontainer.bringToTop(child);

```

```
Copycontainer.sendToBack(child);

```

```
Copycontainer.moveUp(child);

```

```
Copycontainer.moveDown(child);

```

```
Copycontainer.moveAbove(child1, child2);  // Move child1 above child2

```

```
Copycontainer.moveBelow(child1, child2);  // Move child1 below child2

```

```
Copycontainer.swap(child1, child2);

```

```
Copycontainer.reverse();

```

```
Copycontainer.shuffle();

```

### Replace child

```
Copycontainer.replace(oldChild, newChild);
// container.replace(oldChild, newChild, true);  // destroy oldChild

```

### Set properties

```
Copycontainer.setAll(property, value, startIndex, endIndex);

```

### For each child

* Iterate current children list

  ```
  Copycontainer.iterate(callback);
  // container.iterate(callback, context);
  // container.iterate(callback, context, arg0, arg1, ...);

  ```

  + `callback` :

    ```
    Copy```javascript
    function(child, arg0, arg1, ...) {

    }
    ```

    ```
* Iterate a copy of current children list

  ```
  Copycontainer.each(callback);
  // container.each(callback, context);
  // container.each(callback, context, arg0, arg1, ...);

  ```

  + `callback` :

    ```
    Copy```javascript
    function(child, arg0, arg1, ...) {

    }
    ```

    ```

### Get world position, rotation, scale

```
Copyvar matrix = child.getWorldTransformMatrix();
var x = matrix.tx;
var y = matrix.ty;
var rotation = matrix.rotation;
var scaleX = matrix.scaleX;
var scaleY = matrix.scaleY;

```

## Other properties

See [game object](../gameobjects.md)

## Create mask

```
Copyvar mask = container.createBitmapMask();

```

See [mask](../display.md)

## Shader effects

Support [postFX effects](shader.md)

!!! note
No preFX effect support

## Compare with [group object](group.md)

* Container and group objects are all have a children list.
* Container has position, angle, alpha, visible, ...etc, but group does not have.
* Container controls properties of children (position, angle, alpha, visible, ...etc), but group won't.
* A game object could be added to many groups, but it only could be added to one container (`exclusive` mode).

## Author Credits

Content on this page includes work by:

* [RexRainbow](https://github.com/rexrainbow)

Updated on June 4, 2025, 1:16 PM UTC

---

[Blitter](blitter.md)

[Display List](display-list.md)

On this page

* [Container](#container)

  + [Add container](#add-container)
  + [Custom class](#custom-class)
  + [Destroy container](#destroy-container)
  + [Set properties](#set-properties)
  + [Set size](#set-size)
  + [Set scroll factor](#set-scroll-factor)
  + [Hit area](#hit-area)
  + [Non-exclusive](#non-exclusive)
  + [Children](#children)

    - [Add child](#add-child)
    - [Child exists in container](#child-exists-in-container)
    - [Get child](#get-child)
    - [Sort children](#sort-children)
    - [Remove child](#remove-child)
    - [Order of child](#order-of-child)
    - [Replace child](#replace-child)
    - [Set properties](#set-properties-1)
    - [For each child](#for-each-child)
    - [Get world position, rotation, scale](#get-world-position-rotation-scale)
  + [Other properties](#other-properties)
  + [Create mask](#create-mask)
  + [Shader effects](#shader-effects)
  + [Compare with group object](#compare-with-group-object)
  + [Author Credits](#author-credits)

Back to top

©2025[Phaser](../../../index.md)