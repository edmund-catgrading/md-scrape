# Layer

A Guide to the Phaser Layer to group 'layers' of Game Objects

A Layer is a special type of Game Object that acts as a Display List. You can add any type of Game Object to a Layer, just as you would to a Scene. Layers can be used to visually group together 'layers' of Game Objects:

```
Copyconst spaceman = this.add.sprite(150, 300, 'spaceman');
const bunny = this.add.sprite(400, 300, 'bunny');
const elephant = this.add.sprite(650, 300, 'elephant');

const layer = this.add.layer();

layer.add([ spaceman, bunny, elephant ]);

```

The 3 sprites in the example above will now be managed by the Layer they were added to. Therefore, if you then set `layer.setVisible(false)` they would all vanish from the display.

You can also control the depth of the Game Objects within the Layer. For example, calling the `setDepth` method of a child of a Layer will allow you to adjust the depth of that child within the Layer itself, rather than the whole Scene. The Layer, too, can have its depth set as well.

The Layer class also offers many different methods for manipulating the list, such as the methods `moveUp`, `moveDown`, `sendToBack`, `bringToTop` and so on. These allow you to change the display list position of the Layers children, causing it to adjust the order in which they are rendered. Using `setDepth` on a child allows you to override this.

Layers can have Post FX Pipelines set, which allows you to easily enable a post pipeline across a whole range of children, which, depending on the effect, can often be far more efficient that doing so on a per-child basis.

Layers have no position or size within the Scene. This means you cannot enable a Layer for physics or input, or change the position, rotation or scale of a Layer. They also have no scroll factor, texture, tint, origin, crop or bounds.

If you need those kind of features then you should use a Container instead. Containers can be added to Layers, but Layers cannot be added to Containers.

However, you can set the Alpha, Blend Mode, Depth, Mask and Visible state of a Layer. These settings will impact all children being rendered by the Layer.

## Add layer

```
Copyvar layer = this.add.layer();
// var layer = this.add.layer(children);

```

* `children` : Array of game objects added to this layer.

## Custom class

```
Copyclass MyLayer extends Phaser.GameObjects.Layer {
    constructor(scene, children) {
        super(scene, children);
        // ...
        this.add.existing(this);
    }
    // ...

    // preUpdate(time, delta) {}
}

```

* `this.add.existing(gameObject)` : Adds an existing Game Object to this Scene.
  + If the Game Object renders, it will be added to the Display List.
  + If it has a `preUpdate` method, it will be added to the Update List.

Example

```
Copyvar layer = new MyLayer(scene, children);

```

## Add child

* Add child

  ```
  Copylayer.add(gameObject);
  // layer.add(gameObjects);

  ```

  + `gameObject` : A game object, or an array of game objects.
* Add child at

  ```
  Copylayer.addAt(gameObject, index);

  ```
* Replace child

  ```
  Copylayer.replace(oldGameObject, newGameObject);

  ```

## Remove child

* Remove child

  ```
  Copyvar removed = layer.remove(gameObject);

  ```
* Remove child at

  ```
  Copyvar removed = layer.removeAt(index);

  ```
* Remove children between indexes

  ```
  Copyvar removed = layer.removeBetween(startIndex, endIndex);

  ```
* Remove all children

  ```
  Copylayer.removeAll();

  ```

Removed game object won't be added to display list of scene, use

```
CopygameObject.addToDisplayList();

```

to add it back to scene's display list.

## Get child

* Get child at

  ```
  Copyvar gameObject = layer.getAt(index);

  ```
* Get first child by name

  ```
  Copyvar gameObject = layer.getByName(name);

  ```
* Get first child by property

  ```
  Copyvar gameObject = layer.getFirst(property, value);
  // var gameObject = layer.getFirst(property, value, startIndex, endIndex);

  ```
* Get random child

  ```
  Copyvar gameObject = layer.getRandom();
  // var gameObject = layer.getRandom(startIndex, length);

  ```
* Get all children

  ```
  Copyvar gameObjects = layer.getAll();

  ```
* Get index of child

  ```
  Copyvar index = layer.getIndex(gameObject);

  ```
* Get child count

  ```
  Copyvar count = layer.count(property, value);

  ```
* Get total children count

  ```
  Copyvar count = layer.length;

  ```
* Has child

  ```
  Copyvar hasChild = layer.exists(gameObject);

  ```

### Iterate

* Get first child (set iterator index to 0)

  ```
  Copyvar gameObject = layer.first;

  ```
* Get last child (set iterator index to last)

  ```
  Copyvar gameObject = layer.last;

  ```
* Get next child (increase iterator index, until last)

  ```
  Copyvar gameObject = layer.next;

  ```
* Get previous child (decrease iterator index, until 0)

  ```
  Copyvar gameObject = layer.previous;

  ```

## Move child

* Swap

  ```
  Copylayer.swap(gameObject1, gameObject2);

  ```
* Move to

  ```
  Copylayer.moveTo(gameObject, index);

  ```
* Bring to top

  ```
  Copylayer.bringToTop(gameObject);

  ```
* Send to back

  ```
  Copylayer.sendToBack(gameObject);

  ```
* Move up

  ```
  Copylayer.moveUp(gameObject);

  ```
* Move down

  ```
  Copylayer.moveDown(gameObject);

  ```
* Move child1 above child2

  ```
  Copylayer.moveAbove(child1, child2);

  ```
* Move child1 below child2

  ```
  Copylayer.moveBelow(child1, child2);

  ```
* Sort

  ```
  Copylayer.sort(property);

  ```

  or

  ```
  Copylayer.sort('', function(gameObject1, gameObject2) { 
      return 1; // 0, or -1
  });

  ```
* Reverse

  ```
  Copylayer.reverse();

  ```
* Shuffle

  ```
  Copylayer.shuffle();

  ```

!!! note Sort by depth
Children game objects also sort by depth.

## For each child

```
Copylayer.each(function(gameObject) {

}, scope);

```

## Set property

```
Copylayer.setAll(property, value);
// layer.setAll(property, value, startIndex, endIndex);

```

## Events

* On add game object

  ```
  Copylayer.events.on('addedtoscene', function(gameObject, scene) {

  })

  ```
* On remove game object

  ```
  Copylayer.events.on('removedfromscene', function(gameObject, scene) {

  })

  ```

`layer.events` references to `this.events`.

## Other properties

See [game object](../gameobjects.md)

## Create mask

```
Copyvar mask = layer.createBitmapMask();

```

See [mask](../display.md)

## Shader effects

Support [postFX effects](shader.md)

!!! note
No preFX effect support

## Author Credits

Content on this page includes work by:

* [RexRainbow](https://github.com/rexrainbow)

Updated on June 4, 2025, 1:16 PM UTC

---

[Image](image.md)

[Light](light.md)

On this page

* [Layer](#layer)

  + [Add layer](#add-layer)
  + [Custom class](#custom-class)
  + [Add child](#add-child)
  + [Remove child](#remove-child)
  + [Get child](#get-child)

    - [Iterate](#iterate)
  + [Move child](#move-child)
  + [For each child](#for-each-child)
  + [Set property](#set-property)
  + [Events](#events)
  + [Other properties](#other-properties)
  + [Create mask](#create-mask)
  + [Shader effects](#shader-effects)
  + [Author Credits](#author-credits)

Back to top

©2025[Phaser](../../../index.md)