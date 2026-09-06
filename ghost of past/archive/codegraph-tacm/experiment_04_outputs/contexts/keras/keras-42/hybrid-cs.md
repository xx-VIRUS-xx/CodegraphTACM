# keras-42 :: hybrid-cs

query: Allow custom steps_per_epoch for sequences, default to len(generator) if unspecified (#8509)

## selected nodes

- rank=1 layer=FUNCTION tokens=197 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/config.py::set_max_steps_per_epoch file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/config.py
- rank=2 layer=FUNCTION tokens=404 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/epoch_iterator.py::EpochIterator._enumerate_iterator file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/epoch_iterator.py
- rank=3 layer=FUNCTION tokens=148 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/config.py::max_steps_per_epoch file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/config.py
- rank=4 layer=FUNCTION tokens=180 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/callbacks/tensorboard.py::TensorBoard._compute_steps_per_second file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/callbacks/tensorboard.py
- rank=5 layer=FUNCTION tokens=126 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/callbacks/tensorboard.py::TensorBoard.on_epoch_begin file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/callbacks/tensorboard.py
- rank=6 layer=FUNCTION tokens=151 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/epoch_iterator.py::EpochIterator.__next__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/epoch_iterator.py
- rank=7 layer=FUNCTION tokens=544 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/trainer.py::OpenVINOTrainer.predict file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/trainer.py
- rank=8 layer=FUNCTION tokens=528 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/trainer.py::NumpyTrainer.predict file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/trainer.py
- rank=9 layer=FUNCTION tokens=95 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/callbacks/backup_and_restore_test.py::InterruptingCallback.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/callbacks/backup_and_restore_test.py
- rank=10 layer=FUNCTION tokens=811 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/trainer.py::TensorFlowTrainer.predict file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/trainer.py
- rank=11 layer=FUNCTION tokens=103 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/epoch_iterator.py::EpochIterator.num_batches file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/epoch_iterator.py
- rank=12 layer=FUNCTION tokens=567 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/torch/trainer.py::TorchTrainer.predict file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/torch/trainer.py
- rank=13 layer=FUNCTION tokens=78 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/epoch_iterator.py::EpochIterator.enumerate_epoch file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/epoch_iterator.py
- rank=14 layer=FUNCTION tokens=68 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/epoch_iterator_test.py::TestPyDataset.on_epoch_begin file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/epoch_iterator_test.py

## context

```text
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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/callbacks/tensorboard.py::TensorBoard.on_epoch_begin [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/callbacks/tensorboard.py]
    def on_epoch_begin(self, epoch, logs=None):
        # Keeps track of epoch for profiling.
        if self.write_steps_per_second:
            self._previous_epoch_iterations = ops.convert_to_tensor(
                self.model.optimizer.iterations, "float32"
            )
            self._epoch_start_time = time.time()

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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/trainer.py::OpenVINOTrainer.predict [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/trainer.py]
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

        # Container that configures and calls callbacks.
        if not isinstance(callbacks, callbacks_module.CallbackList):
            callbacks = callbacks_module.CallbackList(
                callbacks,
                add_history=True,
                add_progbar=verbose != 0,
                verbose=verbose,
                epochs=1,
                steps=epoch_iterator.num_batches,
                model=self,
            )

        def append_to_outputs(batch_outputs, outputs):
            if outputs is None:
                outputs = tree.map_structure(
                    lambda batch_output: [batch_output],
                    batch_outputs,
                )
            else:
                tree.map_structure_up_to(
                    batch_outputs,
                    lambda output, batch_output: output.append(batch_output),
                    outputs,
                    batch_outputs,
                )
            return outputs

        self.make_predict_function()
        self.stop_predicting = False
        callbacks.on_predict_begin()
        outputs = None
        for begin_step, end_step, data in epoch_iterator.enumerate_epoch():
            callbacks.on_predict_batch_begin(begin_step)
            batch_outputs = self.predict_function(data)
            outputs = append_to_outputs(batch_outputs, outputs)
            callbacks.on_predict_batch_end(end_step, {"outputs": batch_outputs})
            if self.stop_predicting:
                break
        callbacks.on_predict_end()
        return tree.map_structure_up_to(batch_outputs, np.concatenate, outputs)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/trainer.py::NumpyTrainer.predict [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/trainer.py]
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

        # Container that configures and calls callbacks.
        if not isinstance(callbacks, callbacks_module.CallbackList):
            callbacks = callbacks_module.CallbackList(
                callbacks,
                add_progbar=verbose != 0,
                verbose=verbose,
                epochs=1,
                steps=epoch_iterator.num_batches,
                model=self,
            )

        def append_to_outputs(batch_outputs, outputs):
            if outputs is None:
                outputs = tree.map_structure(
                    lambda batch_output: [batch_output],
                    batch_outputs,
                )
            else:
                tree.map_structure_up_to(
                    batch_outputs,
                    lambda output, batch_output: output.append(batch_output),
                    outputs,
                    batch_outputs,
                )
            return outputs

        self.make_predict_function()
        self.stop_predicting = False
        callbacks.on_predict_begin()
        outputs = None
        for begin_step, end_step, data in epoch_iterator:
            callbacks.on_predict_batch_begin(begin_step)
            batch_outputs = self.predict_function(data)
            outputs = append_to_outputs(batch_outputs, outputs)
            callbacks.on_predict_batch_end(end_step, {"outputs": batch_outputs})
            if self.stop_predicting:
                break
        callbacks.on_predict_end()
        return tree.map_structure_up_to(batch_outputs, np.concatenate, outputs)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/callbacks/backup_and_restore_test.py::InterruptingCallback.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/callbacks/backup_and_restore_test.py]
    def __init__(self, steps_int, epoch_int):
        self.batch_count = 0
        self.epoch_count = 0
        self.steps_int = steps_int
        self.epoch_int = epoch_int

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/trainer.py::TensorFlowTrainer.predict [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/trainer.py]
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

        # Container that configures and calls callbacks.
        if not isinstance(callbacks, callbacks_module.CallbackList):
            callbacks = callbacks_module.CallbackList(
                callbacks,
                add_progbar=verbose != 0,
                verbose=verbose,
                epochs=1,
                steps=epoch_iterator.num_batches,
                model=self,
            )

        def append_to_outputs(batch_outputs, outputs):
            if outputs is None:
                outputs = tree.map_structure(
                    lambda batch_output: [batch_output],
                    batch_outputs,
                )
            else:
                tree.map_structure_up_to(
                    batch_outputs,
                    lambda output, batch_output: output.append(batch_output),
                    outputs,
                    batch_outputs,
                )
            return outputs

        def get_data(iterator):
            """Returns data for the next execution."""
            data = []
            for _ in range(self.steps_per_execution):
                try:
                    single_step_data = next(iterator)
                except (StopIteration, tf.errors.OutOfRangeError) as e:
                    if hasattr(data, "__len__") and len(data) > 0:
                        # Suppress the error when still have remaining data.
                        return data
                    else:
                        # Re-raise the error for
                        # EpochIterator.catch_stop_iteration() to catch when
                        # no data left.
                        raise e
                data.append(single_step_data)
            return data

        self.make_predict_function()
        self.stop_predicting = False
        callbacks.on_predict_begin()
        outputs = None
        with epoch_iterator.catch_stop_iteration():
            for begin_step, end_step, iterator in epoch_iterator:
                callbacks.on_predict_batch_begin(begin_step)
                data = get_data(iterator)
                batch_outputs = self.predict_function(data)
                outputs = append_to_outputs(batch_outputs, outputs)
                callbacks.on_predict_batch_end(
                    end_step, {"outputs": batch_outputs}
                )
                if self.stop_predicting:
                    break
        callbacks.on_predict_end()
        outputs = tree.map_structure_up_to(
            batch_outputs, potentially_ragged_concat, outputs
        )
        return tree.map_structure(convert_to_np_if_not_ragged, outputs)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/epoch_iterator.py::EpochIterator.num_batches [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/epoch_iterator.py]
    def num_batches(self):
        if self.steps_per_epoch:
            return self.steps_per_epoch
        # Either copied from the data_adapter, or
        # inferred at the end of an iteration.
        return self._num_batches

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/torch/trainer.py::TorchTrainer.predict [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/torch/trainer.py]
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

        # Container that configures and calls callbacks.
        if not isinstance(callbacks, callbacks_module.CallbackList):
            callbacks = callbacks_module.CallbackList(
                callbacks,
                add_progbar=verbose != 0,
                verbose=verbose,
                epochs=1,
                steps=epoch_iterator.num_batches,
                model=self,
            )

        def append_to_outputs(batch_outputs, outputs):
            if outputs is None:
                outputs = tree.map_structure(
                    lambda batch_output: [batch_output],
                    batch_outputs,
                )
            else:
                tree.map_structure_up_to(
                    batch_outputs,
                    lambda output, batch_output: output.append(batch_output),
                    outputs,
                    batch_outputs,
                )
            return outputs

        # Switch the torch Module back to testing mode.
        self.eval()

        self.make_predict_function()
        self.stop_predicting = False
        callbacks.on_predict_begin()
        outputs = None
        for begin_step, end_step, data in epoch_iterator:
            callbacks.on_predict_batch_begin(begin_step)
            batch_outputs = self.predict_function(data)
            outputs = append_to_outputs(batch_outputs, outputs)
            callbacks.on_predict_batch_end(end_step, {"outputs": batch_outputs})
            if self.stop_predicting:
                break
        callbacks.on_predict_end()
        outputs = tree.map_structure(backend.convert_to_numpy, outputs)
        return tree.map_structure_up_to(batch_outputs, np.concatenate, outputs)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/epoch_iterator.py::EpochIterator.enumerate_epoch [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/epoch_iterator.py]
    def enumerate_epoch(self):
        for begin_step, end_step, data in self:
            yield begin_step, end_step, data

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/epoch_iterator_test.py::TestPyDataset.on_epoch_begin [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/epoch_iterator_test.py]
            def on_epoch_begin(self):
                self.tracker.append(1)
```
