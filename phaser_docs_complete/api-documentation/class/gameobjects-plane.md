# Plane

Phaser.GameObjects.Plane

A Plane Game Object.

The Plane Game Object is a helper class that takes the Mesh Game Object and extends it,

allowing for fast and easy creation of Planes. A Plane is a one-sided grid of cells,

where you specify the number of cells in each dimension. The Plane can have a texture

that is either repeated (tiled) across each cell, or applied to the full Plane.

The Plane can then be manipulated in 3D space, with rotation across all 3 axis.

This allows you to create effects not possible with regular Sprites, such as perspective

distortion. You can also adjust the vertices on a per-vertex basis. Plane data becomes

part of the WebGL batch, just like standard Sprites, so doesn't introduce any additional

shader overhead. Because the Plane just generates vertices into the WebGL batch, like any

other Sprite, you can use all of the common Game Object components on a Plane too,

such as a custom pipeline, mask, blend mode or texture.

You can use the `uvScroll` and `uvScale` methods to adjust the placement and scaling

of the texture if this Plane is using a single texture, and not a frame from a texture

atlas or sprite sheet.

The Plane Game Object also has the Animation component, allowing you to play animations

across the Plane just as you would with a Sprite. The animation frame size must be fixed

as the first frame will be the size of the entire animation, for example use a `SpriteSheet`.

Note that the Plane object is WebGL only and does not have a Canvas counterpart.

The Plane origin is always 0.5 x 0.5 and cannot be changed.

**Constructor**

`new Plane(scene, [x], [y], [texture], [frame], [width], [height], [tile])`

**Parameters**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| scene | [Phaser.Scene](scene.md) | No |  | The Scene to which this Plane belongs. A Plane can only belong to one Scene at a time. |
| --- | --- | --- | --- | --- |
| x | number | Yes |  | The horizontal position of this Plane in the world. |
| y | number | Yes |  | The vertical position of this Plane in the world. |
| texture | string | [Phaser.Textures.Texture](textures-texture.md) | Yes |  | The key, or instance of the Texture this Plane will use to render with, as stored in the Texture Manager. |
| frame | string | number | Yes |  | An optional frame from the Texture this Plane is rendering with. |
| width | number | Yes | 8 | The width of this Plane, in cells, not pixels. |
| height | number | Yes | 8 | The height of this Plane, in cells, not pixels. |
| tile | boolean | Yes | false | Is the texture tiled? I.e. repeated across each cell. |

---

**Scope**: static

**Extends**

> [Phaser.GameObjects.Mesh](gameobjects-mesh.md)

> Source: [src/gameobjects/plane/Plane.js#L14](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/plane/Plane.js#L14)  
> Since: 3.60.0

# Public Members

## active

### active: boolean

**Description:**

The active state of this Game Object.

A Game Object with an active state of `true` is processed by the Scenes UpdateList, if added to it.

An active object is one which is having its logic and internal systems updated.

**Inherits:** [Phaser.GameObjects.GameObject#active](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L113](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L113)  
> Since: 3.0.0

---

## alpha

### alpha: number

**Description:**

The alpha value of the Game Object.

This is a global value, impacting the entire Game Object, not just a region of it.

**Inherits:** [Phaser.GameObjects.Components.AlphaSingle#alpha](../namespace/gameobjects-components-alphasingle.md)

> Source: [src/gameobjects/components/AlphaSingle.js#L68](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/AlphaSingle.js#L68)  
> Since: 3.0.0

---

## angle

### angle: number

**Description:**

The angle of this Game Object as expressed in degrees.

Phaser uses a right-hand clockwise rotation system, where 0 is right, 90 is down, 180/-180 is left

and -90 is up.

If you prefer to work in radians, see the `rotation` property instead.

**Inherits:** [Phaser.GameObjects.Components.Transform#angle](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L211](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L211)  
> Since: 3.0.0

---

## anims

### anims: [Phaser.Animations.AnimationState](animations-animationstate.md)

**Description:**

The Animation State component of this Sprite.

This component provides features to apply animations to this Sprite.

It is responsible for playing, loading, queuing animations for later playback,

mixing between animations and setting the current animation frame to this Sprite.

> Source: [src/gameobjects/plane/Plane.js#L73](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/plane/Plane.js#L73)  
> Since: 3.60.0

---

## blendMode

### blendMode: [Phaser.BlendModes](../namespace/blendmodes.md), string, number

**Description:**

Sets the Blend Mode being used by this Game Object.

This can be a const, such as `Phaser.BlendModes.SCREEN`, or an integer, such as 4 (for Overlay)

Under WebGL only the following Blend Modes are available:

* NORMAL
* ADD
* MULTIPLY
* SCREEN
* ERASE

Canvas has more available depending on browser support.

You can also create your own custom Blend Modes in WebGL.

Blend modes have different effects under Canvas and WebGL, and from browser to browser, depending

on support. Blend Modes also cause a WebGL batch flush should it encounter a new blend mode. For these

reasons try to be careful about the construction of your Scene and the frequency of which blend modes

are used.

**Inherits:** [Phaser.GameObjects.Components.BlendMode#blendMode](../namespace/gameobjects-components-blendmode.md)

> Source: [src/gameobjects/components/BlendMode.js#L30](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/BlendMode.js#L30)  
> Since: 3.0.0

---

## body

### body: [Phaser.Physics.Arcade.Body](physics-arcade-body.md), [Phaser.Physics.Arcade.StaticBody](physics-arcade-staticbody.md), MatterJS.BodyType

**Description:**

If this Game Object is enabled for Arcade or Matter Physics then this property will contain a reference to a Physics Body.

**Inherits:** [Phaser.GameObjects.GameObject#body](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L186](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L186)  
> Since: 3.0.0

---

## cameraFilter

### cameraFilter: number

**Description:**

A bitmask that controls if this Game Object is drawn by a Camera or not.

Not usually set directly, instead call `Camera.ignore`, however you can

set this property directly using the Camera.id property:

**Inherits:** [Phaser.GameObjects.GameObject#cameraFilter](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L160](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L160)  
> Since: 3.0.0

---

## data

### data: [Phaser.Data.DataManager](data-datamanager.md)

**Description:**

A Data Manager.

It allows you to store, query and get key/value paired information specific to this Game Object.

`null` by default. Automatically created if you use `getData` or `setData` or `setDataEnabled`.

**Inherits:** [Phaser.GameObjects.GameObject#data](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L136](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L136)  
> Since: 3.0.0

---

## debugCallback

### debugCallback: function

**Description:**

You can optionally choose to render the vertices of this Mesh to a Graphics instance.

Achieve this by setting the `debugCallback` and the `debugGraphic` properties.

You can do this in a single call via the `Mesh.setDebug` method, which will use the

built-in debug function. You can also set it to your own callback. The callback

will be invoked *once per render* and sent the following parameters:

`debugCallback(src, meshLength, verts)`

`src` is the Mesh instance being debugged.

`meshLength` is the number of mesh vertices in total.

`verts` is an array of the translated vertex coordinates.

To disable rendering, set this property back to `null`.

Please note that high vertex count Meshes will struggle to debug properly.

**Inherits:** [Phaser.GameObjects.Mesh#debugCallback](gameobjects-mesh.md)

> Source: [src/gameobjects/mesh/Mesh.js#L154](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/mesh/Mesh.js#L154)  
> Since: 3.50.0

---

## debugGraphic

### debugGraphic: [Phaser.GameObjects.Graphics](gameobjects-graphics.md)

**Description:**

The Graphics instance that the debug vertices will be drawn to, if `setDebug` has

been called.

**Inherits:** [Phaser.GameObjects.Mesh#debugGraphic](gameobjects-mesh.md)

> Source: [src/gameobjects/mesh/Mesh.js#L179](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/mesh/Mesh.js#L179)  
> Since: 3.50.0

---

## defaultPipeline

### defaultPipeline: [Phaser.Renderer.WebGL.WebGLPipeline](renderer-webgl-webglpipeline.md)

**Description:**

The initial WebGL pipeline of this Game Object.

If you call `resetPipeline` on this Game Object, the pipeline is reset to this default.

**Tags:**

* webglOnly

**Inherits:** [Phaser.GameObjects.Components.Pipeline#defaultPipeline](../namespace/gameobjects-components-pipeline.md)

> Source: [src/gameobjects/components/Pipeline.js#L19](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Pipeline.js#L19)  
> Since: 3.0.0

---

## depth

### depth: number

**Description:**

The depth of this Game Object within the Scene. Ensure this value is only ever set to a number data-type.

The depth is also known as the 'z-index' in some environments, and allows you to change the rendering order

of Game Objects, without actually moving their position in the display list.

The default depth is zero. A Game Object with a higher depth

value will always render in front of one with a lower value.

Setting the depth will queue a depth sort event within the Scene.

**Inherits:** [Phaser.GameObjects.Components.Depth#depth](../namespace/gameobjects-components-depth.md)

> Source: [src/gameobjects/components/Depth.js#L30](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Depth.js#L30)  
> Since: 3.0.0

---

## displayHeight

### displayHeight: number

**Description:**

The displayed height of this Game Object.

This value takes into account the scale factor.

Setting this value will adjust the Game Object's scale property.

**Inherits:** [Phaser.GameObjects.Components.Size#displayHeight](../namespace/gameobjects-components-size.md)

> Source: [src/gameobjects/components/Size.js#L78](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Size.js#L78)  
> Since: 3.0.0

---

## displayList

### displayList: [Phaser.GameObjects.DisplayList](gameobjects-displaylist.md), [Phaser.GameObjects.Layer](gameobjects-layer.md)

**Description:**

Holds a reference to the Display List that contains this Game Object.

This is set automatically when this Game Object is added to a Scene or Layer.

You should treat this property as being read-only.

**Inherits:** [Phaser.GameObjects.GameObject#displayList](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L53](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L53)  
> Since: 3.50.0

---

## displayWidth

### displayWidth: number

**Description:**

The displayed width of this Game Object.

This value takes into account the scale factor.

Setting this value will adjust the Game Object's scale property.

**Inherits:** [Phaser.GameObjects.Components.Size#displayWidth](../namespace/gameobjects-components-size.md)

> Source: [src/gameobjects/components/Size.js#L53](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Size.js#L53)  
> Since: 3.0.0

---

## faces

### faces: Array.<[Phaser.Geom.Mesh.Face](geom-mesh-face.md)>

**Description:**

An array containing the Face instances belonging to this Mesh.

A Face consists of 3 Vertex objects.

This array is populated during calls such as `addVertices` or `addOBJ`.

**Inherits:** [Phaser.GameObjects.Mesh#faces](gameobjects-mesh.md)

> Source: [src/gameobjects/mesh/Mesh.js#L117](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/mesh/Mesh.js#L117)  
> Since: 3.50.0

---

## fov

### fov: number

**Description:**

The Camera fov (field of view) in degrees.

This is set automatically as part of the `Mesh.setPerspective` call, but exposed

here for additional math.

Do not modify this property directly, doing so will not change the fov. For that,

call the respective Mesh methods.

**Inherits:** [Phaser.GameObjects.Mesh#fov](gameobjects-mesh.md)

> Source: [src/gameobjects/mesh/Mesh.js#L351](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/mesh/Mesh.js#L351)  
> Since: 3.60.0

---

## frame

### frame: [Phaser.Textures.Frame](textures-frame.md)

**Description:**

The Texture Frame this Game Object is using to render with.

**Inherits:** [Phaser.GameObjects.Components.Texture#frame](../namespace/gameobjects-components-texture.md)

> Source: [src/gameobjects/components/Texture.js#L30](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Texture.js#L30)  
> Since: 3.0.0

---

## gridHeight

### gridHeight: number

**Description:**

The height of this Plane in cells, not pixels.

This value is read-only. To adjust it, see the `setGridSize` method.

> Source: [src/gameobjects/plane/Plane.js#L98](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/plane/Plane.js#L98)  
> Since: 3.60.0

---

## gridWidth

### gridWidth: number

**Description:**

The width of this Plane in cells, not pixels.

This value is read-only. To adjust it, see the `setGridSize` method.

> Source: [src/gameobjects/plane/Plane.js#L86](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/plane/Plane.js#L86)  
> Since: 3.60.0

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

## hasTransformComponent

### hasTransformComponent: boolean

**Description:**

A property indicating that a Game Object has this component.

**Inherits:** [Phaser.GameObjects.Components.Transform#hasTransformComponent](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L26](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L26)  
> Since: 3.60.0

---

## height

### height: number

**Description:**

The native (un-scaled) height of this Game Object.

Changing this value will not change the size that the Game Object is rendered in-game.

For that you need to either set the scale of the Game Object (`setScale`) or use

the `displayHeight` property.

**Inherits:** [Phaser.GameObjects.Components.Size#height](../namespace/gameobjects-components-size.md)

> Source: [src/gameobjects/components/Size.js#L40](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Size.js#L40)  
> Since: 3.0.0

---

## hideCCW

### hideCCW: boolean

**Description:**

When rendering, skip any Face that isn't counter clockwise?

Enable this to hide backward-facing Faces during rendering.

Disable it to render all Faces.

**Inherits:** [Phaser.GameObjects.Mesh#hideCCW](gameobjects-mesh.md)

> Source: [src/gameobjects/mesh/Mesh.js#L189](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/mesh/Mesh.js#L189)  
> Since: 3.50.0

---

## ignoreDestroy

### ignoreDestroy: boolean

**Description:**

This Game Object will ignore all calls made to its destroy method if this flag is set to `true`.

This includes calls that may come from a Group, Container or the Scene itself.

While it allows you to persist a Game Object across Scenes, please understand you are entirely

responsible for managing references to and from this Game Object.

**Inherits:** [Phaser.GameObjects.GameObject#ignoreDestroy](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L196](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L196)  
> Since: 3.5.0

---

## ignoreDirtyCache

### ignoreDirtyCache: boolean

**Description:**

By default, the Mesh will check to see if its model or view transform has

changed each frame and only recalculate the vertex positions if they have.

This avoids lots of additional math in the `preUpdate` step when not required.

However, if you are performing per-Face or per-Vertex manipulation on this Mesh,

such as tweening a Face, or moving it without moving the rest of the Mesh,

then you may need to disable the dirty cache in order for the Mesh to re-render

correctly. You can toggle this property to do that. Please note that leaving

this set to `true` will cause the Mesh to recalculate the position of every single

vertex in it, every single frame. So only really do this if you know you

need it.

**Inherits:** [Phaser.GameObjects.Mesh#ignoreDirtyCache](gameobjects-mesh.md)

> Source: [src/gameobjects/mesh/Mesh.js#L331](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/mesh/Mesh.js#L331)  
> Since: 3.50.0

---

## input

### input: [Phaser.Types.Input.InteractiveObject](../typedef/types-input.md)

**Description:**

If this Game Object is enabled for input then this property will contain an InteractiveObject instance.

Not usually set directly. Instead call `GameObject.setInteractive()`.

**Inherits:** [Phaser.GameObjects.GameObject#input](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L175](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L175)  
> Since: 3.0.0

---

## isTiled

### isTiled: boolean

**Description:**

Is the texture of this Plane tiled across all cells, or not?

This value is read-only. To adjust it, see the `setGridSize` method.

> Source: [src/gameobjects/plane/Plane.js#L110](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/plane/Plane.js#L110)  
> Since: 3.60.0

---

## mask

### mask: [Phaser.Display.Masks.BitmapMask](display-masks-bitmapmask.md), [Phaser.Display.Masks.GeometryMask](display-masks-geometrymask.md)

**Description:**

The Mask this Game Object is using during render.

**Inherits:** [Phaser.GameObjects.Components.Mask#mask](../namespace/gameobjects-components-mask.md)

> Source: [src/gameobjects/components/Mask.js#L19](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Mask.js#L19)  
> Since: 3.0.0

---

## modelPosition

### modelPosition: [Phaser.Math.Vector3](math-vector3.md)

**Description:**

A Vector3 containing the 3D position of the vertices in this Mesh.

Modifying the components of this property will allow you to reposition where

the vertices are rendered within the Mesh. This happens in the `preUpdate` phase,

where each vertex is transformed using the view and projection matrices.

Changing this property will impact all vertices being rendered by this Mesh.

You can also adjust the 'view' by using the `pan` methods.

**Inherits:** [Phaser.GameObjects.Mesh#modelPosition](gameobjects-mesh.md)

> Source: [src/gameobjects/mesh/Mesh.js#L202](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/mesh/Mesh.js#L202)  
> Since: 3.50.0

---

## modelRotation

### modelRotation: [Phaser.Math.Vector3](math-vector3.md)

**Description:**

A Vector3 containing the 3D rotation of the vertices in this Mesh.

The values should be given in radians, i.e. to rotate the vertices by 90

degrees you can use `modelRotation.x = Phaser.Math.DegToRad(90)`.

Modifying the components of this property will allow you to rotate

the vertices within the Mesh. This happens in the `preUpdate` phase,

where each vertex is transformed using the view and projection matrices.

Changing this property will impact all vertices being rendered by this Mesh.

**Inherits:** [Phaser.GameObjects.Mesh#modelRotation](gameobjects-mesh.md)

> Source: [src/gameobjects/mesh/Mesh.js#L234](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/mesh/Mesh.js#L234)  
> Since: 3.50.0

---

## modelScale

### modelScale: [Phaser.Math.Vector3](math-vector3.md)

**Description:**

A Vector3 containing the 3D scale of the vertices in this Mesh.

Modifying the components of this property will allow you to scale

the vertices within the Mesh. This happens in the `preUpdate` phase,

where each vertex is transformed using the view and projection matrices.

Changing this property will impact all vertices being rendered by this Mesh.

**Inherits:** [Phaser.GameObjects.Mesh#modelScale](gameobjects-mesh.md)

> Source: [src/gameobjects/mesh/Mesh.js#L219](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/mesh/Mesh.js#L219)  
> Since: 3.50.0

---

## name

### name: string

**Description:**

The name of this Game Object.

Empty by default and never populated by Phaser, this is left for developers to use.

**Inherits:** [Phaser.GameObjects.GameObject#name](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L102](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L102)  
> Since: 3.0.0

---

## originX

### originX: number

**Description:**

Do not change this value. It has no effect other than to break things.

> Source: [src/gameobjects/plane/Plane.js#L140](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/plane/Plane.js#L140)  
> Since: 3.70.0

---

## originY

### originY: number

**Description:**

Do not change this value. It has no effect other than to break things.

> Source: [src/gameobjects/plane/Plane.js#L158](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/plane/Plane.js#L158)  
> Since: 3.70.0

---

## parentContainer

### parentContainer: [Phaser.GameObjects.Container](gameobjects-container.md)

**Description:**

The parent Container of this Game Object, if it has one.

**Inherits:** [Phaser.GameObjects.GameObject#parentContainer](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L93](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L93)  
> Since: 3.4.0

---

## pipeline

### pipeline: [Phaser.Renderer.WebGL.WebGLPipeline](renderer-webgl-webglpipeline.md)

**Description:**

The current WebGL pipeline of this Game Object.

**Tags:**

* webglOnly

**Inherits:** [Phaser.GameObjects.Components.Pipeline#pipeline](../namespace/gameobjects-components-pipeline.md)

> Source: [src/gameobjects/components/Pipeline.js#L32](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Pipeline.js#L32)  
> Since: 3.0.0

---

## pipelineData

### pipelineData: object

**Description:**

An object to store pipeline specific data in, to be read by the pipelines this Game Object uses.

**Tags:**

* webglOnly

**Inherits:** [Phaser.GameObjects.Components.Pipeline#pipelineData](../namespace/gameobjects-components-pipeline.md)

> Source: [src/gameobjects/components/Pipeline.js#L43](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Pipeline.js#L43)  
> Since: 3.50.0

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

## projectionMatrix

### projectionMatrix: [Phaser.Math.Matrix4](math-matrix4.md)

**Description:**

The projection matrix for this Mesh.

Update it with the `setPerspective` or `setOrtho` methods.

**Inherits:** [Phaser.GameObjects.Mesh#projectionMatrix](gameobjects-mesh.md)

> Source: [src/gameobjects/mesh/Mesh.js#L294](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/mesh/Mesh.js#L294)  
> Since: 3.50.0

---

## renderFlags

### renderFlags: number

**Description:**

The flags that are compared against `RENDER_MASK` to determine if this Game Object will render or not.

The bits are 0001 | 0010 | 0100 | 1000 set by the components Visible, Alpha, Transform and Texture respectively.

If those components are not used by your custom class then you can use this bitmask as you wish.

**Inherits:** [Phaser.GameObjects.GameObject#renderFlags](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L148](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L148)  
> Since: 3.0.0

---

## rotation

### rotation: number

**Description:**

The angle of this Game Object in radians.

Phaser uses a right-hand clockwise rotation system, where 0 is right, PI/2 is down, +-PI is left

and -PI/2 is up.

If you prefer to work in degrees, see the `angle` property instead.

**Inherits:** [Phaser.GameObjects.Components.Transform#rotation](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L238](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L238)  
> Since: 3.0.0

---

## scale

### scale: number

**Description:**

This is a special setter that allows you to set both the horizontal and vertical scale of this Game Object

to the same value, at the same time. When reading this value the result returned is `(scaleX + scaleY) / 2`.

Use of this property implies you wish the horizontal and vertical scales to be equal to each other. If this

isn't the case, use the `scaleX` or `scaleY` properties instead.

**Inherits:** [Phaser.GameObjects.Components.Transform#scale](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L113](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L113)  
> Since: 3.18.0

---

## scaleX

### scaleX: number

**Description:**

The horizontal scale of this Game Object.

**Inherits:** [Phaser.GameObjects.Components.Transform#scaleX](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L149](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L149)  
> Since: 3.0.0

---

## scaleY

### scaleY: number

**Description:**

The vertical scale of this Game Object.

**Inherits:** [Phaser.GameObjects.Components.Transform#scaleY](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L180](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L180)  
> Since: 3.0.0

---

## scene

### scene: [Phaser.Scene](scene.md)

**Description:**

A reference to the Scene to which this Game Object belongs.

Game Objects can only belong to one Scene.

You should consider this property as being read-only. You cannot move a

Game Object to another Scene by simply changing it.

**Inherits:** [Phaser.GameObjects.GameObject#scene](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L39](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L39)  
> Since: 3.0.0

---

## scrollFactorX

### scrollFactorX: number

**Description:**

The horizontal scroll factor of this Game Object.

The scroll factor controls the influence of the movement of a Camera upon this Game Object.

When a camera scrolls it will change the location at which this Game Object is rendered on-screen.

It does not change the Game Objects actual position values.

A value of 1 means it will move exactly in sync with a camera.

A value of 0 means it will not move at all, even if the camera moves.

Other values control the degree to which the camera movement is mapped to this Game Object.

Please be aware that scroll factor values other than 1 are not taken in to consideration when

calculating physics collisions. Bodies always collide based on their world position, but changing

the scroll factor is a visual adjustment to where the textures are rendered, which can offset

them from physics bodies if not accounted for in your code.

**Inherits:** [Phaser.GameObjects.Components.ScrollFactor#scrollFactorX](../namespace/gameobjects-components-scrollfactor.md)

> Source: [src/gameobjects/components/ScrollFactor.js#L16](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/ScrollFactor.js#L16)  
> Since: 3.0.0

---

## scrollFactorY

### scrollFactorY: number

**Description:**

The vertical scroll factor of this Game Object.

The scroll factor controls the influence of the movement of a Camera upon this Game Object.

When a camera scrolls it will change the location at which this Game Object is rendered on-screen.

It does not change the Game Objects actual position values.

A value of 1 means it will move exactly in sync with a camera.

A value of 0 means it will not move at all, even if the camera moves.

Other values control the degree to which the camera movement is mapped to this Game Object.

Please be aware that scroll factor values other than 1 are not taken in to consideration when

calculating physics collisions. Bodies always collide based on their world position, but changing

the scroll factor is a visual adjustment to where the textures are rendered, which can offset

them from physics bodies if not accounted for in your code.

**Inherits:** [Phaser.GameObjects.Components.ScrollFactor#scrollFactorY](../namespace/gameobjects-components-scrollfactor.md)

> Source: [src/gameobjects/components/ScrollFactor.js#L40](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/ScrollFactor.js#L40)  
> Since: 3.0.0

---

## state

### state: number, string

**Description:**

The current state of this Game Object.

Phaser itself will never modify this value, although plugins may do so.

Use this property to track the state of a Game Object during its lifetime. For example, it could change from

a state of 'moving', to 'attacking', to 'dead'. The state value should be an integer (ideally mapped to a constant

in your game code), or a string. These are recommended to keep it light and simple, with fast comparisons.

If you need to store complex data about your Game Object, look at using the Data Component instead.

**Inherits:** [Phaser.GameObjects.GameObject#state](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L77](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L77)  
> Since: 3.16.0

---

## tabIndex

### tabIndex: number

**Description:**

The Tab Index of the Game Object.

Reserved for future use by plugins and the Input Manager.

**Inherits:** [Phaser.GameObjects.GameObject#tabIndex](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L125](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L125)  
> Since: 3.0.0

---

## texture

### texture: [Phaser.Textures.Texture](textures-texture.md), [Phaser.Textures.CanvasTexture](textures-canvastexture.md)

**Description:**

The Texture this Game Object is using to render with.

**Inherits:** [Phaser.GameObjects.Components.Texture#texture](../namespace/gameobjects-components-texture.md)

> Source: [src/gameobjects/components/Texture.js#L21](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Texture.js#L21)  
> Since: 3.0.0

---

## tintFill

### tintFill: boolean

**Description:**

The tint fill mode.

`false` = An additive tint (the default), where vertices colors are blended with the texture.

`true` = A fill tint, where the vertex colors replace the texture, but respects texture alpha.

**Inherits:** [Phaser.GameObjects.Mesh#tintFill](gameobjects-mesh.md)

> Source: [src/gameobjects/mesh/Mesh.js#L141](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/mesh/Mesh.js#L141)  
> Since: 3.50.0

---

## totalRendered

### totalRendered: number

**Description:**

How many faces were rendered by this Mesh Game Object in the last

draw? This is reset in the `preUpdate` method and then incremented

each time a face is drawn. Note that in multi-camera Scenes this

value may exceed that found in `Mesh.getFaceCount` due to

cameras drawing the same faces more than once.

**Inherits:** [Phaser.GameObjects.Mesh#totalRendered](gameobjects-mesh.md)

> Source: [src/gameobjects/mesh/Mesh.js#L305](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/mesh/Mesh.js#L305)  
> Since: 3.50.0

---

## transformMatrix

### transformMatrix: [Phaser.Math.Matrix4](math-matrix4.md)

**Description:**

The transformation matrix for this Mesh.

**Inherits:** [Phaser.GameObjects.Mesh#transformMatrix](gameobjects-mesh.md)

> Source: [src/gameobjects/mesh/Mesh.js#L265](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/mesh/Mesh.js#L265)  
> Since: 3.50.0

---

## type

### type: string

**Description:**

A textual representation of this Game Object, i.e. `sprite`.

Used internally by Phaser but is available for your own custom classes to populate.

**Inherits:** [Phaser.GameObjects.GameObject#type](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L67](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L67)  
> Since: 3.0.0

---

## vertices

### vertices: Array.<[Phaser.Geom.Mesh.Vertex](geom-mesh-vertex.md)>

**Description:**

An array containing Vertex instances. One instance per vertex in this Mesh.

This array is populated during calls such as `addVertex` or `addOBJ`.

**Inherits:** [Phaser.GameObjects.Mesh#vertices](gameobjects-mesh.md)

> Source: [src/gameobjects/mesh/Mesh.js#L130](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/mesh/Mesh.js#L130)  
> Since: 3.50.0

---

## viewMatrix

### viewMatrix: [Phaser.Math.Matrix4](math-matrix4.md)

**Description:**

The view matrix for this Mesh.

**Inherits:** [Phaser.GameObjects.Mesh#viewMatrix](gameobjects-mesh.md)

> Source: [src/gameobjects/mesh/Mesh.js#L285](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/mesh/Mesh.js#L285)  
> Since: 3.50.0

---

## viewPosition

### viewPosition: [Phaser.Math.Vector3](math-vector3.md)

**Description:**

The view position for this Mesh.

Use the methods`panX`, `panY` and `panZ` to adjust the view.

**Inherits:** [Phaser.GameObjects.Mesh#viewPosition](gameobjects-mesh.md)

> Source: [src/gameobjects/mesh/Mesh.js#L274](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/mesh/Mesh.js#L274)  
> Since: 3.50.0

---

## visible

### visible: boolean

**Description:**

The visible state of the Game Object.

An invisible Game Object will skip rendering, but will still process update logic.

**Inherits:** [Phaser.GameObjects.Components.Visible#visible](../namespace/gameobjects-components-visible.md)

> Source: [src/gameobjects/components/Visible.js#L31](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Visible.js#L31)  
> Since: 3.0.0

---

## w

### w: number

**Description:**

The w position of this Game Object.

**Inherits:** [Phaser.GameObjects.Components.Transform#w](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L103](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L103)  
> Since: 3.0.0

---

## width

### width: number

**Description:**

The native (un-scaled) width of this Game Object.

Changing this value will not change the size that the Game Object is rendered in-game.

For that you need to either set the scale of the Game Object (`setScale`) or use

the `displayWidth` property.

**Inherits:** [Phaser.GameObjects.Components.Size#width](../namespace/gameobjects-components-size.md)

> Source: [src/gameobjects/components/Size.js#L27](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Size.js#L27)  
> Since: 3.0.0

---

## x

### x: number

**Description:**

The x position of this Game Object.

**Inherits:** [Phaser.GameObjects.Components.Transform#x](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L70](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L70)  
> Since: 3.0.0

---

## y

### y: number

**Description:**

The y position of this Game Object.

**Inherits:** [Phaser.GameObjects.Components.Transform#y](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L80](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L80)  
> Since: 3.0.0

---

## z

### z: number

**Description:**

The z position of this Game Object.

Note: The z position does not control the rendering order of 2D Game Objects. Use

[Phaser.GameObjects.Components.Depth#depth](../namespace/gameobjects-components-depth.md) instead.

**Inherits:** [Phaser.GameObjects.Components.Transform#z](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L90](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L90)  
> Since: 3.0.0

---

# Private Members

## \_alpha

### \_alpha: number

**Description:**

Private internal value. Holds the global alpha value.

**Access:** private

**Inherits:** [Phaser.GameObjects.Components.AlphaSingle#\_alpha](../namespace/gameobjects-components-alphasingle.md)

> Source: [src/gameobjects/components/AlphaSingle.js#L22](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/AlphaSingle.js#L22)  
> Since: 3.0.0

---

## \_blendMode

### \_blendMode: number

**Description:**

Private internal value. Holds the current blend mode.

**Access:** private

**Inherits:** [Phaser.GameObjects.Components.BlendMode#\_blendMode](../namespace/gameobjects-components-blendmode.md)

> Source: [src/gameobjects/components/BlendMode.js#L19](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/BlendMode.js#L19)  
> Since: 3.0.0

---

## \_checkerboard

### \_checkerboard: WebGLTexture

**Description:**

If this Plane has a checkboard texture, this is a reference to

the WebGLTexture being used. Otherwise, it's null.

**Access:** private

> Source: [src/gameobjects/plane/Plane.js#L122](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/plane/Plane.js#L122)  
> Since: 3.60.0

---

## \_depth

### \_depth: number

**Description:**

Private internal value. Holds the depth of the Game Object.

**Access:** private

**Inherits:** [Phaser.GameObjects.Components.Depth#\_depth](../namespace/gameobjects-components-depth.md)

> Source: [src/gameobjects/components/Depth.js#L19](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Depth.js#L19)  
> Since: 3.0.0

---

## \_rotation

### \_rotation: number

**Description:**

Private internal value. Holds the rotation value in radians.

**Access:** private

**Inherits:** [Phaser.GameObjects.Components.Transform#\_rotation](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L59](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L59)  
> Since: 3.0.0

---

## \_scaleX

### \_scaleX: number

**Description:**

Private internal value. Holds the horizontal scale value.

**Access:** private

**Inherits:** [Phaser.GameObjects.Components.Transform#\_scaleX](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L37](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L37)  
> Since: 3.0.0

---

## \_scaleY

### \_scaleY: number

**Description:**

Private internal value. Holds the vertical scale value.

**Access:** private

**Inherits:** [Phaser.GameObjects.Components.Transform#\_scaleY](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L48](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L48)  
> Since: 3.0.0

---

## \_sizeComponent

### \_sizeComponent: boolean

**Description:**

A property indicating that a Game Object has this component.

**Access:** private

**Inherits:** [Phaser.GameObjects.Components.Size#\_sizeComponent](../namespace/gameobjects-components-size.md)

> Source: [src/gameobjects/components/Size.js#L16](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Size.js#L16)  
> Since: 3.2.0

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

## dirtyCache

### dirtyCache: Array.<number>

**Description:**

An internal cache, used to compare position, rotation, scale and face data

each frame, to avoid math calculations in `preUpdate`.

Cache structure = position xyz | rotation xyz | scale xyz | face count | view | ortho

**Access:** private

**Inherits:** [Phaser.GameObjects.Mesh#dirtyCache](gameobjects-mesh.md)

> Source: [src/gameobjects/mesh/Mesh.js#L252](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/mesh/Mesh.js#L252)  
> Since: 3.50.0

---

## isCropped

### isCropped: boolean

**Description:**

Internal flag. Not to be set by this Game Object.

**Access:** private

**Inherits:** [Phaser.GameObjects.Components.Texture#isCropped](../namespace/gameobjects-components-texture.md)

> Source: [src/gameobjects/components/Texture.js#L39](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Texture.js#L39)  
> Since: 3.11.0

---

## totalFrame

### totalFrame: number

**Description:**

Internal cache var for the total number of faces rendered this frame.

See `totalRendered` instead for the actual value.

**Access:** private

**Inherits:** [Phaser.GameObjects.Mesh#totalFrame](gameobjects-mesh.md)

> Source: [src/gameobjects/mesh/Mesh.js#L319](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/mesh/Mesh.js#L319)  
> Since: 3.50.0

---

# Public Methods

## addedToScene

### <instance> addedToScene()

**Description:**

This callback is invoked when this Game Object is added to a Scene.

Can be overriden by custom Game Objects, but be aware of some Game Objects that

will use this, such as Sprites, to add themselves into the Update List.

You can also listen for the `ADDED_TO_SCENE` event from this Game Object.

**Inherits:** [Phaser.GameObjects.GameObject#addedToScene](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L562](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L562)  
> Since: 3.50.0

---

## addFace

### <instance> addFace(vertex1, vertex2, vertex3)

**Description:**

Adds a new Face into the faces array of this Mesh.

A Face consists of references to 3 Vertex instances, which must be provided.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| vertex1 | [Phaser.Geom.Mesh.Vertex](geom-mesh-vertex.md) | No | The first vertex of the Face. |
| --- | --- | --- | --- |
| vertex2 | [Phaser.Geom.Mesh.Vertex](geom-mesh-vertex.md) | No | The second vertex of the Face. |
| vertex3 | [Phaser.Geom.Mesh.Vertex](geom-mesh-vertex.md) | No | The third vertex of the Face. |

**Returns:** [Phaser.GameObjects.Plane](gameobjects-plane.md) - This Mesh Game Object.

**Inherits:** [Phaser.GameObjects.Mesh#addFace](gameobjects-mesh.md)

> Source: [src/gameobjects/mesh/Mesh.js#L660](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/mesh/Mesh.js#L660)  
> Since: 3.50.0

---

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

**Returns:** [Phaser.GameObjects.Plane](gameobjects-plane.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#addListener](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L111](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L111)  
> Since: 3.0.0

---

## addToDisplayList

### <instance> addToDisplayList([displayList])

**Description:**

Adds this Game Object to the given Display List.

If no Display List is specified, it will default to the Display List owned by the Scene to which

this Game Object belongs.

A Game Object can only exist on one Display List at any given time, but may move freely between them.

If this Game Object is already on another Display List when this method is called, it will first

be removed from it, before being added to the new list.

You can query which list it is on by looking at the `Phaser.GameObjects.GameObject#displayList` property.

If a Game Object isn't on any display list, it will not be rendered. If you just wish to temporarly

disable it from rendering, consider using the `setVisible` method, instead.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| displayList | [Phaser.GameObjects.DisplayList](gameobjects-displaylist.md) | [Phaser.GameObjects.Layer](gameobjects-layer.md) | Yes | The Display List to add to. Defaults to the Scene Display List. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Plane](gameobjects-plane.md) - This Game Object.

**Fires:** [Phaser.Scenes.Events#event:ADDED\_TO\_SCENE](../event/scenes-events.md), [Phaser.GameObjects.Events#event:ADDED\_TO\_SCENE](../event/gameobjects-events.md)

**Inherits:** [Phaser.GameObjects.GameObject#addToDisplayList](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L684](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L684)  
> Since: 3.53.0

---

## addToUpdateList

### <instance> addToUpdateList()

**Description:**

Adds this Game Object to the Update List belonging to the Scene.

When a Game Object is added to the Update List it will have its `preUpdate` method called

every game frame. This method is passed two parameters: `delta` and `time`.

If you wish to run your own logic within `preUpdate` then you should always call

`super.preUpdate(delta, time)` within it, or it may fail to process required operations,

such as Sprite animations.

**Returns:** [Phaser.GameObjects.Plane](gameobjects-plane.md) - This Game Object.

**Inherits:** [Phaser.GameObjects.GameObject#addToUpdateList](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L735](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L735)  
> Since: 3.53.0

---

## addVertex

### <instance> addVertex(x, y, z, u, v, [color], [alpha])

**Description:**

Adds a new Vertex into the vertices array of this Mesh.

Just adding a vertex isn't enough to render it. You need to also

make it part of a Face, with 3 Vertex instances per Face.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | No |  | The x position of the vertex. |
| --- | --- | --- | --- | --- |
| y | number | No |  | The y position of the vertex. |
| z | number | No |  | The z position of the vertex. |
| u | number | No |  | The UV u coordinate of the vertex. |
| v | number | No |  | The UV v coordinate of the vertex. |
| color | number | Yes | "0xffffff" | The color value of the vertex. |
| alpha | number | Yes | 1 | The alpha value of the vertex. |

**Returns:** [Phaser.GameObjects.Plane](gameobjects-plane.md) - This Mesh Game Object.

**Inherits:** [Phaser.GameObjects.Mesh#addVertex](gameobjects-mesh.md)

> Source: [src/gameobjects/mesh/Mesh.js#L632](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/mesh/Mesh.js#L632)  
> Since: 3.50.0

---

## addVertices

### <instance> addVertices(vertices, uvs, [indicies], [containsZ], [normals], [colors], [alphas])

**Description:**

Adds new vertices to this Mesh by parsing the given data.

This method will take vertex data in one of two formats, based on the `containsZ` parameter.

If your vertex data are `x`, `y` pairs, then `containsZ` should be `false` (this is the default, and will result in `z=0` for each vertex).

If your vertex data is groups of `x`, `y` and `z` values, then the `containsZ` parameter must be true.

The `uvs` parameter is a numeric array consisting of `u` and `v` pairs.

The `normals` parameter is a numeric array consisting of `x`, `y` vertex normal values and, if `containsZ` is true, `z` values as well.

The `indicies` parameter is an optional array that, if given, is an indexed list of vertices to be added.

The `colors` parameter is an optional array, or single value, that if given sets the color of each vertex created.

The `alphas` parameter is an optional array, or single value, that if given sets the alpha of each vertex created.

When providing indexed data it is assumed that *all* of the arrays are indexed, not just the vertices.

The following example will create a 256 x 256 sized quad using an index array:

```
Copy
let mesh = new Mesh(this);  // Assuming `this` is a scene!

const vertices = [

  -128, 128,

  128, 128,

  -128, -128,

  128, -128

];



const uvs = [

  0, 1,

  1, 1,

  0, 0,

  1, 0

];



const indices = [ 0, 2, 1, 2, 3, 1 ];



mesh.addVertices(vertices, uvs, indicies);

// Note: Otherwise the added points will be "behind" the camera! This value will project vertex `x` & `y` values 1:1 to pixel values.

mesh.hideCCW = false;

mesh.setOrtho(mesh.width, mesh.height);


```

If the data is not indexed, it's assumed that the arrays all contain sequential data.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| vertices | Array.<number> | No |  | The vertices array. Either `xy` pairs, or `xyz` if the `containsZ` parameter is `true`. |
| --- | --- | --- | --- | --- |
| uvs | Array.<number> | No |  | The UVs pairs array. |
| indicies | Array.<number> | Yes |  | Optional vertex indicies array. If you don't have one, pass `null` or an empty array. |
| containsZ | boolean | Yes | false | Does the vertices data include a `z` component? If not, it will be assumed `z=0`, see methods `panZ` or `setOrtho`. |
| normals | Array.<number> | Yes |  | Optional vertex normals array. If you don't have one, pass `null` or an empty array. |
| colors | number | Array.<number> | Yes | "0xffffff" | An array of colors, one per vertex, or a single color value applied to all vertices. |
| alphas | number | Array.<number> | Yes | 1 | An array of alpha values, one per vertex, or a single alpha value applied to all vertices. |

**Returns:** [Phaser.GameObjects.Plane](gameobjects-plane.md) - This Mesh Game Object.

**Inherits:** [Phaser.GameObjects.Mesh#addVertices](gameobjects-mesh.md)

> Source: [src/gameobjects/mesh/Mesh.js#L685](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/mesh/Mesh.js#L685)  
> Since: 3.50.0

---

## addVerticesFromObj

### <instance> addVerticesFromObj(key, [scale], [x], [y], [z], [rotateX], [rotateY], [rotateZ], [zIsUp])

**Description:**

This method will add the data from a triangulated Wavefront OBJ model file to this Mesh.

The data should have been loaded via the OBJFile:

```
Copy
this.load.obj(key, url);


```

Then use the same `key` as the first parameter to this method.

Multiple Mesh Game Objects can use the same model data without impacting on each other.

Make sure your 3D package has triangulated the model data prior to exporting it.

You can add multiple models to a single Mesh, although they will act as one when

moved or rotated. You can scale the model data, should it be too small, or too large, to see.

You can also offset the vertices of the model via the `x`, `y` and `z` parameters.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | string | No |  | The key of the model data in the OBJ Cache to add to this Mesh. |
| --- | --- | --- | --- | --- |
| scale | number | Yes | 1 | An amount to scale the model data by. Use this if the model has exported too small, or large, to see. |
| x | number | Yes | 0 | Translate the model x position by this amount. |
| y | number | Yes | 0 | Translate the model y position by this amount. |
| z | number | Yes | 0 | Translate the model z position by this amount. |
| rotateX | number | Yes | 0 | Rotate the model on the x axis by this amount, in radians. |
| rotateY | number | Yes | 0 | Rotate the model on the y axis by this amount, in radians. |
| rotateZ | number | Yes | 0 | Rotate the model on the z axis by this amount, in radians. |
| zIsUp | boolean | Yes | true | Is the z axis up (true), or is y axis up (false)? |

**Returns:** [Phaser.GameObjects.Plane](gameobjects-plane.md) - This Mesh Game Object.

**Inherits:** [Phaser.GameObjects.Mesh#addVerticesFromObj](gameobjects-mesh.md)

> Source: [src/gameobjects/mesh/Mesh.js#L546](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/mesh/Mesh.js#L546)  
> Since: 3.50.0

---

## clear

### <instance> clear()

**Description:**

Iterates and destroys all current Faces in this Mesh, then resets the

`faces` and `vertices` arrays.

**Returns:** [Phaser.GameObjects.Plane](gameobjects-plane.md) - This Mesh Game Object.

**Inherits:** [Phaser.GameObjects.Mesh#clear](gameobjects-mesh.md)

> Source: [src/gameobjects/mesh/Mesh.js#L524](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/mesh/Mesh.js#L524)  
> Since: 3.50.0

---

## clearAlpha

### <instance> clearAlpha()

**Description:**

Clears all alpha values associated with this Game Object.

Immediately sets the alpha levels back to 1 (fully opaque).

**Returns:** [Phaser.GameObjects.Plane](gameobjects-plane.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.AlphaSingle#clearAlpha](../namespace/gameobjects-components-alphasingle.md)

> Source: [src/gameobjects/components/AlphaSingle.js#L33](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/AlphaSingle.js#L33)  
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

**Returns:** [Phaser.GameObjects.Plane](gameobjects-plane.md) - This Game Object.

**Inherits:** [Phaser.GameObjects.Components.PostPipeline#clearFX](../namespace/gameobjects-components-postpipeline.md)

> Source: [src/gameobjects/components/PostPipeline.js#L337](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/PostPipeline.js#L337)  
> Since: 3.60.0

---

## clearMask

### <instance> clearMask([destroyMask])

**Description:**

Clears the mask that this Game Object was using.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| destroyMask | boolean | Yes | false | Destroy the mask before clearing it? |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Plane](gameobjects-plane.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Mask#clearMask](../namespace/gameobjects-components-mask.md)

> Source: [src/gameobjects/components/Mask.js#L56](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Mask.js#L56)  
> Since: 3.6.2

---

## clearTint

### <instance> clearTint()

**Description:**

Clears all tint values associated with this Game Object.

Immediately sets the color values back to 0xffffff on all vertices,

which results in no visible change to the texture.

**Tags:**

* webglOnly

**Returns:** [Phaser.GameObjects.Plane](gameobjects-plane.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Mesh#clearTint](gameobjects-mesh.md)

> Source: [src/gameobjects/mesh/Mesh.js#L1136](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/mesh/Mesh.js#L1136)  
> Since: 3.60.0

---

## copyPosition

### <instance> copyPosition(source)

**Description:**

Copies an object's coordinates to this Game Object's position.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| source | [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) | [Phaser.Types.Math.Vector3Like](../typedef/types-math.md) | [Phaser.Types.Math.Vector4Like](../typedef/types-math.md) | No |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Plane](gameobjects-plane.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Transform#copyPosition](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L293](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L293)  
> Since: 3.50.0

---

## createBitmapMask

### <instance> createBitmapMask([maskObject], [x], [y], [texture], [frame])

**Description:**

Creates and returns a Bitmap Mask. This mask can be used by any Game Object,

including this one, or a Dynamic Texture.

Note: Bitmap Masks only work on WebGL. Geometry Masks work on both WebGL and Canvas.

To create the mask you need to pass in a reference to a renderable Game Object.

A renderable Game Object is one that uses a texture to render with, such as an

Image, Sprite, Render Texture or BitmapText.

If you do not provide a renderable object, and this Game Object has a texture,

it will use itself as the object. This means you can call this method to create

a Bitmap Mask from any renderable texture-based Game Object.

**Tags:**

* generic
* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| maskObject | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | [Phaser.Textures.DynamicTexture](textures-dynamictexture.md) | Yes | The Game Object or Dynamic Texture that will be used as the mask. If `null` it will generate an Image Game Object using the rest of the arguments. |
| --- | --- | --- | --- |
| x | number | Yes | If creating a Game Object, the horizontal position in the world. |
| y | number | Yes | If creating a Game Object, the vertical position in the world. |
| texture | string | [Phaser.Textures.Texture](textures-texture.md) | Yes | If creating a Game Object, the key, or instance of the Texture it will use to render with, as stored in the Texture Manager. |
| frame | string | number | [Phaser.Textures.Frame](textures-frame.md) | Yes |

**Returns:** [Phaser.Display.Masks.BitmapMask](display-masks-bitmapmask.md) - This Bitmap Mask that was created.

**Inherits:** [Phaser.GameObjects.Components.Mask#createBitmapMask](../namespace/gameobjects-components-mask.md)

> Source: [src/gameobjects/components/Mask.js#L80](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Mask.js#L80)  
> Since: 3.6.2

---

## createCheckerboard

### <instance> createCheckerboard([color1], [color2], [alpha1], [alpha2], [height])

**Description:**

Creates a checkerboard style texture, based on the given colors and alpha

values and applies it to this Plane, replacing any current texture it may

have.

The colors are used in an alternating pattern, like a chess board.

Calling this method generates a brand new 16x16 pixel WebGLTexture internally

and applies it to this Plane. While quite fast to do, you should still be

mindful of calling this method either extensively, or in tight parts of

your game.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| color1 | number | Yes | "0xffffff" | The odd cell color, specified as a hex value. |
| --- | --- | --- | --- | --- |
| color2 | number | Yes | "0x0000ff" | The even cell color, specified as a hex value. |
| alpha1 | number | Yes | 255 | The odd cell alpha value, specified as a number between 0 and 255. |
| alpha2 | number | Yes | 255 | The even cell alpha value, specified as a number between 0 and 255. |
| height | number | Yes | 128 | The view height of the Plane after creation, in pixels. |

> Source: [src/gameobjects/plane/Plane.js#L360](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/plane/Plane.js#L360)  
> Since: 3.60.0

---

## createGeometryMask

### <instance> createGeometryMask([graphics])

**Description:**

Creates and returns a Geometry Mask. This mask can be used by any Game Object,

including this one.

To create the mask you need to pass in a reference to a Graphics Game Object.

If you do not provide a graphics object, and this Game Object is an instance

of a Graphics object, then it will use itself to create the mask.

This means you can call this method to create a Geometry Mask from any Graphics Game Object.

**Tags:**

* generic
* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| graphics | [Phaser.GameObjects.Graphics](gameobjects-graphics.md) | [Phaser.GameObjects.Shape](gameobjects-shape.md) | Yes | A Graphics Game Object, or any kind of Shape Game Object. The geometry within it will be used as the mask. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Display.Masks.GeometryMask](display-masks-geometrymask.md) - This Geometry Mask that was created.

**Inherits:** [Phaser.GameObjects.Components.Mask#createGeometryMask](../namespace/gameobjects-components-mask.md)

> Source: [src/gameobjects/components/Mask.js#L120](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Mask.js#L120)  
> Since: 3.6.2

---

## depthSort

### <instance> depthSort()

**Description:**

Runs a depth sort across all Faces in this Mesh, comparing their averaged depth.

This is called automatically if you use any of the `rotate` methods, but you can

also invoke it to sort the Faces should you manually position them.

**Returns:** [Phaser.GameObjects.Plane](gameobjects-plane.md) - This Mesh Game Object.

**Inherits:** [Phaser.GameObjects.Mesh#depthSort](gameobjects-mesh.md)

> Source: [src/gameobjects/mesh/Mesh.js#L614](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/mesh/Mesh.js#L614)  
> Since: 3.50.0

---

## destroy

### <instance> destroy([fromScene])

**Description:**

Destroys this Game Object removing it from the Display List and Update List and

severing all ties to parent resources.

Also removes itself from the Input Manager and Physics Manager if previously enabled.

Use this to remove a Game Object from your game if you don't ever plan to use it again.

As long as no reference to it exists within your own code it should become free for

garbage collection by the browser.

If you just want to temporarily disable an object then look at using the

Game Object Pool instead of destroying it, as destroyed objects cannot be resurrected.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| fromScene | boolean | Yes | false | `True` if this Game Object is being destroyed by the Scene, `false` if not. |
| --- | --- | --- | --- | --- |

**Fires:** [Phaser.GameObjects.Events#event:DESTROY](../event/gameobjects-events.md)

**Inherits:** [Phaser.GameObjects.GameObject#destroy](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L855](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L855)  
> Since: 3.0.0

---

## disableInteractive

### <instance> disableInteractive([resetCursor])

**Description:**

If this Game Object has previously been enabled for input, this will disable it.

An object that is disabled for input stops processing or being considered for

input events, but can be turned back on again at any time by simply calling

`setInteractive()` with no arguments provided.

If want to completely remove interaction from this Game Object then use `removeInteractive` instead.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| resetCursor | boolean | Yes | false | Should the currently active Input cursor, if any, be reset to the default cursor? |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Plane](gameobjects-plane.md) - This GameObject.

**Inherits:** [Phaser.GameObjects.GameObject#disableInteractive](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L494](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L494)  
> Since: 3.7.0

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

## getData

### <instance> getData(key)

**Description:**

Retrieves the value for the given key in this Game Objects Data Manager, or undefined if it doesn't exist.

You can also access values via the `values` object. For example, if you had a key called `gold` you can do either:

```
Copy
sprite.getData('gold');


```

Or access the value directly:

```
Copy
sprite.data.values.gold;


```

You can also pass in an array of keys, in which case an array of values will be returned:

```
Copy
sprite.getData([ 'gold', 'armor', 'health' ]);


```

This approach is useful for destructuring arrays in ES6.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | Array.<string> | No | The key of the value to retrieve, or an array of keys. |
| --- | --- | --- | --- |

**Returns:** \* - The value belonging to the given key, or an array of values, the order of which will match the input array.

**Inherits:** [Phaser.GameObjects.GameObject#getData](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L416](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L416)  
> Since: 3.0.0

---

## getDisplayList

### <instance> getDisplayList()

**Description:**

Returns a reference to the underlying display list *array* that contains this Game Object,

which will be either the Scene's Display List or the internal list belonging

to its parent Container, if it has one.

If this Game Object is not on a display list or in a container, it will return `null`.

You should be very careful with this method, and understand that it returns a direct reference to the

internal array used by the Display List. Mutating this array directly can cause all kinds of subtle

and difficult to debug issues in your game.

**Returns:** Array.<[Phaser.GameObjects.GameObject](gameobjects-gameobject.md)> - The internal Display List array of Game Objects, or `null`.

**Inherits:** [Phaser.GameObjects.GameObject#getDisplayList](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L823](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L823)  
> Since: 3.85.0

---

## getFace

### <instance> getFace(index)

**Description:**

Returns the Face at the given index in this Mesh Game Object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| index | number | No | The index of the Face to get. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Geom.Mesh.Face](geom-mesh-face.md) - The Face at the given index, or `undefined` if index out of range.

**Inherits:** [Phaser.GameObjects.Mesh#getFace](gameobjects-mesh.md)

> Source: [src/gameobjects/mesh/Mesh.js#L792](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/mesh/Mesh.js#L792)  
> Since: 3.50.0

---

## getFaceAt

### <instance> getFaceAt(x, y, [camera])

**Description:**

Return an array of Face objects from this Mesh that intersect with the given coordinates.

The given position is translated through the matrix of this Mesh and the given Camera,

before being compared against the vertices.

If more than one Face intersects, they will all be returned in the array, but the array will

be depth sorted first, so the first element will always be that closest to the camera.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The x position to check against. |
| --- | --- | --- | --- |
| y | number | No | The y position to check against. |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | Yes | The camera to pass the coordinates through. If not give, the default Scene Camera is used. |

**Returns:** Array.<[Phaser.Geom.Mesh.Face](geom-mesh-face.md)> - An array of Face objects that intersect with the given point, ordered by depth.

**Inherits:** [Phaser.GameObjects.Mesh#getFaceAt](gameobjects-mesh.md)

> Source: [src/gameobjects/mesh/Mesh.js#L843](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/mesh/Mesh.js#L843)  
> Since: 3.50.0

---

## getFaceCount

### <instance> getFaceCount()

**Description:**

Returns the total number of Faces in this Mesh Game Object.

**Returns:** number - The number of Faces in this Mesh Game Object.

**Inherits:** [Phaser.GameObjects.Mesh#getFaceCount](gameobjects-mesh.md)

> Source: [src/gameobjects/mesh/Mesh.js#L766](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/mesh/Mesh.js#L766)  
> Since: 3.50.0

---

## getIndexList

### <instance> getIndexList()

**Description:**

Returns an array containing the display list index of either this Game Object, or if it has one,

its parent Container. It then iterates up through all of the parent containers until it hits the

root of the display list (which is index 0 in the returned array).

Used internally by the InputPlugin but also useful if you wish to find out the display depth of

this Game Object and all of its ancestors.

**Returns:** Array.<number> - An array of display list position indexes.

**Inherits:** [Phaser.GameObjects.GameObject#getIndexList](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L635](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L635)  
> Since: 3.4.0

---

## getLocalPoint

### <instance> getLocalPoint(x, y, [point], [camera])

**Description:**

Takes the given `x` and `y` coordinates and converts them into local space for this

Game Object, taking into account parent and local transforms, and the Display Origin.

The returned Vector2 contains the translated point in its properties.

A Camera needs to be provided in order to handle modified scroll factors. If no

camera is specified, it will use the `main` camera from the Scene to which this

Game Object belongs.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The x position to translate. |
| --- | --- | --- | --- |
| y | number | No | The y position to translate. |
| point | [Phaser.Math.Vector2](math-vector2.md) | Yes | A Vector2, or point-like object, to store the results in. |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | Yes | The Camera which is being tested against. If not given will use the Scene default camera. |

**Returns:** [Phaser.Math.Vector2](math-vector2.md) - The translated point.

**Inherits:** [Phaser.GameObjects.Components.Transform#getLocalPoint](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L542](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L542)  
> Since: 3.50.0

---

## getLocalTransformMatrix

### <instance> getLocalTransformMatrix([tempMatrix])

**Description:**

Gets the local transform matrix for this Game Object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tempMatrix | [Phaser.GameObjects.Components.TransformMatrix](gameobjects-components-transformmatrix.md) | Yes | The matrix to populate with the values from this Game Object. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Components.TransformMatrix](gameobjects-components-transformmatrix.md) - The populated Transform Matrix.

**Inherits:** [Phaser.GameObjects.Components.Transform#getLocalTransformMatrix](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L484](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L484)  
> Since: 3.4.0

---

## getParentRotation

### <instance> getParentRotation()

**Description:**

Gets the sum total rotation of all of this Game Objects parent Containers.

The returned value is in radians and will be zero if this Game Object has no parent container.

**Returns:** number - The sum total rotation, in radians, of all parent containers of this Game Object.

**Inherits:** [Phaser.GameObjects.Components.Transform#getParentRotation](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L592](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L592)  
> Since: 3.18.0

---

## getPipelineName

### <instance> getPipelineName()

**Description:**

Gets the name of the WebGL Pipeline this Game Object is currently using.

**Tags:**

* webglOnly

**Returns:** string - The string-based name of the pipeline being used by this Game Object, or null.

**Inherits:** [Phaser.GameObjects.Components.Pipeline#getPipelineName](../namespace/gameobjects-components-pipeline.md)

> Source: [src/gameobjects/components/Pipeline.js#L201](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Pipeline.js#L201)  
> Since: 3.0.0

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

## getVertexCount

### <instance> getVertexCount()

**Description:**

Returns the total number of Vertices in this Mesh Game Object.

**Returns:** number - The number of Vertices in this Mesh Game Object.

**Inherits:** [Phaser.GameObjects.Mesh#getVertexCount](gameobjects-mesh.md)

> Source: [src/gameobjects/mesh/Mesh.js#L779](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/mesh/Mesh.js#L779)  
> Since: 3.50.0

---

## getWorldTransformMatrix

### <instance> getWorldTransformMatrix([tempMatrix], [parentMatrix])

**Description:**

Gets the world transform matrix for this Game Object, factoring in any parent Containers.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tempMatrix | [Phaser.GameObjects.Components.TransformMatrix](gameobjects-components-transformmatrix.md) | Yes | The matrix to populate with the values from this Game Object. |
| --- | --- | --- | --- |
| parentMatrix | [Phaser.GameObjects.Components.TransformMatrix](gameobjects-components-transformmatrix.md) | Yes | A temporary matrix to hold parent values during the calculations. |

**Returns:** [Phaser.GameObjects.Components.TransformMatrix](gameobjects-components-transformmatrix.md) - The populated Transform Matrix.

**Inherits:** [Phaser.GameObjects.Components.Transform#getWorldTransformMatrix](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L501](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L501)  
> Since: 3.4.0

---

## hasFaceAt

### <instance> hasFaceAt(x, y, [camera])

**Description:**

Tests to see if *any* face in this Mesh intersects with the given coordinates.

The given position is translated through the matrix of this Mesh and the given Camera,

before being compared against the vertices.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The x position to check against. |
| --- | --- | --- | --- |
| y | number | No | The y position to check against. |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | Yes | The camera to pass the coordinates through. If not give, the default Scene Camera is used. |

**Returns:** boolean - Returns `true` if *any* face of this Mesh intersects with the given coordinate, otherwise `false`.

**Inherits:** [Phaser.GameObjects.Mesh#hasFaceAt](gameobjects-mesh.md)

> Source: [src/gameobjects/mesh/Mesh.js#L807](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/mesh/Mesh.js#L807)  
> Since: 3.60.0

---

## incData

### <instance> incData(key, [amount])

**Description:**

Increase a value for the given key within this Game Objects Data Manager. If the key doesn't already exist in the Data Manager then it is increased from 0.

If the Game Object has not been enabled for data (via `setDataEnabled`) then it will be enabled

before setting the value.

If the key doesn't already exist in the Data Manager then it is created.

When the value is first set, a `setdata` event is emitted from this Game Object.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | string | No |  | The key to change the value for. |
| --- | --- | --- | --- | --- |
| amount | number | Yes | 1 | The amount to increase the given key by. Pass a negative value to decrease the key. |

**Returns:** [Phaser.GameObjects.Plane](gameobjects-plane.md) - This GameObject.

**Inherits:** [Phaser.GameObjects.GameObject#incData](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L357](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L357)  
> Since: 3.23.0

---

## initPipeline

### <instance> initPipeline([pipeline])

**Description:**

Sets the initial WebGL Pipeline of this Game Object.

This should only be called during the instantiation of the Game Object. After that, use `setPipeline`.

**Tags:**

* webglOnly

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pipeline | string | [Phaser.Renderer.WebGL.WebGLPipeline](renderer-webgl-webglpipeline.md) | Yes | Either the string-based name of the pipeline, or a pipeline instance to set. |
| --- | --- | --- | --- |

**Returns:** boolean - `true` if the pipeline was set successfully, otherwise `false`.

**Inherits:** [Phaser.GameObjects.Components.Pipeline#initPipeline](../namespace/gameobjects-components-pipeline.md)

> Source: [src/gameobjects/components/Pipeline.js#L53](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Pipeline.js#L53)  
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

## isDirty

### <instance> isDirty()

**Description:**

Checks if the transformation data in this mesh is dirty.

This is used internally by the `preUpdate` step to determine if the vertices should

be recalculated or not.

**Returns:** boolean - Returns `true` if the data of this mesh is dirty, otherwise `false`.

**Inherits:** [Phaser.GameObjects.Mesh#isDirty](gameobjects-mesh.md)

> Source: [src/gameobjects/mesh/Mesh.js#L949](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/mesh/Mesh.js#L949)  
> Since: 3.50.0

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

**Returns:** [Phaser.GameObjects.Plane](gameobjects-plane.md) - `this`.

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

**Returns:** [Phaser.GameObjects.Plane](gameobjects-plane.md) - `this`.

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

**Returns:** [Phaser.GameObjects.Plane](gameobjects-plane.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#once](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L124](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L124)  
> Since: 3.0.0

---

## panX

### <instance> panX(v)

**Description:**

Translates the view position of this Mesh on the x axis by the given amount.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| v | number | No | The amount to pan by. |
| --- | --- | --- | --- |

**Inherits:** [Phaser.GameObjects.Mesh#panX](gameobjects-mesh.md)

> Source: [src/gameobjects/mesh/Mesh.js#L399](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/mesh/Mesh.js#L399)  
> Since: 3.50.0

---

## panY

### <instance> panY(v)

**Description:**

Translates the view position of this Mesh on the y axis by the given amount.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| v | number | No | The amount to pan by. |
| --- | --- | --- | --- |

**Inherits:** [Phaser.GameObjects.Mesh#panY](gameobjects-mesh.md)

> Source: [src/gameobjects/mesh/Mesh.js#L416](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/mesh/Mesh.js#L416)  
> Since: 3.50.0

---

## panZ

### <instance> panZ(v)

**Description:**

Translates the view position of this Mesh on the z axis by the given amount.

As the default `panZ` value is 0, vertices with `z=0` (the default) need special

care or else they will not display as they are "behind" the camera.

Consider using `mesh.panZ(mesh.height / (2 * Math.tan(Math.PI / 16)))`,

which will interpret vertex geometry 1:1 with pixel geometry (or see `setOrtho`).

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| v | number | No | The amount to pan by. |
| --- | --- | --- | --- |

**Inherits:** [Phaser.GameObjects.Mesh#panZ](gameobjects-mesh.md)

> Source: [src/gameobjects/mesh/Mesh.js#L433](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/mesh/Mesh.js#L433)  
> Since: 3.50.0

---

## play

### <instance> play(key, [ignoreIfPlaying])

**Description:**

Start playing the given animation on this Plane.

Animations in Phaser can either belong to the global Animation Manager, or specifically to this Plane.

The benefit of a global animation is that multiple Game Objects can all play the same animation, without

having to duplicate the data. You can just create it once and then play it on any animating Game Object.

The following code shows how to create a global repeating animation. The animation will be created

from all of the frames within the sprite sheet that was loaded with the key 'muybridge':

```
Copy
var config = {

    key: 'run',

    frames: 'muybridge',

    frameRate: 15,

    repeat: -1

};



//  This code should be run from within a Scene:

this.anims.create(config);


```

However, if you wish to create an animation that is unique to this Plane, and this Plane alone,

you can call the `Animation.create` method instead. It accepts the exact same parameters as when

creating a global animation, however the resulting data is kept locally in this Plane.

With the animation created, either globally or locally, you can now play it on this Plane:

```
Copy
const plane = this.add.plane(...);

plane.play('run');


```

Alternatively, if you wish to run it at a different frame rate for example, you can pass a config

object instead:

```
Copy
const plane = this.add.plane(...);

plane.play({ key: 'run', frameRate: 24 });


```

When playing an animation on a Plane it will first check to see if it can find a matching key

locally within the Plane. If it can, it will play the local animation. If not, it will then

search the global Animation Manager and look for it there.

If you need a Plane to be able to play both local and global animations, make sure they don't

have conflicting keys.

See the documentation for the `PlayAnimationConfig` config object for more details about this.

Also, see the documentation in the Animation Manager for further details on creating animations.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | string | [Phaser.Animations.Animation](animations-animation.md) | [Phaser.Types.Animations.PlayAnimationConfig](../typedef/types-animations.md) | No |  |
| --- | --- | --- | --- | --- |
| ignoreIfPlaying | boolean | Yes | false | If an animation is already playing then ignore this call. |

**Returns:** [Phaser.GameObjects.Plane](gameobjects-plane.md) - This Game Object.

**Fires:** [Phaser.Animations.Events#event:ANIMATION\_START](../event/animations-events.md)

> Source: [src/gameobjects/plane/Plane.js#L441](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/plane/Plane.js#L441)  
> Since: 3.60.0

---

## playAfterDelay

### <instance> playAfterDelay(key, delay)

**Description:**

Waits for the specified delay, in milliseconds, then starts playback of the given animation.

If the animation *also* has a delay value set in its config, it will be **added** to the delay given here.

If an animation is already running and a new animation is given to this method, it will wait for

the given delay before starting the new animation.

If no animation is currently running, the given one begins after the delay.

When playing an animation on a Game Object it will first check to see if it can find a matching key

locally within the Game Object. If it can, it will play the local animation. If not, it will then

search the global Animation Manager and look for it there.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | [Phaser.Animations.Animation](animations-animation.md) | [Phaser.Types.Animations.PlayAnimationConfig](../typedef/types-animations.md) | No |
| --- | --- | --- | --- |
| delay | number | No | The delay, in milliseconds, to wait before starting the animation playing. |

**Returns:** [Phaser.GameObjects.Plane](gameobjects-plane.md) - This Game Object.

**Fires:** [Phaser.Animations.Events#event:ANIMATION\_START](../event/animations-events.md)

> Source: [src/gameobjects/plane/Plane.js#L575](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/plane/Plane.js#L575)  
> Since: 3.60.0

---

## playAfterRepeat

### <instance> playAfterRepeat(key, [repeatCount])

**Description:**

Waits for the current animation to complete the `repeatCount` number of repeat cycles, then starts playback

of the given animation.

You can use this to ensure there are no harsh jumps between two sets of animations, i.e. going from an

idle animation to a walking animation, by making them blend smoothly into each other.

If no animation is currently running, the given one will start immediately.

When playing an animation on a Game Object it will first check to see if it can find a matching key

locally within the Game Object. If it can, it will play the local animation. If not, it will then

search the global Animation Manager and look for it there.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | string | [Phaser.Animations.Animation](animations-animation.md) | [Phaser.Types.Animations.PlayAnimationConfig](../typedef/types-animations.md) | No |  |
| --- | --- | --- | --- | --- |
| repeatCount | number | Yes | 1 | How many times should the animation repeat before the next one starts? |

**Returns:** [Phaser.GameObjects.Plane](gameobjects-plane.md) - This Game Object.

**Fires:** [Phaser.Animations.Events#event:ANIMATION\_START](../event/animations-events.md)

> Source: [src/gameobjects/plane/Plane.js#L603](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/plane/Plane.js#L603)  
> Since: 3.60.0

---

## playReverse

### <instance> playReverse(key, [ignoreIfPlaying])

**Description:**

Start playing the given animation on this Plane, in reverse.

Animations in Phaser can either belong to the global Animation Manager, or specifically to a Game Object.

The benefit of a global animation is that multiple Game Objects can all play the same animation, without

having to duplicate the data. You can just create it once and then play it on any animating Game Object.

The following code shows how to create a global repeating animation. The animation will be created

from all of the frames within the sprite sheet that was loaded with the key 'muybridge':

```
Copy
var config = {

    key: 'run',

    frames: 'muybridge',

    frameRate: 15,

    repeat: -1

};



//  This code should be run from within a Scene:

this.anims.create(config);


```

However, if you wish to create an animation that is unique to this Game Object, and this Game Object alone,

you can call the `Animation.create` method instead. It accepts the exact same parameters as when

creating a global animation, however the resulting data is kept locally in this Game Object.

With the animation created, either globally or locally, you can now play it on this Game Object:

```
Copy
const plane = this.add.plane(...);

plane.playReverse('run');


```

Alternatively, if you wish to run it at a different frame rate, for example, you can pass a config

object instead:

```
Copy
const plane = this.add.plane(...);

plane.playReverse({ key: 'run', frameRate: 24 });


```

When playing an animation on a Game Object it will first check to see if it can find a matching key

locally within the Game Object. If it can, it will play the local animation. If not, it will then

search the global Animation Manager and look for it there.

If you need a Game Object to be able to play both local and global animations, make sure they don't

have conflicting keys.

See the documentation for the `PlayAnimationConfig` config object for more details about this.

Also, see the documentation in the Animation Manager for further details on creating animations.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | string | [Phaser.Animations.Animation](animations-animation.md) | [Phaser.Types.Animations.PlayAnimationConfig](../typedef/types-animations.md) | No |  |
| --- | --- | --- | --- | --- |
| ignoreIfPlaying | boolean | Yes | false | If an animation is already playing then ignore this call. |

**Returns:** [Phaser.GameObjects.Plane](gameobjects-plane.md) - This Game Object.

**Fires:** [Phaser.Animations.Events#event:ANIMATION\_START](../event/animations-events.md)

> Source: [src/gameobjects/plane/Plane.js#L508](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/plane/Plane.js#L508)  
> Since: 3.60.0

---

## preDestroy

### <instance> preDestroy([width], [height], [tile])

**Description:**

Modifies the layout of this Plane by adjusting the grid dimensions to the

given width and height. The values are given in cells, not pixels.

The `tile` parameter allows you to control if the texture is tiled, or

applied across the entire Plane? A tiled texture will repeat with one

iteration per cell. A non-tiled texture will be applied across the whole

Plane.

Note that if this Plane is using a single texture, not from a texture atlas

or sprite sheet, then you can use the `Plane.uvScale` method to have much

more fine-grained control over the texture tiling.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| width | number | Yes | 8 | The width of this Plane, in cells, not pixels. |
| --- | --- | --- | --- | --- |
| height | number | Yes | 8 | The height of this Plane, in cells, not pixels. |
| tile | boolean | Yes | false | Is the texture tiled? I.e. repeated across each cell. |

**Overrides:** Phaser.GameObjects.Mesh#preDestroy

> Source: [src/gameobjects/plane/Plane.js#L176](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/plane/Plane.js#L176)  
> Since: 3.60.0

---

## preUpdate

### <instance> preUpdate(time, delta)

**Description:**

Runs the preUpdate for this Plane, which will check its Animation State,

if one is playing, and refresh view / model matrices, if updated.

**Access:** protected

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| time | number | No | The current timestamp. |
| --- | --- | --- | --- |
| delta | number | No | The delta time, in ms, elapsed since the last frame. |

**Overrides:** Phaser.GameObjects.Mesh#preUpdate

> Source: [src/gameobjects/plane/Plane.js#L718](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/plane/Plane.js#L718)  
> Since: 3.60.0

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

**Returns:** [Phaser.GameObjects.Plane](gameobjects-plane.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#removeAllListeners](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L165](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L165)  
> Since: 3.0.0

---

## removeCheckerboard

### <instance> removeCheckerboard()

**Description:**

If this Plane has a Checkerboard Texture, this method will destroy it

and reset the internal flag for it.

> Source: [src/gameobjects/plane/Plane.js#L424](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/plane/Plane.js#L424)  
> Since: 3.60.0

---

## removedFromScene

### <instance> removedFromScene()

**Description:**

This callback is invoked when this Game Object is removed from a Scene.

Can be overriden by custom Game Objects, but be aware of some Game Objects that

will use this, such as Sprites, to removed themselves from the Update List.

You can also listen for the `REMOVED_FROM_SCENE` event from this Game Object.

**Inherits:** [Phaser.GameObjects.GameObject#removedFromScene](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L577](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L577)  
> Since: 3.50.0

---

## removeFromDisplayList

### <instance> removeFromDisplayList()

**Description:**

Removes this Game Object from the Display List it is currently on.

A Game Object can only exist on one Display List at any given time, but may move freely removed

and added back at a later stage.

You can query which list it is on by looking at the `Phaser.GameObjects.GameObject#displayList` property.

If a Game Object isn't on any Display List, it will not be rendered. If you just wish to temporarly

disable it from rendering, consider using the `setVisible` method, instead.

**Returns:** [Phaser.GameObjects.Plane](gameobjects-plane.md) - This Game Object.

**Fires:** [Phaser.Scenes.Events#event:REMOVED\_FROM\_SCENE](../event/scenes-events.md), [Phaser.GameObjects.Events#event:REMOVED\_FROM\_SCENE](../event/gameobjects-events.md)

**Inherits:** [Phaser.GameObjects.GameObject#removeFromDisplayList](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L760](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L760)  
> Since: 3.53.0

---

## removeFromUpdateList

### <instance> removeFromUpdateList()

**Description:**

Removes this Game Object from the Scene's Update List.

When a Game Object is on the Update List, it will have its `preUpdate` method called

every game frame. Calling this method will remove it from the list, preventing this.

Removing a Game Object from the Update List will stop most internal functions working.

For example, removing a Sprite from the Update List will prevent it from being able to

run animations.

**Returns:** [Phaser.GameObjects.Plane](gameobjects-plane.md) - This Game Object.

**Inherits:** [Phaser.GameObjects.GameObject#removeFromUpdateList](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L798](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L798)  
> Since: 3.53.0

---

## removeInteractive

### <instance> removeInteractive([resetCursor])

**Description:**

If this Game Object has previously been enabled for input, this will queue it

for removal, causing it to no longer be interactive. The removal happens on

the next game step, it is not immediate.

The Interactive Object that was assigned to this Game Object will be destroyed,

removed from the Input Manager and cleared from this Game Object.

If you wish to re-enable this Game Object at a later date you will need to

re-create its InteractiveObject by calling `setInteractive` again.

If you wish to only temporarily stop an object from receiving input then use

`disableInteractive` instead, as that toggles the interactive state, where-as

this erases it completely.

If you wish to resize a hit area, don't remove and then set it as being

interactive. Instead, access the hitarea object directly and resize the shape

being used. I.e.: `sprite.input.hitArea.setSize(width, height)` (assuming the

shape is a Rectangle, which it is by default.)

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| resetCursor | boolean | Yes | false | Should the currently active Input cursor, if any, be reset to the default cursor? |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Plane](gameobjects-plane.md) - This GameObject.

**Inherits:** [Phaser.GameObjects.GameObject#removeInteractive](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L519](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L519)  
> Since: 3.7.0

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

**Returns:** [Phaser.GameObjects.Plane](gameobjects-plane.md) - `this`.

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

**Returns:** [Phaser.GameObjects.Plane](gameobjects-plane.md) - This Game Object.

**Inherits:** [Phaser.GameObjects.Components.PostPipeline#removePostPipeline](../namespace/gameobjects-components-postpipeline.md)

> Source: [src/gameobjects/components/PostPipeline.js#L299](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/PostPipeline.js#L299)  
> Since: 3.60.0

---

## renderDebug

### <instance> renderDebug(src, faces)

**Description:**

The built-in Mesh debug rendering method.

See `Mesh.setDebug` for more details.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| src | [Phaser.GameObjects.Mesh](gameobjects-mesh.md) | No | The Mesh object being rendered. |
| --- | --- | --- | --- |
| faces | Array.<[Phaser.Geom.Mesh.Face](geom-mesh-face.md)> | No | An array of Faces. |

**Inherits:** [Phaser.GameObjects.Mesh#renderDebug](gameobjects-mesh.md)

> Source: [src/gameobjects/mesh/Mesh.js#L1091](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/mesh/Mesh.js#L1091)  
> Since: 3.50.0

---

## resetPipeline

### <instance> resetPipeline([resetData])

**Description:**

Resets the WebGL Pipeline of this Game Object back to the default it was created with.

**Tags:**

* webglOnly

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| resetData | boolean | Yes | false | Reset the `pipelineData` object to being an empty object? |
| --- | --- | --- | --- | --- |

**Returns:** boolean - `true` if the pipeline was reset successfully, otherwise `false`.

**Inherits:** [Phaser.GameObjects.Components.Pipeline#resetPipeline](../namespace/gameobjects-components-pipeline.md)

> Source: [src/gameobjects/components/Pipeline.js#L176](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Pipeline.js#L176)  
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

## rotateX

### <instance> rotateX()

**Description:**

The x rotation of the Model in 3D space, as specified in degrees.

If you need the value in radians use the `modelRotation.x` property directly.

**Returns:** number - undefined

**Inherits:** [Phaser.GameObjects.Mesh#rotateX](gameobjects-mesh.md)

> Source: [src/gameobjects/mesh/Mesh.js#L1324](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/mesh/Mesh.js#L1324)  
> Since: 3.60.0

---

## rotateY

### <instance> rotateY()

**Description:**

The y rotation of the Model in 3D space, as specified in degrees.

If you need the value in radians use the `modelRotation.y` property directly.

**Returns:** number - undefined

**Inherits:** [Phaser.GameObjects.Mesh#rotateY](gameobjects-mesh.md)

> Source: [src/gameobjects/mesh/Mesh.js#L1347](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/mesh/Mesh.js#L1347)  
> Since: 3.60.0

---

## rotateZ

### <instance> rotateZ()

**Description:**

The z rotation of the Model in 3D space, as specified in degrees.

If you need the value in radians use the `modelRotation.z` property directly.

**Returns:** number - undefined

**Inherits:** [Phaser.GameObjects.Mesh#rotateZ](gameobjects-mesh.md)

> Source: [src/gameobjects/mesh/Mesh.js#L1370](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/mesh/Mesh.js#L1370)  
> Since: 3.60.0

---

## setAbove

### <instance> setAbove(gameObject)

**Description:**

Move this Game Object so that it appears above the given Game Object.

This means it will render immediately after the other object in the display list.

Both objects must belong to the same display list, or parent container.

This method does not change this Game Objects `depth` value, it simply alters its list position.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No | The Game Object that this Game Object will be moved to be above. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Plane](gameobjects-plane.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Depth#setAbove](../namespace/gameobjects-components-depth.md)

> Source: [src/gameobjects/components/Depth.js#L139](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Depth.js#L139)  
> Since: 3.85.0

---

## setActive

### <instance> setActive(value)

**Description:**

Sets the `active` property of this Game Object and returns this Game Object for further chaining.

A Game Object with its `active` property set to `true` will be updated by the Scenes UpdateList.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | boolean | No | True if this Game Object should be set as active, false if not. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Plane](gameobjects-plane.md) - This GameObject.

**Inherits:** [Phaser.GameObjects.GameObject#setActive](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L216](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L216)  
> Since: 3.0.0

---

## setAlpha

### <instance> setAlpha([value])

**Description:**

Set the Alpha level of this Game Object. The alpha controls the opacity of the Game Object as it renders.

Alpha values are provided as a float between 0, fully transparent, and 1, fully opaque.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| value | number | Yes | 1 | The alpha value applied across the whole Game Object. |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Plane](gameobjects-plane.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.AlphaSingle#setAlpha](../namespace/gameobjects-components-alphasingle.md)

> Source: [src/gameobjects/components/AlphaSingle.js#L48](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/AlphaSingle.js#L48)  
> Since: 3.0.0

---

## setAngle

### <instance> setAngle([degrees])

**Description:**

Sets the angle of this Game Object.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| degrees | number | Yes | 0 | The rotation of this Game Object, in degrees. |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Plane](gameobjects-plane.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Transform#setAngle](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L364](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L364)  
> Since: 3.0.0

---

## setBelow

### <instance> setBelow(gameObject)

**Description:**

Move this Game Object so that it appears below the given Game Object.

This means it will render immediately under the other object in the display list.

Both objects must belong to the same display list, or parent container.

This method does not change this Game Objects `depth` value, it simply alters its list position.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No | The Game Object that this Game Object will be moved to be below. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Plane](gameobjects-plane.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Depth#setBelow](../namespace/gameobjects-components-depth.md)

> Source: [src/gameobjects/components/Depth.js#L167](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Depth.js#L167)  
> Since: 3.85.0

---

## setBlendMode

### <instance> setBlendMode(value)

**Description:**

Sets the Blend Mode being used by this Game Object.

This can be a const, such as `Phaser.BlendModes.SCREEN`, or an integer, such as 4 (for Overlay)

Under WebGL only the following Blend Modes are available:

* NORMAL
* ADD
* MULTIPLY
* SCREEN
* ERASE (only works when rendering to a framebuffer, like a Render Texture)

Canvas has more available depending on browser support.

You can also create your own custom Blend Modes in WebGL.

Blend modes have different effects under Canvas and WebGL, and from browser to browser, depending

on support. Blend Modes also cause a WebGL batch flush should it encounter a new blend mode. For these

reasons try to be careful about the construction of your Scene and the frequency in which blend modes

are used.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | string | [Phaser.BlendModes](../namespace/blendmodes.md) | number | No |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Plane](gameobjects-plane.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.BlendMode#setBlendMode](../namespace/gameobjects-components-blendmode.md)

> Source: [src/gameobjects/components/BlendMode.js#L80](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/BlendMode.js#L80)  
> Since: 3.0.0

---

## setData

### <instance> setData(key, [data])

**Description:**

Allows you to store a key value pair within this Game Objects Data Manager.

If the Game Object has not been enabled for data (via `setDataEnabled`) then it will be enabled

before setting the value.

If the key doesn't already exist in the Data Manager then it is created.

```
Copy
sprite.setData('name', 'Red Gem Stone');


```

You can also pass in an object of key value pairs as the first argument:

```
Copy
sprite.setData({ name: 'Red Gem Stone', level: 2, owner: 'Link', gold: 50 });


```

To get a value back again you can call `getData`:

```
Copy
sprite.getData('gold');


```

Or you can access the value directly via the `values` property, where it works like any other variable:

```
Copy
sprite.data.values.gold += 50;


```

When the value is first set, a `setdata` event is emitted from this Game Object.

If the key already exists, a `changedata` event is emitted instead, along an event named after the key.

For example, if you updated an existing key called `PlayerLives` then it would emit the event `changedata-PlayerLives`.

These events will be emitted regardless if you use this method to set the value, or the direct `values` setter.

Please note that the data keys are case-sensitive and must be valid JavaScript Object property strings.

This means the keys `gold` and `Gold` are treated as two unique values within the Data Manager.

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | object | No | The key to set the value for. Or an object of key value pairs. If an object the `data` argument is ignored. |
| --- | --- | --- | --- |
| data | \* | Yes | The value to set for the given key. If an object is provided as the key this argument is ignored. |

**Returns:** [Phaser.GameObjects.Plane](gameobjects-plane.md) - This GameObject.

**Inherits:** [Phaser.GameObjects.GameObject#setData](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L295](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L295)  
> Since: 3.0.0

---

## setDataEnabled

### <instance> setDataEnabled()

**Description:**

Adds a Data Manager component to this Game Object.

**Returns:** [Phaser.GameObjects.Plane](gameobjects-plane.md) - This GameObject.

**Inherits:** [Phaser.GameObjects.GameObject#setDataEnabled](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L276](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L276)  
> Since: 3.0.0

---

## setDebug

### <instance> setDebug([graphic], [callback])

**Description:**

This method enables rendering of the Mesh vertices to the given Graphics instance.

If you enable this feature, you **must** call `Graphics.clear()` in your Scene `update`,

otherwise the Graphics instance you provide to debug will fill-up with draw calls,

eventually crashing the browser. This is not done automatically to allow you to debug

draw multiple Mesh objects to a single Graphics instance.

The Mesh class has a built-in debug rendering callback `Mesh.renderDebug`, however

you can also provide your own callback to be used instead. Do this by setting the `callback` parameter.

The callback is invoked *once per render* and sent the following parameters:

`callback(src, faces)`

`src` is the Mesh instance being debugged.

`faces` is an array of the Faces that were rendered.

You can get the final drawn vertex position from a Face object like this:

```
Copy
let face = faces[i];



let x0 = face.vertex1.tx;

let y0 = face.vertex1.ty;

let x1 = face.vertex2.tx;

let y1 = face.vertex2.ty;

let x2 = face.vertex3.tx;

let y2 = face.vertex3.ty;



graphic.strokeTriangle(x0, y0, x1, y1, x2, y2);


```

If using your own callback you do not have to provide a Graphics instance to this method.

To disable debug rendering, to either your own callback or the built-in one, call this method

with no arguments.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| graphic | [Phaser.GameObjects.Graphics](gameobjects-graphics.md) | Yes | The Graphic instance to render to if using the built-in callback. |
| --- | --- | --- | --- |
| callback | function | Yes | The callback to invoke during debug render. Leave as undefined to use the built-in callback. |

**Returns:** [Phaser.GameObjects.Plane](gameobjects-plane.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Mesh#setDebug](gameobjects-mesh.md)

> Source: [src/gameobjects/mesh/Mesh.js#L883](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/mesh/Mesh.js#L883)  
> Since: 3.50.0

---

## setDepth

### <instance> setDepth(value)

**Description:**

The depth of this Game Object within the Scene.

The depth is also known as the 'z-index' in some environments, and allows you to change the rendering order

of Game Objects, without actually moving their position in the display list.

The default depth is zero. A Game Object with a higher depth

value will always render in front of one with a lower value.

Setting the depth will queue a depth sort event within the Scene.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The depth of this Game Object. Ensure this value is only ever a number data-type. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Plane](gameobjects-plane.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Depth#setDepth](../namespace/gameobjects-components-depth.md)

> Source: [src/gameobjects/components/Depth.js#L64](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Depth.js#L64)  
> Since: 3.0.0

---

## setDisplaySize

### <instance> setDisplaySize(width, height)

**Description:**

Sets the display size of this Game Object.

Calling this will adjust the scale.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| width | number | No | The width of this Game Object. |
| --- | --- | --- | --- |
| height | number | No | The height of this Game Object. |

**Returns:** [Phaser.GameObjects.Plane](gameobjects-plane.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Size#setDisplaySize](../namespace/gameobjects-components-size.md)

> Source: [src/gameobjects/components/Size.js#L166](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Size.js#L166)  
> Since: 3.0.0

---

## setFrame

### <instance> setFrame(frame, [updateSize], [updateOrigin])

**Description:**

Sets the frame this Game Object will use to render with.

If you pass a string or index then the Frame has to belong to the current Texture being used

by this Game Object.

If you pass a Frame instance, then the Texture being used by this Game Object will also be updated.

Calling `setFrame` will modify the `width` and `height` properties of your Game Object.

It will also change the `origin` if the Frame has a custom pivot point, as exported from packages like Texture Packer.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| frame | string | number | [Phaser.Textures.Frame](textures-frame.md) | No |  |
| --- | --- | --- | --- | --- |
| updateSize | boolean | Yes | true | Should this call adjust the size of the Game Object? |
| updateOrigin | boolean | Yes | true | Should this call adjust the origin of the Game Object? |

**Returns:** [Phaser.GameObjects.Plane](gameobjects-plane.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Texture#setFrame](../namespace/gameobjects-components-texture.md)

> Source: [src/gameobjects/components/Texture.js#L75](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Texture.js#L75)  
> Since: 3.0.0

---

## setInteractive

### <instance> setInteractive([config])

**Description:**

Pass this Mesh Game Object to the Input Manager to enable it for Input.

Unlike other Game Objects, the Mesh Game Object uses its own special hit area callback, which you cannot override.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| config | [Phaser.Types.Input.InputConfiguration](../typedef/types-input.md) | Yes | An input configuration object but it will ignore hitArea, hitAreaCallback and pixelPerfect with associated alphaTolerance properties. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Plane](gameobjects-plane.md) - This GameObject.

**Inherits:** [Phaser.GameObjects.Mesh#setInteractive](gameobjects-mesh.md)

> Source: [src/gameobjects/mesh/Mesh.js#L1153](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/mesh/Mesh.js#L1153)  
> Since: 3.60.0

---

## setMask

### <instance> setMask(mask)

**Description:**

Sets the mask that this Game Object will use to render with.

The mask must have been previously created and can be either a GeometryMask or a BitmapMask.

Note: Bitmap Masks only work on WebGL. Geometry Masks work on both WebGL and Canvas.

If a mask is already set on this Game Object it will be immediately replaced.

Masks are positioned in global space and are not relative to the Game Object to which they

are applied. The reason for this is that multiple Game Objects can all share the same mask.

Masks have no impact on physics or input detection. They are purely a rendering component

that allows you to limit what is visible during the render pass.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| mask | [Phaser.Display.Masks.BitmapMask](display-masks-bitmapmask.md) | [Phaser.Display.Masks.GeometryMask](display-masks-geometrymask.md) | No | The mask this Game Object will use when rendering. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Plane](gameobjects-plane.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Mask#setMask](../namespace/gameobjects-components-mask.md)

> Source: [src/gameobjects/components/Mask.js#L28](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Mask.js#L28)  
> Since: 3.6.2

---

## setName

### <instance> setName(value)

**Description:**

Sets the `name` property of this Game Object and returns this Game Object for further chaining.

The `name` property is not populated by Phaser and is presented for your own use.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | string | No | The name to be given to this Game Object. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Plane](gameobjects-plane.md) - This GameObject.

**Inherits:** [Phaser.GameObjects.GameObject#setName](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L234](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L234)  
> Since: 3.0.0

---

## setOrtho

### <instance> setOrtho([scaleX], [scaleY], [near], [far])

**Description:**

Builds a new orthographic projection matrix from the given values.

If using this mode you will often need to set `Mesh.hideCCW` to `false` as well.

By default, calling this method with no parameters will set the scaleX value to

match the renderer's aspect ratio. If you would like to render vertex positions 1:1

to pixel positions, consider calling as `mesh.setOrtho(mesh.width, mesh.height)`.

See also `setPerspective`.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| scaleX | number | Yes | 1 | The default horizontal scale in relation to the Mesh / Renderer dimensions. |
| --- | --- | --- | --- | --- |
| scaleY | number | Yes | 1 | The default vertical scale in relation to the Mesh / Renderer dimensions. |
| near | number | Yes | -1000 | The near value of the view. |
| far | number | Yes | 1000 | The far value of the view. |

**Inherits:** [Phaser.GameObjects.Mesh#setOrtho](gameobjects-mesh.md)

> Source: [src/gameobjects/mesh/Mesh.js#L488](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/mesh/Mesh.js#L488)  
> Since: 3.50.0

---

## setPerspective

### <instance> setPerspective(width, height, [fov], [near], [far])

**Description:**

Builds a new perspective projection matrix from the given values.

These are also the initial projection matrix and parameters for `Mesh` (see `Mesh.panZ` for more discussion).

See also `setOrtho`.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| width | number | No |  | The width of the projection matrix. Typically the same as the Mesh and/or Renderer. |
| --- | --- | --- | --- | --- |
| height | number | No |  | The height of the projection matrix. Typically the same as the Mesh and/or Renderer. |
| fov | number | Yes | 45 | The field of view, in degrees. |
| near | number | Yes | 0.01 | The near value of the view. |
| far | number | Yes | 1000 | The far value of the view. |

**Inherits:** [Phaser.GameObjects.Mesh#setPerspective](gameobjects-mesh.md)

> Source: [src/gameobjects/mesh/Mesh.js#L456](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/mesh/Mesh.js#L456)  
> Since: 3.50.0

---

## setPipeline

### <instance> setPipeline(pipeline, [pipelineData], [copyData])

**Description:**

Sets the main WebGL Pipeline of this Game Object.

Also sets the `pipelineData` property, if the parameter is given.

**Tags:**

* webglOnly

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| pipeline | string | [Phaser.Renderer.WebGL.WebGLPipeline](renderer-webgl-webglpipeline.md) | No |  | Either the string-based name of the pipeline, or a pipeline instance to set. |
| --- | --- | --- | --- | --- |
| pipelineData | object | Yes |  | Optional pipeline data object that is set in to the `pipelineData` property of this Game Object. |
| copyData | boolean | Yes | true | Should the pipeline data object be *deep copied* into the `pipelineData` property of this Game Object? If `false` it will be set by reference instead. |

**Returns:** [Phaser.GameObjects.Plane](gameobjects-plane.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Pipeline#setPipeline](../namespace/gameobjects-components-pipeline.md)

> Source: [src/gameobjects/components/Pipeline.js#L100](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Pipeline.js#L100)  
> Since: 3.0.0

---

## setPipelineData

### <instance> setPipelineData(key, [value])

**Description:**

Adds an entry to the `pipelineData` object belonging to this Game Object.

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

**Returns:** [Phaser.GameObjects.Plane](gameobjects-plane.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Pipeline#setPipelineData](../namespace/gameobjects-components-pipeline.md)

> Source: [src/gameobjects/components/Pipeline.js#L144](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Pipeline.js#L144)  
> Since: 3.50.0

---

## setPosition

### <instance> setPosition([x], [y], [z], [w])

**Description:**

Sets the position of this Game Object.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | Yes | 0 | The x position of this Game Object. |
| --- | --- | --- | --- | --- |
| y | number | Yes | "x" | The y position of this Game Object. If not set it will use the `x` value. |
| z | number | Yes | 0 | The z position of this Game Object. |
| w | number | Yes | 0 | The w position of this Game Object. |

**Returns:** [Phaser.GameObjects.Plane](gameobjects-plane.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Transform#setPosition](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L265](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L265)  
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

**Returns:** [Phaser.GameObjects.Plane](gameobjects-plane.md) - This Game Object instance.

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

**Returns:** [Phaser.GameObjects.Plane](gameobjects-plane.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.PostPipeline#setPostPipelineData](../namespace/gameobjects-components-postpipeline.md)

> Source: [src/gameobjects/components/PostPipeline.js#L205](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/PostPipeline.js#L205)  
> Since: 3.60.0

---

## setRandomPosition

### <instance> setRandomPosition([x], [y], [width], [height])

**Description:**

Sets the position of this Game Object to be a random position within the confines of

the given area.

If no area is specified a random position between 0 x 0 and the game width x height is used instead.

The position does not factor in the size of this Game Object, meaning that only the origin is

guaranteed to be within the area.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | Yes | 0 | The x position of the top-left of the random area. |
| --- | --- | --- | --- | --- |
| y | number | Yes | 0 | The y position of the top-left of the random area. |
| width | number | Yes |  | The width of the random area. |
| height | number | Yes |  | The height of the random area. |

**Returns:** [Phaser.GameObjects.Plane](gameobjects-plane.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Transform#setRandomPosition](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L313](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L313)  
> Since: 3.8.0

---

## setRotation

### <instance> setRotation([radians])

**Description:**

Sets the rotation of this Game Object.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| radians | number | Yes | 0 | The rotation of this Game Object, in radians. |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Plane](gameobjects-plane.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Transform#setRotation](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L345](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L345)  
> Since: 3.0.0

---

## setScale

### <instance> setScale([x], [y])

**Description:**

Sets the scale of this Game Object.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | Yes | 1 | The horizontal scale of this Game Object. |
| --- | --- | --- | --- | --- |
| y | number | Yes | "x" | The vertical scale of this Game Object. If not set it will use the `x` value. |

**Returns:** [Phaser.GameObjects.Plane](gameobjects-plane.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Transform#setScale](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L383](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L383)  
> Since: 3.0.0

---

## setScrollFactor

### <instance> setScrollFactor(x, [y])

**Description:**

Sets the scroll factor of this Game Object.

The scroll factor controls the influence of the movement of a Camera upon this Game Object.

When a camera scrolls it will change the location at which this Game Object is rendered on-screen.

It does not change the Game Objects actual position values.

A value of 1 means it will move exactly in sync with a camera.

A value of 0 means it will not move at all, even if the camera moves.

Other values control the degree to which the camera movement is mapped to this Game Object.

Please be aware that scroll factor values other than 1 are not taken in to consideration when

calculating physics collisions. Bodies always collide based on their world position, but changing

the scroll factor is a visual adjustment to where the textures are rendered, which can offset

them from physics bodies if not accounted for in your code.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | No |  | The horizontal scroll factor of this Game Object. |
| --- | --- | --- | --- | --- |
| y | number | Yes | "x" | The vertical scroll factor of this Game Object. If not set it will use the `x` value. |

**Returns:** [Phaser.GameObjects.Plane](gameobjects-plane.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.ScrollFactor#setScrollFactor](../namespace/gameobjects-components-scrollfactor.md)

> Source: [src/gameobjects/components/ScrollFactor.js#L64](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/ScrollFactor.js#L64)  
> Since: 3.0.0

---

## setSize

### <instance> setSize(width, height)

**Description:**

Sets the internal size of this Game Object, as used for frame or physics body creation.

This will not change the size that the Game Object is rendered in-game.

For that you need to either set the scale of the Game Object (`setScale`) or call the

`setDisplaySize` method, which is the same thing as changing the scale but allows you

to do so by giving pixel values.

If you have enabled this Game Object for input, changing the size will *not* change the

size of the hit area. To do this you should adjust the `input.hitArea` object directly.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| width | number | No | The width of this Game Object. |
| --- | --- | --- | --- |
| height | number | No | The height of this Game Object. |

**Returns:** [Phaser.GameObjects.Plane](gameobjects-plane.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Size#setSize](../namespace/gameobjects-components-size.md)

> Source: [src/gameobjects/components/Size.js#L139](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Size.js#L139)  
> Since: 3.0.0

---

## setSizeToFrame

### <instance> setSizeToFrame([resetUV])

**Description:**

An internal method that resets the perspective projection for this Plane

when it changes texture or frame, and also resets the cell UV coordinates,

if required.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| resetUV | boolean | Yes | true | Reset all of the cell UV coordinates? |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Plane](gameobjects-plane.md) - This Game Object instance.

> Source: [src/gameobjects/plane/Plane.js#L227](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/plane/Plane.js#L227)  
> Since: 3.60.0

---

## setSizeToFrame

### <instance> setSizeToFrame([resetUV])

**Description:**

An internal method that resets the perspective projection for this Plane

when it changes texture or frame, and also resets the cell UV coordinates,

if required.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| resetUV | boolean | Yes | true | Reset all of the cell UV coordinates? |
| --- | --- | --- | --- | --- |

**Overrides:** Phaser.GameObjects.Mesh#setSizeToFrame

**Returns:** [Phaser.GameObjects.Plane](gameobjects-plane.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Size#setSizeToFrame](../namespace/gameobjects-components-size.md)

> Source: [src/gameobjects/plane/Plane.js#L227](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/plane/Plane.js#L227)  
> Since: 3.60.0

---

## setState

### <instance> setState(value)

**Description:**

Sets the current state of this Game Object.

Phaser itself will never modify the State of a Game Object, although plugins may do so.

For example, a Game Object could change from a state of 'moving', to 'attacking', to 'dead'.

The state value should typically be an integer (ideally mapped to a constant

in your game code), but could also be a string. It is recommended to keep it light and simple.

If you need to store complex data about your Game Object, look at using the Data Component instead.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | string | No | The state of the Game Object. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Plane](gameobjects-plane.md) - This GameObject.

**Inherits:** [Phaser.GameObjects.GameObject#setState](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L252](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L252)  
> Since: 3.16.0

---

## setTexture

### <instance> setTexture(key, [frame], [updateSize], [updateOrigin])

**Description:**

Sets the texture and frame this Game Object will use to render with.

Textures are referenced by their string-based keys, as stored in the Texture Manager.

Calling this method will modify the `width` and `height` properties of your Game Object.

It will also change the `origin` if the Frame has a custom pivot point, as exported from packages like Texture Packer.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | string | [Phaser.Textures.Texture](textures-texture.md) | No |  | The key of the texture to be used, as stored in the Texture Manager, or a Texture instance. |
| --- | --- | --- | --- | --- |
| frame | string | number | Yes |  | The name or index of the frame within the Texture. |
| updateSize | boolean | Yes | true | Should this call adjust the size of the Game Object? |
| updateOrigin | boolean | Yes | true | Should this call change the origin of the Game Object? |

**Returns:** [Phaser.GameObjects.Plane](gameobjects-plane.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Texture#setTexture](../namespace/gameobjects-components-texture.md)

> Source: [src/gameobjects/components/Texture.js#L49](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Texture.js#L49)  
> Since: 3.0.0

---

## setTint

### <instance> setTint([tint])

**Description:**

Sets an additive tint on all vertices of this Mesh Game Object.

The tint works by taking the pixel color values from the Game Objects texture, and then

multiplying it by the color value of the tint.

To modify the tint color once set, either call this method again with new values or use the

`tint` property to set all colors at once.

To remove a tint call `clearTint`.

**Tags:**

* webglOnly

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| tint | number | Yes | "0xffffff" | The tint being applied to all vertices of this Mesh Game Object. |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Plane](gameobjects-plane.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Mesh#setTint](gameobjects-mesh.md)

> Source: [src/gameobjects/mesh/Mesh.js#L1198](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/mesh/Mesh.js#L1198)  
> Since: 3.60.0

---

## setToBack

### <instance> setToBack()

**Description:**

Sets this Game Object to the back of the display list, or the back of its parent container.

Being at the back means it will render below everything else.

This method does not change this Game Objects `depth` value, it simply alters its list position.

**Returns:** [Phaser.GameObjects.Plane](gameobjects-plane.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Depth#setToBack](../namespace/gameobjects-components-depth.md)

> Source: [src/gameobjects/components/Depth.js#L115](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Depth.js#L115)  
> Since: 3.85.0

---

## setToTop

### <instance> setToTop()

**Description:**

Sets this Game Object to be at the top of the display list, or the top of its parent container.

Being at the top means it will render on-top of everything else.

This method does not change this Game Objects `depth` value, it simply alters its list position.

**Returns:** [Phaser.GameObjects.Plane](gameobjects-plane.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Depth#setToTop](../namespace/gameobjects-components-depth.md)

> Source: [src/gameobjects/components/Depth.js#L91](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Depth.js#L91)  
> Since: 3.85.0

---

## setViewHeight

### <instance> setViewHeight([value])

**Description:**

Sets the height of this Plane to match the given value, in pixels.

This adjusts the `Plane.viewPosition.z` value to achieve this.

If no `value` parameter is given, it will set the view height to match

that of the current texture frame the Plane is using.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | Yes | The height, in pixels, to set this Plane view height to. |
| --- | --- | --- | --- |

> Source: [src/gameobjects/plane/Plane.js#L336](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/plane/Plane.js#L336)  
> Since: 3.60.0

---

## setVisible

### <instance> setVisible(value)

**Description:**

Sets the visibility of this Game Object.

An invisible Game Object will skip rendering, but will still process update logic.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | boolean | No | The visible state of the Game Object. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Plane](gameobjects-plane.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Visible#setVisible](../namespace/gameobjects-components-visible.md)

> Source: [src/gameobjects/components/Visible.js#L63](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Visible.js#L63)  
> Since: 3.0.0

---

## setW

### <instance> setW([value])

**Description:**

Sets the w position of this Game Object.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| value | number | Yes | 0 | The w position of this Game Object. |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Plane](gameobjects-plane.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Transform#setW](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L465](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L465)  
> Since: 3.0.0

---

## setX

### <instance> setX([value])

**Description:**

Sets the x position of this Game Object.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| value | number | Yes | 0 | The x position of this Game Object. |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Plane](gameobjects-plane.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Transform#setX](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L405](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L405)  
> Since: 3.0.0

---

## setY

### <instance> setY([value])

**Description:**

Sets the y position of this Game Object.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| value | number | Yes | 0 | The y position of this Game Object. |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Plane](gameobjects-plane.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Transform#setY](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L424](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L424)  
> Since: 3.0.0

---

## setZ

### <instance> setZ([value])

**Description:**

Sets the z position of this Game Object.

Note: The z position does not control the rendering order of 2D Game Objects. Use

[Phaser.GameObjects.Components.Depth#setDepth](../namespace/gameobjects-components-depth.md) instead.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| value | number | Yes | 0 | The z position of this Game Object. |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Plane](gameobjects-plane.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Transform#setZ](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L443](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L443)  
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

## sortByDepth

### <instance> sortByDepth(faceA, faceB)

**Description:**

Compare the depth of two Faces.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| faceA | [Phaser.Geom.Mesh.Face](geom-mesh-face.md) | No | The first Face. |
| --- | --- | --- | --- |
| faceB | [Phaser.Geom.Mesh.Face](geom-mesh-face.md) | No | The second Face. |

**Returns:** number - The difference between the depths of each Face.

**Inherits:** [Phaser.GameObjects.Mesh#sortByDepth](gameobjects-mesh.md)

> Source: [src/gameobjects/mesh/Mesh.js#L598](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/mesh/Mesh.js#L598)  
> Since: 3.50.0

---

## stop

### <instance> stop()

**Description:**

Immediately stops the current animation from playing and dispatches the `ANIMATION_STOP` events.

If no animation is playing, no event will be dispatched.

If there is another animation queued (via the `chain` method) then it will start playing immediately.

**Returns:** [Phaser.GameObjects.Plane](gameobjects-plane.md) - This Game Object.

**Fires:** [Phaser.Animations.Events#event:ANIMATION\_STOP](../event/animations-events.md)

> Source: [src/gameobjects/plane/Plane.js#L630](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/plane/Plane.js#L630)  
> Since: 3.60.0

---

## stopAfterDelay

### <instance> stopAfterDelay(delay)

**Description:**

Stops the current animation from playing after the specified time delay, given in milliseconds.

It then dispatches the `ANIMATION_STOP` event.

If no animation is running, no events will be dispatched.

If there is another animation in the queue (set via the `chain` method) then it will start playing,

when the current one stops.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| delay | number | No | The number of milliseconds to wait before stopping this animation. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Plane](gameobjects-plane.md) - This Game Object.

**Fires:** [Phaser.Animations.Events#event:ANIMATION\_STOP](../event/animations-events.md)

> Source: [src/gameobjects/plane/Plane.js#L648](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/plane/Plane.js#L648)  
> Since: 3.60.0

---

## stopAfterRepeat

### <instance> stopAfterRepeat([repeatCount])

**Description:**

Stops the current animation from playing after the given number of repeats.

It then dispatches the `ANIMATION_STOP` event.

If no animation is running, no events will be dispatched.

If there is another animation in the queue (set via the `chain` method) then it will start playing,

when the current one stops.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| repeatCount | number | Yes | 1 | How many times should the animation repeat before stopping? |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Plane](gameobjects-plane.md) - This Game Object.

**Fires:** [Phaser.Animations.Events#event:ANIMATION\_STOP](../event/animations-events.md)

> Source: [src/gameobjects/plane/Plane.js#L671](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/plane/Plane.js#L671)  
> Since: 3.60.0

---

## stopOnFrame

### <instance> stopOnFrame(frame)

**Description:**

Stops the current animation from playing when it next sets the given frame.

If this frame doesn't exist within the animation it will not stop it from playing.

It then dispatches the `ANIMATION_STOP` event.

If no animation is running, no events will be dispatched.

If there is another animation in the queue (set via the `chain` method) then it will start playing,

when the current one stops.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| frame | [Phaser.Animations.AnimationFrame](animations-animationframe.md) | No | The frame to check before stopping this animation. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Plane](gameobjects-plane.md) - This Game Object.

**Fires:** [Phaser.Animations.Events#event:ANIMATION\_STOP](../event/animations-events.md)

> Source: [src/gameobjects/plane/Plane.js#L694](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/plane/Plane.js#L694)  
> Since: 3.60.0

---

## tint

### <instance> tint()

**Description:**

The tint value being applied to the whole of the Game Object.

This property is a setter-only.

**Tags:**

* webglOnly

**Returns:** number - undefined

**Inherits:** [Phaser.GameObjects.Mesh#tint](gameobjects-mesh.md)

> Source: [src/gameobjects/mesh/Mesh.js#L1307](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/mesh/Mesh.js#L1307)  
> Since: 3.60.0

---

## toggleData

### <instance> toggleData(key)

**Description:**

Toggle a boolean value for the given key within this Game Objects Data Manager. If the key doesn't already exist in the Data Manager then it is toggled from false.

If the Game Object has not been enabled for data (via `setDataEnabled`) then it will be enabled

before setting the value.

If the key doesn't already exist in the Data Manager then it is created.

When the value is first set, a `setdata` event is emitted from this Game Object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The key to toggle the value for. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Plane](gameobjects-plane.md) - This GameObject.

**Inherits:** [Phaser.GameObjects.GameObject#toggleData](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L387](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L387)  
> Since: 3.23.0

---

## toJSON

### <instance> toJSON()

**Description:**

Returns a JSON representation of the Game Object.

**Returns:** [Phaser.Types.GameObjects.JSONGameObject](../typedef/types-gameobjects.md) - A JSON representation of the Game Object.

**Inherits:** [Phaser.GameObjects.GameObject#toJSON](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L604](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L604)  
> Since: 3.0.0

---

## update

### <instance> update([args])

**Description:**

To be overridden by custom GameObjects. Allows base objects to be used in a Pool.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| args | \* | Yes | args |
| --- | --- | --- | --- |

**Inherits:** [Phaser.GameObjects.GameObject#update](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L592](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L592)  
> Since: 3.0.0

---

## uvScale

### <instance> uvScale(x, y)

**Description:**

Scales the UV texture coordinates of all faces in this Mesh by

the exact given amounts.

If you only wish to scale one coordinate, pass a value of one

to the other.

Due to a limitation in WebGL1 you can only UV scale textures

that are a power-of-two in size. Scaling NPOT textures will

work but will result in clamping the pixels to the edges if

you scale beyond a value of 1. Scaling below 1 will work

regardless of texture size.

Note that if this Mesh is using a *frame* from a texture atlas

then you will be unable to UV scale its texture.

**Tags:**

* webglOnly

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The amount to horizontally scale the UV coordinates by. |
| --- | --- | --- | --- |
| y | number | No | The amount to vertically scale the UV coordinates by. |

**Returns:** [Phaser.GameObjects.Plane](gameobjects-plane.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Mesh#uvScale](gameobjects-mesh.md)

> Source: [src/gameobjects/mesh/Mesh.js#L1270](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/mesh/Mesh.js#L1270)  
> Since: 3.60.0

---

## uvScroll

### <instance> uvScroll(x, y)

**Description:**

Scrolls the UV texture coordinates of all faces in this Mesh by

adding the given x/y amounts to them.

If you only wish to scroll one coordinate, pass a value of zero

to the other.

Use small values for scrolling. UVs are set from the range 0

to 1, so you should increment (or decrement) them by suitably

small values, such as 0.01.

Due to a limitation in WebGL1 you can only UV scroll textures

that are a power-of-two in size. Scrolling NPOT textures will

work but will result in clamping the pixels to the edges.

Note that if this Mesh is using a *frame* from a texture atlas

then you will be unable to UV scroll its texture.

**Tags:**

* webglOnly

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The amount to horizontally shift the UV coordinates by. |
| --- | --- | --- | --- |
| y | number | No | The amount to vertically shift the UV coordinates by. |

**Returns:** [Phaser.GameObjects.Plane](gameobjects-plane.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Mesh#uvScroll](gameobjects-mesh.md)

> Source: [src/gameobjects/mesh/Mesh.js#L1231](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/mesh/Mesh.js#L1231)  
> Since: 3.60.0

---

## willRender

### <instance> willRender(camera)

**Description:**

Compares the renderMask with the renderFlags to see if this Game Object will render or not.

Also checks the Game Object against the given Cameras exclusion list.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | No | The Camera to check against this Game Object. |
| --- | --- | --- | --- |

**Returns:** boolean - True if the Game Object should be rendered, otherwise false.

**Inherits:** [Phaser.GameObjects.GameObject#willRender](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L617](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L617)  
> Since: 3.0.0

---

# Private Methods

## preDestroy

### <instance> preDestroy()

**Description:**

Handles the pre-destroy step for the Plane, which removes the vertices and debug callbacks.

**Access:** private

**Overrides:** Phaser.GameObjects.Mesh#preDestroy

> Source: [src/gameobjects/plane/Plane.js#L736](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/plane/Plane.js#L736)  
> Since: 3.60.0

---

## renderCanvas

### <instance> renderCanvas(renderer, src, camera)

**Description:**

This is a stub function for Mesh.Render. There is no Canvas renderer for Mesh objects.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| renderer | [Phaser.Renderer.Canvas.CanvasRenderer](renderer-canvas-canvasrenderer.md) | No | A reference to the current active Canvas renderer. |
| --- | --- | --- | --- |
| src | [Phaser.GameObjects.Mesh](gameobjects-mesh.md) | No | The Game Object being rendered in this call. |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | No | The Camera that is rendering the Game Object. |

**Inherits:** [Phaser.GameObjects.Mesh#renderCanvas](gameobjects-mesh.md)

> Source: [src/gameobjects/mesh/MeshCanvasRenderer.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/mesh/MeshCanvasRenderer.js#L7)  
> Since: 3.0.0

---

## renderWebGL

### <instance> renderWebGL(renderer, src, camera, parentMatrix)

**Description:**

Renders this Game Object with the WebGL Renderer to the given Camera.

The object will not render if any of its renderFlags are set or it is being actively filtered out by the Camera.

This method should not be called directly. It is a utility function of the Render module.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| renderer | [Phaser.Renderer.WebGL.WebGLRenderer](renderer-webgl-webglrenderer.md) | No | A reference to the current active WebGL renderer. |
| --- | --- | --- | --- |
| src | [Phaser.GameObjects.Mesh](gameobjects-mesh.md) | No | The Game Object being rendered in this call. |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | No | The Camera that is rendering the Game Object. |
| parentMatrix | [Phaser.GameObjects.Components.TransformMatrix](gameobjects-components-transformmatrix.md) | No | This transform matrix is defined if the game object is nested |

**Overrides:** Phaser.GameObjects.Mesh#renderWebGL

**Inherits:** [Phaser.GameObjects.Mesh#renderWebGL](gameobjects-mesh.md)

> Source: [src/gameobjects/mesh/MeshWebGLRenderer.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/mesh/MeshWebGLRenderer.js#L9)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [active](#active)

    - [active: boolean](#active-boolean)
  + [alpha](#alpha)

    - [alpha: number](#alpha-number)
  + [angle](#angle)

    - [angle: number](#angle-number)
  + [anims](#anims)

    - [anims: Phaser.Animations.AnimationState](#anims-phaseranimationsanimationstate)
  + [blendMode](#blendmode)

    - [blendMode: Phaser.BlendModes, string, number](#blendmode-phaserblendmodes-string-number)
  + [body](#body)

    - [body: Phaser.Physics.Arcade.Body, Phaser.Physics.Arcade.StaticBody, MatterJS.BodyType](#body-phaserphysicsarcadebody-phaserphysicsarcadestaticbody-matterjsbodytype)
  + [cameraFilter](#camerafilter)

    - [cameraFilter: number](#camerafilter-number)
  + [data](#data)

    - [data: Phaser.Data.DataManager](#data-phaserdatadatamanager)
  + [debugCallback](#debugcallback)

    - [debugCallback: function](#debugcallback-function)
  + [debugGraphic](#debuggraphic)

    - [debugGraphic: Phaser.GameObjects.Graphics](#debuggraphic-phasergameobjectsgraphics)
  + [defaultPipeline](#defaultpipeline)

    - [defaultPipeline: Phaser.Renderer.WebGL.WebGLPipeline](#defaultpipeline-phaserrendererwebglwebglpipeline)
  + [depth](#depth)

    - [depth: number](#depth-number)
  + [displayHeight](#displayheight)

    - [displayHeight: number](#displayheight-number)
  + [displayList](#displaylist)

    - [displayList: Phaser.GameObjects.DisplayList, Phaser.GameObjects.Layer](#displaylist-phasergameobjectsdisplaylist-phasergameobjectslayer)
  + [displayWidth](#displaywidth)

    - [displayWidth: number](#displaywidth-number)
  + [faces](#faces)

    - [faces: Array.<Phaser.Geom.Mesh.Face>](#faces-arrayphasergeommeshface)
  + [fov](#fov)

    - [fov: number](#fov-number)
  + [frame](#frame)

    - [frame: Phaser.Textures.Frame](#frame-phasertexturesframe)
  + [gridHeight](#gridheight)

    - [gridHeight: number](#gridheight-number)
  + [gridWidth](#gridwidth)

    - [gridWidth: number](#gridwidth-number)
  + [hasPostPipeline](#haspostpipeline)

    - [hasPostPipeline: boolean](#haspostpipeline-boolean)
  + [hasTransformComponent](#hastransformcomponent)

    - [hasTransformComponent: boolean](#hastransformcomponent-boolean)
  + [height](#height)

    - [height: number](#height-number)
  + [hideCCW](#hideccw)

    - [hideCCW: boolean](#hideccw-boolean)
  + [ignoreDestroy](#ignoredestroy)

    - [ignoreDestroy: boolean](#ignoredestroy-boolean)
  + [ignoreDirtyCache](#ignoredirtycache)

    - [ignoreDirtyCache: boolean](#ignoredirtycache-boolean)
  + [input](#input)

    - [input: Phaser.Types.Input.InteractiveObject](#input-phasertypesinputinteractiveobject)
  + [isTiled](#istiled)

    - [isTiled: boolean](#istiled-boolean)
  + [mask](#mask)

    - [mask: Phaser.Display.Masks.BitmapMask, Phaser.Display.Masks.GeometryMask](#mask-phaserdisplaymasksbitmapmask-phaserdisplaymasksgeometrymask)
  + [modelPosition](#modelposition)

    - [modelPosition: Phaser.Math.Vector3](#modelposition-phasermathvector3)
  + [modelRotation](#modelrotation)

    - [modelRotation: Phaser.Math.Vector3](#modelrotation-phasermathvector3)
  + [modelScale](#modelscale)

    - [modelScale: Phaser.Math.Vector3](#modelscale-phasermathvector3)
  + [name](#name)

    - [name: string](#name-string)
  + [originX](#originx)

    - [originX: number](#originx-number)
  + [originY](#originy)

    - [originY: number](#originy-number)
  + [parentContainer](#parentcontainer)

    - [parentContainer: Phaser.GameObjects.Container](#parentcontainer-phasergameobjectscontainer)
  + [pipeline](#pipeline)

    - [pipeline: Phaser.Renderer.WebGL.WebGLPipeline](#pipeline-phaserrendererwebglwebglpipeline)
  + [pipelineData](#pipelinedata)

    - [pipelineData: object](#pipelinedata-object)
  + [postFX](#postfx)

    - [postFX: Phaser.GameObjects.Components.FX](#postfx-phasergameobjectscomponentsfx)
  + [postPipelineData](#postpipelinedata)

    - [postPipelineData: object](#postpipelinedata-object)
  + [postPipelines](#postpipelines)

    - [postPipelines: Array.<Phaser.Renderer.WebGL.Pipelines.PostFXPipeline>](#postpipelines-arrayphaserrendererwebglpipelinespostfxpipeline)
  + [preFX](#prefx)

    - [preFX: Phaser.GameObjects.Components.FX](#prefx-phasergameobjectscomponentsfx)
  + [projectionMatrix](#projectionmatrix)

    - [projectionMatrix: Phaser.Math.Matrix4](#projectionmatrix-phasermathmatrix4)
  + [renderFlags](#renderflags)

    - [renderFlags: number](#renderflags-number)
  + [rotation](#rotation)

    - [rotation: number](#rotation-number)
  + [scale](#scale)

    - [scale: number](#scale-number)
  + [scaleX](#scalex)

    - [scaleX: number](#scalex-number)
  + [scaleY](#scaley)

    - [scaleY: number](#scaley-number)
  + [scene](#scene)

    - [scene: Phaser.Scene](#scene-phaserscene)
  + [scrollFactorX](#scrollfactorx)

    - [scrollFactorX: number](#scrollfactorx-number)
  + [scrollFactorY](#scrollfactory)

    - [scrollFactorY: number](#scrollfactory-number)
  + [state](#state)

    - [state: number, string](#state-number-string)
  + [tabIndex](#tabindex)

    - [tabIndex: number](#tabindex-number)
  + [texture](#texture)

    - [texture: Phaser.Textures.Texture, Phaser.Textures.CanvasTexture](#texture-phasertexturestexture-phasertexturescanvastexture)
  + [tintFill](#tintfill)

    - [tintFill: boolean](#tintfill-boolean)
  + [totalRendered](#totalrendered)

    - [totalRendered: number](#totalrendered-number)
  + [transformMatrix](#transformmatrix)

    - [transformMatrix: Phaser.Math.Matrix4](#transformmatrix-phasermathmatrix4)
  + [type](#type)

    - [type: string](#type-string)
  + [vertices](#vertices)

    - [vertices: Array.<Phaser.Geom.Mesh.Vertex>](#vertices-arrayphasergeommeshvertex)
  + [viewMatrix](#viewmatrix)

    - [viewMatrix: Phaser.Math.Matrix4](#viewmatrix-phasermathmatrix4)
  + [viewPosition](#viewposition)

    - [viewPosition: Phaser.Math.Vector3](#viewposition-phasermathvector3)
  + [visible](#visible)

    - [visible: boolean](#visible-boolean)
  + [w](#w)

    - [w: number](#w-number)
  + [width](#width)

    - [width: number](#width-number)
  + [x](#x)

    - [x: number](#x-number)
  + [y](#y)

    - [y: number](#y-number)
  + [z](#z)

    - [z: number](#z-number)
* [Private Members](#private-members)

  + [\_alpha](#_alpha)

    - [\_alpha: number](#_alpha-number)
  + [\_blendMode](#_blendmode)

    - [\_blendMode: number](#_blendmode-number)
  + [\_checkerboard](#_checkerboard)

    - [\_checkerboard: WebGLTexture](#_checkerboard-webgltexture)
  + [\_depth](#_depth)

    - [\_depth: number](#_depth-number)
  + [\_rotation](#_rotation)

    - [\_rotation: number](#_rotation-number)
  + [\_scaleX](#_scalex)

    - [\_scaleX: number](#_scalex-number)
  + [\_scaleY](#_scaley)

    - [\_scaleY: number](#_scaley-number)
  + [\_sizeComponent](#_sizecomponent)

    - [\_sizeComponent: boolean](#_sizecomponent-boolean)
  + [\_visible](#_visible)

    - [\_visible: boolean](#_visible-boolean)
  + [dirtyCache](#dirtycache)

    - [dirtyCache: Array.<number>](#dirtycache-arraynumber)
  + [isCropped](#iscropped)

    - [isCropped: boolean](#iscropped-boolean)
  + [totalFrame](#totalframe)

    - [totalFrame: number](#totalframe-number)
* [Public Methods](#public-methods)

  + [addedToScene](#addedtoscene)

    - [<instance> addedToScene()](#instance-addedtoscene)
  + [addFace](#addface)

    - [<instance> addFace(vertex1, vertex2, vertex3)](#instance-addfacevertex1-vertex2-vertex3)
  + [addListener](#addlistener)

    - [<instance> addListener(event, fn, [context])](#instance-addlistenerevent-fn-context)
  + [addToDisplayList](#addtodisplaylist)

    - [<instance> addToDisplayList([displayList])](#instance-addtodisplaylistdisplaylist)
  + [addToUpdateList](#addtoupdatelist)

    - [<instance> addToUpdateList()](#instance-addtoupdatelist)
  + [addVertex](#addvertex)

    - [<instance> addVertex(x, y, z, u, v, [color], [alpha])](#instance-addvertexx-y-z-u-v-color-alpha)
  + [addVertices](#addvertices)

    - [<instance> addVertices(vertices, uvs, [indicies], [containsZ], [normals], [colors], [alphas])](#instance-addverticesvertices-uvs-indicies-containsz-normals-colors-alphas)
  + [addVerticesFromObj](#addverticesfromobj)

    - [<instance> addVerticesFromObj(key, [scale], [x], [y], [z], [rotateX], [rotateY], [rotateZ], [zIsUp])](#instance-addverticesfromobjkey-scale-x-y-z-rotatex-rotatey-rotatez-zisup)
  + [clear](#clear)

    - [<instance> clear()](#instance-clear)
  + [clearAlpha](#clearalpha)

    - [<instance> clearAlpha()](#instance-clearalpha)
  + [clearFX](#clearfx)

    - [<instance> clearFX()](#instance-clearfx)
  + [clearMask](#clearmask)

    - [<instance> clearMask([destroyMask])](#instance-clearmaskdestroymask)
  + [clearTint](#cleartint)

    - [<instance> clearTint()](#instance-cleartint)
  + [copyPosition](#copyposition)

    - [<instance> copyPosition(source)](#instance-copypositionsource)
  + [createBitmapMask](#createbitmapmask)

    - [<instance> createBitmapMask([maskObject], [x], [y], [texture], [frame])](#instance-createbitmapmaskmaskobject-x-y-texture-frame)
  + [createCheckerboard](#createcheckerboard)

    - [<instance> createCheckerboard([color1], [color2], [alpha1], [alpha2], [height])](#instance-createcheckerboardcolor1-color2-alpha1-alpha2-height)
  + [createGeometryMask](#creategeometrymask)

    - [<instance> createGeometryMask([graphics])](#instance-creategeometrymaskgraphics)
  + [depthSort](#depthsort)

    - [<instance> depthSort()](#instance-depthsort)
  + [destroy](#destroy)

    - [<instance> destroy([fromScene])](#instance-destroyfromscene)
  + [disableInteractive](#disableinteractive)

    - [<instance> disableInteractive([resetCursor])](#instance-disableinteractiveresetcursor)
  + [emit](#emit)

    - [<instance> emit(event, [args])](#instance-emitevent-args)
  + [eventNames](#eventnames)

    - [<instance> eventNames()](#instance-eventnames)
  + [getData](#getdata)

    - [<instance> getData(key)](#instance-getdatakey)
  + [getDisplayList](#getdisplaylist)

    - [<instance> getDisplayList()](#instance-getdisplaylist)
  + [getFace](#getface)

    - [<instance> getFace(index)](#instance-getfaceindex)
  + [getFaceAt](#getfaceat)

    - [<instance> getFaceAt(x, y, [camera])](#instance-getfaceatx-y-camera)
  + [getFaceCount](#getfacecount)

    - [<instance> getFaceCount()](#instance-getfacecount)
  + [getIndexList](#getindexlist)

    - [<instance> getIndexList()](#instance-getindexlist)
  + [getLocalPoint](#getlocalpoint)

    - [<instance> getLocalPoint(x, y, [point], [camera])](#instance-getlocalpointx-y-point-camera)
  + [getLocalTransformMatrix](#getlocaltransformmatrix)

    - [<instance> getLocalTransformMatrix([tempMatrix])](#instance-getlocaltransformmatrixtempmatrix)
  + [getParentRotation](#getparentrotation)

    - [<instance> getParentRotation()](#instance-getparentrotation)
  + [getPipelineName](#getpipelinename)

    - [<instance> getPipelineName()](#instance-getpipelinename)
  + [getPostPipeline](#getpostpipeline)

    - [<instance> getPostPipeline(pipeline)](#instance-getpostpipelinepipeline)
  + [getVertexCount](#getvertexcount)

    - [<instance> getVertexCount()](#instance-getvertexcount)
  + [getWorldTransformMatrix](#getworldtransformmatrix)

    - [<instance> getWorldTransformMatrix([tempMatrix], [parentMatrix])](#instance-getworldtransformmatrixtempmatrix-parentmatrix)
  + [hasFaceAt](#hasfaceat)

    - [<instance> hasFaceAt(x, y, [camera])](#instance-hasfaceatx-y-camera)
  + [incData](#incdata)

    - [<instance> incData(key, [amount])](#instance-incdatakey-amount)
  + [initPipeline](#initpipeline)

    - [<instance> initPipeline([pipeline])](#instance-initpipelinepipeline)
  + [initPostPipeline](#initpostpipeline)

    - [<instance> initPostPipeline([preFX])](#instance-initpostpipelineprefx)
  + [isDirty](#isdirty)

    - [<instance> isDirty()](#instance-isdirty)
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
  + [panX](#panx)

    - [<instance> panX(v)](#instance-panxv)
  + [panY](#pany)

    - [<instance> panY(v)](#instance-panyv)
  + [panZ](#panz)

    - [<instance> panZ(v)](#instance-panzv)
  + [play](#play)

    - [<instance> play(key, [ignoreIfPlaying])](#instance-playkey-ignoreifplaying)
  + [playAfterDelay](#playafterdelay)

    - [<instance> playAfterDelay(key, delay)](#instance-playafterdelaykey-delay)
  + [playAfterRepeat](#playafterrepeat)

    - [<instance> playAfterRepeat(key, [repeatCount])](#instance-playafterrepeatkey-repeatcount)
  + [playReverse](#playreverse)

    - [<instance> playReverse(key, [ignoreIfPlaying])](#instance-playreversekey-ignoreifplaying)
  + [preDestroy](#predestroy)

    - [<instance> preDestroy([width], [height], [tile])](#instance-predestroywidth-height-tile)
  + [preUpdate](#preupdate)

    - [<instance> preUpdate(time, delta)](#instance-preupdatetime-delta)
  + [removeAllListeners](#removealllisteners)

    - [<instance> removeAllListeners([event])](#instance-removealllistenersevent)
  + [removeCheckerboard](#removecheckerboard)

    - [<instance> removeCheckerboard()](#instance-removecheckerboard)
  + [removedFromScene](#removedfromscene)

    - [<instance> removedFromScene()](#instance-removedfromscene)
  + [removeFromDisplayList](#removefromdisplaylist)

    - [<instance> removeFromDisplayList()](#instance-removefromdisplaylist)
  + [removeFromUpdateList](#removefromupdatelist)

    - [<instance> removeFromUpdateList()](#instance-removefromupdatelist)
  + [removeInteractive](#removeinteractive)

    - [<instance> removeInteractive([resetCursor])](#instance-removeinteractiveresetcursor)
  + [removeListener](#removelistener)

    - [<instance> removeListener(event, [fn], [context], [once])](#instance-removelistenerevent-fn-context-once)
  + [removePostPipeline](#removepostpipeline)

    - [<instance> removePostPipeline(pipeline)](#instance-removepostpipelinepipeline)
  + [renderDebug](#renderdebug)

    - [<instance> renderDebug(src, faces)](#instance-renderdebugsrc-faces)
  + [resetPipeline](#resetpipeline)

    - [<instance> resetPipeline([resetData])](#instance-resetpipelineresetdata)
  + [resetPostPipeline](#resetpostpipeline)

    - [<instance> resetPostPipeline([resetData])](#instance-resetpostpipelineresetdata)
  + [rotateX](#rotatex)

    - [<instance> rotateX()](#instance-rotatex)
  + [rotateY](#rotatey)

    - [<instance> rotateY()](#instance-rotatey)
  + [rotateZ](#rotatez)

    - [<instance> rotateZ()](#instance-rotatez)
  + [setAbove](#setabove)

    - [<instance> setAbove(gameObject)](#instance-setabovegameobject)
  + [setActive](#setactive)

    - [<instance> setActive(value)](#instance-setactivevalue)
  + [setAlpha](#setalpha)

    - [<instance> setAlpha([value])](#instance-setalphavalue)
  + [setAngle](#setangle)

    - [<instance> setAngle([degrees])](#instance-setangledegrees)
  + [setBelow](#setbelow)

    - [<instance> setBelow(gameObject)](#instance-setbelowgameobject)
  + [setBlendMode](#setblendmode)

    - [<instance> setBlendMode(value)](#instance-setblendmodevalue)
  + [setData](#setdata)

    - [<instance> setData(key, [data])](#instance-setdatakey-data)
  + [setDataEnabled](#setdataenabled)

    - [<instance> setDataEnabled()](#instance-setdataenabled)
  + [setDebug](#setdebug)

    - [<instance> setDebug([graphic], [callback])](#instance-setdebuggraphic-callback)
  + [setDepth](#setdepth)

    - [<instance> setDepth(value)](#instance-setdepthvalue)
  + [setDisplaySize](#setdisplaysize)

    - [<instance> setDisplaySize(width, height)](#instance-setdisplaysizewidth-height)
  + [setFrame](#setframe)

    - [<instance> setFrame(frame, [updateSize], [updateOrigin])](#instance-setframeframe-updatesize-updateorigin)
  + [setInteractive](#setinteractive)

    - [<instance> setInteractive([config])](#instance-setinteractiveconfig)
  + [setMask](#setmask)

    - [<instance> setMask(mask)](#instance-setmaskmask)
  + [setName](#setname)

    - [<instance> setName(value)](#instance-setnamevalue)
  + [setOrtho](#setortho)

    - [<instance> setOrtho([scaleX], [scaleY], [near], [far])](#instance-setorthoscalex-scaley-near-far)
  + [setPerspective](#setperspective)

    - [<instance> setPerspective(width, height, [fov], [near], [far])](#instance-setperspectivewidth-height-fov-near-far)
  + [setPipeline](#setpipeline)

    - [<instance> setPipeline(pipeline, [pipelineData], [copyData])](#instance-setpipelinepipeline-pipelinedata-copydata)
  + [setPipelineData](#setpipelinedata)

    - [<instance> setPipelineData(key, [value])](#instance-setpipelinedatakey-value)
  + [setPosition](#setposition)

    - [<instance> setPosition([x], [y], [z], [w])](#instance-setpositionx-y-z-w)
  + [setPostPipeline](#setpostpipeline)

    - [<instance> setPostPipeline(pipelines, [pipelineData], [copyData])](#instance-setpostpipelinepipelines-pipelinedata-copydata)
  + [setPostPipelineData](#setpostpipelinedata)

    - [<instance> setPostPipelineData(key, [value])](#instance-setpostpipelinedatakey-value)
  + [setRandomPosition](#setrandomposition)

    - [<instance> setRandomPosition([x], [y], [width], [height])](#instance-setrandompositionx-y-width-height)
  + [setRotation](#setrotation)

    - [<instance> setRotation([radians])](#instance-setrotationradians)
  + [setScale](#setscale)

    - [<instance> setScale([x], [y])](#instance-setscalex-y)
  + [setScrollFactor](#setscrollfactor)

    - [<instance> setScrollFactor(x, [y])](#instance-setscrollfactorx-y)
  + [setSize](#setsize)

    - [<instance> setSize(width, height)](#instance-setsizewidth-height)
  + [setSizeToFrame](#setsizetoframe)

    - [<instance> setSizeToFrame([resetUV])](#instance-setsizetoframeresetuv)
  + [setSizeToFrame](#setsizetoframe-1)

    - [<instance> setSizeToFrame([resetUV])](#instance-setsizetoframeresetuv-1)
  + [setState](#setstate)

    - [<instance> setState(value)](#instance-setstatevalue)
  + [setTexture](#settexture)

    - [<instance> setTexture(key, [frame], [updateSize], [updateOrigin])](#instance-settexturekey-frame-updatesize-updateorigin)
  + [setTint](#settint)

    - [<instance> setTint([tint])](#instance-settinttint)
  + [setToBack](#settoback)

    - [<instance> setToBack()](#instance-settoback)
  + [setToTop](#settotop)

    - [<instance> setToTop()](#instance-settotop)
  + [setViewHeight](#setviewheight)

    - [<instance> setViewHeight([value])](#instance-setviewheightvalue)
  + [setVisible](#setvisible)

    - [<instance> setVisible(value)](#instance-setvisiblevalue)
  + [setW](#setw)

    - [<instance> setW([value])](#instance-setwvalue)
  + [setX](#setx)

    - [<instance> setX([value])](#instance-setxvalue)
  + [setY](#sety)

    - [<instance> setY([value])](#instance-setyvalue)
  + [setZ](#setz)

    - [<instance> setZ([value])](#instance-setzvalue)
  + [shutdown](#shutdown)

    - [<instance> shutdown()](#instance-shutdown)
  + [sortByDepth](#sortbydepth)

    - [<instance> sortByDepth(faceA, faceB)](#instance-sortbydepthfacea-faceb)
  + [stop](#stop)

    - [<instance> stop()](#instance-stop)
  + [stopAfterDelay](#stopafterdelay)

    - [<instance> stopAfterDelay(delay)](#instance-stopafterdelaydelay)
  + [stopAfterRepeat](#stopafterrepeat)

    - [<instance> stopAfterRepeat([repeatCount])](#instance-stopafterrepeatrepeatcount)
  + [stopOnFrame](#stoponframe)

    - [<instance> stopOnFrame(frame)](#instance-stoponframeframe)
  + [tint](#tint)

    - [<instance> tint()](#instance-tint)
  + [toggleData](#toggledata)

    - [<instance> toggleData(key)](#instance-toggledatakey)
  + [toJSON](#tojson)

    - [<instance> toJSON()](#instance-tojson)
  + [update](#update)

    - [<instance> update([args])](#instance-updateargs)
  + [uvScale](#uvscale)

    - [<instance> uvScale(x, y)](#instance-uvscalex-y)
  + [uvScroll](#uvscroll)

    - [<instance> uvScroll(x, y)](#instance-uvscrollx-y)
  + [willRender](#willrender)

    - [<instance> willRender(camera)](#instance-willrendercamera)
* [Private Methods](#private-methods)

  + [preDestroy](#predestroy-1)

    - [<instance> preDestroy()](#instance-predestroy)
  + [renderCanvas](#rendercanvas)

    - [<instance> renderCanvas(renderer, src, camera)](#instance-rendercanvasrenderer-src-camera)
  + [renderWebGL](#renderwebgl)

    - [<instance> renderWebGL(renderer, src, camera, parentMatrix)](#instance-renderwebglrenderer-src-camera-parentmatrix)

Back to top

©2025[Phaser](https://docs.phaser.io)