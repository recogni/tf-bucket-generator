import Queue
import tensorflow as tf
from recogni_proto import v0_packet_pb2 as packet
from tf_packet_generator import CameraPacketGenerator


def _parse_camera_packet(msg):
    """ msg is the serialized version of a proto.CameraPacket.
    """
    p = packet.CameraPacket()
    try:
        p.ParseFromString(msg)
    except Exception as e:
        print "Exception parsing CameraPacket:", e
    return p.single.cam.data, p.single.meta[0].classId


def main():
    gen     = CameraPacketGenerator("gs://berend-test/tmp/*.pb")
    dataset = tf.data.Dataset.from_generator(gen.generator, output_types=(tf.string))
    dataset = dataset.map(lambda msg : tf.py_func(_parse_camera_packet, [msg], Tout=[tf.string, tf.int64]))
    dataset = dataset.batch(3)
    dataset = dataset.repeat()
    iter    = dataset.make_one_shot_iterator()
    img, id = iter.get_next()
    op      = tf.Print(id, [id], "ClassId=")

    # Run the session.
    with tf.Session() as sess:
        sess.run(op)
        sess.run(op)
        sess.run(op)


if __name__ == "__main__":
    main()
