#!/usr/bin/env python3

import pytest
import numpy as np
import acquire_zarr
from time import sleep

data = np.arange(64, 64, 3, dtype=np.uint8)

def test_zarr_v2():
    zarr = acquire_zarr.AcquireZarrWriter()
    
    fname = "test.zar"
    zarr.uri = fname
    print ( "uri =", len(zarr.uri))
    assert zarr.uri == "test.zar"
    
    zarr.dimensions = ["x", "y", "t"]
    assert zarr.dimensions == ["x", "y", "t"]
    
    zarr.dimension_sizes = [64, 64, 0]
    assert zarr.dimension_sizes == [64, 64, 0]
    
    zarr.compression_codec = acquire_zarr.CompressionCodec.COMPRESSION_NONE
    assert zarr.compression_codec == acquire_zarr.CompressionCodec.COMPRESSION_NONE
    
    zarr.compression_codec = acquire_zarr.CompressionCodec.COMPRESSION_BLOSC_ZSTD
    assert zarr.compression_codec == acquire_zarr.CompressionCodec.COMPRESSION_BLOSC_ZSTD
    
    zarr.compression_level = 5
    assert zarr.compression_level == 5
    zarr.compression_shuffle = 0
    assert zarr.compression_shuffle == 0
    
    zarr.open()
    for i in range(3):
        zarr.append(data)
        #sleep(0.5)
        
