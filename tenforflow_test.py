import tensorflow as tf

names = ["a", "b", "c"]

inputs_dict = dict()
for name in names:
    inputs_dict[name] = tf.placeholder(dtype=tf.int32,
                                       shape=[None],
                                       name=name
                                       )

inputs = []
for k, v in inputs_dict.items():
    inputs.append(v)
outputs = tf.reduce_sum(inputs)

names_dict = {
    "a": [1, 2, 3],
    "b": [1, 2, 3],
    "c": [1, 2, 3]
}

feed_dict = {
    inputs_dict["a"]: names_dict["a"],
    inputs_dict["b"]: names_dict["b"],
}
feed_dict[inputs_dict["c"]] = names_dict["c"]

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    outputs = sess.run(outputs, feed_dict=feed_dict)
    print(outputs)
