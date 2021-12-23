"""Xiaomi aqara E1 contact sensor device."""

from zigpy.profiles import zha
from zigpy.zcl.clusters.general import Identify, Ota

from zhaquirks.const import (
    DEVICE_TYPE,
    ENDPOINTS,
    INPUT_CLUSTERS,
    MODELS_INFO,
    OUTPUT_CLUSTERS,
    PROFILE_ID,
)
from zhaquirks.xiaomi import BasicCluster, XiaomiAqaraE1Cluster, XiaomiCustomDevice

XIAOMI_CLUSTER_ID = 0xFCC0


class Lunar(XiaomiCustomDevice):
    """Xiaomi Aqara sleep sensor device."""

    signature = {
        #  <SimpleDescriptor endpoint=1 profile=260 device_type=0xfff0
        #  device_version=1
        #  input_clusters=[0, 3, 64704]
        #  output_clusters=[3, 19]>
        MODELS_INFO: [("aqara", "lumi.lunar.acn01")],
        ENDPOINTS: {
            1: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: 0xFFF0,
                INPUT_CLUSTERS: [
                    BasicCluster.cluster_id,
                    Identify.cluster_id,
                    XIAOMI_CLUSTER_ID,
                ],
                OUTPUT_CLUSTERS: [Identify.cluster_id, Ota.cluster_id],
            }
        },
    }
    replacement = {
        ENDPOINTS: {
            1: {
                INPUT_CLUSTERS: [
                    BasicCluster,
                    Identify.cluster_id,
                    XiaomiAqaraE1Cluster,
                ],
                OUTPUT_CLUSTERS: [Identify.cluster_id, Ota.cluster_id],
            }
        },
    }
