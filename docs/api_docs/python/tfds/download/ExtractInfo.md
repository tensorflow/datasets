<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.download.ExtractInfo" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="filetype"/>
<meta itemprop="property" content="path"/>
<meta itemprop="property" content="ByteSize"/>
<meta itemprop="property" content="Clear"/>
<meta itemprop="property" content="ClearField"/>
<meta itemprop="property" content="DiscardUnknownFields"/>
<meta itemprop="property" content="FindInitializationErrors"/>
<meta itemprop="property" content="FromString"/>
<meta itemprop="property" content="HasField"/>
<meta itemprop="property" content="IsInitialized"/>
<meta itemprop="property" content="ListFields"/>
<meta itemprop="property" content="MergeFrom"/>
<meta itemprop="property" content="MergeFromString"/>
<meta itemprop="property" content="RegisterExtension"/>
<meta itemprop="property" content="SerializePartialToString"/>
<meta itemprop="property" content="SerializeToString"/>
<meta itemprop="property" content="SetInParent"/>
<meta itemprop="property" content="WhichOneof"/>
<meta itemprop="property" content="__eq__"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__unicode__"/>
<meta itemprop="property" content="DESCRIPTOR"/>
<meta itemprop="property" content="FILETYPE_FIELD_NUMBER"/>
<meta itemprop="property" content="FileType"/>
<meta itemprop="property" content="GZ"/>
<meta itemprop="property" content="PATH_FIELD_NUMBER"/>
<meta itemprop="property" content="RAR"/>
<meta itemprop="property" content="UNKNOWN"/>
<meta itemprop="property" content="ZIP"/>
</div>

# tfds.download.ExtractInfo

## Class `ExtractInfo`





This is an alias for a Python built-in.



<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(**kwargs)
```





## Properties

<h3 id="filetype"><code>filetype</code></h3>

Magic attribute generated for "filetype" proto field.

<h3 id="path"><code>path</code></h3>

Magic attribute generated for "path" proto field.



## Methods

<h3 id="ByteSize"><code>ByteSize</code></h3>

``` python
ByteSize()
```



<h3 id="Clear"><code>Clear</code></h3>

``` python
Clear()
```



<h3 id="ClearField"><code>ClearField</code></h3>

``` python
ClearField(field_name)
```



<h3 id="DiscardUnknownFields"><code>DiscardUnknownFields</code></h3>

``` python
DiscardUnknownFields()
```



<h3 id="FindInitializationErrors"><code>FindInitializationErrors</code></h3>

``` python
FindInitializationErrors()
```

Finds required fields which are not initialized.

#### Returns:

A list of strings.  Each string is a path to an uninitialized field from
the top-level message, e.g. "foo.bar[5].baz".

<h3 id="FromString"><code>FromString</code></h3>

``` python
@staticmethod
FromString(s)
```



<h3 id="HasField"><code>HasField</code></h3>

``` python
HasField(field_name)
```



<h3 id="IsInitialized"><code>IsInitialized</code></h3>

``` python
IsInitialized(errors=None)
```

Checks if all required fields of a message are set.

#### Args:

* <b>`errors`</b>:  A list which, if provided, will be populated with the field
           paths of all missing required fields.


#### Returns:

True iff the specified message has all required fields set.

<h3 id="ListFields"><code>ListFields</code></h3>

``` python
ListFields()
```



<h3 id="MergeFrom"><code>MergeFrom</code></h3>

``` python
MergeFrom(msg)
```



<h3 id="MergeFromString"><code>MergeFromString</code></h3>

``` python
MergeFromString(serialized)
```



<h3 id="RegisterExtension"><code>RegisterExtension</code></h3>

``` python
@staticmethod
RegisterExtension(extension_handle)
```



<h3 id="SerializePartialToString"><code>SerializePartialToString</code></h3>

``` python
SerializePartialToString(**kwargs)
```



<h3 id="SerializeToString"><code>SerializeToString</code></h3>

``` python
SerializeToString(**kwargs)
```



<h3 id="SetInParent"><code>SetInParent</code></h3>

``` python
SetInParent()
```

Sets the _cached_byte_size_dirty bit to true,
and propagates this to our listener iff this was a state change.

<h3 id="WhichOneof"><code>WhichOneof</code></h3>

``` python
WhichOneof(oneof_name)
```

Returns the name of the currently set field inside a oneof, or None.

<h3 id="__eq__"><code>__eq__</code></h3>

``` python
__eq__(other)
```



<h3 id="__unicode__"><code>__unicode__</code></h3>

``` python
__unicode__()
```





## Class Members

<h3 id="DESCRIPTOR"><code>DESCRIPTOR</code></h3>

<h3 id="FILETYPE_FIELD_NUMBER"><code>FILETYPE_FIELD_NUMBER</code></h3>

<h3 id="FileType"><code>FileType</code></h3>

<h3 id="GZ"><code>GZ</code></h3>

<h3 id="PATH_FIELD_NUMBER"><code>PATH_FIELD_NUMBER</code></h3>

<h3 id="RAR"><code>RAR</code></h3>

<h3 id="UNKNOWN"><code>UNKNOWN</code></h3>

<h3 id="ZIP"><code>ZIP</code></h3>

