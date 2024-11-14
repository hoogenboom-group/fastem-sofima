from tempfile import TemporaryDirectory
import webknossos as wk
import numpy as np

url="https://webknossos.tnw.tudelft.nl"
token="test1234" # Generate from https://webknossos.tnw.tudelft.nl/auth/token"
new_dataset_name = "test"
voxel_size = (4, 4, 100) # x, y, z
bbox = wk.BoundingBox((0, 0, 0),
                      (0, 0, 0)) # ((x0, y0, z0), (x_size, y_size, z_size)), probably equal to array size
himag = wk.Mag('1-1-1')
data = np.array([])

with wk.webknossos_context(
    url=url,
    token=token,
):
    with TemporaryDirectory() as tempdir:
        new_dataset = wk.Dataset(
            dataset_path=tempdir,
            name=new_dataset_name,
            voxel_size=voxel_size
        )
        warped_layer = new_dataset.add_layer(
            "Mito_GT_realigned",
            wk.SEGMENTATION_CATEGORY,
            dtype_per_layer="uint16",
            compressed=True
            )
        warped_layer.bounding_box = bbox.align_with_mag(himag) # Highest MAG
        warped_layer.add_mag(himag, compress=True).write(data)
        # warped_layer.downsample(
        #     coarsest_mag=wk.Mag("128-128-1"),
        #     sampling_mode="constant_z"
        #     )

        remote_ds = new_dataset.upload()