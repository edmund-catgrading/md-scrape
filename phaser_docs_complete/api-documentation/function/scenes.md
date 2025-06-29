# Phaser.Scenes

## GetPhysicsPlugins

### <static> GetPhysicsPlugins(sys)

**Description:**

Builds an array of which physics plugins should be activated for the given Scene.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| sys | [Phaser.Scenes.Systems](../class/scenes-systems.md) | No | The scene system to get the physics systems of. |
| --- | --- | --- | --- |

**Returns:** array - An array of Physics systems to start for this Scene.

> Source: [src/scene/GetPhysicsPlugins.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/GetPhysicsPlugins.js#L10)  
> Since: 3.0.0

## GetScenePlugins

### <static> GetScenePlugins(sys)

**Description:**

Builds an array of which plugins (not including physics plugins) should be activated for the given Scene.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| sys | [Phaser.Scenes.Systems](../class/scenes-systems.md) | No | The Scene Systems object to check for plugins. |
| --- | --- | --- | --- |

**Returns:** array - An array of all plugins which should be activated, either the default ones or the ones configured in the Scene Systems object.

> Source: [src/scene/GetScenePlugins.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/GetScenePlugins.js#L9)  
> Since: 3.0.0

# Phaser.Scenes.Settings

## create

### <static> create(config)

**Description:**

Takes a Scene configuration object and returns a fully formed System Settings object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| config | string | [Phaser.Types.Scenes.SettingsConfig](../typedef/types-scenes.md) | No | The Scene configuration object used to create this Scene Settings. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Types.Scenes.SettingsObject](../typedef/types-scenes.md) - The Scene Settings object created as a result of the config and default settings.

> Source: [src/scene/Settings.js#L18](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/Settings.js#L18)  
> Since: 3.0.0

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [GetPhysicsPlugins](#getphysicsplugins)

  + [<static> GetPhysicsPlugins(sys)](#static-getphysicspluginssys)
* [GetScenePlugins](#getsceneplugins)

  + [<static> GetScenePlugins(sys)](#static-getscenepluginssys)
* [Phaser.Scenes.Settings](#phaserscenessettings)

  + [create](#create)

    - [<static> create(config)](#static-createconfig)

Back to top

©2025[Phaser](https://docs.phaser.io)