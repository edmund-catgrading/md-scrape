# Phaser.Loader.FileTypesManager

Scope:
static

> Source: [src/loader/FileTypesManager.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/FileTypesManager.js#L9)

# Static functions

## destroy

### <static> destroy()

**Description:**

Removed all associated file types.

> Source: [src/loader/FileTypesManager.js#L50](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/FileTypesManager.js#L50)  
> Since: 3.0.0

---

## install

### <static> install(loader)

**Description:**

Static method called when a LoaderPlugin is created.

Loops through the local types object and injects all of them as

properties into the LoaderPlugin instance.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| loader | [Phaser.Loader.LoaderPlugin](../class/loader-loaderplugin.md) | No | The LoaderPlugin to install the types into. |
| --- | --- | --- | --- |

> Source: [src/loader/FileTypesManager.js#L15](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/FileTypesManager.js#L15)  
> Since: 3.0.0

---

## register

### <static> register(key, factoryFunction)

**Description:**

Static method called directly by the File Types.

The key is a reference to the function used to load the files via the Loader, i.e. `image`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The key that will be used as the method name in the LoaderPlugin. |
| --- | --- | --- | --- |
| factoryFunction | function | No | The function that will be called when LoaderPlugin.key is invoked. |

> Source: [src/loader/FileTypesManager.js#L34](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/FileTypesManager.js#L34)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Static functions](#static-functions)

  + [destroy](#destroy)

    - [<static> destroy()](#static-destroy)
  + [install](#install)

    - [<static> install(loader)](#static-installloader)
  + [register](#register)

    - [<static> register(key, factoryFunction)](#static-registerkey-factoryfunction)

Back to top

©2025[Phaser](https://docs.phaser.io)