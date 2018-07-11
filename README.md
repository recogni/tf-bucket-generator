# tf-packet-generator

A tensor generator that facilitates dataset creation from google storage buckets.

## Idea

Inspired by [recogni/tf-http-generator](https://github.com/recogni/tf-http-generator), but for google storage buckets.

Assumes that the underlying system has run and authenticated using `gcloud auth application-default login`.

## Install

```
git clone https://github.com/recogni/tf-packet-generator
cd tf-packet-generator
python setup.py install
```

## Usage

See the `example.py` file for a very simple and completely useless example which illustrates the capability of this library.

## Implementation

This library implements a tf generator which facilitates the creation of datasets using `dataset.from_generator()`.  The generator is responsible for reading data from a google storage bucket as specified by a `glob`.

The `example.py` outlines how `recogni_proto.CameraPacket`s can be read from a `gs://` location (or from the local file system), and transformed into the relevant training / inference tensors.
