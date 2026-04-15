# keras-42 :: tacm-full

query: Allow custom steps_per_epoch for sequences, default to len(generator) if unspecified (#8509)

## selected nodes

- rank=1 layer=FUNCTION tokens=343 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/epoch_iterator.py::EpochIterator.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/epoch_iterator.py
- rank=2 layer=FUNCTION tokens=1546 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/data_adapters/__init__.py::get_data_adapter file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/data_adapters/__init__.py
- rank=3 layer=FUNCTION tokens=197 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/config.py::set_max_steps_per_epoch file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/config.py
- rank=4 layer=FUNCTION tokens=404 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/epoch_iterator.py::EpochIterator._enumerate_iterator file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/epoch_iterator.py
- rank=5 layer=FUNCTION tokens=148 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/config.py::max_steps_per_epoch file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/config.py
- rank=6 layer=FUNCTION tokens=323 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/callbacks/tensorboard.py::TensorBoard._log_epoch_metrics file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/callbacks/tensorboard.py
- rank=7 layer=FUNCTION tokens=966 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/trainer.py::JAXTrainer.predict file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/trainer.py
- rank=8 layer=FUNCTION tokens=55 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/functional.py::Functional.output file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/functional.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/epoch_iterator.py::EpochIterator.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/epoch_iterator.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/data_adapters/__init__.py::get_data_adapter [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/data_adapters/__init__.py]
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

    # Check for multi-process/worker distribution.
    distribution = distribution_lib.distribution()
    if (
        distribution is not None
        and getattr(distribution, "_is_multi_process", False)
        and getattr(distribution, "auto_shard_dataset", False)
        and not is_tf_dataset(x)
    ):
        raise ValueError(
            "When using a multi-worker distribution with auto-sharding enabled, "
            "the data must be provided as a `tf.data.Dataset` instance. "
            f"Received: type(x)={type(x)}. "
            "If the dataset is already sharded across workers, then set "
            "`distribution.auto_shard_dataset = False`."
        )

    if array_data_adapter.can_convert_arrays((x, y, sample_weight)):
        return ArrayDataAdapter(
            x,
            y,
            sample_weight=sample_weight,
            class_weight=class_weight,
            shuffle=shuffle,
            batch_size=batch_size,
            steps=steps_per_epoch,
        )
    elif is_tf_dataset(x):
        # Unsupported args: y, sample_weight, shuffle
        if y is not None:
            raise_unsupported_arg("y", "the targets", "tf.data.Dataset")
        if sample_weight is not None:
            raise_unsupported_arg(
                "sample_weights", "the sample weights", "tf.data.Dataset"
            )
        return TFDatasetAdapter(
            x, class_weight=class_weight, distribution=distribution
        )
        # TODO: should we warn or not?
        # warnings.warn(
        #     "`shuffle=True` was passed, but will be ignored since the "
        #     "data `x` was provided as a tf.data.Dataset. The Dataset is "
        #     "expected to already be shuffled "
        #     "(via `.shuffle(tf.data.AUTOTUNE)`)"
        # )
    elif isinstance(x, py_dataset_adapter.PyDataset):
        if y is not None:
            raise_unsupported_arg("y", "the targets", "PyDataset")
        if sample_weight is not None:
            raise_unsupported_arg(
                "sample_weights", "the sample weights", "PyDataset"
            )
        return PyDatasetAdapter(x, class_weight=class_weight, shuffle=shuffle)
        # TODO: should we warn or not?
        # if x.num_batches is None and shuffle:
        #     warnings.warn(
        #         "`shuffle=True` was passed, but will be ignored since the "
        #         "data `x` was provided as a infinite PyDataset. The "
        #         "PyDataset is expected to already be shuffled."
        # )
    elif is_torch_dataloader(x):
        if y is not None:
            raise_unsupported_arg("y", "the targets", "torch DataLoader")
        if sample_weight is not None:
            raise_unsupported_arg(
                "sample_weights", "the sample weights", "torch DataLoader"
            )
        if class_weight is not None:
            raise ValueError(
                "Argument `class_weight` is not supported for torch "
                f"DataLoader inputs. You can modify your `__getitem__ ` method"
                " to return input tensor, label and class_weight. "
                "Alternatively, use a custom training loop. See the User Guide "
                "https://keras.io/guides/custom_train_step_in_torch/"
                "#supporting-sampleweight-amp-classweight for more details. "
                f"Received: class_weight={class_weight}"
            )
        return TorchDataLoaderAdapter(x)
        # TODO: should we warn or not?
        # warnings.warn(
        #     "`shuffle=True` was passed, but will be ignored since the "
        #     "data `x` was provided as a torch DataLoader. The DataLoader "
        #     "is expected to already be shuffled."
        # )
    elif is_grain_dataset(x):
        if y is not None:
            raise_unsupported_arg(
                "y", "the targets", "grain.Dataset and grain.DataLoader"
            )
        if sample_weight is not None:
            raise_unsupported_arg(
                "sample_weights",
                "the sample weights",
                "grain.Dataset and grain.DataLoader",
            )
        if class_weight is not None:
            raise ValueError(
                "Argument `class_weight` is not supported for grain.Dataset "
                f"and grain.DataLoader inputs. You can modify your "
                "`__getitem__ ` method to return input tensor, label and "
                "class_weight. "
                f"Received: class_weight={class_weight}"
            )
        return GrainDatasetAdapter(x)
        # TODO: should we warn or not?
        # warnings.warn(
        #     "`shuffle=True` was passed, but will be ignored since the "
        #     "data `x` was provided as a grain dataset. The grain dataset "
        #     "is expected to already be shuffled."
        # )
    elif isinstance(x, types.GeneratorType):
        if y is not None:
            raise_unsupported_arg("y", "the targets", "PyDataset")
        if sample_weight is not None:
            raise_unsupported_arg(
                "sample_weights", "the sample weights", "PyDataset"
            )
        if class_weight is not None:
            raise ValueError(
                "Argument `class_weight` is not supported for Python "
                f"generator inputs. Received: class_weight={class_weight}"
            )
        return GeneratorDataAdapter(x)
        # TODO: should we warn or not?
        # warnings.warn(
        #     "`shuffle=True` was passed, but will be ignored since the "
        #     "data `x` was provided as a generator. The generator "
        #     "is expected to yield already-shuffled data."
        # )
    else:
        raise ValueError(f"Unrecognized data type: x={x} (of type {type(x)})")

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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/callbacks/tensorboard.py::TensorBoard._log_epoch_metrics [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/callbacks/tensorboard.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/trainer.py::JAXTrainer.predict [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/trainer.py]
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

        if not all(layer.built for layer in self._flatten_layers()):
            # Build the model on one batch of data.
            for _, _, iterator in epoch_iterator:
                # Build model
                x, _, _ = data_adapter_utils.unpack_x_y_sample_weight(
                    next(iterator)
                )
                if is_nnx_enabled():
                    self(x)
                else:
                    with backend.StatelessScope():
                        self(x)
                break
            epoch_iterator.reset()
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

        self.make_predict_function()
        self.stop_predicting = False
        callbacks.on_predict_begin()

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

        self._jax_state_synced = True
        outputs = None
        non_trainable_variables = None
        with epoch_iterator.catch_stop_iteration():
            for begin_step, end_step, iterator in epoch_iterator:
                callbacks.on_predict_batch_begin(begin_step)
                if self._jax_state_synced:
                    # The state may have been synced by a callback.
                    state = self._get_jax_state(
                        trainable_variables=True,
                        non_trainable_variables=True,
                        purge_model_variables=True,
                    )
                    self._jax_state_synced = False
                batch_outputs, state = self.predict_function(state, iterator)
                (
                    trainable_variables,
                    non_trainable_variables,
                ) = state
                self._jax_state = {
                    "trainable_variables": trainable_variables,
                    # I wouldn't recommend modifying non-trainable model state
                    # during predict(), but it's allowed.
                    "non_trainable_variables": non_trainable_variables,
                }
                outputs = append_to_outputs(batch_outputs, outputs)

                # Dispatch callbacks. This takes care of async dispatch.
                callbacks.on_predict_batch_end(
                    end_step, {"outputs": batch_outputs}
                )

                if self.stop_predicting:
                    break

        self.jax_state_sync()
        callbacks.on_predict_end()
        self._jax_state = None
        return tree.map_structure_up_to(batch_outputs, np.concatenate, outputs)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/functional.py::Functional.output [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/functional.py]
    def output(self):
        return self._outputs_struct
```
