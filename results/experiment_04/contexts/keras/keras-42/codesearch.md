# keras-42 :: codesearch

query: Allow custom steps_per_epoch for sequences, default to len(generator) if unspecified (#8509)

## selected nodes

- rank=1 layer=FUNCTION tokens=78 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/epoch_iterator.py::EpochIterator.enumerate_epoch file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/epoch_iterator.py
- rank=2 layer=FUNCTION tokens=404 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/epoch_iterator.py::EpochIterator._enumerate_iterator file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/epoch_iterator.py
- rank=3 layer=FUNCTION tokens=197 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/config.py::set_max_steps_per_epoch file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/config.py
- rank=4 layer=FUNCTION tokens=863 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/trainer.py::TensorFlowTrainer.multi_step_on_iterator file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/trainer.py
- rank=5 layer=FUNCTION tokens=148 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/config.py::max_steps_per_epoch file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/config.py
- rank=6 layer=FUNCTION tokens=151 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/epoch_iterator.py::EpochIterator.__next__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/epoch_iterator.py
- rank=7 layer=FUNCTION tokens=132 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/nn.py::_step file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/nn.py
- rank=8 layer=FUNCTION tokens=180 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/callbacks/tensorboard.py::TensorBoard._compute_steps_per_second file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/callbacks/tensorboard.py
- rank=9 layer=FUNCTION tokens=96 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/nn.py::_step file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/nn.py
- rank=10 layer=FUNCTION tokens=70 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/trainer.py::JAXTrainer.iterator_step file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/trainer.py
- rank=11 layer=FUNCTION tokens=82 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/trainer_test.py::TracingCounterModel.train_step file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/trainer_test.py
- rank=12 layer=FUNCTION tokens=95 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/callbacks/backup_and_restore_test.py::InterruptingCallback.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/callbacks/backup_and_restore_test.py
- rank=13 layer=FUNCTION tokens=84 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/trainer_test.py::TracingCounterModel.predict_step file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/trainer_test.py
- rank=14 layer=FUNCTION tokens=111 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/trainer.py::TensorFlowTrainer.cond file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/trainer.py
- rank=15 layer=FUNCTION tokens=166 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/math.py::extract_sequences file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/math.py
- rank=16 layer=FUNCTION tokens=68 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/epoch_iterator_test.py::TestPyDataset.on_epoch_begin file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/epoch_iterator_test.py
- rank=17 layer=FUNCTION tokens=87 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/lstm.py::LSTM.call file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/lstm.py
- rank=18 layer=FUNCTION tokens=86 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/gru.py::GRU.call file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/gru.py
- rank=19 layer=FUNCTION tokens=91 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/simple_rnn.py::SimpleRNN.call file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/simple_rnn.py
- rank=20 layer=FUNCTION tokens=126 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/callbacks/tensorboard.py::TensorBoard.on_epoch_begin file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/callbacks/tensorboard.py
- rank=21 layer=FUNCTION tokens=91 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/conv_lstm.py::ConvLSTM.call file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/conv_lstm.py
- rank=22 layer=FUNCTION tokens=399 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/backend.py::_step file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/backend.py
- rank=23 layer=FUNCTION tokens=63 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/trainer.py::TFEpochIterator.__next__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/trainer.py
- rank=24 layer=FUNCTION tokens=60 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/trainer.py::JAXEpochIterator.__next__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/trainer.py
- rank=25 layer=FUNCTION tokens=68 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/loss_scale_optimizer.py::LossScaleOptimizer.increment file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/loss_scale_optimizer.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/epoch_iterator.py::EpochIterator.enumerate_epoch [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/epoch_iterator.py]
    def enumerate_epoch(self):
        for begin_step, end_step, data in self:
            yield begin_step, end_step, data

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/epoch_iterator.py::EpochIterator._enumerate_iterator [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/epoch_iterator.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/config.py::set_max_steps_per_epoch [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/config.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/trainer.py::TensorFlowTrainer.multi_step_on_iterator [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/trainer.py]
        def multi_step_on_iterator(iterator):
            if self.steps_per_execution == 1:
                return tf.experimental.Optional.from_value(
                    one_step_on_data(iterator.get_next())
                )

            # the spec is set lazily during the tracing of `tf.while_loop`
            empty_outputs = tf.experimental.Optional.empty(None)

            def cond(execution_step, optional_outputs, next_optional_inputs):
                return tf.logical_and(
                    tf.less(execution_step, self.steps_per_execution),
                    next_optional_inputs.has_value(),
                )

            def inner_body(
                execution_step, optional_outputs, next_optional_inputs
            ):
                def has_next():
                    next_optional_outputs = tf.experimental.Optional.from_value(
                        one_step_on_data(next_optional_inputs.get_value())
                    )
                    empty_outputs._element_spec = (
                        next_optional_outputs.element_spec
                    )
                    return next_optional_outputs

                def no_has_next():
                    optional_outputs._element_spec = empty_outputs._element_spec
                    return optional_outputs

                next_optional_outputs = tf.cond(
                    tf.logical_and(
                        tf.less(execution_step, self.steps_per_execution),
                        next_optional_inputs.has_value(),
                    ),
                    has_next,
                    no_has_next,
                )

                return (
                    execution_step + 1,
                    next_optional_outputs,
                    # We don't want to iterate if we have reached
                    # `steps_per_execution` steps
                    tf.cond(
                        tf.less(execution_step + 1, self.steps_per_execution),
                        lambda: iterator.get_next_as_optional(),
                        lambda: next_optional_inputs,
                    ),
                )

            def body(execution_step, optional_outputs, next_optional_inputs):
                for _ in range(
                    min(
                        self.unrolled_steps_per_execution,
                        self.steps_per_execution,
                    )
                ):
                    execution_step, optional_outputs, next_optional_inputs = (
                        inner_body(
                            execution_step,
                            optional_outputs,
                            next_optional_inputs,
                        )
                    )

                return (execution_step, optional_outputs, next_optional_inputs)

            execution_step = tf.constant(0)
            next_optional_inputs = iterator.get_next_as_optional()

            # Run the while loop
            _, final_optional_outputs, _ = tf.while_loop(
                cond,
                body,
                loop_vars=[execution_step, empty_outputs, next_optional_inputs],
            )
            final_optional_outputs._element_spec = empty_outputs.element_spec
            return final_optional_outputs

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/config.py::max_steps_per_epoch [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/config.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/epoch_iterator.py::EpochIterator.__next__ [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/epoch_iterator.py]
    def __next__(self):
        buffer = []
        begin_step, end_step, iterator = next(self._epoch_iterator)
        with self.catch_stop_iteration():
            for _ in range(self.steps_per_execution):
                data = next(iterator)
                buffer.append(data)
            return begin_step, end_step, buffer
        if buffer:
            return begin_step, end_step, buffer
        raise StopIteration

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/nn.py::_step [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/nn.py]
    def _step(prev, x):
        paths, scores, masked = prev
        x, seqlen_mask = x

        paths, scores, masked = lax.cond(
            seqlen_mask,
            lambda paths, scores, masked, x: (paths, scores, masked),
            _decode_step,
            paths,
            scores,
            masked,
            x,
        )

        return (paths, scores, masked), None

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/callbacks/tensorboard.py::TensorBoard._compute_steps_per_second [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/callbacks/tensorboard.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/nn.py::_step [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/nn.py]
    def _step(prev, x):
        paths, scores, masked = prev
        x, seqlen_mask = x
        if not seqlen_mask:
            paths, scores, masked = _decode_step(paths, scores, masked, x)
        return (paths, scores, masked), None

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/trainer.py::JAXTrainer.iterator_step [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/trainer.py]
            def iterator_step(state, iterator):
                return step_function(state, next(iterator))

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/trainer_test.py::TracingCounterModel.train_step [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/trainer_test.py]
            def train_step(self, *args):
                tracing_count[0] = tracing_count[0] + 1
                return super().train_step(*args)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/callbacks/backup_and_restore_test.py::InterruptingCallback.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/callbacks/backup_and_restore_test.py]
    def __init__(self, steps_int, epoch_int):
        self.batch_count = 0
        self.epoch_count = 0
        self.steps_int = steps_int
        self.epoch_int = epoch_int

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/trainer_test.py::TracingCounterModel.predict_step [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/trainer_test.py]
            def predict_step(self, *args):
                tracing_count[0] = tracing_count[0] + 1
                return super().predict_step(*args)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/trainer.py::TensorFlowTrainer.cond [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/trainer.py]
            def cond(execution_step, optional_outputs, next_optional_inputs):
                return tf.logical_and(
                    tf.less(execution_step, self.steps_per_execution),
                    next_optional_inputs.has_value(),
                )

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/math.py::extract_sequences [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/math.py]
def extract_sequences(x, sequence_length, sequence_stride):
    *batch_shape, _ = x.shape
    batch_shape = list(batch_shape)
    shape = x.shape[:-1] + (
        (x.shape[-1] - (sequence_length - sequence_stride)) // sequence_stride,
        sequence_length,
    )
    strides = x.strides[:-1] + (
        sequence_stride * x.strides[-1],
        x.strides[-1],
    )
    x = np.lib.stride_tricks.as_strided(x, shape=shape, strides=strides)
    return np.reshape(x, (*batch_shape, *x.shape[-2:]))

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/epoch_iterator_test.py::TestPyDataset.on_epoch_begin [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/epoch_iterator_test.py]
            def on_epoch_begin(self):
                self.tracker.append(1)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/lstm.py::LSTM.call [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/lstm.py]
    def call(self, sequences, initial_state=None, mask=None, training=False):
        return super().call(
            sequences, mask=mask, training=training, initial_state=initial_state
        )

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/gru.py::GRU.call [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/gru.py]
    def call(self, sequences, initial_state=None, mask=None, training=False):
        return super().call(
            sequences, mask=mask, training=training, initial_state=initial_state
        )

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/simple_rnn.py::SimpleRNN.call [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/simple_rnn.py]
    def call(self, sequences, initial_state=None, mask=None, training=False):
        return super().call(
            sequences, mask=mask, training=training, initial_state=initial_state
        )

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/callbacks/tensorboard.py::TensorBoard.on_epoch_begin [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/callbacks/tensorboard.py]
    def on_epoch_begin(self, epoch, logs=None):
        # Keeps track of epoch for profiling.
        if self.write_steps_per_second:
            self._previous_epoch_iterations = ops.convert_to_tensor(
                self.model.optimizer.iterations, "float32"
            )
            self._epoch_start_time = time.time()

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/conv_lstm.py::ConvLSTM.call [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/conv_lstm.py]
    def call(self, sequences, initial_state=None, mask=None, training=False):
        return super().call(
            sequences, initial_state=initial_state, mask=mask, training=training
        )

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/backend.py::_step [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/backend.py]
            def _step(time, output_ta_t, *states):
                """RNN step function.

                Args:
                    time: Current timestep value.
                    output_ta_t: TensorArray.
                    *states: List of states.

                Returns:
                    Tuple: `(time + 1,output_ta_t) + tuple(new_states)`
                """
                current_input = tuple(ta.read(time) for ta in input_ta)
                current_input = tf.nest.pack_sequence_as(inputs, current_input)
                output, new_states = step_function(
                    current_input, tuple(states) + tuple(constants)
                )
                flat_state = tf.nest.flatten(states)
                flat_new_state = tf.nest.flatten(new_states)
                for state, new_state in zip(flat_state, flat_new_state):
                    if isinstance(new_state, tf.Tensor):
                        new_state.set_shape(state.shape)

                flat_output = tf.nest.flatten(output)
                ta_index_to_write = time if return_all_outputs else 0
                output_ta_t = tuple(
                    ta.write(ta_index_to_write, out)
                    for ta, out in zip(output_ta_t, flat_output)
                )

                new_states = tf.nest.pack_sequence_as(
                    initial_states, flat_new_state
                )
                return (time + 1, output_ta_t) + tuple(new_states)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/trainer.py::TFEpochIterator.__next__ [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/trainer.py]
    def __next__(self):
        return next(self._epoch_iterator)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/trainer.py::JAXEpochIterator.__next__ [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/trainer.py]
    def __next__(self):
        return next(self._epoch_iterator)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/loss_scale_optimizer.py::LossScaleOptimizer.increment [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/loss_scale_optimizer.py]
        def increment():
            self.step_counter.assign_add(1)
```
