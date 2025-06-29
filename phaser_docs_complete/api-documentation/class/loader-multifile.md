# MultiFile

Phaser.Loader.MultiFile

A MultiFile is a special kind of parent that contains two, or more, Files as children and looks after

the loading and processing of them all. It is commonly extended and used as a base class for file types such as AtlasJSON or BitmapFont.

You shouldn't create an instance of a MultiFile directly, but should extend it with your own class, setting a custom type and processing methods.

**Constructor**

`new MultiFile(loader, type, key, files)`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| loader | [Phaser.Loader.LoaderPlugin](loader-loaderplugin.md) | No | The Loader that is going to load this File. |
| --- | --- | --- | --- |
| type | string | No | The file type string for sorting within the Loader. |
| key | string | No | The key of the file within the loader. |
| files | Array.<[Phaser.Loader.File](loader-file.md)> | No | An array of Files that make-up this MultiFile. |

---

**Scope**: static

> Source: [src/loader/MultiFile.js#L11](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/MultiFile.js#L11)  
> Since: 3.7.0

# Public Members

## baseURL

### baseURL: string

**Description:**

A reference to the Loaders baseURL at the time this MultiFile was created.

Used to populate child-files.

> Source: [src/loader/MultiFile.js#L146](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/MultiFile.js#L146)  
> Since: 3.20.0

---

## complete

### complete: boolean

**Description:**

The completion status of this MultiFile.

> Source: [src/loader/MultiFile.js#L107](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/MultiFile.js#L107)  
> Since: 3.7.0

---

## config

### config: any

**Description:**

A storage container for transient data that the loading files need.

> Source: [src/loader/MultiFile.js#L137](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/MultiFile.js#L137)  
> Since: 3.7.0

---

## failed

### failed: number

**Description:**

The number of files that failed to load.

> Source: [src/loader/MultiFile.js#L127](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/MultiFile.js#L127)  
> Since: 3.7.0

---

## files

### files: Array.<[Phaser.Loader.File](loader-file.md)>

**Description:**

Array of files that make up this MultiFile.

> Source: [src/loader/MultiFile.js#L89](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/MultiFile.js#L89)  
> Since: 3.7.0

---

## key

### key: string

**Description:**

Unique cache key (unique within its file type)

> Source: [src/loader/MultiFile.js#L63](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/MultiFile.js#L63)  
> Since: 3.7.0

---

## loader

### loader: [Phaser.Loader.LoaderPlugin](loader-loaderplugin.md)

**Description:**

A reference to the Loader that is going to load this file.

> Source: [src/loader/MultiFile.js#L45](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/MultiFile.js#L45)  
> Since: 3.7.0

---

## path

### path: string

**Description:**

A reference to the Loaders path at the time this MultiFile was created.

Used to populate child-files.

> Source: [src/loader/MultiFile.js#L156](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/MultiFile.js#L156)  
> Since: 3.20.0

---

## pending

### pending: number

**Description:**

The number of files to load.

> Source: [src/loader/MultiFile.js#L117](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/MultiFile.js#L117)  
> Since: 3.7.0

---

## prefix

### prefix: string

**Description:**

A reference to the Loaders prefix at the time this MultiFile was created.

Used to populate child-files.

> Source: [src/loader/MultiFile.js#L166](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/MultiFile.js#L166)  
> Since: 3.20.0

---

## state

### state: number

**Description:**

The current state of the file. One of the FILE\_CONST values.

> Source: [src/loader/MultiFile.js#L98](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/MultiFile.js#L98)  
> Since: 3.60.0

---

## type

### type: string

**Description:**

The file type string for sorting within the Loader.

> Source: [src/loader/MultiFile.js#L54](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/MultiFile.js#L54)  
> Since: 3.7.0

---

# Private Members

## multiKeyIndex

### multiKeyIndex: number

**Description:**

The current index being used by multi-file loaders to avoid key clashes.

**Access:** private

> Source: [src/loader/MultiFile.js#L79](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/MultiFile.js#L79)  
> Since: 3.20.0

---

# Public Methods

## addToMultiFile

### <instance> addToMultiFile(files)

**Description:**

Adds another child to this MultiFile, increases the pending count and resets the completion status.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| files | [Phaser.Loader.File](loader-file.md) | No | The File to add to this MultiFile. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Loader.MultiFile](loader-multifile.md) - This MultiFile instance.

> Source: [src/loader/MultiFile.js#L196](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/MultiFile.js#L196)  
> Since: 3.7.0

---

## destroy

### <instance> destroy()

**Description:**

Destroy this Multi File and any references it holds.

> Source: [src/loader/MultiFile.js#L292](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/MultiFile.js#L292)  
> Since: 3.60.0

---

## isReadyToProcess

### <instance> isReadyToProcess()

**Description:**

Checks if this MultiFile is ready to process its children or not.

**Returns:** boolean - `true` if all children of this MultiFile have loaded, otherwise `false`.

> Source: [src/loader/MultiFile.js#L183](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/MultiFile.js#L183)  
> Since: 3.7.0

---

## onFileComplete

### <instance> onFileComplete(file)

**Description:**

Called by each File when it finishes loading.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| file | [Phaser.Loader.File](loader-file.md) | No | The File that has completed processing. |
| --- | --- | --- | --- |

> Source: [src/loader/MultiFile.js#L219](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/MultiFile.js#L219)  
> Since: 3.7.0

---

## onFileFailed

### <instance> onFileFailed(file)

**Description:**

Called by each File that fails to load.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| file | [Phaser.Loader.File](loader-file.md) | No | The File that has failed to load. |
| --- | --- | --- | --- |

> Source: [src/loader/MultiFile.js#L237](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/MultiFile.js#L237)  
> Since: 3.7.0

---

## pendingDestroy

### <instance> pendingDestroy()

**Description:**

Called once all children of this multi file have been added to their caches and is now

ready for deletion from the Loader.

It will emit a `filecomplete` event from the LoaderPlugin.

**Fires:** [Phaser.Loader.Events#event:FILE\_COMPLETE](../event/loader-events.md), [Phaser.Loader.Events#event:FILE\_KEY\_COMPLETE](../event/loader-events.md)

> Source: [src/loader/MultiFile.js#L258](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/MultiFile.js#L258)  
> Since: 3.60.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [baseURL](#baseurl)

    - [baseURL: string](#baseurl-string)
  + [complete](#complete)

    - [complete: boolean](#complete-boolean)
  + [config](#config)

    - [config: any](#config-any)
  + [failed](#failed)

    - [failed: number](#failed-number)
  + [files](#files)

    - [files: Array.<Phaser.Loader.File>](#files-arrayphaserloaderfile)
  + [key](#key)

    - [key: string](#key-string)
  + [loader](#loader)

    - [loader: Phaser.Loader.LoaderPlugin](#loader-phaserloaderloaderplugin)
  + [path](#path)

    - [path: string](#path-string)
  + [pending](#pending)

    - [pending: number](#pending-number)
  + [prefix](#prefix)

    - [prefix: string](#prefix-string)
  + [state](#state)

    - [state: number](#state-number)
  + [type](#type)

    - [type: string](#type-string)
* [Private Members](#private-members)

  + [multiKeyIndex](#multikeyindex)

    - [multiKeyIndex: number](#multikeyindex-number)
* [Public Methods](#public-methods)

  + [addToMultiFile](#addtomultifile)

    - [<instance> addToMultiFile(files)](#instance-addtomultifilefiles)
  + [destroy](#destroy)

    - [<instance> destroy()](#instance-destroy)
  + [isReadyToProcess](#isreadytoprocess)

    - [<instance> isReadyToProcess()](#instance-isreadytoprocess)
  + [onFileComplete](#onfilecomplete)

    - [<instance> onFileComplete(file)](#instance-onfilecompletefile)
  + [onFileFailed](#onfilefailed)

    - [<instance> onFileFailed(file)](#instance-onfilefailedfile)
  + [pendingDestroy](#pendingdestroy)

    - [<instance> pendingDestroy()](#instance-pendingdestroy)

Back to top

©2025[Phaser](https://docs.phaser.io)



MultiFile