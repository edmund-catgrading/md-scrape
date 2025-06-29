# Image

A Guide to the Phaser Image Game Object

An Image is a light-weight Game Object useful for the display of static images in your game, such as logos, backgrounds, scenery or other non-animated elements. Images can have input events and physics bodies, or be tweened, tinted or scrolled. The main difference between an Image and a Sprite is that you cannot animate an Image as they do not have the Animation component.

## Load texture

```
Copythis.load.image(key, url);

```

Reference: [load image](../loader.md)

## Add image object

```
Copyvar image = this.add.image(x, y, key);
// var image = this.add.image(x, y, key, frame);

```

Add image from JSON

```
Copyvar image = this.make.image({
    x: 0,
    y: 0,
    key: '',
    // frame: '',

    // angle: 0,
    // alpha: 1,
    // flipX: true,
    // flipY: true,
    // scale : {
    //    x: 1,
    //    y: 1
    //},
    // origin: {x: 0.5, y: 0.5},

    add: true
});

```

* `key`, `frame` :
  + A string
  + An array of string to pick one element at random
* `x`, `y`, `scale.x`, `scale.y` :
  + A number
  + A callback to get return value

    ```
    Copyfunction() { return 0; }

    ```
  + Random integer between min and max

    ```
    Copy{ randInt: [min, max] }

    ```
  + Random float between min and max

    ```
    Copy{ randFloat: [min, max] }

    ```

## Custom class

```
Copyclass MyImage extends Phaser.GameObjects.Image {
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
Copyvar image = new MyImage(scene, x, y, key);

```

## Texture

See [game object - texture](../gameobjects.md)

## Other properties

See [game object](../gameobjects.md)

## Create mask

```
Copyvar mask = image.createBitmapMask();

```

See [mask](../display.md)

## Shader effects

Support [preFX and postFX effects](shader.md)

## Author Credits

Content on this page includes work by:

* [RexRainbow](https://github.com/rexrainbow)

Updated on June 4, 2025, 1:16 PM UTC

---

[Group](group.md)

[Layer](layer.md)

On this page

* [Image](#image)

  + [Load texture](#load-texture)
  + [Add image object](#add-image-object)
  + [Custom class](#custom-class)
  + [Texture](#texture)
  + [Other properties](#other-properties)
  + [Create mask](#create-mask)
  + [Shader effects](#shader-effects)
  + [Author Credits](#author-credits)

Back to top

©2025[Phaser](../../../index.md)