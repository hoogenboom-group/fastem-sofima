import webknossos as wk

def import_wk_dataset_local(dir_path, MAG, bbox=None) -> None:
    "Locally import data from WebKnossos instance"
    # open local dataset in given directory 
    dataset = wk.Dataset.open(
        dataset_path = dir_path
        )
    voxel_size = dataset.voxel_size

    # return data, voxel size
    return dataset, voxel_size

def import_wk_dataset_remote(dataset_full_url) -> None:
    # open remote dataset with dataset name, organization id and WebKnossos url 
    dataset = wk.Dataset.open_remote(
            dataset_name_or_url=dataset_full_url)
    voxel_size = dataset.voxel_size

    # return data, voxel size
    return dataset, voxel_size

def load_wk_dataset_remote(dataset_full_url,
                             MAG, layer="color", bbox=None) -> None:
    # open remote dataset with dataset name, organization id and WebKnossos url 
    dataset = wk.Dataset.open_remote(
            dataset_name_or_url=dataset_full_url)
    voxel_size = dataset.voxel_size

    EM = dataset.get_layer(layer) # EM data Layer
    mag_view = EM.get_mag(MAG) # MagView

    # Get data at required resolution
    view = mag_view.get_view(absolute_offset=bbox.topleft, size=bbox.size) # "absolute_offset" and "size" are in Mag(1)!

    # Read data from remote
    data = view.read()

    # return data, voxel size
    return dataset, data, voxel_size