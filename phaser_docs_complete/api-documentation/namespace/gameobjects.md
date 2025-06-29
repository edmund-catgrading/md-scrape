# Phaser.GameObjects

Scope:
static

> Source: [src/gameobjects/index.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/index.js#L7)

# Static functions

* [Arc](../class/gameobjects-arc.md)
* [BitmapText](../class/gameobjects-bitmaptext.md)
* [Blitter](../class/gameobjects-blitter.md)
* [Bob](../class/gameobjects-bob.md)
* [Container](../class/gameobjects-container.md)
* [Curve](../class/gameobjects-curve.md)
* [DisplayList](../class/gameobjects-displaylist.md)
* [DOMElement](../class/gameobjects-domelement.md)
* [DynamicBitmapText](../class/gameobjects-dynamicbitmaptext.md)
* [Ellipse](../class/gameobjects-ellipse.md)
* [Extern](../class/gameobjects-extern.md)
* [GameObject](../class/gameobjects-gameobject.md)
* [GameObjectCreator](../class/gameobjects-gameobjectcreator.md)
* [GameObjectFactory](../class/gameobjects-gameobjectfactory.md)
* [Graphics](../class/gameobjects-graphics.md)
* [Grid](../class/gameobjects-grid.md)
* [Group](../class/gameobjects-group.md)
* [Image](../class/gameobjects-image.md)
* [IsoBox](../class/gameobjects-isobox.md)
* [IsoTriangle](../class/gameobjects-isotriangle.md)
* [Layer](../class/gameobjects-layer.md)
* [Light](../class/gameobjects-light.md)
* [LightsManager](../class/gameobjects-lightsmanager.md)
* [LightsPlugin](../class/gameobjects-lightsplugin.md)
* [Line](../class/gameobjects-line.md)
* [Mesh](../class/gameobjects-mesh.md)
* [NineSlice](../class/gameobjects-nineslice.md)
* [PathFollower](../class/gameobjects-pathfollower.md)
* [Plane](../class/gameobjects-plane.md)
* [PointLight](../class/gameobjects-pointlight.md)
* [Polygon](../class/gameobjects-polygon.md)
* [Rectangle](../class/gameobjects-rectangle.md)
* [RenderTexture](../class/gameobjects-rendertexture.md)
* [Rope](../class/gameobjects-rope.md)
* [Shader](../class/gameobjects-shader.md)
* [Shape](../class/gameobjects-shape.md)
* [Sprite](../class/gameobjects-sprite.md)
* [Star](../class/gameobjects-star.md)
* [Text](../class/gameobjects-text.md)
* [TextStyle](../class/gameobjects-textstyle.md)
* [TileSprite](../class/gameobjects-tilesprite.md)
* [Triangle](../class/gameobjects-triangle.md)
* [UpdateList](../class/gameobjects-updatelist.md)
* [Video](../class/gameobjects-video.md)
* [Zone](../class/gameobjects-zone.md)

# Static functions

* [Components](gameobjects-components.md)
* [Events](gameobjects-events.md)
* [Particles](gameobjects-particles.md)
* [RetroFont](gameobjects-retrofont.md)

# Static functions

## BuildGameObject

### <static> BuildGameObject(scene, gameObject, config)

**Description:**

Builds a Game Object using the provided configuration object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| scene | [Phaser.Scene](../class/scene.md) | No | A reference to the Scene. |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No | The initial GameObject. |
| config | [Phaser.Types.GameObjects.GameObjectConfig](../typedef/types-gameobjects.md) | No | The config to build the GameObject with. |

**Returns:** [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) - The built Game Object.

> Source: [src/gameobjects/BuildGameObject.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/BuildGameObject.js#L10)  
> Since: 3.0.0

---

## BuildGameObjectAnimation

### <static> BuildGameObjectAnimation(sprite, config)

**Description:**

Adds an Animation component to a Sprite and populates it based on the given config.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| sprite | [Phaser.GameObjects.Sprite](../class/gameobjects-sprite.md) | No | The sprite to add an Animation component to. |
| --- | --- | --- | --- |
| config | object | No | The animation config. |

**Returns:** [Phaser.GameObjects.Sprite](../class/gameobjects-sprite.md) - The updated Sprite.

> Source: [src/gameobjects/BuildGameObjectAnimation.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/BuildGameObjectAnimation.js#L9)  
> Since: 3.0.0

---

## GetCalcMatrix

### <static> GetCalcMatrix(src, camera, [parentMatrix])

**Description:**

Calculates the Transform Matrix of the given Game Object and Camera, factoring in

the parent matrix if provided.

Note that the object this results contains *references* to the Transform Matrices,

not new instances of them. Therefore, you should use their values immediately, or

copy them to your own matrix, as they will be replaced as soon as another Game

Object is rendered.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| src | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No | The Game Object to calculate the transform matrix for. |
| --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.Camera](../class/cameras-scene2d-camera.md) | No | The camera being used to render the Game Object. |
| parentMatrix | [Phaser.GameObjects.Components.TransformMatrix](../class/gameobjects-components-transformmatrix.md) | Yes | The transform matrix of the parent container, if any. |

**Returns:** [Phaser.Types.GameObjects.GetCalcMatrixResults](../typedef/types-gameobjects.md) - The results object containing the updated transform matrices.

> Source: [src/gameobjects/GetCalcMatrix.js#L15](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GetCalcMatrix.js#L15)  
> Since: 3.50.0

---

## GetTextSize

### <static> GetTextSize(text, size, lines)

**Description:**

Returns an object containing dimensions of the Text object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| text | [Phaser.GameObjects.Text](../class/gameobjects-text.md) | No | The Text object to calculate the size from. |
| --- | --- | --- | --- |
| size | [Phaser.Types.GameObjects.Text.TextMetrics](../typedef/types-gameobjects-text.md) | No | The Text metrics to use when calculating the size. |
| lines | Array.<string> | No | The lines of text to calculate the size from. |

**Returns:** [Phaser.Types.GameObjects.Text.GetTextSizeObject](../typedef/types-gameobjects-text.md) - An object containing dimensions of the Text object.

> Source: [src/gameobjects/text/GetTextSize.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/text/GetTextSize.js#L7)  
> Since: 3.0.0

---

## MeasureText

### <static> MeasureText(textStyle)

**Description:**

Calculates the ascent, descent and fontSize of a given font style.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| textStyle | [Phaser.GameObjects.TextStyle](../class/gameobjects-textstyle.md) | No | The TextStyle object to measure. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Types.GameObjects.Text.TextMetrics](../typedef/types-gameobjects-text.md) - An object containing the ascent, descent and fontSize of the TextStyle.

> Source: [src/gameobjects/text/MeasureText.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/text/MeasureText.js#L9)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Static functions](#static-functions)
* [Static functions](#static-functions-1)
* [Static functions](#static-functions-2)

  + [BuildGameObject](#buildgameobject)

    - [<static> BuildGameObject(scene, gameObject, config)](#static-buildgameobjectscene-gameobject-config)
  + [BuildGameObjectAnimation](#buildgameobjectanimation)

    - [<static> BuildGameObjectAnimation(sprite, config)](#static-buildgameobjectanimationsprite-config)
  + [GetCalcMatrix](#getcalcmatrix)

    - [<static> GetCalcMatrix(src, camera, [parentMatrix])](#static-getcalcmatrixsrc-camera-parentmatrix)
  + [GetTextSize](#gettextsize)

    - [<static> GetTextSize(text, size, lines)](#static-gettextsizetext-size-lines)
  + [MeasureText](#measuretext)

    - [<static> MeasureText(textStyle)](#static-measuretexttextstyle)

Back to top

©2025[Phaser](https://docs.phaser.io)