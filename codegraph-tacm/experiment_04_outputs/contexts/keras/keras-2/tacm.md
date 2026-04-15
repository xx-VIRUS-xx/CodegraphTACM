# keras-2 :: tacm

query: Fix in_top_k tests to include CNTK [Test fails] (#12336)

## selected nodes

- rank=1 layer=FILE tokens=63 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/math.py file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/math.py
- rank=2 layer=FILE tokens=59 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/math.py file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/math.py
- rank=3 layer=FILE tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/math.py file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/math.py
- rank=4 layer=FILE tokens=10 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/__init__.py file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/__init__.py
- rank=5 layer=CLASS tokens=22 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math_test.py::InTopKTest file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math_test.py
- rank=6 layer=CLASS tokens=28 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math_test.py::TopKTest file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math_test.py
- rank=7 layer=CLASS tokens=82 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math_test.py::MathOpsDynamicShapeTest file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math_test.py
- rank=8 layer=CLASS tokens=122 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/confusion_metrics_test.py::PrecisionTest file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/confusion_metrics_test.py
- rank=9 layer=CLASS tokens=121 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/confusion_metrics_test.py::RecallTest file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/confusion_metrics_test.py
- rank=10 layer=CLASS tokens=150 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math_test.py::MathOpsCorrectnessTest file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math_test.py
- rank=11 layer=CLASS tokens=49 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/integration_tests/dataset_tests/imdb_test.py::ImdbLoadDataTest file=/Users/xxvirusxx/PY/CodegraphTACM/keras/integration_tests/dataset_tests/imdb_test.py
- rank=12 layer=CLASS tokens=107 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/preprocessing/hashed_crossing_test.py::HashedCrossingTest file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/preprocessing/hashed_crossing_test.py
- rank=13 layer=CLASS tokens=88 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math_test.py::MathOpsStaticShapeTest file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math_test.py
- rank=14 layer=CLASS tokens=25 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/integration_tests/model_visualization_test.py::ModelVisualizationTest.SplitLayer file=/Users/xxvirusxx/PY/CodegraphTACM/keras/integration_tests/model_visualization_test.py
- rank=15 layer=FUNCTION tokens=22 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/math.py::in_top_k file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/math.py
- rank=16 layer=FUNCTION tokens=49 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/math.py::top_k file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/math.py
- rank=17 layer=FUNCTION tokens=18 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/math.py::top_k file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/math.py
- rank=18 layer=FUNCTION tokens=276 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/math.py::in_top_k file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/math.py
- rank=19 layer=FUNCTION tokens=148 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/metrics_utils.py::_filter_top_k file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/metrics_utils.py
- rank=20 layer=FUNCTION tokens=30 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/backend.py::in_top_k file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/backend.py
- rank=21 layer=FUNCTION tokens=224 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math.py::top_k file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math.py
- rank=22 layer=FUNCTION tokens=108 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/math.py::erfinv file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/math.py
- rank=23 layer=FUNCTION tokens=152 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/math.py::top_k file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/math.py
- rank=24 layer=FUNCTION tokens=103 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/math.py::in_top_k file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/math.py
- rank=25 layer=FUNCTION tokens=164 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/applications/applications_test.py::_get_elephant file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/applications/applications_test.py
- rank=26 layer=FUNCTION tokens=92 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/math.py::top_k file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/math.py
- rank=27 layer=FUNCTION tokens=239 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math.py::in_top_k file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math.py
- rank=28 layer=FUNCTION tokens=93 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/torch/math.py::in_top_k file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/torch/math.py
- rank=29 layer=FUNCTION tokens=64 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/math.py::in_top_k file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/math.py
- rank=30 layer=FUNCTION tokens=45 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/integration_tests/import_test.py::run_keras_flow file=/Users/xxvirusxx/PY/CodegraphTACM/keras/integration_tests/import_test.py
- rank=31 layer=FUNCTION tokens=70 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/applications/mobilenet_v2.py::MobileNetV2 file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/applications/mobilenet_v2.py
- rank=32 layer=FUNCTION tokens=70 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/applications/convnext.py::ConvNeXt file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/applications/convnext.py
- rank=33 layer=FUNCTION tokens=70 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/applications/inception_v3.py::InceptionV3 file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/applications/inception_v3.py
- rank=34 layer=FUNCTION tokens=174 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/applications/efficientnet_v2.py::EfficientNetV2B0 file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/applications/efficientnet_v2.py
- rank=35 layer=FUNCTION tokens=174 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/applications/efficientnet_v2.py::EfficientNetV2B1 file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/applications/efficientnet_v2.py
- rank=36 layer=FUNCTION tokens=174 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/applications/efficientnet_v2.py::EfficientNetV2B2 file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/applications/efficientnet_v2.py
- rank=37 layer=FUNCTION tokens=174 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/applications/efficientnet_v2.py::EfficientNetV2B3 file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/applications/efficientnet_v2.py
- rank=38 layer=FUNCTION tokens=174 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/applications/efficientnet_v2.py::EfficientNetV2S file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/applications/efficientnet_v2.py
- rank=39 layer=FUNCTION tokens=68 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/metrics_utils.py::update_confusion_matrix_variables file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/metrics_utils.py
- rank=40 layer=FUNCTION tokens=25 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/torch/math.py::top_k file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/torch/math.py

## context

```text
file backend/tensorflow/math.py
imports: tensorflow, keras
defines: segment_sum, segment_max, top_k, in_top_k, logsumexp, qr, extract_sequences, _get_complex_tensor_from_tuple, fft, fft2, ifft2, rfft, irfft, stft, win, istft, rsqrt, erf, erfinv, logdet

file backend/jax/math.py
imports: math, jax, keras
defines: segment_sum, segment_max, top_k, in_top_k, logsumexp, qr, extract_sequences, _get_complex_tensor_from_tuple, fft, fft2, ifft2, rfft, irfft, stft, istft, rsqrt, erf, erfinv, logdet

file backend/openvino/math.py
imports: numpy, openvino, scipy, keras
defines: _segment_reduction_fn, segment_sum, segment_max, top_k, in_top_k, logsumexp, qr, extract_sequences, _dft, fft, fft2, ifft2, rfft, irfft, stft, _overlap_sequences_ov, istft, rsqrt, erf, erfinv

file __init__.py
imports: keras
defines: —

class InTopKTest(testing.TestCase):  [ops/math_test.py:1150]
methods: test_in_top_k_call

class TopKTest(testing.TestCase):  [ops/math_test.py:1130]
methods: test_top_k_call_indices, test_top_k_call_values

class MathOpsDynamicShapeTest(testing.TestCase):  [ops/math_test.py:145]
methods: test_extract_sequences, test_fft, test_fft2, test_ifft2
         test_in_top_k, test_irfft, test_istft
         test_istft_with_length, test_logdet
         test_logsumexp, test_rfft, test_rsqrt
         test_segment_reduce, test_stft, test_top_k

class PrecisionTest(testing.TestCase):  [metrics/confusion_metrics_test.py:377]
methods: test_config, test_div_by_zero, test_multiple_updates
         test_unweighted, test_unweighted_all_incorrect
         test_unweighted_class_id_multiclass
         test_unweighted_class_id_should_throw_error_1d
         test_unweighted_top_k
         test_unweighted_top_k_and_threshold
         test_unweighted_with_threshold, test_weighted
         test_weighted_top_k, test_weighted_with_threshold

class RecallTest(testing.TestCase):  [metrics/confusion_metrics_test.py:543]
methods: test_config, test_div_by_zero, test_multiple_updates
         test_unweighted, test_unweighted_all_incorrect
         test_unweighted_class_id_multiclass
         test_unweighted_class_id_should_throw_error_1d
         test_unweighted_top_k
         test_unweighted_top_k_and_threshold
         test_unweighted_with_threshold, test_weighted
         test_weighted_top_k, test_weighted_with_threshold

class MathOpsCorrectnessTest(testing.TestCase):  [ops/math_test.py:482]
methods: run_segment_reduce_test, test_erf_operation_basic
         test_erf_operation_dtype
         test_erf_operation_edge_cases
         test_erfinv_operation_basic
         test_erfinv_operation_dtype
         test_erfinv_operation_edge_cases
         test_extract_sequences, test_fft, test_fft2
         test_ifft2, test_in_top_k, test_irfft, test_istft
         test_logdet, test_logsumexp, test_rfft
         test_rsqrt, test_segment_reduce
         test_segment_reduce_explicit_num_segments
         test_stft, test_top_k

class ImdbLoadDataTest(testing.TestCase):  [integration_tests/dataset_tests/imdb_test.py:7]
methods: test_get_word_index, test_load_data_default, test_maxlen
         test_num_words, test_skip_top

class HashedCrossingTest(testing.TestCase):  [layers/preprocessing/hashed_crossing_test.py:12]
methods: call_layer, test_basics, test_correctness
         test_cross_output_dtype, test_float_input_fails
         test_non_list_input_fails
         test_single_input_fails, test_sparse_input_fails
         test_static_shape_preserved
         test_tf_data_compatibility, test_tf_string
         test_unsupported_shape_input_fails

class MathOpsStaticShapeTest(testing.TestCase):  [ops/math_test.py:338]
methods: test_extract_sequences, test_fft, test_fft2, test_ifft2
         test_in_top_k, test_irfft, test_istft
         test_logdet, test_logsumexp, test_rfft
         test_rsqrt, test_segment_reduce
         test_segment_reduce_explicit_num_segments
         test_stft, test_topk

class SplitLayer(keras.Layer):  [keras/integration_tests/model_visualization_test.py:266]
methods: —

def in_top_k(targets, predictions, k):
    return tf.math.in_top_k(targets, predictions, k)

def top_k(x, k, sorted=True):
    # Jax does not supported `sorted`, but in the case where `sorted=False`,
    # order is not guaranteed, so OK to return sorted output.
    return jax.lax.top_k(x, k)

def top_k(x, k, sorted=True):
    return tf.math.top_k(x, k, sorted=sorted)

def in_top_k(targets, predictions, k):
    from keras.src.backend.openvino.numpy import take_along_axis

    # Expand targets: (batch,) → (batch, 1) for use with take_along_axis
    targets = ov_opset.unsqueeze(
        get_ov_output(targets), ov_opset.constant(1, Type.i32)
    ).output(0)
    predictions = get_ov_output(predictions)

    # top_k returns (batch, k) sorted descending; last col is the k-th largest
    topk_values = top_k(predictions, k)[0]
    # Grab only the last column (index k-1): threshold value, shape (batch,)
    k_minus_1_idx = ov_opset.constant([k - 1], dtype=Type.i32).output(0)
    topk_values_axis = ov_opset.constant(1, dtype=Type.i32).output(0)
    topk_min = ov_opset.gather(
        topk_values, k_minus_1_idx, topk_values_axis
    ).output(0)

    # Gather the prediction score at each true class index → shape (batch, 1)
    targets_values = take_along_axis(predictions, targets, axis=-1)
    # target score >= k-th largest score means it belongs in the top-k
    mask = ov_opset.greater_equal(targets_values, topk_min).output(0)
    return OpenVINOKerasTensor(mask)

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

def in_top_k(predictions, targets, k):
    """DEPRECATED."""
    return tf.compat.v1.math.in_top_k(predictions, targets, k)

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

def erfinv(x):
    # TODO: Float64 infinity values are clamped on CPU backend,
    # breaking erfinv(±1) = ±inf
    # See https://github.com/openvinotoolkit/openvino/issues/34138
    # Tests excluded: test_erfinv_operation_basic, test_erfinv_operation_dtype
    x = get_ov_output(x)
    dtype = x.get_element_type()

    a = 0.147
    two_over_pi_a = 2.0 / (np.pi * a)
    two_over_sqrt_pi = 2.0 / np.sqrt(np.pi)

    # ... truncated

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

def in_top_k(targets, predictions, k):
    preds_at_label = jnp.take_along_axis(
        predictions, jnp.expand_dims(targets, axis=-1), axis=-1
    )
    # `nan` shouldn't be considered as large probability.
    preds_at_label = jnp.where(
        jnp.isnan(preds_at_label), -jnp.inf, preds_at_label
    )
    rank = 1 + jnp.sum(jnp.greater(predictions, preds_at_label), axis=-1)
    return jnp.less_equal(rank, k)

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

def top_k(x, k, sorted=True):
    x = get_ov_output(x)
    k_tensor = ov_opset.constant(k, dtype=Type.i32)
    axis = -1
    sort_type = "value" if sorted else "none"
    topk_node = ov_opset.topk(x, k_tensor, axis, "max", sort_type)
    values = topk_node.output(0)
    indices = topk_node.output(1)
    return OpenVINOKerasTensor(values), OpenVINOKerasTensor(indices)

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

def in_top_k(targets, predictions, k):
    targets = convert_to_tensor(targets).type(torch.int64)
    targets = targets[:, None]
    predictions = convert_to_tensor(predictions)
    topk_values = top_k(predictions, k).values
    targets_values = torch.take_along_dim(predictions, targets, dim=-1)
    mask = targets_values >= topk_values
    return torch.any(mask, axis=-1)

def in_top_k(targets, predictions, k):
    targets = targets[:, None]
    topk_values = top_k(predictions, k)[0]
    targets_values = np.take_along_axis(predictions, targets, axis=-1)
    mask = targets_values >= topk_values
    return np.any(mask, axis=-1)

def run_keras_flow():
    test_script = [
        # Runs the example script
        "python -m pytest integration_tests/basic_full_flow.py",
    ]
    run_commands_venv(test_script)

def MobileNetV2(
    input_shape=None,
    alpha=1.0,
    include_top=True,
    weights="imagenet",
    input_tensor=None,
    pooling=None,
    classes=1000,
    classifier_activation="softmax",
    name=None,
):
    """Instantiates the MobileNetV2 architecture.
    # ... truncated

def ConvNeXt(
    depths,
    projection_dims,
    drop_path_rate=0.0,
    layer_scale_init_value=1e-6,
    default_size=224,
    name="convnext",
    include_preprocessing=True,
    include_top=True,
    weights=None,
    input_tensor=None,
    input_shape=None,
    # ... truncated

def InceptionV3(
    include_top=True,
    weights="imagenet",
    input_tensor=None,
    input_shape=None,
    pooling=None,
    classes=1000,
    classifier_activation="softmax",
    name="inception_v3",
):
    """Instantiates the Inception v3 architecture.

    # ... truncated

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

def update_confusion_matrix_variables(
    variables_to_update,
    y_true,
    y_pred,
    thresholds,
    top_k=None,
    class_id=None,
    sample_weight=None,
    multi_label=False,
    label_weights=None,
    thresholds_distributed_evenly=False,
):
    # ... truncated

def top_k(x, k, sorted=True):
    x = convert_to_tensor(x)
    return torch.topk(x, k, sorted=sorted)
```
