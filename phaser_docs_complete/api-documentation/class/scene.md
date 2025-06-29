# Scene

Phaser.Scene

A base Phaser.Scene class which can be extended for your own use.

You can also define the optional methods [init()](../typedef/types-scenes.md), [preload()](../typedef/types-scenes.md), and [create()](../typedef/types-scenes.md).

**Constructor**

`new Scene([config])`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| config | string | [Phaser.Types.Scenes.SettingsConfig](../typedef/types-scenes.md) | Yes | The scene key or scene specific configuration settings. |
| --- | --- | --- | --- |

---

**Scope**: static

> Source: [src/scene/Scene.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/Scene.js#L10)  
> Since: 3.0.0

# Public Members

## add

### add: [Phaser.GameObjects.GameObjectFactory](gameobjects-gameobjectfactory.md)

**Description:**

The Scene Game Object Factory.

This property will only be available if defined in the Scene Injection Map.

> Source: [src/scene/Scene.js#L126](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/Scene.js#L126)  
> Since: 3.0.0

---

## anims

### anims: [Phaser.Animations.AnimationManager](animations-animationmanager.md)

**Description:**

A reference to the global Animation Manager.

This property will only be available if defined in the Scene Injection Map.

> Source: [src/scene/Scene.js#L49](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/Scene.js#L49)  
> Since: 3.0.0

---

## cache

### cache: [Phaser.Cache.CacheManager](cache-cachemanager.md)

**Description:**

A reference to the global Cache.

This property will only be available if defined in the Scene Injection Map.

> Source: [src/scene/Scene.js#L60](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/Scene.js#L60)  
> Since: 3.0.0

---

## cameras

### cameras: [Phaser.Cameras.Scene2D.CameraManager](cameras-scene2d-cameramanager.md)

**Description:**

The Scene Camera Manager.

This property will only be available if defined in the Scene Injection Map.

> Source: [src/scene/Scene.js#L115](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/Scene.js#L115)  
> Since: 3.0.0

---

## children

### children: [Phaser.GameObjects.DisplayList](gameobjects-displaylist.md)

**Description:**

The Game Object Display List belonging to this Scene.

This property will only be available if defined in the Scene Injection Map.

> Source: [src/scene/Scene.js#L159](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/Scene.js#L159)  
> Since: 3.0.0

---

## data

### data: [Phaser.Data.DataManager](data-datamanager.md)

**Description:**

A Scene specific Data Manager Plugin.

See the `registry` property for the global Data Manager.

This property will only be available if defined in the Scene Injection Map and the plugin is installed.

> Source: [src/scene/Scene.js#L181](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/Scene.js#L181)  
> Since: 3.0.0

---

## events

### events: [Phaser.Events.EventEmitter](events-eventemitter.md)

**Description:**

A Scene specific Event Emitter.

This property will only be available if defined in the Scene Injection Map.

> Source: [src/scene/Scene.js#L104](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/Scene.js#L104)  
> Since: 3.0.0

---

## facebook

### facebook: [Phaser.FacebookInstantGamesPlugin](facebookinstantgamesplugin.md)

**Description:**

The Facebook Instant Games Plugin.

This property will only be available if defined in the Scene Injection Map, the plugin is installed and configured.

> Source: [src/scene/Scene.js#L262](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/Scene.js#L262)  
> Since: 3.12.0

---

## game

### game: [Phaser.Game](game.md)

**Description:**

A reference to the Phaser.Game instance.

This property will only be available if defined in the Scene Injection Map.

> Source: [src/scene/Scene.js#L38](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/Scene.js#L38)  
> Since: 3.0.0

---

## input

### input: [Phaser.Input.InputPlugin](input-inputplugin.md)

**Description:**

The Scene Input Manager Plugin.

This property will only be available if defined in the Scene Injection Map and the plugin is installed.

> Source: [src/scene/Scene.js#L194](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/Scene.js#L194)  
> Since: 3.0.0

---

## lights

### lights: [Phaser.GameObjects.LightsManager](gameobjects-lightsmanager.md)

**Description:**

The Scene Lights Manager Plugin.

This property will only be available if defined in the Scene Injection Map and the plugin is installed.

> Source: [src/scene/Scene.js#L170](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/Scene.js#L170)  
> Since: 3.0.0

---

## load

### load: [Phaser.Loader.LoaderPlugin](loader-loaderplugin.md)

**Description:**

The Scene Loader Plugin.

This property will only be available if defined in the Scene Injection Map and the plugin is installed.

> Source: [src/scene/Scene.js#L205](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/Scene.js#L205)  
> Since: 3.0.0

---

## make

### make: [Phaser.GameObjects.GameObjectCreator](gameobjects-gameobjectcreator.md)

**Description:**

The Scene Game Object Creator.

This property will only be available if defined in the Scene Injection Map.

> Source: [src/scene/Scene.js#L137](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/Scene.js#L137)  
> Since: 3.0.0

---

## matter

### matter: [Phaser.Physics.Matter.MatterPhysics](physics-matter-matterphysics.md)

**Description:**

The Scene Matter Physics Plugin.

This property will only be available if defined in the Scene Injection Map, the plugin is installed and configured.

> Source: [src/scene/Scene.js#L249](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/Scene.js#L249)  
> Since: 3.0.0

---

## physics

### physics: [Phaser.Physics.Arcade.ArcadePhysics](physics-arcade-arcadephysics.md)

**Description:**

The Scene Arcade Physics Plugin.

This property will only be available if defined in the Scene Injection Map, the plugin is installed and configured.

> Source: [src/scene/Scene.js#L238](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/Scene.js#L238)  
> Since: 3.0.0

---

## plugins

### plugins: [Phaser.Plugins.PluginManager](plugins-pluginmanager.md)

**Description:**

A reference to the global Plugin Manager.

The Plugin Manager is a global system that allows plugins to register themselves with it, and can then install

those plugins into Scenes as required.

> Source: [src/scene/Scene.js#L285](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/Scene.js#L285)  
> Since: 3.0.0

---

## registry

### registry: [Phaser.Data.DataManager](data-datamanager.md)

**Description:**

A reference to the global Data Manager.

This property will only be available if defined in the Scene Injection Map.

> Source: [src/scene/Scene.js#L71](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/Scene.js#L71)  
> Since: 3.0.0

---

## renderer

### renderer: [Phaser.Renderer.Canvas.CanvasRenderer](renderer-canvas-canvasrenderer.md), [Phaser.Renderer.WebGL.WebGLRenderer](renderer-webgl-webglrenderer.md)

**Description:**

A reference to the renderer instance Phaser is using, either Canvas Renderer or WebGL Renderer.

> Source: [src/scene/Scene.js#L297](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/Scene.js#L297)  
> Since: 3.50.0

---

## scale

### scale: [Phaser.Scale.ScaleManager](scale-scalemanager.md)

**Description:**

A reference to the global Scale Manager.

This property will only be available if defined in the Scene Injection Map.

> Source: [src/scene/Scene.js#L274](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/Scene.js#L274)  
> Since: 3.16.2

---

## scene

### scene: [Phaser.Scenes.ScenePlugin](scenes-sceneplugin.md)

**Description:**

A reference to the Scene Manager Plugin.

This property will only be available if defined in the Scene Injection Map.

> Source: [src/scene/Scene.js#L148](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/Scene.js#L148)  
> Since: 3.0.0

---

## sound

### sound: [Phaser.Sound.NoAudioSoundManager](sound-noaudiosoundmanager.md), [Phaser.Sound.HTML5AudioSoundManager](sound-html5audiosoundmanager.md), [Phaser.Sound.WebAudioSoundManager](sound-webaudiosoundmanager.md)

**Description:**

A reference to the Sound Manager.

This property will only be available if defined in the Scene Injection Map and the plugin is installed.

> Source: [src/scene/Scene.js#L82](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/Scene.js#L82)  
> Since: 3.0.0

---

## sys

### sys: [Phaser.Scenes.Systems](scenes-systems.md)

**Description:**

The Scene Systems. You must never overwrite this property, or all hell will break lose.

> Source: [src/scene/Scene.js#L29](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/Scene.js#L29)  
> Since: 3.0.0

---

## textures

### textures: [Phaser.Textures.TextureManager](textures-texturemanager.md)

**Description:**

A reference to the Texture Manager.

This property will only be available if defined in the Scene Injection Map.

> Source: [src/scene/Scene.js#L93](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/Scene.js#L93)  
> Since: 3.0.0

---

## time

### time: [Phaser.Time.Clock](time-clock.md)

**Description:**

The Scene Time and Clock Plugin.

This property will only be available if defined in the Scene Injection Map and the plugin is installed.

> Source: [src/scene/Scene.js#L216](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/Scene.js#L216)  
> Since: 3.0.0

---

## tweens

### tweens: [Phaser.Tweens.TweenManager](tweens-tweenmanager.md)

**Description:**

The Scene Tween Manager Plugin.

This property will only be available if defined in the Scene Injection Map and the plugin is installed.

> Source: [src/scene/Scene.js#L227](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/Scene.js#L227)  
> Since: 3.0.0

---

# Public Methods

## update

### <instance> update(time, delta)

**Description:**

This method should be overridden by your own Scenes.

This method is called once per game step while the scene is running.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| time | number | No | The current time. Either a High Resolution Timer value if it comes from Request Animation Frame, or Date.now if using SetTimeout. |
| --- | --- | --- | --- |
| delta | number | No | The delta time in ms since the last frame. This is a smoothed and capped value based on the FPS rate. |

> Source: [src/scene/Scene.js#L307](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/Scene.js#L307)  
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
  + [children](#children)

    - [children: Phaser.GameObjects.DisplayList](#children-phasergameobjectsdisplaylist)
  + [data](#data)

    - [data: Phaser.Data.DataManager](#data-phaserdatadatamanager)
  + [events](#events)

    - [events: Phaser.Events.EventEmitter](#events-phasereventseventemitter)
  + [facebook](#facebook)

    - [facebook: Phaser.FacebookInstantGamesPlugin](#facebook-phaserfacebookinstantgamesplugin)
  + [game](#game)

    - [game: Phaser.Game](#game-phasergame)
  + [input](#input)

    - [input: Phaser.Input.InputPlugin](#input-phaserinputinputplugin)
  + [lights](#lights)

    - [lights: Phaser.GameObjects.LightsManager](#lights-phasergameobjectslightsmanager)
  + [load](#load)

    - [load: Phaser.Loader.LoaderPlugin](#load-phaserloaderloaderplugin)
  + [make](#make)

    - [make: Phaser.GameObjects.GameObjectCreator](#make-phasergameobjectsgameobjectcreator)
  + [matter](#matter)

    - [matter: Phaser.Physics.Matter.MatterPhysics](#matter-phaserphysicsmattermatterphysics)
  + [physics](#physics)

    - [physics: Phaser.Physics.Arcade.ArcadePhysics](#physics-phaserphysicsarcadearcadephysics)
  + [plugins](#plugins)

    - [plugins: Phaser.Plugins.PluginManager](#plugins-phaserpluginspluginmanager)
  + [registry](#registry)

    - [registry: Phaser.Data.DataManager](#registry-phaserdatadatamanager)
  + [renderer](#renderer)

    - [renderer: Phaser.Renderer.Canvas.CanvasRenderer, Phaser.Renderer.WebGL.WebGLRenderer](#renderer-phaserrenderercanvascanvasrenderer-phaserrendererwebglwebglrenderer)
  + [scale](#scale)

    - [scale: Phaser.Scale.ScaleManager](#scale-phaserscalescalemanager)
  + [scene](#scene)

    - [scene: Phaser.Scenes.ScenePlugin](#scene-phaserscenessceneplugin)
  + [sound](#sound)

    - [sound: Phaser.Sound.NoAudioSoundManager, Phaser.Sound.HTML5AudioSoundManager, Phaser.Sound.WebAudioSoundManager](#sound-phasersoundnoaudiosoundmanager-phasersoundhtml5audiosoundmanager-phasersoundwebaudiosoundmanager)
  + [sys](#sys)

    - [sys: Phaser.Scenes.Systems](#sys-phaserscenessystems)
  + [textures](#textures)

    - [textures: Phaser.Textures.TextureManager](#textures-phasertexturestexturemanager)
  + [time](#time)

    - [time: Phaser.Time.Clock](#time-phasertimeclock)
  + [tweens](#tweens)

    - [tweens: Phaser.Tweens.TweenManager](#tweens-phasertweenstweenmanager)
* [Public Methods](#public-methods)

  + [update](#update)

    - [<instance> update(time, delta)](#instance-updatetime-delta)

Back to top

©2025[Phaser](https://docs.phaser.io)



Scene