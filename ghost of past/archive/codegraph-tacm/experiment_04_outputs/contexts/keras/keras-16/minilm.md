# keras-16 :: minilm

query: Modify Sequential config to include model name (breaking change). Matches tf.keras behavior as of TF 1.11.0. (#11133)

## selected nodes

- rank=1 layer=FUNCTION tokens=175 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/base_benchmark.py::LayerBenchmark._build_tf_keras_model file=/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/base_benchmark.py
- rank=2 layer=FUNCTION tokens=475 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/callbacks/tensorboard.py::TensorBoard._configure_embeddings file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/callbacks/tensorboard.py
- rank=3 layer=FUNCTION tokens=1822 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/export/tf2onnx_lib.py::patch_tf2onnx file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/export/tf2onnx_lib.py
- rank=4 layer=FUNCTION tokens=205 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/data_adapters/data_adapter.py::DataAdapter.get_tf_dataset file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/data_adapters/data_adapter.py
- rank=5 layer=FUNCTION tokens=539 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/function.py::Function.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/function.py
- rank=6 layer=FUNCTION tokens=375 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/export/openvino_test.py::get_model file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/export/openvino_test.py
- rank=7 layer=FUNCTION tokens=373 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/export/onnx_test.py::get_model file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/export/onnx_test.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/base_benchmark.py::LayerBenchmark._build_tf_keras_model [/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/base_benchmark.py]
    def _build_tf_keras_model(self, input_shape, flat_call_inputs=True):
        inputs = []
        if not isinstance(input_shape[0], (tuple, list)):
            input_shape = [input_shape]

        for shape in input_shape:
            inputs.append(tf.keras.Input(shape=shape))

        if flat_call_inputs:
            outputs = self._tf_keras_layer(*inputs)
        else:
            outputs = self._tf_keras_layer(inputs)
        return tf.keras.Model(inputs=inputs, outputs=outputs)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/callbacks/tensorboard.py::TensorBoard._configure_embeddings [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/callbacks/tensorboard.py]
    def _configure_embeddings(self):
        """Configure the Projector for embeddings."""
        from google.protobuf import text_format
        from tensorboard.plugins import projector

        config = projector.ProjectorConfig()
        for layer in self.model.layers:
            if isinstance(layer, Embedding):
                embedding = config.embeddings.add()
                # Embeddings are always the first layer, so this naming should
                # be consistent in any keras models checkpoints.
                name = (
                    "layer_with_weights-0/embeddings/.ATTRIBUTES/VARIABLE_VALUE"
                )
                embedding.tensor_name = name

                if self.embeddings_metadata is not None:
                    if isinstance(self.embeddings_metadata, str):
                        embedding.metadata_path = self.embeddings_metadata
                    else:
                        if layer.name in self.embeddings_metadata.keys():
                            embedding.metadata_path = (
                                self.embeddings_metadata.pop(layer.name)
                            )

        if self.embeddings_metadata and not isinstance(
            self.embeddings_metadata, str
        ):
            raise ValueError(
                "Unrecognized `Embedding` layer names passed to "
                "`keras.callbacks.TensorBoard` `embeddings_metadata` "
                f"argument: {self.embeddings_metadata.keys()}"
            )

        config_pbtxt = text_format.MessageToString(config)
        path = os.path.join(self._log_write_dir, "projector_config.pbtxt")
        with file_utils.File(path, "w") as f:
            f.write(config_pbtxt)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/export/tf2onnx_lib.py::patch_tf2onnx [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/export/tf2onnx_lib.py]
def patch_tf2onnx():
    """Patches `tf2onnx` to ensure compatibility with numpy>=2.0.0."""

    from onnx import AttributeProto
    from onnx import TensorProto

    from keras.src.utils.module_utils import tf2onnx

    logger = logging.getLogger(tf2onnx.__name__)

    if not hasattr(np, "object"):
        np.object = object

    def patched_rewrite_constant_fold(g, ops):
        """
        We call tensorflow transform with constant folding but in some cases
        tensorflow does fold all constants. Since there are a bunch of ops in
        onnx that use attributes where tensorflow has dynamic inputs, we badly
        want constant folding to work. For cases where tensorflow missed
        something, make another pass over the graph and fix want we care about.
        """
        func_map = {
            "Add": np.add,
            "GreaterEqual": np.greater_equal,
            "Cast": np.asarray,
            "ConcatV2": np.concatenate,
            "Less": np.less,
            "ListDiff": np.setdiff1d,
            "Mul": np.multiply,
            "Pack": np.stack,
            "Range": np.arange,
            "Sqrt": np.sqrt,
            "Sub": np.subtract,
        }
        ops = list(ops)

        keep_looking = True
        while keep_looking:
            keep_looking = False
            for idx, op in enumerate(ops):
                func = func_map.get(op.type)
                if func is None:
                    continue
                if set(op.output) & set(g.outputs):
                    continue
                try:
                    inputs = []
                    for node in op.inputs:
                        if not node.is_const():
                            break
                        inputs.append(node.get_tensor_value(as_list=False))

                    logger.debug(
                        "op name %s, %s, %s",
                        op.name,
                        len(op.input),
                        len(inputs),
                    )
                    if inputs and len(op.input) == len(inputs):
                        logger.info(
                            "folding node type=%s, name=%s" % (op.type, op.name)
                        )
                        if op.type == "Cast":
                            dst = op.get_attr_int("to")
                            np_type = tf2onnx.utils.map_onnx_to_numpy_type(dst)
                            val = np.asarray(*inputs, dtype=np_type)
                        elif op.type == "ConcatV2":
                            axis = inputs[-1]
                            values = inputs[:-1]
                            val = func(tuple(values), axis)
                        elif op.type == "ListDiff":
                            out_type = op.get_attr_int("out_idx")
                            np_type = tf2onnx.utils.map_onnx_to_numpy_type(
                                out_type
                            )
                            val = func(*inputs)
                            val = val.astype(np_type)
                        elif op.type in ["Pack"]:
                            # handle ops that need input array and axis
                            axis = op.get_attr_int("axis")
                            val = func(inputs, axis=axis)
                        elif op.type == "Range":
                            dtype = op.get_attr_int("Tidx")
                            np_type = tf2onnx.utils.map_onnx_to_numpy_type(
                                dtype
                            )
                            val = func(*inputs, dtype=np_type)
                        else:
                            val = func(*inputs)

                        new_node_name = tf2onnx.utils.make_name(op.name)
                        new_output_name = new_node_name
                        old_output_name = op.output[0]
                        old_node_name = op.name
                        logger.debug(
                            "create const node [%s] replacing [%s]",
                            new_node_name,
                            old_node_name,
                        )
                        ops[idx] = g.make_const(new_node_name, val)

                        logger.debug(
                            "replace old output [%s] with new output [%s]",
                            old_output_name,
                            new_output_name,
                        )
                        # need to re-write the consumers input name to use the
                        # const name
                        consumers = g.find_output_consumers(old_output_name)
                        if consumers:
                            for consumer in consumers:
                                g.replace_input(
                                    consumer, old_output_name, new_output_name
                                )

                        # keep looking until there is nothing we can fold.
                        # We keep the graph in topological order so if we
                        # folded, the result might help a following op.
                        keep_looking = True
                except Exception as ex:
                    tb = traceback.format_exc()
                    logger.info("exception: %s, details: %s", ex, tb)
                    # ignore errors

        return ops

    def patched_get_value_attr(self, external_tensor_storage=None):
        """
        Return onnx attr for value property of node.
        Attr is modified to point to external tensor data stored in
        external_tensor_storage, if included.
        """
        a = self._attr["value"]
        if (
            external_tensor_storage is not None
            and self in external_tensor_storage.node_to_modified_value_attr
        ):
            return external_tensor_storage.node_to_modified_value_attr[self]
        if external_tensor_storage is None or a.type != AttributeProto.TENSOR:
            return a

        def prod(x):
            if hasattr(np, "product"):
                return np.product(x)
            else:
                return np.prod(x)

        if (
            prod(a.t.dims)
            > external_tensor_storage.external_tensor_size_threshold
        ):
            a = copy.deepcopy(a)
            tensor_name = (
                f"{self.name.strip()}_{external_tensor_storage.name_counter}"
            )
            for c in '~"#%&*:<>?/\\{|}':
                tensor_name = tensor_name.replace(c, "_")
            external_tensor_storage.name_counter += 1
            external_tensor_storage.name_to_tensor_data[tensor_name] = (
                a.t.raw_data
            )
            external_tensor_storage.node_to_modified_value_attr[self] = a
            a.t.raw_data = b""
            a.t.ClearField("raw_data")
            location = a.t.external_data.add()
            location.key = "location"
            location.value = tensor_name
            a.t.data_location = TensorProto.EXTERNAL
        return a

    tf2onnx.tfonnx.rewrite_constant_fold = patched_rewrite_constant_fold
    tf2onnx.graph.Node.get_value_attr = patched_get_value_attr

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/data_adapters/data_adapter.py::DataAdapter.get_tf_dataset [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/data_adapters/data_adapter.py]
    def get_tf_dataset(self):
        """Get a `tf.data.Dataset` instance for the DataAdapter.

        Note that the dataset returned does not repeat for epoch, so caller
        might need to create new iterator for the same dataset at the beginning
        of the epoch. This behavior might change in the future.

        Returns:
            A `tf.data.Dataset`. Caller might use the dataset in different
            context, e.g. iter(dataset) in eager to get the value directly, or
            in graph mode, provide the iterator tensor to Keras model function.
        """
        raise NotImplementedError

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/function.py::Function.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/function.py]
    def __init__(self, inputs, outputs, name=None):
        super().__init__(name=name)

        if backend() == "tensorflow":
            # Temporary work around for
            # https://github.com/keras-team/keras/issues/931
            # This stop tensorflow from wrapping tf.function output in a
            # _DictWrapper object.
            _self_setattr_tracking = getattr(
                self, "_self_setattr_tracking", True
            )
            self._self_setattr_tracking = False
        self._inputs_struct = tree.map_structure(lambda x: x, inputs)
        self._outputs_struct = tree.map_structure(lambda x: x, outputs)
        self._inputs = tree.flatten(inputs)
        self._outputs = tree.flatten(outputs)
        if not self._inputs:
            raise ValueError(
                "`inputs` argument cannot be empty. Received:\n"
                f"inputs={inputs}\n"
                f"outputs={outputs}"
            )
        if not self._outputs:
            raise ValueError(
                "`outputs` argument cannot be empty. Received:\n"
                f"inputs={inputs}\n"
                f"outputs={outputs}"
            )

        if backend() == "tensorflow":
            self._self_setattr_tracking = _self_setattr_tracking

        (nodes, nodes_by_depth, operations, operations_by_depth) = map_graph(
            self._inputs, self._outputs
        )
        self._nodes = nodes
        self._nodes_by_depth = nodes_by_depth
        self._operations = operations
        self._operations_by_depth = operations_by_depth

        # Run through graph to check all outputs are connected to the inputs.
        def empty_op_outputs(op, *args, **kwargs):
            return [None] * len(tree.flatten(op.output))

        self._run_through_graph(
            [None] * len(self._inputs), call_fn=empty_op_outputs
        )

        # Special handling for NNX to ensure consistent operation instance usage
        if is_nnx_enabled():
            self._setup_nnx_op_mapping()

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/export/openvino_test.py::get_model [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/export/openvino_test.py]
def get_model(type="sequential", input_shape=(10,), layer_list=None):
    layer_list = layer_list or [
        layers.Dense(10, activation="relu"),
        layers.BatchNormalization(),
        layers.Dense(1, activation="sigmoid"),
    ]
    if type == "sequential":
        return models.Sequential(layer_list)
    elif type == "functional":
        input = output = tree.map_shape_structure(layers.Input, input_shape)
        for layer in layer_list:
            output = layer(output)
        return models.Model(inputs=input, outputs=output)
    elif type == "subclass":
        return CustomModel(layer_list)
    elif type == "lstm":
        # https://github.com/keras-team/keras/issues/21390
        inputs = layers.Input((4, 10))
        x = layers.Bidirectional(
            layers.LSTM(
                10,
                kernel_initializer="he_normal",
                return_sequences=True,
                kernel_regularizer=None,
            ),
            merge_mode="sum",
        )(inputs)
        outputs = layers.Bidirectional(
            layers.LSTM(
                10,
                kernel_initializer="he_normal",
                return_sequences=True,
                kernel_regularizer=None,
            ),
            merge_mode="concat",
        )(x)
        return models.Model(inputs=inputs, outputs=outputs)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/export/onnx_test.py::get_model [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/export/onnx_test.py]
def get_model(type="sequential", input_shape=(10,), layer_list=None):
    layer_list = layer_list or [
        layers.Dense(10, activation="relu"),
        layers.BatchNormalization(),
        layers.Dense(1, activation="sigmoid"),
    ]
    if type == "sequential":
        return models.Sequential(layer_list)
    elif type == "functional":
        input = output = tree.map_shape_structure(layers.Input, input_shape)
        for layer in layer_list:
            output = layer(output)
        return models.Model(inputs=input, outputs=output)
    elif type == "subclass":
        return CustomModel(layer_list)
    elif type == "lstm":
        # https://github.com/keras-team/keras/issues/21390
        inputs = layers.Input((4, 10))
        x = layers.Bidirectional(
            layers.LSTM(
                10,
                kernel_initializer="he_normal",
                return_sequences=True,
                kernel_regularizer=None,
            ),
            merge_mode="sum",
        )(inputs)
        outputs = layers.Bidirectional(
            layers.LSTM(
                10,
                kernel_initializer="he_normal",
                return_sequences=True,
                kernel_regularizer=None,
            ),
            merge_mode="concat",
        )(x)
        return models.Model(inputs=inputs, outputs=outputs)
```
