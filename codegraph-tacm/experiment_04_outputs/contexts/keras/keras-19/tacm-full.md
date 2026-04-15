# keras-19 :: tacm-full

query: Update the RNN cell API to be explicit about output_size. (#11021)

## selected nodes

- rank=1 layer=FUNCTION tokens=124 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/operation.py::Operation.output file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/operation.py
- rank=2 layer=FUNCTION tokens=193 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/stacked_rnn_cells.py::StackedRNNCells.build file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/stacked_rnn_cells.py
- rank=3 layer=FUNCTION tokens=206 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py::RNN.get_initial_state file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py
- rank=4 layer=FUNCTION tokens=273 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py::RNN.build file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py
- rank=5 layer=FUNCTION tokens=146 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/dropout_rnn_cell.py::DropoutRNNCell.reset_dropout_mask file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/dropout_rnn_cell.py
- rank=6 layer=FUNCTION tokens=182 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py::RNN.compute_mask file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py
- rank=7 layer=FUNCTION tokens=55 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/functional.py::Functional.output file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/functional.py
- rank=8 layer=FUNCTION tokens=255 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/rnn.py::_assert_valid_mask file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/rnn.py
- rank=9 layer=FUNCTION tokens=177 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/python_utils.py::ensure_value_to_cell file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/python_utils.py
- rank=10 layer=FUNCTION tokens=419 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/numpy.py::unique file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/numpy.py
- rank=11 layer=FUNCTION tokens=414 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/api_gen.py::build file=/Users/xxvirusxx/PY/CodegraphTACM/keras/api_gen.py
- rank=12 layer=FUNCTION tokens=873 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/operation_utils.py::compute_pooling_output_shape file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/operation_utils.py
- rank=13 layer=FUNCTION tokens=264 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/torch/rnn.py::_assert_valid_mask file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/torch/rnn.py
- rank=14 layer=FUNCTION tokens=285 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py::RNN.compute_output_shape file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py
- rank=15 layer=FUNCTION tokens=59 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/conv_lstm.py::ConvLSTM.kernel_size file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/conv_lstm.py
- rank=16 layer=FUNCTION tokens=72 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/metric.py::Metric.update_state file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/metric.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/operation.py::Operation.output [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/operation.py]
    def output(self):
        """Retrieves the output tensor(s) of a layer.

        Only returns the tensor(s) corresponding to the *first time*
        the operation was called.

        Returns:
            Output tensor or list of output tensors.
        """
        return self._get_node_attribute_at_index(0, "output_tensors", "output")

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/stacked_rnn_cells.py::StackedRNNCells.build [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/stacked_rnn_cells.py]
    def build(self, input_shape):
        for cell in self.cells:
            if isinstance(cell, Layer) and not cell.built:
                cell.build(input_shape)
                cell.built = True
            if getattr(cell, "output_size", None) is not None:
                output_dim = cell.output_size
            elif isinstance(cell.state_size, (list, tuple)):
                output_dim = cell.state_size[0]
            else:
                output_dim = cell.state_size
            batch_size = tree.flatten(input_shape)[0]
            input_shape = (batch_size, output_dim)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py::RNN.get_initial_state [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py]
    def get_initial_state(self, batch_size):
        get_initial_state_fn = getattr(self.cell, "get_initial_state", None)
        if get_initial_state_fn:
            init_state = get_initial_state_fn(batch_size=batch_size)
        else:
            return [
                ops.zeros((batch_size, d), dtype=self.cell.compute_dtype)
                for d in self.state_size
            ]

        # RNN expect the states in a list, even if single state.
        if not tree.is_nested(init_state):
            init_state = [init_state]
        # Force the state to be a list in case it is a namedtuple eg
        # LSTMStateTuple.
        return list(init_state)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py::RNN.build [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py]
    def build(self, sequences_shape, initial_state_shape=None):
        # Build cell (if layer).
        step_input_shape = (sequences_shape[0],) + tuple(sequences_shape[2:])
        if isinstance(self.cell, Layer) and not self.cell.built:
            self.cell.build(step_input_shape)
            self.cell.built = True
        if self.stateful:
            if self.states is not None:
                self.reset_state()
            else:
                if sequences_shape[0] is None:
                    raise ValueError(
                        "When using `stateful=True` in a RNN, the "
                        "batch size must be static. Found dynamic "
                        f"batch size: sequence.shape={sequences_shape}"
                    )
                self._create_state_variables(sequences_shape[0])
                self._expected_batch_size = ops.shape(
                    tree.flatten(self.states)[0]
                )[0]

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/dropout_rnn_cell.py::DropoutRNNCell.reset_dropout_mask [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/dropout_rnn_cell.py]
    def reset_dropout_mask(self):
        """Reset the cached dropout mask if any.

        The RNN layer invokes this in the `call()` method
        so that the cached mask is cleared after calling `cell.call()`. The
        mask should be cached across all timestep within the same batch, but
        shouldn't be cached between batches.
        """
        self._dropout_mask = None

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py::RNN.compute_mask [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py]
    def compute_mask(self, _, mask):
        # Time step masks must be the same for each input.
        # This is because the mask for an RNN is of size [batch, time_steps, 1],
        # and specifies which time steps should be skipped, and a time step
        # must be skipped for all inputs.
        mask = tree.flatten(mask)[0]
        output_mask = mask if self.return_sequences else None
        if self.return_state:
            state_mask = [None for _ in self.state_size]
            return [output_mask] + state_mask
        else:
            return output_mask

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/functional.py::Functional.output [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/functional.py]
    def output(self):
        return self._outputs_struct

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/rnn.py::_assert_valid_mask [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/rnn.py]
def _assert_valid_mask(mask):
    valid = tf.logical_and(
        tf.logical_not(_has_fully_masked_sequence(mask)),
        _is_sequence_right_padded(mask),
    )
    tf.Assert(
        valid,
        [
            (
                "You are passing a RNN mask that does not correspond to "
                "right-padded sequences, while using cuDNN, which is not "
                "supported. With cuDNN, RNN masks can only be used for "
                "right-padding, e.g. `[[True, True, False, False]]` would "
                "be a valid mask, but any mask that isn't just contiguous "
                "`True`'s on the left and contiguous `False`'s on the right "
                "would be invalid. You can pass `use_cudnn=False` to your "
                "RNN layer to stop using cuDNN (this may be slower)."
            )
        ],
    )

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/python_utils.py::ensure_value_to_cell [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/python_utils.py]
    def ensure_value_to_cell(value):
        """Ensures that a value is converted to a python cell object.

        Args:
            value: Any value that needs to be casted to the cell type

        Returns:
            A value wrapped as a cell object (see function "func_load")
        """

        def dummy_fn():
            value  # just access it so it gets captured in .__closure__

        cell_value = dummy_fn.__closure__[0]
        if not isinstance(value, type(cell_value)):
            return cell_value
        return value

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/numpy.py::unique [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/numpy.py]
def unique(
    x,
    sorted=True,
    return_inverse=False,
    return_counts=False,
    axis=None,
    size=None,
    fill_value=None,
):
    # Note: np.unique always sorts the output in versions < 2.3.0.
    # We accept the 'sorted' argument for API consistency across backends
    # but do not pass it to np.unique to avoid TypeError in older versions.
    output = np.unique(
        x,
        return_inverse=return_inverse,
        return_counts=return_counts,
        axis=axis,
        equal_nan=False,
    )

    if not (return_inverse or return_counts):
        output = [output]
    else:
        output = list(output)

    values = output[0]

    if size is not None:
        dim = axis if axis is not None else 0
        values_count = values.shape[dim]

        if values_count > size:
            # Truncate
            indices = [slice(None)] * values.ndim
            indices[dim] = slice(0, size)
            values = values[tuple(indices)]
            if return_counts:
                output[-1] = output[-1][tuple(indices)]

        elif values_count < size:
            # Pad
            pad_width = [(0, 0)] * values.ndim
            pad_width[dim] = (0, size - values_count)
            fill = 0 if fill_value is None else fill_value
            values = np.pad(values, pad_width, constant_values=fill)
            if return_counts:
                output[-1] = np.pad(output[-1], pad_width, constant_values=0)

    output[0] = values
    return output[0] if len(output) == 1 else tuple(output)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/api_gen.py::build [/Users/xxvirusxx/PY/CodegraphTACM/keras/api_gen.py]
def build():
    root_path = os.path.dirname(os.path.abspath(__file__))
    code_api_dir = os.path.join(root_path, PACKAGE, "api")
    # Create temp build dir
    build_dir = copy_source_to_build_directory(root_path)
    build_api_dir = os.path.join(build_dir, PACKAGE)
    build_src_dir = os.path.join(build_api_dir, "src")
    build_api_init_fname = os.path.join(build_api_dir, "__init__.py")
    try:
        os.chdir(build_dir)
        open(build_api_init_fname, "w").close()
        namex.generate_api_files(
            "keras",
            code_directory="src",
            exclude_directories=[
                os.path.join("src", "backend", "jax"),
                os.path.join("src", "backend", "openvino"),
                os.path.join("src", "backend", "tensorflow"),
                os.path.join("src", "backend", "torch"),
            ],
        )
        # Add __version__ to `api/`.
        export_version_string(build_api_init_fname)
        # Creates `_tf_keras` with full keras API
        create_legacy_directory(package_dir=os.path.join(build_dir, PACKAGE))
        # Copy back the keras/api and keras/__init__.py from build directory
        if os.path.exists(build_src_dir):
            shutil.rmtree(build_src_dir)
        if os.path.exists(code_api_dir):
            shutil.rmtree(code_api_dir)
        shutil.copytree(
            build_api_dir, code_api_dir, ignore=shutil.ignore_patterns("src/")
        )
    finally:
        # Clean up: remove the build directory (no longer needed)
        shutil.rmtree(build_dir)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/operation_utils.py::compute_pooling_output_shape [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/operation_utils.py]
def compute_pooling_output_shape(
    input_shape,
    pool_size,
    strides,
    padding="valid",
    data_format="channels_last",
):
    """Computes the output shape of pooling operations.

    Args:
        input_shape: Input shape. Must be a tuple of integers.
        pool_size: Size of the pooling operation. Must be a tuple of integers.
        strides: Stride of the pooling operation. Must be a tuple of integers.
            Defaults to `pool_size`.
        padding: Padding method. Available methods are `"valid"` or `"same"`.
            Defaults to `"valid"`.
        data_format: String, either `"channels_last"` or `"channels_first"`.
            The ordering of the dimensions in the inputs. `"channels_last"`
            corresponds to inputs with shape `(batch, height, width, channels)`
            while `"channels_first"` corresponds to inputs with shape
            `(batch, channels, height, weight)`. Defaults to `"channels_last"`.

    Returns:
        Tuple of ints: The output shape of the pooling operation.

    Examples:

    # Basic usage with square pooling on a single image
    >>> compute_pooling_output_shape((1, 4, 4, 1), (2, 2))
    (1, 2, 2, 1)

    # Strided pooling on a single image with strides different from pool_size
    >>> compute_pooling_output_shape((1, 4, 4, 1), (2, 2), strides=(1, 1))
    (1, 3, 3, 1)

    # Pooling on a batch of images
    >>> compute_pooling_output_shape((32, 4, 4, 3), (2, 2))
    (32, 2, 2, 3)
    """
    strides = pool_size if strides is None else strides
    input_shape_origin = list(input_shape)
    input_shape = np.array(input_shape)
    if data_format == "channels_last":
        spatial_shape = input_shape[1:-1]
    else:
        spatial_shape = input_shape[2:]
    none_dims = []
    for i in range(len(spatial_shape)):
        if spatial_shape[i] is None:
            # Set `None` shape to a manual value so that we can run numpy
            # computation on `spatial_shape`.
            spatial_shape[i] = -1
            none_dims.append(i)
    pool_size = np.array(pool_size)
    if padding == "valid":
        output_spatial_shape = (
            np.floor((spatial_shape - pool_size) / strides) + 1
        )
        for i in range(len(output_spatial_shape)):
            if i not in none_dims and output_spatial_shape[i] < 0:
                raise ValueError(
                    "Computed output size would be negative. Received: "
                    f"`inputs.shape={input_shape}` and `pool_size={pool_size}`."
                )
    elif padding == "same":
        output_spatial_shape = np.floor((spatial_shape - 1) / strides) + 1
    else:
        raise ValueError(
            "Argument `padding` must be either 'valid' or 'same'. Received: "
            f"padding={padding}"
        )
    output_spatial_shape = [int(i) for i in output_spatial_shape]
    for i in none_dims:
        output_spatial_shape[i] = None
    output_spatial_shape = tuple(output_spatial_shape)
    if data_format == "channels_last":
        output_shape = (
            (input_shape_origin[0],)
            + output_spatial_shape
            + (input_shape_origin[-1],)
        )
    else:
        output_shape = (
            input_shape_origin[0],
            input_shape_origin[1],
        ) + output_spatial_shape
    return output_shape

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/torch/rnn.py::_assert_valid_mask [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/torch/rnn.py]
def _assert_valid_mask(mask):
    # Check if mask is valid for cuDNN
    no_fully_masked = ~_has_fully_masked_sequence(mask)
    is_right_padded = _is_sequence_right_padded(mask)
    valid = no_fully_masked & is_right_padded

    if not valid.item():
        error_message = (
            "You are passing a RNN mask that does not correspond to "
            "right-padded sequences, while using cuDNN, which is not "
            "supported. With cuDNN, RNN masks can only be used for "
            "right-padding, e.g. `[[True, True, False, False]]` would "
            "be a valid mask, but any mask that isn't just contiguous "
            "`True`'s on the left and contiguous `False`'s on the right "
            "would be invalid. You can pass `use_cudnn=False` to your "
            "RNN layer to stop using cuDNN (this may be slower)."
        )
        raise ValueError(error_message)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py::RNN.compute_output_shape [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py]
    def compute_output_shape(self, sequences_shape, initial_state_shape=None):
        batch_size = sequences_shape[0]
        length = sequences_shape[1]
        states_shape = []
        for state_size in self.state_size:
            if isinstance(state_size, int):
                states_shape.append((batch_size, state_size))
            elif isinstance(state_size, (list, tuple)):
                states_shape.append([(batch_size, s) for s in state_size])

        output_size = getattr(self.cell, "output_size", None)
        if output_size is None:
            output_size = self.state_size[0]
        if not isinstance(output_size, int):
            raise ValueError("output_size must be an integer.")
        if self.return_sequences:
            output_shape = (batch_size, length, output_size)
        else:
            output_shape = (batch_size, output_size)
        if self.return_state:
            return output_shape, *states_shape
        return output_shape

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/conv_lstm.py::ConvLSTM.kernel_size [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/conv_lstm.py]
    def kernel_size(self):
        return self.cell.kernel_size

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/metric.py::Metric.update_state [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/metric.py]
    def update_state(self, *args, **kwargs):
        """Accumulate statistics for the metric."""
        raise NotImplementedError
```
