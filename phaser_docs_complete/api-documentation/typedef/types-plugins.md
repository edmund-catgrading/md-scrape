# Types.Plugins

Phaser.Types.Plugins

## CorePluginContainer

### <static> CorePluginContainer

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | string | No |  | The unique name of this plugin in the core plugin cache. |
| --- | --- | --- | --- | --- |
| plugin | function | No |  | The plugin to be stored. Should be the source object, not instantiated. |
| mapping | string | Yes |  | If this plugin is to be injected into the Scene Systems, this is the property key map used. |
| custom | boolean | Yes | false | Core Scene plugin or a Custom Scene plugin? |

**Type**: object

**Member of**: Phaser.Types.Plugins

> Source: [src/plugins/typedefs/CorePluginContainer.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/plugins/typedefs/CorePluginContainer.js#L1)  
> Since: 3.8.0

---

## CustomPluginContainer

### <static> CustomPluginContainer

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The unique name of this plugin in the custom plugin cache. |
| --- | --- | --- | --- |
| plugin | function | No | The plugin to be stored. Should be the source object, not instantiated. |

**Type**: object

**Member of**: Phaser.Types.Plugins

> Source: [src/plugins/typedefs/CustomPluginContainer.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/plugins/typedefs/CustomPluginContainer.js#L1)  
> Since: 3.8.0

---

## GlobalPlugin

### <static> GlobalPlugin

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The unique name of this plugin within the plugin cache. |
| --- | --- | --- | --- |
| plugin | function | No | An instance of the plugin. |
| active | boolean | Yes | Is the plugin active or not? |
| mapping | string | Yes | If this plugin is to be injected into the Scene Systems, this is the property key map used. |

**Type**: object

**Member of**: Phaser.Types.Plugins

> Source: [src/plugins/typedefs/GlobalPlugin.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/plugins/typedefs/GlobalPlugin.js#L1)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Types.Plugins](#typesplugins)

  + [CorePluginContainer](#coreplugincontainer)

    - [<static> CorePluginContainer](#static-coreplugincontainer)
  + [CustomPluginContainer](#customplugincontainer)

    - [<static> CustomPluginContainer](#static-customplugincontainer)
  + [GlobalPlugin](#globalplugin)

    - [<static> GlobalPlugin](#static-globalplugin)

Back to top

©2025[Phaser](https://docs.phaser.io)



Types.Plugins