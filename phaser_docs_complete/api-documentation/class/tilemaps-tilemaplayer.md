# TilemapLayer

Phaser.Tilemaps.TilemapLayer

A Tilemap Layer is a Game Object that renders LayerData from a Tilemap when used in combination

with one, or more, Tilesets.

Do not add TilemapLayers to Containers, they are stand-alone display objects.

**Constructor**

`new TilemapLayer(scene, tilemap, layerIndex, tileset, [x], [y])`

**Parameters**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| scene | [Phaser.Scene](scene.md) | No |  | The Scene to which this Game Object belongs. |
| --- | --- | --- | --- | --- |
| tilemap | [Phaser.Tilemaps.Tilemap](tilemaps-tilemap.md) | No |  | The Tilemap this layer is a part of. |
| layerIndex | number | No |  | The index of the LayerData associated with this layer. |
| tileset | string | Array.<string> | [Phaser.Tilemaps.Tileset](tilemaps-tileset.md) | Array.<[Phaser.Tilemaps.Tileset](tilemaps-tileset.md)> | No |
| x | number | Yes | 0 | The world x position where the top left of this layer will be placed. |
| y | number | Yes | 0 | The world y position where the top left of this layer will be placed. |

---

**Scope**: static

**Extends**

> [Phaser.GameObjects.GameObject](gameobjects-gameobject.md)  
> [Phaser.GameObjects.Components.Alpha](../namespace/gameobjects-components-alpha.md)  
> [Phaser.GameObjects.Components.BlendMode](../namespace/gameobjects-components-blendmode.md)  
> [Phaser.GameObjects.Components.ComputedSize](../namespace/gameobjects-components-computedsize.md)  
> [Phaser.GameObjects.Components.Depth](../namespace/gameobjects-components-depth.md)  
> [Phaser.GameObjects.Components.Flip](../namespace/gameobjects-components-flip.md)  
> [Phaser.GameObjects.Components.GetBounds](../namespace/gameobjects-components-getbounds.md)  
> [Phaser.GameObjects.Components.Mask](../namespace/gameobjects-components-mask.md)  
> [Phaser.GameObjects.Components.Origin](../namespace/gameobjects-components-origin.md)  
> [Phaser.GameObjects.Components.Pipeline](../namespace/gameobjects-components-pipeline.md)  
> [Phaser.GameObjects.Components.PostPipeline](../namespace/gameobjects-components-postpipeline.md)  
> [Phaser.GameObjects.Components.ScrollFactor](../namespace/gameobjects-components-scrollfactor.md)  
> [Phaser.GameObjects.Components.Transform](../namespace/gameobjects-components-transform.md)  
> [Phaser.GameObjects.Components.Visible](../namespace/gameobjects-components-visible.md)  
> [Phaser.Physics.Arcade.Components.Collision](../namespace/physics-arcade-components-collision.md)

> Source: [src/tilemaps/TilemapLayer.js#L15](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/TilemapLayer.js#L15)  
> Since: 3.50.0

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

**Inherits:** [Phaser.GameObjects.Components.Alpha#alpha](../namespace/gameobjects-components-alpha.md)

> Source: [src/gameobjects/components/Alpha.js#L129](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Alpha.js#L129)  
> Since: 3.0.0

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

## collisionCategory

### collisionCategory: number

**Description:**

The Tilemap Layer Collision Category.

This is exclusively used by the Arcade Physics system.

This can be set to any valid collision bitfield value.

See the `setCollisionCategory` method for more details.

> Source: [src/tilemaps/TilemapLayer.js#L264](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/TilemapLayer.js#L264)  
> Since: 3.70.0

---

## collisionMask

### collisionMask: number

**Description:**

The Tilemap Layer Collision Mask.

This is exclusively used by the Arcade Physics system.

See the `setCollidesWith` method for more details.

> Source: [src/tilemaps/TilemapLayer.js#L279](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/TilemapLayer.js#L279)  
> Since: 3.70.0

---

## cullCallback

### cullCallback: function

**Description:**

The callback that is invoked when the tiles are culled.

It will call a different function based on the map orientation:

Orthogonal (the default) is `TilemapComponents.CullTiles`

Isometric is `TilemapComponents.IsometricCullTiles`

Hexagonal is `TilemapComponents.HexagonalCullTiles`

Staggered is `TilemapComponents.StaggeredCullTiles`

However, you can override this to call any function you like.

It will be sent 4 arguments:

1. The Phaser.Tilemaps.LayerData object for this Layer
2. The Camera that is culling the layer. You can check its `dirty` property to see if it has changed since the last cull.
3. A reference to the `culledTiles` array, which should be used to store the tiles you want rendered.
4. The Render Order constant.

See the `TilemapComponents.CullTiles` source code for details on implementing your own culling system.

> Source: [src/tilemaps/TilemapLayer.js#L195](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/TilemapLayer.js#L195)  
> Since: 3.50.0

---

## culledTiles

### culledTiles: Array.<[Phaser.Tilemaps.Tile](tilemaps-tile.md)>

**Description:**

Used internally during rendering. This holds the tiles that are visible within the Camera.

> Source: [src/tilemaps/TilemapLayer.js#L148](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/TilemapLayer.js#L148)  
> Since: 3.50.0

---

## cullPaddingX

### cullPaddingX: number

**Description:**

The amount of extra tiles to add into the cull rectangle when calculating its horizontal size.

See the method `setCullPadding` for more details.

> Source: [src/tilemaps/TilemapLayer.js#L171](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/TilemapLayer.js#L171)  
> Since: 3.50.0

---

## cullPaddingY

### cullPaddingY: number

**Description:**

The amount of extra tiles to add into the cull rectangle when calculating its vertical size.

See the method `setCullPadding` for more details.

> Source: [src/tilemaps/TilemapLayer.js#L183](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/TilemapLayer.js#L183)  
> Since: 3.50.0

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

**Inherits:** [Phaser.GameObjects.Components.ComputedSize#displayHeight](../namespace/gameobjects-components-computedsize.md)

> Source: [src/gameobjects/components/ComputedSize.js#L68](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/ComputedSize.js#L68)  
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

## displayOriginX

### displayOriginX: number

**Description:**

The horizontal display origin of this Tilemap Layer.

**Overrides:** Phaser.GameObjects.Components.Origin#displayOriginX

> Source: [src/tilemaps/TilemapLayer.js#L312](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/TilemapLayer.js#L312)  
> Since: 3.0.0

---

## displayOriginY

### displayOriginY: number

**Description:**

The vertical display origin of this Tilemap Layer.

**Overrides:** Phaser.GameObjects.Components.Origin#displayOriginY

> Source: [src/tilemaps/TilemapLayer.js#L322](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/TilemapLayer.js#L322)  
> Since: 3.0.0

---

## displayWidth

### displayWidth: number

**Description:**

The displayed width of this Game Object.

This value takes into account the scale factor.

Setting this value will adjust the Game Object's scale property.

**Inherits:** [Phaser.GameObjects.Components.ComputedSize#displayWidth](../namespace/gameobjects-components-computedsize.md)

> Source: [src/gameobjects/components/ComputedSize.js#L43](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/ComputedSize.js#L43)  
> Since: 3.0.0

---

## flipX

### flipX: boolean

**Description:**

The horizontally flipped state of the Game Object.

A Game Object that is flipped horizontally will render inversed on the horizontal axis.

Flipping always takes place from the middle of the texture and does not impact the scale value.

If this Game Object has a physics body, it will not change the body. This is a rendering toggle only.

**Inherits:** [Phaser.GameObjects.Components.Flip#flipX](../namespace/gameobjects-components-flip.md)

> Source: [src/gameobjects/components/Flip.js#L17](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Flip.js#L17)  
> Since: 3.0.0

---

## flipY

### flipY: boolean

**Description:**

The vertically flipped state of the Game Object.

A Game Object that is flipped vertically will render inversed on the vertical axis (i.e. upside down)

Flipping always takes place from the middle of the texture and does not impact the scale value.

If this Game Object has a physics body, it will not change the body. This is a rendering toggle only.

**Inherits:** [Phaser.GameObjects.Components.Flip#flipY](../namespace/gameobjects-components-flip.md)

> Source: [src/gameobjects/components/Flip.js#L31](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Flip.js#L31)  
> Since: 3.0.0

---

## gidMap

### gidMap: Array.<[Phaser.Tilemaps.Tileset](tilemaps-tileset.md)>

**Description:**

An array holding the mapping between the tile indexes and the tileset they belong to.

> Source: [src/tilemaps/TilemapLayer.js#L245](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/TilemapLayer.js#L245)  
> Since: 3.50.0

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

**Inherits:** [Phaser.GameObjects.Components.ComputedSize#height](../namespace/gameobjects-components-computedsize.md)

> Source: [src/gameobjects/components/ComputedSize.js#L30](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/ComputedSize.js#L30)  
> Since: 3.0.0

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

## input

### input: [Phaser.Types.Input.InteractiveObject](../typedef/types-input.md)

**Description:**

If this Game Object is enabled for input then this property will contain an InteractiveObject instance.

Not usually set directly. Instead call `GameObject.setInteractive()`.

**Inherits:** [Phaser.GameObjects.GameObject#input](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L175](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L175)  
> Since: 3.0.0

---

## isTilemap

### isTilemap: boolean

**Description:**

Used internally by physics system to perform fast type checks.

> Source: [src/tilemaps/TilemapLayer.js#L78](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/TilemapLayer.js#L78)  
> Since: 3.50.0

---

## layer

### layer: [Phaser.Tilemaps.LayerData](tilemaps-layerdata.md)

**Description:**

The LayerData associated with this layer. LayerData can only be associated with one

tilemap layer.

> Source: [src/tilemaps/TilemapLayer.js#L106](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/TilemapLayer.js#L106)  
> Since: 3.50.0

---

## layerIndex

### layerIndex: number

**Description:**

The index of the LayerData associated with this layer.

> Source: [src/tilemaps/TilemapLayer.js#L97](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/TilemapLayer.js#L97)  
> Since: 3.50.0

---

## mask

### mask: [Phaser.Display.Masks.BitmapMask](display-masks-bitmapmask.md), [Phaser.Display.Masks.GeometryMask](display-masks-geometrymask.md)

**Description:**

The Mask this Game Object is using during render.

**Inherits:** [Phaser.GameObjects.Components.Mask#mask](../namespace/gameobjects-components-mask.md)

> Source: [src/gameobjects/components/Mask.js#L19](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Mask.js#L19)  
> Since: 3.0.0

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

The horizontal origin of this Tilemap Layer.

**Overrides:** Phaser.GameObjects.Components.Origin#originX

> Source: [src/tilemaps/TilemapLayer.js#L292](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/TilemapLayer.js#L292)  
> Since: 3.0.0

---

## originY

### originY: number

**Description:**

The vertical origin of this Tilemap Layer.

**Overrides:** Phaser.GameObjects.Components.Origin#originY

> Source: [src/tilemaps/TilemapLayer.js#L302](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/TilemapLayer.js#L302)  
> Since: 3.0.0

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

## skipCull

### skipCull: boolean

**Description:**

You can control if the camera should cull tiles on this layer before rendering them or not.

By default the camera will try to cull the tiles in this layer, to avoid over-drawing to the renderer.

However, there are some instances when you may wish to disable this, and toggling this flag allows

you to do so. Also see `setSkipCull` for a chainable method that does the same thing.

> Source: [src/tilemaps/TilemapLayer.js#L157](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/TilemapLayer.js#L157)  
> Since: 3.50.0

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

## tilemap

### tilemap: [Phaser.Tilemaps.Tilemap](tilemaps-tilemap.md)

**Description:**

The Tilemap that this layer is a part of.

> Source: [src/tilemaps/TilemapLayer.js#L88](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/TilemapLayer.js#L88)  
> Since: 3.50.0

---

## tilesDrawn

### tilesDrawn: number

**Description:**

The total number of tiles drawn by the renderer in the last frame.

> Source: [src/tilemaps/TilemapLayer.js#L128](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/TilemapLayer.js#L128)  
> Since: 3.50.0

---

## tileset

### tileset: Array.<[Phaser.Tilemaps.Tileset](tilemaps-tileset.md)>

**Description:**

An array of `Tileset` objects associated with this layer.

> Source: [src/tilemaps/TilemapLayer.js#L119](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/TilemapLayer.js#L119)  
> Since: 3.50.0

---

## tilesTotal

### tilesTotal: number

**Description:**

The total number of tiles in this layer. Updated every frame.

> Source: [src/tilemaps/TilemapLayer.js#L138](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/TilemapLayer.js#L138)  
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

**Inherits:** [Phaser.GameObjects.Components.ComputedSize#width](../namespace/gameobjects-components-computedsize.md)

> Source: [src/gameobjects/components/ComputedSize.js#L17](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/ComputedSize.js#L17)  
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

## \_blendMode

### \_blendMode: number

**Description:**

Private internal value. Holds the current blend mode.

**Access:** private

**Inherits:** [Phaser.GameObjects.Components.BlendMode#\_blendMode](../namespace/gameobjects-components-blendmode.md)

> Source: [src/gameobjects/components/BlendMode.js#L19](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/BlendMode.js#L19)  
> Since: 3.0.0

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

## \_originComponent

### \_originComponent: boolean

**Description:**

A property indicating that a Game Object has this component.

**Access:** private

**Inherits:** [Phaser.GameObjects.Components.Origin#\_originComponent](../namespace/gameobjects-components-origin.md)

> Source: [src/gameobjects/components/Origin.js#L19](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Origin.js#L19)  
> Since: 3.2.0

---

## \_renderOrder

### \_renderOrder: number

**Description:**

The rendering (draw) order of the tiles in this layer.

The default is 0 which is 'right-down', meaning it will draw the tiles starting from the top-left,

drawing to the right and then moving down to the next row.

The draw orders are:

0 = right-down

1 = left-down

2 = right-up

3 = left-up

This can be changed via the `setRenderOrder` method.

**Access:** private

> Source: [src/tilemaps/TilemapLayer.js#L222](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/TilemapLayer.js#L222)  
> Since: 3.50.0

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

## \_visible

### \_visible: boolean

**Description:**

Private internal value. Holds the visible value.

**Access:** private

**Inherits:** [Phaser.GameObjects.Components.Visible#\_visible](../namespace/gameobjects-components-visible.md)

> Source: [src/gameobjects/components/Visible.js#L20](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Visible.js#L20)  
> Since: 3.0.0

---

## tempVec

### tempVec: [Phaser.Math.Vector2](math-vector2.md)

**Description:**

A temporary Vector2 used in the tile coordinate methods.

**Access:** private

> Source: [src/tilemaps/TilemapLayer.js#L254](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/TilemapLayer.js#L254)  
> Since: 3.60.0

---

# Public Methods

## addCollidesWith

### <instance> addCollidesWith(category)

**Description:**

Adds the given Collision Category to the list of those that this

Arcade Physics Body will collide with.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| category | number | No | The collision category to add. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This Game Object.

**Inherits:** [Phaser.Physics.Arcade.Components.Collision#addCollidesWith](../namespace/physics-arcade-components-collision.md)

> Source: [src/physics/arcade/components/Collision.js#L60](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/components/Collision.js#L60)  
> Since: 3.70.0

---

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

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - `this`.

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

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This Game Object.

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

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This Game Object.

**Inherits:** [Phaser.GameObjects.GameObject#addToUpdateList](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L735](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L735)  
> Since: 3.53.0

---

## calculateFacesAt

### <instance> calculateFacesAt(tileX, tileY)

**Description:**

Calculates interesting faces at the given tile coordinates of the specified layer. Interesting

faces are used internally for optimizing collisions against tiles. This method is mostly used

internally to optimize recalculating faces when only one tile has been changed.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tileX | number | No | The x coordinate. |
| --- | --- | --- | --- |
| tileY | number | No | The y coordinate. |

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This Tilemap Layer object.

> Source: [src/tilemaps/TilemapLayer.js#L430](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/TilemapLayer.js#L430)  
> Since: 3.50.0

---

## calculateFacesWithin

### <instance> calculateFacesWithin([tileX], [tileY], [width], [height])

**Description:**

Calculates interesting faces within the rectangular area specified (in tile coordinates) of the

layer. Interesting faces are used internally for optimizing collisions against tiles. This method

is mostly used internally.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tileX | number | Yes | The left most tile index (in tile coordinates) to use as the origin of the area. |
| --- | --- | --- | --- |
| tileY | number | Yes | The top most tile index (in tile coordinates) to use as the origin of the area. |
| width | number | Yes | How many tiles wide from the `tileX` index the area will be. |
| height | number | Yes | How many tiles tall from the `tileY` index the area will be. |

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This Tilemap Layer object.

> Source: [src/tilemaps/TilemapLayer.js#L450](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/TilemapLayer.js#L450)  
> Since: 3.50.0

---

## clearAlpha

### <instance> clearAlpha()

**Description:**

Clears all alpha values associated with this Game Object.

Immediately sets the alpha levels back to 1 (fully opaque).

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This Game Object instance.

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

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This Game Object.

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

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Mask#clearMask](../namespace/gameobjects-components-mask.md)

> Source: [src/gameobjects/components/Mask.js#L56](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Mask.js#L56)  
> Since: 3.6.2

---

## copy

### <instance> copy(srcTileX, srcTileY, width, height, destTileX, destTileY, [recalculateFaces])

**Description:**

Copies the tiles in the source rectangular area to a new destination (all specified in tile

coordinates) within the layer. This copies all tile properties & recalculates collision

information in the destination region.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| srcTileX | number | No |  | The x coordinate of the area to copy from, in tiles, not pixels. |
| --- | --- | --- | --- | --- |
| srcTileY | number | No |  | The y coordinate of the area to copy from, in tiles, not pixels. |
| width | number | No |  | The width of the area to copy, in tiles, not pixels. |
| height | number | No |  | The height of the area to copy, in tiles, not pixels. |
| destTileX | number | No |  | The x coordinate of the area to copy to, in tiles, not pixels. |
| destTileY | number | No |  | The y coordinate of the area to copy to, in tiles, not pixels. |
| recalculateFaces | boolean | Yes | true | `true` if the faces data should be recalculated. |

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This Tilemap Layer object.

> Source: [src/tilemaps/TilemapLayer.js#L513](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/TilemapLayer.js#L513)  
> Since: 3.50.0

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

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This Game Object instance.

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

## createFromTiles

### <instance> createFromTiles(indexes, replacements, [spriteConfig], [scene], [camera])

**Description:**

Creates a Sprite for every object matching the given tile indexes in the layer. You can

optionally specify if each tile will be replaced with a new tile after the Sprite has been

created. This is useful if you want to lay down special tiles in a level that are converted to

Sprites, but want to replace the tile itself with a floor tile or similar once converted.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| indexes | number | array | No | The tile index, or array of indexes, to create Sprites from. |
| --- | --- | --- | --- |
| replacements | number | array | No | The tile index, or array of indexes, to change a converted tile to. Set to `null` to leave the tiles unchanged. If an array is given, it is assumed to be a one-to-one mapping with the indexes array. |
| spriteConfig | [Phaser.Types.GameObjects.Sprite.SpriteConfig](../typedef/types-gameobjects-sprite.md) | Yes | The config object to pass into the Sprite creator (i.e. scene.make.sprite). |
| scene | [Phaser.Scene](scene.md) | Yes | The Scene to create the Sprites within. |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | Yes | The Camera to use when determining the world XY |

**Returns:** Array.<[Phaser.GameObjects.Sprite](gameobjects-sprite.md)> - An array of the Sprites that were created.

> Source: [src/tilemaps/TilemapLayer.js#L472](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/TilemapLayer.js#L472)  
> Since: 3.50.0

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

## cull

### <instance> cull([camera])

**Description:**

Returns the tiles in the given layer that are within the cameras viewport.

This is used internally during rendering.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | Yes | The Camera to run the cull check against. |
| --- | --- | --- | --- |

**Returns:** Array.<[Phaser.Tilemaps.Tile](tilemaps-tile.md)> - An array of Tile objects to render.

> Source: [src/tilemaps/TilemapLayer.js#L497](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/TilemapLayer.js#L497)  
> Since: 3.50.0

---

## destroy

### <instance> destroy([removeFromTilemap])

**Description:**

Destroys this TilemapLayer and removes its link to the associated LayerData.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| removeFromTilemap | boolean | Yes | true | Remove this layer from the parent Tilemap? |
| --- | --- | --- | --- | --- |

**Overrides:** Phaser.GameObjects.GameObject#destroy

> Source: [src/tilemaps/TilemapLayer.js#L1491](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/TilemapLayer.js#L1491)  
> Since: 3.50.0

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

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This GameObject.

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

## fill

### <instance> fill(index, [tileX], [tileY], [width], [height], [recalculateFaces])

**Description:**

Sets the tiles in the given rectangular area (in tile coordinates) of the layer with the

specified index. Tiles will be set to collide if the given index is a colliding index.

Collision information in the region will be recalculated.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| index | number | No |  | The tile index to fill the area with. |
| --- | --- | --- | --- | --- |
| tileX | number | Yes |  | The left most tile index (in tile coordinates) to use as the origin of the area. |
| tileY | number | Yes |  | The top most tile index (in tile coordinates) to use as the origin of the area. |
| width | number | Yes |  | How many tiles wide from the `tileX` index the area will be. |
| height | number | Yes |  | How many tiles tall from the `tileY` index the area will be. |
| recalculateFaces | boolean | Yes | true | `true` if the faces data should be recalculated. |

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This Tilemap Layer object.

> Source: [src/tilemaps/TilemapLayer.js#L538](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/TilemapLayer.js#L538)  
> Since: 3.50.0

---

## filterTiles

### <instance> filterTiles(callback, [context], [tileX], [tileY], [width], [height], [filteringOptions])

**Description:**

For each tile in the given rectangular area (in tile coordinates) of the layer, run the given

filter callback function. Any tiles that pass the filter test (i.e. where the callback returns

true) will returned as a new array. Similar to Array.prototype.Filter in vanilla JS.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| callback | function | No | The callback. Each tile in the given area will be passed to this callback as the first and only parameter. The callback should return true for tiles that pass the filter. |
| --- | --- | --- | --- |
| context | object | Yes | The context under which the callback should be run. |
| tileX | number | Yes | The left most tile index (in tile coordinates) to use as the origin of the area to filter. |
| tileY | number | Yes | The top most tile index (in tile coordinates) to use as the origin of the area to filter. |
| width | number | Yes | How many tiles wide from the `tileX` index the area will be. |
| height | number | Yes | How many tiles tall from the `tileY` index the area will be. |
| filteringOptions | [Phaser.Types.Tilemaps.FilteringOptions](../typedef/types-tilemaps.md) | Yes | Optional filters to apply when getting the tiles. |

**Returns:** Array.<[Phaser.Tilemaps.Tile](tilemaps-tile.md)> - An array of Tile objects.

> Source: [src/tilemaps/TilemapLayer.js#L562](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/TilemapLayer.js#L562)  
> Since: 3.50.0

---

## findByIndex

### <instance> findByIndex(index, [skip], [reverse])

**Description:**

Searches the entire map layer for the first tile matching the given index, then returns that Tile

object. If no match is found, it returns null. The search starts from the top-left tile and

continues horizontally until it hits the end of the row, then it drops down to the next column.

If the reverse boolean is true, it scans starting from the bottom-right corner traveling up to

the top-left.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| index | number | No |  | The tile index value to search for. |
| --- | --- | --- | --- | --- |
| skip | number | Yes | 0 | The number of times to skip a matching tile before returning. |
| reverse | boolean | Yes | false | If true it will scan the layer in reverse, starting at the bottom-right. Otherwise it scans from the top-left. |

**Returns:** [Phaser.Tilemaps.Tile](tilemaps-tile.md) - The first matching Tile object.

> Source: [src/tilemaps/TilemapLayer.js#L587](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/TilemapLayer.js#L587)  
> Since: 3.50.0

---

## findTile

### <instance> findTile(callback, [context], [tileX], [tileY], [width], [height], [filteringOptions])

**Description:**

Find the first tile in the given rectangular area (in tile coordinates) of the layer that

satisfies the provided testing function. I.e. finds the first tile for which `callback` returns

true. Similar to Array.prototype.find in vanilla JS.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| callback | FindTileCallback | No | The callback. Each tile in the given area will be passed to this callback as the first and only parameter. |
| --- | --- | --- | --- |
| context | object | Yes | The context under which the callback should be run. |
| tileX | number | Yes | The left most tile index (in tile coordinates) to use as the origin of the area to search. |
| tileY | number | Yes | The top most tile index (in tile coordinates) to use as the origin of the area to search. |
| width | number | Yes | How many tiles wide from the `tileX` index the area will be. |
| height | number | Yes | How many tiles tall from the `tileY` index the area will be. |
| filteringOptions | [Phaser.Types.Tilemaps.FilteringOptions](../typedef/types-tilemaps.md) | Yes | Optional filters to apply when getting the tiles. |

**Returns:** [Phaser.Tilemaps.Tile](tilemaps-tile.md) - The first Tile found at the given location.

> Source: [src/tilemaps/TilemapLayer.js#L608](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/TilemapLayer.js#L608)  
> Since: 3.50.0

---

## forEachTile

### <instance> forEachTile(callback, [context], [tileX], [tileY], [width], [height], [filteringOptions])

**Description:**

For each tile in the given rectangular area (in tile coordinates) of the layer, run the given

callback. Similar to Array.prototype.forEach in vanilla JS.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| callback | EachTileCallback | No | The callback. Each tile in the given area will be passed to this callback as the first and only parameter. |
| --- | --- | --- | --- |
| context | object | Yes | The context, or scope, under which the callback should be run. |
| tileX | number | Yes | The left most tile index (in tile coordinates) to use as the origin of the area to search. |
| tileY | number | Yes | The top most tile index (in tile coordinates) to use as the origin of the area to search. |
| width | number | Yes | How many tiles wide from the `tileX` index the area will be. |
| height | number | Yes | How many tiles tall from the `tileY` index the area will be. |
| filteringOptions | [Phaser.Types.Tilemaps.FilteringOptions](../typedef/types-tilemaps.md) | Yes | Optional filters to apply when getting the tiles. |

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This Tilemap Layer object.

> Source: [src/tilemaps/TilemapLayer.js#L631](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/TilemapLayer.js#L631)  
> Since: 3.50.0

---

## getBottomCenter

### <instance> getBottomCenter([output], [includeParent])

**Description:**

Gets the bottom-center coordinate of this Game Object, regardless of origin.

The returned point is calculated in local space and does not factor in any parent Containers,

unless the `includeParent` argument is set to `true`.

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| output | [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) | Yes |  | An object to store the values in. If not provided a new Vector2 will be created. |
| --- | --- | --- | --- | --- |
| includeParent | boolean | Yes | false | If this Game Object has a parent Container, include it (and all other ancestors) in the resulting vector? |

**Returns:** [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) - The values stored in the output object.

**Inherits:** [Phaser.GameObjects.Components.GetBounds#getBottomCenter](../namespace/gameobjects-components-getbounds.md)

> Source: [src/gameobjects/components/GetBounds.js#L236](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/GetBounds.js#L236)  
> Since: 3.18.0

---

## getBottomLeft

### <instance> getBottomLeft([output], [includeParent])

**Description:**

Gets the bottom-left corner coordinate of this Game Object, regardless of origin.

The returned point is calculated in local space and does not factor in any parent Containers,

unless the `includeParent` argument is set to `true`.

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| output | [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) | Yes |  | An object to store the values in. If not provided a new Vector2 will be created. |
| --- | --- | --- | --- | --- |
| includeParent | boolean | Yes | false | If this Game Object has a parent Container, include it (and all other ancestors) in the resulting vector? |

**Returns:** [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) - The values stored in the output object.

**Inherits:** [Phaser.GameObjects.Components.GetBounds#getBottomLeft](../namespace/gameobjects-components-getbounds.md)

> Source: [src/gameobjects/components/GetBounds.js#L210](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/GetBounds.js#L210)  
> Since: 3.0.0

---

## getBottomRight

### <instance> getBottomRight([output], [includeParent])

**Description:**

Gets the bottom-right corner coordinate of this Game Object, regardless of origin.

The returned point is calculated in local space and does not factor in any parent Containers,

unless the `includeParent` argument is set to `true`.

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| output | [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) | Yes |  | An object to store the values in. If not provided a new Vector2 will be created. |
| --- | --- | --- | --- | --- |
| includeParent | boolean | Yes | false | If this Game Object has a parent Container, include it (and all other ancestors) in the resulting vector? |

**Returns:** [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) - The values stored in the output object.

**Inherits:** [Phaser.GameObjects.Components.GetBounds#getBottomRight](../namespace/gameobjects-components-getbounds.md)

> Source: [src/gameobjects/components/GetBounds.js#L262](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/GetBounds.js#L262)  
> Since: 3.0.0

---

## getBounds

### <instance> getBounds([output])

**Description:**

Gets the bounds of this Game Object, regardless of origin.

The values are stored and returned in a Rectangle, or Rectangle-like, object.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| output | [Phaser.Geom.Rectangle](geom-rectangle.md) | object | Yes | An object to store the values in. If not provided a new Rectangle will be created. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Geom.Rectangle](geom-rectangle.md), object - The values stored in the output object.

**Inherits:** [Phaser.GameObjects.Components.GetBounds#getBounds](../namespace/gameobjects-components-getbounds.md)

> Source: [src/gameobjects/components/GetBounds.js#L288](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/GetBounds.js#L288)  
> Since: 3.0.0

---

## getCenter

### <instance> getCenter([output], [includeParent])

**Description:**

Gets the center coordinate of this Game Object, regardless of origin.

The returned point is calculated in local space and does not factor in any parent Containers,

unless the `includeParent` argument is set to `true`.

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| output | [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) | Yes |  | An object to store the values in. If not provided a new Vector2 will be created. |
| --- | --- | --- | --- | --- |
| includeParent | boolean | Yes | false | If this Game Object has a parent Container, include it (and all other ancestors) in the resulting vector? |

**Returns:** [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) - The values stored in the output object.

**Inherits:** [Phaser.GameObjects.Components.GetBounds#getCenter](../namespace/gameobjects-components-getbounds.md)

> Source: [src/gameobjects/components/GetBounds.js#L54](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/GetBounds.js#L54)  
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

## getIsoTileAtWorldXY

### <instance> getIsoTileAtWorldXY(worldX, worldY, [originTop], [nonNull], [camera])

**Description:**

Gets a tile at the given world coordinates from the given isometric layer.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| worldX | number | No |  | X position to get the tile from (given in pixels) |
| --- | --- | --- | --- | --- |
| worldY | number | No |  | Y position to get the tile from (given in pixels) |
| originTop | boolean | Yes | true | Which is the active face of the isometric tile? The top (default, true), or the base? (false) |
| nonNull | boolean | Yes | false | For empty tiles, return a Tile object with an index of -1 instead of null. |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | Yes |  | The Camera to use when calculating the tile index from the world values. |

**Returns:** [Phaser.Tilemaps.Tile](tilemaps-tile.md) - The tile at the given coordinates or null if no tile was found or the coordinates were invalid.

> Source: [src/tilemaps/TilemapLayer.js#L766](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/TilemapLayer.js#L766)  
> Since: 3.60.0

---

## getLeftCenter

### <instance> getLeftCenter([output], [includeParent])

**Description:**

Gets the left-center coordinate of this Game Object, regardless of origin.

The returned point is calculated in local space and does not factor in any parent Containers,

unless the `includeParent` argument is set to `true`.

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| output | [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) | Yes |  | An object to store the values in. If not provided a new Vector2 will be created. |
| --- | --- | --- | --- | --- |
| includeParent | boolean | Yes | false | If this Game Object has a parent Container, include it (and all other ancestors) in the resulting vector? |

**Returns:** [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) - The values stored in the output object.

**Inherits:** [Phaser.GameObjects.Components.GetBounds#getLeftCenter](../namespace/gameobjects-components-getbounds.md)

> Source: [src/gameobjects/components/GetBounds.js#L158](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/GetBounds.js#L158)  
> Since: 3.18.0

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

## getRightCenter

### <instance> getRightCenter([output], [includeParent])

**Description:**

Gets the right-center coordinate of this Game Object, regardless of origin.

The returned point is calculated in local space and does not factor in any parent Containers,

unless the `includeParent` argument is set to `true`.

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| output | [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) | Yes |  | An object to store the values in. If not provided a new Vector2 will be created. |
| --- | --- | --- | --- | --- |
| includeParent | boolean | Yes | false | If this Game Object has a parent Container, include it (and all other ancestors) in the resulting vector? |

**Returns:** [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) - The values stored in the output object.

**Inherits:** [Phaser.GameObjects.Components.GetBounds#getRightCenter](../namespace/gameobjects-components-getbounds.md)

> Source: [src/gameobjects/components/GetBounds.js#L184](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/GetBounds.js#L184)  
> Since: 3.18.0

---

## getTileAt

### <instance> getTileAt(tileX, tileY, [nonNull])

**Description:**

Gets a tile at the given tile coordinates from the given layer.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| tileX | number | No |  | X position to get the tile from (given in tile units, not pixels). |
| --- | --- | --- | --- | --- |
| tileY | number | No |  | Y position to get the tile from (given in tile units, not pixels). |
| nonNull | boolean | Yes | false | For empty tiles, return a Tile object with an index of -1 instead of null. |

**Returns:** [Phaser.Tilemaps.Tile](tilemaps-tile.md) - The Tile at the given coordinates or null if no tile was found or the coordinates were invalid.

> Source: [src/tilemaps/TilemapLayer.js#L731](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/TilemapLayer.js#L731)  
> Since: 3.50.0

---

## getTileAtWorldXY

### <instance> getTileAtWorldXY(worldX, worldY, [nonNull], [camera])

**Description:**

Gets a tile at the given world coordinates from the given layer.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| worldX | number | No |  | X position to get the tile from (given in pixels) |
| --- | --- | --- | --- | --- |
| worldY | number | No |  | Y position to get the tile from (given in pixels) |
| nonNull | boolean | Yes | false | For empty tiles, return a Tile object with an index of -1 instead of null. |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | Yes |  | The Camera to use when calculating the tile index from the world values. |

**Returns:** [Phaser.Tilemaps.Tile](tilemaps-tile.md) - The tile at the given coordinates or null if no tile was found or the coordinates were invalid.

> Source: [src/tilemaps/TilemapLayer.js#L748](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/TilemapLayer.js#L748)  
> Since: 3.50.0

---

## getTileCorners

### <instance> getTileCorners(tileX, tileY, [camera])

**Description:**

Returns an array of Vector2s where each entry corresponds to the corner of the requested tile.

The `tileX` and `tileY` parameters are in tile coordinates, not world coordinates.

The corner coordinates are in world space, having factored in TilemapLayer scale, position

and the camera, if given.

The size of the array will vary based on the orientation of the map. For example an

orthographic map will return an array of 4 vectors, where-as a hexagonal map will,

of course, return an array of 6 corner vectors.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tileX | number | No | The x coordinate, in tiles, not pixels. |
| --- | --- | --- | --- |
| tileY | number | No | The y coordinate, in tiles, not pixels. |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | Yes | The Camera to use when calculating the tile index from the world values. |

**Returns:** Array.<[Phaser.Math.Vector2](math-vector2.md)> - Returns an array of Vector2s, or null if the layer given was invalid.

> Source: [src/tilemaps/TilemapLayer.js#L1367](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/TilemapLayer.js#L1367)  
> Since: 3.60.0

---

## getTilesWithin

### <instance> getTilesWithin([tileX], [tileY], [width], [height], [filteringOptions])

**Description:**

Gets the tiles in the given rectangular area (in tile coordinates) of the layer.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tileX | number | Yes | The left most tile index (in tile coordinates) to use as the origin of the area. |
| --- | --- | --- | --- |
| tileY | number | Yes | The top most tile index (in tile coordinates) to use as the origin of the area. |
| width | number | Yes | How many tiles wide from the `tileX` index the area will be. |
| height | number | Yes | How many tiles tall from the `tileY` index the area will be. |
| filteringOptions | [Phaser.Types.Tilemaps.FilteringOptions](../typedef/types-tilemaps.md) | Yes | Optional filters to apply when getting the tiles. |

**Returns:** Array.<[Phaser.Tilemaps.Tile](tilemaps-tile.md)> - An array of Tile objects found within the area.

> Source: [src/tilemaps/TilemapLayer.js#L791](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/TilemapLayer.js#L791)  
> Since: 3.50.0

---

## getTilesWithinShape

### <instance> getTilesWithinShape(shape, [filteringOptions], [camera])

**Description:**

Gets the tiles that overlap with the given shape in the given layer. The shape must be a Circle,

Line, Rectangle or Triangle. The shape should be in world coordinates.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| shape | [Phaser.Geom.Circle](geom-circle.md) | [Phaser.Geom.Line](geom-line.md) | [Phaser.Geom.Rectangle](geom-rectangle.md) | [Phaser.Geom.Triangle](geom-triangle.md) |
| --- | --- | --- | --- |
| filteringOptions | [Phaser.Types.Tilemaps.FilteringOptions](../typedef/types-tilemaps.md) | Yes | Optional filters to apply when getting the tiles. |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | Yes | The Camera to use when factoring in which tiles to return. |

**Returns:** Array.<[Phaser.Tilemaps.Tile](tilemaps-tile.md)> - An array of Tile objects found within the shape.

> Source: [src/tilemaps/TilemapLayer.js#L810](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/TilemapLayer.js#L810)  
> Since: 3.50.0

---

## getTilesWithinWorldXY

### <instance> getTilesWithinWorldXY(worldX, worldY, width, height, [filteringOptions], [camera])

**Description:**

Gets the tiles in the given rectangular area (in world coordinates) of the layer.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| worldX | number | No | The world x coordinate for the top-left of the area. |
| --- | --- | --- | --- |
| worldY | number | No | The world y coordinate for the top-left of the area. |
| width | number | No | The width of the area. |
| height | number | No | The height of the area. |
| filteringOptions | [Phaser.Types.Tilemaps.FilteringOptions](../typedef/types-tilemaps.md) | Yes | Optional filters to apply when getting the tiles. |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | Yes | The Camera to use when factoring in which tiles to return. |

**Returns:** Array.<[Phaser.Tilemaps.Tile](tilemaps-tile.md)> - An array of Tile objects found within the area.

> Source: [src/tilemaps/TilemapLayer.js#L828](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/TilemapLayer.js#L828)  
> Since: 3.50.0

---

## getTopCenter

### <instance> getTopCenter([output], [includeParent])

**Description:**

Gets the top-center coordinate of this Game Object, regardless of origin.

The returned point is calculated in local space and does not factor in any parent Containers,

unless the `includeParent` argument is set to `true`.

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| output | [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) | Yes |  | An object to store the values in. If not provided a new Vector2 will be created. |
| --- | --- | --- | --- | --- |
| includeParent | boolean | Yes | false | If this Game Object has a parent Container, include it (and all other ancestors) in the resulting vector? |

**Returns:** [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) - The values stored in the output object.

**Inherits:** [Phaser.GameObjects.Components.GetBounds#getTopCenter](../namespace/gameobjects-components-getbounds.md)

> Source: [src/gameobjects/components/GetBounds.js#L106](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/GetBounds.js#L106)  
> Since: 3.18.0

---

## getTopLeft

### <instance> getTopLeft([output], [includeParent])

**Description:**

Gets the top-left corner coordinate of this Game Object, regardless of origin.

The returned point is calculated in local space and does not factor in any parent Containers,

unless the `includeParent` argument is set to `true`.

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| output | [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) | Yes |  | An object to store the values in. If not provided a new Vector2 will be created. |
| --- | --- | --- | --- | --- |
| includeParent | boolean | Yes | false | If this Game Object has a parent Container, include it (and all other ancestors) in the resulting vector? |

**Returns:** [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) - The values stored in the output object.

**Inherits:** [Phaser.GameObjects.Components.GetBounds#getTopLeft](../namespace/gameobjects-components-getbounds.md)

> Source: [src/gameobjects/components/GetBounds.js#L80](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/GetBounds.js#L80)  
> Since: 3.0.0

---

## getTopRight

### <instance> getTopRight([output], [includeParent])

**Description:**

Gets the top-right corner coordinate of this Game Object, regardless of origin.

The returned point is calculated in local space and does not factor in any parent Containers,

unless the `includeParent` argument is set to `true`.

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| output | [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) | Yes |  | An object to store the values in. If not provided a new Vector2 will be created. |
| --- | --- | --- | --- | --- |
| includeParent | boolean | Yes | false | If this Game Object has a parent Container, include it (and all other ancestors) in the resulting vector? |

**Returns:** [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) - The values stored in the output object.

**Inherits:** [Phaser.GameObjects.Components.GetBounds#getTopRight](../namespace/gameobjects-components-getbounds.md)

> Source: [src/gameobjects/components/GetBounds.js#L132](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/GetBounds.js#L132)  
> Since: 3.0.0

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

## hasTileAt

### <instance> hasTileAt(tileX, tileY)

**Description:**

Checks if there is a tile at the given location (in tile coordinates) in the given layer. Returns

false if there is no tile or if the tile at that location has an index of -1.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tileX | number | No | The x coordinate, in tiles, not pixels. |
| --- | --- | --- | --- |
| tileY | number | No | The y coordinate, in tiles, not pixels. |

**Returns:** boolean - `true` if a tile was found at the given location, otherwise `false`.

> Source: [src/tilemaps/TilemapLayer.js#L848](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/TilemapLayer.js#L848)  
> Since: 3.50.0

---

## hasTileAtWorldXY

### <instance> hasTileAtWorldXY(worldX, worldY, [camera])

**Description:**

Checks if there is a tile at the given location (in world coordinates) in the given layer. Returns

false if there is no tile or if the tile at that location has an index of -1.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| worldX | number | No | The x coordinate, in pixels. |
| --- | --- | --- | --- |
| worldY | number | No | The y coordinate, in pixels. |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | Yes | The Camera to use when factoring in which tiles to return. |

**Returns:** boolean - `true` if a tile was found at the given location, otherwise `false`.

> Source: [src/tilemaps/TilemapLayer.js#L865](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/TilemapLayer.js#L865)  
> Since: 3.50.0

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

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This GameObject.

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

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - `this`.

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

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - `this`.

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

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#once](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L124](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L124)  
> Since: 3.0.0

---

## putTileAt

### <instance> putTileAt(tile, tileX, tileY, [recalculateFaces])

**Description:**

Puts a tile at the given tile coordinates in the specified layer. You can pass in either an index

or a Tile object. If you pass in a Tile, all attributes will be copied over to the specified

location. If you pass in an index, only the index at the specified location will be changed.

Collision information will be recalculated at the specified location.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| tile | number | [Phaser.Tilemaps.Tile](tilemaps-tile.md) | No |  | The index of this tile to set or a Tile object. |
| --- | --- | --- | --- | --- |
| tileX | number | No |  | The x coordinate, in tiles, not pixels. |
| tileY | number | No |  | The y coordinate, in tiles, not pixels. |
| recalculateFaces | boolean | Yes | true | `true` if the faces data should be recalculated. |

**Returns:** [Phaser.Tilemaps.Tile](tilemaps-tile.md) - The Tile object that was inserted at the given coordinates.

> Source: [src/tilemaps/TilemapLayer.js#L883](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/TilemapLayer.js#L883)  
> Since: 3.50.0

---

## putTileAtWorldXY

### <instance> putTileAtWorldXY(tile, worldX, worldY, [recalculateFaces], [camera])

**Description:**

Puts a tile at the given world coordinates (pixels) in the specified layer. You can pass in either

an index or a Tile object. If you pass in a Tile, all attributes will be copied over to the

specified location. If you pass in an index, only the index at the specified location will be

changed. Collision information will be recalculated at the specified location.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tile | number | [Phaser.Tilemaps.Tile](tilemaps-tile.md) | No | The index of this tile to set or a Tile object. |
| --- | --- | --- | --- |
| worldX | number | No | The x coordinate, in pixels. |
| worldY | number | No | The y coordinate, in pixels. |
| recalculateFaces | boolean | Yes | `true` if the faces data should be recalculated. |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | Yes | The Camera to use when calculating the tile index from the world values. |

**Returns:** [Phaser.Tilemaps.Tile](tilemaps-tile.md) - The Tile object that was inserted at the given coordinates.

> Source: [src/tilemaps/TilemapLayer.js#L904](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/TilemapLayer.js#L904)  
> Since: 3.50.0

---

## putTilesAt

### <instance> putTilesAt(tile, tileX, tileY, [recalculateFaces])

**Description:**

Puts an array of tiles or a 2D array of tiles at the given tile coordinates in the specified

layer. The array can be composed of either tile indexes or Tile objects. If you pass in a Tile,

all attributes will be copied over to the specified location. If you pass in an index, only the

index at the specified location will be changed. Collision information will be recalculated

within the region tiles were changed.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| tile | Array.<number> | Array.<Array.<number>> | Array.<[Phaser.Tilemaps.Tile](tilemaps-tile.md)> | Array.<Array.<[Phaser.Tilemaps.Tile](tilemaps-tile.md)>> | No |
| --- | --- | --- | --- | --- |
| tileX | number | No |  | The x coordinate, in tiles, not pixels. |
| tileY | number | No |  | The y coordinate, in tiles, not pixels. |
| recalculateFaces | boolean | Yes | true | `true` if the faces data should be recalculated. |

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This Tilemap Layer object.

> Source: [src/tilemaps/TilemapLayer.js#L926](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/TilemapLayer.js#L926)  
> Since: 3.50.0

---

## randomize

### <instance> randomize([tileX], [tileY], [width], [height], [indexes])

**Description:**

Randomizes the indexes of a rectangular region of tiles (in tile coordinates) within the

specified layer. Each tile will receive a new index. If an array of indexes is passed in, then

those will be used for randomly assigning new tile indexes. If an array is not provided, the

indexes found within the region (excluding -1) will be used for randomly assigning new tile

indexes. This method only modifies tile indexes and does not change collision information.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tileX | number | Yes | The left most tile index (in tile coordinates) to use as the origin of the area. |
| --- | --- | --- | --- |
| tileY | number | Yes | The top most tile index (in tile coordinates) to use as the origin of the area. |
| width | number | Yes | How many tiles wide from the `tileX` index the area will be. |
| height | number | Yes | How many tiles tall from the `tileY` index the area will be. |
| indexes | Array.<number> | Yes | An array of indexes to randomly draw from during randomization. |

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This Tilemap Layer object.

> Source: [src/tilemaps/TilemapLayer.js#L950](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/TilemapLayer.js#L950)  
> Since: 3.50.0

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

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#removeAllListeners](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L165](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L165)  
> Since: 3.0.0

---

## removeCollidesWith

### <instance> removeCollidesWith(category)

**Description:**

Removes the given Collision Category from the list of those that this

Arcade Physics Body will collide with.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| category | number | No | The collision category to add. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This Game Object.

**Inherits:** [Phaser.Physics.Arcade.Components.Collision#removeCollidesWith](../namespace/physics-arcade-components-collision.md)

> Source: [src/physics/arcade/components/Collision.js#L80](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/components/Collision.js#L80)  
> Since: 3.70.0

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

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This Game Object.

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

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This Game Object.

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

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This GameObject.

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

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - `this`.

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

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This Game Object.

**Inherits:** [Phaser.GameObjects.Components.PostPipeline#removePostPipeline](../namespace/gameobjects-components-postpipeline.md)

> Source: [src/gameobjects/components/PostPipeline.js#L299](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/PostPipeline.js#L299)  
> Since: 3.60.0

---

## removeTileAt

### <instance> removeTileAt(tileX, tileY, [replaceWithNull], [recalculateFaces])

**Description:**

Removes the tile at the given tile coordinates in the specified layer and updates the layers

collision information.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| tileX | number | No |  | The x coordinate, in tiles, not pixels. |
| --- | --- | --- | --- | --- |
| tileY | number | No |  | The y coordinate, in tiles, not pixels. |
| replaceWithNull | boolean | Yes | true | If true, this will replace the tile at the specified location with null instead of a Tile with an index of -1. |
| recalculateFaces | boolean | Yes | true | `true` if the faces data should be recalculated. |

**Returns:** [Phaser.Tilemaps.Tile](tilemaps-tile.md) - A Tile object.

> Source: [src/tilemaps/TilemapLayer.js#L975](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/TilemapLayer.js#L975)  
> Since: 3.50.0

---

## removeTileAtWorldXY

### <instance> removeTileAtWorldXY(worldX, worldY, [replaceWithNull], [recalculateFaces], [camera])

**Description:**

Removes the tile at the given world coordinates in the specified layer and updates the layers

collision information.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| worldX | number | No |  | The x coordinate, in pixels. |
| --- | --- | --- | --- | --- |
| worldY | number | No |  | The y coordinate, in pixels. |
| replaceWithNull | boolean | Yes | true | If true, this will replace the tile at the specified location with null instead of a Tile with an index of -1. |
| recalculateFaces | boolean | Yes | true | `true` if the faces data should be recalculated. |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | Yes |  | The Camera to use when calculating the tile index from the world values. |

**Returns:** [Phaser.Tilemaps.Tile](tilemaps-tile.md) - The Tile object that was removed from the given location.

> Source: [src/tilemaps/TilemapLayer.js#L994](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/TilemapLayer.js#L994)  
> Since: 3.50.0

---

## renderDebug

### <instance> renderDebug(graphics, [styleConfig])

**Description:**

Draws a debug representation of the layer to the given Graphics. This is helpful when you want to

get a quick idea of which of your tiles are colliding and which have interesting faces. The tiles

are drawn starting at (0, 0) in the Graphics, allowing you to place the debug representation

wherever you want on the screen.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| graphics | [Phaser.GameObjects.Graphics](gameobjects-graphics.md) | No | The target Graphics object to draw upon. |
| --- | --- | --- | --- |
| styleConfig | [Phaser.Types.Tilemaps.StyleConfig](../typedef/types-tilemaps.md) | Yes | An object specifying the colors to use for the debug drawing. |

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This Tilemap Layer object.

> Source: [src/tilemaps/TilemapLayer.js#L1014](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/TilemapLayer.js#L1014)  
> Since: 3.50.0

---

## replaceByIndex

### <instance> replaceByIndex(findIndex, newIndex, [tileX], [tileY], [width], [height])

**Description:**

Scans the given rectangular area (given in tile coordinates) for tiles with an index matching

`findIndex` and updates their index to match `newIndex`. This only modifies the index and does

not change collision information.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| findIndex | number | No | The index of the tile to search for. |
| --- | --- | --- | --- |
| newIndex | number | No | The index of the tile to replace it with. |
| tileX | number | Yes | The left most tile index (in tile coordinates) to use as the origin of the area. |
| tileY | number | Yes | The top most tile index (in tile coordinates) to use as the origin of the area. |
| width | number | Yes | How many tiles wide from the `tileX` index the area will be. |
| height | number | Yes | How many tiles tall from the `tileY` index the area will be. |

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This Tilemap Layer object.

> Source: [src/tilemaps/TilemapLayer.js#L1035](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/TilemapLayer.js#L1035)  
> Since: 3.50.0

---

## resetCollisionCategory

### <instance> resetCollisionCategory()

**Description:**

Resets the Collision Category and Mask back to the defaults,

which is to collide with everything.

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This Game Object.

**Inherits:** [Phaser.Physics.Arcade.Components.Collision#resetCollisionCategory](../namespace/physics-arcade-components-collision.md)

> Source: [src/physics/arcade/components/Collision.js#L130](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/components/Collision.js#L130)  
> Since: 3.70.0

---

## resetFlip

### <instance> resetFlip()

**Description:**

Resets the horizontal and vertical flipped state of this Game Object back to their default un-flipped state.

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Flip#resetFlip](../namespace/gameobjects-components-flip.md)

> Source: [src/gameobjects/components/Flip.js#L140](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Flip.js#L140)  
> Since: 3.0.0

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

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This Game Object instance.

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

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This GameObject.

**Inherits:** [Phaser.GameObjects.GameObject#setActive](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L216](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L216)  
> Since: 3.0.0

---

## setAlpha

### <instance> setAlpha([topLeft], [topRight], [bottomLeft], [bottomRight])

**Description:**

Set the Alpha level of this Game Object. The alpha controls the opacity of the Game Object as it renders.

Alpha values are provided as a float between 0, fully transparent, and 1, fully opaque.

If your game is running under WebGL you can optionally specify four different alpha values, each of which

correspond to the four corners of the Game Object. Under Canvas only the `topLeft` value given is used.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| topLeft | number | Yes | 1 | The alpha value used for the top-left of the Game Object. If this is the only value given it's applied across the whole Game Object. |
| --- | --- | --- | --- | --- |
| topRight | number | Yes |  | The alpha value used for the top-right of the Game Object. WebGL only. |
| bottomLeft | number | Yes |  | The alpha value used for the bottom-left of the Game Object. WebGL only. |
| bottomRight | number | Yes |  | The alpha value used for the bottom-right of the Game Object. WebGL only. |

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Alpha#setAlpha](../namespace/gameobjects-components-alpha.md)

> Source: [src/gameobjects/components/Alpha.js#L92](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Alpha.js#L92)  
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

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This Game Object instance.

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

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This Game Object instance.

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

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.BlendMode#setBlendMode](../namespace/gameobjects-components-blendmode.md)

> Source: [src/gameobjects/components/BlendMode.js#L80](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/BlendMode.js#L80)  
> Since: 3.0.0

---

## setCollidesWith

### <instance> setCollidesWith(categories)

**Description:**

Sets all of the Collision Categories that this Arcade Physics Body

will collide with. You can either pass a single category value, or

an array of them.

Calling this method will reset all of the collision categories,

so only those passed to this method are enabled.

If you wish to add a new category to the existing mask, call

the `addCollisionCategory` method.

If you wish to reset the collision category and mask, call

the `resetCollisionCategory` method.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| categories | number | Array.<number> | No | The collision category to collide with, or an array of them. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This Game Object.

**Inherits:** [Phaser.Physics.Arcade.Components.Collision#setCollidesWith](../namespace/physics-arcade-components-collision.md)

> Source: [src/physics/arcade/components/Collision.js#L100](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/components/Collision.js#L100)  
> Since: 3.70.0

---

## setCollision

### <instance> setCollision(indexes, [collides], [recalculateFaces], [updateLayer])

**Description:**

Sets collision on the given tile or tiles within a layer by index. You can pass in either a

single numeric index or an array of indexes: [2, 3, 15, 20]. The `collides` parameter controls if

collision will be enabled (true) or disabled (false).

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| indexes | number | array | No |  | Either a single tile index, or an array of tile indexes. |
| --- | --- | --- | --- | --- |
| collides | boolean | Yes | true | If true it will enable collision. If false it will clear collision. |
| recalculateFaces | boolean | Yes | true | Whether or not to recalculate the tile faces after the update. |
| updateLayer | boolean | Yes | true | If true, updates the current tiles on the layer. Set to false if no tiles have been placed for significant performance boost. |

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This Tilemap Layer object.

> Source: [src/tilemaps/TilemapLayer.js#L1108](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/TilemapLayer.js#L1108)  
> Since: 3.50.0

---

## setCollisionBetween

### <instance> setCollisionBetween(start, stop, [collides], [recalculateFaces])

**Description:**

Sets collision on a range of tiles in a layer whose index is between the specified `start` and

`stop` (inclusive). Calling this with a start value of 10 and a stop value of 14 would set

collision for tiles 10, 11, 12, 13 and 14. The `collides` parameter controls if collision will be

enabled (true) or disabled (false).

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| start | number | No |  | The first index of the tile to be set for collision. |
| --- | --- | --- | --- | --- |
| stop | number | No |  | The last index of the tile to be set for collision. |
| collides | boolean | Yes | true | If true it will enable collision. If false it will clear collision. |
| recalculateFaces | boolean | Yes | true | Whether or not to recalculate the tile faces after the update. |

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This Tilemap Layer object.

> Source: [src/tilemaps/TilemapLayer.js#L1130](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/TilemapLayer.js#L1130)  
> Since: 3.50.0

---

## setCollisionByExclusion

### <instance> setCollisionByExclusion(indexes, [collides], [recalculateFaces])

**Description:**

Sets collision on all tiles in the given layer, except for tiles that have an index specified in

the given array. The `collides` parameter controls if collision will be enabled (true) or

disabled (false). Tile indexes not currently in the layer are not affected.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| indexes | Array.<number> | No |  | An array of the tile indexes to not be counted for collision. |
| --- | --- | --- | --- | --- |
| collides | boolean | Yes | true | If true it will enable collision. If false it will clear collision. |
| recalculateFaces | boolean | Yes | true | Whether or not to recalculate the tile faces after the update. |

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This Tilemap Layer object.

> Source: [src/tilemaps/TilemapLayer.js#L1178](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/TilemapLayer.js#L1178)  
> Since: 3.50.0

---

## setCollisionByProperty

### <instance> setCollisionByProperty(properties, [collides], [recalculateFaces])

**Description:**

Sets collision on the tiles within a layer by checking tile properties. If a tile has a property

that matches the given properties object, its collision flag will be set. The `collides`

parameter controls if collision will be enabled (true) or disabled (false). Passing in

`{ collides: true }` would update the collision flag on any tiles with a "collides" property that

has a value of true. Any tile that doesn't have "collides" set to true will be ignored. You can

also use an array of values, e.g. `{ types: ["stone", "lava", "sand" ] }`. If a tile has a

"types" property that matches any of those values, its collision flag will be updated.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| properties | object | No |  | An object with tile properties and corresponding values that should be checked. |
| --- | --- | --- | --- | --- |
| collides | boolean | Yes | true | If true it will enable collision. If false it will clear collision. |
| recalculateFaces | boolean | Yes | true | Whether or not to recalculate the tile faces after the update. |

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This Tilemap Layer object.

> Source: [src/tilemaps/TilemapLayer.js#L1153](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/TilemapLayer.js#L1153)  
> Since: 3.50.0

---

## setCollisionCategory

### <instance> setCollisionCategory(category)

**Description:**

Sets the Collision Category that this Arcade Physics Body

will use in order to determine what it can collide with.

It can only have one single category assigned to it.

If you wish to reset the collision category and mask, call

the `resetCollisionCategory` method.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| category | number | No | The collision category. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This Game Object.

**Inherits:** [Phaser.Physics.Arcade.Components.Collision#setCollisionCategory](../namespace/physics-arcade-components-collision.md)

> Source: [src/physics/arcade/components/Collision.js#L17](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/components/Collision.js#L17)  
> Since: 3.70.0

---

## setCollisionFromCollisionGroup

### <instance> setCollisionFromCollisionGroup([collides], [recalculateFaces])

**Description:**

Sets collision on the tiles within a layer by checking each tiles collision group data

(typically defined in Tiled within the tileset collision editor). If any objects are found within

a tiles collision group, the tile's colliding information will be set. The `collides` parameter

controls if collision will be enabled (true) or disabled (false).

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| collides | boolean | Yes | true | If true it will enable collision. If false it will clear collision. |
| --- | --- | --- | --- | --- |
| recalculateFaces | boolean | Yes | true | Whether or not to recalculate the tile faces after the update. |

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This Tilemap Layer object.

> Source: [src/tilemaps/TilemapLayer.js#L1199](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/TilemapLayer.js#L1199)  
> Since: 3.50.0

---

## setCullPadding

### <instance> setCullPadding([paddingX], [paddingY])

**Description:**

When a Camera culls the tiles in this layer it does so using its view into the world, building up a

rectangle inside which the tiles must exist or they will be culled. Sometimes you may need to expand the size

of this 'cull rectangle', especially if you plan on rotating the Camera viewing the layer. Do so

by providing the padding values. The values given are in tiles, not pixels. So if the tile width was 32px

and you set `paddingX` to be 4, it would add 32px x 4 to the cull rectangle (adjusted for scale)

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| paddingX | number | Yes | 1 | The amount of extra horizontal tiles to add to the cull check padding. |
| --- | --- | --- | --- | --- |
| paddingY | number | Yes | 1 | The amount of extra vertical tiles to add to the cull check padding. |

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This Tilemap Layer object.

> Source: [src/tilemaps/TilemapLayer.js#L1082](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/TilemapLayer.js#L1082)  
> Since: 3.50.0

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

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This GameObject.

**Inherits:** [Phaser.GameObjects.GameObject#setData](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L295](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L295)  
> Since: 3.0.0

---

## setDataEnabled

### <instance> setDataEnabled()

**Description:**

Adds a Data Manager component to this Game Object.

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This GameObject.

**Inherits:** [Phaser.GameObjects.GameObject#setDataEnabled](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L276](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L276)  
> Since: 3.0.0

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

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Depth#setDepth](../namespace/gameobjects-components-depth.md)

> Source: [src/gameobjects/components/Depth.js#L64](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Depth.js#L64)  
> Since: 3.0.0

---

## setDisplayOrigin

### <instance> setDisplayOrigin([x], [y])

**Description:**

Sets the display origin of this Game Object.

The difference between this and setting the origin is that you can use pixel values for setting the display origin.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | Yes | 0 | The horizontal display origin value. |
| --- | --- | --- | --- | --- |
| y | number | Yes | "x" | The vertical display origin value. If not defined it will be set to the value of `x`. |

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Origin#setDisplayOrigin](../namespace/gameobjects-components-origin.md)

> Source: [src/gameobjects/components/Origin.js#L159](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Origin.js#L159)  
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

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.ComputedSize#setDisplaySize](../namespace/gameobjects-components-computedsize.md)

> Source: [src/gameobjects/components/ComputedSize.js#L120](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/ComputedSize.js#L120)  
> Since: 3.4.0

---

## setFlip

### <instance> setFlip(x, y)

**Description:**

Sets the horizontal and vertical flipped state of this Game Object.

A Game Object that is flipped will render inversed on the flipped axis.

Flipping always takes place from the middle of the texture and does not impact the scale value.

If this Game Object has a physics body, it will not change the body. This is a rendering toggle only.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | boolean | No | The horizontal flipped state. `false` for no flip, or `true` to be flipped. |
| --- | --- | --- | --- |
| y | boolean | No | The horizontal flipped state. `false` for no flip, or `true` to be flipped. |

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Flip#setFlip](../namespace/gameobjects-components-flip.md)

> Source: [src/gameobjects/components/Flip.js#L117](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Flip.js#L117)  
> Since: 3.0.0

---

## setFlipX

### <instance> setFlipX(value)

**Description:**

Sets the horizontal flipped state of this Game Object.

A Game Object that is flipped horizontally will render inversed on the horizontal axis.

Flipping always takes place from the middle of the texture and does not impact the scale value.

If this Game Object has a physics body, it will not change the body. This is a rendering toggle only.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | boolean | No | The flipped state. `false` for no flip, or `true` to be flipped. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Flip#setFlipX](../namespace/gameobjects-components-flip.md)

> Source: [src/gameobjects/components/Flip.js#L79](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Flip.js#L79)  
> Since: 3.0.0

---

## setFlipY

### <instance> setFlipY(value)

**Description:**

Sets the vertical flipped state of this Game Object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | boolean | No | The flipped state. `false` for no flip, or `true` to be flipped. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Flip#setFlipY](../namespace/gameobjects-components-flip.md)

> Source: [src/gameobjects/components/Flip.js#L100](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Flip.js#L100)  
> Since: 3.0.0

---

## setInteractive

### <instance> setInteractive([hitArea], [callback], [dropZone])

**Description:**

Pass this Game Object to the Input Manager to enable it for Input.

Input works by using hit areas, these are nearly always geometric shapes, such as rectangles or circles, that act as the hit area

for the Game Object. However, you can provide your own hit area shape and callback, should you wish to handle some more advanced

input detection.

If no arguments are provided it will try and create a rectangle hit area based on the texture frame the Game Object is using. If

this isn't a texture-bound object, such as a Graphics or BitmapText object, this will fail, and you'll need to provide a specific

shape for it to use.

You can also provide an Input Configuration Object as the only argument to this method.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| hitArea | [Phaser.Types.Input.InputConfiguration](../typedef/types-input.md) | any | Yes |  | Either an input configuration object, or a geometric shape that defines the hit area for the Game Object. If not given it will try to create a Rectangle based on the texture frame. |
| --- | --- | --- | --- | --- |
| callback | [Phaser.Types.Input.HitAreaCallback](../typedef/types-input.md) | Yes |  | The callback that determines if the pointer is within the Hit Area shape or not. If you provide a shape you must also provide a callback. |
| dropZone | boolean | Yes | false | Should this Game Object be treated as a drop zone target? |

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This GameObject.

**Inherits:** [Phaser.GameObjects.GameObject#setInteractive](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L456](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L456)  
> Since: 3.0.0

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

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This Game Object instance.

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

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This GameObject.

**Inherits:** [Phaser.GameObjects.GameObject#setName](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L234](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L234)  
> Since: 3.0.0

---

## setOrigin

### <instance> setOrigin([x], [y])

**Description:**

Sets the origin of this Game Object.

The values are given in the range 0 to 1.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | Yes | 0.5 | The horizontal origin value. |
| --- | --- | --- | --- | --- |
| y | number | Yes | "x" | The vertical origin value. If not defined it will be set to the value of `x`. |

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Origin#setOrigin](../namespace/gameobjects-components-origin.md)

> Source: [src/gameobjects/components/Origin.js#L112](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Origin.js#L112)  
> Since: 3.0.0

---

## setOriginFromFrame

### <instance> setOriginFromFrame()

**Description:**

Sets the origin of this Game Object based on the Pivot values in its Frame.

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Origin#setOriginFromFrame](../namespace/gameobjects-components-origin.md)

> Source: [src/gameobjects/components/Origin.js#L136](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Origin.js#L136)  
> Since: 3.0.0

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

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This Game Object instance.

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

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This Game Object instance.

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

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This Game Object instance.

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

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This Game Object instance.

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

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This Game Object instance.

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

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Transform#setRandomPosition](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L313](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L313)  
> Since: 3.8.0

---

## setRenderOrder

### <instance> setRenderOrder(renderOrder)

**Description:**

Sets the rendering (draw) order of the tiles in this layer.

The default is 'right-down', meaning it will order the tiles starting from the top-left,

drawing to the right and then moving down to the next row.

The draw orders are:

0 = right-down

1 = left-down

2 = right-up

3 = left-up

Setting the render order does not change the tiles or how they are stored in the layer,

it purely impacts the order in which they are rendered.

You can provide either an integer (0 to 3), or the string version of the order.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| renderOrder | number | string | No | The render (draw) order value. Either an integer between 0 and 3, or a string: 'right-down', 'left-down', 'right-up' or 'left-up'. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This Tilemap Layer object.

> Source: [src/tilemaps/TilemapLayer.js#L388](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/TilemapLayer.js#L388)  
> Since: 3.50.0

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

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This Game Object instance.

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

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This Game Object instance.

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

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This Game Object instance.

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

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.ComputedSize#setSize](../namespace/gameobjects-components-computedsize.md)

> Source: [src/gameobjects/components/ComputedSize.js#L93](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/ComputedSize.js#L93)  
> Since: 3.4.0

---

## setSkipCull

### <instance> setSkipCull([value])

**Description:**

You can control if the Cameras should cull tiles before rendering them or not.

By default the camera will try to cull the tiles in this layer, to avoid over-drawing to the renderer.

However, there are some instances when you may wish to disable this.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| value | boolean | Yes | true | Set to `true` to stop culling tiles. Set to `false` to enable culling again. |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This Tilemap Layer object.

> Source: [src/tilemaps/TilemapLayer.js#L1059](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/TilemapLayer.js#L1059)  
> Since: 3.50.0

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

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This GameObject.

**Inherits:** [Phaser.GameObjects.GameObject#setState](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L252](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L252)  
> Since: 3.16.0

---

## setTileIndexCallback

### <instance> setTileIndexCallback(indexes, callback, callbackContext)

**Description:**

Sets a global collision callback for the given tile index within the layer. This will affect all

tiles on this layer that have the same index. If a callback is already set for the tile index it

will be replaced. Set the callback to null to remove it. If you want to set a callback for a tile

at a specific location on the map then see setTileLocationCallback.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| indexes | number | Array.<number> | No | Either a single tile index, or an array of tile indexes to have a collision callback set for. |
| --- | --- | --- | --- |
| callback | function | No | The callback that will be invoked when the tile is collided with. |
| callbackContext | object | No | The context under which the callback is called. |

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This Tilemap Layer object.

> Source: [src/tilemaps/TilemapLayer.js#L1220](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/TilemapLayer.js#L1220)  
> Since: 3.50.0

---

## setTileLocationCallback

### <instance> setTileLocationCallback([tileX], [tileY], [width], [height], [callback], [callbackContext])

**Description:**

Sets a collision callback for the given rectangular area (in tile coordinates) within the layer.

If a callback is already set for the tile index it will be replaced. Set the callback to null to

remove it.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tileX | number | Yes | The left most tile index (in tile coordinates) to use as the origin of the area. |
| --- | --- | --- | --- |
| tileY | number | Yes | The top most tile index (in tile coordinates) to use as the origin of the area. |
| width | number | Yes | How many tiles wide from the `tileX` index the area will be. |
| height | number | Yes | How many tiles tall from the `tileY` index the area will be. |
| callback | function | Yes | The callback that will be invoked when the tile is collided with. |
| callbackContext | object | Yes | The context, or scope, under which the callback is invoked. |

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This Tilemap Layer object.

> Source: [src/tilemaps/TilemapLayer.js#L1242](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/TilemapLayer.js#L1242)  
> Since: 3.50.0

---

## setTint

### <instance> setTint([tint], [tileX], [tileY], [width], [height], [filteringOptions])

**Description:**

Sets an additive tint on each Tile within the given area.

The tint works by taking the pixel color values from the tileset texture, and then

multiplying it by the color value of the tint.

If no area values are given then all tiles will be tinted to the given color.

To remove a tint call this method with either no parameters, or by passing white `0xffffff` as the tint color.

If a tile already has a tint set then calling this method will override that.

**Tags:**

* webglOnly

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| tint | number | Yes | "0xffffff" | The tint color being applied to each tile within the region. Given as a hex value, i.e. `0xff0000` for red. Set to white (`0xffffff`) to reset the tint. |
| --- | --- | --- | --- | --- |
| tileX | number | Yes |  | The left most tile index (in tile coordinates) to use as the origin of the area to search. |
| tileY | number | Yes |  | The top most tile index (in tile coordinates) to use as the origin of the area to search. |
| width | number | Yes |  | How many tiles wide from the `tileX` index the area will be. |
| height | number | Yes |  | How many tiles tall from the `tileY` index the area will be. |
| filteringOptions | [Phaser.Types.Tilemaps.FilteringOptions](../typedef/types-tilemaps.md) | Yes |  | Optional filters to apply when getting the tiles. |

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This Tilemap Layer object.

> Source: [src/tilemaps/TilemapLayer.js#L655](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/TilemapLayer.js#L655)  
> Since: 3.60.0

---

## setTintFill

### <instance> setTintFill([tint], [tileX], [tileY], [width], [height], [filteringOptions])

**Description:**

Sets a fill-based tint on each Tile within the given area.

Unlike an additive tint, a fill-tint literally replaces the pixel colors from the texture

with those in the tint.

If no area values are given then all tiles will be tinted to the given color.

To remove a tint call this method with either no parameters, or by passing white `0xffffff` as the tint color.

If a tile already has a tint set then calling this method will override that.

**Tags:**

* webglOnly

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| tint | number | Yes | "0xffffff" | The tint color being applied to each tile within the region. Given as a hex value, i.e. `0xff0000` for red. Set to white (`0xffffff`) to reset the tint. |
| --- | --- | --- | --- | --- |
| tileX | number | Yes |  | The left most tile index (in tile coordinates) to use as the origin of the area to search. |
| tileY | number | Yes |  | The top most tile index (in tile coordinates) to use as the origin of the area to search. |
| width | number | Yes |  | How many tiles wide from the `tileX` index the area will be. |
| height | number | Yes |  | How many tiles tall from the `tileY` index the area will be. |
| filteringOptions | [Phaser.Types.Tilemaps.FilteringOptions](../typedef/types-tilemaps.md) | Yes |  | Optional filters to apply when getting the tiles. |

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This Tilemap Layer object.

> Source: [src/tilemaps/TilemapLayer.js#L693](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/TilemapLayer.js#L693)  
> Since: 3.70.0

---

## setToBack

### <instance> setToBack()

**Description:**

Sets this Game Object to the back of the display list, or the back of its parent container.

Being at the back means it will render below everything else.

This method does not change this Game Objects `depth` value, it simply alters its list position.

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This Game Object instance.

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

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Depth#setToTop](../namespace/gameobjects-components-depth.md)

> Source: [src/gameobjects/components/Depth.js#L91](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Depth.js#L91)  
> Since: 3.85.0

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

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This Game Object instance.

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

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This Game Object instance.

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

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This Game Object instance.

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

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This Game Object instance.

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

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Transform#setZ](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L443](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L443)  
> Since: 3.0.0

---

## shuffle

### <instance> shuffle([tileX], [tileY], [width], [height])

**Description:**

Shuffles the tiles in a rectangular region (specified in tile coordinates) within the given

layer. It will only randomize the tiles in that area, so if they're all the same nothing will

appear to have changed! This method only modifies tile indexes and does not change collision

information.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tileX | number | Yes | The left most tile index (in tile coordinates) to use as the origin of the area. |
| --- | --- | --- | --- |
| tileY | number | Yes | The top most tile index (in tile coordinates) to use as the origin of the area. |
| width | number | Yes | How many tiles wide from the `tileX` index the area will be. |
| height | number | Yes | How many tiles tall from the `tileY` index the area will be. |

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This Tilemap Layer object.

> Source: [src/tilemaps/TilemapLayer.js#L1266](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/TilemapLayer.js#L1266)  
> Since: 3.50.0

---

## shutdown

### <instance> shutdown()

**Description:**

Removes all listeners.

**Inherits:** [Phaser.Events.EventEmitter#shutdown](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L31](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L31)  
> Since: 3.0.0

---

## swapByIndex

### <instance> swapByIndex(tileA, tileB, [tileX], [tileY], [width], [height])

**Description:**

Scans the given rectangular area (given in tile coordinates) for tiles with an index matching

`indexA` and swaps then with `indexB`. This only modifies the index and does not change collision

information.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tileA | number | No | First tile index. |
| --- | --- | --- | --- |
| tileB | number | No | Second tile index. |
| tileX | number | Yes | The left most tile index (in tile coordinates) to use as the origin of the area. |
| tileY | number | Yes | The top most tile index (in tile coordinates) to use as the origin of the area. |
| width | number | Yes | How many tiles wide from the `tileX` index the area will be. |
| height | number | Yes | How many tiles tall from the `tileY` index the area will be. |

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This Tilemap Layer object.

> Source: [src/tilemaps/TilemapLayer.js#L1289](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/TilemapLayer.js#L1289)  
> Since: 3.50.0

---

## tileToWorldX

### <instance> tileToWorldX(tileX, [camera])

**Description:**

Converts from tile X coordinates (tile units) to world X coordinates (pixels), factoring in the

layers position, scale and scroll.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tileX | number | No | The x coordinate, in tiles, not pixels. |
| --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | Yes | The Camera to use when calculating the tile index from the world values. |

**Returns:** number - The Tile X coordinate converted to pixels.

> Source: [src/tilemaps/TilemapLayer.js#L1313](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/TilemapLayer.js#L1313)  
> Since: 3.50.0

---

## tileToWorldXY

### <instance> tileToWorldXY(tileX, tileY, [point], [camera])

**Description:**

Converts from tile XY coordinates (tile units) to world XY coordinates (pixels), factoring in the

layers position, scale and scroll. This will return a new Vector2 object or update the given

`point` object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tileX | number | No | The x coordinate, in tiles, not pixels. |
| --- | --- | --- | --- |
| tileY | number | No | The y coordinate, in tiles, not pixels. |
| point | [Phaser.Math.Vector2](math-vector2.md) | Yes | A Vector2 to store the coordinates in. If not given a new Vector2 is created. |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | Yes | The Camera to use when calculating the tile index from the world values. |

**Returns:** [Phaser.Math.Vector2](math-vector2.md) - A Vector2 containing the world coordinates of the Tile.

> Source: [src/tilemaps/TilemapLayer.js#L1347](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/TilemapLayer.js#L1347)  
> Since: 3.50.0

---

## tileToWorldY

### <instance> tileToWorldY(tileY, [camera])

**Description:**

Converts from tile Y coordinates (tile units) to world Y coordinates (pixels), factoring in the

layers position, scale and scroll.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tileY | number | No | The y coordinate, in tiles, not pixels. |
| --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | Yes | The Camera to use when calculating the tile index from the world values. |

**Returns:** number - The Tile Y coordinate converted to pixels.

> Source: [src/tilemaps/TilemapLayer.js#L1330](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/TilemapLayer.js#L1330)  
> Since: 3.50.0

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

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This GameObject.

**Inherits:** [Phaser.GameObjects.GameObject#toggleData](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L387](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L387)  
> Since: 3.23.0

---

## toggleFlipX

### <instance> toggleFlipX()

**Description:**

Toggles the horizontal flipped state of this Game Object.

A Game Object that is flipped horizontally will render inversed on the horizontal axis.

Flipping always takes place from the middle of the texture and does not impact the scale value.

If this Game Object has a physics body, it will not change the body. This is a rendering toggle only.

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Flip#toggleFlipX](../namespace/gameobjects-components-flip.md)

> Source: [src/gameobjects/components/Flip.js#L45](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Flip.js#L45)  
> Since: 3.0.0

---

## toggleFlipY

### <instance> toggleFlipY()

**Description:**

Toggles the vertical flipped state of this Game Object.

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Flip#toggleFlipY](../namespace/gameobjects-components-flip.md)

> Source: [src/gameobjects/components/Flip.js#L64](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Flip.js#L64)  
> Since: 3.0.0

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

## updateDisplayOrigin

### <instance> updateDisplayOrigin()

**Description:**

Updates the Display Origin cached values internally stored on this Game Object.

You don't usually call this directly, but it is exposed for edge-cases where you may.

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Origin#updateDisplayOrigin](../namespace/gameobjects-components-origin.md)

> Source: [src/gameobjects/components/Origin.js#L182](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Origin.js#L182)  
> Since: 3.0.0

---

## weightedRandomize

### <instance> weightedRandomize(weightedIndexes, [tileX], [tileY], [width], [height])

**Description:**

Randomizes the indexes of a rectangular region of tiles (in tile coordinates) within the

specified layer. Each tile will receive a new index. New indexes are drawn from the given

weightedIndexes array. An example weighted array:

[

{ index: 6, weight: 4 }, // Probability of index 6 is 4 / 8

{ index: 7, weight: 2 }, // Probability of index 7 would be 2 / 8

{ index: 8, weight: 1.5 }, // Probability of index 8 would be 1.5 / 8

{ index: 26, weight: 0.5 } // Probability of index 27 would be 0.5 / 8

]

The probability of any index being choose is (the index's weight) / (sum of all weights). This

method only modifies tile indexes and does not change collision information.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| weightedIndexes | Array.<object> | No | An array of objects to randomly draw from during randomization. They should be in the form: { index: 0, weight: 4 } or { index: [0, 1], weight: 4 } if you wish to draw from multiple tile indexes. |
| --- | --- | --- | --- |
| tileX | number | Yes | The left most tile index (in tile coordinates) to use as the origin of the area. |
| tileY | number | Yes | The top most tile index (in tile coordinates) to use as the origin of the area. |
| width | number | Yes | How many tiles wide from the `tileX` index the area will be. |
| height | number | Yes | How many tiles tall from the `tileY` index the area will be. |

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - This Tilemap Layer object.

> Source: [src/tilemaps/TilemapLayer.js#L1393](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/TilemapLayer.js#L1393)  
> Since: 3.50.0

---

## willCollideWith

### <instance> willCollideWith(category)

**Description:**

Checks to see if the given Collision Category will collide with

this Arcade Physics object or not.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| category | number | No | Collision category value to test. |
| --- | --- | --- | --- |

**Returns:** boolean - `true` if the given category will collide with this object, otherwise `false`.

**Inherits:** [Phaser.Physics.Arcade.Components.Collision#willCollideWith](../namespace/physics-arcade-components-collision.md)

> Source: [src/physics/arcade/components/Collision.js#L42](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/components/Collision.js#L42)  
> Since: 3.70.0

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

## worldToTileX

### <instance> worldToTileX(worldX, [snapToFloor], [camera])

**Description:**

Converts from world X coordinates (pixels) to tile X coordinates (tile units), factoring in the

layers position, scale and scroll.

You cannot call this method for Isometric or Hexagonal tilemaps as they require

both `worldX` and `worldY` values to determine the correct tile, instead you

should use the `worldToTileXY` method.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| worldX | number | No | The x coordinate to be converted, in pixels, not tiles. |
| --- | --- | --- | --- |
| snapToFloor | boolean | Yes | Whether or not to round the tile coordinate down to the nearest integer. |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | Yes | The Camera to use when calculating the tile index from the world values. |

**Returns:** number - The tile X coordinate based on the world value.

> Source: [src/tilemaps/TilemapLayer.js#L1426](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/TilemapLayer.js#L1426)  
> Since: 3.50.0

---

## worldToTileXY

### <instance> worldToTileXY(worldX, worldY, [snapToFloor], [point], [camera])

**Description:**

Converts from world XY coordinates (pixels) to tile XY coordinates (tile units), factoring in the

layers position, scale and scroll. This will return a new Vector2 object or update the given

`point` object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| worldX | number | No | The x coordinate to be converted, in pixels, not tiles. |
| --- | --- | --- | --- |
| worldY | number | No | The y coordinate to be converted, in pixels, not tiles. |
| snapToFloor | boolean | Yes | Whether or not to round the tile coordinate down to the nearest integer. |
| point | [Phaser.Math.Vector2](math-vector2.md) | Yes | A Vector2 to store the coordinates in. If not given a new Vector2 is created. |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | Yes | The Camera to use when calculating the tile index from the world values. |

**Returns:** [Phaser.Math.Vector2](math-vector2.md) - A Vector2 containing the tile coordinates of the world values.

> Source: [src/tilemaps/TilemapLayer.js#L1470](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/TilemapLayer.js#L1470)  
> Since: 3.50.0

---

## worldToTileY

### <instance> worldToTileY(worldY, [snapToFloor], [camera])

**Description:**

Converts from world Y coordinates (pixels) to tile Y coordinates (tile units), factoring in the

layers position, scale and scroll.

You cannot call this method for Isometric or Hexagonal tilemaps as they require

both `worldX` and `worldY` values to determine the correct tile, instead you

should use the `worldToTileXY` method.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| worldY | number | No | The y coordinate to be converted, in pixels, not tiles. |
| --- | --- | --- | --- |
| snapToFloor | boolean | Yes | Whether or not to round the tile coordinate down to the nearest integer. |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | Yes | The Camera to use when calculating the tile index from the world values. |

**Returns:** number - The tile Y coordinate based on the world value.

> Source: [src/tilemaps/TilemapLayer.js#L1448](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/TilemapLayer.js#L1448)  
> Since: 3.50.0

---

# Private Methods

## prepareBoundsOutput

### <instance> prepareBoundsOutput(output, [includeParent])

**Description:**

Processes the bounds output vector before returning it.

**Tags:**

* generic

**Access:** private

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| output | [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) | No |  | An object to store the values in. If not provided a new Vector2 will be created. |
| --- | --- | --- | --- | --- |
| includeParent | boolean | Yes | false | If this Game Object has a parent Container, include it (and all other ancestors) in the resulting vector? |

**Returns:** [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) - The values stored in the output object.

**Inherits:** [Phaser.GameObjects.Components.GetBounds#prepareBoundsOutput](../namespace/gameobjects-components-getbounds.md)

> Source: [src/gameobjects/components/GetBounds.js#L21](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/GetBounds.js#L21)  
> Since: 3.18.0

---

## renderCanvas

### <instance> renderCanvas(renderer, src, camera, parentMatrix)

**Description:**

Renders this Game Object with the Canvas Renderer to the given Camera.

The object will not render if any of its renderFlags are set or it is being actively filtered out by the Camera.

This method should not be called directly. It is a utility function of the Render module.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| renderer | [Phaser.Renderer.Canvas.CanvasRenderer](renderer-canvas-canvasrenderer.md) | No | A reference to the current active Canvas renderer. |
| --- | --- | --- | --- |
| src | [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) | No | The Game Object being rendered in this call. |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | No | The Camera that is rendering the Game Object. |
| parentMatrix | [Phaser.GameObjects.Components.TransformMatrix](gameobjects-components-transformmatrix.md) | No | This transform matrix is defined if the game object is nested |

> Source: [src/tilemaps/TilemapLayerCanvasRenderer.js#L13](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/TilemapLayerCanvasRenderer.js#L13)  
> Since: 3.50.0

---

## renderWebGL

### <instance> renderWebGL(renderer, src, camera)

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
| src | [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) | No | The Game Object being rendered in this call. |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | No | The Camera that is rendering the Game Object. |

> Source: [src/tilemaps/TilemapLayerWebGLRenderer.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/TilemapLayerWebGLRenderer.js#L9)  
> Since: 3.0.0

---

## setTilesets

### <instance> setTilesets(tileset)

**Description:**

Populates the internal `tileset` array with the Tileset references this Layer requires for rendering.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tileset | string | Array.<string> | [Phaser.Tilemaps.Tileset](tilemaps-tileset.md) | Array.<[Phaser.Tilemaps.Tileset](tilemaps-tileset.md)> |
| --- | --- | --- | --- |

> Source: [src/tilemaps/TilemapLayer.js#L342](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/TilemapLayer.js#L342)  
> Since: 3.50.0

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
  + [alphaBottomLeft](#alphabottomleft)

    - [alphaBottomLeft: number](#alphabottomleft-number)
  + [alphaBottomRight](#alphabottomright)

    - [alphaBottomRight: number](#alphabottomright-number)
  + [alphaTopLeft](#alphatopleft)

    - [alphaTopLeft: number](#alphatopleft-number)
  + [alphaTopRight](#alphatopright)

    - [alphaTopRight: number](#alphatopright-number)
  + [angle](#angle)

    - [angle: number](#angle-number)
  + [blendMode](#blendmode)

    - [blendMode: Phaser.BlendModes, string, number](#blendmode-phaserblendmodes-string-number)
  + [body](#body)

    - [body: Phaser.Physics.Arcade.Body, Phaser.Physics.Arcade.StaticBody, MatterJS.BodyType](#body-phaserphysicsarcadebody-phaserphysicsarcadestaticbody-matterjsbodytype)
  + [cameraFilter](#camerafilter)

    - [cameraFilter: number](#camerafilter-number)
  + [collisionCategory](#collisioncategory)

    - [collisionCategory: number](#collisioncategory-number)
  + [collisionMask](#collisionmask)

    - [collisionMask: number](#collisionmask-number)
  + [cullCallback](#cullcallback)

    - [cullCallback: function](#cullcallback-function)
  + [culledTiles](#culledtiles)

    - [culledTiles: Array.<Phaser.Tilemaps.Tile>](#culledtiles-arrayphasertilemapstile)
  + [cullPaddingX](#cullpaddingx)

    - [cullPaddingX: number](#cullpaddingx-number)
  + [cullPaddingY](#cullpaddingy)

    - [cullPaddingY: number](#cullpaddingy-number)
  + [data](#data)

    - [data: Phaser.Data.DataManager](#data-phaserdatadatamanager)
  + [defaultPipeline](#defaultpipeline)

    - [defaultPipeline: Phaser.Renderer.WebGL.WebGLPipeline](#defaultpipeline-phaserrendererwebglwebglpipeline)
  + [depth](#depth)

    - [depth: number](#depth-number)
  + [displayHeight](#displayheight)

    - [displayHeight: number](#displayheight-number)
  + [displayList](#displaylist)

    - [displayList: Phaser.GameObjects.DisplayList, Phaser.GameObjects.Layer](#displaylist-phasergameobjectsdisplaylist-phasergameobjectslayer)
  + [displayOriginX](#displayoriginx)

    - [displayOriginX: number](#displayoriginx-number)
  + [displayOriginY](#displayoriginy)

    - [displayOriginY: number](#displayoriginy-number)
  + [displayWidth](#displaywidth)

    - [displayWidth: number](#displaywidth-number)
  + [flipX](#flipx)

    - [flipX: boolean](#flipx-boolean)
  + [flipY](#flipy)

    - [flipY: boolean](#flipy-boolean)
  + [gidMap](#gidmap)

    - [gidMap: Array.<Phaser.Tilemaps.Tileset>](#gidmap-arrayphasertilemapstileset)
  + [hasPostPipeline](#haspostpipeline)

    - [hasPostPipeline: boolean](#haspostpipeline-boolean)
  + [hasTransformComponent](#hastransformcomponent)

    - [hasTransformComponent: boolean](#hastransformcomponent-boolean)
  + [height](#height)

    - [height: number](#height-number)
  + [ignoreDestroy](#ignoredestroy)

    - [ignoreDestroy: boolean](#ignoredestroy-boolean)
  + [input](#input)

    - [input: Phaser.Types.Input.InteractiveObject](#input-phasertypesinputinteractiveobject)
  + [isTilemap](#istilemap)

    - [isTilemap: boolean](#istilemap-boolean)
  + [layer](#layer)

    - [layer: Phaser.Tilemaps.LayerData](#layer-phasertilemapslayerdata)
  + [layerIndex](#layerindex)

    - [layerIndex: number](#layerindex-number)
  + [mask](#mask)

    - [mask: Phaser.Display.Masks.BitmapMask, Phaser.Display.Masks.GeometryMask](#mask-phaserdisplaymasksbitmapmask-phaserdisplaymasksgeometrymask)
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
  + [skipCull](#skipcull)

    - [skipCull: boolean](#skipcull-boolean)
  + [state](#state)

    - [state: number, string](#state-number-string)
  + [tabIndex](#tabindex)

    - [tabIndex: number](#tabindex-number)
  + [tilemap](#tilemap)

    - [tilemap: Phaser.Tilemaps.Tilemap](#tilemap-phasertilemapstilemap)
  + [tilesDrawn](#tilesdrawn)

    - [tilesDrawn: number](#tilesdrawn-number)
  + [tileset](#tileset)

    - [tileset: Array.<Phaser.Tilemaps.Tileset>](#tileset-arrayphasertilemapstileset)
  + [tilesTotal](#tilestotal)

    - [tilesTotal: number](#tilestotal-number)
  + [type](#type)

    - [type: string](#type-string)
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
  + [\_alphaBL](#_alphabl)

    - [\_alphaBL: number](#_alphabl-number)
  + [\_alphaBR](#_alphabr)

    - [\_alphaBR: number](#_alphabr-number)
  + [\_alphaTL](#_alphatl)

    - [\_alphaTL: number](#_alphatl-number)
  + [\_alphaTR](#_alphatr)

    - [\_alphaTR: number](#_alphatr-number)
  + [\_blendMode](#_blendmode)

    - [\_blendMode: number](#_blendmode-number)
  + [\_depth](#_depth)

    - [\_depth: number](#_depth-number)
  + [\_originComponent](#_origincomponent)

    - [\_originComponent: boolean](#_origincomponent-boolean)
  + [\_renderOrder](#_renderorder)

    - [\_renderOrder: number](#_renderorder-number)
  + [\_rotation](#_rotation)

    - [\_rotation: number](#_rotation-number)
  + [\_scaleX](#_scalex)

    - [\_scaleX: number](#_scalex-number)
  + [\_scaleY](#_scaley)

    - [\_scaleY: number](#_scaley-number)
  + [\_visible](#_visible)

    - [\_visible: boolean](#_visible-boolean)
  + [tempVec](#tempvec)

    - [tempVec: Phaser.Math.Vector2](#tempvec-phasermathvector2)
* [Public Methods](#public-methods)

  + [addCollidesWith](#addcollideswith)

    - [<instance> addCollidesWith(category)](#instance-addcollideswithcategory)
  + [addedToScene](#addedtoscene)

    - [<instance> addedToScene()](#instance-addedtoscene)
  + [addListener](#addlistener)

    - [<instance> addListener(event, fn, [context])](#instance-addlistenerevent-fn-context)
  + [addToDisplayList](#addtodisplaylist)

    - [<instance> addToDisplayList([displayList])](#instance-addtodisplaylistdisplaylist)
  + [addToUpdateList](#addtoupdatelist)

    - [<instance> addToUpdateList()](#instance-addtoupdatelist)
  + [calculateFacesAt](#calculatefacesat)

    - [<instance> calculateFacesAt(tileX, tileY)](#instance-calculatefacesattilex-tiley)
  + [calculateFacesWithin](#calculatefaceswithin)

    - [<instance> calculateFacesWithin([tileX], [tileY], [width], [height])](#instance-calculatefaceswithintilex-tiley-width-height)
  + [clearAlpha](#clearalpha)

    - [<instance> clearAlpha()](#instance-clearalpha)
  + [clearFX](#clearfx)

    - [<instance> clearFX()](#instance-clearfx)
  + [clearMask](#clearmask)

    - [<instance> clearMask([destroyMask])](#instance-clearmaskdestroymask)
  + [copy](#copy)

    - [<instance> copy(srcTileX, srcTileY, width, height, destTileX, destTileY, [recalculateFaces])](#instance-copysrctilex-srctiley-width-height-desttilex-desttiley-recalculatefaces)
  + [copyPosition](#copyposition)

    - [<instance> copyPosition(source)](#instance-copypositionsource)
  + [createBitmapMask](#createbitmapmask)

    - [<instance> createBitmapMask([maskObject], [x], [y], [texture], [frame])](#instance-createbitmapmaskmaskobject-x-y-texture-frame)
  + [createFromTiles](#createfromtiles)

    - [<instance> createFromTiles(indexes, replacements, [spriteConfig], [scene], [camera])](#instance-createfromtilesindexes-replacements-spriteconfig-scene-camera)
  + [createGeometryMask](#creategeometrymask)

    - [<instance> createGeometryMask([graphics])](#instance-creategeometrymaskgraphics)
  + [cull](#cull)

    - [<instance> cull([camera])](#instance-cullcamera)
  + [destroy](#destroy)

    - [<instance> destroy([removeFromTilemap])](#instance-destroyremovefromtilemap)
  + [disableInteractive](#disableinteractive)

    - [<instance> disableInteractive([resetCursor])](#instance-disableinteractiveresetcursor)
  + [emit](#emit)

    - [<instance> emit(event, [args])](#instance-emitevent-args)
  + [eventNames](#eventnames)

    - [<instance> eventNames()](#instance-eventnames)
  + [fill](#fill)

    - [<instance> fill(index, [tileX], [tileY], [width], [height], [recalculateFaces])](#instance-fillindex-tilex-tiley-width-height-recalculatefaces)
  + [filterTiles](#filtertiles)

    - [<instance> filterTiles(callback, [context], [tileX], [tileY], [width], [height], [filteringOptions])](#instance-filtertilescallback-context-tilex-tiley-width-height-filteringoptions)
  + [findByIndex](#findbyindex)

    - [<instance> findByIndex(index, [skip], [reverse])](#instance-findbyindexindex-skip-reverse)
  + [findTile](#findtile)

    - [<instance> findTile(callback, [context], [tileX], [tileY], [width], [height], [filteringOptions])](#instance-findtilecallback-context-tilex-tiley-width-height-filteringoptions)
  + [forEachTile](#foreachtile)

    - [<instance> forEachTile(callback, [context], [tileX], [tileY], [width], [height], [filteringOptions])](#instance-foreachtilecallback-context-tilex-tiley-width-height-filteringoptions)
  + [getBottomCenter](#getbottomcenter)

    - [<instance> getBottomCenter([output], [includeParent])](#instance-getbottomcenteroutput-includeparent)
  + [getBottomLeft](#getbottomleft)

    - [<instance> getBottomLeft([output], [includeParent])](#instance-getbottomleftoutput-includeparent)
  + [getBottomRight](#getbottomright)

    - [<instance> getBottomRight([output], [includeParent])](#instance-getbottomrightoutput-includeparent)
  + [getBounds](#getbounds)

    - [<instance> getBounds([output])](#instance-getboundsoutput)
  + [getCenter](#getcenter)

    - [<instance> getCenter([output], [includeParent])](#instance-getcenteroutput-includeparent)
  + [getData](#getdata)

    - [<instance> getData(key)](#instance-getdatakey)
  + [getDisplayList](#getdisplaylist)

    - [<instance> getDisplayList()](#instance-getdisplaylist)
  + [getIndexList](#getindexlist)

    - [<instance> getIndexList()](#instance-getindexlist)
  + [getIsoTileAtWorldXY](#getisotileatworldxy)

    - [<instance> getIsoTileAtWorldXY(worldX, worldY, [originTop], [nonNull], [camera])](#instance-getisotileatworldxyworldx-worldy-origintop-nonnull-camera)
  + [getLeftCenter](#getleftcenter)

    - [<instance> getLeftCenter([output], [includeParent])](#instance-getleftcenteroutput-includeparent)
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
  + [getRightCenter](#getrightcenter)

    - [<instance> getRightCenter([output], [includeParent])](#instance-getrightcenteroutput-includeparent)
  + [getTileAt](#gettileat)

    - [<instance> getTileAt(tileX, tileY, [nonNull])](#instance-gettileattilex-tiley-nonnull)
  + [getTileAtWorldXY](#gettileatworldxy)

    - [<instance> getTileAtWorldXY(worldX, worldY, [nonNull], [camera])](#instance-gettileatworldxyworldx-worldy-nonnull-camera)
  + [getTileCorners](#gettilecorners)

    - [<instance> getTileCorners(tileX, tileY, [camera])](#instance-gettilecornerstilex-tiley-camera)
  + [getTilesWithin](#gettileswithin)

    - [<instance> getTilesWithin([tileX], [tileY], [width], [height], [filteringOptions])](#instance-gettileswithintilex-tiley-width-height-filteringoptions)
  + [getTilesWithinShape](#gettileswithinshape)

    - [<instance> getTilesWithinShape(shape, [filteringOptions], [camera])](#instance-gettileswithinshapeshape-filteringoptions-camera)
  + [getTilesWithinWorldXY](#gettileswithinworldxy)

    - [<instance> getTilesWithinWorldXY(worldX, worldY, width, height, [filteringOptions], [camera])](#instance-gettileswithinworldxyworldx-worldy-width-height-filteringoptions-camera)
  + [getTopCenter](#gettopcenter)

    - [<instance> getTopCenter([output], [includeParent])](#instance-gettopcenteroutput-includeparent)
  + [getTopLeft](#gettopleft)

    - [<instance> getTopLeft([output], [includeParent])](#instance-gettopleftoutput-includeparent)
  + [getTopRight](#gettopright)

    - [<instance> getTopRight([output], [includeParent])](#instance-gettoprightoutput-includeparent)
  + [getWorldTransformMatrix](#getworldtransformmatrix)

    - [<instance> getWorldTransformMatrix([tempMatrix], [parentMatrix])](#instance-getworldtransformmatrixtempmatrix-parentmatrix)
  + [hasTileAt](#hastileat)

    - [<instance> hasTileAt(tileX, tileY)](#instance-hastileattilex-tiley)
  + [hasTileAtWorldXY](#hastileatworldxy)

    - [<instance> hasTileAtWorldXY(worldX, worldY, [camera])](#instance-hastileatworldxyworldx-worldy-camera)
  + [incData](#incdata)

    - [<instance> incData(key, [amount])](#instance-incdatakey-amount)
  + [initPipeline](#initpipeline)

    - [<instance> initPipeline([pipeline])](#instance-initpipelinepipeline)
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
  + [putTileAt](#puttileat)

    - [<instance> putTileAt(tile, tileX, tileY, [recalculateFaces])](#instance-puttileattile-tilex-tiley-recalculatefaces)
  + [putTileAtWorldXY](#puttileatworldxy)

    - [<instance> putTileAtWorldXY(tile, worldX, worldY, [recalculateFaces], [camera])](#instance-puttileatworldxytile-worldx-worldy-recalculatefaces-camera)
  + [putTilesAt](#puttilesat)

    - [<instance> putTilesAt(tile, tileX, tileY, [recalculateFaces])](#instance-puttilesattile-tilex-tiley-recalculatefaces)
  + [randomize](#randomize)

    - [<instance> randomize([tileX], [tileY], [width], [height], [indexes])](#instance-randomizetilex-tiley-width-height-indexes)
  + [removeAllListeners](#removealllisteners)

    - [<instance> removeAllListeners([event])](#instance-removealllistenersevent)
  + [removeCollidesWith](#removecollideswith)

    - [<instance> removeCollidesWith(category)](#instance-removecollideswithcategory)
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
  + [removeTileAt](#removetileat)

    - [<instance> removeTileAt(tileX, tileY, [replaceWithNull], [recalculateFaces])](#instance-removetileattilex-tiley-replacewithnull-recalculatefaces)
  + [removeTileAtWorldXY](#removetileatworldxy)

    - [<instance> removeTileAtWorldXY(worldX, worldY, [replaceWithNull], [recalculateFaces], [camera])](#instance-removetileatworldxyworldx-worldy-replacewithnull-recalculatefaces-camera)
  + [renderDebug](#renderdebug)

    - [<instance> renderDebug(graphics, [styleConfig])](#instance-renderdebuggraphics-styleconfig)
  + [replaceByIndex](#replacebyindex)

    - [<instance> replaceByIndex(findIndex, newIndex, [tileX], [tileY], [width], [height])](#instance-replacebyindexfindindex-newindex-tilex-tiley-width-height)
  + [resetCollisionCategory](#resetcollisioncategory)

    - [<instance> resetCollisionCategory()](#instance-resetcollisioncategory)
  + [resetFlip](#resetflip)

    - [<instance> resetFlip()](#instance-resetflip)
  + [resetPipeline](#resetpipeline)

    - [<instance> resetPipeline([resetData])](#instance-resetpipelineresetdata)
  + [resetPostPipeline](#resetpostpipeline)

    - [<instance> resetPostPipeline([resetData])](#instance-resetpostpipelineresetdata)
  + [setAbove](#setabove)

    - [<instance> setAbove(gameObject)](#instance-setabovegameobject)
  + [setActive](#setactive)

    - [<instance> setActive(value)](#instance-setactivevalue)
  + [setAlpha](#setalpha)

    - [<instance> setAlpha([topLeft], [topRight], [bottomLeft], [bottomRight])](#instance-setalphatopleft-topright-bottomleft-bottomright)
  + [setAngle](#setangle)

    - [<instance> setAngle([degrees])](#instance-setangledegrees)
  + [setBelow](#setbelow)

    - [<instance> setBelow(gameObject)](#instance-setbelowgameobject)
  + [setBlendMode](#setblendmode)

    - [<instance> setBlendMode(value)](#instance-setblendmodevalue)
  + [setCollidesWith](#setcollideswith)

    - [<instance> setCollidesWith(categories)](#instance-setcollideswithcategories)
  + [setCollision](#setcollision)

    - [<instance> setCollision(indexes, [collides], [recalculateFaces], [updateLayer])](#instance-setcollisionindexes-collides-recalculatefaces-updatelayer)
  + [setCollisionBetween](#setcollisionbetween)

    - [<instance> setCollisionBetween(start, stop, [collides], [recalculateFaces])](#instance-setcollisionbetweenstart-stop-collides-recalculatefaces)
  + [setCollisionByExclusion](#setcollisionbyexclusion)

    - [<instance> setCollisionByExclusion(indexes, [collides], [recalculateFaces])](#instance-setcollisionbyexclusionindexes-collides-recalculatefaces)
  + [setCollisionByProperty](#setcollisionbyproperty)

    - [<instance> setCollisionByProperty(properties, [collides], [recalculateFaces])](#instance-setcollisionbypropertyproperties-collides-recalculatefaces)
  + [setCollisionCategory](#setcollisioncategory)

    - [<instance> setCollisionCategory(category)](#instance-setcollisioncategorycategory)
  + [setCollisionFromCollisionGroup](#setcollisionfromcollisiongroup)

    - [<instance> setCollisionFromCollisionGroup([collides], [recalculateFaces])](#instance-setcollisionfromcollisiongroupcollides-recalculatefaces)
  + [setCullPadding](#setcullpadding)

    - [<instance> setCullPadding([paddingX], [paddingY])](#instance-setcullpaddingpaddingx-paddingy)
  + [setData](#setdata)

    - [<instance> setData(key, [data])](#instance-setdatakey-data)
  + [setDataEnabled](#setdataenabled)

    - [<instance> setDataEnabled()](#instance-setdataenabled)
  + [setDepth](#setdepth)

    - [<instance> setDepth(value)](#instance-setdepthvalue)
  + [setDisplayOrigin](#setdisplayorigin)

    - [<instance> setDisplayOrigin([x], [y])](#instance-setdisplayoriginx-y)
  + [setDisplaySize](#setdisplaysize)

    - [<instance> setDisplaySize(width, height)](#instance-setdisplaysizewidth-height)
  + [setFlip](#setflip)

    - [<instance> setFlip(x, y)](#instance-setflipx-y)
  + [setFlipX](#setflipx)

    - [<instance> setFlipX(value)](#instance-setflipxvalue)
  + [setFlipY](#setflipy)

    - [<instance> setFlipY(value)](#instance-setflipyvalue)
  + [setInteractive](#setinteractive)

    - [<instance> setInteractive([hitArea], [callback], [dropZone])](#instance-setinteractivehitarea-callback-dropzone)
  + [setMask](#setmask)

    - [<instance> setMask(mask)](#instance-setmaskmask)
  + [setName](#setname)

    - [<instance> setName(value)](#instance-setnamevalue)
  + [setOrigin](#setorigin)

    - [<instance> setOrigin([x], [y])](#instance-setoriginx-y)
  + [setOriginFromFrame](#setoriginfromframe)

    - [<instance> setOriginFromFrame()](#instance-setoriginfromframe)
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
  + [setRenderOrder](#setrenderorder)

    - [<instance> setRenderOrder(renderOrder)](#instance-setrenderorderrenderorder)
  + [setRotation](#setrotation)

    - [<instance> setRotation([radians])](#instance-setrotationradians)
  + [setScale](#setscale)

    - [<instance> setScale([x], [y])](#instance-setscalex-y)
  + [setScrollFactor](#setscrollfactor)

    - [<instance> setScrollFactor(x, [y])](#instance-setscrollfactorx-y)
  + [setSize](#setsize)

    - [<instance> setSize(width, height)](#instance-setsizewidth-height)
  + [setSkipCull](#setskipcull)

    - [<instance> setSkipCull([value])](#instance-setskipcullvalue)
  + [setState](#setstate)

    - [<instance> setState(value)](#instance-setstatevalue)
  + [setTileIndexCallback](#settileindexcallback)

    - [<instance> setTileIndexCallback(indexes, callback, callbackContext)](#instance-settileindexcallbackindexes-callback-callbackcontext)
  + [setTileLocationCallback](#settilelocationcallback)

    - [<instance> setTileLocationCallback([tileX], [tileY], [width], [height], [callback], [callbackContext])](#instance-settilelocationcallbacktilex-tiley-width-height-callback-callbackcontext)
  + [setTint](#settint)

    - [<instance> setTint([tint], [tileX], [tileY], [width], [height], [filteringOptions])](#instance-settinttint-tilex-tiley-width-height-filteringoptions)
  + [setTintFill](#settintfill)

    - [<instance> setTintFill([tint], [tileX], [tileY], [width], [height], [filteringOptions])](#instance-settintfilltint-tilex-tiley-width-height-filteringoptions)
  + [setToBack](#settoback)

    - [<instance> setToBack()](#instance-settoback)
  + [setToTop](#settotop)

    - [<instance> setToTop()](#instance-settotop)
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
  + [shuffle](#shuffle)

    - [<instance> shuffle([tileX], [tileY], [width], [height])](#instance-shuffletilex-tiley-width-height)
  + [shutdown](#shutdown)

    - [<instance> shutdown()](#instance-shutdown)
  + [swapByIndex](#swapbyindex)

    - [<instance> swapByIndex(tileA, tileB, [tileX], [tileY], [width], [height])](#instance-swapbyindextilea-tileb-tilex-tiley-width-height)
  + [tileToWorldX](#tiletoworldx)

    - [<instance> tileToWorldX(tileX, [camera])](#instance-tiletoworldxtilex-camera)
  + [tileToWorldXY](#tiletoworldxy)

    - [<instance> tileToWorldXY(tileX, tileY, [point], [camera])](#instance-tiletoworldxytilex-tiley-point-camera)
  + [tileToWorldY](#tiletoworldy)

    - [<instance> tileToWorldY(tileY, [camera])](#instance-tiletoworldytiley-camera)
  + [toggleData](#toggledata)

    - [<instance> toggleData(key)](#instance-toggledatakey)
  + [toggleFlipX](#toggleflipx)

    - [<instance> toggleFlipX()](#instance-toggleflipx)
  + [toggleFlipY](#toggleflipy)

    - [<instance> toggleFlipY()](#instance-toggleflipy)
  + [toJSON](#tojson)

    - [<instance> toJSON()](#instance-tojson)
  + [update](#update)

    - [<instance> update([args])](#instance-updateargs)
  + [updateDisplayOrigin](#updatedisplayorigin)

    - [<instance> updateDisplayOrigin()](#instance-updatedisplayorigin)
  + [weightedRandomize](#weightedrandomize)

    - [<instance> weightedRandomize(weightedIndexes, [tileX], [tileY], [width], [height])](#instance-weightedrandomizeweightedindexes-tilex-tiley-width-height)
  + [willCollideWith](#willcollidewith)

    - [<instance> willCollideWith(category)](#instance-willcollidewithcategory)
  + [willRender](#willrender)

    - [<instance> willRender(camera)](#instance-willrendercamera)
  + [worldToTileX](#worldtotilex)

    - [<instance> worldToTileX(worldX, [snapToFloor], [camera])](#instance-worldtotilexworldx-snaptofloor-camera)
  + [worldToTileXY](#worldtotilexy)

    - [<instance> worldToTileXY(worldX, worldY, [snapToFloor], [point], [camera])](#instance-worldtotilexyworldx-worldy-snaptofloor-point-camera)
  + [worldToTileY](#worldtotiley)

    - [<instance> worldToTileY(worldY, [snapToFloor], [camera])](#instance-worldtotileyworldy-snaptofloor-camera)
* [Private Methods](#private-methods)

  + [prepareBoundsOutput](#prepareboundsoutput)

    - [<instance> prepareBoundsOutput(output, [includeParent])](#instance-prepareboundsoutputoutput-includeparent)
  + [renderCanvas](#rendercanvas)

    - [<instance> renderCanvas(renderer, src, camera, parentMatrix)](#instance-rendercanvasrenderer-src-camera-parentmatrix)
  + [renderWebGL](#renderwebgl)

    - [<instance> renderWebGL(renderer, src, camera)](#instance-renderwebglrenderer-src-camera)
  + [setTilesets](#settilesets)

    - [<instance> setTilesets(tileset)](#instance-settilesetstileset)

Back to top

©2025[Phaser](https://docs.phaser.io)