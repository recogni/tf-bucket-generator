"""
Tensor generator that yields images and labels for the image.

Accepts HTTP POSTs which will enqueue data to the process queue.
"""
import time
from tensorflow.python.lib.io import file_io
from recogni_proto import v0_packet_pb2 as packet

class CameraPacketGenerator():
    """ Generator class to wrap the recogni specific camera packet
        generator.

    """
    patterns = None

    def __init__(self, *patterns):
        """ Custom gs bucket generator.
        """
        self.patterns = []
        for pattern in patterns:
            self.patterns.append(pattern)


    def generator(self):
        """ generator function for the dataset.  This will yield a single
            recogni v0_packet_pb2.CameraPacket at a time.
        """
        bundle = packet.Bundle()
        for pattern in self.patterns:
            print "Using pattern: ", pattern
            files = file_io.get_matching_files(pattern)
            for file in files:
                print "... file ", file
                with file_io.FileIO(file, "rb") as fin:
                    bs = fin.read()
                    try:
                        bundle.Clear()
                        bundle.ParseFromString(bs)
                        for pkt in bundle.packets:
                            yield pkt.SerializeToString()
                    except:
                        continue
