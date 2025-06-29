# Phaser.Loader

# Phaser.Loader.File

## createObjectURL

### <static> createObjectURL(image, blob, defaultType)

**Description:**

Static method for creating object URL using URL API and setting it as image 'src' attribute.

If URL API is not supported (usually on old browsers) it falls back to creating Base64 encoded url using FileReader.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| image | HTMLImageElement | No | Image object which 'src' attribute should be set to object URL. |
| --- | --- | --- | --- |
| blob | Blob | No | A Blob object to create an object URL for. |
| defaultType | string | No | Default mime type used if blob type is not available. |

> Source: [src/loader/File.js#L564](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/File.js#L564)  
> Since: 3.7.0

## revokeObjectURL

### <static> revokeObjectURL(image)

**Description:**

Static method for releasing an existing object URL which was previously created

by calling [Phaser.Loader.File.createObjectURL](../class/loader-file.md) method.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| image | HTMLImageElement | No | Image object which 'src' attribute should be revoked. |
| --- | --- | --- | --- |

> Source: [src/loader/File.js#L598](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/File.js#L598)  
> Since: 3.7.0

# Phaser.Loader.FileTypesManager

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

## destroy

### <static> destroy()

**Description:**

Removed all associated file types.

> Source: [src/loader/FileTypesManager.js#L50](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/FileTypesManager.js#L50)  
> Since: 3.0.0

## GetURL

### <static> GetURL(file, baseURL)

**Description:**

Given a File and a baseURL value this returns the URL the File will use to download from.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| file | [Phaser.Loader.File](../class/loader-file.md) | No | The File object. |
| --- | --- | --- | --- |
| baseURL | string | No | A default base URL. |

**Returns:** string - The URL the File will use.

> Source: [src/loader/GetURL.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/GetURL.js#L7)  
> Since: 3.0.0

## MergeXHRSettings

### <static> MergeXHRSettings(global, local)

**Description:**

Takes two XHRSettings Objects and creates a new XHRSettings object from them.

The new object is seeded by the values given in the global settings, but any setting in

the local object overrides the global ones.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| global | [Phaser.Types.Loader.XHRSettingsObject](../typedef/types-loader.md) | No | The global XHRSettings object. |
| --- | --- | --- | --- |
| local | [Phaser.Types.Loader.XHRSettingsObject](../typedef/types-loader.md) | No | The local XHRSettings object. |

**Returns:** [Phaser.Types.Loader.XHRSettingsObject](../typedef/types-loader.md) - A newly formed XHRSettings object.

> Source: [src/loader/MergeXHRSettings.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/MergeXHRSettings.js#L10)  
> Since: 3.0.0

## XHRLoader

### <static> XHRLoader(file, globalXHRSettings)

**Description:**

Creates a new XMLHttpRequest (xhr) object based on the given File and XHRSettings

and starts the download of it. It uses the Files own XHRSettings and merges them

with the global XHRSettings object to set the xhr values before download.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| file | [Phaser.Loader.File](../class/loader-file.md) | No | The File to download. |
| --- | --- | --- | --- |
| globalXHRSettings | [Phaser.Types.Loader.XHRSettingsObject](../typedef/types-loader.md) | No | The global XHRSettings object. |

**Returns:** XMLHttpRequest - The XHR object, or a FakeXHR Object in the base of base64 data.

> Source: [src/loader/XHRLoader.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/XHRLoader.js#L9)  
> Since: 3.0.0

## XHRSettings

### <static> XHRSettings([responseType], [async], [user], [password], [timeout], [withCredentials])

**Description:**

Creates an XHRSettings Object with default values.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| responseType | XMLHttpRequestResponseType | Yes | "''" | The responseType, such as 'text'. |
| --- | --- | --- | --- | --- |
| async | boolean | Yes | true | Should the XHR request use async or not? |
| user | string | Yes | "''" | Optional username for the XHR request. |
| password | string | Yes | "''" | Optional password for the XHR request. |
| timeout | number | Yes | 0 | Optional XHR timeout value. |
| withCredentials | boolean | Yes | false | Optional XHR withCredentials value. |

**Returns:** [Phaser.Types.Loader.XHRSettingsObject](../typedef/types-loader.md) - The XHRSettings object as used by the Loader.

> Source: [src/loader/XHRSettings.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/XHRSettings.js#L7)  
> Since: 3.0.0

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Phaser.Loader.File](#phaserloaderfile)

  + [createObjectURL](#createobjecturl)

    - [<static> createObjectURL(image, blob, defaultType)](#static-createobjecturlimage-blob-defaulttype)
  + [revokeObjectURL](#revokeobjecturl)

    - [<static> revokeObjectURL(image)](#static-revokeobjecturlimage)
* [Phaser.Loader.FileTypesManager](#phaserloaderfiletypesmanager)

  + [install](#install)

    - [<static> install(loader)](#static-installloader)
  + [register](#register)

    - [<static> register(key, factoryFunction)](#static-registerkey-factoryfunction)
  + [destroy](#destroy)

    - [<static> destroy()](#static-destroy)
  + [GetURL](#geturl)

    - [<static> GetURL(file, baseURL)](#static-geturlfile-baseurl)
  + [MergeXHRSettings](#mergexhrsettings)

    - [<static> MergeXHRSettings(global, local)](#static-mergexhrsettingsglobal-local)
  + [XHRLoader](#xhrloader)

    - [<static> XHRLoader(file, globalXHRSettings)](#static-xhrloaderfile-globalxhrsettings)
  + [XHRSettings](#xhrsettings)

    - [<static> XHRSettings([responseType], [async], [user], [password], [timeout], [withCredentials])](#static-xhrsettingsresponsetype-async-user-password-timeout-withcredentials)

Back to top

©2025[Phaser](https://docs.phaser.io)