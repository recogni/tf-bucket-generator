import Queue
import tensorflow as tf
from tf_bucket_generator import GsBucketGenerator

def main():
    gen     = GsBucketGenerator("gs://berend-test/run1/*.pb")
    dataset = tf.data.Dataset.from_generator(gen.generator, output_types=(tf.string))
    dataset = dataset.batch(2)
    iter    = dataset.make_one_shot_iterator()
    packet  = iter.get_next()
    op      = tf.Print(packet, [packet], "Packet=")

    # Run the session.
    with tf.Session() as sess:
        sess.run(op)
        sess.run(op)

if __name__ == "__main__":
    main()
