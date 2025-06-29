# Phaser.Types.Scenes

Scope:
static

> Source: [src/scene/typedefs/index.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/typedefs/index.js#L7)

# Static functions

## CreateSceneFromObjectConfig

### CreateSceneFromObjectConfig

> Source: [src/scene/typedefs/CreateSceneFromObjectConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/typedefs/CreateSceneFromObjectConfig.js#L1)  
> Since: 3.17.0

---

## SceneCreateCallback

### SceneCreateCallback

**Description:**

Can be defined on your own Scenes. Use it to create your game objects.

This method is called by the Scene Manager when the scene starts, after `init()` and `preload()`.

If the LoaderPlugin started after `preload()`, then this method is called only after loading is complete.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| data | object | No | Any data passed via `ScenePlugin.add()` or `ScenePlugin.start()`. Same as Scene.settings.data. |
| --- | --- | --- | --- |

> Source: [src/scene/typedefs/SceneCreateCallback.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/typedefs/SceneCreateCallback.js#L1)  
> Since: 3.0.0

---

## SceneInitCallback

### SceneInitCallback

**Description:**

Can be defined on your own Scenes.

This method is called by the Scene Manager when the scene starts, before `preload()` and `create()`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| data | object | No | Any data passed via `ScenePlugin.add()` or `ScenePlugin.start()`. Same as Scene.settings.data. |
| --- | --- | --- | --- |

> Source: [src/scene/typedefs/SceneInitCallback.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/typedefs/SceneInitCallback.js#L1)  
> Since: 3.0.0

---

## ScenePreloadCallback

### ScenePreloadCallback

**Description:**

Can be defined on your own Scenes. Use it to load assets.

This method is called by the Scene Manager, after `init()` and before `create()`, only if the Scene has a LoaderPlugin.

After this method completes, if the LoaderPlugin's queue isn't empty, the LoaderPlugin will start automatically.

> Source: [src/scene/typedefs/ScenePreloadCallback.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/typedefs/ScenePreloadCallback.js#L1)  
> Since: 3.0.0

---

## SceneTransitionConfig

### SceneTransitionConfig

> Source: [src/scene/typedefs/SceneTransitionConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/typedefs/SceneTransitionConfig.js#L1)  
> Since: 3.5.0

---

## SceneTransitionOnStartCallback

### SceneTransitionOnStartCallback

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| fromScene | [Phaser.Scene](../class/scene.md) | No | Scene instance to transition from. |
| --- | --- | --- | --- |
| toScene | [Phaser.Scene](../class/scene.md) | No | Scene instance to transition to. |

> Source: [src/scene/typedefs/SceneTransitionStartCallback.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/typedefs/SceneTransitionStartCallback.js#L1)  
> Since: 3.60.0

---

## SceneType

### SceneType

> Source: [src/scene/typedefs/SceneType.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/typedefs/SceneType.js#L1)  
> Since: 3.60.0

---

## SceneUpdateCallback

### SceneUpdateCallback

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| time | number | No | The current time. Either a High Resolution Timer value if it comes from Request Animation Frame, or Date.now if using SetTimeout. |
| --- | --- | --- | --- |
| delta | number | No | The delta time in ms since the last frame. This is a smoothed and capped value based on the FPS rate. |

> Source: [src/scene/typedefs/SceneUpdateCallback.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/typedefs/SceneUpdateCallback.js#L1)  
> Since: 3.0.0

---

## SettingsConfig

### SettingsConfig

> Source: [src/scene/typedefs/SettingsConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/typedefs/SettingsConfig.js#L1)  
> Since: 3.0.0

---

## SettingsObject

### SettingsObject

> Source: [src/scene/typedefs/SettingsObject.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/typedefs/SettingsObject.js#L1)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Static functions](#static-functions)

  + [CreateSceneFromObjectConfig](#createscenefromobjectconfig)

    - [CreateSceneFromObjectConfig](#createscenefromobjectconfig-1)
  + [SceneCreateCallback](#scenecreatecallback)

    - [SceneCreateCallback](#scenecreatecallback-1)
  + [SceneInitCallback](#sceneinitcallback)

    - [SceneInitCallback](#sceneinitcallback-1)
  + [ScenePreloadCallback](#scenepreloadcallback)

    - [ScenePreloadCallback](#scenepreloadcallback-1)
  + [SceneTransitionConfig](#scenetransitionconfig)

    - [SceneTransitionConfig](#scenetransitionconfig-1)
  + [SceneTransitionOnStartCallback](#scenetransitiononstartcallback)

    - [SceneTransitionOnStartCallback](#scenetransitiononstartcallback-1)
  + [SceneType](#scenetype)

    - [SceneType](#scenetype-1)
  + [SceneUpdateCallback](#sceneupdatecallback)

    - [SceneUpdateCallback](#sceneupdatecallback-1)
  + [SettingsConfig](#settingsconfig)

    - [SettingsConfig](#settingsconfig-1)
  + [SettingsObject](#settingsobject)

    - [SettingsObject](#settingsobject-1)

Back to top

©2025[Phaser](https://docs.phaser.io)