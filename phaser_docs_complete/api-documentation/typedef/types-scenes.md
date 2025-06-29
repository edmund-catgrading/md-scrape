# Types.Scenes

Phaser.Types.Scenes

## CreateSceneFromObjectConfig

### <static> CreateSceneFromObjectConfig

| name | type | optional | description |
| --- | --- | --- | --- |
| init | [Phaser.Types.Scenes.SceneInitCallback](types-scenes.md) | Yes | The scene's init callback. |
| --- | --- | --- | --- |
| preload | [Phaser.Types.Scenes.ScenePreloadCallback](types-scenes.md) | Yes | The scene's preload callback. |
| create | [Phaser.Types.Scenes.SceneCreateCallback](types-scenes.md) | Yes | The scene's create callback. |
| update | [Phaser.Types.Scenes.SceneUpdateCallback](types-scenes.md) | Yes | The scene's update callback. See {@link Phaser.Scene#update}. |
| extend | any | Yes | Any additional properties, which will be copied to the Scene after it's created (except `data` or `sys`). |
| extend.data | any | Yes | Any values, which will be merged into the Scene's Data Manager store. |

**Type**: object

**Member of**: Phaser.Types.Scenes

> Source: [src/scene/typedefs/CreateSceneFromObjectConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/typedefs/CreateSceneFromObjectConfig.js#L1)  
> Since: 3.17.0

---

## SceneCreateCallback

### <static> SceneCreateCallback

Can be defined on your own Scenes. Use it to create your game objects.

This method is called by the Scene Manager when the scene starts, after `init()` and `preload()`.

If the LoaderPlugin started after `preload()`, then this method is called only after loading is complete.

**Type**: function

**Member of**: Phaser.Types.Scenes

> Source: [src/scene/typedefs/SceneCreateCallback.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/typedefs/SceneCreateCallback.js#L1)  
> Since: 3.0.0

---

## SceneInitCallback

### <static> SceneInitCallback

Can be defined on your own Scenes.

This method is called by the Scene Manager when the scene starts, before `preload()` and `create()`.

**Type**: function

**Member of**: Phaser.Types.Scenes

> Source: [src/scene/typedefs/SceneInitCallback.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/typedefs/SceneInitCallback.js#L1)  
> Since: 3.0.0

---

## ScenePreloadCallback

### <static> ScenePreloadCallback

Can be defined on your own Scenes. Use it to load assets.

This method is called by the Scene Manager, after `init()` and before `create()`, only if the Scene has a LoaderPlugin.

After this method completes, if the LoaderPlugin's queue isn't empty, the LoaderPlugin will start automatically.

**Type**: function

**Member of**: Phaser.Types.Scenes

> Source: [src/scene/typedefs/ScenePreloadCallback.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/typedefs/ScenePreloadCallback.js#L1)  
> Since: 3.0.0

---

## SceneTransitionConfig

### <static> SceneTransitionConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| target | string | No |  | The Scene key to transition to. |
| --- | --- | --- | --- | --- |
| duration | number | Yes | 1000 | The duration, in ms, for the transition to last. |
| sleep | boolean | Yes | false | Will the Scene responsible for the transition be sent to sleep on completion (`true`), or stopped? (`false`) |
| remove | boolean | Yes | false | Will the Scene responsible for the transition be removed from the Scene Manager after the transition completes? |
| allowInput | boolean | Yes | false | Will the Scenes Input system be able to process events while it is transitioning in or out? |
| moveAbove | boolean | Yes |  | Move the target Scene to be above this one before the transition starts. |
| moveBelow | boolean | Yes |  | Move the target Scene to be below this one before the transition starts. |
| onUpdate | function | Yes |  | This callback is invoked every frame for the duration of the transition. |
| onUpdateScope | any | Yes |  | The context in which the callback is invoked. |
| onStart | [Phaser.Types.Scenes.SceneTransitionOnStartCallback](types-scenes.md) | Yes |  | This callback is invoked when transition starting. |
| onStartScope | any | Yes |  | The context in which the callback is invoked. |
| data | any | Yes |  | An object containing any data you wish to be passed to the target scene's init / create methods (if sleep is false) or to the target scene's wake event callback (if sleep is true). |

**Type**: object

**Member of**: Phaser.Types.Scenes

> Source: [src/scene/typedefs/SceneTransitionConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/typedefs/SceneTransitionConfig.js#L1)  
> Since: 3.5.0

---

## SceneTransitionOnStartCallback

### <static> SceneTransitionOnStartCallback

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| duration | number | Yes | 1000 | The duration, in ms, for the transition to last. |
| --- | --- | --- | --- | --- |

**Type**: function

**Member of**: Phaser.Types.Scenes

> Source: [src/scene/typedefs/SceneTransitionStartCallback.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/typedefs/SceneTransitionStartCallback.js#L1)  
> Since: 3.60.0

---

## SceneType

### <static> SceneType

**Type**: [Phaser.Scene](../class/scene.md) | [Phaser.Types.Scenes.SettingsConfig](types-scenes.md) | [Phaser.Types.Scenes.CreateSceneFromObjectConfig](types-scenes.md) | function

**Member of**: Phaser.Types.Scenes

> Source: [src/scene/typedefs/SceneType.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/typedefs/SceneType.js#L1)  
> Since: 3.60.0

---

## SceneUpdateCallback

### <static> SceneUpdateCallback

**Type**: function

**Member of**: Phaser.Types.Scenes

> Source: [src/scene/typedefs/SceneUpdateCallback.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/typedefs/SceneUpdateCallback.js#L1)  
> Since: 3.0.0

---

## SettingsConfig

### <static> SettingsConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | string | Yes |  | The unique key of this Scene. Must be unique within the entire Game instance. |
| --- | --- | --- | --- | --- |
| active | boolean | Yes | false | Does the Scene start as active or not? An active Scene updates each step. |
| visible | boolean | Yes | true | Does the Scene start as visible or not? A visible Scene renders each step. |
| pack | false | [Phaser.Types.Loader.FileTypes.PackFileSection](types-loader-filetypes.md) | Yes | false | Files to be loaded before the Scene begins. |
| cameras | [Phaser.Types.Cameras.Scene2D.CameraConfig](types-cameras-scene2d.md) | Array.<[Phaser.Types.Cameras.Scene2D.CameraConfig](types-cameras-scene2d.md)> | Yes | null | An optional Camera configuration object. |
| map | Object.<string, string> | Yes |  | Overwrites the default injection map for a scene. |
| mapAdd | Object.<string, string> | Yes |  | Extends the injection map for a scene. |
| physics | [Phaser.Types.Core.PhysicsConfig](types-core.md) | Yes | "{}" | The physics configuration object for the Scene. |
| loader | [Phaser.Types.Core.LoaderConfig](types-core.md) | Yes | "{}" | The loader configuration object for the Scene. |
| plugins | false | \* | Yes | false | The plugin configuration object for the Scene. |

**Type**: object

**Member of**: Phaser.Types.Scenes

> Source: [src/scene/typedefs/SettingsConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/typedefs/SettingsConfig.js#L1)  
> Since: 3.0.0

---

## SettingsObject

### <static> SettingsObject

| name | type | optional | description |
| --- | --- | --- | --- |
| status | number | No | The current status of the Scene. Maps to the Scene constants. |
| --- | --- | --- | --- |
| key | string | No | The unique key of this Scene. Unique within the entire Game instance. |
| active | boolean | No | The active state of this Scene. An active Scene updates each step. |
| visible | boolean | No | The visible state of this Scene. A visible Scene renders each step. |
| isBooted | boolean | No | Has the Scene finished booting? |
| isTransition | boolean | No | Is the Scene in a state of transition? |
| transitionFrom | [Phaser.Scene](../class/scene.md) | No | The Scene this Scene is transitioning from, if set. |
| transitionDuration | number | No | The duration of the transition, if set. |
| transitionAllowInput | boolean | No | Is this Scene allowed to receive input during transitions? |
| data | object | No | a data bundle passed to this Scene from the Scene Manager. |
| pack | false | [Phaser.Types.Loader.FileTypes.PackFileSection](types-loader-filetypes.md) | No | Files to be loaded before the Scene begins. |
| cameras | [Phaser.Types.Cameras.Scene2D.CameraConfig](types-cameras-scene2d.md) | Array.<[Phaser.Types.Cameras.Scene2D.CameraConfig](types-cameras-scene2d.md)> | No | The Camera configuration object. |
| map | Object.<string, string> | No | The Scene's Injection Map. |
| physics | [Phaser.Types.Core.PhysicsConfig](types-core.md) | No | The physics configuration object for the Scene. |
| loader | [Phaser.Types.Core.LoaderConfig](types-core.md) | No | The loader configuration object for the Scene. |
| plugins | false | \* | No | The plugin configuration object for the Scene. |

**Type**: object

**Member of**: Phaser.Types.Scenes

> Source: [src/scene/typedefs/SettingsObject.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/typedefs/SettingsObject.js#L1)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Types.Scenes](#typesscenes)

  + [CreateSceneFromObjectConfig](#createscenefromobjectconfig)

    - [<static> CreateSceneFromObjectConfig](#static-createscenefromobjectconfig)
  + [SceneCreateCallback](#scenecreatecallback)

    - [<static> SceneCreateCallback](#static-scenecreatecallback)
  + [SceneInitCallback](#sceneinitcallback)

    - [<static> SceneInitCallback](#static-sceneinitcallback)
  + [ScenePreloadCallback](#scenepreloadcallback)

    - [<static> ScenePreloadCallback](#static-scenepreloadcallback)
  + [SceneTransitionConfig](#scenetransitionconfig)

    - [<static> SceneTransitionConfig](#static-scenetransitionconfig)
  + [SceneTransitionOnStartCallback](#scenetransitiononstartcallback)

    - [<static> SceneTransitionOnStartCallback](#static-scenetransitiononstartcallback)
  + [SceneType](#scenetype)

    - [<static> SceneType](#static-scenetype)
  + [SceneUpdateCallback](#sceneupdatecallback)

    - [<static> SceneUpdateCallback](#static-sceneupdatecallback)
  + [SettingsConfig](#settingsconfig)

    - [<static> SettingsConfig](#static-settingsconfig)
  + [SettingsObject](#settingsobject)

    - [<static> SettingsObject](#static-settingsobject)

Back to top

©2025[Phaser](https://docs.phaser.io)



Types.Scenes