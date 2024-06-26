import webknossos as wk
import math

def define_bbox_chunks(view, mag, bbox_size=5000):
    """Define bbox chunks for parallel import
    
    view: webknossos.dataset.view
            Bounding box to data in specific MagView
    mag: webknossos.geometry.mag
            Magnification level of data layer (usually highest mag)
    bbox_size: int
            Size of bbox chunks
    returns list of wk.BoundingBox objects
    """
    
    # Infer data set dimensions (in desired mag)
    dim = view.bounding_box.in_mag(mag).size
    
    # Offset
    x0 = view.bounding_box.in_mag(mag).topleft.x
    y0 = view.bounding_box.in_mag(mag).topleft.y

    # Determine number of chunks to split data into in all dimensions
    chunks_x, chunks_y, chunks_z = math.ceil(dim.x / bbox_size), math.ceil(dim.y / bbox_size), math.ceil(dim.z / 256)

    # Determine z size of bbox (x an y sizes are defined by bbox_size)
    size_z = min(dim.z, 256)

    # From # chunks, define bboxes to be used
    # Loop over x, y, z chunk indices, define bbox on multiples of bbox_size starting from topleft of og bbox
    bboxes = []
    for i in range(chunks_x):
        for j in range(chunks_y):
            if bbox_size*(i+1) >= dim.x: # check if bbox is larger than max x and adjust bbox dimension 
                bbox_size_x = dim.x - bbox_size*i
            else: # not exceeding stack dimensions, use regular bbox_size
                bbox_size_x = bbox_size
            
            if bbox_size*(j+1) >= dim.y: # check if bbox is larger than max y and adjust bbox dimension 
                bbox_size_y = dim.y - bbox_size*j
            else: # not exceeding stack dimensions, use regular bbox_size
                bbox_size_y = bbox_size
            
            for k in range(chunks_z):
                # Generate bbox
                bbox_small = wk.BoundingBox(topleft=(x0 + bbox_size*i, y0 + bbox_size*j, 256*k),
                                            size=(bbox_size_x, bbox_size_y, size_z))\
                                                .from_mag_to_mag1(from_mag=mag)        
                bboxes.append(bbox_small)   
    
    return bboxes


def define_tiles_for_warping(data_2_warp, tilesize=2000):
    """Define tiles for parallel warping
    
    data_2_warp: np.array
            Array with data to warp
    tilesize: int
            size of tiles in x and y to warp individually
    
    returns list of tile
    """
    dim = data_2_warp.shape
    
    # Determine number of chunks to split data into in all dimensions
    chunks_x, chunks_y = math.ceil(dim[0]/ tilesize), math.ceil(dim[1] / tilesize)
    
    # From # chunks, define bboxes to be used
    # Loop over x, y, z chunk indices, define bbox on multiples of bbox_size starting from topleft of og bbox
    tiles = []
    for i in range(chunks_y):
        for j in range(chunks_x):
            if tilesize*(i+1) >= dim[0]: # check if bbox is larger than max x and adjust bbox dimension 
                bbox_size_y = dim[0] - tilesize*i
            else: # not exceeding stack dimensions, use regular bbox_size
                bbox_size_y = tilesize
            
            if tilesize*(j+1) >= dim[1]: # check if bbox is larger than max y and adjust bbox dimension 
                bbox_size_x = dim[1] - tilesize*j
            else: # not exceeding stack dimensions, use regular bbox_size
                bbox_size_x = tilesize
    
            # Generate bbox
            bbox_small = (i*tilesize, i*tilesize+bbox_size_y, j*tilesize, j*tilesize+bbox_size_x) # y0, y1, x0, x1)       
            tiles.append(bbox_small)   
    
    return tiles