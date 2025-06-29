# Phaser.Input.InputPluginCache

Scope:
static

> Source: [src/input/InputPluginCache.js#L13](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPluginCache.js#L13)

# Static functions

## getPlugin

### <static> getPlugin(key)

**Description:**

Returns the input plugin object from the cache based on the given key.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The key of the input plugin to get. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Types.Input.InputPluginContainer](../typedef/types-input.md) - The input plugin object.

> Source: [src/input/InputPluginCache.js#L40](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPluginCache.js#L40)  
> Since: 3.10.0

---

## install

### <static> install(target)

**Description:**

Installs all of the registered Input Plugins into the given target.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| target | [Phaser.Input.InputPlugin](../class/input-inputplugin.md) | No | The target InputPlugin to install the plugins into. |
| --- | --- | --- | --- |

> Source: [src/input/InputPluginCache.js#L56](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPluginCache.js#L56)  
> Since: 3.10.0

---

## register

### <static> register(key, plugin, mapping, settingsKey, configKey)

**Description:**

Static method called directly by the Core internal Plugins.

Key is a reference used to get the plugin from the plugins object (i.e. InputPlugin)

Plugin is the object to instantiate to create the plugin

Mapping is what the plugin is injected into the Scene.Systems as (i.e. input)

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | A reference used to get this plugin from the plugin cache. |
| --- | --- | --- | --- |
| plugin | function | No | The plugin to be stored. Should be the core object, not instantiated. |
| mapping | string | No | If this plugin is to be injected into the Input Plugin, this is the property key used. |
| settingsKey | string | No | The key in the Scene Settings to check to see if this plugin should install or not. |
| configKey | string | No | The key in the Game Config to check to see if this plugin should install or not. |

> Source: [src/input/InputPluginCache.js#L19](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPluginCache.js#L19)  
> Since: 3.10.0

---

## remove

### <static> remove(key)

**Description:**

Removes an input plugin based on the given key.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The key of the input plugin to remove. |
| --- | --- | --- | --- |

> Source: [src/input/InputPluginCache.js#L85](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPluginCache.js#L85)  
> Since: 3.10.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Static functions](#static-functions)

  + [getPlugin](#getplugin)

    - [<static> getPlugin(key)](#static-getpluginkey)
  + [install](#install)

    - [<static> install(target)](#static-installtarget)
  + [register](#register)

    - [<static> register(key, plugin, mapping, settingsKey, configKey)](#static-registerkey-plugin-mapping-settingskey-configkey)
  + [remove](#remove)

    - [<static> remove(key)](#static-removekey)

Back to top

©2025[Phaser](https://docs.phaser.io)