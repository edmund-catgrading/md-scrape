# Systems

Phaser.Scenes.Systems

The Scene Systems class.

This class is available from within a Scene under the property `sys`.

It is responsible for managing all of the plugins a Scene has running, including the display list, and

handling the update step and renderer. It also contains references to global systems belonging to Game.

**Constructor**

`new Systems(scene, config)`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| scene | [Phaser.Scene](scene.md) | No | The Scene that owns this Systems instance. |
| --- | --- | --- | --- |
| config | string | [Phaser.Types.Scenes.SettingsConfig](../typedef/types-scenes.md) | No | Scene specific configuration settings. |

---

**Scope**: static

> Source: [src/scene/Systems.js#L16](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/Systems.js#L16)  
> Since: 3.0.0

# Public Members

## add

### add: [Phaser.GameObjects.GameObjectFactory](gameobjects-gameobjectfactory.md)

**Description:**

A reference to the Scene's Game Object Factory.

Use this to quickly and easily create new Game Object's.

In the default set-up you can access this from within a Scene via the `this.add` property.

> Source: [src/scene/Systems.js#L196](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/Systems.js#L196)  
> Since: 3.0.0

---

## anims

### anims: [Phaser.Animations.AnimationManager](animations-animationmanager.md)

**Description:**

A reference to the global Animations Manager.

In the default set-up you can access this from within a Scene via the `this.anims` property.

> Source: [src/scene/Systems.js#L115](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/Systems.js#L115)  
> Since: 3.0.0

---

## cache

### cache: [Phaser.Cache.CacheManager](cache-cachemanager.md)

**Description:**

A reference to the global Cache. The Cache stores all files bought in to Phaser via

the Loader, with the exception of images. Images are stored in the Texture Manager.

In the default set-up you can access this from within a Scene via the `this.cache` property.

> Source: [src/scene/Systems.js#L126](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/Systems.js#L126)  
> Since: 3.0.0

---

## cameras

### cameras: [Phaser.Cameras.Scene2D.CameraManager](cameras-scene2d-cameramanager.md)

**Description:**

A reference to the Scene's Camera Manager.

Use this to manipulate and create Cameras for this specific Scene.

In the default set-up you can access this from within a Scene via the `this.cameras` property.

> Source: [src/scene/Systems.js#L209](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/Systems.js#L209)  
> Since: 3.0.0

---

## canvas

### canvas: HTMLCanvasElement

**Description:**

A handy reference to the Scene canvas / context.

> Source: [src/scene/Systems.js#L95](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/Systems.js#L95)  
> Since: 3.0.0

---

## config

### config: string, [Phaser.Types.Scenes.SettingsConfig](../typedef/types-scenes.md)

**Description:**

The Scene Configuration object, as passed in when creating the Scene.

> Source: [src/scene/Systems.js#L77](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/Systems.js#L77)  
> Since: 3.0.0

---

## context

### context: CanvasRenderingContext2D

**Description:**

A reference to the Canvas Rendering Context being used by the renderer.

> Source: [src/scene/Systems.js#L104](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/Systems.js#L104)  
> Since: 3.0.0

---

## displayList

### displayList: [Phaser.GameObjects.DisplayList](gameobjects-displaylist.md)

**Description:**

A reference to the Scene's Display List.

Use this to organize the children contained in the display list.

In the default set-up you can access this from within a Scene via the `this.children` property.

> Source: [src/scene/Systems.js#L222](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/Systems.js#L222)  
> Since: 3.0.0

---

## events

### events: [Phaser.Events.EventEmitter](events-eventemitter.md)

**Description:**

A reference to the Scene's Event Manager.

Use this to listen for Scene specific events, such as `pause` and `shutdown`.

In the default set-up you can access this from within a Scene via the `this.events` property.

> Source: [src/scene/Systems.js#L235](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/Systems.js#L235)  
> Since: 3.0.0

---

## facebook

### facebook: [Phaser.FacebookInstantGamesPlugin](facebookinstantgamesplugin.md)

**Description:**

The Facebook Instant Games Plugin.

> Source: [src/scene/Systems.js#L67](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/Systems.js#L67)  
> Since: 3.12.0

---

## game

### game: [Phaser.Game](game.md)

**Description:**

A reference to the Phaser Game instance.

> Source: [src/scene/Systems.js#L47](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/Systems.js#L47)  
> Since: 3.0.0

---

## make

### make: [Phaser.GameObjects.GameObjectCreator](gameobjects-gameobjectcreator.md)

**Description:**

A reference to the Scene's Game Object Creator.

Use this to quickly and easily create new Game Object's. The difference between this and the

Game Object Factory, is that the Creator just creates and returns Game Object instances, it

doesn't then add them to the Display List or Update List.

In the default set-up you can access this from within a Scene via the `this.make` property.

> Source: [src/scene/Systems.js#L248](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/Systems.js#L248)  
> Since: 3.0.0

---

## plugins

### plugins: [Phaser.Plugins.PluginManager](plugins-pluginmanager.md)

**Description:**

A reference to the global Plugins Manager.

In the default set-up you can access this from within a Scene via the `this.plugins` property.

> Source: [src/scene/Systems.js#L138](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/Systems.js#L138)  
> Since: 3.0.0

---

## registry

### registry: [Phaser.Data.DataManager](data-datamanager.md)

**Description:**

A reference to the global registry. This is a game-wide instance of the Data Manager, allowing

you to exchange data between Scenes via a universal and shared point.

In the default set-up you can access this from within a Scene via the `this.registry` property.

> Source: [src/scene/Systems.js#L149](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/Systems.js#L149)  
> Since: 3.0.0

---

## renderer

### renderer: [Phaser.Renderer.Canvas.CanvasRenderer](renderer-canvas-canvasrenderer.md), [Phaser.Renderer.WebGL.WebGLRenderer](renderer-webgl-webglrenderer.md)

**Description:**

A reference to either the Canvas or WebGL Renderer that this Game is using.

> Source: [src/scene/Systems.js#L56](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/Systems.js#L56)  
> Since: 3.17.0

---

## scale

### scale: [Phaser.Scale.ScaleManager](scale-scalemanager.md)

**Description:**

A reference to the global Scale Manager.

In the default set-up you can access this from within a Scene via the `this.scale` property.

> Source: [src/scene/Systems.js#L161](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/Systems.js#L161)  
> Since: 3.15.0

---

## scene

### scene: [Phaser.Scene](scene.md)

**Description:**

A reference to the Scene that these Systems belong to.

> Source: [src/scene/Systems.js#L38](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/Systems.js#L38)  
> Since: 3.0.0

---

## scenePlugin

### scenePlugin: [Phaser.Scenes.ScenePlugin](scenes-sceneplugin.md)

**Description:**

A reference to the Scene Manager Plugin.

Use this to manipulate both this and other Scene's in your game, for example to launch a parallel Scene,

or pause or resume a Scene, or switch from this Scene to another.

In the default set-up you can access this from within a Scene via the `this.scene` property.

> Source: [src/scene/Systems.js#L263](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/Systems.js#L263)  
> Since: 3.0.0

---

## settings

### settings: [Phaser.Types.Scenes.SettingsObject](../typedef/types-scenes.md)

**Description:**

The Scene Settings. This is the parsed output based on the Scene configuration.

> Source: [src/scene/Systems.js#L86](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/Systems.js#L86)  
> Since: 3.0.0

---

## sound

### sound: [Phaser.Sound.NoAudioSoundManager](sound-noaudiosoundmanager.md), [Phaser.Sound.HTML5AudioSoundManager](sound-html5audiosoundmanager.md), [Phaser.Sound.WebAudioSoundManager](sound-webaudiosoundmanager.md)

**Description:**

A reference to the global Sound Manager.

In the default set-up you can access this from within a Scene via the `this.sound` property.

> Source: [src/scene/Systems.js#L172](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/Systems.js#L172)  
> Since: 3.0.0

---

## textures

### textures: [Phaser.Textures.TextureManager](textures-texturemanager.md)

**Description:**

A reference to the global Texture Manager.

In the default set-up you can access this from within a Scene via the `this.textures` property.

> Source: [src/scene/Systems.js#L183](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/Systems.js#L183)  
> Since: 3.0.0

---

## updateList

### updateList: [Phaser.GameObjects.UpdateList](gameobjects-updatelist.md)

**Description:**

A reference to the Scene's Update List.

Use this to organize the children contained in the update list.

The Update List is responsible for managing children that need their `preUpdate` methods called,

in order to process so internal components, such as Sprites with Animations.

In the default set-up there is no reference to this from within the Scene itself.

> Source: [src/scene/Systems.js#L277](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/Systems.js#L277)  
> Since: 3.0.0

---

# Private Members

## sceneUpdate

### sceneUpdate: function

**Description:**

The Scene Update function.

This starts out as NOOP during init, preload and create, and at the end of create

it swaps to be whatever the Scene.update function is.

**Access:** private

> Source: [src/scene/Systems.js#L293](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/Systems.js#L293)  
> Since: 3.10.0

---

# Public Methods

## canInput

### <instance> canInput()

**Description:**

Can this Scene receive Input events?

**Returns:** boolean - `true` if this Scene can receive Input events.

> Source: [src/scene/Systems.js#L575](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/Systems.js#L575)  
> Since: 3.60.0

---

## depthSort

### <instance> depthSort()

**Description:**

Immediately sorts the display list if the flag is set.

> Source: [src/scene/Systems.js#L404](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/Systems.js#L404)  
> Since: 3.0.0

---

## getData

### <instance> getData()

**Description:**

Returns any data that was sent to this Scene by another Scene.

The data is also passed to `Scene.init` and in various Scene events, but

you can access it at any point via this method.

**Returns:** any - The Scene Data.

> Source: [src/scene/Systems.js#L546](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/Systems.js#L546)  
> Since: 3.22.0

---

## getStatus

### <instance> getStatus()

**Description:**

Returns the current status of this Scene.

**Returns:** number - The status of this Scene. One of the `Phaser.Scene` constants.

> Source: [src/scene/Systems.js#L562](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/Systems.js#L562)  
> Since: 3.60.0

---

## init

### <instance> init(game)

**Description:**

This method is called only once by the Scene Manager when the Scene is instantiated.

It is responsible for setting up all of the Scene plugins and references.

It should never be called directly.

**Access:** protected

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| game | [Phaser.Game](game.md) | No | A reference to the Phaser Game instance. |
| --- | --- | --- | --- |

**Fires:** [Phaser.Scenes.Events#event:BOOT](../event/scenes-events.md)

> Source: [src/scene/Systems.js#L307](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/Systems.js#L307)  
> Since: 3.0.0

---

## isActive

### <instance> isActive()

**Description:**

Is this Scene running?

**Returns:** boolean - `true` if this Scene is running, otherwise `false`.

> Source: [src/scene/Systems.js#L603](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/Systems.js#L603)  
> Since: 3.0.0

---

## isPaused

### <instance> isPaused()

**Description:**

Is this Scene paused?

**Returns:** boolean - `true` if this Scene is paused, otherwise `false`.

> Source: [src/scene/Systems.js#L616](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/Systems.js#L616)  
> Since: 3.13.0

---

## isSleeping

### <instance> isSleeping()

**Description:**

Is this Scene sleeping?

**Returns:** boolean - `true` if this Scene is asleep, otherwise `false`.

> Source: [src/scene/Systems.js#L590](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/Systems.js#L590)  
> Since: 3.0.0

---

## isTransitionIn

### <instance> isTransitionIn()

**Description:**

Is this Scene currently transitioning in from another Scene?

**Returns:** boolean - `true` if this Scene is transitioning in from another Scene, otherwise `false`.

> Source: [src/scene/Systems.js#L655](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/Systems.js#L655)  
> Since: 3.5.0

---

## isTransitioning

### <instance> isTransitioning()

**Description:**

Is this Scene currently transitioning out to, or in from another Scene?

**Returns:** boolean - `true` if this Scene is currently transitioning, otherwise `false`.

> Source: [src/scene/Systems.js#L629](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/Systems.js#L629)  
> Since: 3.5.0

---

## isTransitionOut

### <instance> isTransitionOut()

**Description:**

Is this Scene currently transitioning out from itself to another Scene?

**Returns:** boolean - `true` if this Scene is in transition to another Scene, otherwise `false`.

> Source: [src/scene/Systems.js#L642](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/Systems.js#L642)  
> Since: 3.5.0

---

## isVisible

### <instance> isVisible()

**Description:**

Is this Scene visible and rendering?

**Returns:** boolean - `true` if this Scene is visible, otherwise `false`.

> Source: [src/scene/Systems.js#L668](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/Systems.js#L668)  
> Since: 3.0.0

---

## pause

### <instance> pause([data])

**Description:**

Pause this Scene.

A paused Scene still renders, it just doesn't run any of its update handlers or systems.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| data | object | Yes | A data object that will be passed in the 'pause' event. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Scenes.Systems](scenes-systems.md) - This Systems object.

**Fires:** [Phaser.Scenes.Events#event:PAUSE](../event/scenes-events.md)

> Source: [src/scene/Systems.js#L415](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/Systems.js#L415)  
> Since: 3.0.0

---

## queueDepthSort

### <instance> queueDepthSort()

**Description:**

Force a sort of the display list on the next render.

> Source: [src/scene/Systems.js#L393](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/Systems.js#L393)  
> Since: 3.0.0

---

## render

### <instance> render(renderer)

**Description:**

Called automatically by the Scene Manager.

Instructs the Scene to render itself via its Camera Manager to the renderer given.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| renderer | [Phaser.Renderer.Canvas.CanvasRenderer](renderer-canvas-canvasrenderer.md) | [Phaser.Renderer.WebGL.WebGLRenderer](renderer-webgl-webglrenderer.md) | No | The renderer that invoked the render call. |
| --- | --- | --- | --- |

**Fires:** [Phaser.Scenes.Events#event:PRE\_RENDER](../event/scenes-events.md), [Phaser.Scenes.Events#event:RENDER](../event/scenes-events.md)

> Source: [src/scene/Systems.js#L369](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/Systems.js#L369)  
> Since: 3.0.0

---

## resume

### <instance> resume([data])

**Description:**

Resume this Scene from a paused state.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| data | object | Yes | A data object that will be passed in the 'resume' event. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Scenes.Systems](scenes-systems.md) - This Systems object.

**Fires:** [Phaser.Scenes.Events#event:RESUME](../event/scenes-events.md)

> Source: [src/scene/Systems.js#L449](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/Systems.js#L449)  
> Since: 3.0.0

---

## setActive

### <instance> setActive(value, [data])

**Description:**

Set the active state of this Scene.

An active Scene will run its core update loop.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | boolean | No | If `true` the Scene will be resumed, if previously paused. If `false` it will be paused. |
| --- | --- | --- | --- |
| data | object | Yes | A data object that will be passed in the 'resume' or 'pause' events. |

**Returns:** [Phaser.Scenes.Systems](scenes-systems.md) - This Systems object.

> Source: [src/scene/Systems.js#L699](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/Systems.js#L699)  
> Since: 3.0.0

---

## setVisible

### <instance> setVisible(value)

**Description:**

Sets the visible state of this Scene.

An invisible Scene will not render, but will still process updates.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | boolean | No | `true` to render this Scene, otherwise `false`. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Scenes.Systems](scenes-systems.md) - This Systems object.

> Source: [src/scene/Systems.js#L681](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/Systems.js#L681)  
> Since: 3.0.0

---

## shutdown

### <instance> shutdown([data])

**Description:**

Shutdown this Scene and send a shutdown event to all of its systems.

A Scene that has been shutdown will not run its update loop or render, but it does

not destroy any of its plugins or references. It is put into hibernation for later use.

If you don't ever plan to use this Scene again, then it should be destroyed instead

to free-up resources.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| data | object | Yes | A data object that will be passed in the 'shutdown' event. |
| --- | --- | --- | --- |

**Fires:** [Phaser.Scenes.Events#event:SHUTDOWN](../event/scenes-events.md)

> Source: [src/scene/Systems.js#L757](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/Systems.js#L757)  
> Since: 3.0.0

---

## sleep

### <instance> sleep([data])

**Description:**

Send this Scene to sleep.

A sleeping Scene doesn't run its update step or render anything, but it also isn't shut down

or has any of its systems or children removed, meaning it can be re-activated at any point and

will carry on from where it left off. It also keeps everything in memory and events and callbacks

from other Scenes may still invoke changes within it, so be careful what is left active.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| data | object | Yes | A data object that will be passed in the 'sleep' event. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Scenes.Systems](scenes-systems.md) - This Systems object.

**Fires:** [Phaser.Scenes.Events#event:SLEEP](../event/scenes-events.md)

> Source: [src/scene/Systems.js#L477](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/Systems.js#L477)  
> Since: 3.0.0

---

## start

### <instance> start(data)

**Description:**

Start this Scene running and rendering.

Called automatically by the SceneManager.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| data | object | No | Optional data object that may have been passed to this Scene from another. |
| --- | --- | --- | --- |

**Fires:** [Phaser.Scenes.Events#event:START](../event/scenes-events.md), [Phaser.Scenes.Events#event:READY](../event/scenes-events.md)

> Source: [src/scene/Systems.js#L724](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/Systems.js#L724)  
> Since: 3.0.0

---

## step

### <instance> step(time, delta)

**Description:**

A single game step. Called automatically by the Scene Manager as a result of a Request Animation

Frame or Set Timeout call to the main Game instance.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| time | number | No | The time value from the most recent Game step. Typically a high-resolution timer value, or Date.now(). |
| --- | --- | --- | --- |
| delta | number | No | The delta value since the last frame. This is smoothed to avoid delta spikes by the TimeStep class. |

**Fires:** [Phaser.Scenes.Events#event:PRE\_UPDATE](../event/scenes-events.md), [Phaser.Scenes.Events#event:UPDATE](../event/scenes-events.md), [Phaser.Scenes.Events#event:POST\_UPDATE](../event/scenes-events.md)

> Source: [src/scene/Systems.js#L343](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/Systems.js#L343)  
> Since: 3.0.0

---

## wake

### <instance> wake([data])

**Description:**

Wake-up this Scene if it was previously asleep.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| data | object | Yes | A data object that will be passed in the 'wake' event. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Scenes.Systems](scenes-systems.md) - This Systems object.

**Fires:** [Phaser.Scenes.Events#event:WAKE](../event/scenes-events.md)

> Source: [src/scene/Systems.js#L515](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/Systems.js#L515)  
> Since: 3.0.0

---

# Private Methods

## destroy

### <instance> destroy()

**Description:**

Destroy this Scene and send a destroy event all of its systems.

A destroyed Scene cannot be restarted.

You should not call this directly, instead use `SceneManager.remove`.

**Access:** private

**Fires:** [Phaser.Scenes.Events#event:DESTROY](../event/scenes-events.md)

> Source: [src/scene/Systems.js#L788](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/Systems.js#L788)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [add](#add)

    - [add: Phaser.GameObjects.GameObjectFactory](#add-phasergameobjectsgameobjectfactory)
  + [anims](#anims)

    - [anims: Phaser.Animations.AnimationManager](#anims-phaseranimationsanimationmanager)
  + [cache](#cache)

    - [cache: Phaser.Cache.CacheManager](#cache-phasercachecachemanager)
  + [cameras](#cameras)

    - [cameras: Phaser.Cameras.Scene2D.CameraManager](#cameras-phasercamerasscene2dcameramanager)
  + [canvas](#canvas)

    - [canvas: HTMLCanvasElement](#canvas-htmlcanvaselement)
  + [config](#config)

    - [config: string, Phaser.Types.Scenes.SettingsConfig](#config-string-phasertypesscenessettingsconfig)
  + [context](#context)

    - [context: CanvasRenderingContext2D](#context-canvasrenderingcontext2d)
  + [displayList](#displaylist)

    - [displayList: Phaser.GameObjects.DisplayList](#displaylist-phasergameobjectsdisplaylist)
  + [events](#events)

    - [events: Phaser.Events.EventEmitter](#events-phasereventseventemitter)
  + [facebook](#facebook)

    - [facebook: Phaser.FacebookInstantGamesPlugin](#facebook-phaserfacebookinstantgamesplugin)
  + [game](#game)

    - [game: Phaser.Game](#game-phasergame)
  + [make](#make)

    - [make: Phaser.GameObjects.GameObjectCreator](#make-phasergameobjectsgameobjectcreator)
  + [plugins](#plugins)

    - [plugins: Phaser.Plugins.PluginManager](#plugins-phaserpluginspluginmanager)
  + [registry](#registry)

    - [registry: Phaser.Data.DataManager](#registry-phaserdatadatamanager)
  + [renderer](#renderer)

    - [renderer: Phaser.Renderer.Canvas.CanvasRenderer, Phaser.Renderer.WebGL.WebGLRenderer](#renderer-phaserrenderercanvascanvasrenderer-phaserrendererwebglwebglrenderer)
  + [scale](#scale)

    - [scale: Phaser.Scale.ScaleManager](#scale-phaserscalescalemanager)
  + [scene](#scene)

    - [scene: Phaser.Scene](#scene-phaserscene)
  + [scenePlugin](#sceneplugin)

    - [scenePlugin: Phaser.Scenes.ScenePlugin](#sceneplugin-phaserscenessceneplugin)
  + [settings](#settings)

    - [settings: Phaser.Types.Scenes.SettingsObject](#settings-phasertypesscenessettingsobject)
  + [sound](#sound)

    - [sound: Phaser.Sound.NoAudioSoundManager, Phaser.Sound.HTML5AudioSoundManager, Phaser.Sound.WebAudioSoundManager](#sound-phasersoundnoaudiosoundmanager-phasersoundhtml5audiosoundmanager-phasersoundwebaudiosoundmanager)
  + [textures](#textures)

    - [textures: Phaser.Textures.TextureManager](#textures-phasertexturestexturemanager)
  + [updateList](#updatelist)

    - [updateList: Phaser.GameObjects.UpdateList](#updatelist-phasergameobjectsupdatelist)
* [Private Members](#private-members)

  + [sceneUpdate](#sceneupdate)

    - [sceneUpdate: function](#sceneupdate-function)
* [Public Methods](#public-methods)

  + [canInput](#caninput)

    - [<instance> canInput()](#instance-caninput)
  + [depthSort](#depthsort)

    - [<instance> depthSort()](#instance-depthsort)
  + [getData](#getdata)

    - [<instance> getData()](#instance-getdata)
  + [getStatus](#getstatus)

    - [<instance> getStatus()](#instance-getstatus)
  + [init](#init)

    - [<instance> init(game)](#instance-initgame)
  + [isActive](#isactive)

    - [<instance> isActive()](#instance-isactive)
  + [isPaused](#ispaused)

    - [<instance> isPaused()](#instance-ispaused)
  + [isSleeping](#issleeping)

    - [<instance> isSleeping()](#instance-issleeping)
  + [isTransitionIn](#istransitionin)

    - [<instance> isTransitionIn()](#instance-istransitionin)
  + [isTransitioning](#istransitioning)

    - [<instance> isTransitioning()](#instance-istransitioning)
  + [isTransitionOut](#istransitionout)

    - [<instance> isTransitionOut()](#instance-istransitionout)
  + [isVisible](#isvisible)

    - [<instance> isVisible()](#instance-isvisible)
  + [pause](#pause)

    - [<instance> pause([data])](#instance-pausedata)
  + [queueDepthSort](#queuedepthsort)

    - [<instance> queueDepthSort()](#instance-queuedepthsort)
  + [render](#render)

    - [<instance> render(renderer)](#instance-renderrenderer)
  + [resume](#resume)

    - [<instance> resume([data])](#instance-resumedata)
  + [setActive](#setactive)

    - [<instance> setActive(value, [data])](#instance-setactivevalue-data)
  + [setVisible](#setvisible)

    - [<instance> setVisible(value)](#instance-setvisiblevalue)
  + [shutdown](#shutdown)

    - [<instance> shutdown([data])](#instance-shutdowndata)
  + [sleep](#sleep)

    - [<instance> sleep([data])](#instance-sleepdata)
  + [start](#start)

    - [<instance> start(data)](#instance-startdata)
  + [step](#step)

    - [<instance> step(time, delta)](#instance-steptime-delta)
  + [wake](#wake)

    - [<instance> wake([data])](#instance-wakedata)
* [Private Methods](#private-methods)

  + [destroy](#destroy)

    - [<instance> destroy()](#instance-destroy)

Back to top

©2025[Phaser](https://docs.phaser.io)