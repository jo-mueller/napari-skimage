from typing import TYPE_CHECKING

from magicgui import magic_factory
from magicgui.widgets import CheckBox, Container, create_widget
from qtpy.QtWidgets import QHBoxLayout, QPushButton, QWidget
from skimage.util import img_as_float
import skimage.filters as sf
from napari.layers import Image
import napari.types


if TYPE_CHECKING:
    import napari

@magic_factory(
        image_layer={'label': 'Image'},
        mode={'choices': ['reflect', 'constant', 'nearest', 'mirror', 'wrap']},
        call_button="Apply Farid filter"
        )
def farid_filter_widget(
    image_layer: Image, mode='reflect') -> napari.types.LayerDataTuple:
    return (
        sf.farid(image_layer.data),
        {'name': f'{image_layer.name}_farid'},
        'image')

@magic_factory(
        image_layer={'label': 'Image'},
        call_button="Apply Laplace filter"
        )
def laplace_filter_widget(
    image_layer: Image,
    ksize: int = 3.0) -> napari.types.LayerDataTuple:
    return (
        sf.laplace(image_layer.data, ksize=ksize),
        {'name': f'{image_layer.name}_laplace'},
        'image')
    
@magic_factory(
        img_layer={'label': 'Image'},
        mode={'choices': ['reflect', 'constant', 'nearest', 'mirror', 'wrap']},
        call_button="Apply Gaussian Filter"
        )
def gaussian_filter_widget(
    img_layer: Image,
    sigma: float = 1.0,
    preserve_range: bool = False,
    mode = "reflect",
) -> napari.types.LayerDataTuple:
    return (
        sf.gaussian(img_layer.data, sigma=sigma, preserve_range=preserve_range, mode=mode),
        {'name': f'{img_layer.name}_gaussian_σ={sigma}'},
        'image')