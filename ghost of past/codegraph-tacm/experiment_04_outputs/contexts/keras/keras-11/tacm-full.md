# keras-11 :: tacm-full

query: Improve type-check for Sequence (#11468)

## selected nodes

- rank=1 layer=FUNCTION tokens=217 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/torch/rnn.py::_has_fully_masked_sequence file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/torch/rnn.py
- rank=2 layer=FUNCTION tokens=234 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/rnn.py::_has_fully_masked_sequence file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/rnn.py
- rank=3 layer=FUNCTION tokens=950 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/math.py::stft file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/math.py
- rank=4 layer=FUNCTION tokens=602 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/math.py::stft file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/math.py
- rank=5 layer=FUNCTION tokens=603 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/math.py::stft file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/math.py
- rank=6 layer=FUNCTION tokens=643 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/torch/math.py::stft file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/torch/math.py
- rank=7 layer=FUNCTION tokens=204 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/numpy.py::searchsorted file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/numpy.py
- rank=8 layer=FUNCTION tokens=108 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/compile_utils.py::CompileLoss.key_check_fn file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/compile_utils.py
- rank=9 layer=FUNCTION tokens=182 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/numpy.py::searchsorted file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/numpy.py
- rank=10 layer=FUNCTION tokens=211 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/audio_dataset_utils_test.py::AudioDatasetFromDirectoryTest._get_audio_samples file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/audio_dataset_utils_test.py
- rank=11 layer=FUNCTION tokens=46 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/core.py::shape file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/core.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/torch/rnn.py::_has_fully_masked_sequence [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/torch/rnn.py]
def _has_fully_masked_sequence(mask):
    """Check if input sequence contains any fully masked data.

    cuDNN kernel will error out if the input sequence contains any fully masked
    data. We work around this issue by rerouting the computation to the
    standard kernel until the issue on the cuDNN side has been fixed. For a
    fully masked sequence, it will contain all `False` values. To make it easy
    to check, we invert the boolean and check if any of the sequences has all
    `True` values.

    Args:
        mask: The mask tensor.

    Returns:
        A boolean tensor, `True` if the mask contains a fully masked sequence.
    """
    return torch.any(torch.all(~mask, dim=1))

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/rnn.py::_has_fully_masked_sequence [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/rnn.py]
def _has_fully_masked_sequence(mask):
    """Check if input sequence contains any fully masked data.

    cuDNN kernel will error out if the input sequence contains any fully masked
    data. We work around this issue by rerouting the computation to the
    standard kernel until the issue on the cuDNN side has been fixed. For a
    fully masked sequence, it will contain all `False` values. To make it easy
    to check, we invert the boolean and check if any of the sequences has all
    `True` values.

    Args:
        mask: The mask tensor.

    Returns:
        A boolean tensor, `True` if the mask contains a fully masked sequence.
    """
    return tf.reduce_any(
        tf.reduce_all(tf.logical_not(tf.cast(mask, dtype="bool")), axis=1)
    )

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/math.py::stft [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/math.py]
def stft(
    x, sequence_length, sequence_stride, fft_length, window="hann", center=True
):
    if standardize_dtype(x.dtype) not in {"float32", "float64"}:
        raise TypeError(
            "Invalid input type. Expected `float32` or `float64`. "
            f"Received: input type={x.dtype}"
        )
    if fft_length < sequence_length:
        raise ValueError(
            "`fft_length` must equal or larger than `sequence_length`. "
            f"Received: sequence_length={sequence_length}, "
            f"fft_length={fft_length}"
        )
    if isinstance(window, str):
        if window not in {"hann", "hamming"}:
            raise ValueError(
                "If a string is passed to `window`, it must be one of "
                f'`"hann"`, `"hamming"`. Received: window={window}'
            )

    ori_dtype = x.dtype
    x = get_ov_output(x)

    ori_shape = x.shape
    num_dims = len(ori_shape)

    if num_dims > 2:
        flatten_shape = ov_opset.constant([-1, ori_shape[-1]], Type.i32).output(
            0
        )
        x = ov_opset.reshape(x, flatten_shape, False).output(0)

    if center:
        # pad x with reflect mode
        pad_begin = [0] * len(x.shape)
        pad_end = [0] * len(x.shape)
        pad_begin[-1] = fft_length // 2
        pad_end[-1] = fft_length // 2
        pad_begin_node = ov_opset.constant(pad_begin, Type.i32).output(0)
        pad_end_node = ov_opset.constant(pad_end, Type.i32).output(0)
        x = ov_opset.pad(x, pad_begin_node, pad_end_node, "reflect").output(0)

    l_pad = (fft_length - sequence_length) // 2
    r_pad = fft_length - sequence_length - l_pad

    element_type = x.get_element_type()
    if element_type == Type.f64:
        x = ov_opset.convert(x, Type.f32).output(0)
        element_type = Type.f32

    if window is not None:
        if isinstance(window, str):
            win = scipy.signal.get_window(window, sequence_length)
        else:
            win = window
        if len(win.shape) != 1 or win.shape[-1] != sequence_length:
            raise ValueError(
                "The shape of `window` must be equal to [sequence_length]."
                f"Received: window shape={win.shape}"
            )
        win = np.pad(win, [[l_pad, r_pad]])
        win_node = ov_opset.constant(win, element_type).output(0)
    else:
        win = np.ones((sequence_length + l_pad + r_pad))
        win_node = ov_opset.constant(win, element_type).output(0)

    frame_size_node = ov_opset.constant(fft_length, Type.i32).output(0)
    frame_step_node = ov_opset.constant(sequence_stride, Type.i32).output(0)

    stft_node = ov_opset.stft(
        x, win_node, frame_size_node, frame_step_node, transpose_frames=False
    ).output(0)

    out_real = ov_opset.gather(
        stft_node,
        ov_opset.constant(0, Type.i32),
        ov_opset.constant(-1, Type.i32),
    ).output(0)
    out_imag = ov_opset.gather(
        stft_node,
        ov_opset.constant(1, Type.i32),
        ov_opset.constant(-1, Type.i32),
    ).output(0)

    if num_dims > 2:
        target_shape = list(ori_shape[:-1]) + [-1, fft_length // 2 + 1]
        target_shape_node = ov_opset.constant(target_shape, Type.i32).output(0)
        out_real = ov_opset.reshape(out_real, target_shape_node, False).output(
            0
        )
        out_imag = ov_opset.reshape(out_imag, target_shape_node, False).output(
            0
        )

    if ori_dtype == "float64":
        out_real = ov_opset.convert(out_real, Type.f64).output(0)
        out_imag = ov_opset.convert(out_imag, Type.f64).output(0)

    return OpenVINOKerasTensor(out_real), OpenVINOKerasTensor(out_imag)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/math.py::stft [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/math.py]
def stft(
    x, sequence_length, sequence_stride, fft_length, window="hann", center=True
):
    if standardize_dtype(x.dtype) not in {"float32", "float64"}:
        raise TypeError(
            "Invalid input type. Expected `float32` or `float64`. "
            f"Received: input type={x.dtype}"
        )
    if fft_length < sequence_length:
        raise ValueError(
            "`fft_length` must equal or larger than `sequence_length`. "
            f"Received: sequence_length={sequence_length}, "
            f"fft_length={fft_length}"
        )
    if isinstance(window, str):
        if window not in {"hann", "hamming"}:
            raise ValueError(
                "If a string is passed to `window`, it must be one of "
                f'`"hann"`, `"hamming"`. Received: window={window}'
            )
    x = convert_to_tensor(x)

    if center:
        pad_width = [(0, 0) for _ in range(len(x.shape))]
        pad_width[-1] = (fft_length // 2, fft_length // 2)
        x = jnp.pad(x, pad_width, mode="reflect")

    l_pad = (fft_length - sequence_length) // 2
    r_pad = fft_length - sequence_length - l_pad

    if window is not None:
        if isinstance(window, str):
            win = convert_to_tensor(
                scipy.signal.get_window(window, sequence_length), dtype=x.dtype
            )
        else:
            win = convert_to_tensor(window, dtype=x.dtype)
        if len(win.shape) != 1 or win.shape[-1] != sequence_length:
            raise ValueError(
                "The shape of `window` must be equal to [sequence_length]."
                f"Received: window shape={win.shape}"
            )
        win = jnp.pad(win, [[l_pad, r_pad]])
    else:
        win = jnp.ones((sequence_length + l_pad + r_pad), dtype=x.dtype)

    result = jax.scipy.signal.stft(
        x,
        fs=1.0,
        window=win,
        nperseg=(sequence_length + l_pad + r_pad),
        noverlap=(sequence_length + l_pad + r_pad - sequence_stride),
        nfft=fft_length,
        boundary=None,
        padded=False,
    )[-1]
    # scale and swap to (..., num_sequences, fft_bins)
    scale = jnp.sqrt(1.0 / win.sum() ** 2)
    result = result / scale
    result = jnp.swapaxes(result, -2, -1)
    return jnp.real(result), jnp.imag(result)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/math.py::stft [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/math.py]
def stft(
    x, sequence_length, sequence_stride, fft_length, window="hann", center=True
):
    if standardize_dtype(x.dtype) not in {"float32", "float64"}:
        raise TypeError(
            "Invalid input type. Expected `float32` or `float64`. "
            f"Received: input type={x.dtype}"
        )
    if fft_length < sequence_length:
        raise ValueError(
            "`fft_length` must equal or larger than `sequence_length`. "
            f"Received: sequence_length={sequence_length}, "
            f"fft_length={fft_length}"
        )
    if isinstance(window, str):
        if window not in {"hann", "hamming"}:
            raise ValueError(
                "If a string is passed to `window`, it must be one of "
                f'`"hann"`, `"hamming"`. Received: window={window}'
            )
    x = convert_to_tensor(x)
    ori_dtype = x.dtype

    if center:
        pad_width = [(0, 0) for _ in range(len(x.shape))]
        pad_width[-1] = (fft_length // 2, fft_length // 2)
        x = np.pad(x, pad_width, mode="reflect")

    l_pad = (fft_length - sequence_length) // 2
    r_pad = fft_length - sequence_length - l_pad

    if window is not None:
        if isinstance(window, str):
            win = convert_to_tensor(
                scipy.signal.get_window(window, sequence_length), dtype=x.dtype
            )
        else:
            win = convert_to_tensor(window, dtype=x.dtype)
        if len(win.shape) != 1 or win.shape[-1] != sequence_length:
            raise ValueError(
                "The shape of `window` must be equal to [sequence_length]."
                f"Received: window shape={win.shape}"
            )
        win = np.pad(win, [[l_pad, r_pad]])
    else:
        win = np.ones((sequence_length + l_pad + r_pad), dtype=x.dtype)

    x = scipy.signal.stft(
        x,
        fs=1.0,
        window=win,
        nperseg=(sequence_length + l_pad + r_pad),
        noverlap=(sequence_length + l_pad + r_pad - sequence_stride),
        nfft=fft_length,
        boundary=None,
        padded=False,
    )[-1]

    # scale and swap to (..., num_sequences, fft_bins)
    x = x / np.sqrt(1.0 / win.sum() ** 2)
    x = np.swapaxes(x, -2, -1)
    return np.real(x).astype(ori_dtype), np.imag(x).astype(ori_dtype)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/torch/math.py::stft [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/torch/math.py]
def stft(
    x, sequence_length, sequence_stride, fft_length, window="hann", center=True
):
    if standardize_dtype(x.dtype) not in {"float32", "float64"}:
        raise TypeError(
            "Invalid input type. Expected `float32` or `float64`. "
            f"Received: input type={x.dtype}"
        )
    if fft_length < sequence_length:
        raise ValueError(
            "`fft_length` must equal or larger than `sequence_length`. "
            f"Received: sequence_length={sequence_length}, "
            f"fft_length={fft_length}"
        )
    if isinstance(window, str):
        if window not in {"hann", "hamming"}:
            raise ValueError(
                "If a string is passed to `window`, it must be one of "
                f'`"hann"`, `"hamming"`. Received: window={window}'
            )
    x = convert_to_tensor(x)

    if window is not None:
        if isinstance(window, str):
            if window == "hann":
                win = torch.hann_window(
                    sequence_length,
                    periodic=True,
                    dtype=x.dtype,
                    device=get_device(),
                )
            else:
                win = torch.hamming_window(
                    sequence_length,
                    periodic=True,
                    dtype=x.dtype,
                    device=get_device(),
                )
        else:
            win = convert_to_tensor(window, dtype=x.dtype)
        if len(win.shape) != 1 or win.shape[-1] != sequence_length:
            raise ValueError(
                "The shape of `window` must be equal to [sequence_length]."
                f"Received: window shape={win.shape}"
            )
    else:
        win = torch.ones((sequence_length,), dtype=x.dtype, device=get_device())

    need_unpack = False
    *batch_shape, samples = x.shape
    if len(x.shape) > 2:
        need_unpack = True
        flat_batchsize = math.prod(batch_shape)
        x = torch.reshape(x, (flat_batchsize, samples))

    x = torch.stft(
        x,
        n_fft=fft_length,
        hop_length=sequence_stride,
        win_length=sequence_length,
        window=win,
        center=center,
        return_complex=True,
    )
    if need_unpack:
        fft_unique_bins, num_sequences = x.shape[-2:]
        x = torch.reshape(x, (*batch_shape, fft_unique_bins, num_sequences))

    x = torch.swapaxes(x, -2, -1)
    return x.real, x.imag

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/numpy.py::searchsorted [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/numpy.py]
def searchsorted(sorted_sequence, values, side="left"):
    if ndim(sorted_sequence) != 1:
        raise ValueError(
            "`searchsorted` only supports 1-D sorted sequences. "
            "You can use `keras.ops.vectorized_map` "
            "to extend it to N-D sequences. Received: "
            f"sorted_sequence.shape={sorted_sequence.shape}"
        )
    sequence_len = sorted_sequence.shape[0]
    out_type = (
        "int32"
        if sequence_len is not None and sequence_len <= np.iinfo(np.int32).max
        else "int64"
    )
    return tf.searchsorted(
        sorted_sequence, values, side=side, out_type=out_type
    )

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/compile_utils.py::CompileLoss.key_check_fn [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/compile_utils.py]
            def key_check_fn(key, objs):
                return all(
                    [
                        issubclass(type(obj), (list, tuple)) and key < len(obj)
                        for obj in objs
                    ]
                )

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/numpy.py::searchsorted [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/numpy.py]
def searchsorted(sorted_sequence, values, side="left"):
    if ndim(sorted_sequence) != 1:
        raise ValueError(
            "`searchsorted` only supports 1-D sorted sequences. "
            "You can use `keras.ops.vectorized_map` "
            "to extend it to N-D sequences. Received: "
            f"sorted_sequence.shape={sorted_sequence.shape}"
        )
    out_type = (
        "int32"
        if sorted_sequence.shape[0] <= np.iinfo(np.int32).max
        else "int64"
    )
    return np.searchsorted(sorted_sequence, values, side=side).astype(out_type)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/audio_dataset_utils_test.py::AudioDatasetFromDirectoryTest._get_audio_samples [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/audio_dataset_utils_test.py]
    def _get_audio_samples(self, count=16, different_sequence_lengths=False):
        sequence_length = 30
        num_channels = 1
        audio_samples = []
        for _ in range(count):
            if different_sequence_lengths:
                random_sequence_length = np.random.randint(
                    10, sequence_length + 1
                )
                audio = np.random.random((random_sequence_length, num_channels))
            else:
                audio = np.random.random((sequence_length, num_channels))
            audio_samples.append(tf.audio.encode_wav(audio, 1000))
        return audio_samples

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/core.py::shape [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/core.py]
def shape(x):
    return x.shape
```
