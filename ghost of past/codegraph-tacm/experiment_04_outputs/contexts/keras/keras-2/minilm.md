# keras-2 :: minilm

query: Fix in_top_k tests to include CNTK [Test fails] (#12336)

## selected nodes

- rank=1 layer=FUNCTION tokens=132 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/math.py::top_k file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/math.py
- rank=2 layer=FUNCTION tokens=68 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/backend.py::in_top_k file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/backend.py
- rank=3 layer=FUNCTION tokens=60 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/math.py::top_k file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/math.py
- rank=4 layer=FUNCTION tokens=203 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/random_rotation_benchmark.py::main file=/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/random_rotation_benchmark.py
- rank=5 layer=FUNCTION tokens=205 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/conv_benchmark.py::main file=/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/conv_benchmark.py
- rank=6 layer=FUNCTION tokens=64 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/math.py::in_top_k file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/math.py
- rank=7 layer=FUNCTION tokens=88 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/trainer_test.py::CustomCallback.on_test_end file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/trainer_test.py
- rank=8 layer=FUNCTION tokens=461 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/attention/grouped_query_attention.py::GroupedQueryAttention.call file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/attention/grouped_query_attention.py
- rank=9 layer=FUNCTION tokens=64 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/torch/math.py::top_k file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/torch/math.py
- rank=10 layer=FUNCTION tokens=92 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/trainer_test.py::CustomCallback.on_test_batch_end file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/trainer_test.py
- rank=11 layer=FUNCTION tokens=205 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/attention_benchmark.py::benchmark_multi_head_attention file=/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/attention_benchmark.py
- rank=12 layer=FUNCTION tokens=211 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/normalization_benchmark.py::main file=/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/normalization_benchmark.py
- rank=13 layer=FUNCTION tokens=212 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/regularization_benchmark.py::main file=/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/regularization_benchmark.py
- rank=14 layer=FUNCTION tokens=209 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/attention_benchmark.py::main file=/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/attention_benchmark.py
- rank=15 layer=FUNCTION tokens=207 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/merge_benchmark.py::main file=/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/merge_benchmark.py
- rank=16 layer=FUNCTION tokens=206 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/rnn_benchmark.py::main file=/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/rnn_benchmark.py
- rank=17 layer=FUNCTION tokens=208 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/pooling_benchmark.py::main file=/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/pooling_benchmark.py
- rank=18 layer=FUNCTION tokens=207 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/core_benchmark.py::main file=/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/core_benchmark.py
- rank=19 layer=FUNCTION tokens=209 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/reshaping_benchmark.py::main file=/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/reshaping_benchmark.py
- rank=20 layer=FUNCTION tokens=210 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/activation_benchmark.py::main file=/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/activation_benchmark.py
- rank=21 layer=FUNCTION tokens=220 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/attention/attention.py::Attention.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/attention/attention.py
- rank=22 layer=FUNCTION tokens=103 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/math.py::in_top_k file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/math.py
- rank=23 layer=FUNCTION tokens=86 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/trainer_test.py::CustomCallback.on_test_batch_begin file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/trainer_test.py
- rank=24 layer=FUNCTION tokens=54 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math.py::TopK.call file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/math.py::top_k [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/math.py]
def top_k(x, k, sorted=True):
    x = get_ov_output(x)
    k_tensor = ov_opset.constant(k, dtype=Type.i32)
    axis = -1
    sort_type = "value" if sorted else "none"
    topk_node = ov_opset.topk(x, k_tensor, axis, "max", sort_type)
    values = topk_node.output(0)
    indices = topk_node.output(1)
    return OpenVINOKerasTensor(values), OpenVINOKerasTensor(indices)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/backend.py::in_top_k [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/backend.py]
def in_top_k(predictions, targets, k):
    """DEPRECATED."""
    return tf.compat.v1.math.in_top_k(predictions, targets, k)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/math.py::top_k [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/math.py]
def top_k(x, k, sorted=True):
    return tf.math.top_k(x, k, sorted=sorted)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/random_rotation_benchmark.py::main [/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/random_rotation_benchmark.py]
def main(_):
    benchmark_name = FLAGS.benchmark_name
    num_samples = FLAGS.num_samples
    batch_size = FLAGS.batch_size
    jit_compile = FLAGS.jit_compile

    if benchmark_name is None:
        for benchmark_fn in BENCHMARK_NAMES.values():
            benchmark_fn(num_samples, batch_size, jit_compile)
        return

    if benchmark_name not in BENCHMARK_NAMES:
        raise ValueError(
            f"Invalid benchmark name: {benchmark_name}, "
            f"`benchmark_name` must be one of {BENCHMARK_NAMES.keys()}"
        )

    BENCHMARK_NAMES[benchmark_name](num_samples, batch_size, jit_compile)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/conv_benchmark.py::main [/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/conv_benchmark.py]
def main(_):
    benchmark_name = FLAGS.benchmark_name
    num_samples = FLAGS.num_samples
    batch_size = FLAGS.batch_size
    jit_compile = FLAGS.jit_compile

    if benchmark_name is None:
        for name, benchmark_fn in BENCHMARK_NAMES:
            benchmark_fn(num_samples, batch_size, jit_compile)
        return

    if benchmark_name not in BENCHMARK_NAMES:
        raise ValueError(
            f"Invalid benchmark name: {benchmark_name}, `benchmark_name` must "
            f"be one of {BENCHMARK_NAMES.keys()}"
        )
    benchmark_fn = BENCHMARK_NAMES[benchmark_name]
    benchmark_fn(num_samples, batch_size, jit_compile)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/math.py::in_top_k [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/math.py]
def in_top_k(targets, predictions, k):
    return tf.math.in_top_k(targets, predictions, k)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/trainer_test.py::CustomCallback.on_test_end [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/trainer_test.py]
            def on_test_end(self, logs=None):
                keys = sorted(list(logs.keys()))
                test_obj.assertEqual(keys, ["loss", "mean_absolute_error"])

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/attention/grouped_query_attention.py::GroupedQueryAttention.call [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/attention/grouped_query_attention.py]
    def call(
        self,
        query,
        value,
        key=None,
        query_mask=None,
        value_mask=None,
        key_mask=None,
        attention_mask=None,
        return_attention_scores=False,
        training=None,
        use_causal_mask=False,
    ):
        self._return_attention_scores = return_attention_scores
        if key is None:
            key = value

        attention_mask = self._compute_attention_mask(
            query,
            value,
            query_mask=query_mask,
            value_mask=value_mask,
            key_mask=key_mask,
            attention_mask=attention_mask,
            use_causal_mask=use_causal_mask,
        )
        if self.use_gate:
            gate = self._gate_dense(query)
        query = self._query_dense(query)
        key = self._key_dense(key)
        value = self._value_dense(value)

        key = ops.repeat(
            key, self.num_repeats, axis=2
        )  # (batch_dim, source_seq_len, query_heads, head_dim)
        value = ops.repeat(
            value, self.num_repeats, axis=2
        )  # (batch_dim, source_seq_len, query_heads, head_dim)

        output, scores = self._compute_attention(
            query,
            key,
            value,
            attention_mask=attention_mask,
            training=training,
        )
        # (batch_dim, target_seq_len, feature_dim)
        if self.use_gate:
            output = self._output_dense(ops.multiply(output, gate))
        else:
            output = self._output_dense(output)

        if return_attention_scores:
            return output, scores
        return output

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/torch/math.py::top_k [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/torch/math.py]
def top_k(x, k, sorted=True):
    x = convert_to_tensor(x)
    return torch.topk(x, k, sorted=sorted)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/trainer_test.py::CustomCallback.on_test_batch_end [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/trainer_test.py]
            def on_test_batch_end(self, batch, logs=None):
                keys = sorted(list(logs.keys()))
                test_obj.assertEqual(keys, ["loss", "mean_absolute_error"])

# /Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/attention_benchmark.py::benchmark_multi_head_attention [/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/attention_benchmark.py]
def benchmark_multi_head_attention(
    num_samples,
    batch_size,
    jit_compile=True,
):
    layer_name = "MultiHeadAttention"
    init_args = {
        "num_heads": 4,
        "key_dim": 16,
    }
    benchmark = LayerBenchmark(
        layer_name,
        init_args,
        input_shape=[[256, 64], [256, 64], [256, 64]],
        flat_call_inputs=True,
        jit_compile=jit_compile,
    )

    benchmark.benchmark_predict(
        num_samples=num_samples,
        batch_size=batch_size,
    )

    benchmark.benchmark_train(
        num_samples=num_samples,
        batch_size=batch_size,
    )

# /Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/normalization_benchmark.py::main [/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/normalization_benchmark.py]
def main(_):
    benchmark_name = FLAGS.benchmark_name
    num_samples = FLAGS.num_samples
    batch_size = FLAGS.batch_size
    jit_compile = FLAGS.jit_compile

    if benchmark_name is None:
        for name, benchmark_fn in BENCHMARK_NAMES.items():
            benchmark_fn(num_samples, batch_size, jit_compile)
        return

    if benchmark_name not in BENCHMARK_NAMES:
        raise ValueError(
            f"Invalid benchmark name: {benchmark_name}, `benchmark_name` must "
            f"be one of {BENCHMARK_NAMES.keys()}"
        )
    benchmark_fn = BENCHMARK_NAMES[benchmark_name]
    benchmark_fn(num_samples, batch_size, jit_compile)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/regularization_benchmark.py::main [/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/regularization_benchmark.py]
def main(_):
    benchmark_name = FLAGS.benchmark_name
    num_samples = FLAGS.num_samples
    batch_size = FLAGS.batch_size
    jit_compile = FLAGS.jit_compile

    if benchmark_name is None:
        for name, benchmark_fn in BENCHMARK_NAMES.items():
            benchmark_fn(num_samples, batch_size, jit_compile)
        return

    if benchmark_name not in BENCHMARK_NAMES:
        raise ValueError(
            f"Invalid benchmark name: {benchmark_name}, `benchmark_name` must "
            f"be one of {BENCHMARK_NAMES.keys()}"
        )
    benchmark_fn = BENCHMARK_NAMES[benchmark_name]
    benchmark_fn(num_samples, batch_size, jit_compile)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/attention_benchmark.py::main [/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/attention_benchmark.py]
def main(_):
    benchmark_name = FLAGS.benchmark_name
    num_samples = FLAGS.num_samples
    batch_size = FLAGS.batch_size
    jit_compile = FLAGS.jit_compile

    if benchmark_name is None:
        for name, benchmark_fn in BENCHMARK_NAMES.items():
            benchmark_fn(num_samples, batch_size, jit_compile)
        return

    if benchmark_name not in BENCHMARK_NAMES:
        raise ValueError(
            f"Invalid benchmark name: {benchmark_name}, `benchmark_name` must "
            f"be one of {BENCHMARK_NAMES.keys()}"
        )
    benchmark_fn = BENCHMARK_NAMES[benchmark_name]
    benchmark_fn(num_samples, batch_size, jit_compile)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/merge_benchmark.py::main [/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/merge_benchmark.py]
def main(_):
    benchmark_name = FLAGS.benchmark_name
    num_samples = FLAGS.num_samples
    batch_size = FLAGS.batch_size
    jit_compile = FLAGS.jit_compile

    if benchmark_name is None:
        for name, benchmark_fn in BENCHMARK_NAMES.items():
            benchmark_fn(num_samples, batch_size, jit_compile)
        return

    if benchmark_name not in BENCHMARK_NAMES:
        raise ValueError(
            f"Invalid benchmark name: {benchmark_name}, `benchmark_name` must "
            f"be one of {BENCHMARK_NAMES.keys()}"
        )
    benchmark_fn = BENCHMARK_NAMES[benchmark_name]
    benchmark_fn(num_samples, batch_size, jit_compile)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/rnn_benchmark.py::main [/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/rnn_benchmark.py]
def main(_):
    benchmark_name = FLAGS.benchmark_name
    num_samples = FLAGS.num_samples
    batch_size = FLAGS.batch_size
    jit_compile = FLAGS.jit_compile

    if benchmark_name is None:
        for name, benchmark_fn in BENCHMARK_NAMES.items():
            benchmark_fn(num_samples, batch_size, jit_compile)
        return

    if benchmark_name not in BENCHMARK_NAMES:
        raise ValueError(
            f"Invalid benchmark name: {benchmark_name}, `benchmark_name` must "
            f"be one of {BENCHMARK_NAMES.keys()}"
        )
    benchmark_fn = BENCHMARK_NAMES[benchmark_name]
    benchmark_fn(num_samples, batch_size, jit_compile)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/pooling_benchmark.py::main [/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/pooling_benchmark.py]
def main(_):
    benchmark_name = FLAGS.benchmark_name
    num_samples = FLAGS.num_samples
    batch_size = FLAGS.batch_size
    jit_compile = FLAGS.jit_compile

    if benchmark_name is None:
        for name, benchmark_fn in BENCHMARK_NAMES.items():
            benchmark_fn(num_samples, batch_size, jit_compile)
        return

    if benchmark_name not in BENCHMARK_NAMES:
        raise ValueError(
            f"Invalid benchmark name: {benchmark_name}, `benchmark_name` must "
            f"be one of {BENCHMARK_NAMES.keys()}"
        )
    benchmark_fn = BENCHMARK_NAMES[benchmark_name]
    benchmark_fn(num_samples, batch_size, jit_compile)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/core_benchmark.py::main [/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/core_benchmark.py]
def main(_):
    benchmark_name = FLAGS.benchmark_name
    num_samples = FLAGS.num_samples
    batch_size = FLAGS.batch_size
    jit_compile = FLAGS.jit_compile

    if benchmark_name is None:
        for name, benchmark_fn in BENCHMARK_NAMES.items():
            benchmark_fn(num_samples, batch_size, jit_compile)
        return

    if benchmark_name not in BENCHMARK_NAMES:
        raise ValueError(
            f"Invalid benchmark name: {benchmark_name}, `benchmark_name` must "
            f"be one of {BENCHMARK_NAMES.keys()}"
        )
    benchmark_fn = BENCHMARK_NAMES[benchmark_name]
    benchmark_fn(num_samples, batch_size, jit_compile)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/reshaping_benchmark.py::main [/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/reshaping_benchmark.py]
def main(_):
    benchmark_name = FLAGS.benchmark_name
    num_samples = FLAGS.num_samples
    batch_size = FLAGS.batch_size
    jit_compile = FLAGS.jit_compile

    if benchmark_name is None:
        for name, benchmark_fn in BENCHMARK_NAMES.items():
            benchmark_fn(num_samples, batch_size, jit_compile)
        return

    if benchmark_name not in BENCHMARK_NAMES:
        raise ValueError(
            f"Invalid benchmark name: {benchmark_name}, `benchmark_name` must "
            f"be one of {BENCHMARK_NAMES.keys()}"
        )
    benchmark_fn = BENCHMARK_NAMES[benchmark_name]
    benchmark_fn(num_samples, batch_size, jit_compile)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/activation_benchmark.py::main [/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/activation_benchmark.py]
def main(_):
    benchmark_name = FLAGS.benchmark_name
    num_samples = FLAGS.num_samples
    batch_size = FLAGS.batch_size
    jit_compile = FLAGS.jit_compile

    if benchmark_name is None:
        for name, benchmark_fn in BENCHMARK_NAMES.items():
            benchmark_fn(num_samples, batch_size, jit_compile)
        return

    if benchmark_name not in BENCHMARK_NAMES:
        raise ValueError(
            f"Invalid benchmark name: {benchmark_name}, `benchmark_name` must "
            f"be one of {BENCHMARK_NAMES.keys()}"
        )
    benchmark_fn = BENCHMARK_NAMES[benchmark_name]
    benchmark_fn(num_samples, batch_size, jit_compile)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/attention/attention.py::Attention.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/attention/attention.py]
    def __init__(
        self,
        use_scale=False,
        score_mode="dot",
        dropout=0.0,
        seed=None,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.use_scale = use_scale
        self.score_mode = score_mode
        self.dropout = dropout
        if self.dropout > 0:
            self.seed_generator = backend.random.SeedGenerator(seed=seed)

        if self.score_mode not in ["dot", "concat"]:
            raise ValueError(
                "Invalid value for argument score_mode. "
                "Expected one of {'dot', 'concat'}. "
                f"Received: score_mode={score_mode}"
            )

        self._return_attention_scores = False

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/math.py::in_top_k [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/math.py]
def in_top_k(targets, predictions, k):
    targets = targets[:, None]
    topk_values = top_k(predictions, k)[0]
    targets_values = np.take_along_axis(predictions, targets, axis=-1)
    mask = targets_values >= topk_values
    return np.any(mask, axis=-1)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/trainer_test.py::CustomCallback.on_test_batch_begin [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/trainer_test.py]
            def on_test_batch_begin(self, batch, logs=None):
                keys = sorted(list(logs.keys()))
                test_obj.assertEqual(keys, [])

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math.py::TopK.call [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math.py]
    def call(self, x):
        return backend.math.top_k(x, self.k, self.sorted)
```
