# PipelineManager

Phaser.Renderer.WebGL.PipelineManager

The Pipeline Manager is responsible for the creation, activation, running and destruction

of WebGL Pipelines and Post FX Pipelines in Phaser 3.

The `WebGLRenderer` owns a single instance of the Pipeline Manager, which you can access

via the `WebGLRenderer.pipelines` property.

By default, there are 9 pipelines installed into the Pipeline Manager when Phaser boots:

1. The Multi Pipeline. Responsible for all multi-texture rendering, i.e. Sprites and Tilemaps.
2. The Rope Pipeline. Responsible for rendering the Rope Game Object.
3. The Light Pipeline. Responsible for rendering the Light Game Object.
4. The Point Light Pipeline. Responsible for rendering the Point Light Game Object.
5. The Single Pipeline. Responsible for rendering Game Objects that explicitly require one bound texture.
6. The Bitmap Mask Pipeline. Responsible for Bitmap Mask rendering.
7. The Utility Pipeline. Responsible for providing lots of handy texture manipulation functions.
8. The Mobile Pipeline. Responsible for rendering on mobile with single-bound textures.
9. The FX Pipeline. Responsible for rendering Game Objects with special FX applied to them.

You can add your own custom pipeline via the `PipelineManager.add` method. Pipelines are

identified by unique string-based keys.

**Constructor**

`new PipelineManager(renderer)`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| renderer | [Phaser.Renderer.WebGL.WebGLRenderer](renderer-webgl-webglrenderer.md) | No | A reference to the WebGL Renderer that owns this Pipeline Manager. |
| --- | --- | --- | --- |

---

**Scope**: static

> Source: [src/renderer/webgl/PipelineManager.js#L30](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/PipelineManager.js#L30)  
> Since: 3.50.0

# Public Members

## BITMAPMASK\_PIPELINE

### BITMAPMASK\_PIPELINE: [Phaser.Renderer.WebGL.Pipelines.BitmapMaskPipeline](renderer-webgl-pipelines-bitmapmaskpipeline.md)

**Description:**

A constant-style reference to the Bitmap Mask Pipeline Instance.

This is the default Phaser 3 mask pipeline and is used Game Objects using

a Bitmap Mask. This property is set during the `boot` method.

> Source: [src/renderer/webgl/PipelineManager.js#L201](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/PipelineManager.js#L201)  
> Since: 3.50.0

---

## classes

### classes: Phaser.Structs.Map.<string, Class>

**Description:**

This map stores all pipeline classes available in this manager.

The Utility Class must always come first.

> Source: [src/renderer/webgl/PipelineManager.js#L84](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/PipelineManager.js#L84)  
> Since: 3.50.0

---

## current

### current: [Phaser.Renderer.WebGL.WebGLPipeline](renderer-webgl-webglpipeline.md)

**Description:**

Current pipeline in use by the WebGLRenderer.

> Source: [src/renderer/webgl/PipelineManager.js#L166](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/PipelineManager.js#L166)  
> Since: 3.50.0

---

## default

### default: [Phaser.Renderer.WebGL.WebGLPipeline](renderer-webgl-webglpipeline.md)

**Description:**

The default Game Object pipeline.

> Source: [src/renderer/webgl/PipelineManager.js#L156](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/PipelineManager.js#L156)  
> Since: 3.60.0

---

## frameInc

### frameInc: number

**Description:**

The amount in which each target frame will increase.

Defaults to 32px but can be overridden in the config.

> Source: [src/renderer/webgl/PipelineManager.js#L332](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/PipelineManager.js#L332)  
> Since: 3.60.0

---

## fullFrame1

### fullFrame1: [Phaser.Renderer.WebGL.RenderTarget](renderer-webgl-rendertarget.md)

**Description:**

A reference to the Full Frame 1 Render Target that belongs to the

Utility Pipeline. This property is set during the `boot` method.

This Render Target is the full size of the renderer.

You can use this directly in Post FX Pipelines for multi-target effects.

However, be aware that these targets are shared between all post fx pipelines.

> Source: [src/renderer/webgl/PipelineManager.js#L250](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/PipelineManager.js#L250)  
> Since: 3.50.0

---

## fullFrame2

### fullFrame2: [Phaser.Renderer.WebGL.RenderTarget](renderer-webgl-rendertarget.md)

**Description:**

A reference to the Full Frame 2 Render Target that belongs to the

Utility Pipeline. This property is set during the `boot` method.

This Render Target is the full size of the renderer.

You can use this directly in Post FX Pipelines for multi-target effects.

However, be aware that these targets are shared between all post fx pipelines.

> Source: [src/renderer/webgl/PipelineManager.js#L266](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/PipelineManager.js#L266)  
> Since: 3.50.0

---

## FX\_PIPELINE

### FX\_PIPELINE: [Phaser.Renderer.WebGL.Pipelines.FXPipeline](renderer-webgl-pipelines-fxpipeline.md)

**Description:**

A constant-style reference to the FX Pipeline Instance.

This is the default Phaser 3 FX pipeline and is used by the WebGL Renderer to manage

Game Objects with special effects enabled. This property is set during the `boot` method.

> Source: [src/renderer/webgl/PipelineManager.js#L237](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/PipelineManager.js#L237)  
> Since: 3.60.0

---

## game

### game: [Phaser.Game](game.md)

**Description:**

A reference to the Game instance.

> Source: [src/renderer/webgl/PipelineManager.js#L66](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/PipelineManager.js#L66)  
> Since: 3.50.0

---

## halfFrame1

### halfFrame1: [Phaser.Renderer.WebGL.RenderTarget](renderer-webgl-rendertarget.md)

**Description:**

A reference to the Half Frame 1 Render Target that belongs to the

Utility Pipeline. This property is set during the `boot` method.

This Render Target is half the size of the renderer.

You can use this directly in Post FX Pipelines for multi-target effects.

However, be aware that these targets are shared between all post fx pipelines.

> Source: [src/renderer/webgl/PipelineManager.js#L282](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/PipelineManager.js#L282)  
> Since: 3.50.0

---

## halfFrame2

### halfFrame2: [Phaser.Renderer.WebGL.RenderTarget](renderer-webgl-rendertarget.md)

**Description:**

A reference to the Half Frame 2 Render Target that belongs to the

Utility Pipeline. This property is set during the `boot` method.

This Render Target is half the size of the renderer.

You can use this directly in Post FX Pipelines for multi-target effects.

However, be aware that these targets are shared between all post fx pipelines.

> Source: [src/renderer/webgl/PipelineManager.js#L298](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/PipelineManager.js#L298)  
> Since: 3.50.0

---

## maxDimension

### maxDimension: number

**Description:**

The largest render target dimension before we just use a full-screen target.

> Source: [src/renderer/webgl/PipelineManager.js#L323](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/PipelineManager.js#L323)  
> Since: 3.60.0

---

## MOBILE\_PIPELINE

### MOBILE\_PIPELINE: [Phaser.Renderer.WebGL.Pipelines.MobilePipeline](renderer-webgl-pipelines-mobilepipeline.md)

**Description:**

A constant-style reference to the Mobile Pipeline Instance.

This is the default Phaser 3 mobile pipeline and is used by the WebGL Renderer to manage

camera effects and more on mobile devices. This property is set during the `boot` method.

> Source: [src/renderer/webgl/PipelineManager.js#L224](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/PipelineManager.js#L224)  
> Since: 3.60.0

---

## MULTI\_PIPELINE

### MULTI\_PIPELINE: [Phaser.Renderer.WebGL.Pipelines.MultiPipeline](renderer-webgl-pipelines-multipipeline.md)

**Description:**

A constant-style reference to the Multi Pipeline Instance.

This is the default Phaser 3 pipeline and is used by the WebGL Renderer to manage

camera effects and more. This property is set during the `boot` method.

> Source: [src/renderer/webgl/PipelineManager.js#L188](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/PipelineManager.js#L188)  
> Since: 3.50.0

---

## pipelines

### pipelines: Phaser.Structs.Map.<string, [Phaser.Renderer.WebGL.WebGLPipeline](renderer-webgl-webglpipeline.md)>

**Description:**

This map stores all pipeline instances in this manager.

This is populated with the default pipelines in the `boot` method.

> Source: [src/renderer/webgl/PipelineManager.js#L137](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/PipelineManager.js#L137)  
> Since: 3.50.0

---

## postPipelineClasses

### postPipelineClasses: Phaser.Structs.Map.<string, Class>

**Description:**

This map stores all Post FX Pipeline classes available in this manager.

As of v3.60 this is now populated by default with the following

Post FX Pipelines:

* Barrel
* Bloom
* Blur
* Bokeh / TiltShift
* Circle
* ColorMatrix
* Displacement
* Glow
* Gradient
* Pixelate
* Shadow
* Shine
* Vignette
* Wipe

These are added as part of the boot process.

If you do not wish to add them, specify `disableFX: true` in your game config.

See the FX Controller class for more details about each FX.

> Source: [src/renderer/webgl/PipelineManager.js#L104](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/PipelineManager.js#L104)  
> Since: 3.50.0

---

## postPipelineInstances

### postPipelineInstances: Array.<[Phaser.Renderer.WebGL.Pipelines.PostFXPipeline](renderer-webgl-pipelines-postfxpipeline.md)>

**Description:**

An array of all post-pipelines that are created by this manager.

> Source: [src/renderer/webgl/PipelineManager.js#L148](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/PipelineManager.js#L148)

---

## previous

### previous: [Phaser.Renderer.WebGL.WebGLPipeline](renderer-webgl-webglpipeline.md)

**Description:**

The previous WebGLPipeline that was in use.

This is set when `clearPipeline` is called and restored in `rebindPipeline` if none is given.

> Source: [src/renderer/webgl/PipelineManager.js#L176](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/PipelineManager.js#L176)  
> Since: 3.50.0

---

## renderer

### renderer: [Phaser.Renderer.WebGL.WebGLRenderer](renderer-webgl-webglrenderer.md)

**Description:**

A reference to the WebGL Renderer instance.

> Source: [src/renderer/webgl/PipelineManager.js#L75](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/PipelineManager.js#L75)  
> Since: 3.50.0

---

## renderTargets

### renderTargets: Array.<[Phaser.Renderer.WebGL.RenderTarget](renderer-webgl-rendertarget.md)>

**Description:**

An array of RenderTarget instances that belong to this pipeline.

> Source: [src/renderer/webgl/PipelineManager.js#L314](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/PipelineManager.js#L314)  
> Since: 3.60.0

---

## targetIndex

### targetIndex: number

**Description:**

The Render Target index. Used internally by the methods

in this class. Do not modify directly.

> Source: [src/renderer/webgl/PipelineManager.js#L343](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/PipelineManager.js#L343)  
> Since: 3.60.0

---

## UTILITY\_PIPELINE

### UTILITY\_PIPELINE: [Phaser.Renderer.WebGL.Pipelines.UtilityPipeline](renderer-webgl-pipelines-utilitypipeline.md)

**Description:**

A constant-style reference to the Utility Pipeline Instance.

> Source: [src/renderer/webgl/PipelineManager.js#L214](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/PipelineManager.js#L214)  
> Since: 3.50.0

---

# Public Methods

## add

### <instance> add(name, pipeline)

**Description:**

Adds a pipeline instance to this Pipeline Manager.

The name of the instance must be unique within this manager.

Make sure to pass an instance to this method, not a base class.

For example, you should pass it like this:

```
Copy
this.add('yourName', new CustomPipeline(game));`


```

and **not** like this:

```
Copy
this.add('yourName', CustomPipeline);`


```

To add a **Post Pipeline**, see `addPostPipeline` instead.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| name | string | No | A unique string-based key for the pipeline within the manager. |
| --- | --- | --- | --- |
| pipeline | [Phaser.Renderer.WebGL.WebGLPipeline](renderer-webgl-webglpipeline.md) | No | A pipeline *instance* which must extend `WebGLPipeline`. |

**Returns:** [Phaser.Renderer.WebGL.WebGLPipeline](renderer-webgl-webglpipeline.md) - The pipeline instance that was passed.

> Source: [src/renderer/webgl/PipelineManager.js#L532](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/PipelineManager.js#L532)  
> Since: 3.50.0

---

## addPostPipeline

### <instance> addPostPipeline(name, pipeline)

**Description:**

Adds a Post Pipeline to this Pipeline Manager.

Make sure to pass a base class to this method, not an instance.

For example, you should pass it like this:

```
Copy
this.addPostPipeline('yourName', CustomPipeline);`


```

and **not** like this:

```
Copy
this.addPostPipeline('yourName', new CustomPipeline());`


```

To add a regular pipeline, see the `add` method instead.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| name | string | No | A unique string-based key for the pipeline within the manager. |
| --- | --- | --- | --- |
| pipeline | function | No | A pipeline class which must extend `PostFXPipeline`. |

**Returns:** [Phaser.Renderer.WebGL.PipelineManager](renderer-webgl-pipelinemanager.md) - This Pipeline Manager.

> Source: [src/renderer/webgl/PipelineManager.js#L598](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/PipelineManager.js#L598)  
> Since: 3.50.0

---

## blendFrames

### <instance> blendFrames(source1, source2, [target], [strength], [clearAlpha])

**Description:**

Draws the `source1` and `source2` Render Targets to the `target` Render Target

using a linear blend effect, which is controlled by the `strength` parameter.

The draw itself is handled by the Utility Pipeline.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| source1 | [Phaser.Renderer.WebGL.RenderTarget](renderer-webgl-rendertarget.md) | No |  | The first source Render Target. |
| --- | --- | --- | --- | --- |
| source2 | [Phaser.Renderer.WebGL.RenderTarget](renderer-webgl-rendertarget.md) | No |  | The second source Render Target. |
| target | [Phaser.Renderer.WebGL.RenderTarget](renderer-webgl-rendertarget.md) | Yes |  | The target Render Target. |
| strength | number | Yes | 1 | The strength of the blend. |
| clearAlpha | boolean | Yes | true | Clear the alpha channel when running `gl.clear` on the target? |

**Returns:** [Phaser.Renderer.WebGL.PipelineManager](renderer-webgl-pipelinemanager.md) - This Pipeline Manager instance.

> Source: [src/renderer/webgl/PipelineManager.js#L1099](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/PipelineManager.js#L1099)  
> Since: 3.50.0

---

## blendFramesAdditive

### <instance> blendFramesAdditive(source1, source2, [target], [strength], [clearAlpha])

**Description:**

Draws the `source1` and `source2` Render Targets to the `target` Render Target

using an additive blend effect, which is controlled by the `strength` parameter.

The draw itself is handled by the Utility Pipeline.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| source1 | [Phaser.Renderer.WebGL.RenderTarget](renderer-webgl-rendertarget.md) | No |  | The first source Render Target. |
| --- | --- | --- | --- | --- |
| source2 | [Phaser.Renderer.WebGL.RenderTarget](renderer-webgl-rendertarget.md) | No |  | The second source Render Target. |
| target | [Phaser.Renderer.WebGL.RenderTarget](renderer-webgl-rendertarget.md) | Yes |  | The target Render Target. |
| strength | number | Yes | 1 | The strength of the blend. |
| clearAlpha | boolean | Yes | true | Clear the alpha channel when running `gl.clear` on the target? |

**Returns:** [Phaser.Renderer.WebGL.PipelineManager](renderer-webgl-pipelinemanager.md) - This Pipeline Manager instance.

> Source: [src/renderer/webgl/PipelineManager.js#L1123](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/PipelineManager.js#L1123)  
> Since: 3.50.0

---

## blitFrame

### <instance> blitFrame(source, target, [brightness], [clear], [clearAlpha], [eraseMode])

**Description:**

Copy the `source` Render Target to the `target` Render Target.

The difference with this copy is that no resizing takes place. If the `source`

Render Target is larger than the `target` then only a portion the same size as

the `target` dimensions is copied across.

You can optionally set the brightness factor of the copy.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| source | [Phaser.Renderer.WebGL.RenderTarget](renderer-webgl-rendertarget.md) | No |  | The source Render Target. |
| --- | --- | --- | --- | --- |
| target | [Phaser.Renderer.WebGL.RenderTarget](renderer-webgl-rendertarget.md) | No |  | The target Render Target. |
| brightness | number | Yes | 1 | The brightness value applied to the frame copy. |
| clear | boolean | Yes | true | Clear the target before copying? |
| clearAlpha | boolean | Yes | true | Clear the alpha channel when running `gl.clear` on the target? |
| eraseMode | boolean | Yes | false | Erase source from target using ERASE Blend Mode? |

**Returns:** [Phaser.Renderer.WebGL.PipelineManager](renderer-webgl-pipelinemanager.md) - This Pipeline Manager instance.

> Source: [src/renderer/webgl/PipelineManager.js#L1165](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/PipelineManager.js#L1165)  
> Since: 3.50.0

---

## boot

### <instance> boot(pipelineConfig, defaultPipeline, autoMobilePipeline)

**Description:**

Internal boot handler, called by the WebGLRenderer durings its boot process.

Adds all of the default pipelines, based on the game config, and then calls

the `boot` method on each one of them.

Finally, the default pipeline is set.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pipelineConfig | [Phaser.Types.Core.PipelineConfig](../typedef/types-core.md) | No | The pipeline configuration object as set in the Game Config. |
| --- | --- | --- | --- |
| defaultPipeline | string | No | The name of the default Game Object pipeline, as set in the Game Config |
| autoMobilePipeline | boolean | No | Automatically set the default pipeline to mobile if non-desktop detected? |

> Source: [src/renderer/webgl/PipelineManager.js#L354](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/PipelineManager.js#L354)  
> Since: 3.50.0

---

## clear

### <instance> clear()

**Description:**

Flushes the current pipeline being used and then clears it, along with the

the current shader program and vertex buffer from the `WebGLRenderer`.

Then resets the blend mode to NORMAL.

Call this before jumping to your own gl context handler, and then call `rebind` when

you wish to return control to Phaser again.

> Source: [src/renderer/webgl/PipelineManager.js#L1373](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/PipelineManager.js#L1373)  
> Since: 3.50.0

---

## clearFrame

### <instance> clearFrame(target, [clearAlpha])

**Description:**

Clears the given Render Target.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| target | [Phaser.Renderer.WebGL.RenderTarget](renderer-webgl-rendertarget.md) | No |  | The Render Target to clear. |
| --- | --- | --- | --- | --- |
| clearAlpha | boolean | Yes | true | Clear the alpha channel when running `gl.clear` on the target? |

**Returns:** [Phaser.Renderer.WebGL.PipelineManager](renderer-webgl-pipelinemanager.md) - This Pipeline Manager instance.

> Source: [src/renderer/webgl/PipelineManager.js#L1147](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/PipelineManager.js#L1147)  
> Since: 3.50.0

---

## copyFrame

### <instance> copyFrame(source, [target], [brightness], [clear], [clearAlpha])

**Description:**

Copy the `source` Render Target to the `target` Render Target.

You can optionally set the brightness factor of the copy.

The difference between this method and `drawFrame` is that this method

uses a faster copy shader, where only the brightness can be modified.

If you need color level manipulation, see `drawFrame` instead.

The copy itself is handled by the Utility Pipeline.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| source | [Phaser.Renderer.WebGL.RenderTarget](renderer-webgl-rendertarget.md) | No |  | The source Render Target. |
| --- | --- | --- | --- | --- |
| target | [Phaser.Renderer.WebGL.RenderTarget](renderer-webgl-rendertarget.md) | Yes |  | The target Render Target. |
| brightness | number | Yes | 1 | The brightness value applied to the frame copy. |
| clear | boolean | Yes | true | Clear the target before copying? |
| clearAlpha | boolean | Yes | true | Clear the alpha channel when running `gl.clear` on the target? |

**Returns:** [Phaser.Renderer.WebGL.PipelineManager](renderer-webgl-pipelinemanager.md) - This Pipeline Manager instance.

> Source: [src/renderer/webgl/PipelineManager.js#L1020](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/PipelineManager.js#L1020)  
> Since: 3.50.0

---

## copyFrameRect

### <instance> copyFrameRect(source, target, x, y, width, height, [clear], [clearAlpha])

**Description:**

Binds the `source` Render Target and then copies a section of it to the `target` Render Target.

This method is extremely fast because it uses `gl.copyTexSubImage2D` and doesn't

require the use of any shaders. Remember the coordinates are given in standard WebGL format,

where x and y specify the lower-left corner of the section, not the top-left. Also, the

copy entirely replaces the contents of the target texture, no 'merging' or 'blending' takes

place.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| source | [Phaser.Renderer.WebGL.RenderTarget](renderer-webgl-rendertarget.md) | No |  | The source Render Target. |
| --- | --- | --- | --- | --- |
| target | [Phaser.Renderer.WebGL.RenderTarget](renderer-webgl-rendertarget.md) | No |  | The target Render Target. |
| x | number | No |  | The x coordinate of the lower left corner where to start copying. |
| y | number | No |  | The y coordinate of the lower left corner where to start copying. |
| width | number | No |  | The width of the texture. |
| height | number | No |  | The height of the texture. |
| clear | boolean | Yes | true | Clear the target before copying? |
| clearAlpha | boolean | Yes | true | Clear the alpha channel when running `gl.clear` on the target? |

**Returns:** [Phaser.Renderer.WebGL.PipelineManager](renderer-webgl-pipelinemanager.md) - This Pipeline Manager instance.

> Source: [src/renderer/webgl/PipelineManager.js#L1193](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/PipelineManager.js#L1193)  
> Since: 3.50.0

---

## copyToGame

### <instance> copyToGame(source)

**Description:**

Pops the framebuffer from the renderers FBO stack and sets that as the active target,

then draws the `source` Render Target to it. It then resets the renderer textures.

This should be done when you need to draw the *final* results of a pipeline to the game

canvas, or the next framebuffer in line on the FBO stack. You should only call this once

in the `onDraw` handler and it should be the final thing called. Be careful not to call

this if you need to actually use the pipeline shader, instead of the copy shader. In

those cases, use the `bindAndDraw` method.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| source | [Phaser.Renderer.WebGL.RenderTarget](renderer-webgl-rendertarget.md) | No | The Render Target to draw from. |
| --- | --- | --- | --- |

> Source: [src/renderer/webgl/PipelineManager.js#L1049](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/PipelineManager.js#L1049)  
> Since: 3.50.0

---

## destroy

### <instance> destroy()

**Description:**

Destroy the Pipeline Manager, cleaning up all related resources and references.

> Source: [src/renderer/webgl/PipelineManager.js#L1479](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/PipelineManager.js#L1479)  
> Since: 3.50.0

---

## drawFrame

### <instance> drawFrame(source, [target], [clearAlpha], [colorMatrix])

**Description:**

Copy the `source` Render Target to the `target` Render Target, using the

given Color Matrix.

The difference between this method and `copyFrame` is that this method

uses a color matrix shader, where you have full control over the luminance

values used during the copy. If you don't need this, you can use the faster

`copyFrame` method instead.

The copy itself is handled by the Utility Pipeline.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| source | [Phaser.Renderer.WebGL.RenderTarget](renderer-webgl-rendertarget.md) | No |  | The source Render Target. |
| --- | --- | --- | --- | --- |
| target | [Phaser.Renderer.WebGL.RenderTarget](renderer-webgl-rendertarget.md) | Yes |  | The target Render Target. |
| clearAlpha | boolean | Yes | true | Clear the alpha channel when running `gl.clear` on the target? |
| colorMatrix | [Phaser.Display.ColorMatrix](display-colormatrix.md) | Yes |  | The Color Matrix to use when performing the draw. |

**Returns:** [Phaser.Renderer.WebGL.PipelineManager](renderer-webgl-pipelinemanager.md) - This Pipeline Manager instance.

> Source: [src/renderer/webgl/PipelineManager.js#L1071](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/PipelineManager.js#L1071)  
> Since: 3.50.0

---

## flush

### <instance> flush()

**Description:**

Flushes the current pipeline, if one is bound.

> Source: [src/renderer/webgl/PipelineManager.js#L633](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/PipelineManager.js#L633)  
> Since: 3.50.0

---

## forceZero

### <instance> forceZero()

**Description:**

Returns `true` if the current pipeline is forced to use texture unit zero.

**Returns:** boolean - `true` if the current pipeline is forced to use texture unit zero.

> Source: [src/renderer/webgl/PipelineManager.js#L1223](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/PipelineManager.js#L1223)  
> Since: 3.50.0

---

## get

### <instance> get(pipeline)

**Description:**

Returns the pipeline instance based on the given name, or instance.

If no instance, or matching name, exists in this manager, it returns `undefined`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pipeline | string | [Phaser.Renderer.WebGL.WebGLPipeline](renderer-webgl-webglpipeline.md) | No | Either the string-based name of the pipeline to get, or a pipeline instance to look-up. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Renderer.WebGL.WebGLPipeline](renderer-webgl-webglpipeline.md) - The pipeline instance, or `undefined` if not found.

> Source: [src/renderer/webgl/PipelineManager.js#L673](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/PipelineManager.js#L673)  
> Since: 3.50.0

---

## getAltSwapRenderTarget

### <instance> getAltSwapRenderTarget()

**Description:**

Gets a matching Render Target, the same size as the one the Sprite was drawn to,

useful for double-buffer style effects such as blurs.

**Returns:** [Phaser.Renderer.WebGL.RenderTarget](renderer-webgl-rendertarget.md) - The Render Target swap frame.

> Source: [src/renderer/webgl/PipelineManager.js#L1465](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/PipelineManager.js#L1465)  
> Since: 3.60.0

---

## getPostPipeline

### <instance> getPostPipeline(pipeline, [gameObject], [config])

**Description:**

Returns a *new instance* of the post pipeline based on the given name, or class.

If no instance, or matching name, exists in this manager, it returns `undefined`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pipeline | string | function | [Phaser.Renderer.WebGL.Pipelines.PostFXPipeline](renderer-webgl-pipelines-postfxpipeline.md) | No |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | Yes | If this post pipeline is being installed into a Game Object or Camera, this is a reference to it. |
| config | object | Yes | Optional pipeline data object that is set in to the `postPipelineData` property of this Game Object. |

**Returns:** [Phaser.Renderer.WebGL.Pipelines.PostFXPipeline](renderer-webgl-pipelines-postfxpipeline.md) - The pipeline instance, or `undefined` if not found.

> Source: [src/renderer/webgl/PipelineManager.js#L699](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/PipelineManager.js#L699)  
> Since: 3.50.0

---

## getRenderTarget

### <instance> getRenderTarget(size)

**Description:**

Gets a Render Target the right size to render the Sprite on.

If the Sprite exceeds the size of the renderer, the Render Target will only ever be the maximum

size of the renderer.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| size | number | No | The maximum dimension required. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Renderer.WebGL.RenderTarget](renderer-webgl-rendertarget.md) - A Render Target large enough to fit the sprite.

> Source: [src/renderer/webgl/PipelineManager.js#L1414](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/PipelineManager.js#L1414)  
> Since: 3.60.0

---

## getSwapRenderTarget

### <instance> getSwapRenderTarget()

**Description:**

Gets a matching Render Target, the same size as the one the Sprite was drawn to,

useful for double-buffer style effects such as blurs.

**Returns:** [Phaser.Renderer.WebGL.RenderTarget](renderer-webgl-rendertarget.md) - The Render Target swap frame.

> Source: [src/renderer/webgl/PipelineManager.js#L1451](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/PipelineManager.js#L1451)  
> Since: 3.60.0

---

## has

### <instance> has(pipeline)

**Description:**

Checks if a pipeline is present in this Pipeline Manager.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pipeline | string | [Phaser.Renderer.WebGL.WebGLPipeline](renderer-webgl-webglpipeline.md) | No | Either the string-based name of the pipeline to get, or a pipeline instance to look-up. |
| --- | --- | --- | --- |

**Returns:** boolean - `true` if the given pipeline is loaded, otherwise `false`.

> Source: [src/renderer/webgl/PipelineManager.js#L647](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/PipelineManager.js#L647)  
> Since: 3.50.0

---

## isCurrent

### <instance> isCurrent(pipeline, [currentShader])

**Description:**

Checks to see if the given pipeline is already the active pipeline, both within this

Pipeline Manager and also has the same shader set in the Renderer.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pipeline | [Phaser.Renderer.WebGL.WebGLPipeline](renderer-webgl-webglpipeline.md) | No | The pipeline instance to be checked. |
| --- | --- | --- | --- |
| currentShader | [Phaser.Renderer.WebGL.WebGLShader](renderer-webgl-webglshader.md) | Yes | The shader to set as being current. |

**Returns:** boolean - `true` if the given pipeline is already the current pipeline, otherwise `false`.

> Source: [src/renderer/webgl/PipelineManager.js#L995](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/PipelineManager.js#L995)  
> Since: 3.50.0

---

## postBatch

### <instance> postBatch(gameObject)

**Description:**

This method is called by the `WebGLPipeline.batchQuad` method, right after a quad

belonging to a Game Object has been added to the batch.

It is also called directly bu custom Game Objects, such as Nine Slice or Mesh,

from their render methods.

It causes a batch flush, then calls the `postBatch` method on the Post FX Pipelines

belonging to the Game Object.

It should be preceeded by a call to `preBatch` to start the process.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No | The Game Object that was just added to the batch. |
| --- | --- | --- | --- |

> Source: [src/renderer/webgl/PipelineManager.js#L895](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/PipelineManager.js#L895)  
> Since: 3.50.0

---

## postBatchCamera

### <instance> postBatchCamera(camera)

**Description:**

Called at the end of the `WebGLRenderer.postRenderCamera` method.

If the Camera has post pipelines set, it will flush the batch and then call the

`postBatch` method on the post-fx pipelines belonging to the Camera.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | No | The Camera that was just rendered. |
| --- | --- | --- | --- |

> Source: [src/renderer/webgl/PipelineManager.js#L964](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/PipelineManager.js#L964)  
> Since: 3.50.0

---

## preBatch

### <instance> preBatch(gameObject)

**Description:**

This method is called by the `WebGLPipeline.batchQuad` method, right before a quad

belonging to a Game Object is about to be added to the batch.

It is also called directly bu custom Game Objects, such as Nine Slice or Mesh,

from their render methods.

It causes a batch flush, then calls the `preBatch` method on the Post FX Pipelines

belonging to the Game Object.

It should be followed by a call to `postBatch` to complete the process.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No | The Game Object about to be batched. |
| --- | --- | --- | --- |

> Source: [src/renderer/webgl/PipelineManager.js#L857](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/PipelineManager.js#L857)  
> Since: 3.50.0

---

## preBatchCamera

### <instance> preBatchCamera(camera)

**Description:**

Called at the start of the `WebGLRenderer.preRenderCamera` method.

If the Camera has post pipelines set, it will flush the batch and then call the

`preBatch` method on the post-fx pipelines belonging to the Camera.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | No | The Camera about to be rendered. |
| --- | --- | --- | --- |

> Source: [src/renderer/webgl/PipelineManager.js#L932](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/PipelineManager.js#L932)  
> Since: 3.50.0

---

## rebind

### <instance> rebind([pipeline])

**Description:**

Use this to reset the gl context to the state that Phaser requires to continue rendering.

Calling this will:

* Disable `DEPTH_TEST`, `CULL_FACE` and `STENCIL_TEST`.
* Clear the depth buffer and stencil buffers.
* Reset the viewport size.
* Reset the blend mode.
* Bind a blank texture as the active texture on texture unit zero.
* Rebinds the given pipeline instance.

You should call this if you have previously called `clear`, and then wish to return

rendering control to Phaser again.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pipeline | [Phaser.Renderer.WebGL.WebGLPipeline](renderer-webgl-webglpipeline.md) | Yes | The pipeline instance to be rebound. If not given, the previous pipeline will be bound. |
| --- | --- | --- | --- |

> Source: [src/renderer/webgl/PipelineManager.js#L1301](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/PipelineManager.js#L1301)  
> Since: 3.50.0

---

## remove

### <instance> remove(name, [removeClass], [removePostPipelineClass])

**Description:**

Removes a pipeline instance based on the given name.

If no pipeline matches the name, this method does nothing.

Note that the pipeline will not be flushed or destroyed, it's simply removed from

this manager.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| name | string | No |  | The name of the pipeline to be removed. |
| --- | --- | --- | --- | --- |
| removeClass | boolean | Yes | true | Remove the pipeline class as well as the instance? |
| removePostPipelineClass | boolean | Yes | true | Remove the post pipeline class as well as the instance? |

> Source: [src/renderer/webgl/PipelineManager.js#L777](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/PipelineManager.js#L777)  
> Since: 3.50.0

---

## removePostPipeline

### <instance> removePostPipeline(pipeline)

**Description:**

Removes a PostFXPipeline instance from this Pipeline Manager.

Note that the pipeline will not be flushed or destroyed, it's simply removed from

this manager.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pipeline | [Phaser.Renderer.WebGL.Pipelines.PostFXPipeline](renderer-webgl-pipelines-postfxpipeline.md) | No | The pipeline instance to be removed. |
| --- | --- | --- | --- |

> Source: [src/renderer/webgl/PipelineManager.js#L761](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/PipelineManager.js#L761)  
> Since: 3.80.0

---

## restoreContext

### <instance> restoreContext()

**Description:**

Restore WebGL resources after context was lost.

Calls `rebind` on this Pipeline Manager.

Then calls `restoreContext` on each pipeline in turn.

> Source: [src/renderer/webgl/PipelineManager.js#L1279](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/PipelineManager.js#L1279)  
> Since: 3.80.0

---

## set

### <instance> set(pipeline, [gameObject], [currentShader])

**Description:**

Sets the current pipeline to be used by the `WebGLRenderer`.

This method accepts a pipeline instance as its parameter, not the name.

If the pipeline isn't already the current one it will call `WebGLPipeline.bind` and then `onBind`.

You cannot set Post FX Pipelines using this method. To use a Post FX Pipeline, you should

apply it to either a Camera, Container or other supporting Game Object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pipeline | [Phaser.Renderer.WebGL.WebGLPipeline](renderer-webgl-webglpipeline.md) | No | The pipeline instance to be set as current. |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | Yes | The Game Object that invoked this pipeline, if any. |
| currentShader | [Phaser.Renderer.WebGL.WebGLShader](renderer-webgl-webglshader.md) | Yes | The shader to set as being current. |

**Returns:** [Phaser.Renderer.WebGL.WebGLPipeline](renderer-webgl-webglpipeline.md) - The pipeline that was set, or undefined if it couldn't be set.

> Source: [src/renderer/webgl/PipelineManager.js#L810](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/PipelineManager.js#L810)  
> Since: 3.50.0

---

## setDefaultPipeline

### <instance> setDefaultPipeline(pipeline)

**Description:**

Sets the default pipeline being used by Game Objects.

If no instance, or matching name, exists in this manager, it returns `undefined`.

You can use this to override the default pipeline, for example by forcing

the Mobile or Multi Tint Pipelines, which is especially useful for development

testing.

Make sure you call this method *before* creating any Game Objects, as it will

only impact Game Objects created after you call it.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pipeline | string | [Phaser.Renderer.WebGL.WebGLPipeline](renderer-webgl-webglpipeline.md) | No | Either the string-based name of the pipeline to get, or a pipeline instance to look-up. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Renderer.WebGL.WebGLPipeline](renderer-webgl-webglpipeline.md) - The pipeline instance that was set as default, or `undefined` if not found.

> Source: [src/renderer/webgl/PipelineManager.js#L501](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/PipelineManager.js#L501)  
> Since: 3.60.0

---

## setFX

### <instance> setFX()

**Description:**

Sets the FX Pipeline to be the currently bound pipeline.

**Returns:** [Phaser.Renderer.WebGL.Pipelines.FXPipeline](renderer-webgl-pipelines-fxpipeline.md) - The FX Pipeline instance.

> Source: [src/renderer/webgl/PipelineManager.js#L1266](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/PipelineManager.js#L1266)  
> Since: 3.60.0

---

## setMulti

### <instance> setMulti()

**Description:**

Sets the Multi Pipeline to be the currently bound pipeline.

This is the default Phaser 3 rendering pipeline.

**Returns:** [Phaser.Renderer.WebGL.Pipelines.MultiPipeline](renderer-webgl-pipelines-multipipeline.md) - The Multi Pipeline instance.

> Source: [src/renderer/webgl/PipelineManager.js#L1236](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/PipelineManager.js#L1236)  
> Since: 3.50.0

---

## setUtility

### <instance> setUtility([currentShader])

**Description:**

Sets the Utility Pipeline to be the currently bound pipeline.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| currentShader | [Phaser.Renderer.WebGL.WebGLShader](renderer-webgl-webglshader.md) | Yes | The shader to set as being current. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Renderer.WebGL.Pipelines.UtilityPipeline](renderer-webgl-pipelines-utilitypipeline.md) - The Utility Pipeline instance.

> Source: [src/renderer/webgl/PipelineManager.js#L1251](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/PipelineManager.js#L1251)  
> Since: 3.50.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [BITMAPMASK\_PIPELINE](#bitmapmask_pipeline)

    - [BITMAPMASK\_PIPELINE: Phaser.Renderer.WebGL.Pipelines.BitmapMaskPipeline](#bitmapmask_pipeline-phaserrendererwebglpipelinesbitmapmaskpipeline)
  + [classes](#classes)

    - [classes: Phaser.Structs.Map.<string, Class>](#classes-phaserstructsmapstring-class)
  + [current](#current)

    - [current: Phaser.Renderer.WebGL.WebGLPipeline](#current-phaserrendererwebglwebglpipeline)
  + [default](#default)

    - [default: Phaser.Renderer.WebGL.WebGLPipeline](#default-phaserrendererwebglwebglpipeline)
  + [frameInc](#frameinc)

    - [frameInc: number](#frameinc-number)
  + [fullFrame1](#fullframe1)

    - [fullFrame1: Phaser.Renderer.WebGL.RenderTarget](#fullframe1-phaserrendererwebglrendertarget)
  + [fullFrame2](#fullframe2)

    - [fullFrame2: Phaser.Renderer.WebGL.RenderTarget](#fullframe2-phaserrendererwebglrendertarget)
  + [FX\_PIPELINE](#fx_pipeline)

    - [FX\_PIPELINE: Phaser.Renderer.WebGL.Pipelines.FXPipeline](#fx_pipeline-phaserrendererwebglpipelinesfxpipeline)
  + [game](#game)

    - [game: Phaser.Game](#game-phasergame)
  + [halfFrame1](#halfframe1)

    - [halfFrame1: Phaser.Renderer.WebGL.RenderTarget](#halfframe1-phaserrendererwebglrendertarget)
  + [halfFrame2](#halfframe2)

    - [halfFrame2: Phaser.Renderer.WebGL.RenderTarget](#halfframe2-phaserrendererwebglrendertarget)
  + [maxDimension](#maxdimension)

    - [maxDimension: number](#maxdimension-number)
  + [MOBILE\_PIPELINE](#mobile_pipeline)

    - [MOBILE\_PIPELINE: Phaser.Renderer.WebGL.Pipelines.MobilePipeline](#mobile_pipeline-phaserrendererwebglpipelinesmobilepipeline)
  + [MULTI\_PIPELINE](#multi_pipeline)

    - [MULTI\_PIPELINE: Phaser.Renderer.WebGL.Pipelines.MultiPipeline](#multi_pipeline-phaserrendererwebglpipelinesmultipipeline)
  + [pipelines](#pipelines)

    - [pipelines: Phaser.Structs.Map.<string, Phaser.Renderer.WebGL.WebGLPipeline>](#pipelines-phaserstructsmapstring-phaserrendererwebglwebglpipeline)
  + [postPipelineClasses](#postpipelineclasses)

    - [postPipelineClasses: Phaser.Structs.Map.<string, Class>](#postpipelineclasses-phaserstructsmapstring-class)
  + [postPipelineInstances](#postpipelineinstances)

    - [postPipelineInstances: Array.<Phaser.Renderer.WebGL.Pipelines.PostFXPipeline>](#postpipelineinstances-arrayphaserrendererwebglpipelinespostfxpipeline)
  + [previous](#previous)

    - [previous: Phaser.Renderer.WebGL.WebGLPipeline](#previous-phaserrendererwebglwebglpipeline)
  + [renderer](#renderer)

    - [renderer: Phaser.Renderer.WebGL.WebGLRenderer](#renderer-phaserrendererwebglwebglrenderer)
  + [renderTargets](#rendertargets)

    - [renderTargets: Array.<Phaser.Renderer.WebGL.RenderTarget>](#rendertargets-arrayphaserrendererwebglrendertarget)
  + [targetIndex](#targetindex)

    - [targetIndex: number](#targetindex-number)
  + [UTILITY\_PIPELINE](#utility_pipeline)

    - [UTILITY\_PIPELINE: Phaser.Renderer.WebGL.Pipelines.UtilityPipeline](#utility_pipeline-phaserrendererwebglpipelinesutilitypipeline)
* [Public Methods](#public-methods)

  + [add](#add)

    - [<instance> add(name, pipeline)](#instance-addname-pipeline)
  + [addPostPipeline](#addpostpipeline)

    - [<instance> addPostPipeline(name, pipeline)](#instance-addpostpipelinename-pipeline)
  + [blendFrames](#blendframes)

    - [<instance> blendFrames(source1, source2, [target], [strength], [clearAlpha])](#instance-blendframessource1-source2-target-strength-clearalpha)
  + [blendFramesAdditive](#blendframesadditive)

    - [<instance> blendFramesAdditive(source1, source2, [target], [strength], [clearAlpha])](#instance-blendframesadditivesource1-source2-target-strength-clearalpha)
  + [blitFrame](#blitframe)

    - [<instance> blitFrame(source, target, [brightness], [clear], [clearAlpha], [eraseMode])](#instance-blitframesource-target-brightness-clear-clearalpha-erasemode)
  + [boot](#boot)

    - [<instance> boot(pipelineConfig, defaultPipeline, autoMobilePipeline)](#instance-bootpipelineconfig-defaultpipeline-automobilepipeline)
  + [clear](#clear)

    - [<instance> clear()](#instance-clear)
  + [clearFrame](#clearframe)

    - [<instance> clearFrame(target, [clearAlpha])](#instance-clearframetarget-clearalpha)
  + [copyFrame](#copyframe)

    - [<instance> copyFrame(source, [target], [brightness], [clear], [clearAlpha])](#instance-copyframesource-target-brightness-clear-clearalpha)
  + [copyFrameRect](#copyframerect)

    - [<instance> copyFrameRect(source, target, x, y, width, height, [clear], [clearAlpha])](#instance-copyframerectsource-target-x-y-width-height-clear-clearalpha)
  + [copyToGame](#copytogame)

    - [<instance> copyToGame(source)](#instance-copytogamesource)
  + [destroy](#destroy)

    - [<instance> destroy()](#instance-destroy)
  + [drawFrame](#drawframe)

    - [<instance> drawFrame(source, [target], [clearAlpha], [colorMatrix])](#instance-drawframesource-target-clearalpha-colormatrix)
  + [flush](#flush)

    - [<instance> flush()](#instance-flush)
  + [forceZero](#forcezero)

    - [<instance> forceZero()](#instance-forcezero)
  + [get](#get)

    - [<instance> get(pipeline)](#instance-getpipeline)
  + [getAltSwapRenderTarget](#getaltswaprendertarget)

    - [<instance> getAltSwapRenderTarget()](#instance-getaltswaprendertarget)
  + [getPostPipeline](#getpostpipeline)

    - [<instance> getPostPipeline(pipeline, [gameObject], [config])](#instance-getpostpipelinepipeline-gameobject-config)
  + [getRenderTarget](#getrendertarget)

    - [<instance> getRenderTarget(size)](#instance-getrendertargetsize)
  + [getSwapRenderTarget](#getswaprendertarget)

    - [<instance> getSwapRenderTarget()](#instance-getswaprendertarget)
  + [has](#has)

    - [<instance> has(pipeline)](#instance-haspipeline)
  + [isCurrent](#iscurrent)

    - [<instance> isCurrent(pipeline, [currentShader])](#instance-iscurrentpipeline-currentshader)
  + [postBatch](#postbatch)

    - [<instance> postBatch(gameObject)](#instance-postbatchgameobject)
  + [postBatchCamera](#postbatchcamera)

    - [<instance> postBatchCamera(camera)](#instance-postbatchcameracamera)
  + [preBatch](#prebatch)

    - [<instance> preBatch(gameObject)](#instance-prebatchgameobject)
  + [preBatchCamera](#prebatchcamera)

    - [<instance> preBatchCamera(camera)](#instance-prebatchcameracamera)
  + [rebind](#rebind)

    - [<instance> rebind([pipeline])](#instance-rebindpipeline)
  + [remove](#remove)

    - [<instance> remove(name, [removeClass], [removePostPipelineClass])](#instance-removename-removeclass-removepostpipelineclass)
  + [removePostPipeline](#removepostpipeline)

    - [<instance> removePostPipeline(pipeline)](#instance-removepostpipelinepipeline)
  + [restoreContext](#restorecontext)

    - [<instance> restoreContext()](#instance-restorecontext)
  + [set](#set)

    - [<instance> set(pipeline, [gameObject], [currentShader])](#instance-setpipeline-gameobject-currentshader)
  + [setDefaultPipeline](#setdefaultpipeline)

    - [<instance> setDefaultPipeline(pipeline)](#instance-setdefaultpipelinepipeline)
  + [setFX](#setfx)

    - [<instance> setFX()](#instance-setfx)
  + [setMulti](#setmulti)

    - [<instance> setMulti()](#instance-setmulti)
  + [setUtility](#setutility)

    - [<instance> setUtility([currentShader])](#instance-setutilitycurrentshader)

Back to top

©2025[Phaser](https://docs.phaser.io)