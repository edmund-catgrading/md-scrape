# Rope

A Guide to the Phaser Rope Game Object

The Rope object is *WebGL only* and does not have a Canvas counterpart.

A Rope is a special kind of Game Object that has a texture is stretched along its entire length.

Unlike a Sprite, it isn't restricted to using just a quad and can have as many vertices as you define when creating it. The vertices can be arranged in a horizontal or vertical strip and have their own color and alpha values as well.

A Ropes origin is always 0.5 x 0.5 and cannot be changed.

## Load texture

```
Copythis.load.image(key, url);

```

Reference: [load image](../loader.md)

## Add object

```
Copyvar rope = this.add.rope(x, y, texture, frame, points, horizontal);
// var rope = this.add.rope(x, y, texture, frame, points, horizontal, colors, alphas);

```

* `points` :
  + A number : Segments to split the texture frame into.
  + An number array : An array containing the vertices data.
* `horizontal` :
  + `true` : Vertices of this Rope be aligned horizontally.
  + `false` : Vertices of this Rope be aligned vertically.
* `colors` : An optional array containing the color data for this Rope. One color value per pair of vertices.
* `alphas` : An optional array containing the alpha data for this Rope. One alpha value per pair of vertices.

Add rope from JSON

```
Copyvar rope = this.make.rope({
    x: 0,
    y: 0,
    key: '',
    frame: null,
    horizontal: true,
    points: undefined,
    colors: undefined,
    alphas: undefined,

    // angle: 0,
    // alpha: 1
    // flipX: true,
    // flipY: true,
    // origin: {x: 0.5, y: 0.5},
    
    add: true
});

```

## Custom rope class

* Define class

  ```
  Copyclass MyRope extends Phaser.GameObjects.Rope {
      constructor(scene, x, y, texture, frame, points, horizontal, colors, alphas) {
          super(scene, x, y, texture, frame, points, horizontal, colors, alphas);
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
  Copyvar rope = new MyRope(scene, x, y, texture, frame, points, horizontal);

  ```

## Origin

A Ropes origin is always 0.5 x 0.5 and cannot be changed.

## Set vertices

Set vertices via

```
Copyrope.setPoints(points);
// rope.setPoints(points, colors, alphas);

```

* `points` :
  + A number : Segments to split the texture frame into.
  + An number array : An array containing the vertices data.
* `colors` : An optional array containing the color data for this Rope. One color value per pair of vertices.
* `alphas` : An optional array containing the alpha data for this Rope. One alpha value per pair of vertices.

Also change horizontal mode :

* Change vertical rope to horizontal rope, do nothing if rope is horizontal mode already

  ```
  Copyrope.setHorizontal(points);
  // rope.setHorizontal(points, colors, alphas);

  ```
* Change horizontal rope to vertical rope, do nothing if rope is vertical mode already

  ```
  Copyrope.setVertical(points);
  // rope.setVertical(points, colors, alphas);

  ```

Or set `rope.points` directly :

1. Change `rope.points`
   * Horizontal rope : `rope.points[i].y = newY`
   * Vertical rope : `rope.points[i].x = newX`
2. Call `rope.setDirty()`, or `rope.updateVertices()`

Each point is relative to position of rope object, get points of world via

```
Copyvar worldX = rope.points[i].x + rope.x;
var worldY = rope.points[i].y + rope.y;

```

## Play animation

```
Copyrope.play(key);
// rope.play(key, ignoreIfPlaying, startFrame);

```

* `ignoreIfPlaying` : If an animation is already playing then ignore this call. Default value is `false`.
* `startFrame` : Optionally start the animation playing from this frame index. Default value is `0`.

## Alpha

* Single alpha

  ```
  Copyrope.setAlphas(alpha);

  ```
* Top - bottom alpha

  ```
  Copyrope.setAlphas(topAlpha, bottomAlpha);

  ```
* Alpha array for each point

  ```
  Copyrope.setAlphas(alphaArray);

  ```

  + `alphaArray` : Array of alpha value.

## Color tint

* Single color tint

  ```
  Copyrope.setColors(color);

  ```
* Color tint array for each point

  ```
  Copyrope.setAlphas(colorArray);

  ```

  + `colorArray` : Array of color tint value.

### Tint fill mode

Sets the tint fill mode.

```
Copyrope.setTintFill(mode);

```

* `mode` :
  + `0` : Additive tint, blends the vertices colors with the texture. Default behavior.
  + `1` : Fill tint with alpha.
  + `2` : Fill tint without alpha.

## Flip

```
Copyrope.flipX = flip;
rope.flipY = flip;

```

If this Game Object has a physics body, it will not change the body. This is a rendering toggle only.

## Debug

Draw debug mesh each render tick.

```
Copyrope.setDebug(graphic);
// rope.setDebug(graphic, callback);

```

* `graphic` : [Graphics game object](graphics.md)
* `callback` : Callback of rendering debug graphics ([default callback](https://github.com/photonstorm/phaser/blob/master/src/gameobjects/rope/Rope.js#L996-L1024))

  ```
  Copyfunction(rope, meshLength, verts) {
      // var graphic = rope.debugGraphic;
  }

  ```

  + `rope` : Rope instance.
    - `rope.debugGraphic` : [Graphics game object](graphics.md)
  + `meshLength` : The number of mesh vertices in total.
  + `verts` : An array of the translated vertex coordinates.

!!! note
Clear Debug graphics (`rope.debugGraphic.clear()`) during scene's update stage (`this.update() { }`)

## Author Credits

Content on this page includes work by:

* [RexRainbow](https://github.com/rexrainbow)

Updated on June 4, 2025, 1:16 PM UTC

---

[Render Texture](render-texture.md)

[Shader](shader.md)

On this page

* [Rope](#rope)

  + [Load texture](#load-texture)
  + [Add object](#add-object)
  + [Custom rope class](#custom-rope-class)
  + [Origin](#origin)
  + [Set vertices](#set-vertices)
  + [Play animation](#play-animation)
  + [Alpha](#alpha)
  + [Color tint](#color-tint)

    - [Tint fill mode](#tint-fill-mode)
  + [Flip](#flip)
  + [Debug](#debug)
  + [Author Credits](#author-credits)

Back to top

©2025[Phaser](../../../index.md)