# keras-2 :: tacm-full

query: Fix in_top_k tests to include CNTK [Test fails] (#12336)

## selected nodes

- rank=1 layer=FUNCTION tokens=191 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/metrics_utils.py::_filter_top_k file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/metrics_utils.py
- rank=2 layer=FUNCTION tokens=64 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/math.py::in_top_k file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/math.py
- rank=3 layer=FUNCTION tokens=68 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/backend.py::in_top_k file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/backend.py
- rank=4 layer=FUNCTION tokens=257 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math.py::top_k file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math.py
- rank=5 layer=FUNCTION tokens=191 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/math.py::top_k file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/math.py
- rank=6 layer=FUNCTION tokens=87 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/math.py::top_k file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/math.py
- rank=7 layer=FUNCTION tokens=210 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/applications/applications_test.py::_get_elephant file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/applications/applications_test.py
- rank=8 layer=FUNCTION tokens=273 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math.py::in_top_k file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math.py
- rank=9 layer=FUNCTION tokens=132 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/torch/math.py::in_top_k file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/torch/math.py
- rank=10 layer=FUNCTION tokens=60 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/math.py::top_k file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/math.py
- rank=11 layer=FUNCTION tokens=103 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/math.py::in_top_k file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/math.py
- rank=12 layer=FUNCTION tokens=86 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/integration_tests/import_test.py::run_keras_flow file=/Users/xxvirusxx/PY/CodegraphTACM/keras/integration_tests/import_test.py
- rank=13 layer=FUNCTION tokens=62 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math.py::InTopK.call file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math.py
- rank=14 layer=FUNCTION tokens=221 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/applications/efficientnet_v2.py::EfficientNetV2B0 file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/applications/efficientnet_v2.py
- rank=15 layer=FUNCTION tokens=221 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/applications/efficientnet_v2.py::EfficientNetV2B1 file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/applications/efficientnet_v2.py
- rank=16 layer=FUNCTION tokens=221 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/applications/efficientnet_v2.py::EfficientNetV2B2 file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/applications/efficientnet_v2.py
- rank=17 layer=FUNCTION tokens=221 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/applications/efficientnet_v2.py::EfficientNetV2B3 file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/applications/efficientnet_v2.py
- rank=18 layer=FUNCTION tokens=220 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/applications/efficientnet_v2.py::EfficientNetV2S file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/applications/efficientnet_v2.py
- rank=19 layer=FUNCTION tokens=220 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/applications/efficientnet_v2.py::EfficientNetV2M file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/applications/efficientnet_v2.py
- rank=20 layer=FUNCTION tokens=220 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/applications/efficientnet_v2.py::EfficientNetV2L file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/applications/efficientnet_v2.py
- rank=21 layer=FUNCTION tokens=64 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/torch/math.py::top_k file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/torch/math.py
- rank=22 layer=FUNCTION tokens=130 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py::TopKCategoricalAccuracy.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py
- rank=23 layer=FUNCTION tokens=257 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/applications/convnext.py::ConvNeXtXLarge file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/applications/convnext.py
- rank=24 layer=FUNCTION tokens=187 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/applications/efficientnet.py::EfficientNetB0 file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/applications/efficientnet.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/metrics_utils.py::_filter_top_k [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/metrics_utils.py]
def _filter_top_k(x, k):
    """Filters top-k values in the last dim of x and set the rest to NEG_INF.

    Used for computing top-k prediction values in dense labels (which has the
    same shape as predictions) for recall and precision top-k metrics.

    Args:
      x: tensor with any dimensions.
      k: the number of values to keep.

    Returns:
      tensor with same shape and dtype as x.
    """
    _, top_k_idx = ops.top_k(x, k)
    top_k_mask = ops.sum(
        ops.one_hot(top_k_idx, ops.shape(x)[-1], axis=-1), axis=-2
    )
    return x * top_k_mask + NEG_INF * (1 - top_k_mask)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/math.py::in_top_k [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/math.py]
def in_top_k(targets, predictions, k):
    return tf.math.in_top_k(targets, predictions, k)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/backend.py::in_top_k [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/backend.py]
def in_top_k(predictions, targets, k):
    """DEPRECATED."""
    return tf.compat.v1.math.in_top_k(predictions, targets, k)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math.py::top_k [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math.py]
def top_k(x, k, sorted=True):
    """Finds the top-k values and their indices in a tensor.

    Args:
        x: Input tensor.
        k: An integer representing the number of top elements to retrieve.
        sorted: A boolean indicating whether to sort the output in
        descending order. Defaults to `True`.

    Returns:
        A tuple containing two tensors. The first tensor contains the
        top-k values, and the second tensor contains the indices of the
        top-k values in the input tensor.

    Example:

    >>> x = keras.ops.convert_to_tensor([5, 2, 7, 1, 9, 3])
    >>> values, indices = top_k(x, k=3)
    >>> print(values)
    array([9 7 5], shape=(3,), dtype=int32)
    >>> print(indices)
    array([4 2 0], shape=(3,), dtype=int32)

    """
    if any_symbolic_tensors((x,)):
        return TopK(k, sorted).symbolic_call(x)
    return backend.math.top_k(x, k, sorted)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/math.py::top_k [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/math.py]
def top_k(x, k, sorted=True):
    if sorted:
        # Take the k largest values.
        sorted_indices = np.argsort(x, axis=-1)[..., ::-1]
        sorted_values = np.take_along_axis(x, sorted_indices, axis=-1)
        top_k_values = sorted_values[..., :k]
        top_k_indices = sorted_indices[..., :k]
    else:
        # Partition the array such that all values larger than the k-th
        # largest value are to the right of it.
        top_k_indices = np.argpartition(x, -k, axis=-1)[..., -k:]
        top_k_values = np.take_along_axis(x, top_k_indices, axis=-1)
    return top_k_values, top_k_indices

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/math.py::top_k [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/math.py]
def top_k(x, k, sorted=True):
    # Jax does not supported `sorted`, but in the case where `sorted=False`,
    # order is not guaranteed, so OK to return sorted output.
    return jax.lax.top_k(x, k)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/applications/applications_test.py::_get_elephant [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/applications/applications_test.py]
def _get_elephant(target_size):
    # For models that don't include a Flatten step,
    # the default is to accept variable-size inputs
    # even when loading ImageNet weights (since it is possible).
    # In this case, default to 299x299.
    TEST_IMAGE_PATH = (
        "https://storage.googleapis.com/tensorflow/"
        "keras-applications/tests/elephant.jpg"
    )

    if target_size[0] is None:
        target_size = (299, 299)
    test_image = file_utils.get_file("elephant.jpg", TEST_IMAGE_PATH)
    img = image_utils.load_img(test_image, target_size=tuple(target_size))
    x = image_utils.img_to_array(img)
    return np.expand_dims(x, axis=0)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math.py::in_top_k [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math.py]
def in_top_k(targets, predictions, k):
    """Checks if the targets are in the top-k predictions.

    Args:
        targets: A tensor of true labels.
        predictions: A tensor of predicted labels.
        k: An integer representing the number of predictions to consider.

    Returns:
        A boolean tensor of the same shape as `targets`, where each element
        indicates whether the corresponding target is in the top-k predictions.

    Example:

    >>> targets = keras.ops.convert_to_tensor([2, 5, 3])
    >>> predictions = keras.ops.convert_to_tensor(
    ... [[0.1, 0.4, 0.6, 0.9, 0.5],
    ...  [0.1, 0.7, 0.9, 0.8, 0.3],
    ...  [0.1, 0.6, 0.9, 0.9, 0.5]])
    >>> in_top_k(targets, predictions, k=3)
    array([ True False  True], shape=(3,), dtype=bool)
    """
    if any_symbolic_tensors((targets, predictions)):
        return InTopK(k).symbolic_call(targets, predictions)
    return backend.math.in_top_k(targets, predictions, k)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/torch/math.py::in_top_k [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/torch/math.py]
def in_top_k(targets, predictions, k):
    targets = convert_to_tensor(targets).type(torch.int64)
    targets = targets[:, None]
    predictions = convert_to_tensor(predictions)
    topk_values = top_k(predictions, k).values
    targets_values = torch.take_along_dim(predictions, targets, dim=-1)
    mask = targets_values >= topk_values
    return torch.any(mask, axis=-1)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/math.py::top_k [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/math.py]
def top_k(x, k, sorted=True):
    return tf.math.top_k(x, k, sorted=sorted)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/math.py::in_top_k [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/math.py]
def in_top_k(targets, predictions, k):
    targets = targets[:, None]
    topk_values = top_k(predictions, k)[0]
    targets_values = np.take_along_axis(predictions, targets, axis=-1)
    mask = targets_values >= topk_values
    return np.any(mask, axis=-1)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/integration_tests/import_test.py::run_keras_flow [/Users/xxvirusxx/PY/CodegraphTACM/keras/integration_tests/import_test.py]
def run_keras_flow():
    test_script = [
        # Runs the example script
        "python -m pytest integration_tests/basic_full_flow.py",
    ]
    run_commands_venv(test_script)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math.py::InTopK.call [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math.py]
    def call(self, targets, predictions):
        return backend.math.in_top_k(targets, predictions, self.k)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/applications/efficientnet_v2.py::EfficientNetV2B0 [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/applications/efficientnet_v2.py]
def EfficientNetV2B0(
    include_top=True,
    weights="imagenet",
    input_tensor=None,
    input_shape=None,
    pooling=None,
    classes=1000,
    classifier_activation="softmax",
    include_preprocessing=True,
    name="efficientnetv2-b0",
):
    return EfficientNetV2(
        width_coefficient=1.0,
        depth_coefficient=1.0,
        default_size=224,
        name=name,
        include_top=include_top,
        weights=weights,
        input_tensor=input_tensor,
        input_shape=input_shape,
        pooling=pooling,
        classes=classes,
        classifier_activation=classifier_activation,
        include_preprocessing=include_preprocessing,
        weights_name="b0",
    )

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/applications/efficientnet_v2.py::EfficientNetV2B1 [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/applications/efficientnet_v2.py]
def EfficientNetV2B1(
    include_top=True,
    weights="imagenet",
    input_tensor=None,
    input_shape=None,
    pooling=None,
    classes=1000,
    classifier_activation="softmax",
    include_preprocessing=True,
    name="efficientnetv2-b1",
):
    return EfficientNetV2(
        width_coefficient=1.0,
        depth_coefficient=1.1,
        default_size=240,
        name=name,
        include_top=include_top,
        weights=weights,
        input_tensor=input_tensor,
        input_shape=input_shape,
        pooling=pooling,
        classes=classes,
        classifier_activation=classifier_activation,
        include_preprocessing=include_preprocessing,
        weights_name="b1",
    )

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/applications/efficientnet_v2.py::EfficientNetV2B2 [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/applications/efficientnet_v2.py]
def EfficientNetV2B2(
    include_top=True,
    weights="imagenet",
    input_tensor=None,
    input_shape=None,
    pooling=None,
    classes=1000,
    classifier_activation="softmax",
    include_preprocessing=True,
    name="efficientnetv2-b2",
):
    return EfficientNetV2(
        width_coefficient=1.1,
        depth_coefficient=1.2,
        default_size=260,
        name=name,
        include_top=include_top,
        weights=weights,
        input_tensor=input_tensor,
        input_shape=input_shape,
        pooling=pooling,
        classes=classes,
        classifier_activation=classifier_activation,
        include_preprocessing=include_preprocessing,
        weights_name="b2",
    )

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/applications/efficientnet_v2.py::EfficientNetV2B3 [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/applications/efficientnet_v2.py]
def EfficientNetV2B3(
    include_top=True,
    weights="imagenet",
    input_tensor=None,
    input_shape=None,
    pooling=None,
    classes=1000,
    classifier_activation="softmax",
    include_preprocessing=True,
    name="efficientnetv2-b3",
):
    return EfficientNetV2(
        width_coefficient=1.2,
        depth_coefficient=1.4,
        default_size=300,
        name=name,
        include_top=include_top,
        weights=weights,
        input_tensor=input_tensor,
        input_shape=input_shape,
        pooling=pooling,
        classes=classes,
        classifier_activation=classifier_activation,
        include_preprocessing=include_preprocessing,
        weights_name="b3",
    )

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/applications/efficientnet_v2.py::EfficientNetV2S [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/applications/efficientnet_v2.py]
def EfficientNetV2S(
    include_top=True,
    weights="imagenet",
    input_tensor=None,
    input_shape=None,
    pooling=None,
    classes=1000,
    classifier_activation="softmax",
    include_preprocessing=True,
    name="efficientnetv2-s",
):
    return EfficientNetV2(
        width_coefficient=1.0,
        depth_coefficient=1.0,
        default_size=384,
        name=name,
        include_top=include_top,
        weights=weights,
        input_tensor=input_tensor,
        input_shape=input_shape,
        pooling=pooling,
        classes=classes,
        classifier_activation=classifier_activation,
        include_preprocessing=include_preprocessing,
        weights_name="-s",
    )

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/applications/efficientnet_v2.py::EfficientNetV2M [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/applications/efficientnet_v2.py]
def EfficientNetV2M(
    include_top=True,
    weights="imagenet",
    input_tensor=None,
    input_shape=None,
    pooling=None,
    classes=1000,
    classifier_activation="softmax",
    include_preprocessing=True,
    name="efficientnetv2-m",
):
    return EfficientNetV2(
        width_coefficient=1.0,
        depth_coefficient=1.0,
        default_size=480,
        name=name,
        include_top=include_top,
        weights=weights,
        input_tensor=input_tensor,
        input_shape=input_shape,
        pooling=pooling,
        classes=classes,
        classifier_activation=classifier_activation,
        include_preprocessing=include_preprocessing,
        weights_name="-m",
    )

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/applications/efficientnet_v2.py::EfficientNetV2L [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/applications/efficientnet_v2.py]
def EfficientNetV2L(
    include_top=True,
    weights="imagenet",
    input_tensor=None,
    input_shape=None,
    pooling=None,
    classes=1000,
    classifier_activation="softmax",
    include_preprocessing=True,
    name="efficientnetv2-l",
):
    return EfficientNetV2(
        width_coefficient=1.0,
        depth_coefficient=1.0,
        default_size=480,
        name=name,
        include_top=include_top,
        weights=weights,
        input_tensor=input_tensor,
        input_shape=input_shape,
        pooling=pooling,
        classes=classes,
        classifier_activation=classifier_activation,
        include_preprocessing=include_preprocessing,
        weights_name="-l",
    )

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/torch/math.py::top_k [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/torch/math.py]
def top_k(x, k, sorted=True):
    x = convert_to_tensor(x)
    return torch.topk(x, k, sorted=sorted)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py::TopKCategoricalAccuracy.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py]
    def __init__(self, k=5, name="top_k_categorical_accuracy", dtype=None):
        super().__init__(
            fn=top_k_categorical_accuracy,
            name=name,
            dtype=dtype,
            k=k,
        )
        self.k = k
        # Metric should be maximized during optimization.
        self._direction = "up"

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/applications/convnext.py::ConvNeXtXLarge [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/applications/convnext.py]
def ConvNeXtXLarge(
    include_top=True,
    include_preprocessing=True,
    weights="imagenet",
    input_tensor=None,
    input_shape=None,
    pooling=None,
    classes=1000,
    classifier_activation="softmax",
    name="convnext_xlarge",
):
    return ConvNeXt(
        weights_name="convnext_xlarge",
        depths=MODEL_CONFIGS["xlarge"]["depths"],
        projection_dims=MODEL_CONFIGS["xlarge"]["projection_dims"],
        drop_path_rate=0.0,
        layer_scale_init_value=1e-6,
        default_size=MODEL_CONFIGS["xlarge"]["default_size"],
        name=name,
        include_top=include_top,
        include_preprocessing=include_preprocessing,
        weights=weights,
        input_tensor=input_tensor,
        input_shape=input_shape,
        pooling=pooling,
        classes=classes,
        classifier_activation=classifier_activation,
    )

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/applications/efficientnet.py::EfficientNetB0 [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/applications/efficientnet.py]
def EfficientNetB0(
    include_top=True,
    weights="imagenet",
    input_tensor=None,
    input_shape=None,
    pooling=None,
    classes=1000,
    classifier_activation="softmax",
    name="efficientnetb0",
):
    return EfficientNet(
        1.0,
        1.0,
        224,
        0.2,
        name=name,
        include_top=include_top,
        weights=weights,
        input_tensor=input_tensor,
        input_shape=input_shape,
        pooling=pooling,
        classes=classes,
        classifier_activation=classifier_activation,
        weights_name="b0",
    )
```
