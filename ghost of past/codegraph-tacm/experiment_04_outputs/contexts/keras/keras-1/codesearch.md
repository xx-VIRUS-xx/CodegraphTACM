# keras-1 :: codesearch

query: Fix initializers and update ops.

## selected nodes

- rank=1 layer=FUNCTION tokens=96 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib_test.py::SavingTest.setUp file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib_test.py
- rank=2 layer=FUNCTION tokens=161 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/function.py::Function._setup_nnx_op_mapping file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/function.py
- rank=3 layer=FUNCTION tokens=100 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/epoch_iterator.py::EpochIterator.reset file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/epoch_iterator.py
- rank=4 layer=FUNCTION tokens=76 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer_test.py::TrainingLayer.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer_test.py
- rank=5 layer=FUNCTION tokens=68 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/config.py::Config.update file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/config.py
- rank=6 layer=FUNCTION tokens=258 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/core.py::scatter_update file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/core.py
- rank=7 layer=FUNCTION tokens=127 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/nn.py::_adjust_kernel file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/nn.py
- rank=8 layer=FUNCTION tokens=1377 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/numpy.py::use_custom_ops file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/numpy.py
- rank=9 layer=FUNCTION tokens=75 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/keras_tensor.py::KerasTensor.__mod__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/keras_tensor.py
- rank=10 layer=FUNCTION tokens=74 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/f_score_metrics.py::FBetaScore.reset_state file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/f_score_metrics.py
- rank=11 layer=FUNCTION tokens=75 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/regression_metrics.py::R2Score.reset_state file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/regression_metrics.py
- rank=12 layer=FUNCTION tokens=77 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/iou_metrics.py::_IoUBase.reset_state file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/iou_metrics.py
- rank=13 layer=FUNCTION tokens=173 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/export/saved_model_test.py::ExportArchiveTest.setUp file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/export/saved_model_test.py
- rank=14 layer=FUNCTION tokens=209 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/image.py::fix_index file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/image.py
- rank=15 layer=FUNCTION tokens=106 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/attention/grouped_query_attention_test.py::GroupedQueryAttentionTest.setUp file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/attention/grouped_query_attention_test.py
- rank=16 layer=FUNCTION tokens=103 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/attention/multi_head_attention_test.py::MultiHeadAttentionTest.setUp file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/attention/multi_head_attention_test.py
- rank=17 layer=FUNCTION tokens=481 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/node.py::Node.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/node.py
- rank=18 layer=FUNCTION tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/core.py::SliceUpdate.call file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/core.py
- rank=19 layer=FUNCTION tokens=86 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/callbacks/swap_ema_weights.py::SwapEMAWeights.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/callbacks/swap_ema_weights.py
- rank=20 layer=FUNCTION tokens=97 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/trainer_test.py::StepObserver.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/trainer_test.py
- rank=21 layer=FUNCTION tokens=54 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/function.py::Function.operations file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/function.py
- rank=22 layer=FUNCTION tokens=57 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/preprocessing/image.py::Iterator.reset file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/preprocessing/image.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib_test.py::SavingTest.setUp [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib_test.py]
    def setUp(self):
        super().setUp()
        # Set `_MEMORY_UPPER_BOUND` to zero for testing purpose.
        self.original_value = saving_lib._MEMORY_UPPER_BOUND
        saving_lib._MEMORY_UPPER_BOUND = 0

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/function.py::Function._setup_nnx_op_mapping [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/function.py]
    def _setup_nnx_op_mapping(self):
        """Setup operation mapping for NNX"""
        # Create a mapping from operation id to operation instance
        self._nnx_op_mapping = {}

        # Assign the list of operations to a single attribute for NNX traversal
        self.nnx_operations = self._operations[:]
        for operation in self._operations:
            # Map the operation id to this operation instance
            self._nnx_op_mapping[id(operation)] = operation

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/epoch_iterator.py::EpochIterator.reset [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/epoch_iterator.py]
    def reset(self):
        self._current_iterator = None
        self._num_batches = self.data_adapter.num_batches
        self._steps_seen = 0
        self._epoch_iterator = None
        self.data_adapter.on_epoch_end()

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer_test.py::TrainingLayer.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer_test.py]
            def __init__(self):
                super().__init__()
                self.post_build_modify_layer = PostBuildModifyLayer()

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/config.py::Config.update [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/config.py]
    def update(self, *args, **kwargs):
        self._raise_if_frozen()
        return self._config.update(*args, **kwargs)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/core.py::scatter_update [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/core.py]
def scatter_update(inputs, indices, updates, reduction=None):
    inputs = get_ov_output(inputs)
    indices = get_ov_output(indices)
    updates = get_ov_output(updates)

    inputs, updates = align_operand_types(inputs, updates, "scatter_update")

    # Map Keras reduction to OpenVINO ScatterNDUpdate reduction.
    # OpenVINO Opset 15 supports: "none", "sum", "sub", "prod", "min", "max".
    if reduction is None:
        ov_reduction = "none"
    elif reduction == "add":
        ov_reduction = "sum"
    elif reduction == "mul":
        ov_reduction = "prod"
    elif reduction in ("max", "min"):
        ov_reduction = reduction
    else:
        raise ValueError(f"Unsupported reduction: {reduction}")

    result = ov_opset.scatter_nd_update(
        inputs, indices, updates, reduction=ov_reduction
    ).output(0)
    return OpenVINOKerasTensor(result)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/nn.py::_adjust_kernel [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/nn.py]
def _adjust_kernel(kernel, num_spatial_dims):
    if num_spatial_dims == 1:
        permutation = [2, 1, 0]
    elif num_spatial_dims == 2:
        permutation = [3, 2, 0, 1]
    else:
        permutation = [4, 3, 0, 1, 2]
    permutation = ov_opset.constant(permutation, Type.i32)
    return ov_opset.transpose(kernel, permutation).output(0)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/numpy.py::use_custom_ops [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/numpy.py]
    def use_custom_ops(subscripts, *operands, output_type):
        # Replace tf.einsum with custom ops to utilize hardware-accelerated
        # matmul
        x, y = operands[0], operands[1]
        if subscripts == "a,b->ab":
            x = tf.expand_dims(x, axis=-1)
            y = tf.expand_dims(y, axis=0)
            return tf.matmul(x, y, output_type=output_type)
        elif subscripts == "ab,b->a":
            y = tf.expand_dims(y, axis=-1)
            result = tf.matmul(x, y, output_type=output_type)
            return tf.squeeze(result, axis=-1)
        elif subscripts == "ab,bc->ac":
            return tf.matmul(x, y, output_type=output_type)
        elif subscripts == "ab,cb->ac":
            y = tf.transpose(y, [1, 0])
            return tf.matmul(x, y, output_type=output_type)
        elif subscripts == "abc,cd->abd":
            return tf.matmul(x, y, output_type=output_type)
        elif subscripts == "abc,cde->abde":
            _, b1, c1 = x.shape
            c2, d2, e2 = y.shape
            b, c, d, e = b1, c1 or c2, d2, e2
            y = tf.reshape(y, [c, -1])
            result = tf.matmul(x, y, output_type=output_type)
            return tf.reshape(result, [-1, b, d, e])
        elif subscripts == "abc,dc->abd":
            y = tf.transpose(y, [1, 0])
            return tf.matmul(x, y, output_type=output_type)
        elif subscripts == "abc,dce->abde":
            _, b1, c1 = x.shape
            d2, c2, e2 = y.shape
            b, c, d, e = b1, c1 or c2, d2, e2
            y = tf.transpose(y, [1, 0, 2])  # cde
            y = tf.reshape(y, [c, -1])
            result = tf.matmul(x, y, output_type=output_type)
            return tf.reshape(result, [-1, b, d, e])
        elif subscripts == "abc,dec->abde":
            _, b1, c1 = x.shape
            d2, e2, c2 = y.shape
            b, c, d, e = b1, c1 or c2, d2, e2
            y = tf.transpose(y, [2, 0, 1])  # cde
            y = tf.reshape(y, [c, -1])
            result = tf.matmul(x, y, output_type=output_type)
            return tf.reshape(result, [-1, b, d, e])
        elif subscripts == "abcd,abde->abce":
            return tf.matmul(x, y, output_type=output_type)
        elif subscripts == "abcd,abed->abce":
            y = tf.transpose(y, [0, 1, 3, 2])
            return tf.matmul(x, y, output_type=output_type)
        elif subscripts == "abcd,acbe->adbe":
            x = tf.transpose(x, [0, 1, 3, 2])
            y = tf.transpose(y, [0, 2, 1, 3])
            result = tf.matmul(x, y, output_type=output_type)
            return tf.transpose(result, [0, 2, 1, 3])
        elif subscripts == "abcd,adbe->acbe":
            y = tf.transpose(y, [0, 2, 1, 3])  # abde
            result = tf.matmul(x, y, output_type=output_type)  # abce
            return tf.transpose(result, [0, 2, 1, 3])
        elif subscripts == "abcd,aecd->acbe":
            x = tf.transpose(x, [0, 2, 1, 3])  # acbd
            y = tf.transpose(y, [0, 2, 3, 1])  # acde
            return tf.matmul(x, y, output_type=output_type)
        elif subscripts == "abcd,aecd->aceb":
            x = tf.transpose(x, [0, 2, 1, 3])
            y = tf.transpose(y, [0, 2, 3, 1])
            result = tf.matmul(x, y, output_type=output_type)  # acbe
            return tf.transpose(result, [0, 1, 3, 2])
        elif subscripts == "abcd,cde->abe":
            _, b1, c1, d1 = x.shape
            c2, d2, e2 = y.shape
            b, c, d, e = b1, c1 or c2, d1 or d2, e2
            x = tf.reshape(x, [-1, b, c * d])
            y = tf.reshape(y, [-1, e])
            return tf.matmul(x, y, output_type=output_type)
        elif subscripts == "abcd,ced->abe":
            _, b1, c1, d1 = x.shape
            c2, e2, d2 = y.shape
            b, c, d, e = b1, c1 or c2, d1 or d2, e2
            x = tf.reshape(x, [-1, b, c * d])
            y = tf.transpose(y, [0, 2, 1])
            y = tf.reshape(y, [-1, e])
            return tf.matmul(x, y, output_type=output_type)
        elif subscripts == "abcd,ecd->abe":
            _, b1, c1, d1 = x.shape
            e2, c2, d2 = y.shape
            b, c, d, e = b1, c1 or c2, d1 or d2, e2
            x = tf.reshape(x, [-1, b, c * d])
            y = tf.transpose(y, [1, 2, 0])
            y = tf.reshape(y, [-1, e])
            return tf.matmul(x, y, output_type=output_type)
        elif subscripts == "abcde,aebf->adbcf":
            _, b1, c1, d1, e1 = x.shape
            _, e2, b2, f2 = y.shape
            b, c, d, e, f = b1 or b2, c1, d1, e1 or e2, f2
            x = tf.reshape(x, [-1, b, c * d, e])  # ab(cd)e
            y = tf.transpose(y, [0, 2, 1, 3])  # abef
            result = tf.matmul(x, y, output_type=output_type)  # ab(cd)f
            result = tf.reshape(result, [-1, b, c, d, f])  # abcdf
            return tf.transpose(result, [0, 3, 1, 2, 4])
        elif subscripts == "abcde,afce->acdbf":
            _, b1, c1, d1, e1 = x.shape
            _, f2, c2, e2 = y.shape
            b, c, d, e, f = b1, c1 or c2, d1, e1 or e2, f2
            x = tf.transpose(x, [0, 2, 3, 1, 4])  # acdbe
            x = tf.reshape(x, [-1, c, d * b, e])  # ac(db)e
            y = tf.transpose(y, [0, 2, 3, 1])  # acef
            result = tf.matmul(x, y, output_type=output_type)  # ac(db)f
            return tf.reshape(result, [-1, c, d, b, f])
        else:
            raise NotImplementedError

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/keras_tensor.py::KerasTensor.__mod__ [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/keras_tensor.py]
    def __mod__(self, other):
        from keras.src import ops

        return ops.Mod().symbolic_call(self, other)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/f_score_metrics.py::FBetaScore.reset_state [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/f_score_metrics.py]
    def reset_state(self):
        for v in self.variables:
            v.assign(ops.zeros(v.shape, dtype=v.dtype))

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/regression_metrics.py::R2Score.reset_state [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/regression_metrics.py]
    def reset_state(self):
        for v in self.variables:
            v.assign(ops.zeros(v.shape, dtype=v.dtype))

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/iou_metrics.py::_IoUBase.reset_state [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/iou_metrics.py]
    def reset_state(self):
        self.total_cm.assign(
            ops.zeros(self.total_cm.shape, dtype=self.total_cm.dtype)
        )

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/export/saved_model_test.py::ExportArchiveTest.setUp [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/export/saved_model_test.py]
    def setUp(self):
        super().setUp()
        self.add_endpoint_kwargs = {}
        if testing.jax_uses_gpu():
            self.add_endpoint_kwargs = {
                "jax2tf_kwargs": {
                    "native_serialization_platforms": ("cpu", "cuda")
                }
            }
        elif testing.jax_uses_tpu():
            self.add_endpoint_kwargs = {
                "jax2tf_kwargs": {
                    "native_serialization_platforms": ("cpu", "tpu")
                }
            }

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/image.py::fix_index [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/image.py]
    def fix_index(index, size_node):
        if fill_mode in ("constant", "nearest"):
            zero = ov_opset.constant(0, dtype=Type.i32).output(0)
            size_m1 = ov_opset.subtract(
                size_node, ov_opset.constant(1, dtype=Type.i32)
            ).output(0)
            return ov_opset.minimum(
                ov_opset.maximum(index, zero), size_m1
            ).output(0)
        elif fill_mode == "wrap":
            return ov_opset.floor_mod(index, size_node).output(0)
        elif fill_mode == "mirror":
            return _mirror_index_fixer(index, size_node)
        else:  # reflect
            return _reflect_index_fixer(index, size_node)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/attention/grouped_query_attention_test.py::GroupedQueryAttentionTest.setUp [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/attention/grouped_query_attention_test.py]
    def setUp(self):
        super().setUp()
        # Flash attention is a newly introduced feature. We need to disable it
        # for testing purposes.
        disable_flash_attention()

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/attention/multi_head_attention_test.py::MultiHeadAttentionTest.setUp [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/attention/multi_head_attention_test.py]
    def setUp(self):
        super().setUp()
        # Flash attention is a newly introduced feature. We need to disable it
        # for testing purposes.
        disable_flash_attention()

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/node.py::Node.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/node.py]
    def __init__(
        self, operation, call_args=None, call_kwargs=None, outputs=None
    ):
        self.operation = operation
        self.arguments = SymbolicArguments(*call_args, **call_kwargs)
        self.outputs = [] if outputs is None else tree.flatten(outputs)
        for x in self.outputs:
            if not isinstance(x, KerasTensor):
                raise ValueError(
                    "All operation outputs must be tensors. "
                    f"Operation {operation} returned a non-tensor. "
                    f"Non-tensor received: {x}"
                )

        zero_history = any(
            not x.record_history for x in self.arguments.keras_tensors
        )

        # If inputs don't have metadata yet, add it.
        if not zero_history:
            for tensor in self.arguments.keras_tensors:
                if not hasattr(tensor, "_keras_history"):
                    tensor._keras_history = KerasHistory(
                        operation=None, node_index=0, tensor_index=0
                    )

        # Wire up Node to Operations.
        self.operation._inbound_nodes.append(self)
        for kt in self.arguments.keras_tensors:
            inbound_op = kt._keras_history.operation
            if inbound_op is not None:  # It's a graph entry point.
                inbound_op._outbound_nodes.append(self)

        # Set metadata on outputs.
        if not zero_history:
            node_index = len(self.operation._inbound_nodes) - 1
            for i, tensor in enumerate(self.outputs):
                tensor._keras_history = KerasHistory(
                    operation=operation, node_index=node_index, tensor_index=i
                )

        # Whether this is a root node.
        self.is_input = not self.arguments.keras_tensors

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/core.py::SliceUpdate.call [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/core.py]
    def call(self, inputs, start_indices, updates):
        return backend.core.slice_update(inputs, start_indices, updates)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/callbacks/swap_ema_weights.py::SwapEMAWeights.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/callbacks/swap_ema_weights.py]
    def __init__(self, swap_on_epoch=False):
        super().__init__()
        self.swap_on_epoch = swap_on_epoch

        self._ema_weights_in_model = False

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/trainer_test.py::StepObserver.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/trainer_test.py]
    def __init__(self):
        super().__init__()
        self.begin_count = 0
        self.end_count = 0
        self.epoch_begin_count = 0
        self.epoch_end_count = 0
        self.batch_loss_history = []

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/function.py::Function.operations [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/function.py]
    def operations(self):
        return self._operations[:]

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/preprocessing/image.py::Iterator.reset [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/preprocessing/image.py]
    def reset(self):
        self.batch_index = 0
```
