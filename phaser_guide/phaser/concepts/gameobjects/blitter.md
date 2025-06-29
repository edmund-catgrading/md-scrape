# Blitter

A Guide to the Phaser Blitter Game Object

The Blitter Game Object is a special kind of container that creates, updates and manages Bob objects. Bobs are designed for rendering speed rather than flexibility. They consist of a texture, or frame from a texture, a position and an alpha value. You cannot scale or rotate them. They use a batched drawing method for speed during rendering.

A Blitter Game Object has one texture bound to it. Bobs created by the Blitter can use any Frame from this Texture to render with, but they cannot use any other Texture. It is this single texture-bind that allows them their speed.

If you have a need to blast a large volume of frames around the screen then Blitter objects are well worth investigating. They are especially useful for using as a base for your own special effects systems.

## Load texture

```
Copythis.load.image(key, url);

```

Reference: [load image](../loader.md)

## Add blitter container

Add blitter container

```
Copyvar blitter = this.add.blitter(x, y, key);

```

* `key` : The key of the texture this Game Object will use for rendering. The Texture must already exist in the Texture Manager.

Add blitter container from JSON

```
Copyvar blitter = this.make.blitter({
    x: 0,
    y: 0,
    key: '',

    // angle: 0,
    // alpha: 1
    // flipX: true,
    // flipY: true,
    // origin: {x: 0.5, y: 0.5},
    
    add: true
});

```

## Custom class

```
Copyclass MyBlitter extends Phaser.GameObjects.Blitter {
    constructor(scene, x, y, texture, frame) {
        super(scene, x, y, texture, frame);
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
Copyvar blitter = new MyBlitter(scene, x, y, key);

```

## Add bob object

```
Copyvar bob = blitter.create(x, y);
// var bob = blitter.create(x, y, frame, visible, index);

```

* `frame` : The Frame the Bob will use. It must be part of the Texture the parent Blitter object is using.
* `visible` : Should the created Bob render or not?
* `index` : The position in the Blitters Display List to add the new Bob at. Defaults to the top of the list.

### Add mutiple bob objects

```
Copyvar bobs = blitter.createMultiple(quantity, frame, visible);

```

* `quantity` : The quantity of Bob objects to create.

### Add bob object from callback

```
Copyvar bobs = blitter.createFromCallback(callback, quantity, frame, visible);
// var callback = function(bob, i){};

```

## Get bob objects

```
Copyvar bobs = blitter.children.list;

```

## Clear all bob objects

```
Copyblitter.clear();

```

## Bob object

A Bob has a position, `alpha` value and a `frame` from a texture that it uses to render with. You can also toggle the flipped and visible state of the Bob.

### Position

* Get

  ```
  Copyvar x = bob.x;
  var y = bob.y;

  ```
* Set

  ```
  Copybob.setPosition(x, y);
  // bob.x = 0;
  // bob.y = 0;

  ```

  or

  ```
  Copybob.reset(x, y);
  // bob.reset(x, y, frame);

  ```

### Frame

* Get

  ```
  Copyvar frame = bob.frame;

  ```

  + `frame` : [Frame object](../textures.md).
* Set

  ```
  Copybob.setFrame(frame);

  ```

### Flip

* Get

  ```
  Copyvar flipX = bob.flipX;
  var flipY = bob.flipY;

  ```
* Set

  ```
  Copybob.setFlip(boolX, boolY);
  // bob.setFlipX(boolean);
  // bob.setFlipY(boolean);
  // bob.flipX = flipX;
  // bob.flipY = flipY;

  ```

  or

  ```
  Copybob.resetFlip(); // bob.setFlip(false, false)

  ```

### Visible

* Get

  ```
  Copyvar visible = bob.visible;

  ```
* Set

  ```
  Copybob.setVisible(boolean);
  // bob.visible = v;

  ```

### Alpha

* Get

  ```
  Copyvar alpha = bob.alpha;

  ```
* Set

  ```
  Copybob.setAlpha(v);
  // bob.aplha = v;

  ```

### Tint

* Get

  ```
  Copyvar tint = bob.tint;

  ```
* Set

  ```
  Copybob.setTint(tint);
  // bob.tint = tint;

  ```

  + `tint` : Tint value, between `0` and `0xffffff`.

### Destroy

```
Copybob.destroy();

```

### Data

```
Copyvar data = bob.data;  // {}

```

## Other properties

See [game object](../gameobjects.md)

## Create mask

```
Copyvar mask = bob.createBitmapMask();

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

[Bitmap Text](bitmap-text.md)

[Container](container.md)

On this page

* [Blitter](#blitter)

  + [Load texture](#load-texture)
  + [Add blitter container](#add-blitter-container)
  + [Custom class](#custom-class)
  + [Add bob object](#add-bob-object)

    - [Add mutiple bob objects](#add-mutiple-bob-objects)
    - [Add bob object from callback](#add-bob-object-from-callback)
  + [Get bob objects](#get-bob-objects)
  + [Clear all bob objects](#clear-all-bob-objects)
  + [Bob object](#bob-object)

    - [Position](#position)
    - [Frame](#frame)
    - [Flip](#flip)
    - [Visible](#visible)
    - [Alpha](#alpha)
    - [Tint](#tint)
    - [Destroy](#destroy)
    - [Data](#data)
  + [Other properties](#other-properties)
  + [Create mask](#create-mask)
  + [Shader effects](#shader-effects)
  + [Author Credits](#author-credits)

Back to top

©2025[Phaser](../../../index.md)