# File

Phaser.Loader.File

The base File class used by all File Types that the Loader can support.

You shouldn't create an instance of a File directly, but should extend it with your own class, setting a custom type and processing methods.

**Constructor**

`new File(loader, fileConfig)`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| loader | [Phaser.Loader.LoaderPlugin](loader-loaderplugin.md) | No | The Loader that is going to load this File. |
| --- | --- | --- | --- |
| fileConfig | [Phaser.Types.Loader.FileConfig](../typedef/types-loader.md) | No | The file configuration object, as created by the file type. |

---

**Scope**: static

> Source: [src/loader/File.js#L16](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/File.js#L16)  
> Since: 3.0.0

# Public Members

## base64

### base64: boolean

**Description:**

Does this File contain a data URI?

> Source: [src/loader/File.js#L236](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/File.js#L236)  
> Since: 3.80.0

---

## bytesLoaded

### bytesLoaded: number

**Description:**

Updated as the file loads.

Only set if loading via XHR.

> Source: [src/loader/File.js#L165](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/File.js#L165)  
> Since: 3.0.0

---

## bytesTotal

### bytesTotal: number

**Description:**

The total size of this file.

Set by onProgress and only if loading via XHR.

> Source: [src/loader/File.js#L154](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/File.js#L154)  
> Since: 3.0.0

---

## cache

### cache: [Phaser.Cache.BaseCache](cache-basecache.md), [Phaser.Textures.TextureManager](textures-texturemanager.md)

**Description:**

A reference to the Cache, or Texture Manager, that is going to store this file if it loads.

> Source: [src/loader/File.js#L44](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/File.js#L44)  
> Since: 3.7.0

---

## config

### config: \*

**Description:**

A config object that can be used by file types to store transitional data.

> Source: [src/loader/File.js#L206](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/File.js#L206)  
> Since: 3.0.0

---

## crossOrigin

### crossOrigin: string, undefined

**Description:**

For CORs based loading.

If this is undefined then the File will check BaseLoader.crossOrigin and use that (if set)

> Source: [src/loader/File.js#L187](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/File.js#L187)  
> Since: 3.0.0

---

## data

### data: \*

**Description:**

The processed file data, stored here after the file has loaded.

> Source: [src/loader/File.js#L197](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/File.js#L197)  
> Since: 3.0.0

---

## key

### key: string

**Description:**

Unique cache key (unique within its file type)

> Source: [src/loader/File.js#L67](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/File.js#L67)  
> Since: 3.0.0

---

## linkFile

### linkFile: [Phaser.Loader.File](loader-file.md)

**Description:**

Does this file have an associated linked file? Such as an image and a normal map.

Atlases and Bitmap Fonts use the multiFile, because those files need loading together but aren't

actually bound by data, where-as a linkFile is.

> Source: [src/loader/File.js#L225](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/File.js#L225)  
> Since: 3.7.0

---

## loader

### loader: [Phaser.Loader.LoaderPlugin](loader-loaderplugin.md)

**Description:**

A reference to the Loader that is going to load this file.

> Source: [src/loader/File.js#L35](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/File.js#L35)  
> Since: 3.0.0

---

## multiFile

### multiFile: [Phaser.Loader.MultiFile](loader-multifile.md)

**Description:**

If this is a multipart file, i.e. an atlas and its json together, then this is a reference

to the parent MultiFile. Set and used internally by the Loader or specific file types.

> Source: [src/loader/File.js#L215](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/File.js#L215)  
> Since: 3.7.0

---

## percentComplete

### percentComplete: number

**Description:**

A percentage value between 0 and 1 indicating how much of this file has loaded.

Only set if loading via XHR.

> Source: [src/loader/File.js#L176](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/File.js#L176)  
> Since: 3.0.0

---

## retryAttempts

### retryAttempts: number

**Description:**

The counter for the number of times to retry loading this file before it fails.

You can set this property value in the FileConfig object. If not present,

this property is read from the `LoaderPlugin.maxRetries` property when

this File instance is created.

You can set this value via the Game Config, or you can adjust the `LoaderPlugin` property

at any point after the Loader has started. However, it will not apply to files

that have already been added to the Loader, only those added after this value

is changed.

> Source: [src/loader/File.js#L245](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/File.js#L245)  
> Since: 3.85.0

---

## src

### src: string

**Description:**

The final URL this file will load from, including baseURL and path.

Set automatically when the Loader calls 'load' on this file.

> Source: [src/loader/File.js#L112](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/File.js#L112)  
> Since: 3.0.0

---

## state

### state: number

**Description:**

The current state of the file. One of the FILE\_CONST values.

> Source: [src/loader/File.js#L145](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/File.js#L145)  
> Since: 3.0.0

---

## type

### type: string

**Description:**

The file type string (image, json, etc) for sorting within the Loader.

> Source: [src/loader/File.js#L53](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/File.js#L53)  
> Since: 3.0.0

---

## url

### url: object, string

**Description:**

The URL of the file, not including baseURL.

Automatically has Loader.path prepended to it if a string.

Can also be a JavaScript Object, such as the results of parsing JSON data.

> Source: [src/loader/File.js#L99](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/File.js#L99)  
> Since: 3.0.0

---

## xhrLoader

### xhrLoader: XMLHttpRequest

**Description:**

The XMLHttpRequest instance (as created by XHR Loader) that is loading this File.

> Source: [src/loader/File.js#L136](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/File.js#L136)  
> Since: 3.0.0

---

## xhrSettings

### xhrSettings: [Phaser.Types.Loader.XHRSettingsObject](../typedef/types-loader.md)

**Description:**

The merged XHRSettings for this file.

> Source: [src/loader/File.js#L122](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/File.js#L122)  
> Since: 3.0.0

---

# Public Methods

## addToCache

### <instance> addToCache()

**Description:**

Adds this file to its target cache upon successful loading and processing.

This method is often overridden by specific file types.

> Source: [src/loader/File.js#L502](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/File.js#L502)  
> Since: 3.7.0

---

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

---

## destroy

### <instance> destroy()

**Description:**

Destroy this File and any references it holds.

> Source: [src/loader/File.js#L546](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/File.js#L546)  
> Since: 3.7.0

---

## hasCacheConflict

### <instance> hasCacheConflict()

**Description:**

Checks if a key matching the one used by this file exists in the target Cache or not.

This is called automatically by the LoaderPlugin to decide if the file can be safely

loaded or will conflict.

**Returns:** boolean - `true` if adding this file will cause a conflict, otherwise `false`.

> Source: [src/loader/File.js#L487](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/File.js#L487)  
> Since: 3.7.0

---

## load

### <instance> load()

**Description:**

Called by the Loader, starts the actual file downloading.

During the load the methods onLoad, onError and onProgress are called, based on the XHR events.

You shouldn't normally call this method directly, it's meant to be invoked by the Loader.

> Source: [src/loader/File.js#L296](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/File.js#L296)  
> Since: 3.0.0

---

## onBase64Load

### <instance> onBase64Load(xhr)

**Description:**

Called by the XHRLoader if it was given a File with base64 data to load.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| xhr | XMLHttpRequest | No | The FakeXHR object containing the decoded base64 data. |
| --- | --- | --- | --- |

> Source: [src/loader/File.js#L364](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/File.js#L364)  
> Since: 3.80.0

---

## onError

### <instance> onError(xhr, event)

**Description:**

Called if the file errors while loading, is sent a DOM ProgressEvent.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| xhr | XMLHttpRequest | No | The XMLHttpRequest that caused this onload event. |
| --- | --- | --- | --- |
| event | ProgressEvent | No | The DOM ProgressEvent that resulted from this error. |

> Source: [src/loader/File.js#L385](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/File.js#L385)  
> Since: 3.0.0

---

## onLoad

### <instance> onLoad(xhr, event)

**Description:**

Called when the file finishes loading, is sent a DOM ProgressEvent.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| xhr | XMLHttpRequest | No | The XMLHttpRequest that caused this onload event. |
| --- | --- | --- | --- |
| event | ProgressEvent | No | The DOM ProgressEvent that resulted from this load. |

> Source: [src/loader/File.js#L331](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/File.js#L331)  
> Since: 3.0.0

---

## onProcess

### <instance> onProcess()

**Description:**

Usually overridden by the FileTypes and is called by Loader.nextFile.

This method controls what extra work this File does with its loaded data, for example a JSON file will parse itself during this stage.

> Source: [src/loader/File.js#L432](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/File.js#L432)  
> Since: 3.0.0

---

## onProcessComplete

### <instance> onProcessComplete()

**Description:**

Called when the File has completed processing.

Checks on the state of its multifile, if set.

> Source: [src/loader/File.js#L446](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/File.js#L446)  
> Since: 3.7.0

---

## onProcessError

### <instance> onProcessError()

**Description:**

Called when the File has completed processing but it generated an error.

Checks on the state of its multifile, if set.

> Source: [src/loader/File.js#L465](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/File.js#L465)  
> Since: 3.7.0

---

## onProgress

### <instance> onProgress(event)

**Description:**

Called during the file load progress. Is sent a DOM ProgressEvent.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | ProgressEvent | No | The DOM ProgressEvent. |
| --- | --- | --- | --- |

**Fires:** [Phaser.Loader.Events#event:FILE\_PROGRESS](../event/loader-events.md)

> Source: [src/loader/File.js#L410](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/File.js#L410)  
> Since: 3.0.0

---

## pendingDestroy

### <instance> pendingDestroy()

**Description:**

Called once the file has been added to its cache and is now ready for deletion from the Loader.

It will emit a `filecomplete` event from the LoaderPlugin.

**Fires:** [Phaser.Loader.Events#event:FILE\_COMPLETE](../event/loader-events.md), [Phaser.Loader.Events#event:FILE\_KEY\_COMPLETE](../event/loader-events.md)

> Source: [src/loader/File.js#L517](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/File.js#L517)  
> Since: 3.7.0

---

## resetXHR

### <instance> resetXHR()

**Description:**

Resets the XHRLoader instance this file is using.

> Source: [src/loader/File.js#L280](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/File.js#L280)  
> Since: 3.0.0

---

## revokeObjectURL

### <static> revokeObjectURL(image)

**Description:**

Static method for releasing an existing object URL which was previously created

by calling [Phaser.Loader.File.createObjectURL](loader-file.md) method.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| image | HTMLImageElement | No | Image object which 'src' attribute should be revoked. |
| --- | --- | --- | --- |

> Source: [src/loader/File.js#L598](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/File.js#L598)  
> Since: 3.7.0

---

## setLink

### <instance> setLink(fileB)

**Description:**

Links this File with another, so they depend upon each other for loading and processing.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| fileB | [Phaser.Loader.File](loader-file.md) | No | The file to link to this one. |
| --- | --- | --- | --- |

> Source: [src/loader/File.js#L265](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/File.js#L265)  
> Since: 3.7.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [base64](#base64)

    - [base64: boolean](#base64-boolean)
  + [bytesLoaded](#bytesloaded)

    - [bytesLoaded: number](#bytesloaded-number)
  + [bytesTotal](#bytestotal)

    - [bytesTotal: number](#bytestotal-number)
  + [cache](#cache)

    - [cache: Phaser.Cache.BaseCache, Phaser.Textures.TextureManager](#cache-phasercachebasecache-phasertexturestexturemanager)
  + [config](#config)

    - [config: \*](#config-)
  + [crossOrigin](#crossorigin)

    - [crossOrigin: string, undefined](#crossorigin-string-undefined)
  + [data](#data)

    - [data: \*](#data-)
  + [key](#key)

    - [key: string](#key-string)
  + [linkFile](#linkfile)

    - [linkFile: Phaser.Loader.File](#linkfile-phaserloaderfile)
  + [loader](#loader)

    - [loader: Phaser.Loader.LoaderPlugin](#loader-phaserloaderloaderplugin)
  + [multiFile](#multifile)

    - [multiFile: Phaser.Loader.MultiFile](#multifile-phaserloadermultifile)
  + [percentComplete](#percentcomplete)

    - [percentComplete: number](#percentcomplete-number)
  + [retryAttempts](#retryattempts)

    - [retryAttempts: number](#retryattempts-number)
  + [src](#src)

    - [src: string](#src-string)
  + [state](#state)

    - [state: number](#state-number)
  + [type](#type)

    - [type: string](#type-string)
  + [url](#url)

    - [url: object, string](#url-object-string)
  + [xhrLoader](#xhrloader)

    - [xhrLoader: XMLHttpRequest](#xhrloader-xmlhttprequest)
  + [xhrSettings](#xhrsettings)

    - [xhrSettings: Phaser.Types.Loader.XHRSettingsObject](#xhrsettings-phasertypesloaderxhrsettingsobject)
* [Public Methods](#public-methods)

  + [addToCache](#addtocache)

    - [<instance> addToCache()](#instance-addtocache)
  + [createObjectURL](#createobjecturl)

    - [<static> createObjectURL(image, blob, defaultType)](#static-createobjecturlimage-blob-defaulttype)
  + [destroy](#destroy)

    - [<instance> destroy()](#instance-destroy)
  + [hasCacheConflict](#hascacheconflict)

    - [<instance> hasCacheConflict()](#instance-hascacheconflict)
  + [load](#load)

    - [<instance> load()](#instance-load)
  + [onBase64Load](#onbase64load)

    - [<instance> onBase64Load(xhr)](#instance-onbase64loadxhr)
  + [onError](#onerror)

    - [<instance> onError(xhr, event)](#instance-onerrorxhr-event)
  + [onLoad](#onload)

    - [<instance> onLoad(xhr, event)](#instance-onloadxhr-event)
  + [onProcess](#onprocess)

    - [<instance> onProcess()](#instance-onprocess)
  + [onProcessComplete](#onprocesscomplete)

    - [<instance> onProcessComplete()](#instance-onprocesscomplete)
  + [onProcessError](#onprocesserror)

    - [<instance> onProcessError()](#instance-onprocesserror)
  + [onProgress](#onprogress)

    - [<instance> onProgress(event)](#instance-onprogressevent)
  + [pendingDestroy](#pendingdestroy)

    - [<instance> pendingDestroy()](#instance-pendingdestroy)
  + [resetXHR](#resetxhr)

    - [<instance> resetXHR()](#instance-resetxhr)
  + [revokeObjectURL](#revokeobjecturl)

    - [<static> revokeObjectURL(image)](#static-revokeobjecturlimage)
  + [setLink](#setlink)

    - [<instance> setLink(fileB)](#instance-setlinkfileb)

Back to top

©2025[Phaser](https://docs.phaser.io)



File