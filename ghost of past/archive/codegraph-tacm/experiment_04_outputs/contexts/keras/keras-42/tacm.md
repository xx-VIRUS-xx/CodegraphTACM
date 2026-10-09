# keras-42 :: tacm

query: Allow custom steps_per_epoch for sequences, default to len(generator) if unspecified (#8509)

## selected nodes

- rank=1 layer=FILE tokens=92 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/config.py file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/config.py
- rank=2 layer=FILE tokens=33 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/random/seed_generator.py file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/random/seed_generator.py
- rank=3 layer=FILE tokens=64 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/python_utils.py file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/python_utils.py
- rank=4 layer=FILE tokens=10 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/__init__.py file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/__init__.py
- rank=5 layer=CLASS tokens=639 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/trainer_test.py::TestTrainer file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/trainer_test.py
- rank=6 layer=CLASS tokens=73 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/preprocessing/text.py::Tokenizer file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/preprocessing/text.py
- rank=7 layer=CLASS tokens=29 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/random/seed_generator.py::SeedGenerator file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/random/seed_generator.py
- rank=8 layer=CLASS tokens=47 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/sequence_utils_test.py::PadSequencesTest file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/sequence_utils_test.py
- rank=9 layer=CLASS tokens=12 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/node.py::KerasHistory file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/node.py
- rank=10 layer=FUNCTION tokens=155 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/config.py::set_max_steps_per_epoch file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/config.py
- rank=11 layer=FUNCTION tokens=107 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/config.py::max_steps_per_epoch file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/config.py
- rank=12 layer=FUNCTION tokens=71 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/data_adapters/__init__.py::get_data_adapter file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/data_adapters/__init__.py
- rank=13 layer=FUNCTION tokens=297 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/epoch_iterator.py::EpochIterator.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/epoch_iterator.py
- rank=14 layer=FUNCTION tokens=27 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/preprocessing/text.py::Tokenizer.sequences_to_texts file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/preprocessing/text.py
- rank=15 layer=FUNCTION tokens=355 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/epoch_iterator.py::EpochIterator._enumerate_iterator file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/epoch_iterator.py
- rank=16 layer=FUNCTION tokens=25 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/preprocessing/text.py::Tokenizer.texts_to_sequences file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/preprocessing/text.py
- rank=17 layer=FUNCTION tokens=185 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/preprocessing/text.py::Tokenizer.sequences_to_texts_generator file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/preprocessing/text.py
- rank=18 layer=FUNCTION tokens=277 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/callbacks/tensorboard.py::TensorBoard._log_epoch_metrics file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/callbacks/tensorboard.py
- rank=19 layer=FUNCTION tokens=52 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/preprocessing/text.py::Tokenizer.fit_on_sequences file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/preprocessing/text.py
- rank=20 layer=FUNCTION tokens=132 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/callbacks/tensorboard.py::TensorBoard._compute_steps_per_second file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/callbacks/tensorboard.py
- rank=21 layer=FUNCTION tokens=102 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/trainer.py::JAXTrainer.predict file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/trainer.py
- rank=22 layer=FUNCTION tokens=110 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/preprocessing/text.py::Tokenizer.sequences_to_matrix file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/preprocessing/text.py
- rank=23 layer=FUNCTION tokens=103 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/torch/trainer.py::TorchTrainer.predict file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/torch/trainer.py
- rank=24 layer=FUNCTION tokens=116 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/trainer.py::TensorFlowTrainer.predict file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/trainer.py
- rank=25 layer=FUNCTION tokens=101 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/trainer.py::OpenVINOTrainer.predict file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/trainer.py
- rank=26 layer=FUNCTION tokens=101 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/trainer.py::NumpyTrainer.predict file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/trainer.py
- rank=27 layer=FUNCTION tokens=329 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/preprocessing/text.py::Tokenizer.texts_to_sequences_generator file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/preprocessing/text.py
- rank=28 layer=FUNCTION tokens=81 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/callbacks/tensorboard.py::TensorBoard.on_epoch_begin file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/callbacks/tensorboard.py
- rank=29 layer=FUNCTION tokens=57 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/epoch_iterator.py::EpochIterator.num_batches file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/epoch_iterator.py
- rank=30 layer=FUNCTION tokens=41 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/preprocessing/text.py::Tokenizer.texts_to_matrix file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/preprocessing/text.py
- rank=31 layer=FUNCTION tokens=85 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/operation.py::Operation.output file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/operation.py
- rank=32 layer=FUNCTION tokens=14 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/functional.py::Functional.output file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/functional.py
- rank=33 layer=FUNCTION tokens=69 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/config.py::floatx file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/config.py
- rank=34 layer=FUNCTION tokens=8 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/serialization_lib_test.py::custom_fn file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/serialization_lib_test.py

## context

```text
file backend/config.py
imports: json, os, keras
defines: floatx, set_floatx, epsilon, set_epsilon, image_data_format, set_image_data_format, enable_flash_attention, disable_flash_attention, is_flash_attention_enabled, is_nnx_enabled, set_nnx_enabled, standardize_data_format, keras_home, backend, set_max_epochs, set_max_steps_per_epoch, max_epochs, max_steps_per_epoch

file random/seed_generator.py
imports: random, numpy, keras
defines: SeedGenerator, global_seed_generator, make_default_seed, draw_seed

file utils/python_utils.py
imports: binascii, codecs, marshal, os, types
defines: is_continuous_axis, default, is_default, func_dump, func_load, ensure_value_to_cell, dummy_fn, to_list, remove_long_seq, removeprefix, removesuffix, remove_by_id, pythonify_logs

file __init__.py
imports: keras
defines: —

class TestTrainer(testing.TestCase):  [trainers/trainer_test.py:350]
methods: data_generator, data_generator, gen_i, gen_i
         generate_batches, generate_uneven_batches
         get_functional, get_layer, get_model
         infinite_gen, infinite_gen, loss_fn, metrics_one
         metrics_zero, mock_optimizer_assign
         test_adds_loss_scaling_optimizer
         test_callback_methods_keys
         test_callbacks_can_update_state_at_batch_boundary
         test_compile_eager_vs_jit_torch
         test_compute_loss_no_training_backwards_compatibility
         test_constraints_are_applied, test_evaluate_flow
         test_evaluate_return_list_respect_metrics_order
         test_evaluate_sparse
         test_evaluate_with_custom_compute_loss
         test_evaluate_with_custom_test_step
         test_evaluate_with_different_batch_size_same_loss
         test_fit_eval_flow_for_jax_model_weights
         test_fit_flow, test_fit_sparse
         test_fit_with_custom_train_step
         test_fit_with_data_adapter
         test_fit_with_different_batch_size_same_loss
         test_fit_with_val_split
         test_for_eval_epoch_iterator
         test_fwd_pass_loss_presence_in_compute_loss
         test_internal_only_loss
         test_jit_compile_with_tf_determinism
         test_loss_scaling_prevents_underflow
         test_loss_weights, test_max_epochs_and_steps
         test_metric_tracking
         test_metric_update_in_compute_loss
         test_multiple_compiles, test_nested_input_predict
         test_nested_inputs, test_nested_trainer_metrics
         test_nested_trainer_metrics_without_compile
         test_on_batch_methods
         test_on_batch_methods_without_training
         test_partial_loss_partial_label
         test_predict_dropout, test_predict_flow
         test_predict_flow_struct, test_predict_generator
         test_predict_preserve_order, test_predict_sparse
         test_recompile, test_retracing
         test_retracing_predict
         test_rng_updated_during_predict
         test_steps_per_epoch
         test_steps_per_execution_steps_count
         test_steps_per_execution_steps_count_unknown_dataset_size
         test_steps_per_execution_steps_count_without_training
         test_steps_per_execution_steps_per_epoch
         test_steps_per_execution_steps_per_epoch_unknown_data_size
         test_steps_per_execution_unrolled_steps_steps_count
         test_stop_loop, test_symbolic_build
         test_trainer_with_raggeds, test_training_arg
         test_validation_data_infinite_generator

class Tokenizer:  [legacy/preprocessing/text.py:82]
methods: fit_on_sequences, fit_on_texts, get_config
         sequences_to_matrix, sequences_to_texts
         sequences_to_texts_generator, texts_to_matrix
         texts_to_sequences, texts_to_sequences_generator
         to_json, __init__

class SeedGenerator:  [random/seed_generator.py:15]
methods: from_config, get_config, next, seed_initializer, __init__

class PadSequencesTest(testing.TestCase):  [utils/sequence_utils_test.py:5]
methods: test_pad_sequences, test_pad_sequences_float
         test_pad_sequences_str, test_pad_sequences_vector

class KerasHistory(  [ops/node.py:111]
methods: —

def set_max_steps_per_epoch(max_steps_per_epoch):
    """Limit the maximum number of steps for any call to fit/evaluate/predict.

    This will cap the number of steps for single epoch of a call to `fit()`,
    `evaluate()`, or `predict()`. This is purely for debugging, and can also be
    set via the `KERAS_MAX_STEPS_PER_EPOCH` environment variable to quickly run
    a scrip without modifying its source.

    Args:
        max_epochs: The integer limit on the number of epochs or `None`. If
            `None`, no limit is applied.
    """
    global _MAX_STEPS_PER_EPOCH
    _MAX_STEPS_PER_EPOCH = max_steps_per_epoch

def max_steps_per_epoch():
    """Get the maximum number of steps for any call to fit/evaluate/predict.

    Retrieves the limit on the number of epochs set by
    `keras.config.set_max_steps_per_epoch` or the `KERAS_MAX_STEPS_PER_EPOCH`
    environment variable.

    Args:
        max_epochs: The integer limit on the number of epochs or `None`. If
            `None`, no limit is applied.
    """
    return _MAX_STEPS_PER_EPOCH

def get_data_adapter(
    x,
    y=None,
    sample_weight=None,
    batch_size=None,
    steps_per_epoch=None,
    shuffle=False,
    class_weight=None,
):
    # Allow passing a custom data adapter.
    if isinstance(x, data_adapter.DataAdapter):
        return x
    # ... truncated

    def __init__(
        self,
        x,
        y=None,
        sample_weight=None,
        batch_size=None,
        steps_per_epoch=None,
        shuffle=False,
        class_weight=None,
        steps_per_execution=1,
    ):
        # Possibly cap steps_per_epoch for debugging runs.
        max_steps_per_epoch = config.max_steps_per_epoch()
        if max_steps_per_epoch:
            if not steps_per_epoch or max_steps_per_epoch < steps_per_epoch:
                warnings.warn(
                    "Limiting steps_per_epoch to %d" % max_steps_per_epoch
                )
                steps_per_epoch = max_steps_per_epoch
        self.steps_per_epoch = steps_per_epoch
        self.steps_per_execution = steps_per_execution
        self._current_iterator = None
        self._epoch_iterator = None
        self._steps_seen = 0
        self.data_adapter = data_adapters.get_data_adapter(
            x=x,
            y=y,
            sample_weight=sample_weight,
            batch_size=batch_size,
            steps_per_epoch=steps_per_epoch,
            shuffle=shuffle,
            class_weight=class_weight,
        )
        self._num_batches = self.data_adapter.num_batches

    def sequences_to_texts(self, sequences):
        return list(self.sequences_to_texts_generator(sequences))

    def _enumerate_iterator(self):
        self.data_adapter.on_epoch_begin()
        steps_per_epoch = self.steps_per_epoch or self._num_batches or -1

        if steps_per_epoch > 0:
            if self._current_iterator is None or self.steps_per_epoch is None:
                self._current_iterator = iter(self._get_iterator())
                self._steps_seen = 0
            for step in range(0, steps_per_epoch, self.steps_per_execution):
                if self._num_batches and self._steps_seen >= self._num_batches:
                    if self.steps_per_epoch:
                        self._interrupted_warning()
                    break
                self._steps_seen += self.steps_per_execution
                yield (
                    step,
                    step + self.steps_per_execution - 1,
                    self._current_iterator,
                )
            if self._num_batches and self._steps_seen >= self._num_batches:
                self._current_iterator = iter(self._get_iterator())
                self._steps_seen = 0
        else:
            iterator = iter(self._get_iterator())
            step = -self.steps_per_execution
            while True:
                step += self.steps_per_execution
                self._steps_seen = step + self.steps_per_execution
                yield step, step + self.steps_per_execution - 1, iterator
        self.data_adapter.on_epoch_end()

    def texts_to_sequences(self, texts):
        return list(self.texts_to_sequences_generator(texts))

    def sequences_to_texts_generator(self, sequences):
        num_words = self.num_words
        oov_token_index = self.word_index.get(self.oov_token)
        for seq in sequences:
            vect = []
            for num in seq:
                word = self.index_word.get(num)
                if word is not None:
                    if num_words and num >= num_words:
                        if oov_token_index is not None:
                            vect.append(self.index_word[oov_token_index])
                    else:
                        vect.append(word)
                elif self.oov_token is not None:
                    vect.append(self.index_word[oov_token_index])
            vect = " ".join(vect)
            yield vect

    def _log_epoch_metrics(self, epoch, logs):
        """Writes epoch metrics out as scalar summaries.

        Args:
            epoch: Int. The global step to use for TensorBoard.
            logs: Dict. Keys are scalar summary names, values are scalars.
        """
        if not logs:
            return

        train_logs = {k: v for k, v in logs.items() if not k.startswith("val_")}
        val_logs = {k: v for k, v in logs.items() if k.startswith("val_")}
        train_logs = self._collect_learning_rate(train_logs)
        if self.write_steps_per_second:
            train_logs["steps_per_second"] = self._compute_steps_per_second()

        if train_logs:
            with self._train_writer.as_default():
                for name, value in train_logs.items():
                    self.summary.scalar(f"epoch_{name}", value, step=epoch)
        if val_logs:
            with self._val_writer.as_default():
                for name, value in val_logs.items():
                    name = name[4:]  # Remove 'val_' prefix.
                    self.summary.scalar(f"epoch_{name}", value, step=epoch)

    def fit_on_sequences(self, sequences):
        self.document_count += len(sequences)
        for seq in sequences:
            seq = set(seq)
            for i in seq:
                self.index_docs[i] += 1

    def _compute_steps_per_second(self):
        current_iteration = self.model.optimizer.iterations
        time_since_epoch_begin = time.time() - self._epoch_start_time
        current_iteration = ops.convert_to_tensor(current_iteration, "float32")
        time_since_epoch_begin = ops.convert_to_tensor(
            time_since_epoch_begin, "float32"
        )

        steps_per_second = (
            current_iteration - self._previous_epoch_iterations
        ) / time_since_epoch_begin
        return float(steps_per_second)

    def predict(
        self, x, batch_size=None, verbose="auto", steps=None, callbacks=None
    ):
        # Create an iterator that yields batches of input data.
        epoch_iterator = JAXEpochIterator(
            x=x,
            batch_size=batch_size,
            steps_per_epoch=steps,
            shuffle=False,
            steps_per_execution=self.steps_per_execution,
        )

    # ... truncated

    def sequences_to_matrix(self, sequences, mode="binary"):
        if not self.num_words:
            if self.word_index:
                num_words = len(self.word_index) + 1
            else:
                raise ValueError(
                    "Specify a dimension (`num_words` argument), "
                    "or fit on some text data first."
                )
        else:
            num_words = self.num_words

    # ... truncated

    def predict(
        self, x, batch_size=None, verbose="auto", steps=None, callbacks=None
    ):
        # Create an iterator that yields batches of input data.
        epoch_iterator = TorchEpochIterator(
            x=x,
            batch_size=batch_size,
            steps_per_epoch=steps,
            shuffle=False,
            steps_per_execution=self.steps_per_execution,
        )

    # ... truncated

    def predict(
        self, x, batch_size=None, verbose="auto", steps=None, callbacks=None
    ):
        # Create an iterator that yields batches of input data.
        epoch_iterator = TFEpochIterator(
            x=x,
            batch_size=batch_size,
            steps_per_epoch=steps,
            shuffle=False,
            distribute_strategy=self.distribute_strategy,
            steps_per_execution=self.steps_per_execution,
        )
    # ... truncated

    def predict(
        self, x, batch_size=None, verbose="auto", steps=None, callbacks=None
    ):
        # Create an iterator that yields batches of input data.
        epoch_iterator = EpochIterator(
            x=x,
            batch_size=batch_size,
            steps_per_epoch=steps,
            shuffle=False,
            steps_per_execution=self.steps_per_execution,
        )

    # ... truncated

    def predict(
        self, x, batch_size=None, verbose="auto", steps=None, callbacks=None
    ):
        # Create an iterator that yields batches of input data.
        epoch_iterator = EpochIterator(
            x=x,
            batch_size=batch_size,
            steps_per_epoch=steps,
            shuffle=False,
            steps_per_execution=self.steps_per_execution,
        )

    # ... truncated

    def texts_to_sequences_generator(self, texts):
        num_words = self.num_words
        oov_token_index = self.word_index.get(self.oov_token)
        for text in texts:
            if self.char_level or isinstance(text, list):
                if self.lower:
                    if isinstance(text, list):
                        text = [text_elem.lower() for text_elem in text]
                    else:
                        text = text.lower()
                seq = text
            else:
                if self.analyzer is None:
                    seq = text_to_word_sequence(
                        text,
                        filters=self.filters,
                        lower=self.lower,
                        split=self.split,
                    )
                else:
                    seq = self.analyzer(text)
            vect = []
            for w in seq:
                i = self.word_index.get(w)
                if i is not None:
                    if num_words and i >= num_words:
                        if oov_token_index is not None:
                            vect.append(oov_token_index)
                    else:
                        vect.append(i)
                elif self.oov_token is not None:
                    vect.append(oov_token_index)
            yield vect

    def on_epoch_begin(self, epoch, logs=None):
        # Keeps track of epoch for profiling.
        if self.write_steps_per_second:
            self._previous_epoch_iterations = ops.convert_to_tensor(
                self.model.optimizer.iterations, "float32"
            )
            self._epoch_start_time = time.time()

    def num_batches(self):
        if self.steps_per_epoch:
            return self.steps_per_epoch
        # Either copied from the data_adapter, or
        # inferred at the end of an iteration.
        return self._num_batches

    def texts_to_matrix(self, texts, mode="binary"):
        sequences = self.texts_to_sequences(texts)
        return self.sequences_to_matrix(sequences, mode=mode)

    def output(self):
        """Retrieves the output tensor(s) of a layer.

        Only returns the tensor(s) corresponding to the *first time*
        the operation was called.

        Returns:
            Output tensor or list of output tensors.
        """
        return self._get_node_attribute_at_index(0, "output_tensors", "output")

    def output(self):
        return self._outputs_struct

def floatx():
    """Return the default float type, as a string.

    E.g. `'bfloat16'`, `'float16'`, `'float32'`, `'float64'`.

    Returns:
        String, the current default float type.

    Example:

    >>> keras.config.floatx()
    'float32'

    """
    return _FLOATX

def custom_fn(x):
    return x**2
```
