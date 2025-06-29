# Phaser.Plugins

# Phaser.Plugins.PluginCache

## register

### <static> register(key, plugin, mapping, [custom])

**Description:**

Static method called directly by the Core internal Plugins.

Key is a reference used to get the plugin from the plugins object (i.e. InputPlugin)

Plugin is the object to instantiate to create the plugin

Mapping is what the plugin is injected into the Scene.Systems as (i.e. input)

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | string | No |  | A reference used to get this plugin from the plugin cache. |
| --- | --- | --- | --- | --- |
| plugin | function | No |  | The plugin to be stored. Should be the core object, not instantiated. |
| mapping | string | No |  | If this plugin is to be injected into the Scene Systems, this is the property key map used. |
| custom | boolean | Yes | false | Core Scene plugin or a Custom Scene plugin? |

> Source: [src/plugins/PluginCache.js#L21](https://github.com/phaserjs/phaser/blob/v3.87.0/src/plugins/PluginCache.js#L21)  
> Since: 3.8.0

## registerCustom

### <static> registerCustom(key, plugin, mapping, data)

**Description:**

Stores a custom plugin in the global plugin cache.

The key must be unique, within the scope of the cache.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | A reference used to get this plugin from the plugin cache. |
| --- | --- | --- | --- |
| plugin | function | No | The plugin to be stored. Should be the core object, not instantiated. |
| mapping | string | No | If this plugin is to be injected into the Scene Systems, this is the property key map used. |
| data | any | No | A value to be passed to the plugin's `init` method. |

> Source: [src/plugins/PluginCache.js#L42](https://github.com/phaserjs/phaser/blob/v3.87.0/src/plugins/PluginCache.js#L42)  
> Since: 3.8.0

## hasCore

### <static> hasCore(key)

**Description:**

Checks if the given key is already being used in the core plugin cache.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The key to check for. |
| --- | --- | --- | --- |

**Returns:** boolean - `true` if the key is already in use in the core cache, otherwise `false`.

> Source: [src/plugins/PluginCache.js#L59](https://github.com/phaserjs/phaser/blob/v3.87.0/src/plugins/PluginCache.js#L59)  
> Since: 3.8.0

## hasCustom

### <static> hasCustom(key)

**Description:**

Checks if the given key is already being used in the custom plugin cache.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The key to check for. |
| --- | --- | --- | --- |

**Returns:** boolean - `true` if the key is already in use in the custom cache, otherwise `false`.

> Source: [src/plugins/PluginCache.js#L74](https://github.com/phaserjs/phaser/blob/v3.87.0/src/plugins/PluginCache.js#L74)  
> Since: 3.8.0

## getCore

### <static> getCore(key)

**Description:**

Returns the core plugin object from the cache based on the given key.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The key of the core plugin to get. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Types.Plugins.CorePluginContainer](../typedef/types-plugins.md) - The core plugin object.

> Source: [src/plugins/PluginCache.js#L89](https://github.com/phaserjs/phaser/blob/v3.87.0/src/plugins/PluginCache.js#L89)  
> Since: 3.8.0

## getCustom

### <static> getCustom(key)

**Description:**

Returns the custom plugin object from the cache based on the given key.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The key of the custom plugin to get. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Types.Plugins.CustomPluginContainer](../typedef/types-plugins.md) - The custom plugin object.

> Source: [src/plugins/PluginCache.js#L104](https://github.com/phaserjs/phaser/blob/v3.87.0/src/plugins/PluginCache.js#L104)  
> Since: 3.8.0

## getCustomClass

### <static> getCustomClass(key)

**Description:**

Returns an object from the custom cache based on the given key that can be instantiated.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The key of the custom plugin to get. |
| --- | --- | --- | --- |

**Returns:** function - The custom plugin object.

> Source: [src/plugins/PluginCache.js#L119](https://github.com/phaserjs/phaser/blob/v3.87.0/src/plugins/PluginCache.js#L119)  
> Since: 3.8.0

## remove

### <static> remove(key)

**Description:**

Removes a core plugin based on the given key.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The key of the core plugin to remove. |
| --- | --- | --- | --- |

> Source: [src/plugins/PluginCache.js#L134](https://github.com/phaserjs/phaser/blob/v3.87.0/src/plugins/PluginCache.js#L134)  
> Since: 3.8.0

## removeCustom

### <static> removeCustom(key)

**Description:**

Removes a custom plugin based on the given key.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The key of the custom plugin to remove. |
| --- | --- | --- | --- |

> Source: [src/plugins/PluginCache.js#L150](https://github.com/phaserjs/phaser/blob/v3.87.0/src/plugins/PluginCache.js#L150)  
> Since: 3.8.0

## destroyCorePlugins

### <static> destroyCorePlugins()

**Description:**

Removes all Core Plugins.

This includes all of the internal system plugins that Phaser needs, like the Input Plugin and Loader Plugin.

So be sure you only call this if you do not wish to run Phaser again.

> Source: [src/plugins/PluginCache.js#L166](https://github.com/phaserjs/phaser/blob/v3.87.0/src/plugins/PluginCache.js#L166)  
> Since: 3.12.0

## destroyCustomPlugins

### <static> destroyCustomPlugins()

**Description:**

Removes all Custom Plugins.

> Source: [src/plugins/PluginCache.js#L186](https://github.com/phaserjs/phaser/blob/v3.87.0/src/plugins/PluginCache.js#L186)  
> Since: 3.12.0

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Phaser.Plugins.PluginCache](#phaserpluginsplugincache)

  + [register](#register)

    - [<static> register(key, plugin, mapping, [custom])](#static-registerkey-plugin-mapping-custom)
  + [registerCustom](#registercustom)

    - [<static> registerCustom(key, plugin, mapping, data)](#static-registercustomkey-plugin-mapping-data)
  + [hasCore](#hascore)

    - [<static> hasCore(key)](#static-hascorekey)
  + [hasCustom](#hascustom)

    - [<static> hasCustom(key)](#static-hascustomkey)
  + [getCore](#getcore)

    - [<static> getCore(key)](#static-getcorekey)
  + [getCustom](#getcustom)

    - [<static> getCustom(key)](#static-getcustomkey)
  + [getCustomClass](#getcustomclass)

    - [<static> getCustomClass(key)](#static-getcustomclasskey)
  + [remove](#remove)

    - [<static> remove(key)](#static-removekey)
  + [removeCustom](#removecustom)

    - [<static> removeCustom(key)](#static-removecustomkey)
  + [destroyCorePlugins](#destroycoreplugins)

    - [<static> destroyCorePlugins()](#static-destroycoreplugins)
  + [destroyCustomPlugins](#destroycustomplugins)

    - [<static> destroyCustomPlugins()](#static-destroycustomplugins)

Back to top

©2025[Phaser](https://docs.phaser.io)