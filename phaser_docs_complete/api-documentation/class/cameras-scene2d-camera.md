# Camera

Phaser.Cameras.Scene2D.Camera

A Camera.

The Camera is the way in which all games are rendered in Phaser. They provide a view into your game world,

and can be positioned, rotated, zoomed and scrolled accordingly.

A Camera consists of two elements: The viewport and the scroll values.

The viewport is the physical position and size of the Camera within your game. Cameras, by default, are

created the same size as your game, but their position and size can be set to anything. This means if you

wanted to create a camera that was 320x200 in size, positioned in the bottom-right corner of your game,

you'd adjust the viewport to do that (using methods like `setViewport` and `setSize`).

If you wish to change where the Camera is looking in your game, then you scroll it. You can do this

via the properties `scrollX` and `scrollY` or the method `setScroll`. Scrolling has no impact on the

viewport, and changing the viewport has no impact on the scrolling.

By default a Camera will render all Game Objects it can see. You can change this using the `ignore` method,

allowing you to filter Game Objects out on a per-Camera basis.

A Camera also has built-in special effects including Fade, Flash and Camera Shake.

**Constructor**

`new Camera(x, y, width, height)`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The x position of the Camera, relative to the top-left of the game canvas. |
| --- | --- | --- | --- |
| y | number | No | The y position of the Camera, relative to the top-left of the game canvas. |
| width | number | No | The width of the Camera, in pixels. |
| height | number | No | The height of the Camera, in pixels. |

---

**Scope**: static

**Extends**

> [Phaser.Cameras.Scene2D.BaseCamera](cameras-scene2d-basecamera.md)  
> [Phaser.GameObjects.Components.PostPipeline](../namespace/gameobjects-components-postpipeline.md)

> Source: [src/cameras/2d/Camera.js#L18](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/Camera.js#L18)  
> Since: 3.0.0

# Public Members

## alpha

### alpha: number

**Description:**

The Camera alpha value. Setting this property impacts every single object that this Camera

renders. You can either set the property directly, i.e. via a Tween, to fade a Camera in or out,

or via the chainable `setAlpha` method instead.

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#alpha](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L377](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L377)  
> Since: 3.11.0

---

## alphaBottomLeft

### alphaBottomLeft: number

**Description:**

The alpha value starting from the bottom-left of the Game Object.

This value is interpolated from the corner to the center of the Game Object.

**Tags:**

* webglOnly

**Inherits:** [Phaser.GameObjects.Components.Alpha#alphaBottomLeft](../namespace/gameobjects-components-alpha.md)

> Source: [src/gameobjects/components/Alpha.js#L227](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Alpha.js#L227)  
> Since: 3.0.0

---

## alphaBottomRight

### alphaBottomRight: number

**Description:**

The alpha value starting from the bottom-right of the Game Object.

This value is interpolated from the corner to the center of the Game Object.

**Tags:**

* webglOnly

**Inherits:** [Phaser.GameObjects.Components.Alpha#alphaBottomRight](../namespace/gameobjects-components-alpha.md)

> Source: [src/gameobjects/components/Alpha.js#L257](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Alpha.js#L257)  
> Since: 3.0.0

---

## alphaTopLeft

### alphaTopLeft: number

**Description:**

The alpha value starting from the top-left of the Game Object.

This value is interpolated from the corner to the center of the Game Object.

**Tags:**

* webglOnly

**Inherits:** [Phaser.GameObjects.Components.Alpha#alphaTopLeft](../namespace/gameobjects-components-alpha.md)

> Source: [src/gameobjects/components/Alpha.js#L167](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Alpha.js#L167)  
> Since: 3.0.0

---

## alphaTopRight

### alphaTopRight: number

**Description:**

The alpha value starting from the top-right of the Game Object.

This value is interpolated from the corner to the center of the Game Object.

**Tags:**

* webglOnly

**Inherits:** [Phaser.GameObjects.Components.Alpha#alphaTopRight](../namespace/gameobjects-components-alpha.md)

> Source: [src/gameobjects/components/Alpha.js#L197](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Alpha.js#L197)  
> Since: 3.0.0

---

## backgroundColor

### backgroundColor: [Phaser.Display.Color](../namespace/display-color.md)

**Description:**

The background color of this Camera. Only used if `transparent` is `false`.

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#backgroundColor](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L368](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L368)  
> Since: 3.0.0

---

## cameraManager

### cameraManager: [Phaser.Cameras.Scene2D.CameraManager](cameras-scene2d-cameramanager.md)

**Description:**

A reference to the Scene's Camera Manager to which this Camera belongs.

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#cameraManager](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L106](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L106)  
> Since: 3.17.0

---

## centerX

### centerX: number

**Description:**

The horizontal position of the center of the Camera's viewport, relative to the left of the game canvas.

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#centerX](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L1879](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L1879)  
> Since: 3.10.0

---

## centerY

### centerY: number

**Description:**

The vertical position of the center of the Camera's viewport, relative to the top of the game canvas.

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#centerY](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L1896](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L1896)  
> Since: 3.10.0

---

## deadzone

### deadzone: [Phaser.Geom.Rectangle](geom-rectangle.md)

**Description:**

The Camera dead zone.

The deadzone is only used when the camera is following a target.

It defines a rectangular region within which if the target is present, the camera will not scroll.

If the target moves outside of this area, the camera will begin scrolling in order to follow it.

The `lerp` values that you can set for a follower target also apply when using a deadzone.

You can directly set this property to be an instance of a Rectangle. Or, you can use the

`setDeadzone` method for a chainable approach.

The rectangle you provide can have its dimensions adjusted dynamically, however, please

note that its position is updated every frame, as it is constantly re-centered on the cameras mid point.

Calling `setDeadzone` with no arguments will reset an active deadzone, as will setting this property

to `null`.

> Source: [src/cameras/2d/Camera.js#L169](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/Camera.js#L169)  
> Since: 3.11.0

---

## dirty

### dirty: boolean

**Description:**

Is this Camera dirty?

A dirty Camera has had either its viewport size, bounds, scroll, rotation or zoom levels changed since the last frame.

This flag is cleared during the `postRenderCamera` method of the renderer.

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#dirty](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L183](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L183)  
> Since: 3.11.0

---

## disableCull

### disableCull: boolean

**Description:**

Should the camera cull Game Objects before checking them for input hit tests?

In some special cases it may be beneficial to disable this.

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#disableCull](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L388](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L388)  
> Since: 3.0.0

---

## displayHeight

### displayHeight: number

**Description:**

The displayed height of the camera viewport, factoring in the camera zoom level.

If a camera has a viewport height of 600 and a zoom of 0.5 then its display height

would be 1200, as it's displaying twice as many pixels as zoom level 1.

Equally, a camera with a height of 600 and zoom of 2 would have a display height

of 300 pixels.

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#displayHeight](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L1936](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L1936)  
> Since: 3.11.0

---

## displayWidth

### displayWidth: number

**Description:**

The displayed width of the camera viewport, factoring in the camera zoom level.

If a camera has a viewport width of 800 and a zoom of 0.5 then its display width

would be 1600, as it's displaying twice as many pixels as zoom level 1.

Equally, a camera with a width of 800 and zoom of 2 would have a display width

of 400 pixels.

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#displayWidth](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L1913](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L1913)  
> Since: 3.11.0

---

## fadeEffect

### fadeEffect: [Phaser.Cameras.Scene2D.Effects.Fade](cameras-scene2d-effects-fade.md)

**Description:**

The Camera Fade effect handler.

To fade this camera see the `Camera.fade` methods.

> Source: [src/cameras/2d/Camera.js#L80](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/Camera.js#L80)  
> Since: 3.5.0

---

## flashEffect

### flashEffect: [Phaser.Cameras.Scene2D.Effects.Flash](cameras-scene2d-effects-flash.md)

**Description:**

The Camera Flash effect handler.

To flash this camera see the `Camera.flash` method.

> Source: [src/cameras/2d/Camera.js#L90](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/Camera.js#L90)  
> Since: 3.5.0

---

## followOffset

### followOffset: [Phaser.Math.Vector2](math-vector2.md)

**Description:**

The values stored in this property are subtracted from the Camera targets position, allowing you to

offset the camera from the actual target x/y coordinates by this amount.

Can also be set via `setFollowOffset` or as part of the `startFollow` call.

> Source: [src/cameras/2d/Camera.js#L158](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/Camera.js#L158)  
> Since: 3.9.0

---

## hasPostPipeline

### hasPostPipeline: boolean

**Description:**

Does this Game Object have any Post Pipelines set?

**Tags:**

* webglOnly

**Inherits:** [Phaser.GameObjects.Components.PostPipeline#hasPostPipeline](../namespace/gameobjects-components-postpipeline.md)

> Source: [src/gameobjects/components/PostPipeline.js#L21](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/PostPipeline.js#L21)  
> Since: 3.60.0

---

## height

### height: number

**Description:**

The height of the Camera viewport, in pixels.

The viewport is the area into which the Camera renders. Setting the viewport does

not restrict where the Camera can scroll to.

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#height](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L1663](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L1663)  
> Since: 3.0.0

---

## id

### id: number

**Description:**

The Camera ID. Assigned by the Camera Manager and used to handle camera exclusion.

This value is a bitmask.

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#id](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L115](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L115)  
> Since: 3.11.0

---

## inputEnabled

### inputEnabled: boolean

**Description:**

Does this Camera allow the Game Objects it renders to receive input events?

> Source: [src/cameras/2d/Camera.js#L70](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/Camera.js#L70)  
> Since: 3.0.0

---

## isSceneCamera

### isSceneCamera: boolean

**Description:**

Is this Camera a Scene Camera? (which is the default), or a Camera

belonging to a Texture?

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#isSceneCamera](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L510](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L510)  
> Since: 3.60.0

---

## lerp

### lerp: [Phaser.Math.Vector2](math-vector2.md)

**Description:**

The linear interpolation value to use when following a target.

Can also be set via `setLerp` or as part of the `startFollow` call.

The default values of 1 means the camera will instantly snap to the target coordinates.

A lower value, such as 0.1 means the camera will more slowly track the target, giving

a smooth transition. You can set the horizontal and vertical values independently, and also

adjust this value in real-time during your game.

Be sure to keep the value between 0 and 1. A value of zero will disable tracking on that axis.

> Source: [src/cameras/2d/Camera.js#L140](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/Camera.js#L140)  
> Since: 3.9.0

---

## mask

### mask: [Phaser.Display.Masks.BitmapMask](display-masks-bitmapmask.md), [Phaser.Display.Masks.GeometryMask](display-masks-geometrymask.md)

**Description:**

The Mask this Camera is using during render.

Set the mask using the `setMask` method. Remove the mask using the `clearMask` method.

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#mask](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L470](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L470)  
> Since: 3.17.0

---

## midPoint

### midPoint: [Phaser.Math.Vector2](math-vector2.md)

**Description:**

The mid-point of the Camera in 'world' coordinates.

Use it to obtain exactly where in the world the center of the camera is currently looking.

This value is updated in the preRender method, after the scroll values and follower

have been processed.

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#midPoint](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L410](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L410)  
> Since: 3.11.0

---

## name

### name: string

**Description:**

The name of the Camera. This is left empty for your own use.

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#name](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L126](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L126)  
> Since: 3.0.0

---

## originX

### originX: number

**Description:**

The horizontal origin of rotation for this Camera.

By default the camera rotates around the center of the viewport.

Changing the origin allows you to adjust the point in the viewport from which rotation happens.

A value of 0 would rotate from the top-left of the viewport. A value of 1 from the bottom right.

See `setOrigin` to set both origins in a single, chainable call.

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#originX](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L425](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L425)  
> Since: 3.11.0

---

## originY

### originY: number

**Description:**

The vertical origin of rotation for this Camera.

By default the camera rotates around the center of the viewport.

Changing the origin allows you to adjust the point in the viewport from which rotation happens.

A value of 0 would rotate from the top-left of the viewport. A value of 1 from the bottom right.

See `setOrigin` to set both origins in a single, chainable call.

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#originY](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L442](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L442)  
> Since: 3.11.0

---

## panEffect

### panEffect: [Phaser.Cameras.Scene2D.Effects.Pan](cameras-scene2d-effects-pan.md)

**Description:**

The Camera Pan effect handler.

To pan this camera see the `Camera.pan` method.

> Source: [src/cameras/2d/Camera.js#L110](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/Camera.js#L110)  
> Since: 3.11.0

---

## postFX

### postFX: [Phaser.GameObjects.Components.FX](gameobjects-components-fx.md)

**Description:**

The Post FX component of this Game Object.

This component allows you to apply a variety of built-in effects to this Game Object, such

as glow, blur, bloom, displacements, vignettes and more. You access them via this property,

for example:

```
Copy
const player = this.add.sprite();

player.postFX.addBloom();


```

All FX are WebGL only and do not have Canvas counterparts.

Please see the FX Class for more details and available methods.

This property is always `null` until the `initPostPipeline` method is called.

**Tags:**

* webglOnly

**Inherits:** [Phaser.GameObjects.Components.PostPipeline#postFX](../namespace/gameobjects-components-postpipeline.md)

> Source: [src/gameobjects/components/PostPipeline.js#L88](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/PostPipeline.js#L88)  
> Since: 3.60.0

---

## postPipelineData

### postPipelineData: object

**Description:**

An object to store pipeline specific data in, to be read by the pipelines this Game Object uses.

**Tags:**

* webglOnly

**Inherits:** [Phaser.GameObjects.Components.PostPipeline#postPipelineData](../namespace/gameobjects-components-postpipeline.md)

> Source: [src/gameobjects/components/PostPipeline.js#L46](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/PostPipeline.js#L46)  
> Since: 3.60.0

---

## postPipelines

### postPipelines: Array.<[Phaser.Renderer.WebGL.Pipelines.PostFXPipeline](renderer-webgl-pipelines-postfxpipeline.md)>

**Description:**

The WebGL Post FX Pipelines this Game Object uses for post-render effects.

The pipelines are processed in the order in which they appear in this array.

If you modify this array directly, be sure to set the

`hasPostPipeline` property accordingly.

**Tags:**

* webglOnly

**Inherits:** [Phaser.GameObjects.Components.PostPipeline#postPipelines](../namespace/gameobjects-components-postpipeline.md)

> Source: [src/gameobjects/components/PostPipeline.js#L31](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/PostPipeline.js#L31)  
> Since: 3.60.0

---

## preFX

### preFX: [Phaser.GameObjects.Components.FX](gameobjects-components-fx.md)

**Description:**

The Pre FX component of this Game Object.

This component allows you to apply a variety of built-in effects to this Game Object, such

as glow, blur, bloom, displacements, vignettes and more. You access them via this property,

for example:

```
Copy
const player = this.add.sprite();

player.preFX.addBloom();


```

Only the following Game Objects support Pre FX:

* Image
* Sprite
* TileSprite
* Text
* RenderTexture
* Video

All FX are WebGL only and do not have Canvas counterparts.

Please see the FX Class for more details and available methods.

**Tags:**

* webglOnly

**Inherits:** [Phaser.GameObjects.Components.PostPipeline#preFX](../namespace/gameobjects-components-postpipeline.md)

> Source: [src/gameobjects/components/PostPipeline.js#L56](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/PostPipeline.js#L56)  
> Since: 3.60.0

---

## renderList

### renderList: Array.<[Phaser.GameObjects.GameObject](gameobjects-gameobject.md)>

**Description:**

This array is populated with all of the Game Objects that this Camera has rendered

in the previous (or current, depending on when you inspect it) frame.

It is cleared at the start of `Camera.preUpdate`, or if the Camera is destroyed.

You should not modify this array as it is used internally by the input system,

however you can read it as required. Note that Game Objects may appear in this

list multiple times if they belong to multiple non-exclusive Containers.

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#renderList](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L494](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L494)  
> Since: 3.52.0

---

## renderRoundPixels

### renderRoundPixels: boolean

**Description:**

Can this Camera render rounded pixel values?

This property is updated during the `preRender` method and should not be

set directly. It is set based on the `roundPixels` property of the Camera

combined with the zoom level. If the zoom is an integer then the WebGL

Renderer can apply rounding during rendering.

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#renderRoundPixels](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L521](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L521)  
> Since: 3.86.0

---

## rotateToEffect

### rotateToEffect: [Phaser.Cameras.Scene2D.Effects.RotateTo](cameras-scene2d-effects-rotateto.md)

**Description:**

The Camera Rotate To effect handler.

To rotate this camera see the `Camera.rotateTo` method.

> Source: [src/cameras/2d/Camera.js#L120](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/Camera.js#L120)  
> Since: 3.23.0

---

## roundPixels

### roundPixels: boolean

**Description:**

Should this camera round its pixel values to integers?

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#roundPixels](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L136](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L136)  
> Since: 3.0.0

---

## scaleManager

### scaleManager: [Phaser.Scale.ScaleManager](scale-scalemanager.md)

**Description:**

A reference to the Game Scale Manager.

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#scaleManager](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L97](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L97)  
> Since: 3.16.0

---

## scene

### scene: [Phaser.Scene](scene.md)

**Description:**

A reference to the Scene this camera belongs to.

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#scene](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L79](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L79)  
> Since: 3.0.0

---

## sceneManager

### sceneManager: [Phaser.Scenes.SceneManager](scenes-scenemanager.md)

**Description:**

A reference to the Game Scene Manager.

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#sceneManager](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L88](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L88)  
> Since: 3.12.0

---

## scrollX

### scrollX: number

**Description:**

The horizontal scroll position of this Camera.

Change this value to cause the Camera to scroll around your Scene.

Alternatively, setting the Camera to follow a Game Object, via the `startFollow` method,

will automatically adjust the Camera scroll values accordingly.

You can set the bounds within which the Camera can scroll via the `setBounds` method.

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#scrollX](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L1688](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L1688)  
> Since: 3.0.0

---

## scrollY

### scrollY: number

**Description:**

The vertical scroll position of this Camera.

Change this value to cause the Camera to scroll around your Scene.

Alternatively, setting the Camera to follow a Game Object, via the `startFollow` method,

will automatically adjust the Camera scroll values accordingly.

You can set the bounds within which the Camera can scroll via the `setBounds` method.

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#scrollY](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L1721](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L1721)  
> Since: 3.0.0

---

## shakeEffect

### shakeEffect: [Phaser.Cameras.Scene2D.Effects.Shake](cameras-scene2d-effects-shake.md)

**Description:**

The Camera Shake effect handler.

To shake this camera see the `Camera.shake` method.

> Source: [src/cameras/2d/Camera.js#L100](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/Camera.js#L100)  
> Since: 3.5.0

---

## transparent

### transparent: boolean

**Description:**

Does this Camera have a transparent background?

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#transparent](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L358](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L358)  
> Since: 3.0.0

---

## useBounds

### useBounds: boolean

**Description:**

Is this Camera using a bounds to restrict scrolling movement?

Set this property along with the bounds via `Camera.setBounds`.

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#useBounds](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L158](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L158)  
> Since: 3.0.0

---

## visible

### visible: boolean

**Description:**

Is this Camera visible or not?

A visible camera will render and perform input tests.

An invisible camera will not render anything and will skip input tests.

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#visible](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L146](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L146)  
> Since: 3.10.0

---

## width

### width: number

**Description:**

The width of the Camera viewport, in pixels.

The viewport is the area into which the Camera renders. Setting the viewport does

not restrict where the Camera can scroll to.

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#width](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L1638](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L1638)  
> Since: 3.0.0

---

## worldView

### worldView: [Phaser.Geom.Rectangle](geom-rectangle.md)

**Description:**

The World View is a Rectangle that defines the area of the 'world' the Camera is currently looking at.

This factors in the Camera viewport size, zoom and scroll position and is updated in the Camera preRender step.

If you have enabled Camera bounds the worldview will be clamped to those bounds accordingly.

You can use it for culling or intersection checks.

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#worldView](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L170](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L170)  
> Since: 3.11.0

---

## x

### x: number

**Description:**

The x position of the Camera viewport, relative to the top-left of the game canvas.

The viewport is the area into which the camera renders.

To adjust the position the camera is looking at in the game world, see the `scrollX` value.

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#x](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L1590](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L1590)  
> Since: 3.0.0

---

## y

### y: number

**Description:**

The y position of the Camera viewport, relative to the top-left of the game canvas.

The viewport is the area into which the camera renders.

To adjust the position the camera is looking at in the game world, see the `scrollY` value.

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#y](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L1614](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L1614)  
> Since: 3.0.0

---

## zoom

### zoom: number

**Description:**

The Camera zoom value. Change this value to zoom in, or out of, a Scene.

A value of 0.5 would zoom the Camera out, so you can now see twice as much

of the Scene as before. A value of 2 would zoom the Camera in, so every pixel

now takes up 2 pixels when rendered.

Set to 1 to return to the default zoom level.

Be careful to never set this value to zero.

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#zoom](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L1754](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L1754)  
> Since: 3.0.0

---

## zoomEffect

### zoomEffect: [Phaser.Cameras.Scene2D.Effects.Zoom](cameras-scene2d-effects-zoom.md)

**Description:**

The Camera Zoom effect handler.

To zoom this camera see the `Camera.zoom` method.

> Source: [src/cameras/2d/Camera.js#L130](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/Camera.js#L130)  
> Since: 3.11.0

---

## zoomX

### zoomX: number

**Description:**

The Camera horizontal zoom value. Change this value to zoom in, or out of, a Scene.

A value of 0.5 would zoom the Camera out, so you can now see twice as much

of the Scene as before. A value of 2 would zoom the Camera in, so every pixel

now takes up 2 pixels when rendered.

Set to 1 to return to the default zoom level.

Be careful to never set this value to zero.

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#zoomX](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L1787](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L1787)  
> Since: 3.50.0

---

## zoomY

### zoomY: number

**Description:**

The Camera vertical zoom value. Change this value to zoom in, or out of, a Scene.

A value of 0.5 would zoom the Camera out, so you can now see twice as much

of the Scene as before. A value of 2 would zoom the Camera in, so every pixel

now takes up 2 pixels when rendered.

Set to 1 to return to the default zoom level.

Be careful to never set this value to zero.

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#zoomY](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L1818](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L1818)  
> Since: 3.50.0

---

# Private Members

## \_alpha

### \_alpha: number

**Description:**

Private internal value. Holds the global alpha value.

**Access:** private

**Inherits:** [Phaser.GameObjects.Components.Alpha#\_alpha](../namespace/gameobjects-components-alpha.md)

> Source: [src/gameobjects/components/Alpha.js#L22](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Alpha.js#L22)  
> Since: 3.0.0

---

## \_alphaBL

### \_alphaBL: number

**Description:**

Private internal value. Holds the bottom-left alpha value.

**Access:** private

**Inherits:** [Phaser.GameObjects.Components.Alpha#\_alphaBL](../namespace/gameobjects-components-alpha.md)

> Source: [src/gameobjects/components/Alpha.js#L55](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Alpha.js#L55)  
> Since: 3.0.0

---

## \_alphaBR

### \_alphaBR: number

**Description:**

Private internal value. Holds the bottom-right alpha value.

**Access:** private

**Inherits:** [Phaser.GameObjects.Components.Alpha#\_alphaBR](../namespace/gameobjects-components-alpha.md)

> Source: [src/gameobjects/components/Alpha.js#L66](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Alpha.js#L66)  
> Since: 3.0.0

---

## \_alphaTL

### \_alphaTL: number

**Description:**

Private internal value. Holds the top-left alpha value.

**Access:** private

**Inherits:** [Phaser.GameObjects.Components.Alpha#\_alphaTL](../namespace/gameobjects-components-alpha.md)

> Source: [src/gameobjects/components/Alpha.js#L33](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Alpha.js#L33)  
> Since: 3.0.0

---

## \_alphaTR

### \_alphaTR: number

**Description:**

Private internal value. Holds the top-right alpha value.

**Access:** private

**Inherits:** [Phaser.GameObjects.Components.Alpha#\_alphaTR](../namespace/gameobjects-components-alpha.md)

> Source: [src/gameobjects/components/Alpha.js#L44](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Alpha.js#L44)  
> Since: 3.0.0

---

## \_bounds

### \_bounds: [Phaser.Geom.Rectangle](geom-rectangle.md)

**Description:**

The bounds the camera is restrained to during scrolling.

**Access:** private

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#\_bounds](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L247](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L247)  
> Since: 3.0.0

---

## \_customViewport

### \_customViewport: boolean

**Description:**

Does this Camera have a custom viewport?

**Access:** private

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#\_customViewport](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L459](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L459)  
> Since: 3.12.0

---

## \_follow

### \_follow: any

**Description:**

Internal follow target reference.

**Access:** private

> Source: [src/cameras/2d/Camera.js#L194](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/Camera.js#L194)  
> Since: 3.0.0

---

## \_height

### \_height: number

**Description:**

The height of the Camera viewport, in pixels.

The viewport is the area into which the Camera renders. Setting the viewport does

not restrict where the Camera can scroll to.

**Access:** private

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#\_height](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L234](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L234)  
> Since: 3.11.0

---

## \_maskCamera

### \_maskCamera: [Phaser.Cameras.Scene2D.BaseCamera](cameras-scene2d-basecamera.md)

**Description:**

The Camera that this Camera uses for translation during masking.

If the mask is fixed in position this will be a reference to

the CameraManager.default instance. Otherwise, it'll be a reference

to itself.

**Access:** private

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#\_maskCamera](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L480](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L480)  
> Since: 3.17.0

---

## \_rotation

### \_rotation: number

**Description:**

The rotation of the Camera in radians.

Camera rotation always takes place based on the Camera viewport. By default, rotation happens

in the center of the viewport. You can adjust this with the `originX` and `originY` properties.

Rotation influences the rendering of *all* Game Objects visible by this Camera. However, it does not

rotate the Camera viewport itself, which always remains an axis-aligned rectangle.

**Access:** private

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#\_rotation](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L331](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L331)  
> Since: 3.11.0

---

## \_scrollX

### \_scrollX: number

**Description:**

The horizontal scroll position of this Camera.

Change this value to cause the Camera to scroll around your Scene.

Alternatively, setting the Camera to follow a Game Object, via the `startFollow` method,

will automatically adjust the Camera scroll values accordingly.

You can set the bounds within which the Camera can scroll via the `setBounds` method.

**Access:** private

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#\_scrollX](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L257](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L257)  
> Since: 3.11.0

---

## \_scrollY

### \_scrollY: number

**Description:**

The vertical scroll position of this Camera.

Change this value to cause the Camera to scroll around your Scene.

Alternatively, setting the Camera to follow a Game Object, via the `startFollow` method,

will automatically adjust the Camera scroll values accordingly.

You can set the bounds within which the Camera can scroll via the `setBounds` method.

**Access:** private

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#\_scrollY](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L275](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L275)  
> Since: 3.11.0

---

## \_visible

### \_visible: boolean

**Description:**

Private internal value. Holds the visible value.

**Access:** private

**Inherits:** [Phaser.GameObjects.Components.Visible#\_visible](../namespace/gameobjects-components-visible.md)

> Source: [src/gameobjects/components/Visible.js#L20](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Visible.js#L20)  
> Since: 3.0.0

---

## \_width

### \_width: number

**Description:**

The width of the Camera viewport, in pixels.

The viewport is the area into which the Camera renders. Setting the viewport does

not restrict where the Camera can scroll to.

**Access:** private

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#\_width](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L221](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L221)  
> Since: 3.11.0

---

## \_x

### \_x: number

**Description:**

The x position of the Camera viewport, relative to the top-left of the game canvas.

The viewport is the area into which the camera renders.

To adjust the position the camera is looking at in the game world, see the `scrollX` value.

**Access:** private

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#\_x](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L197](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L197)  
> Since: 3.0.0

---

## \_y

### \_y: number

**Description:**

The y position of the Camera, relative to the top-left of the game canvas.

The viewport is the area into which the camera renders.

To adjust the position the camera is looking at in the game world, see the `scrollY` value.

**Access:** private

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#\_y](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L209](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L209)  
> Since: 3.0.0

---

## \_zoomX

### \_zoomX: number

**Description:**

The Camera horizontal zoom value. Change this value to zoom in, or out of, a Scene.

A value of 0.5 would zoom the Camera out, so you can now see twice as much

of the Scene as before. A value of 2 would zoom the Camera in, so every pixel

now takes up 2 pixels when rendered.

Set to 1 to return to the default zoom level.

Be careful to never set this value to zero.

**Access:** private

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#\_zoomX](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L293](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L293)  
> Since: 3.50.0

---

## \_zoomY

### \_zoomY: number

**Description:**

The Camera vertical zoom value. Change this value to zoom in, or out of, a Scene.

A value of 0.5 would zoom the Camera out, so you can now see twice as much

of the Scene as before. A value of 2 would zoom the Camera in, so every pixel

now takes up 2 pixels when rendered.

Set to 1 to return to the default zoom level.

Be careful to never set this value to zero.

**Access:** private

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#\_zoomY](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L312](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L312)  
> Since: 3.50.0

---

## culledObjects

### culledObjects: Array.<[Phaser.GameObjects.GameObject](gameobjects-gameobject.md)>

**Description:**

A temporary array of culled objects.

**Access:** private

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#culledObjects](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L399](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L399)  
> Since: 3.0.0

---

## matrix

### matrix: [Phaser.GameObjects.Components.TransformMatrix](gameobjects-components-transformmatrix.md)

**Description:**

A local transform matrix used for internal calculations.

**Access:** private

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#matrix](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L348](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L348)  
> Since: 3.0.0

---

## rotation

### rotation: number

**Description:**

The rotation of the Camera in radians.

Camera rotation always takes place based on the Camera viewport. By default, rotation happens

in the center of the viewport. You can adjust this with the `originX` and `originY` properties.

Rotation influences the rendering of *all* Game Objects visible by this Camera. However, it does not

rotate the Camera viewport itself, which always remains an axis-aligned rectangle.

**Access:** private

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#rotation](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L1849](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L1849)  
> Since: 3.11.0

---

# Public Methods

## addListener

### <instance> addListener(event, fn, [context])

**Description:**

Add a listener for a given event.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| event | string | symbol | No |  | The event name. |
| --- | --- | --- | --- | --- |
| fn | function | No |  | The listener function. |
| context | \* | Yes | "this" | The context to invoke the listener with. |

**Returns:** [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#addListener](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L111](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L111)  
> Since: 3.0.0

---

## addToRenderList

### <instance> addToRenderList(child)

**Description:**

Adds the given Game Object to this cameras render list.

This is invoked during the rendering stage. Only objects that are actually rendered

will appear in the render list.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| child | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No | The Game Object to add to the render list. |
| --- | --- | --- | --- |

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#addToRenderList](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L538](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L538)  
> Since: 3.52.0

---

## centerOn

### <instance> centerOn(x, y)

**Description:**

Moves the Camera so that it is centered on the given coordinates, bounds allowing.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The horizontal coordinate to center on. |
| --- | --- | --- | --- |
| y | number | No | The vertical coordinate to center on. |

**Returns:** [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) - This Camera instance.

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#centerOn](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L682](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L682)  
> Since: 3.11.0

---

## centerOnX

### <instance> centerOnX(x)

**Description:**

Moves the Camera horizontally so that it is centered on the given x coordinate, bounds allowing.

Calling this does not change the scrollY value.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The horizontal coordinate to center on. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) - This Camera instance.

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#centerOnX](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L628](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L628)  
> Since: 3.16.0

---

## centerOnY

### <instance> centerOnY(y)

**Description:**

Moves the Camera vertically so that it is centered on the given y coordinate, bounds allowing.

Calling this does not change the scrollX value.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| y | number | No | The vertical coordinate to center on. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) - This Camera instance.

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#centerOnY](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L655](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L655)  
> Since: 3.16.0

---

## centerToBounds

### <instance> centerToBounds()

**Description:**

Moves the Camera so that it is looking at the center of the Camera Bounds, if enabled.

**Returns:** [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) - This Camera instance.

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#centerToBounds](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L701](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L701)  
> Since: 3.0.0

---

## centerToSize

### <instance> centerToSize()

**Description:**

Moves the Camera so that it is re-centered based on its viewport size.

**Returns:** [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) - This Camera instance.

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#centerToSize](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L726](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L726)  
> Since: 3.0.0

---

## clampX

### <instance> clampX(x)

**Description:**

Takes an x value and checks it's within the range of the Camera bounds, adjusting if required.

Do not call this method if you are not using camera bounds.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The value to horizontally scroll clamp. |
| --- | --- | --- | --- |

**Returns:** number - The adjusted value to use as scrollX.

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#clampX](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L931](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L931)  
> Since: 3.11.0

---

## clampY

### <instance> clampY(y)

**Description:**

Takes a y value and checks it's within the range of the Camera bounds, adjusting if required.

Do not call this method if you are not using camera bounds.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| y | number | No | The value to vertically scroll clamp. |
| --- | --- | --- | --- |

**Returns:** number - The adjusted value to use as scrollY.

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#clampY](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L963](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L963)  
> Since: 3.11.0

---

## clearAlpha

### <instance> clearAlpha()

**Description:**

Clears all alpha values associated with this Game Object.

Immediately sets the alpha levels back to 1 (fully opaque).

**Returns:** [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Alpha#clearAlpha](../namespace/gameobjects-components-alpha.md)

> Source: [src/gameobjects/components/Alpha.js#L77](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Alpha.js#L77)  
> Since: 3.0.0

---

## clearFX

### <instance> clearFX()

**Description:**

Removes all Pre and Post FX Controllers from this Game Object.

If you wish to remove a single controller, use the `preFX.remove(fx)` or `postFX.remove(fx)` methods instead.

If you wish to clear a single controller, use the `preFX.clear()` or `postFX.clear()` methods instead.

**Tags:**

* webglOnly

**Returns:** [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) - This Game Object.

**Inherits:** [Phaser.GameObjects.Components.PostPipeline#clearFX](../namespace/gameobjects-components-postpipeline.md)

> Source: [src/gameobjects/components/PostPipeline.js#L337](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/PostPipeline.js#L337)  
> Since: 3.60.0

---

## clearMask

### <instance> clearMask([destroyMask])

**Description:**

Clears the mask that this Camera was using.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| destroyMask | boolean | Yes | false | Destroy the mask before clearing it? |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) - This Camera instance.

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#clearMask](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L1413](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L1413)  
> Since: 3.17.0

---

## cull

### <instance> cull(renderableObjects)

**Description:**

Takes an array of Game Objects and returns a new array featuring only those objects

visible by this camera.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| renderableObjects | Array.<[Phaser.GameObjects.GameObject](gameobjects-gameobject.md)> | No | An array of Game Objects to cull. |
| --- | --- | --- | --- |

**Returns:** Array.<[Phaser.GameObjects.GameObject](gameobjects-gameobject.md)> - An array of Game Objects visible to this Camera.

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#cull](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L742](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L742)  
> Since: 3.0.0

---

## destroy

### <instance> destroy()

**Description:**

Destroys this Camera instance. You rarely need to call this directly.

Called by the Camera Manager. If you wish to destroy a Camera please use `CameraManager.remove` as

cameras are stored in a pool, ready for recycling later, and calling this directly will prevent that.

**Overrides:** Phaser.Cameras.Scene2D.BaseCamera#destroy

**Fires:** [Phaser.Cameras.Scene2D.Events#event:DESTROY](../event/cameras-scene2d-events.md)

> Source: [src/cameras/2d/Camera.js#L780](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/Camera.js#L780)  
> Since: 3.0.0

---

## emit

### <instance> emit(event, [args])

**Description:**

Calls each of the listeners registered for a given event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | string | symbol | No | The event name. |
| --- | --- | --- | --- |
| args | \* | Yes | Additional arguments that will be passed to the event handler. |

**Returns:** boolean - `true` if the event had listeners, else `false`.

**Inherits:** [Phaser.Events.EventEmitter#emit](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L86](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L86)  
> Since: 3.0.0

---

## eventNames

### <instance> eventNames()

**Description:**

Return an array listing the events for which the emitter has registered listeners.

**Returns:** Array.<(string | symbol)> - undefined

**Inherits:** [Phaser.Events.EventEmitter#eventNames](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L55](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L55)  
> Since: 3.0.0

---

## fade

### <instance> fade([duration], [red], [green], [blue], [force], [callback], [context])

**Description:**

Fades the Camera from transparent to the given color over the duration specified.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| duration | number | Yes | 1000 | The duration of the effect in milliseconds. |
| --- | --- | --- | --- | --- |
| red | number | Yes | 0 | The amount to fade the red channel towards. A value between 0 and 255. |
| green | number | Yes | 0 | The amount to fade the green channel towards. A value between 0 and 255. |
| blue | number | Yes | 0 | The amount to fade the blue channel towards. A value between 0 and 255. |
| force | boolean | Yes | false | Force the effect to start immediately, even if already running. |
| callback | function | Yes |  | This callback will be invoked every frame for the duration of the effect. It is sent two arguments: A reference to the camera and a progress amount between 0 and 1 indicating how complete the effect is. |
| context | any | Yes |  | The context in which the callback is invoked. Defaults to the Scene to which the Camera belongs. |

**Returns:** [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) - This Camera instance.

**Fires:** [Phaser.Cameras.Scene2D.Events#event:FADE\_OUT\_START](../event/cameras-scene2d-events.md), [Phaser.Cameras.Scene2D.Events#event:FADE\_OUT\_COMPLETE](../event/cameras-scene2d-events.md)

> Source: [src/cameras/2d/Camera.js#L339](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/Camera.js#L339)  
> Since: 3.0.0

---

## fadeFrom

### <instance> fadeFrom([duration], [red], [green], [blue], [force], [callback], [context])

**Description:**

Fades the Camera from the given color to transparent over the duration specified.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| duration | number | Yes | 1000 | The duration of the effect in milliseconds. |
| --- | --- | --- | --- | --- |
| red | number | Yes | 0 | The amount to fade the red channel towards. A value between 0 and 255. |
| green | number | Yes | 0 | The amount to fade the green channel towards. A value between 0 and 255. |
| blue | number | Yes | 0 | The amount to fade the blue channel towards. A value between 0 and 255. |
| force | boolean | Yes | false | Force the effect to start immediately, even if already running. |
| callback | function | Yes |  | This callback will be invoked every frame for the duration of the effect. It is sent two arguments: A reference to the camera and a progress amount between 0 and 1 indicating how complete the effect is. |
| context | any | Yes |  | The context in which the callback is invoked. Defaults to the Scene to which the Camera belongs. |

**Returns:** [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) - This Camera instance.

**Fires:** [Phaser.Cameras.Scene2D.Events#event:FADE\_IN\_START](../event/cameras-scene2d-events.md), [Phaser.Cameras.Scene2D.Events#event:FADE\_IN\_COMPLETE](../event/cameras-scene2d-events.md)

> Source: [src/cameras/2d/Camera.js#L315](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/Camera.js#L315)  
> Since: 3.5.0

---

## fadeIn

### <instance> fadeIn([duration], [red], [green], [blue], [callback], [context])

**Description:**

Fades the Camera in from the given color over the duration specified.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| duration | number | Yes | 1000 | The duration of the effect in milliseconds. |
| --- | --- | --- | --- | --- |
| red | number | Yes | 0 | The amount to fade the red channel towards. A value between 0 and 255. |
| green | number | Yes | 0 | The amount to fade the green channel towards. A value between 0 and 255. |
| blue | number | Yes | 0 | The amount to fade the blue channel towards. A value between 0 and 255. |
| callback | function | Yes |  | This callback will be invoked every frame for the duration of the effect. It is sent two arguments: A reference to the camera and a progress amount between 0 and 1 indicating how complete the effect is. |
| context | any | Yes |  | The context in which the callback is invoked. Defaults to the Scene to which the Camera belongs. |

**Returns:** [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) - This Camera instance.

**Fires:** [Phaser.Cameras.Scene2D.Events#event:FADE\_IN\_START](../event/cameras-scene2d-events.md), [Phaser.Cameras.Scene2D.Events#event:FADE\_IN\_COMPLETE](../event/cameras-scene2d-events.md)

> Source: [src/cameras/2d/Camera.js#L268](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/Camera.js#L268)  
> Since: 3.3.0

---

## fadeOut

### <instance> fadeOut([duration], [red], [green], [blue], [callback], [context])

**Description:**

Fades the Camera out to the given color over the duration specified.

This is an alias for Camera.fade that forces the fade to start, regardless of existing fades.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| duration | number | Yes | 1000 | The duration of the effect in milliseconds. |
| --- | --- | --- | --- | --- |
| red | number | Yes | 0 | The amount to fade the red channel towards. A value between 0 and 255. |
| green | number | Yes | 0 | The amount to fade the green channel towards. A value between 0 and 255. |
| blue | number | Yes | 0 | The amount to fade the blue channel towards. A value between 0 and 255. |
| callback | function | Yes |  | This callback will be invoked every frame for the duration of the effect. It is sent two arguments: A reference to the camera and a progress amount between 0 and 1 indicating how complete the effect is. |
| context | any | Yes |  | The context in which the callback is invoked. Defaults to the Scene to which the Camera belongs. |

**Returns:** [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) - This Camera instance.

**Fires:** [Phaser.Cameras.Scene2D.Events#event:FADE\_OUT\_START](../event/cameras-scene2d-events.md), [Phaser.Cameras.Scene2D.Events#event:FADE\_OUT\_COMPLETE](../event/cameras-scene2d-events.md)

> Source: [src/cameras/2d/Camera.js#L291](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/Camera.js#L291)  
> Since: 3.3.0

---

## flash

### <instance> flash([duration], [red], [green], [blue], [force], [callback], [context])

**Description:**

Flashes the Camera by setting it to the given color immediately and then fading it away again quickly over the duration specified.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| duration | number | Yes | 250 | The duration of the effect in milliseconds. |
| --- | --- | --- | --- | --- |
| red | number | Yes | 255 | The amount to fade the red channel towards. A value between 0 and 255. |
| green | number | Yes | 255 | The amount to fade the green channel towards. A value between 0 and 255. |
| blue | number | Yes | 255 | The amount to fade the blue channel towards. A value between 0 and 255. |
| force | boolean | Yes | false | Force the effect to start immediately, even if already running. |
| callback | function | Yes |  | This callback will be invoked every frame for the duration of the effect. It is sent two arguments: A reference to the camera and a progress amount between 0 and 1 indicating how complete the effect is. |
| context | any | Yes |  | The context in which the callback is invoked. Defaults to the Scene to which the Camera belongs. |

**Returns:** [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) - This Camera instance.

**Fires:** [Phaser.Cameras.Scene2D.Events#event:FLASH\_START](../event/cameras-scene2d-events.md), [Phaser.Cameras.Scene2D.Events#event:FLASH\_COMPLETE](../event/cameras-scene2d-events.md)

> Source: [src/cameras/2d/Camera.js#L363](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/Camera.js#L363)  
> Since: 3.0.0

---

## getBounds

### <instance> getBounds([out])

**Description:**

Returns a rectangle containing the bounds of the Camera.

If the Camera does not have any bounds the rectangle will be empty.

The rectangle is a copy of the bounds, so is safe to modify.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| out | [Phaser.Geom.Rectangle](geom-rectangle.md) | Yes | An optional Rectangle to store the bounds in. If not given, a new Rectangle will be created. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Geom.Rectangle](geom-rectangle.md) - A rectangle containing the bounds of this Camera.

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#getBounds](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L1118](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L1118)  
> Since: 3.16.0

---

## getPostPipeline

### <instance> getPostPipeline(pipeline)

**Description:**

Gets a Post Pipeline instance from this Game Object, based on the given name, and returns it.

**Tags:**

* webglOnly

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pipeline | string | function | [Phaser.Renderer.WebGL.Pipelines.PostFXPipeline](renderer-webgl-pipelines-postfxpipeline.md) | No |
| --- | --- | --- | --- |

**Returns:** [Phaser.Renderer.WebGL.Pipelines.PostFXPipeline](renderer-webgl-pipelines-postfxpipeline.md), Array.<[Phaser.Renderer.WebGL.Pipelines.PostFXPipeline](renderer-webgl-pipelines-postfxpipeline.md)> - An array of all the Post Pipelines matching the name. This array will be empty if there was no match. If there was only one single match, that pipeline is returned directly, not in an array.

**Inherits:** [Phaser.GameObjects.Components.PostPipeline#getPostPipeline](../namespace/gameobjects-components-postpipeline.md)

> Source: [src/gameobjects/components/PostPipeline.js#L237](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/PostPipeline.js#L237)  
> Since: 3.60.0

---

## getScroll

### <instance> getScroll(x, y, [out])

**Description:**

Calculates what the Camera.scrollX and scrollY values would need to be in order to move

the Camera so it is centered on the given x and y coordinates, without actually moving

the Camera there. The results are clamped based on the Camera bounds, if set.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The horizontal coordinate to center on. |
| --- | --- | --- | --- |
| y | number | No | The vertical coordinate to center on. |
| out | [Phaser.Math.Vector2](math-vector2.md) | Yes | A Vector2 to store the values in. If not given a new Vector2 is created. |

**Returns:** [Phaser.Math.Vector2](math-vector2.md) - The scroll coordinates stored in the `x` and `y` properties.

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#getScroll](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L595](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L595)  
> Since: 3.11.0

---

## getWorldPoint

### <instance> getWorldPoint(x, y, [output])

**Description:**

Converts the given `x` and `y` coordinates into World space, based on this Cameras transform.

You can optionally provide a Vector2, or similar object, to store the results in.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The x position to convert to world space. |
| --- | --- | --- | --- |
| y | number | No | The y position to convert to world space. |
| output | object | [Phaser.Math.Vector2](math-vector2.md) | Yes | An optional object to store the results in. If not provided a new Vector2 will be created. |

**Returns:** [Phaser.Math.Vector2](math-vector2.md) - An object holding the converted values in its `x` and `y` properties.

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#getWorldPoint](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L823](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L823)  
> Since: 3.0.0

---

## ignore

### <instance> ignore(entries)

**Description:**

Given a Game Object, or an array of Game Objects, it will update all of their camera filter settings

so that they are ignored by this Camera. This means they will not be rendered by this Camera.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| entries | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | Array.<[Phaser.GameObjects.GameObject](gameobjects-gameobject.md)> | [Phaser.GameObjects.Group](gameobjects-group.md) | [Phaser.GameObjects.Layer](gameobjects-layer.md) |
| --- | --- | --- | --- |

**Returns:** [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) - This Camera instance.

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#ignore](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L890](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L890)  
> Since: 3.0.0

---

## initPostPipeline

### <instance> initPostPipeline([preFX])

**Description:**

This should only be called during the instantiation of the Game Object.

It is called by default by all core Game Objects and doesn't need

calling again.

After that, use `setPostPipeline`.

**Tags:**

* webglOnly

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| preFX | boolean | Yes | false | Does this Game Object support Pre FX? |
| --- | --- | --- | --- | --- |

**Inherits:** [Phaser.GameObjects.Components.PostPipeline#initPostPipeline](../namespace/gameobjects-components-postpipeline.md)

> Source: [src/gameobjects/components/PostPipeline.js#L113](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/PostPipeline.js#L113)  
> Since: 3.60.0

---

## listenerCount

### <instance> listenerCount(event)

**Description:**

Return the number of listeners listening to a given event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | string | symbol | No | The event name. |
| --- | --- | --- | --- |

**Returns:** number - The number of listeners.

**Inherits:** [Phaser.Events.EventEmitter#listenerCount](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L75](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L75)  
> Since: 3.0.0

---

## listeners

### <instance> listeners(event)

**Description:**

Return the listeners registered for a given event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | string | symbol | No | The event name. |
| --- | --- | --- | --- |

**Returns:** Array.<function()> - The registered listeners.

**Inherits:** [Phaser.Events.EventEmitter#listeners](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L64](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L64)  
> Since: 3.0.0

---

## off

### <instance> off(event, [fn], [context], [once])

**Description:**

Remove the listeners of a given event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | string | symbol | No | The event name. |
| --- | --- | --- | --- |
| fn | function | Yes | Only remove the listeners that match this function. |
| context | \* | Yes | Only remove the listeners that have this context. |
| once | boolean | Yes | Only remove one-time listeners. |

**Returns:** [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#off](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L151](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L151)  
> Since: 3.0.0

---

## on

### <instance> on(event, fn, [context])

**Description:**

Add a listener for a given event.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| event | string | symbol | No |  | The event name. |
| --- | --- | --- | --- | --- |
| fn | function | No |  | The listener function. |
| context | \* | Yes | "this" | The context to invoke the listener with. |

**Returns:** [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#on](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L98](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L98)  
> Since: 3.0.0

---

## once

### <instance> once(event, fn, [context])

**Description:**

Add a one-time listener for a given event.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| event | string | symbol | No |  | The event name. |
| --- | --- | --- | --- | --- |
| fn | function | No |  | The listener function. |
| context | \* | Yes | "this" | The context to invoke the listener with. |

**Returns:** [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#once](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L124](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L124)  
> Since: 3.0.0

---

## pan

### <instance> pan(x, y, [duration], [ease], [force], [callback], [context])

**Description:**

This effect will scroll the Camera so that the center of its viewport finishes at the given destination,

over the duration and with the ease specified.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | No |  | The destination x coordinate to scroll the center of the Camera viewport to. |
| --- | --- | --- | --- | --- |
| y | number | No |  | The destination y coordinate to scroll the center of the Camera viewport to. |
| duration | number | Yes | 1000 | The duration of the effect in milliseconds. |
| ease | string | function | Yes | "'Linear'" | The ease to use for the pan. Can be any of the Phaser Easing constants or a custom function. |
| force | boolean | Yes | false | Force the pan effect to start immediately, even if already running. |
| callback | [Phaser.Types.Cameras.Scene2D.CameraPanCallback](../typedef/types-cameras-scene2d.md) | Yes |  | This callback will be invoked every frame for the duration of the effect. It is sent four arguments: A reference to the camera, a progress amount between 0 and 1 indicating how complete the effect is, the current camera scroll x coordinate and the current camera scroll y coordinate. |
| context | any | Yes |  | The context in which the callback is invoked. Defaults to the Scene to which the Camera belongs. |

**Returns:** [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) - This Camera instance.

**Fires:** [Phaser.Cameras.Scene2D.Events#event:PAN\_START](../event/cameras-scene2d-events.md), [Phaser.Cameras.Scene2D.Events#event:PAN\_COMPLETE](../event/cameras-scene2d-events.md)

> Source: [src/cameras/2d/Camera.js#L409](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/Camera.js#L409)  
> Since: 3.11.0

---

## preRender

### <instance> preRender()

**Description:**

Internal preRender step.

**Access:** protected

> Source: [src/cameras/2d/Camera.js#L483](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/Camera.js#L483)  
> Since: 3.0.0

---

## removeAllListeners

### <instance> removeAllListeners([event])

**Description:**

Remove all listeners, or those of the specified event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | string | symbol | Yes | The event name. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#removeAllListeners](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L165](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L165)  
> Since: 3.0.0

---

## removeBounds

### <instance> removeBounds()

**Description:**

If this Camera has previously had movement bounds set on it, this will remove them.

**Returns:** [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) - This Camera instance.

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#removeBounds](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L1000](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L1000)  
> Since: 3.0.0

---

## removeListener

### <instance> removeListener(event, [fn], [context], [once])

**Description:**

Remove the listeners of a given event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | string | symbol | No | The event name. |
| --- | --- | --- | --- |
| fn | function | Yes | Only remove the listeners that match this function. |
| context | \* | Yes | Only remove the listeners that have this context. |
| once | boolean | Yes | Only remove one-time listeners. |

**Returns:** [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#removeListener](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L137](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L137)  
> Since: 3.0.0

---

## removePostPipeline

### <instance> removePostPipeline(pipeline)

**Description:**

Removes a type of Post Pipeline instances from this Game Object, based on the given name, and destroys them.

If you wish to remove all Post Pipelines use the `resetPostPipeline` method instead.

**Tags:**

* webglOnly

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pipeline | string | [Phaser.Renderer.WebGL.Pipelines.PostFXPipeline](renderer-webgl-pipelines-postfxpipeline.md) | No | The string-based name of the pipeline, or a pipeline class. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) - This Game Object.

**Inherits:** [Phaser.GameObjects.Components.PostPipeline#removePostPipeline](../namespace/gameobjects-components-postpipeline.md)

> Source: [src/gameobjects/components/PostPipeline.js#L299](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/PostPipeline.js#L299)  
> Since: 3.60.0

---

## resetFX

### <instance> resetFX()

**Description:**

Resets any active FX, such as a fade, flash or shake. Useful to call after a fade in order to

remove the fade.

**Returns:** [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) - This Camera instance.

> Source: [src/cameras/2d/Camera.js#L737](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/Camera.js#L737)  
> Since: 3.0.0

---

## resetPostPipeline

### <instance> resetPostPipeline([resetData])

**Description:**

Resets the WebGL Post Pipelines of this Game Object. It does this by calling

the `destroy` method on each post pipeline and then clearing the local array.

**Tags:**

* webglOnly

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| resetData | boolean | Yes | false | Reset the `postPipelineData` object to being an empty object? |
| --- | --- | --- | --- | --- |

**Inherits:** [Phaser.GameObjects.Components.PostPipeline#resetPostPipeline](../namespace/gameobjects-components-postpipeline.md)

> Source: [src/gameobjects/components/PostPipeline.js#L269](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/PostPipeline.js#L269)  
> Since: 3.60.0

---

## rotateTo

### <instance> rotateTo(radians, [shortestPath], [duration], [ease], [force], [callback], [context])

**Description:**

This effect will rotate the Camera so that the viewport finishes at the given angle in radians,

over the duration and with the ease specified.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| radians | number | No |  | The destination angle in radians to rotate the Camera viewport to. If the angle is positive then the rotation is clockwise else anticlockwise |
| --- | --- | --- | --- | --- |
| shortestPath | boolean | Yes | false | If shortest path is set to true the camera will rotate in the quickest direction clockwise or anti-clockwise. |
| duration | number | Yes | 1000 | The duration of the effect in milliseconds. |
| ease | string | function | Yes | "'Linear'" | The ease to use for the rotation. Can be any of the Phaser Easing constants or a custom function. |
| force | boolean | Yes | false | Force the rotation effect to start immediately, even if already running. |
| callback | CameraRotateCallback | Yes |  | This callback will be invoked every frame for the duration of the effect. It is sent four arguments: A reference to the camera, a progress amount between 0 and 1 indicating how complete the effect is, the current camera rotation angle in radians. |
| context | any | Yes |  | The context in which the callback is invoked. Defaults to the Scene to which the Camera belongs. |

**Returns:** [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) - This Camera instance.

> Source: [src/cameras/2d/Camera.js#L435](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/Camera.js#L435)  
> Since: 3.23.0

---

## setAlpha

### <instance> setAlpha([value])

**Description:**

Set the Alpha level of this Camera. The alpha controls the opacity of the Camera as it renders.

Alpha values are provided as a float between 0, fully transparent, and 1, fully opaque.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| value | number | Yes | 1 | The Camera alpha value. |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) - This Camera instance.

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#setAlpha](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L554](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L554)  
> Since: 3.11.0

---

## setAngle

### <instance> setAngle([value])

**Description:**

Set the rotation of this Camera. This causes everything it renders to appear rotated.

Rotating a camera does not rotate the viewport itself, it is applied during rendering.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| value | number | Yes | 0 | The cameras angle of rotation, given in degrees. |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) - This Camera instance.

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#setAngle](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L1019](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L1019)  
> Since: 3.0.0

---

## setBackgroundColor

### <instance> setBackgroundColor([color])

**Description:**

Sets the background color for this Camera.

By default a Camera has a transparent background but it can be given a solid color, with any level

of transparency, via this method.

The color value can be specified using CSS color notation, hex or numbers.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| color | string | number | [Phaser.Types.Display.InputColorObject](../typedef/types-display.md) | Yes | "'rgba(0,0,0,0)'" |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) - This Camera instance.

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#setBackgroundColor](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L1040](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L1040)  
> Since: 3.0.0

---

## setBounds

### <instance> setBounds(x, y, width, height, [centerOn])

**Description:**

Set the bounds of the Camera. The bounds are an axis-aligned rectangle.

The Camera bounds controls where the Camera can scroll to, stopping it from scrolling off the

edges and into blank space. It does not limit the placement of Game Objects, or where

the Camera viewport can be positioned.

Temporarily disable the bounds by changing the boolean `Camera.useBounds`.

Clear the bounds entirely by calling `Camera.removeBounds`.

If you set bounds that are smaller than the viewport it will stop the Camera from being

able to scroll. The bounds can be positioned where-ever you wish. By default they are from

0x0 to the canvas width x height. This means that the coordinate 0x0 is the top left of

the Camera bounds. However, you can position them anywhere. So if you wanted a game world

that was 2048x2048 in size, with 0x0 being the center of it, you can set the bounds x/y

to be -1024, -1024, with a width and height of 2048. Depending on your game you may find

it easier for 0x0 to be the top-left of the bounds, or you may wish 0x0 to be the middle.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | No |  | The top-left x coordinate of the bounds. |
| --- | --- | --- | --- | --- |
| y | number | No |  | The top-left y coordinate of the bounds. |
| width | number | No |  | The width of the bounds, in pixels. |
| height | number | No |  | The height of the bounds, in pixels. |
| centerOn | boolean | Yes | false | If `true` the Camera will automatically be centered on the new bounds. |

**Returns:** [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) - This Camera instance.

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#setBounds](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L1066](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L1066)  
> Since: 3.0.0

---

## setDeadzone

### <instance> setDeadzone([width], [height])

**Description:**

Sets the Camera dead zone.

The deadzone is only used when the camera is following a target.

It defines a rectangular region within which if the target is present, the camera will not scroll.

If the target moves outside of this area, the camera will begin scrolling in order to follow it.

The deadzone rectangle is re-positioned every frame so that it is centered on the mid-point

of the camera. This allows you to use the object for additional game related checks, such as

testing if an object is within it or not via a Rectangle.contains call.

The `lerp` values that you can set for a follower target also apply when using a deadzone.

Calling this method with no arguments will reset an active deadzone.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| width | number | Yes | The width of the deadzone rectangle in pixels. If not specified the deadzone is removed. |
| --- | --- | --- | --- |
| height | number | Yes | The height of the deadzone rectangle in pixels. |

**Returns:** [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) - This Camera instance.

> Source: [src/cameras/2d/Camera.js#L206](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/Camera.js#L206)  
> Since: 3.11.0

---

## setFollowOffset

### <instance> setFollowOffset([x], [y])

**Description:**

Sets the horizontal and vertical offset of the camera from its follow target.

The values are subtracted from the targets position during the Cameras update step.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | Yes | 0 | The horizontal offset from the camera follow target.x position. |
| --- | --- | --- | --- | --- |
| y | number | Yes | 0 | The vertical offset from the camera follow target.y position. |

**Returns:** [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) - This Camera instance.

> Source: [src/cameras/2d/Camera.js#L635](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/Camera.js#L635)  
> Since: 3.9.0

---

## setIsSceneCamera

### <instance> setIsSceneCamera(value)

**Description:**

Set if this Camera is being used as a Scene Camera, or a Texture

Camera.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | boolean | No | Is this being used as a Scene Camera, or a Texture camera? |
| --- | --- | --- | --- |

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#setIsSceneCamera](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L1502](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L1502)  
> Since: 3.60.0

---

## setLerp

### <instance> setLerp([x], [y])

**Description:**

Sets the linear interpolation value to use when following a target.

The default values of 1 means the camera will instantly snap to the target coordinates.

A lower value, such as 0.1 means the camera will more slowly track the target, giving

a smooth transition. You can set the horizontal and vertical values independently, and also

adjust this value in real-time during your game.

Be sure to keep the value between 0 and 1. A value of zero will disable tracking on that axis.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | Yes | 1 | The amount added to the horizontal linear interpolation of the follow target. |
| --- | --- | --- | --- | --- |
| y | number | Yes | 1 | The amount added to the vertical linear interpolation of the follow target. |

**Returns:** [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) - This Camera instance.

> Source: [src/cameras/2d/Camera.js#L607](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/Camera.js#L607)  
> Since: 3.9.0

---

## setMask

### <instance> setMask(mask, [fixedPosition])

**Description:**

Sets the mask to be applied to this Camera during rendering.

The mask must have been previously created and can be either a GeometryMask or a BitmapMask.

Bitmap Masks only work on WebGL. Geometry Masks work on both WebGL and Canvas.

If a mask is already set on this Camera it will be immediately replaced.

Masks have no impact on physics or input detection. They are purely a rendering component

that allows you to limit what is visible during the render pass.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| mask | [Phaser.Display.Masks.BitmapMask](display-masks-bitmapmask.md) | [Phaser.Display.Masks.GeometryMask](display-masks-geometrymask.md) | No |  | The mask this Camera will use when rendering. |
| --- | --- | --- | --- | --- |
| fixedPosition | boolean | Yes | true | Should the mask translate along with the Camera, or be fixed in place and not impacted by the Cameras transform? |

**Returns:** [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) - This Camera instance.

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#setMask](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L1382](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L1382)  
> Since: 3.17.0

---

## setName

### <instance> setName([value])

**Description:**

Sets the name of this Camera.

This value is for your own use and isn't used internally.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| value | string | Yes | "''" | The name of the Camera. |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) - This Camera instance.

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#setName](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L1143](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L1143)  
> Since: 3.0.0

---

## setOrigin

### <instance> setOrigin([x], [y])

**Description:**

Sets the rotation origin of this Camera.

The values are given in the range 0 to 1 and are only used when calculating Camera rotation.

By default the camera rotates around the center of the viewport.

Changing the origin allows you to adjust the point in the viewport from which rotation happens.

A value of 0 would rotate from the top-left of the viewport. A value of 1 from the bottom right.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | Yes | 0.5 | The horizontal origin value. |
| --- | --- | --- | --- | --- |
| y | number | Yes | "x" | The vertical origin value. If not defined it will be set to the value of `x`. |

**Returns:** [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) - This Camera instance.

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#setOrigin](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L566](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L566)  
> Since: 3.11.0

---

## setPosition

### <instance> setPosition(x, [y])

**Description:**

Set the position of the Camera viewport within the game.

This does not change where the camera is 'looking'. See `setScroll` to control that.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | No |  | The top-left x coordinate of the Camera viewport. |
| --- | --- | --- | --- | --- |
| y | number | Yes | "x" | The top-left y coordinate of the Camera viewport. |

**Returns:** [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) - This Camera instance.

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#setPosition](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L1163](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L1163)  
> Since: 3.0.0

---

## setPostPipeline

### <instance> setPostPipeline(pipelines, [pipelineData], [copyData])

**Description:**

Sets one, or more, Post Pipelines on this Game Object.

Post Pipelines are invoked after this Game Object has rendered to its target and

are commonly used for post-fx.

The post pipelines are appended to the `postPipelines` array belonging to this

Game Object. When the renderer processes this Game Object, it iterates through the post

pipelines in the order in which they appear in the array. If you are stacking together

multiple effects, be aware that the order is important.

If you call this method multiple times, the new pipelines will be appended to any existing

post pipelines already set. Use the `resetPostPipeline` method to clear them first, if required.

You can optionally also set the `postPipelineData` property, if the parameter is given.

**Tags:**

* webglOnly

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| pipelines | string | Array.<string> | function | Array.<function()> | [Phaser.Renderer.WebGL.Pipelines.PostFXPipeline](renderer-webgl-pipelines-postfxpipeline.md) |
| --- | --- | --- | --- | --- |
| pipelineData | object | Yes |  | Optional pipeline data object that is set in to the `postPipelineData` property of this Game Object. |
| copyData | boolean | Yes | true | Should the pipeline data object be *deep copied* into the `postPipelineData` property of this Game Object? If `false` it will be set by reference instead. |

**Returns:** [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.PostPipeline#setPostPipeline](../namespace/gameobjects-components-postpipeline.md)

> Source: [src/gameobjects/components/PostPipeline.js#L140](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/PostPipeline.js#L140)  
> Since: 3.60.0

---

## setPostPipelineData

### <instance> setPostPipelineData(key, [value])

**Description:**

Adds an entry to the `postPipelineData` object belonging to this Game Object.

If the 'key' already exists, its value is updated. If it doesn't exist, it is created.

If `value` is undefined, and `key` exists, `key` is removed from the data object.

**Tags:**

* webglOnly

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The key of the pipeline data to set, update, or delete. |
| --- | --- | --- | --- |
| value | any | Yes | The value to be set with the key. If `undefined` then `key` will be deleted from the object. |

**Returns:** [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.PostPipeline#setPostPipelineData](../namespace/gameobjects-components-postpipeline.md)

> Source: [src/gameobjects/components/PostPipeline.js#L205](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/PostPipeline.js#L205)  
> Since: 3.60.0

---

## setRotation

### <instance> setRotation([value])

**Description:**

Set the rotation of this Camera. This causes everything it renders to appear rotated.

Rotating a camera does not rotate the viewport itself, it is applied during rendering.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| value | number | Yes | 0 | The rotation of the Camera, in radians. |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) - This Camera instance.

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#setRotation](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L1186](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L1186)  
> Since: 3.0.0

---

## setRoundPixels

### <instance> setRoundPixels(value)

**Description:**

Should the Camera round pixel values to whole integers when rendering Game Objects?

In some types of game, especially with pixel art, this is required to prevent sub-pixel aliasing.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | boolean | No | `true` to round Camera pixels, `false` to not. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) - This Camera instance.

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#setRoundPixels](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L1207](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L1207)  
> Since: 3.0.0

---

## setScene

### <instance> setScene(scene, [isSceneCamera])

**Description:**

Sets the Scene the Camera is bound to.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| scene | [Phaser.Scene](scene.md) | No |  | The Scene the camera is bound to. |
| --- | --- | --- | --- | --- |
| isSceneCamera | boolean | Yes | true | Is this Camera being used for a Scene (true) or a Texture? (false) |

**Returns:** [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) - This Camera instance.

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#setScene](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L1226](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L1226)  
> Since: 3.0.0

---

## setScroll

### <instance> setScroll(x, [y])

**Description:**

Set the position of where the Camera is looking within the game.

You can also modify the properties `Camera.scrollX` and `Camera.scrollY` directly.

Use this method, or the scroll properties, to move your camera around the game world.

This does not change where the camera viewport is placed. See `setPosition` to control that.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | No |  | The x coordinate of the Camera in the game world. |
| --- | --- | --- | --- | --- |
| y | number | Yes | "x" | The y coordinate of the Camera in the game world. |

**Returns:** [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) - This Camera instance.

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#setScroll](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L1260](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L1260)  
> Since: 3.0.0

---

## setSize

### <instance> setSize(width, [height])

**Description:**

Set the size of the Camera viewport.

By default a Camera is the same size as the game, but can be made smaller via this method,

allowing you to create mini-cam style effects by creating and positioning a smaller Camera

viewport within your game.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| width | number | No |  | The width of the Camera viewport. |
| --- | --- | --- | --- | --- |
| height | number | Yes | "width" | The height of the Camera viewport. |

**Returns:** [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) - This Camera instance.

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#setSize](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L1285](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L1285)  
> Since: 3.0.0

---

## setViewport

### <instance> setViewport(x, y, width, [height])

**Description:**

This method sets the position and size of the Camera viewport in a single call.

If you're trying to change where the Camera is looking at in your game, then see

the method `Camera.setScroll` instead. This method is for changing the viewport

itself, not what the camera can see.

By default a Camera is the same size as the game, but can be made smaller via this method,

allowing you to create mini-cam style effects by creating and positioning a smaller Camera

viewport within your game.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | No |  | The top-left x coordinate of the Camera viewport. |
| --- | --- | --- | --- | --- |
| y | number | No |  | The top-left y coordinate of the Camera viewport. |
| width | number | No |  | The width of the Camera viewport. |
| height | number | Yes | "width" | The height of the Camera viewport. |

**Returns:** [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) - This Camera instance.

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#setViewport](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L1310](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L1310)  
> Since: 3.0.0

---

## setVisible

### <instance> setVisible(value)

**Description:**

Sets the visibility of this Camera.

An invisible Camera will skip rendering and input tests of everything it can see.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | boolean | No | The visible state of the Camera. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) - This Camera instance.

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#setVisible](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L1437](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L1437)  
> Since: 3.10.0

---

## setZoom

### <instance> setZoom([x], [y])

**Description:**

Set the zoom value of the Camera.

Changing to a smaller value, such as 0.5, will cause the camera to 'zoom out'.

Changing to a larger value, such as 2, will cause the camera to 'zoom in'.

A value of 1 means 'no zoom' and is the default.

Changing the zoom does not impact the Camera viewport in any way, it is only applied during rendering.

As of Phaser 3.50 you can now set the horizontal and vertical zoom values independently.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | Yes | 1 | The horizontal zoom value of the Camera. The minimum it can be is 0.001. |
| --- | --- | --- | --- | --- |
| y | number | Yes | "x" | The vertical zoom value of the Camera. The minimum it can be is 0.001. |

**Returns:** [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) - This Camera instance.

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#setZoom](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L1341](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L1341)  
> Since: 3.0.0

---

## shake

### <instance> shake([duration], [intensity], [force], [callback], [context])

**Description:**

Shakes the Camera by the given intensity over the duration specified.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| duration | number | Yes | 100 | The duration of the effect in milliseconds. |
| --- | --- | --- | --- | --- |
| intensity | number | [Phaser.Math.Vector2](math-vector2.md) | Yes | 0.05 | The intensity of the shake. |
| force | boolean | Yes | false | Force the shake effect to start immediately, even if already running. |
| callback | function | Yes |  | This callback will be invoked every frame for the duration of the effect. It is sent two arguments: A reference to the camera and a progress amount between 0 and 1 indicating how complete the effect is. |
| context | any | Yes |  | The context in which the callback is invoked. Defaults to the Scene to which the Camera belongs. |

**Returns:** [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) - This Camera instance.

**Fires:** [Phaser.Cameras.Scene2D.Events#event:SHAKE\_START](../event/cameras-scene2d-events.md), [Phaser.Cameras.Scene2D.Events#event:SHAKE\_COMPLETE](../event/cameras-scene2d-events.md)

> Source: [src/cameras/2d/Camera.js#L387](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/Camera.js#L387)  
> Since: 3.0.0

---

## shutdown

### <instance> shutdown()

**Description:**

Removes all listeners.

**Inherits:** [Phaser.Events.EventEmitter#shutdown](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L31](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L31)  
> Since: 3.0.0

---

## startFollow

### <instance> startFollow(target, [roundPixels], [lerpX], [lerpY], [offsetX], [offsetY])

**Description:**

Sets the Camera to follow a Game Object.

When enabled the Camera will automatically adjust its scroll position to keep the target Game Object

in its center.

You can set the linear interpolation value used in the follow code.

Use low lerp values (such as 0.1) to automatically smooth the camera motion.

If you find you're getting a slight "jitter" effect when following an object it's probably to do with sub-pixel

rendering of the targets position. This can be rounded by setting the `roundPixels` argument to `true` to

force full pixel rounding rendering. Note that this can still be broken if you have specified a non-integer zoom

value on the camera. So be sure to keep the camera zoom to integers.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| target | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | object | No |  | The target for the Camera to follow. |
| --- | --- | --- | --- | --- |
| roundPixels | boolean | Yes | false | Round the camera position to whole integers to avoid sub-pixel rendering? |
| lerpX | number | Yes | 1 | A value between 0 and 1. This value specifies the amount of linear interpolation to use when horizontally tracking the target. The closer the value to 1, the faster the camera will track. |
| lerpY | number | Yes | 1 | A value between 0 and 1. This value specifies the amount of linear interpolation to use when vertically tracking the target. The closer the value to 1, the faster the camera will track. |
| offsetX | number | Yes | 0 | The horizontal offset from the camera follow target.x position. |
| offsetY | number | Yes | 0 | The vertical offset from the camera follow target.y position. |

**Returns:** [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) - This Camera instance.

> Source: [src/cameras/2d/Camera.js#L657](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/Camera.js#L657)  
> Since: 3.0.0

---

## stopFollow

### <instance> stopFollow()

**Description:**

Stops a Camera from following a Game Object, if previously set via `Camera.startFollow`.

**Returns:** [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) - This Camera instance.

> Source: [src/cameras/2d/Camera.js#L722](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/Camera.js#L722)  
> Since: 3.0.0

---

## toJSON

### <instance> toJSON()

**Description:**

Returns an Object suitable for JSON storage containing all of the Camera viewport and rendering properties.

**Returns:** [Phaser.Types.Cameras.Scene2D.JSONCamera](../typedef/types-cameras-scene2d.md) - A well-formed object suitable for conversion to JSON.

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#toJSON](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L1450](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L1450)  
> Since: 3.0.0

---

## update

### <instance> update(time, delta)

**Description:**

Internal method called automatically by the Camera Manager.

**Access:** protected

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| time | number | No | The current timestamp as generated by the Request Animation Frame or SetTimeout. |
| --- | --- | --- | --- |
| delta | number | No | The delta time, in ms, elapsed since the last frame. |

**Overrides:** Phaser.Cameras.Scene2D.BaseCamera#update

> Source: [src/cameras/2d/Camera.js#L757](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/Camera.js#L757)  
> Since: 3.0.0

---

## zoomTo

### <instance> zoomTo(zoom, [duration], [ease], [force], [callback], [context])

**Description:**

This effect will zoom the Camera to the given scale, over the duration and with the ease specified.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| zoom | number | No |  | The target Camera zoom value. |
| --- | --- | --- | --- | --- |
| duration | number | Yes | 1000 | The duration of the effect in milliseconds. |
| ease | string | function | Yes | "'Linear'" | The ease to use for the pan. Can be any of the Phaser Easing constants or a custom function. |
| force | boolean | Yes | false | Force the pan effect to start immediately, even if already running. |
| callback | [Phaser.Types.Cameras.Scene2D.CameraPanCallback](../typedef/types-cameras-scene2d.md) | Yes |  | This callback will be invoked every frame for the duration of the effect. It is sent four arguments: A reference to the camera, a progress amount between 0 and 1 indicating how complete the effect is, the current camera scroll x coordinate and the current camera scroll y coordinate. |
| context | any | Yes |  | The context in which the callback is invoked. Defaults to the Scene to which the Camera belongs. |

**Returns:** [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) - This Camera instance.

**Fires:** [Phaser.Cameras.Scene2D.Events#event:ZOOM\_START](../event/cameras-scene2d-events.md), [Phaser.Cameras.Scene2D.Events#event:ZOOM\_COMPLETE](../event/cameras-scene2d-events.md)

> Source: [src/cameras/2d/Camera.js#L459](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/Camera.js#L459)  
> Since: 3.11.0

---

# Private Methods

## updateSystem

### <instance> updateSystem()

**Description:**

Internal method called automatically when the viewport changes.

**Access:** private

**Inherits:** [Phaser.Cameras.Scene2D.BaseCamera#updateSystem](cameras-scene2d-basecamera.md)

> Source: [src/cameras/2d/BaseCamera.js#L1518](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/BaseCamera.js#L1518)  
> Since: 3.12.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [alpha](#alpha)

    - [alpha: number](#alpha-number)
  + [alphaBottomLeft](#alphabottomleft)

    - [alphaBottomLeft: number](#alphabottomleft-number)
  + [alphaBottomRight](#alphabottomright)

    - [alphaBottomRight: number](#alphabottomright-number)
  + [alphaTopLeft](#alphatopleft)

    - [alphaTopLeft: number](#alphatopleft-number)
  + [alphaTopRight](#alphatopright)

    - [alphaTopRight: number](#alphatopright-number)
  + [backgroundColor](#backgroundcolor)

    - [backgroundColor: Phaser.Display.Color](#backgroundcolor-phaserdisplaycolor)
  + [cameraManager](#cameramanager)

    - [cameraManager: Phaser.Cameras.Scene2D.CameraManager](#cameramanager-phasercamerasscene2dcameramanager)
  + [centerX](#centerx)

    - [centerX: number](#centerx-number)
  + [centerY](#centery)

    - [centerY: number](#centery-number)
  + [deadzone](#deadzone)

    - [deadzone: Phaser.Geom.Rectangle](#deadzone-phasergeomrectangle)
  + [dirty](#dirty)

    - [dirty: boolean](#dirty-boolean)
  + [disableCull](#disablecull)

    - [disableCull: boolean](#disablecull-boolean)
  + [displayHeight](#displayheight)

    - [displayHeight: number](#displayheight-number)
  + [displayWidth](#displaywidth)

    - [displayWidth: number](#displaywidth-number)
  + [fadeEffect](#fadeeffect)

    - [fadeEffect: Phaser.Cameras.Scene2D.Effects.Fade](#fadeeffect-phasercamerasscene2deffectsfade)
  + [flashEffect](#flasheffect)

    - [flashEffect: Phaser.Cameras.Scene2D.Effects.Flash](#flasheffect-phasercamerasscene2deffectsflash)
  + [followOffset](#followoffset)

    - [followOffset: Phaser.Math.Vector2](#followoffset-phasermathvector2)
  + [hasPostPipeline](#haspostpipeline)

    - [hasPostPipeline: boolean](#haspostpipeline-boolean)
  + [height](#height)

    - [height: number](#height-number)
  + [id](#id)

    - [id: number](#id-number)
  + [inputEnabled](#inputenabled)

    - [inputEnabled: boolean](#inputenabled-boolean)
  + [isSceneCamera](#isscenecamera)

    - [isSceneCamera: boolean](#isscenecamera-boolean)
  + [lerp](#lerp)

    - [lerp: Phaser.Math.Vector2](#lerp-phasermathvector2)
  + [mask](#mask)

    - [mask: Phaser.Display.Masks.BitmapMask, Phaser.Display.Masks.GeometryMask](#mask-phaserdisplaymasksbitmapmask-phaserdisplaymasksgeometrymask)
  + [midPoint](#midpoint)

    - [midPoint: Phaser.Math.Vector2](#midpoint-phasermathvector2)
  + [name](#name)

    - [name: string](#name-string)
  + [originX](#originx)

    - [originX: number](#originx-number)
  + [originY](#originy)

    - [originY: number](#originy-number)
  + [panEffect](#paneffect)

    - [panEffect: Phaser.Cameras.Scene2D.Effects.Pan](#paneffect-phasercamerasscene2deffectspan)
  + [postFX](#postfx)

    - [postFX: Phaser.GameObjects.Components.FX](#postfx-phasergameobjectscomponentsfx)
  + [postPipelineData](#postpipelinedata)

    - [postPipelineData: object](#postpipelinedata-object)
  + [postPipelines](#postpipelines)

    - [postPipelines: Array.<Phaser.Renderer.WebGL.Pipelines.PostFXPipeline>](#postpipelines-arrayphaserrendererwebglpipelinespostfxpipeline)
  + [preFX](#prefx)

    - [preFX: Phaser.GameObjects.Components.FX](#prefx-phasergameobjectscomponentsfx)
  + [renderList](#renderlist)

    - [renderList: Array.<Phaser.GameObjects.GameObject>](#renderlist-arrayphasergameobjectsgameobject)
  + [renderRoundPixels](#renderroundpixels)

    - [renderRoundPixels: boolean](#renderroundpixels-boolean)
  + [rotateToEffect](#rotatetoeffect)

    - [rotateToEffect: Phaser.Cameras.Scene2D.Effects.RotateTo](#rotatetoeffect-phasercamerasscene2deffectsrotateto)
  + [roundPixels](#roundpixels)

    - [roundPixels: boolean](#roundpixels-boolean)
  + [scaleManager](#scalemanager)

    - [scaleManager: Phaser.Scale.ScaleManager](#scalemanager-phaserscalescalemanager)
  + [scene](#scene)

    - [scene: Phaser.Scene](#scene-phaserscene)
  + [sceneManager](#scenemanager)

    - [sceneManager: Phaser.Scenes.SceneManager](#scenemanager-phaserscenesscenemanager)
  + [scrollX](#scrollx)

    - [scrollX: number](#scrollx-number)
  + [scrollY](#scrolly)

    - [scrollY: number](#scrolly-number)
  + [shakeEffect](#shakeeffect)

    - [shakeEffect: Phaser.Cameras.Scene2D.Effects.Shake](#shakeeffect-phasercamerasscene2deffectsshake)
  + [transparent](#transparent)

    - [transparent: boolean](#transparent-boolean)
  + [useBounds](#usebounds)

    - [useBounds: boolean](#usebounds-boolean)
  + [visible](#visible)

    - [visible: boolean](#visible-boolean)
  + [width](#width)

    - [width: number](#width-number)
  + [worldView](#worldview)

    - [worldView: Phaser.Geom.Rectangle](#worldview-phasergeomrectangle)
  + [x](#x)

    - [x: number](#x-number)
  + [y](#y)

    - [y: number](#y-number)
  + [zoom](#zoom)

    - [zoom: number](#zoom-number)
  + [zoomEffect](#zoomeffect)

    - [zoomEffect: Phaser.Cameras.Scene2D.Effects.Zoom](#zoomeffect-phasercamerasscene2deffectszoom)
  + [zoomX](#zoomx)

    - [zoomX: number](#zoomx-number)
  + [zoomY](#zoomy)

    - [zoomY: number](#zoomy-number)
* [Private Members](#private-members)

  + [\_alpha](#_alpha)

    - [\_alpha: number](#_alpha-number)
  + [\_alphaBL](#_alphabl)

    - [\_alphaBL: number](#_alphabl-number)
  + [\_alphaBR](#_alphabr)

    - [\_alphaBR: number](#_alphabr-number)
  + [\_alphaTL](#_alphatl)

    - [\_alphaTL: number](#_alphatl-number)
  + [\_alphaTR](#_alphatr)

    - [\_alphaTR: number](#_alphatr-number)
  + [\_bounds](#_bounds)

    - [\_bounds: Phaser.Geom.Rectangle](#_bounds-phasergeomrectangle)
  + [\_customViewport](#_customviewport)

    - [\_customViewport: boolean](#_customviewport-boolean)
  + [\_follow](#_follow)

    - [\_follow: any](#_follow-any)
  + [\_height](#_height)

    - [\_height: number](#_height-number)
  + [\_maskCamera](#_maskcamera)

    - [\_maskCamera: Phaser.Cameras.Scene2D.BaseCamera](#_maskcamera-phasercamerasscene2dbasecamera)
  + [\_rotation](#_rotation)

    - [\_rotation: number](#_rotation-number)
  + [\_scrollX](#_scrollx)

    - [\_scrollX: number](#_scrollx-number)
  + [\_scrollY](#_scrolly)

    - [\_scrollY: number](#_scrolly-number)
  + [\_visible](#_visible)

    - [\_visible: boolean](#_visible-boolean)
  + [\_width](#_width)

    - [\_width: number](#_width-number)
  + [\_x](#_x)

    - [\_x: number](#_x-number)
  + [\_y](#_y)

    - [\_y: number](#_y-number)
  + [\_zoomX](#_zoomx)

    - [\_zoomX: number](#_zoomx-number)
  + [\_zoomY](#_zoomy)

    - [\_zoomY: number](#_zoomy-number)
  + [culledObjects](#culledobjects)

    - [culledObjects: Array.<Phaser.GameObjects.GameObject>](#culledobjects-arrayphasergameobjectsgameobject)
  + [matrix](#matrix)

    - [matrix: Phaser.GameObjects.Components.TransformMatrix](#matrix-phasergameobjectscomponentstransformmatrix)
  + [rotation](#rotation)

    - [rotation: number](#rotation-number)
* [Public Methods](#public-methods)

  + [addListener](#addlistener)

    - [<instance> addListener(event, fn, [context])](#instance-addlistenerevent-fn-context)
  + [addToRenderList](#addtorenderlist)

    - [<instance> addToRenderList(child)](#instance-addtorenderlistchild)
  + [centerOn](#centeron)

    - [<instance> centerOn(x, y)](#instance-centeronx-y)
  + [centerOnX](#centeronx)

    - [<instance> centerOnX(x)](#instance-centeronxx)
  + [centerOnY](#centerony)

    - [<instance> centerOnY(y)](#instance-centeronyy)
  + [centerToBounds](#centertobounds)

    - [<instance> centerToBounds()](#instance-centertobounds)
  + [centerToSize](#centertosize)

    - [<instance> centerToSize()](#instance-centertosize)
  + [clampX](#clampx)

    - [<instance> clampX(x)](#instance-clampxx)
  + [clampY](#clampy)

    - [<instance> clampY(y)](#instance-clampyy)
  + [clearAlpha](#clearalpha)

    - [<instance> clearAlpha()](#instance-clearalpha)
  + [clearFX](#clearfx)

    - [<instance> clearFX()](#instance-clearfx)
  + [clearMask](#clearmask)

    - [<instance> clearMask([destroyMask])](#instance-clearmaskdestroymask)
  + [cull](#cull)

    - [<instance> cull(renderableObjects)](#instance-cullrenderableobjects)
  + [destroy](#destroy)

    - [<instance> destroy()](#instance-destroy)
  + [emit](#emit)

    - [<instance> emit(event, [args])](#instance-emitevent-args)
  + [eventNames](#eventnames)

    - [<instance> eventNames()](#instance-eventnames)
  + [fade](#fade)

    - [<instance> fade([duration], [red], [green], [blue], [force], [callback], [context])](#instance-fadeduration-red-green-blue-force-callback-context)
  + [fadeFrom](#fadefrom)

    - [<instance> fadeFrom([duration], [red], [green], [blue], [force], [callback], [context])](#instance-fadefromduration-red-green-blue-force-callback-context)
  + [fadeIn](#fadein)

    - [<instance> fadeIn([duration], [red], [green], [blue], [callback], [context])](#instance-fadeinduration-red-green-blue-callback-context)
  + [fadeOut](#fadeout)

    - [<instance> fadeOut([duration], [red], [green], [blue], [callback], [context])](#instance-fadeoutduration-red-green-blue-callback-context)
  + [flash](#flash)

    - [<instance> flash([duration], [red], [green], [blue], [force], [callback], [context])](#instance-flashduration-red-green-blue-force-callback-context)
  + [getBounds](#getbounds)

    - [<instance> getBounds([out])](#instance-getboundsout)
  + [getPostPipeline](#getpostpipeline)

    - [<instance> getPostPipeline(pipeline)](#instance-getpostpipelinepipeline)
  + [getScroll](#getscroll)

    - [<instance> getScroll(x, y, [out])](#instance-getscrollx-y-out)
  + [getWorldPoint](#getworldpoint)

    - [<instance> getWorldPoint(x, y, [output])](#instance-getworldpointx-y-output)
  + [ignore](#ignore)

    - [<instance> ignore(entries)](#instance-ignoreentries)
  + [initPostPipeline](#initpostpipeline)

    - [<instance> initPostPipeline([preFX])](#instance-initpostpipelineprefx)
  + [listenerCount](#listenercount)

    - [<instance> listenerCount(event)](#instance-listenercountevent)
  + [listeners](#listeners)

    - [<instance> listeners(event)](#instance-listenersevent)
  + [off](#off)

    - [<instance> off(event, [fn], [context], [once])](#instance-offevent-fn-context-once)
  + [on](#on)

    - [<instance> on(event, fn, [context])](#instance-onevent-fn-context)
  + [once](#once)

    - [<instance> once(event, fn, [context])](#instance-onceevent-fn-context)
  + [pan](#pan)

    - [<instance> pan(x, y, [duration], [ease], [force], [callback], [context])](#instance-panx-y-duration-ease-force-callback-context)
  + [preRender](#prerender)

    - [<instance> preRender()](#instance-prerender)
  + [removeAllListeners](#removealllisteners)

    - [<instance> removeAllListeners([event])](#instance-removealllistenersevent)
  + [removeBounds](#removebounds)

    - [<instance> removeBounds()](#instance-removebounds)
  + [removeListener](#removelistener)

    - [<instance> removeListener(event, [fn], [context], [once])](#instance-removelistenerevent-fn-context-once)
  + [removePostPipeline](#removepostpipeline)

    - [<instance> removePostPipeline(pipeline)](#instance-removepostpipelinepipeline)
  + [resetFX](#resetfx)

    - [<instance> resetFX()](#instance-resetfx)
  + [resetPostPipeline](#resetpostpipeline)

    - [<instance> resetPostPipeline([resetData])](#instance-resetpostpipelineresetdata)
  + [rotateTo](#rotateto)

    - [<instance> rotateTo(radians, [shortestPath], [duration], [ease], [force], [callback], [context])](#instance-rotatetoradians-shortestpath-duration-ease-force-callback-context)
  + [setAlpha](#setalpha)

    - [<instance> setAlpha([value])](#instance-setalphavalue)
  + [setAngle](#setangle)

    - [<instance> setAngle([value])](#instance-setanglevalue)
  + [setBackgroundColor](#setbackgroundcolor)

    - [<instance> setBackgroundColor([color])](#instance-setbackgroundcolorcolor)
  + [setBounds](#setbounds)

    - [<instance> setBounds(x, y, width, height, [centerOn])](#instance-setboundsx-y-width-height-centeron)
  + [setDeadzone](#setdeadzone)

    - [<instance> setDeadzone([width], [height])](#instance-setdeadzonewidth-height)
  + [setFollowOffset](#setfollowoffset)

    - [<instance> setFollowOffset([x], [y])](#instance-setfollowoffsetx-y)
  + [setIsSceneCamera](#setisscenecamera)

    - [<instance> setIsSceneCamera(value)](#instance-setisscenecameravalue)
  + [setLerp](#setlerp)

    - [<instance> setLerp([x], [y])](#instance-setlerpx-y)
  + [setMask](#setmask)

    - [<instance> setMask(mask, [fixedPosition])](#instance-setmaskmask-fixedposition)
  + [setName](#setname)

    - [<instance> setName([value])](#instance-setnamevalue)
  + [setOrigin](#setorigin)

    - [<instance> setOrigin([x], [y])](#instance-setoriginx-y)
  + [setPosition](#setposition)

    - [<instance> setPosition(x, [y])](#instance-setpositionx-y)
  + [setPostPipeline](#setpostpipeline)

    - [<instance> setPostPipeline(pipelines, [pipelineData], [copyData])](#instance-setpostpipelinepipelines-pipelinedata-copydata)
  + [setPostPipelineData](#setpostpipelinedata)

    - [<instance> setPostPipelineData(key, [value])](#instance-setpostpipelinedatakey-value)
  + [setRotation](#setrotation)

    - [<instance> setRotation([value])](#instance-setrotationvalue)
  + [setRoundPixels](#setroundpixels)

    - [<instance> setRoundPixels(value)](#instance-setroundpixelsvalue)
  + [setScene](#setscene)

    - [<instance> setScene(scene, [isSceneCamera])](#instance-setscenescene-isscenecamera)
  + [setScroll](#setscroll)

    - [<instance> setScroll(x, [y])](#instance-setscrollx-y)
  + [setSize](#setsize)

    - [<instance> setSize(width, [height])](#instance-setsizewidth-height)
  + [setViewport](#setviewport)

    - [<instance> setViewport(x, y, width, [height])](#instance-setviewportx-y-width-height)
  + [setVisible](#setvisible)

    - [<instance> setVisible(value)](#instance-setvisiblevalue)
  + [setZoom](#setzoom)

    - [<instance> setZoom([x], [y])](#instance-setzoomx-y)
  + [shake](#shake)

    - [<instance> shake([duration], [intensity], [force], [callback], [context])](#instance-shakeduration-intensity-force-callback-context)
  + [shutdown](#shutdown)

    - [<instance> shutdown()](#instance-shutdown)
  + [startFollow](#startfollow)

    - [<instance> startFollow(target, [roundPixels], [lerpX], [lerpY], [offsetX], [offsetY])](#instance-startfollowtarget-roundpixels-lerpx-lerpy-offsetx-offsety)
  + [stopFollow](#stopfollow)

    - [<instance> stopFollow()](#instance-stopfollow)
  + [toJSON](#tojson)

    - [<instance> toJSON()](#instance-tojson)
  + [update](#update)

    - [<instance> update(time, delta)](#instance-updatetime-delta)
  + [zoomTo](#zoomto)

    - [<instance> zoomTo(zoom, [duration], [ease], [force], [callback], [context])](#instance-zoomtozoom-duration-ease-force-callback-context)
* [Private Methods](#private-methods)

  + [updateSystem](#updatesystem)

    - [<instance> updateSystem()](#instance-updatesystem)

Back to top

©2025[Phaser](https://docs.phaser.io)