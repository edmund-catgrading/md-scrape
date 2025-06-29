# Phaser.Loader

Scope:
static

> Source: [src/loader/index.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/index.js#L10)

# Static functions

* [File](../class/loader-file.md)
* [LoaderPlugin](../class/loader-loaderplugin.md)
* [MultiFile](../class/loader-multifile.md)

# Static functions

## FILE\_COMPLETE

### FILE\_COMPLETE: number

**Description:**

File has finished processing.

> Source: [src/loader/const.js#L117](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/const.js#L117)  
> Since: 3.0.0

---

## FILE\_DESTROYED

### FILE\_DESTROYED: number

**Description:**

File has been destroyed.

> Source: [src/loader/const.js#L126](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/const.js#L126)  
> Since: 3.0.0

---

## FILE\_ERRORED

### FILE\_ERRORED: number

**Description:**

The File has errored somehow during processing.

> Source: [src/loader/const.js#L108](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/const.js#L108)  
> Since: 3.0.0

---

## FILE\_FAILED

### FILE\_FAILED: number

**Description:**

File failed to load.

> Source: [src/loader/const.js#L90](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/const.js#L90)  
> Since: 3.0.0

---

## FILE\_LOADED

### FILE\_LOADED: number

**Description:**

File has loaded successfully, awaiting processing.

> Source: [src/loader/const.js#L81](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/const.js#L81)  
> Since: 3.0.0

---

## FILE\_LOADING

### FILE\_LOADING: number

**Description:**

File has been started to load by the loader (onLoad called)

> Source: [src/loader/const.js#L72](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/const.js#L72)  
> Since: 3.0.0

---

## FILE\_PENDING

### FILE\_PENDING: number

**Description:**

File is in the load queue but not yet started.

> Source: [src/loader/const.js#L63](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/const.js#L63)  
> Since: 3.0.0

---

## FILE\_PENDING\_DESTROY

### FILE\_PENDING\_DESTROY: number

**Description:**

File is pending being destroyed.

> Source: [src/loader/const.js#L144](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/const.js#L144)  
> Since: 3.60.0

---

## FILE\_POPULATED

### FILE\_POPULATED: number

**Description:**

File was populated from local data and doesn't need an HTTP request.

> Source: [src/loader/const.js#L135](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/const.js#L135)  
> Since: 3.0.0

---

## FILE\_PROCESSING

### FILE\_PROCESSING: number

**Description:**

File is being processed (onProcess callback)

> Source: [src/loader/const.js#L99](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/const.js#L99)  
> Since: 3.0.0

---

## LOADER\_COMPLETE

### LOADER\_COMPLETE: number

**Description:**

The Loader has completed loading and processing.

> Source: [src/loader/const.js#L36](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/const.js#L36)  
> Since: 3.0.0

---

## LOADER\_DESTROYED

### LOADER\_DESTROYED: number

**Description:**

The Loader has been destroyed.

> Source: [src/loader/const.js#L54](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/const.js#L54)  
> Since: 3.0.0

---

## LOADER\_IDLE

### LOADER\_IDLE: number

**Description:**

The Loader is idle.

> Source: [src/loader/const.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/const.js#L9)  
> Since: 3.0.0

---

## LOADER\_LOADING

### LOADER\_LOADING: number

**Description:**

The Loader is actively loading.

> Source: [src/loader/const.js#L18](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/const.js#L18)  
> Since: 3.0.0

---

## LOADER\_PROCESSING

### LOADER\_PROCESSING: number

**Description:**

The Loader is processing files is has loaded.

> Source: [src/loader/const.js#L27](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/const.js#L27)  
> Since: 3.0.0

---

## LOADER\_SHUTDOWN

### LOADER\_SHUTDOWN: number

**Description:**

The Loader is shutting down.

> Source: [src/loader/const.js#L45](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/const.js#L45)  
> Since: 3.0.0

---

# Static functions

* [Events](loader-events.md)
* [FileTypes](loader-filetypes.md)
* [FileTypesManager](loader-filetypesmanager.md)

# Static functions

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

---

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

---

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

---

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

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Static functions](#static-functions)
* [Static functions](#static-functions-1)

  + [FILE\_COMPLETE](#file_complete)

    - [FILE\_COMPLETE: number](#file_complete-number)
  + [FILE\_DESTROYED](#file_destroyed)

    - [FILE\_DESTROYED: number](#file_destroyed-number)
  + [FILE\_ERRORED](#file_errored)

    - [FILE\_ERRORED: number](#file_errored-number)
  + [FILE\_FAILED](#file_failed)

    - [FILE\_FAILED: number](#file_failed-number)
  + [FILE\_LOADED](#file_loaded)

    - [FILE\_LOADED: number](#file_loaded-number)
  + [FILE\_LOADING](#file_loading)

    - [FILE\_LOADING: number](#file_loading-number)
  + [FILE\_PENDING](#file_pending)

    - [FILE\_PENDING: number](#file_pending-number)
  + [FILE\_PENDING\_DESTROY](#file_pending_destroy)

    - [FILE\_PENDING\_DESTROY: number](#file_pending_destroy-number)
  + [FILE\_POPULATED](#file_populated)

    - [FILE\_POPULATED: number](#file_populated-number)
  + [FILE\_PROCESSING](#file_processing)

    - [FILE\_PROCESSING: number](#file_processing-number)
  + [LOADER\_COMPLETE](#loader_complete)

    - [LOADER\_COMPLETE: number](#loader_complete-number)
  + [LOADER\_DESTROYED](#loader_destroyed)

    - [LOADER\_DESTROYED: number](#loader_destroyed-number)
  + [LOADER\_IDLE](#loader_idle)

    - [LOADER\_IDLE: number](#loader_idle-number)
  + [LOADER\_LOADING](#loader_loading)

    - [LOADER\_LOADING: number](#loader_loading-number)
  + [LOADER\_PROCESSING](#loader_processing)

    - [LOADER\_PROCESSING: number](#loader_processing-number)
  + [LOADER\_SHUTDOWN](#loader_shutdown)

    - [LOADER\_SHUTDOWN: number](#loader_shutdown-number)
* [Static functions](#static-functions-2)
* [Static functions](#static-functions-3)

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